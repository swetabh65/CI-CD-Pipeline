from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from GitHub Actions CI/CD Pipeline!"

if __name__ == '__main__':
    app.run(debug=True)

