# mlapp
This is an API that predicts the handwritten digit in the image provided, this prediction is done by the TensorFlow model created by me and trained on mnist data. The source code for this model can be found in the repository.

This repository contains kubernetes manifests for deploying MYSQL and FastApi applications on kubernetes cluster, along with the source code.

## Prerequisites
Before deploying to the kubernetes cluster, ensure you have the following requirements installed on your local system.
- [minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/) installed and configured to access the cluster
- docker

## API Endpoints

### `/`

- **Method:** GET
- **Description:** The root endpoint that provides information about the API.

### `/prediction`

- **Method:** POST
- **Description:** Endpoint for predicting handwritten digits using an image URL.
- **Request:**
  - **Content Type:** JSON
  - **Example Request:**
    ```json
    {
      "image_url": "https://example.com/image.jpg"
    }
    ```
- **Response:**
  - **Content Type:** JSON
  - **Example:**
    ```json
    {
      "prediction": 7
    }
    ```



## Deployment Instructions

Follow these steps to deploy the MYSQL and FastAPI applications on your Kubernetes cluster:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Bhargav-Dasari/mlapp.git
   cd mlapp
2. **Deploy FastApi and MYSQL:**
   Apply the MYSQL and FastApi deployment and services manifests using the following command in terminal
   ```bash
   kubectl apply -f fastapi-deployment.yaml
3. **Access The API:**
   After deploying verify that the services and up and running
   ```bash
   kubectl get services
   kubectl get pods
   ```
   if the services are running, get the Nodeport value using
   ```bash
   kubectl get svc fastapi-service
   ```
   To access FastApi using browser run the cammand using minikube
   ```bash
   minikube service fastapi-service
   ```
   A Browser tab will be opened on defauld browser where you can access the api

## Swagger UI

The API is documented using Swagger UI, which provides an interactive way to explore and test the endpoints.

To access Swagger UI:

1. After deploying the FastAPI application, get the NodePort value for the service:

   ```bash
   minikube service fastapi-service --url
   ```
2. This will provide an url that can be used to access the service using browser
   ```
   <url from above step>/docs
   
   

   






