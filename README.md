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

<img width="1462" height="497" alt="image" src="https://github.com/user-attachments/assets/c5b4c833-045b-4e22-b258-deef0edfc9ba" />



<img width="593" height="390" alt="image" src="https://github.com/user-attachments/assets/c68077b2-9d5e-4804-abf0-6c7cdcc1775e" />

<img width="1131" height="361" alt="image" src="https://github.com/user-attachments/assets/c3f31637-3165-4a7c-9c0c-21c71645bf13" />

<img width="886" height="111" alt="image" src="https://github.com/user-attachments/assets/47473588-546b-489e-b335-6b7fa43bca17" />

<img width="1110" height="679" alt="image" src="https://github.com/user-attachments/assets/076d4095-a934-4365-9690-715c9f389f6f" />

<img width="947" height="279" alt="image" src="https://github.com/user-attachments/assets/553748ac-4121-4a21-b648-83fff7e9c7ca" />

<img width="569" height="97" alt="image" src="https://github.com/user-attachments/assets/8738b2c8-a2a0-4c88-bccd-0b178cfddf70" />

<img width="1395" height="364" alt="image" src="https://github.com/user-attachments/assets/05f5ad42-626e-4e24-906a-6f4e1313221f" />

<img width="593" height="112" alt="image" src="https://github.com/user-attachments/assets/2be30813-dc82-4fd0-af6e-cf25a258681c" />






