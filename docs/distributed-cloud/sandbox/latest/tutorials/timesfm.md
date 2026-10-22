---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/tutorials/timesfm/
title: Deploy TimesFM on GDC Sandbox \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:37.581381+00:00
---

# Deploy TimesFM on GDC Sandbox  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/tutorials/timesfm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Deploy TimesFM on GDC Sandbox Stay organized with collections  Save and categorize content based on your preferences. 

The Google Research [TimesFM](https://github.com/google-research/timesfm) model is a foundation model for time-series forecasting that has been pre-trained on billions of time points from many real-world datasets, so you can apply it to new forecasting datasets across many domains.

This tutorial guide shows how to deploy TimesFM on GDC Sandbox and has the following objectives.

  * Create a Docker container that runs TimesFM,
  * Deploy the container using GPUs provided by GDC Sandbox AI Optimized SKU, and
  * Invoke TimesFM functions using simple http requests.



## Before you begin

The GPUs provided by the GDC Sandbox AI Optimized SKU are included in the `org-infra` cluster. 

  * To run commands against the org infrastructure cluster, make sure that you have the kubeconfig of the `org-1-infra` cluster, as described in [Work with clusters](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/clusters#org-infra-cluster):

    * Configure and authenticate with the `gdcloud` command line, and
    * generate the kubeconfig file for the org infrastructure cluster, and assign its path to the environment variable `KUBECONFIG`.
  * Ensure the user has `sandbox-gpu-admin` role assigned for the project `sandbox-gpu-project`. By default, the role is assigned to the `platform-admin` user. You can assign the role to other users by signing in as the `platform-admin` and running the following command:
        
        kubectl --kubeconfig ${KUBECONFIG} create rolebinding ${NAME} --role=sandbox-gpu-admin \
        --user=${USER} --namespace=sandbox-gpu-project
        

  * Make sure to set up Artifact Registry repository as described in the [Using Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images) and sign in to be able to push and pull images to the artifact registry.




### Deploy TimesFM model

The deployment is orchestrated through a set of Kubernetes configuration files (YAML manifests), each defining a specific component or service.

  1. Create a flask based python script `app.py` with functions `predict` to do time-series forecasting and `timeseries` to generate a visualization based on the test data.
         
         from flask import Flask, jsonify, request
           import numpy as np
           import pandas as pd
           from sklearn.preprocessing import StandardScaler
         
           # Initialize Flask application
           app = Flask(__name__)
         
           # Sample route to display a welcome message
           @app.route('/')
           def home():
               return "Welcome to TimesFM! Use the API to interact with the app."
         
           # Example route for predictions (TimesFM might do time-series forecasting or music recommendations)
           @app.route('/predict', methods=['POST'])
           def predict():
               data = request.get_json()
         
               # Ensure the data is in the right format
               if 'features' not in data:
                   return jsonify({'error': 'No features provided'}), 400
         
               # For this example, assume 'features' is a list of numbers that need to be scaled
               features = data['features']
               features = np.array(features).reshape(1, -1)
         
               # Dummy model: Apply standard scaling (you would use an actual model here)
               scaler = StandardScaler()
               scaled_features = scaler.fit_transform(features)
         
               # You would normally load your model here (e.g., using pickle or joblib)
               # For simplicity, let's just return the scaled features as a placeholder for prediction
               result = scaled_features.tolist()
         
               return jsonify({'scaled_features': result})
         
           # Example of a route for data visualization or analysis
           @app.route('/timeseries', methods=['GET'])
           def timeseries_analysis():
               # Generate a dummy time series data (replace with actual data)
               time_series_data = pd.Series(np.random.randn(100), name="Random Data")
         
               # Example analysis: compute simple moving average
               moving_avg = time_series_data.rolling(window=10).mean()
         
               return jsonify({
                   'time_series': time_series_data.tolist(),
                   'moving_average': moving_avg.tolist()
               })
         
           # Run the app
           if __name__ == '__main__':
               app.run(debug=True, host='0.0.0.0', port=5000)
         

  2. Create a Dockerfile with `timesfm` installed invoking the app.
         
         # Use a base image with Python installed
          FROM python:3.11-slim
          # Set the working directory inside the container
          WORKDIR /app
          # Copy the requirements.txt (if any) and install dependencies
          COPY requirements.txt .
          RUN pip install --no-cache-dir numpy pandas timesfm huggingface_hub jax pytest flask scikit-learn
         
          # Copy the rest of the code into the container
          COPY . .
         
          # Expose the necessary port (default 5000 or whatever your app uses)
          EXPOSE 5000
         
          # Define the entrypoint for the container
          CMD ["python", "app.py"] # Replace with the correct entry script for TimesFM
         

  3. Build the docker image and upload it to Artifact Registry repository.
         
         docker build -t timesfm .
         docker tag timesfm "REGISTRY_REPOSITORY_URL"/timesfm:latest
         docker push "REGISTRY_REPOSITORY_URL"/timesfm:latest
         

Replace the following:

     * `REGISTRY_REPOSITORY_URL`: the repository URL.
  4. Create a secret to save the docker credentials.
         
         export SECRET="DOCKER_REGISTRY_SECRET"
         export DOCKER_TEST_CONFIG=~/.docker/config.json 
         kubectl --kubeconfig ${KUBECONFIG} create secret docker-registry ${SECRET} --from-file=.dockerconfigjson=${DOCKER_TEST_CONFIG} -n sandbox-gpu-project
         

Replace the following:

     * `DOCKER_REGISTRY_SECRET` name of the secret.
  5. Create a file `timesfm-deployment.yaml` to deploy `timesfm`.

The deployment of the `timesfm` server requests one GPU.
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: timesfm-deployment
           namespace: sandbox-gpu-project
           labels:
             app: timesfm
         spec:
           replicas: 1 # You can scale up depending on your needs
           selector:
             matchLabels:
               app: timesfm
           template:
             metadata:
               labels:
                 app: timesfm
             spec:
               containers:
               - name: timesfm
                 image: REGISTRY_REPOSITORY_URL/timesfm:latest
                 ports:
                 - containerPort: 5000
                 resources:
                   requests:
                     nvidia.com/gpu-pod-NVIDIA_H100_80GB_HBM3: 1  # Request 1 GPU
                   limits:
                     nvidia.com/gpu-pod-NVIDIA_H100_80GB_HBM3: 1  # Limit to 1 GPU
                 env:
                 - name: ENV
                   value: "production"
               imagePullSecrets:
               - name: docker-registry-secret
         

Replace the following:

     * `REGISTRY_REPOSITORY_URL`: the repository URL.
     * `DOCKER_REGISTRY_SECRET`: name of the docker secret.
  6. Create a file `timesfm-service.yaml` to expose the `timesfm` server internally.
         
         apiVersion: v1
         kind: Service
         metadata:
           name: timesfm-service
         spec:
           selector:
             app: timesfm
           ports:
             - protocol: TCP
               port: 80 # External port exposed
               targetPort: 5000 # Internal container port for Flask
           type: LoadBalancer # Use NodePort for internal access
         

  7. Apply the manifests.
         
         kubectl --kubeconfig ${KUBECONFIG} apply -f timesfm-deployment.yaml
         kubectl --kubeconfig ${KUBECONFIG} apply -f timesfm-service.yaml
         

  8. Ensure the `TimesFM` pods are running.
         
         kubectl --kubeconfig ${KUBECONFIG} get deployments timesfm-deployment -n sandbox-gpu-project
         kubectl --kubeconfig ${KUBECONFIG} get service timesfm-service -n sandbox-gpu-project
         

  9. Create a Project Network Policy to allow the inbound traffic from external IP addresses.
         
         kubectl --kubeconfig ${KUBECONFIG} apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: sandbox-gpu-project
           name: allow-inbound-traffic-from-external
         spec:
           policyType: Ingress
           subject:
             subjectType: UserWorkload
           ingress:
           - from:
             - ipBlock:
                 cidr: 0.0.0.0/0
         EOF
         

**Note:** This network policy is unsecure, and is not safe outside the GDC Sandbox environment. In a real production environment, you are responsible for creating a more secure network policy.
  10. Identify the external IP of the TimesFM service by running the following command. Keep a note of it for use in later steps, where you will substitute this value for TIMESFM_END_POINT.
         
         kubectl --kubeconfig ${KUBECONFIG} get service timesfm-service \
                 -n sandbox-gpu-project -o jsonpath='{.status.loadBalancer.ingress[*].ip}'
         




## Test the service.

  1. To get a prediction, send data to the service using a `curl` command, replacing TIMESFM_END_POINT with the service's actual address and your input values for features. This invokes the `predict` function defined in `app.py`, which will perform some manipulation on your input data and return it in json format.
         
         curl -X POST http://TIMESFM_END_POINT/predict -H "Content-Type: application/json" -d '{"features": [1.2, 3.4, 5.6]}'
         

  2. Send a curl request to /timeseries to see an example of data visualization using randomly generated data. This invokes the time series function defined in app.py, which generates a random time series and performs a moving average analysis on it.
         
         curl http://TIMESFM_END_POINT/timeseries
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
