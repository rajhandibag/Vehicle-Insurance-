🚗 VEHICLE INSURANCE MLOPS PIPELINE
⚡ End-to-End Machine Learning System with Cloud, Docker & CI/CD

🌟 Project Overview

This project showcases a real-world MLOps pipeline built to handle vehicle insurance data—from ingestion to deployment.

It demonstrates how modern ML systems are designed using:

Scalable data pipelines
Cloud-based storage & deployment
Automated CI/CD workflows

👉 The goal is simple: build, automate, and deploy a production-ready ML system

🧠 What Makes This Project Stand Out

✔ End-to-End ML Lifecycle Implementation
✔ Cloud Integration (MongoDB + AWS)
✔ Automated CI/CD Pipeline
✔ Dockerized Deployment on EC2
✔ Modular & Scalable Architecture

🏗️ Project Architecture
📦 Vehicle Insurance MLOps
 ┣ 📂 src
 ┃ ┣ 📂 components
 ┃ ┣ 📂 pipeline
 ┃ ┣ 📂 entity
 ┃ ┣ 📂 configuration
 ┃ ┗ 📂 aws_storage
 ┣ 📂 notebook
 ┣ 📂 templates
 ┣ 📂 static
 ┣ 🐳 Dockerfile
 ┣ ⚙️ GitHub Actions (CI/CD)
 ┗ 🚀 app.py
 
🔄 End-to-End Workflow
⚙️ Tech Stack
👨‍💻 Machine Learning
Python 3.10
Scikit-learn
Pandas, NumPy
☁️ Cloud & Storage
MongoDB Atlas
AWS S3 (Model Registry)
AWS EC2 (Deployment Server)
AWS ECR (Container Registry)
🔄 DevOps & MLOps
Docker
GitHub Actions
Logging & Exception Handling
🚀 Key Features

🔥 Automated ML Pipeline
🔥 Schema-Based Data Validation
🔥 Feature Engineering & Transformation
🔥 Model Versioning in AWS S3
🔥 Dockerized Application
🔥 CI/CD Automation
🔥 Cloud Deployment on EC2

📊 Data Pipeline
📥 Data Ingestion
Data stored in MongoDB Atlas
Retrieved and converted into DataFrame
🔍 Data Validation
Schema validation using YAML
Data quality checks
🔄 Data Transformation
Feature engineering
Preprocessing pipeline
🤖 Model Pipeline
🧠 Model Training
Multiple ML models trained
Best model selected
📊 Model Evaluation
Threshold-based selection
Performance comparison
📤 Model Deployment
Model pushed to AWS S3
Version-controlled storage
🌐 Deployment & CI/CD
🐳 Docker
docker build -t vehicle-project .
docker run -p 8080:8080 vehicle-project
🔁 CI/CD Workflow
Code pushed to GitHub
GitHub Actions triggers pipeline
Docker image built & pushed to AWS ECR
Automatically deployed on EC2
🌍 Live Application
http://<EC2-PUBLIC-IP>:8080
🧪 Run Locally
conda create -n vehicle python=3.10 -y
conda activate vehicle

pip install -r requirements.txt

python app.py
🔐 Environment Variables
MongoDB
export MONGODB_URL="your_connection_string"
AWS
export AWS_ACCESS_KEY_ID="YOUR_KEY"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET"
🎯 Project Workflow Summary

Data Ingestion
➡ Data Validation
➡ Data Transformation
➡ Model Training
➡ Model Evaluation
➡ Model Deployment

🚀 Fully Automated via CI/CD Pipeline

🛠️ Additional Resources
setup.py & pyproject.toml → see crashcourse.txt
GitHub Secrets → secure CI/CD configuration
👨‍💻 Author

Raj Handibag
🚀 Machine Learning | MLOps 

⭐ Future Enhancements
📊 Model Monitoring
🔁 Auto Retraining Pipeline
☸️ Kubernetes Deployment
📈 Analytics Dashboard
💬 Connect

If you found this project helpful or want to collaborate, feel free to reach out!
