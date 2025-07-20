# CI-CD-Pipeline 🚀

This project demonstrates a **complete CI/CD pipeline** for a Python-based Flask application using **GitHub Actions**.

The pipeline includes:

- ✅ Code checkout
- ✅ Dependency installation
- ✅ Automated testing using `pytest`
- ✅ Deployment to staging and production environments
- ✅ Notification upon success/failure

---

## 📁 Project Structure

CI-CD-Pipeline/
├── app.py # Flask application entry point
├── requirements.txt # Project dependencies
├── test_app.py # Unit tests for Flask app
├── .github/
│ └── workflows/
│ └── ci-cd.yml # GitHub Actions workflow
├── README.md # This file


---

## ⚙️ Technologies Used

- **Python 3.8+**
- **Flask**
- **Pytest** (for testing)
- **GitHub Actions** (for CI/CD)
- **Virtualenv** (for local isolation)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/swetabh65/CI-CD-Pipeline.git
cd CI-CD-Pipeline


### 2. Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Run the Flask App
python app.py
The app should now be running at: http://127.0.0.1:5000/


🧪 Run Tests Locally
pytest test_app.py

<img width="1889" height="195" alt="image" src="https://github.com/user-attachments/assets/48f2d211-1058-4f72-bb7e-489b4865725e" />


🤖 GitHub Actions CI/CD Workflow
Path: .github/workflows/ci-cd.yml

🔄 Triggered On:
Every push to staging or main branches

Pull Requests targeting main


✅ Workflow Steps:

| Step                 | Description                               |
| -------------------- | ----------------------------------------- |
| Checkout             | Pull the latest code                      |
| Setup Python         | Configure Python environment              |
| Install Dependencies | `pip install -r requirements.txt`         |
| Run Tests            | Executes `pytest`                         |
| Deploy to Staging    | Runs deploy script if on `staging` branch |
| Deploy to Production | Runs deploy script if on `main` branch    |
| Notifications        | Prints deployment status                  |


✅ CI/CD Branch Strategy

| Branch    | Purpose                        |
| --------- | ------------------------------ |
| `staging` | For integration and QA testing |
| `main`    | Production-ready code only     |


Push to staging → triggers tests + deploy to staging.
Merge to main → triggers tests + deploy to production.

🔔 GitHub Action Output Example

🟢 Tests Passed: 2/2
🚀 Deploying to staging...
✅ Deployment Complete

