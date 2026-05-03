from flask import Flask, render_template, request, session
import logging

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Logging setup (file + console)
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

@app.route("/")
def home():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    if not session.get("visited"):
        session["visited"] = True
        logging.info(f"NEW VISIT | IP: {ip} | Device: {user_agent}")
        print(f"NEW VISIT | IP: {ip}")
    else:
        logging.info(f"RETURN VISIT | IP: {ip}")

    return render_template("index.html")


@app.route("/log", methods=["POST"])
def log_action():
    data = request.json
    action = data.get("action")

    ip = request.remote_addr
    logging.info(f"ACTION | {action} | IP: {ip}")
    print(f"ACTION | {action}")

    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)