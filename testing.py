from flask import Flask, render_template, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1144977648532066375/6kfmreM9A2oalG5Nr8Mx8OOQZDZIceHpXhwtT93eHKskbdWl0Gy1Sn4IOrr2epCGhfFV"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    email = request.form.get("email")

    # Send Discord notification
    data = {
        "content": f"New membership application:\nUsername: {username}\nEmail: {email}"
    }
    response = requests.post(https://discord.com/api/webhooks/1144977648532066375/6kfmreM9A2oalG5Nr8Mx8OOQZDZIceHpXhwtT93eHKskbdWl0Gy1Sn4IOrr2epCGhfFV, json=data)

    if response.status_code == 204:
        return "Application submitted and Discord notification sent!"
    else:
        return "An error occurred while processing the application."

if __name__ == "__main__":
    app.run(debug=True)
