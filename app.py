from flask import Flask
app= Flask(__name__)

@app.route("/")
def home():
    return "Hello CI pipeline by anni Roy the Best Developer!"

if __name__ == "__main__":
    app.run(debug=True)
    
