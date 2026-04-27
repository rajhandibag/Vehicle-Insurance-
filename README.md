
# 🚗 Vehicle Insurance MLOps Pipeline

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green?style=for-the-badge&logo=mongodb)
![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20EC2%20%7C%20ECR-orange?style=for-the-badge&logo=amazonaws)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black?style=for-the-badge&logo=githubactions)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=for-the-badge&logo=scikitlearn)

**A production-grade, end-to-end MLOps pipeline for vehicle insurance risk prediction — built with real-world engineering standards including automated data pipelines, cloud-native deployment, and full CI/CD automation.**

[📊 View Pipeline](#️-architecture--workflow) · [⚙️ Setup Guide](#️-project-setup) · [☁️ Deployment](#️-cloud--deployment) · [🔄 CI/CD](#-cicd-pipeline)

</div>

---

## 🚀 Project Overview

This project implements a **fully automated machine learning pipeline** for vehicle insurance data — from raw data ingestion through MongoDB Atlas to model deployment on AWS EC2, with zero-touch CI/CD via GitHub Actions.

> Built to simulate the engineering rigor of a real ML platform team — not a notebook experiment. Every component is modular, logged, versioned, and deployable.

**What it solves:** Automating the full lifecycle of an ML model — ingesting messy insurance records, validating data quality, engineering features, training models, evaluating against production baselines, and serving predictions through a live web API — all without manual intervention.

---

## 🔥 Key Features

- **📥 Automated Data Ingestion** — Pulls data directly from MongoDB Atlas into a structured pipeline with schema-aware validation
- **✅ Data Validation Layer** — Detects schema drift, missing columns, and distributional anomalies before training begins
- **⚙️ Feature Engineering Pipeline** — Preprocessing and transformation steps encapsulated as reusable Scikit-learn pipeline objects
- **🤖 Model Training & Selection** — Configurable training workflow with serialized model artifacts
- **📈 Model Evaluation with Baseline Gating** — New models only promote to production if they outperform the current S3-hosted champion by a defined threshold
- **☁️ Model Registry on AWS S3** — Versioned model storage decoupled from deployment infrastructure
- **🐳 Dockerized Application** — Fully containerized Flask app for consistent, portable deployments
- **🔄 End-to-End CI/CD** — Push to `main` → GitHub Actions → Docker build → ECR push → EC2 deploy, fully automated
- **📋 Custom Logging & Exception Handling** — Structured logging and traceable exceptions across all pipeline stages
- **🌐 Prediction API + Web UI** — REST endpoint and browser interface for real-time insurance predictions

---

## 🏗️ Architecture / Workflow

```
                        ┌─────────────────────────────────────────────┐
                        │              TRAINING PIPELINE               │
                        └─────────────────────────────────────────────┘
                                            │
        ┌───────────────┐                   │
        │  MongoDB Atlas│──── Fetch Data ───▼
        └───────────────┘                   │
                                   ┌───────────────────┐
                                   │  Data Ingestion   │  → Raw train/test split
                                   └────────┬──────────┘
                                            │
                                   ┌────────▼──────────┐
                                   │  Data Validation  │  → Schema & drift checks
                                   └────────┬──────────┘
                                            │
                                   ┌────────▼──────────┐
                                   │ Data Transformation│  → Feature engineering
                                   └────────┬──────────┘
                                            │
                                   ┌────────▼──────────┐
                                   │   Model Trainer   │  → Train & serialize model
                                   └────────┬──────────┘
                                            │
                                   ┌────────▼──────────┐
                                   │  Model Evaluation │  → Compare vs. S3 champion
                                   └────────┬──────────┘
                                            │
                                   ┌────────▼──────────┐
                                   │   Model Pusher    │  → Push to AWS S3 registry
                                   └───────────────────┘

                        ┌─────────────────────────────────────────────┐
                        │             PREDICTION PIPELINE             │
                        └─────────────────────────────────────────────┘
                                User Request → Flask App → Pull Model from S3 → Predict → Return Result
                
                        ┌─────────────────────────────────────────────┐
                        │               CI/CD PIPELINE                │
                        └─────────────────────────────────────────────┘
                                Git Push → GitHub Actions → Docker Build → Push to ECR → Deploy on EC2
```

Each pipeline stage produces a typed **Artifact** object — making the entire workflow auditable, debuggable, and resumable.

---

## 📊 Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.10 |
| **ML & Data** | Scikit-learn, Pandas, NumPy |
| **Database** | MongoDB Atlas |
| **Cloud Storage** | AWS S3 (model registry) |
| **Deployment** | AWS EC2 + AWS ECR |
| **Containerization** | Docker |
| **CI/CD** | GitHub Actions |
| **Web Framework** | Flask |
| **Package Management** | Conda + pip |
| **Config & Schema** | YAML |

---

## ⚙️ Project Setup

### Prerequisites

- Python 3.10
- Conda
- MongoDB Atlas account
- AWS account with S3, EC2, and ECR access

### 1. Clone the Repository

```bash
git clone https://github.com/rajhandibag/vehicle-insurance-mlops.git
cd vehicle-insurance-mlops
```

### 2. Create and Activate Environment

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

**MongoDB Connection:**
```bash
# Bash
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/"

# PowerShell
$env:MONGODB_URL = "mongodb+srv://<username>:<password>@cluster.mongodb.net/"
```

**AWS Credentials:**
```bash
# Bash
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"

# PowerShell
$env:AWS_ACCESS_KEY_ID = "your-access-key"
$env:AWS_SECRET_ACCESS_KEY = "your-secret-key"
```

### 5. Run the Training Pipeline

```bash
python demo.py
```

### 6. Launch the Web Application

```bash
python app.py
```

App will be available at `http://localhost:5000`

---

## ☁️ Cloud & Deployment

### AWS Infrastructure

| Service | Purpose |
|---|---|
| **S3** | Versioned model registry (`my-model-mlopsproj` bucket) |
| **ECR** | Docker image repository for the Flask app |
| **EC2** (Ubuntu 24.04, T2 Medium) | Production server hosting the deployed application |
| **IAM** | Least-privilege access roles for pipeline operations |

### Docker

The application is fully containerized. Build and run locally:

```bash
docker build -t vehicle-insurance-app .
docker run -p 5080:5080 vehicle-insurance-app
```

In production, the image is built by GitHub Actions, pushed to ECR, and pulled by EC2 automatically on every deployment.

---

## 🔄 CI/CD Pipeline

Every push to the `main` branch triggers a fully automated deployment workflow:

```
Code Push to main
      │
      ▼
GitHub Actions Triggered
      │
      ├── 1. Lint & Validate
      ├── 2. Docker Image Build
      ├── 3. Push to AWS ECR
      └── 4. SSH Deploy to EC2
                  │
                  └── Pull latest image → Restart container → App live
```

**GitHub Secrets Required:**

| Secret | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | IAM user access key |
| `AWS_SECRET_ACCESS_KEY` | IAM user secret key |
| `AWS_DEFAULT_REGION` | Target region (us-east-1) |
| `ECR_REPO` | ECR repository URI |

The EC2 instance runs as a **self-hosted GitHub Actions runner**, enabling direct deployment without external orchestration tools.

---

## 🌐 Application Demo

The deployed application exposes two entry points:

- **`/`** — Web UI for submitting insurance data and receiving predictions
- **`/training`** — Trigger a fresh model training run via browser or API call

> 🔗 **Live App:** `http://54.87.12.125:8080`

---

## 📈 What This Project Demonstrates

This project was built to reflect the kind of ML engineering expected in a real data science or MLOps role:

- **Pipeline Modularity** — Each component (ingestion, validation, transformation, training, evaluation, deployment) is independently testable and replaceable
- **Config-Driven Architecture** — Constants, schema definitions, and thresholds are centralized — no hardcoded values scattered across scripts
- **Artifact-Based State Management** — Each pipeline stage produces typed artifact objects, enabling traceability and stage-level restarts
- **Production-Grade Logging** — Structured logs with source file, line number, and stage context across the full pipeline
- **Model Gating Logic** — A new model only replaces the production model if it clears a configurable performance threshold — exactly how model promotion works in industry
- **Cloud-Native Storage** — Model artifacts are decoupled from application code and versioned in S3
- **Zero-Touch Deployment** — A single `git push` rebuilds, packages, and deploys the entire application stack

---

## 💡 Why This Project Stands Out

Most ML projects stop at a Jupyter notebook. This one doesn't.

- ✅ **No notebook spaghetti** — production Python package structure with proper imports, `setup.py`, and `pyproject.toml`
- ✅ **Real cloud integration** — not mocked, not local files — actual MongoDB Atlas + AWS S3 + EC2 + ECR
- ✅ **CI/CD that actually works** — tested, end-to-end automated deployment pipeline
- ✅ **Separation of concerns** — data access, configuration, entities, components, and pipeline layers are clearly separated
- ✅ **Repeatable and scalable** — swap the dataset, update the schema YAML, retrain — the pipeline handles the rest

This is the kind of project that bridges the gap between "I can train a model" and "I can ship a model."

---

## 📁 Project Structure

```
vehicle-insurance-mlops/
├── src/
│   ├── components/          # Pipeline stage implementations
│   ├── configuration/       # MongoDB & AWS connection configs
│   ├── constants/           # Centralized constants
│   ├── data_access/         # MongoDB data fetch layer
│   ├── entity/              # Config & artifact dataclasses
│   ├── pipeline/            # Training & prediction orchestration
│   └── utils/               # Shared utilities
├── config/
│   └── schema.yaml          # Dataset schema for validation
├── notebook/                # EDA & feature engineering exploration
├── static/                  # Frontend assets
├── templates/               # HTML templates
├── .github/workflows/       # GitHub Actions CI/CD config
├── Dockerfile
├── app.py                   # Flask application entry point
├── demo.py                  # Pipeline test runner
└── requirements.txt
```

---



> *Open to MLOps, Data Engineering, and ML Platform roles. Feel free to reach out!*

---

<div align="center">

✨ Thanks for checking out my project!  
🚀 Built as part of my hands-on experience in Machine Learning and deployment pipelines  
💡 Always open to feedback and improvements  
⭐ Feel free to star the repo if you found it useful!

</div>

