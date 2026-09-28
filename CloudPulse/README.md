# ☁️ CLOUDPULSE

## Containerized Cloud Monitoring & Information API

**CloudPulse** is a lightweight containerized web application built with **Python, FastAPI, Uvicorn, and Docker**. The project demonstrates how a modern Python application can be developed, packaged into a Docker image, executed inside a Docker container, tested locally, version-controlled with Git, published to GitHub, and distributed through Docker Hub.

---

## 👨‍💻 PROJECT INFORMATION

**Project Name:** CloudPulse  
**Student:** ITISHREE ACHARYA  
**Class:** CSE-2  
**College:** DRONACHARYA COLLEGE OF ENGINEERING  
**Project Type:** Containerized Microservice / Web Application  
**Primary Language:** Python  
**Framework:** FastAPI  
**Containerization:** Docker  

---

## 🎯 PROJECT OBJECTIVE

The main objective of CloudPulse is to understand the complete lifecycle of a containerized application, starting from application development and ending with application distribution.

The project demonstrates:

- Python web application development
- FastAPI API development
- Dependency management
- Docker containerization
- Docker image creation
- Docker container execution
- Port mapping
- API testing
- Git version control
- GitHub source-code hosting
- Docker Hub image distribution
- Reproducible application deployment

The complete concept can be represented as:

```text
        SOURCE CODE
             │
             ▼
       PYTHON / FASTAPI
             │
             ▼
         DOCKERFILE
             │
             ▼
       DOCKER BUILD
             │
             ▼
       DOCKER IMAGE
             │
             ▼
      DOCKER CONTAINER
             │
             ▼
       RUNNING SERVICE
             │
             ▼
        WEB BROWSER













  PROJECT LIFE CYCLE 

          ()

┌─────────────────────────┐
│    WRITE APPLICATION    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     TEST APPLICATION    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│      CREATE DOCKERFILE  │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       DOCKER BUILD      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       DOCKER IMAGE      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     DOCKER CONTAINER    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     TEST APPLICATION    │
└────────────┬────────────┘
             │
       ┌─────┴──────┐
       │            │
       ▼            ▼
    GITHUB      DOCKER HUB
       │            │
       ▼            ▼
   SOURCE CODE     IMAGE
       │            │
       ▼            ▼
    git clone    docker pull
       │            │
       ▼            ▼
 docker build    docker run
       │            │
       └─────┬──────┘
             ▼
     RUNNING APPLICATION