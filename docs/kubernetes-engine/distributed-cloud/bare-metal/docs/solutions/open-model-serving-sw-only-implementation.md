---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/open-model-serving-sw-only-implementation/
title: Open model serving on Distributed Cloud software only reference implementation \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:13.348635+00:00
---

# Open model serving on Distributed Cloud software only reference implementation  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/open-model-serving-sw-only-implementation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Open model serving on Distributed Cloud software only reference implementation Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This document serves as the **Solution Reference Implementation (SRI)** guide, describing the concrete steps required to deploy, serve, and validate the **Open Model Serving on Distributed Cloud software only** solution.

This guide implements the deployment of the optimized **vLLM serving engine** running **Gemma 4** (`google/gemma-4-31B-it`) on a Distributed Cloud software only **Single-Node Cluster configuration targeted for edge deployment** utilizing physical NVIDIA GPU resources (e.g., RTX PRO 6000).

This walkthrough is designed to be executed from a CLI terminal client with `kubectl` access to the Distributed Cloud software only cluster.

**Note:** Throughout this guide, the following placeholders are used: 

  * `<local-working-dir>`: The root directory of your project workspace (e.g., `~/gdcso-open-model-serving/`).
  * `<local-config-dir>`: The directory containing your local configurations and environment files (e.g., `gdcso-open-model-serving-local/`).



## Objectives

By completing this Solution Reference Implementation, you will:

  * **Configure serving environment parameters** via a local `.env` file.
  * **Deploy a Persistent Volume Claim (PVC)** using the `local-shared` storage class to persist model weights.
  * **Deploy the optimized vLLM serving engine** utilizing Vertex AI-qualified containers, mapping physical `nvidia.com/gpu` resources.
  * **Deploy the Gradio Web UI** to provide an interactive chat interface.
  * **Establish local port-forwarding tunnels** to validate serving responsiveness via APIs and the Web UI.
  * **Verify observability integration** by confirming log and metric ingestion (including GPU telemetry) into Cloud Logging and Cloud Monitoring.



## Before you begin

### Prerequisites (cluster setup)

