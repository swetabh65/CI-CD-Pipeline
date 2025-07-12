# 🧪 Flask CI/CD Pipeline using Jenkins

This project demonstrates a **Jenkins CI/CD pipeline** for a simple Python Flask web application. The pipeline automates build, test, and deployment stages using Jenkins and is hosted on an AWS EC2 instance.

---

## 🚀 Project Structure

CI-CD-Pipeline/
├── app.py # Flask application
├── test_app.py # Unit test using Pytest
├── requirements.txt # Project dependencies
└── Jenkinsfile # Jenkins declarative pipeline script


---

## 🛠️ Technologies Used

- **Flask** – Lightweight Python web framework
- **Pytest** – Testing framework
- **Jenkins** – CI/CD automation server
- **Git** – Version control
- **AWS EC2** – Hosting Jenkins and Flask app
- **Bash** – Deployment automation

---

## 📦 Pipeline Stages (Jenkinsfile)

| Stage   | Description                                  |
|---------|----------------------------------------------|
| **Build**  | Creates Python virtual environment and installs dependencies |
| **Test**   | Runs unit tests using Pytest                |
| **Deploy** | Deploys Flask app using `nohup` if tests pass |

---

## 🔁 Pipeline Flow

1. Jenkins pulls the latest code from the GitHub repository.
2. Creates a virtual environment and installs Flask & Pytest.
3. Executes `test_app.py` via Pytest.
4. If all tests pass:
    - Runs the app using `nohup` in background.
5. Sends **email notifications** for success/failure.

<img width="1882" height="881" alt="image" src="https://github.com/user-attachments/assets/b0297f84-e8e8-4df7-8d04-a08a0fed60ad" />

---

## ✅ How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/swetabh65/CI-CD-Pipeline.git
   cd CI-CD-Pipeline

<img width="1389" height="322" alt="image" src="https://github.com/user-attachments/assets/e94a1603-041b-4e48-ac5f-0911382ae263" />

<img width="818" height="285" alt="image" src="https://github.com/user-attachments/assets/d618308b-3566-4ddf-a461-6633e6649ddc" />

