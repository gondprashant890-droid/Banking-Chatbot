from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").lower()

    if "hello" in message or "hi" in message:
        reply = "Hello! 👋 Welcome to Banking Chatbot. How can I help you?"

    elif "balance" in message:
        reply = "You can check your account balance using your bank's mobile app, ATM, or internet banking."

    elif "transfer" in message or "send money" in message:
        reply = "You can transfer money through your bank's mobile app or internet banking."

    elif "atm" in message or "card" in message:
        reply = "If your ATM card is lost or stolen, immediately block it using your bank's official app or customer care."

    elif "pin" in message:
        reply = "You can reset your ATM PIN through your bank's official app or ATM."

    elif "loan" in message:
        reply = "Banks offer different loans such as personal, home, education and vehicle loans."

    elif "account" in message:
        reply = "To open a bank account, you generally need valid KYC documents such as identity and address proof."

    else:
        reply = "Sorry, I don't understand. Please ask about balance, account, transfer, ATM, PIN or loans."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)