This guide assumes you have a running Distributed Cloud software only cluster with GPU support configured. For installing the cluster, refer to the official [Distributed Cloud software only for bare metal documentation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal#install). The GPU configuration must comply with the official Google Cloud documentation for [Set up and use NVIDIA GPUs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/gpu-manual-use).

### Client workstation prerequisites

Ensure your local terminal environment has the following tools installed and configured:

  * **gcloud CLI:** Required for project configuration and querying logs. **Must be authenticated (`gcloud auth login`) and configured to the active Google Cloud project where the Distributed Cloud software only cluster is registered.**
  * **kubectl:** Required for managing cluster resources. Must be configured with the appropriate context to access the target Distributed Cloud software only cluster (e.g., via connect gateway or direct local network access).
  * **curl:** Required for sending test requests to the serving endpoint.
  * **jq:** Required for parsing JSON output from the serving endpoint.



### Hugging Face model access

To download and deploy the Gemma 4 model, you must have access to the Hugging Face repository:

  1. **Hugging Face Account:** Ensure you have a registered account on [Hugging Face](https://huggingface.co/).
  2. **Accept Model License:** Navigate to the [Gemma 4 31B IT model page](https://huggingface.co/google/gemma-4-31B-it) and agree to the license terms to gain access to the gated model weights.
  3. **Generate Access Token:** Generate a **User Access Token** with **Read** permissions from your Hugging Face account settings (Settings -> Access Tokens). This token will be used as `HF_TOKEN` in your configuration.



### Central reference configuration

All deployment parameters are managed via a central `.env` file located at `<local-config-dir>/.env`. Ensure this file exists and contains your specific parameters (Hugging Face token, namespace, model name, etc.).

Example `.env` structure:
    
    
    # GDCso Cluster Namespace
    NAMESPACE_NAME="your-custom-namespace"
    
    # Hugging Face Token (Required to download gated Gemma models)
    HF_TOKEN="your-hf-token-here"
    
    # Model Sizing Parameters
    MODEL_NAME="google/gemma-4-31B-it"
    SAFE_MODEL_NAME="google-gemma-4-31B-it"
    
    # Hyperparameters
    MAX_MODEL_LEN=8192
    GPU_MEMORY_UTILIZATION=0.95
    MAX_NUM_SEQS=512
    MAX_NUM_BATCHED_TOKENS=4096
    DTYPE="bfloat16"
    
    # Pod Sizing Requests
    CPU_REQUEST="4"
    MEMORY_REQUEST="80"
    

## Set up environment and credentials

### Create namespace and Hugging Face secret

Before deploying, you must create the namespace and the Hugging Face token secret:
    
    
    # Navigate to your project root
    cd <local-working-dir>
    
    # Sourced from your local .env file
    source <local-config-dir>/.env
    
    # Create namespace
    kubectl create namespace ${NAMESPACE_NAME} --dry-run=client -o yaml | kubectl apply -f -
    
    # Create Hugging Face token secret
    kubectl create secret generic hf-token-secret \
      --from-literal=token="${HF_TOKEN}" \
      -n "${NAMESPACE_NAME}" --dry-run=client -o yaml | kubectl apply -f -
    

## vLLM deployment on Kubernetes

The deployment consists of three main manifests: PVC, Service, and Deployment. These templates use environment variables that are substituted at deployment time.

### Persistent Volume Claim (PVC)

The PVC ensures model weights persist across pod restarts, using the Distributed Cloud software only `local-shared` storage class.

Create a file named `vllm-pvc.yaml` with the following content:
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: model-cache-pvc
      namespace: ${NAMESPACE_NAME}
    spec:
      accessModes:
        - ReadWriteOnce
      storageClassName: local-shared
      resources:
        requests:
          storage: 100Gi
    

### Service

Exposes the vLLM API server internally on port 8000.

Create a file named `vllm-service.yaml` with the following content:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: vllm-service
      namespace: ${NAMESPACE_NAME}
      labels:
        app: vllm
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/path: "/metrics"
        prometheus.io/port: "8000"
    spec:
      ports:
        - name: http
          port: 8000
          targetPort: 8000
      selector:
        app: vllm
      type: ClusterIP
    

### Deployment

Runs the vLLM container, mounts the model cache volume, and requests physical GPU resources. While 96 GB of VRAM fits unquantized BF16 weights (~62 GB), this reference implementation enables Blackwell FP8 quantization (`--quantization=fp8`, ~31 GB weights) to expand the KV cache to 56.53 GiB (`61,728` tokens) for higher concurrent throughput.

Create a file named `vllm-deployment.yaml` with the following content:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: vllm-deployment
      namespace: ${NAMESPACE_NAME}
      labels:
        app: vllm
        ai.gke.io/inference-server: vllm
        ai.gke.io/model: ${SAFE_MODEL_NAME}
    spec:
      replicas: 1
      strategy:
        type: Recreate
      selector:
        matchLabels:
          app: vllm
      template:
        metadata:
          labels:
            app: vllm
            examples.ai.gke.io/source: user-guide
            ai.gke.io/inference-server: vllm
            ai.gke.io/model: ${SAFE_MODEL_NAME}
        spec:
          runtimeClassName: nvidia
          containers:
            - name: vllm-container
              image: us-docker.pkg.dev/vertex-ai/vertex-vision-model-garden-dockers/pytorch-vllm-serve:gemma4
              imagePullPolicy: IfNotPresent
              command: ["python3", "-m", "vllm.entrypoints.openai.api_server"]
              args:
                - --model=$(MODEL_ID)
                - --host=0.0.0.0
                - --port=8000
                - --tensor-parallel-size=1
                - --enable-log-requests
                - --max-model-len=${MAX_MODEL_LEN}
                - --gpu-memory-utilization=${GPU_MEMORY_UTILIZATION}
                - --max-num-seqs=${MAX_NUM_SEQS}
                - --max-num-batched-tokens=${MAX_NUM_BATCHED_TOKENS}
                - --dtype=${DTYPE}
                - --trust-remote-code
                - --enable-prefix-caching
                - --enable-chunked-prefill
                - --quantization=fp8
              env:
                - name: MODEL_ID
                  value: ${MODEL_NAME}
                - name: HUGGING_FACE_HUB_TOKEN
                  valueFrom:
                    secretKeyRef:
                      name: hf-token-secret
                      key: token
                - name: LD_LIBRARY_PATH
                  value: "/usr/local/nvidia/lib64"
              ports:
                - name: http
                  containerPort: 8000
              resources:
                requests:
                  cpu: ${CPU_REQUEST}
                  memory: "${MEMORY_REQUEST}Gi"
                  nvidia.com/gpu: "1"
                limits:
                  cpu: ${CPU_REQUEST}
                  memory: "${MEMORY_REQUEST}Gi"
                  nvidia.com/gpu: "1"
              volumeMounts:
                - mountPath: /root/.cache/huggingface
                  name: cache-volume
                - mountPath: /dev/shm
                  name: dshm
          volumes:
            - name: cache-volume
              persistentVolumeClaim:
                claimName: model-cache-pvc
            - name: dshm
              emptyDir:
                medium: Memory
                sizeLimit: 16Gi
    

## Gradio UI deployment

The Gradio UI provides an interactive web interface to chat with the model. It is deployed within the cluster and connects to the vLLM service via the internal Kubernetes network.

### Gradio deployment

Create a file named `gradio-deployment.yaml` with the following content:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: gradio-deployment
      namespace: ${NAMESPACE_NAME}
      labels:
        app: gradio
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: gradio
      template:
        metadata:
          labels:
            app: gradio
        spec:
          containers:
          - name: gradio
            image: us-docker.pkg.dev/google-samples/containers/gke/gradio-app:v1.0.4
            resources:
              requests:
                cpu: "250m"
                memory: "512Mi"
              limits:
                cpu: "500m"
                memory: "512Mi"
            env:
            - name: CONTEXT_PATH
              value: "/v1/chat/completions"
            - name: HOST
              value: "http://vllm-service:8000"
            - name: MODEL_ID
              value: "${MODEL_NAME}"
            ports:
            - containerPort: 7860
    

### Gradio service

Create a file named `gradio-service.yaml` with the following content:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: gradio-service
      namespace: ${NAMESPACE_NAME}
    spec:
      selector:
        app: gradio
      ports:
      - protocol: TCP
        port: 8080
        targetPort: 7860
      type: ClusterIP
    

## Observability configuration

For details on configuring application logging and monitoring, refer to the official [Application logging and monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/application-logging-monitoring) guide.

### vLLM monitoring

To enable scraping of vLLM metrics by Google Cloud Managed Service for Prometheus (GMP), we deploy a `PodMonitoring` resource targeting the vLLM pods.

Create a file named `vllm-pod-monitoring.yaml` with the following content:
    
    
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      name: vllm-pod-monitoring
      namespace: ${NAMESPACE_NAME}
    spec:
      selector:
        matchLabels:
          app: vllm
      endpoints:
      - port: http
        interval: 30s
    

### GPU monitoring

To enable scraping of GPU metrics from the NVIDIA DCGM Exporter by Google Cloud Managed Service for Prometheus (GMP), we deploy a `PodMonitoring` resource in the `gpu-operator` namespace. For more details, refer to [Send GPU metrics to Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/gpu-metrics).

**Note:** Deploying this resource requires write permissions to the `gpu-operator` namespace. This may need to be performed by a cluster administrator. 

Create a file named `gpu-pod-monitoring.yaml` with the following content:
    
    
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      name: dcgm-gmp
      namespace: gpu-operator
    spec:
      selector:
        matchLabels:
          app: nvidia-dcgm-exporter
      endpoints:
      - port: metrics
        interval: 30s
    

## Execution steps

### Deploy manifests

Apply the manifests to the cluster. Since the YAML files contain environment variable placeholders, use `envsubst` to substitute the variables from your `.env` file before applying them.

  1. Navigate to your working directory containing the YAML files:
         
         cd <local-working-dir>
         

  2. Source the environment variables:
         
         source <local-config-dir>/.env
         

  3. Apply the manifests in sequence:
         
         # Apply core serving manifests
         envsubst < vllm-pvc.yaml | kubectl apply -f -
         envsubst < vllm-service.yaml | kubectl apply -f -
         envsubst < vllm-deployment.yaml | kubectl apply -f -
         
         # Apply observability manifests
         envsubst < vllm-pod-monitoring.yaml | kubectl apply -f -
         kubectl apply -f gpu-pod-monitoring.yaml
         
         # Apply Gradio UI manifests
         envsubst < gradio-deployment.yaml | kubectl apply -f -
         envsubst < gradio-service.yaml | kubectl apply -f -
         




## Verification

### Monitor pod boot sequence

Stream the container logs to track the startup sequence:
    
    
    # 1. Check pod status (wait until it is Running)
    kubectl get pods -n ${NAMESPACE_NAME} -l app=vllm
    
    # 2. Stream logs to verify model loading
    kubectl logs -f -l app=vllm -n ${NAMESPACE_NAME}
    

Wait until you see the active serving ready signal in your logs:
    
    
    INFO: Application startup complete.
    

### Establish port-forwarding tunnel

To test the endpoint locally, forward the service port 8000:
    
    
    kubectl port-forward service/vllm-service 8000:8000 -n ${NAMESPACE_NAME}
    

Keep this terminal open or run it in the background.

### Query serving endpoint

From a separate terminal, test the API responsiveness:

#### 1\. Query models list
    
    
    curl -s http://localhost:8000/v1/models | jq
    

#### 2\. Query chat completions
    
    
    curl -s http://localhost:8000/v1/chat/completions \
      -H "Content-Type: application/json" \
      -d '{
        "model": "'"${MODEL_NAME}"'",
        "messages": [
          {"role": "user", "content": "What is AGI in 100 words"}
        ],
        "max_tokens": 150
      }' | jq
    

### Verify GPU and VRAM allocations

To ensure the model is utilizing the hardware efficiently and that the memory footprint is correct, you can run a GPU audit.

#### Audit GPU via nvidia-smi inside the pod

Retrieve the name of your active vLLM pod and execute `nvidia-smi` inside the container:
    
    
    # Dynamically get the pod name
    export VLLM_POD_NAME=$(kubectl get pods -n ${NAMESPACE_NAME} -l app=vllm -o jsonpath='{.items[0].metadata.name}')
    
    # Run nvidia-smi inside the container
    kubectl exec ${VLLM_POD_NAME} -n ${NAMESPACE_NAME} -- nvidia-smi
    

Expected Output: The output should report physical VRAM utilization matching your `GPU_MEMORY_UTILIZATION` parameter. For example, on a workstation with an NVIDIA RTX PRO 6000 (approx. 96 GB VRAM) running `google/gemma-4-31B-it` with `GPU_MEMORY_UTILIZATION=0.95`, you should see ~95,800 MiB allocated to `VLLM::EngineCore`:
    
    
    +-----------------------------------------------------------------------------------------+
    | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
    |                                         |                        |               MIG M. |
    |=========================================+========================+======================|
    |   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:05:00.0 Off |                    0 |
    | N/A   36C    P0             85W /  600W |   95805MiB /  97887MiB |      0%      Default |
    +-----------------------------------------+------------------------+----------------------+
    

#### Verify KV cache allocation in logs

You can also check the vLLM internal allocation logs to verify the KV Cache size and token concurrency:
    
    
    kubectl logs ${VLLM_POD_NAME} -n ${NAMESPACE_NAME} | grep -E "Available KV cache|GPU KV cache size"
    

Expected Output:
    
    
    (EngineCore pid=362) INFO 06-18 15:03:43 [gpu_worker.py:456] Available KV cache memory: 56.53 GiB
    (EngineCore pid=362) INFO 06-18 15:03:43 [kv_cache_utils.py:1316] GPU KV cache size: 61,728 tokens
    

This confirms that 56.53 GiB of VRAM is reserved for context KV cache, allowing a large number of concurrent tokens.

### Verify Gradio UI deployment

Once the Gradio pod is running, you can access the UI by establishing a port-forwarding tunnel.

#### Monitor Gradio pod status

Ensure the Gradio pod is running:
    
    
    kubectl get pods -n ${NAMESPACE_NAME} -l app=gradio
    

Expected Output:
    
    
    NAME                                READY   STATUS    RESTARTS   AGE
    gradio-deployment-yyyyyyyy-yyyyy    1/1     Running   0          1m
    

#### Establish port-forwarding tunnel to Gradio

Forward the Gradio service port 8080 to your local port 7860:
    
    
    kubectl port-forward service/gradio-service 7860:8080 -n ${NAMESPACE_NAME}
    

Keep this terminal open or run it in the background:
    
    
    kubectl port-forward service/gradio-service 7860:8080 -n ${NAMESPACE_NAME} > pf_gradio.log 2>&1 & sleep 3
    

#### Access the web UI

  * **If running on a Local Workstation:** Open your browser and navigate directly to: `http://localhost:7860`
  * **If running inside Cloud Shell:** Use the **Web Preview** button, select **Change Port** , enter `7860`, and click **Change and Preview**.



You should see the Gradio chatbot interface. You can type a message to interact with the Gemma model. The Gradio pod will route the request internally to the `vllm-service` endpoint.

#### Clean up tunnels

To stop the port-forwarding tunnel:
    
    
    pkill -f "port-forward service/gradio-service"
    

### Monitoring verification

Once vLLM is deployed and the `PodMonitoring` resource is applied, you can verify that metrics are being ingested into Cloud Monitoring.

#### Verify PodMonitoring status

Ensure the `PodMonitoring` resource is created and active:
    
    
    kubectl get podmonitoring -n ${NAMESPACE_NAME}
    

#### Verify metric ingestion using the Google Cloud console

You can verify that metrics are being ingested using the Google Cloud console (Metrics Explorer):

  1. Open the **Metrics Explorer** in the Google Cloud console: 
     * Go to `https://console.cloud.google.com/monitoring/metrics-explorer` (ensure you select your project `${GCP_PROJECT_ID}`).
  2. In the **Select a metric** drop-down, search for and select: 
     * `prometheus.googleapis.com/vllm:num_requests_running/gauge` to verify vLLM metrics.
     * `prometheus.googleapis.com/DCGM_FI_DEV_GPU_UTIL/gauge` to verify GPU utilization metrics.
  3. Observe the chart to confirm that data points are being actively plotted.



### Logging verification

Once the workload is running, you can verify that logs are being exported to Cloud Logging.

#### Verify vLLM log ingestion

Verify that vLLM container logs are being exported to Cloud Logging:
    
    
    project_id=$(gcloud config get-value project)
    
    gcloud logging read "resource.type=\"k8s_container\" AND resource.labels.namespace_name=\"${NAMESPACE_NAME}\" AND resource.labels.container_name=\"vllm-container\"" --limit=10 --project=${project_id}
    

#### Verify GPU exporter log ingestion

Verify that GPU exporter container logs are being exported to Cloud Logging:
    
    
    project_id=$(gcloud config get-value project)
    
    gcloud logging read "resource.type=\"k8s_container\" AND resource.labels.namespace_name=\"gpu-operator\" AND resource.labels.container_name=\"nvidia-dcgm-exporter\"" --limit=10 --project=${project_id}
    

#### Verify logs using the Google Cloud console (Logs Explorer)

You can also verify log ingestion using the Google Cloud console:

  1. Open the **Logs Explorer** in the Google Cloud console: 
     * Go to `https://console.cloud.google.com/logs/query` (ensure you select your project `${GCP_PROJECT_ID}`).
  2. In the **Query** box, enter the following query to view vLLM logs:
         
         resource.type="k8s_container"
         resource.labels.namespace_name="<NAMESPACE_NAME>"
         resource.labels.container_name="vllm-container"
         

_(Replace`<NAMESPACE_NAME>` with your actual namespace, e.g., `your-custom-namespace`)_.

  3. Click **Run query**. You should see the log entries from the vLLM container.

  4. To verify GPU exporter logs, run the following query:
         
         resource.type="k8s_container"
         resource.labels.namespace_name="gpu-operator"
         resource.labels.container_name="nvidia-dcgm-exporter"
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
