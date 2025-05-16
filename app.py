from flask import Flask, request, render_template, redirect, flash, url_for, g
import sqlite3
import joblib
import numpy as np

app = Flask(__name__, static_url_path='/static')
app.secret_key = "your_secret_key"  # Replace with your actual secret key

DATABASE = "feedback.db"

# ---------- Database Setup ----------
def get_db():
    if "db" not in g: 
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

# Create feedback table if it doesn't exist
with sqlite3.connect(DATABASE) as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        rating INTEGER NOT NULL,
        comment TEXT
    )
    """)
    conn.commit()

# ---------- Feedback Functions ----------
def fetch_feedbacks():
    db = get_db()
    return db.execute("SELECT * FROM feedback ORDER BY id DESC").fetchall()

def add_feedback(name, rating, comment):
    db = get_db()
    db.execute(
        "INSERT INTO feedback (name, rating, comment) VALUES (?, ?, ?)",
        (name, rating, comment if comment else None)
    )
    db.commit()

def delete_feedback_entry(feedback_id):
    db = get_db()
    db.execute("DELETE FROM feedback WHERE id = ?", (feedback_id,))
    db.commit()

# ---------- Load Models ----------
heart_model = joblib.load("Multiple_Disease_prediction_usingML-main/models/heart.pkl")


# Debug: Print expected input shapes
print("Heart model input shape:", heart_model.n_features_in_)

# ---------- Routes ----------
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        rating = request.form.get("rating")
        comment = request.form.get("comment")

        if not name or not rating:
            flash("Name and rating are required!", "danger")
            return redirect(url_for("home"))

        try:
            rating = int(rating)
            add_feedback(name, rating, comment)
            flash("Feedback submitted successfully!", "success")
        except ValueError:
            flash("Invalid rating. Please try again.", "danger")

        return redirect(url_for("home") + "#feedback_section")

    feedbacks = fetch_feedbacks()
    return render_template("home.html", feedbacks=feedbacks)

@app.route("/delete-feedback/<int:feedback_id>", methods=["POST"])
def delete_feedback(feedback_id):
    secret_key = request.form.get("secret_key")
    ADMIN_SECRET_KEY = "admin123"

    if secret_key != ADMIN_SECRET_KEY:
        flash("You are not authorized to delete feedback.", "danger")
        return redirect(url_for("home") + "#feedback_section")

    delete_feedback_entry(feedback_id)
    flash("Feedback deleted successfully!", "success")
    return redirect(url_for("home") + "#feedback_section")
@app.route("/heart", methods=['GET', 'POST'])
def heart():
    input_data = {}  # Initialize input_data to avoid the error
    prediction = None

    if request.method == "POST":
        try:
            input_array = np.array([[  
                float(request.form["age"]),
                float(request.form["sex"]),
                float(request.form["cp"]),
                float(request.form["trestbps"]),
                float(request.form["chol"]),
                float(request.form["fbs"]),
                float(request.form["restecg"]),
                float(request.form["thalach"]),
                float(request.form["exang"]),
                float(request.form["oldpeak"]),
                float(request.form["slope"]),
                float(request.form["ca"]),
                float(request.form["thal"]),
            ]])

            prediction = heart_model.predict(input_array)
            result = "Negative for Heart Disease" if prediction[0] == 1 else "Positive for Heart Disease"
        except ValueError:
            result = "Invalid input. Please enter valid numerical values."

        # Pass input_data and prediction to the template
        return render_template("heart.html", input_data=request.form, prediction=result)

    # Pass empty input_data for GET request
    return render_template("heart.html", input_data=input_data)




# ---------- Run App ----------
if __name__ == "__main__":
    app.run(debug=True)     