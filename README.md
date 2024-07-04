# my-app

## Description
This is a simple Flask application with a `/version` endpoint.

## Setup

### Prerequisites
- Docker
- Kubernetes
- Terraform
- AWS CLI
- GitHub Actions

### Steps
1. Clone the repository
2. Build and run the Docker container
   ```sh
   docker build -t my-app .
   docker run -p 5000:5000 my-app
   ```
3. Deploy to Kubernetes
   ```sh
   kubectl apply -f kubernetes/deployment.yaml
   kubectl apply -f kubernetes/service.yaml
   ```
4. Provision Kubernetes cluster using Terraform
   ```sh
   cd terraform
   terraform init
   terraform apply
   ```

## CI/CD
GitHub Actions is used to build, test, and deploy the application to a Kubernetes cluster.
