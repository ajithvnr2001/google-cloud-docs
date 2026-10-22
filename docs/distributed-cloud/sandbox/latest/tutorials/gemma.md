---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/tutorials/gemma/
title: Deploying Gemma using Ollama and Open-WebUI \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:09.309415+00:00
---

# Deploying Gemma using Ollama and Open-WebUI  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/tutorials/gemma/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Deploying Gemma using Ollama and Open-WebUI Stay organized with collections  Save and categorize content based on your preferences. 

With the enterprise-grade NVIDIA GPUS included in the GDC Sandbox AI Optimized SKU, you can develop and test demanding AI training and inference applications, such as generative AI.

Gemma is a lightweight Large Language Model based on Gemini technology. This tutorial guide shows how to deploy Gemma with [Ollama](https://ollama.com/) and [Open-WebUI](https://github.com/open-webui/open-webui) on GDC Sandbox and has the following objectives.

  * Deploy Ollama with the Gemma model on a AI-Optimized GDC Sandbox with GPUs.
  * Send prompts to the Ollama service on its private endpoint through the Open-WebUI interface.



### Before you begin

The GPUs provided by the GDC Sandbox AI Optimized SKU are included in the org-infra cluster. 

  * To run commands against the org infrastructure cluster, make sure that you have the kubeconfig of the `org-1-infra` cluster, as described in [Work with clusters](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/clusters#org-infra-cluster):

    * Configure and authenticate with the `gdcloud` command line, and
    * generate the kubeconfig file for the org infrastructure cluster, and assign its path to the environment variable `KUBECONFIG`.
  * Ensure the user has `sandbox-gpu-admin` role assigned for the project `sandbox-gpu-project`. By default, the role is assigned to the `platform-admin` user. You can assign the role to other users by signing in as the `platform-admin` and running the following command:
        
        kubectl --kubeconfig ${KUBECONFIG} create rolebinding ${NAME} --role=sandbox-gpu-admin \
        --user=${USER} --namespace=sandbox-gpu-project
        

  * Make sure to set up Artifact Registry repository as described in the [Using Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images) and sign in to be able to push and pull images to the artifact registry.




### Deploy Gemma model with Ollama and Open-WebUI

The deployment is orchestrated through a set of Kubernetes configuration files (YAML manifests), each defining a specific component or service.

  1. Create a Dockerfile with Gemma pre downloaded.
         
         FROM ubuntu
         
          # Install Ollama
          # This uses Ollamas official installation script, which adds Ollama to /usr/local/bin
          RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates zstd
          RUN curl -fsSL https://ollama.com/install.sh -o install.sh
          RUN chmod +x install.sh
          RUN ./install.sh && \
              rm -rf /var/lib/apt/lists/*
         
          # Set environment variables for Ollama (optional, but good practice)
          ENV OLLAMA_HOST="0.0.0.0"
          # ENV OLLAMA_MODELS="/usr/local/ollama/models" # Default is /root/.ollama
          # If you want to customize the model storage path within the container, set OLLAMA_MODELS
          # and then ensure you create and populate that directory. Default is usually fine for pre-downloaded.
         
          # --- Predownload Gemma Model ---
          # This step starts Ollama server in the background, pulls the model,
          # and then kills the server to allow the Docker build to continue.
          # This approach works around Docker''s RUN command limitations for services.
         
          RUN ollama serve & \
              sleep 5 && \
              # Give the Ollama server a moment to start up
              # Use --retry and --retry-connrefused to handle startup delays
              curl --retry 10 --retry-connrefused -s http://localhost:11434 || true && \
              echo "Attempting to pull gemma:7b..." && \
              ollama pull gemma:7b && \
              echo "Model pull complete. Cleaning up background Ollama process." && \
              pkill ollama || true # Gracefully kill the ollama serve process
         
          # Expose Ollama's default port
          EXPOSE 11434
         
          # Command to run Ollama server when the container starts
          CMD ["ollama", "serve"]
         
         


**Note:** Alternatively, download `mistral:7b` using `ollama pull mistral:7b` when building the Docker image to deploy Mistral with Ollama.

  1. Build the docker image and upload it to Artifact Registry repository.
         
         docker build -t ollama-gemma .
         docker tag ollama-gemma REGISTRY_REPOSITORY_URL/ollama-gemma:latest
         docker push REGISTRY_REPOSITORY_URL/ollama-gemma:latest
         

Replace the following:

     * `REGISTRY_REPOSITORY_URL` with the repository URL.
  2. Create a secret to save the docker credentials.
         
         export SECRET=DOCKER_REGISTRY_SECRET
         export DOCKER_TEST_CONFIG=~/.docker/config.json
         kubectl --kubeconfig ${KUBECONFIG} create secret docker-registry ${SECRET} --from-file=.dockerconfigjson=${DOCKER_TEST_CONFIG} -n sandbox-gpu-project
         

Replace the following:

     * `DOCKER_REGISTRY_SECRET` name of the secret.
  3. Create a file `ollama-deployment.yaml` to define the Ollama AI engine deployment:

The deployment of the Ollama server requests one GPU.
         
         apiVersion: apps/v1
           kind: Deployment
           metadata:
             annotations:
               deployment.kubernetes.io/revision: "9"
             name: ollama
             namespace: sandbox-gpu-project
           spec:
             progressDeadlineSeconds: 600
             replicas: 1
             revisionHistoryLimit: 10
             selector:
               matchLabels:
                 app: ollama
             strategy:
               rollingUpdate:
                 maxSurge: 25%
                 maxUnavailable: 25%
               type: RollingUpdate
             template:
               metadata:
                 creationTimestamp: null
                 labels:
                   app: ollama
                   egress.networking.gke.io/enabled: "true"
               spec:
                 containers:
                   - name: ollama
                     image: REGISTRY_REPOSITORY_URL/ollama-gemma:latest
                     imagePullPolicy: Always
                     ports:
                       - containerPort: 11434
                         protocol: TCP
                     resources:
                       limits:
                         nvidia.com/gpu-pod-NVIDIA_H100_80GB_HBM3: "1"
                       requests:
                         nvidia.com/gpu-pod-NVIDIA_H100_80GB_HBM3: "1"
                     env:
                       - name: OLLAMA_HOST
                         value: 0.0.0.0
                       - name: OLLAMA_ORIGINS
                         value: http://localhost:8080,http://ollama-webui.ollama-llm.svc.cluster.local:8080,http://ollama-webui:8080
                     securityContext:
                       seLinuxOptions:
                         type: unconfined_t
                     terminationMessagePath: /dev/termination-log
                     terminationMessagePolicy: File
                 imagePullSecrets:
                 - name: DOCKER_REGISTRY_SECRET
                 dnsConfig:
                   nameservers:
                     - 8.8.8.8
                 dnsPolicy: ClusterFirst
                 restartPolicy: Always
                 schedulerName: default-scheduler
                 terminationGracePeriodSeconds: 30
         
         

Replace the following:

     * `REGISTRY_REPOSITORY_URL`: the repository URL.
     * `DOCKER_REGISTRY_SECRET`: name of the secret.
  4. Create the file `ollama-service.yaml` to expose the Ollama server internally.
         
         apiVersion: v1
         kind: Service
         metadata:
           name: ollama
           namespace: sandbox-gpu-project
           annotations:
             metallb.universe.tf/ip-allocated-from-pool: lb-address-pool-0-ptleg
         spec:
           type: LoadBalancer
           selector:
             app: ollama
           ports:
             - port: 11434
               nodePort: 30450
           ipFamilyPolicy: SingleStack
           ipFamilies:
             - IPv4
           clusterIPs:
             - 10.1.122.216
           clusterIP: 10.1.122.216
         

  5. Apply the manifests
         
         kubectl --kubeconfig ${KUBECONFIG} apply -f ollama-deployment.yaml
         kubectl --kubeconfig ${KUBECONFIG} apply -f ollama-service.yaml
         

  6. Ensure the ollama pods are running.
         
         kubectl --kubeconfig ${KUBECONFIG} get deployments -n sandbox-gpu-project
         kubectl --kubeconfig ${KUBECONFIG} get service -n sandbox-gpu-project
         

  7. Keep a note of the External IP of the Ollama service `OLLAMA_BASE_END_POINT` from the output
         
         kubectl --kubeconfig ${KUBECONFIG} get service ollama \
               -n sandbox-gpu-project -o jsonpath='{.status.loadBalancer.ingress[*].ip}'
         

  8. Create file `openweb-ui-deployment.yaml` to deploy Open-WebUI Interface.
         
         apiVersion: apps/v1
           kind: Deployment
           metadata:
             name: ollama-webui
             namespace: sandbox-gpu-project
             labels:
               app: ollama-webui
             annotations:
               deployment.kubernetes.io/revision: "5"
           spec:
             replicas: 1
             selector:
               matchLabels:
                 app: ollama-webui
             strategy:
               type: RollingUpdate
               rollingUpdate:
                 maxSurge: 25%
                 maxUnavailable: 25%
             progressDeadlineSeconds: 600
             revisionHistoryLimit: 10
             template:
               metadata:
                 labels:
                   app: ollama-webui
                 creationTimestamp: null
               spec:
                 containers:
                   - name: ollama-webui
                     image: ghcr.io/open-webui/open-webui:main
                     imagePullPolicy: IfNotPresent
                     ports:
                       - name: http
                         containerPort: 8080
                         protocol: TCP
                     env:
                       - name: OLLAMA_BASE_URL
                         value: OLLAMA_BASE_END_POINT
                       - name: PORT
                         value: "8080"
                     terminationMessagePath: /dev/termination-log
                     terminationMessagePolicy: File
                 restartPolicy: Always
                 dnsPolicy: ClusterFirst
                 schedulerName: default-scheduler
                 terminationGracePeriodSeconds: 30
         

Replace the following:

     * `OLLAMA_BASE_END_POINT`: the external IP address of the Ollama service.
  9. Create a file `ollama-webui-service.yaml` to externally expose the open webui interface.
         
         apiVersion: v1
         kind: Service
         metadata:
           name: ollama-webui
           namespace: sandbox-gpu-project
           annotations:
             metallb.universe.tf/ip-allocated-from-pool: lb-address-pool-0-ptleg
         spec:
           type: LoadBalancer
           ipFamilyPolicy: SingleStack
           ipFamilies:
           - IPv4
           clusterIPs:
           - 10.1.104.52
           clusterIP: 10.1.104.52
           ports:
           - port: 80
             targetPort: 8080
             nodePort: 32351
           selector:
             app: ollama-webui
         

  10. Apply the manifests `openweb-ui-deployment.yaml` and `ollama-webui-service.yaml`` against the cluster.
         
         kubectl --kubeconfig ${KUBECONFIG} apply -f openweb-ui-deployment.yaml
             kubectl --kubeconfig ${KUBECONFIG} apply -f ollama-webui-service.yaml
         

  11. Create a Project Network Policy to allow inbound traffic from external IP addresses.
         
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
  12. Identity the external IP of the Ollama service by running the following command. Keep a note of it for use in later steps, where you will substitute this value for `OPEN_WEB_UI_ENDPOINT`.
         
         kubectl --kubeconfig ${KUBECONFIG} get service -n sandbox-gpu-project
         

  13. Open Google Chrome and enter the URL using the external IP address you found in the previous step. You can now interact with the Gemma model through the Open Web UI interface.
         
         http://OPEN_WEB_UI_ENDPOINT/
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
