from flask import Flask, render_template, request
from IHA import encode  # Import your hashing function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    hash_result = ""
    input_text = ""
    if request.method == "POST":
        input_text = request.form.get("user_input", "")
        if input_text:
            hash_result = encode(input_text)  # Call your hashing function

    return render_template("index.html", input_text=input_text, hash_result=hash_result)

if __name__ == "__main__":
    app.run(debug=True)
