from flask import Flask, request

import MySQLdb
app = Flask(__name__)

DB_HOST = "workforceconnect-db.chywmsgq452e.us-east-2.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = "WorkforceConnect123!"
DB_NAME = "workforceconnect"

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        conn = MySQLdb.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWORD,
            db=DB_NAME
        )

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO registrations (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()
        cursor.close()
        conn.close()

        message = "Registration saved successfully!"

    return f"""
    <h1>WorkforceConnect Registration</h1>
    <form method="POST">
        <label>Name:</label><br>
        <input type="text" name="name"><br><br>

        <label>Email:</label><br>
        <input type="email" name="email"><br><br>

        <button type="submit">Submit</button>
    </form>

    <p>{message}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

