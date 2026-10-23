---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multi-host-tpu-llm/
title: Serve Gemma open models using multi-host TPUs on GKE with Ray \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:11.217352+00:00
---

# Serve Gemma open models using multi-host TPUs on GKE with Ray  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multi-host-tpu-llm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Serve Gemma open models using multi-host TPUs on GKE with Ray Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial walks you through deploying a multi-host TPU inference service using [Ray Serve LLM](https://docs.ray.io/en/latest/serve/llm/index.html). By leveraging Ray's native TPU support to atomically co-schedule distributed engine workers across complex accelerator topologies, you can deploy large models over a multi-host TPU slice for inference.

**Tip:** For production deployments on GKE, we recommend using [Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference-quickstart) is recommended to get tailored best practices and configurations for your model inference.

This tutorial is intended for Machine learning (ML) engineers, Platform admins and operators, and for Data and AI specialists who are interested in using Kubernetes container orchestration capabilities for serving AI/ML workloads on distributed, multi-host TPU slices. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following:

  * [Autopilot mode and Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)
  * [Multi-host TPU slices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host)
  * [GKE managed DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra)



## Background

This section describes the key technologies used in this guide.

### TPUs

[Tensor Processing Units](https://cloud.google.com/tpu) (TPUs) let you accelerate specific workloads running on your nodes, such as machine learning and data processing. The primary advantage of TPUs is performance at scale. This tutorial uses [TPU Trillium](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#trillium-benefits), the sixth generation of [Cloud TPU](https://docs.cloud.google.com/tpu/docs/v6e). Multi-host TPU slices consist of multiple physical nodes communicating using a high-speed inter-chip interconnect (ICI), which works well for high-throughput and low-latency serving.

### vLLM on Ray

[vLLM](https://docs.vllm.ai/en/latest/) is a high-throughput, memory-efficient LLM serving engine. By integrating with [Ray Serve](https://docs.ray.io/en/latest/serve/index.html), vLLM can scale across multiple hosts and access physical hardware topologies natively. This tutorial demonstrates using Ray Serve's `LLMConfig` and `LLMServer` deployments to orchestrate vLLM inference across multi-host slices, letting the framework handle topology distribution and placement group spreading automatically.

## Objectives

This tutorial provides a foundation for understanding and exploring practical LLM deployment for inference in a managed Kubernetes environment that uses multi-host TPUs.

  1. Prepare your environment with a GKE cluster in Autopilot or Standard.
  2. Build a custom container image with baked-in dependencies.
  3. Deploy a Ray LLM Python script to your cluster to orchestrate vLLM inference over a TPU slice.
  4. Use Ray LLM to serve the Gemma 4 model through `curl` and an optional web chat interface.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure your project has sufficient quota for TPU Trillium (v6e) capacity in your selected region. For more information, see [Cloud TPU quotas](https://docs.cloud.google.com/tpu/docs/quota).
  * Ensure your GKE cluster uses GKE Dataplane V2 and satisfies version requirements for DRANET: **1.35.2-gke.1842000 or later** for both Standard and Autopilot.
  * Ensure that you have the following [IAM roles](https://docs.cloud.google.com/iam/docs/roles-permissions): 
    * `roles/container.admin`
    * `roles/iam.serviceAccountAdmin`



## Prepare your environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with the software you need for this tutorial, including `kubectl` and the `gcloud` CLI.

To set up your environment with Cloud Shell, follow these steps:

  1. In the Google Cloud console, launch a Cloud Shell session by clicking **Activate Cloud Shell** ![Activate Shell Button](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png). This launches a session in the bottom pane of the Google Cloud console.

  2. Create and activate a Python virtual environment:
         
         python3 -m venv ray-env
         source ray-env/bin/activate
         

  3. Install the Ray CLI:
         
         pip install "ray"
         

  4. Set the default environment variables:
         
         export PROJECT_ID=$(gcloud config get project)
         export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
         export CLUSTER_NAME=ray-llm-cluster
         export REGION=REGION
         export ZONE=ZONE
         export NAMESPACE=default
         export KSA_NAME=ray-ksa
         export NETWORK_NAME=${CLUSTER_NAME}-net
         export GS_BUCKET=BUCKET_NAME
         export REPO_NAME=ray-repo
         export CUSTOM_IMAGE_URI=REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/vllm-tpu-ray:vllm-tpu
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `CLUSTER_NAME`: the name of your cluster.
     * `REGION`: the region where your TPU Trillium capacity is available.
     * `ZONE`: the zone where your TPU Trillium capacity is available. For more information, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
     * `REPOSITORY`: the name of your Artifact Registry repository.
     * `BUCKET_NAME`: the name of your storage bucket.



## Create and configure Google Cloud resources

Follow these instructions to create the required resources.

### Create a GKE cluster and node pool

You can serve Gemma on TPUs in a GKE Autopilot or Standard cluster. GKE managed DRANET dynamically requests and manages high-performance networking resources for your distributed Pods, allowing GKE to automatically provision secondary high-speed networks for accelerator inter-communication without requiring manual VPC setup.

### Autopilot

  1. In Cloud Shell, create the Autopilot cluster:
         
         gcloud container clusters create-auto ${CLUSTER_NAME} \
             --project=${PROJECT_ID} \
             --enable-ray-operator \
             --location=${REGION}
         

  2. Configure `kubectl` to communicate with your cluster:
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} \
             --location=${REGION}
         

  3. To use GKE managed DRANET in Autopilot mode, deploy the custom ComputeClass resource provided in the repository to opt-in to dynamic networking:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: dranet-compute-class
         spec:
           nodePoolAutoCreation:
             enabled: true
           nodePoolConfig:
             dra:
               networking:
                 enabled: true
           priorities:
           - machineType: ct6e-standard-4t
             acceleratorNetworkProfile: auto

  4. Apply the manifest to your cluster:
         
         kubectl apply -f ai-ml/gke-ray/rayserve/llm/tpu/networking/dranet-compute-class.yaml
         




### Standard

  1. In Cloud Shell, create a Standard cluster that enables the Ray operator and uses GKE Dataplane V2:
         
         gcloud container clusters create ${CLUSTER_NAME} \
             --project=${PROJECT_ID} \
             --addons=RayOperator,GcsFuseCsiDriver \
             --machine-type=n2-standard-8 \
             --enable-dataplane-v2 \
             --workload-pool=${PROJECT_ID}.svc.id.goog \
             --location=${ZONE}
         

  2. Create a multi-host TPU slice node pool with the DRANET driver enabled:
         
         gcloud container node-pools create v6e-16 \
             --location=${ZONE} \
             --cluster=${CLUSTER_NAME} \
             --machine-type=ct6e-standard-4t \
             --tpu-topology=4x4 \
             --num-nodes=4 \
             --enable-gvnic \
             --scopes=https://www.googleapis.com/auth/cloud-platform \
             --accelerator-network-profile=auto \
             --node-labels=cloud.google.com/gke-networking-dra-driver=true
         




### Configure storage and authentication

Create a Cloud Storage bucket and initialize a Rapid Cache instance to accelerate model loading, then configure authentication for Hugging Face:

  1. In your TPU zone, create a storage bucket and initialize the Rapid Cache instance:
         
         gcloud storage buckets create gs://${GS_BUCKET} \
             --project=${PROJECT_ID} \
             --default-storage-class=STANDARD \
             --location=${REGION} \
             --uniform-bucket-level-access
         
         gcloud storage buckets anywhere-caches create gs://${GS_BUCKET} ${ZONE} \
             --ttl=1d \
             --admission-policy=ADMIT_ON_FIRST_MISS
         

  2. To allow your GKE Pods to mount the weight bucket, create a Kubernetes ServiceAccount:
         
         kubectl create serviceaccount ${KSA_NAME} --namespace ${NAMESPACE}
         

  3. Grant the Kubernetes ServiceAccount the Storage Object Admin role (`roles/storage.objectAdmin`) on the bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://${GS_BUCKET} \
             --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/${NAMESPACE}/sa/${KSA_NAME}" \
             --role="roles/storage.objectAdmin" \
             --condition=None
         

  4. To download the Gemma 4 model weights, you must acknowledge Google's license agreement on Hugging Face. Go to the [Gemma 4 model page on Hugging Face](https://huggingface.co/google/gemma-4-31B-it).

  5. Sign in accept the license terms by clicking **Agree and access repository**.

  6. Navigate to your Hugging Face account settings and generate an [Access Token](https://huggingface.co/settings/tokens) with the `Read` role.

  7. Export your Hugging Face token and create a Kubernetes secret so Ray can pull the model weights:
         
         export HF_TOKEN=YOUR_HUGGING_FACE_TOKEN
         
         kubectl create secret generic hf-secret \
           --from-literal=hf_api_token=${HF_TOKEN}
         




## Build the custom container image

To ensure the multi-host environment has all required dependencies, build a custom image based on vLLM's TPU image and copy your serving script into it.

  1. Create an Artifact Registry repository:
         
         gcloud artifacts repositories create ${REPO_NAME} \
             --repository-format=docker \
             --location=${REGION}
         

  2. Authenticate Docker to your project:
         
         gcloud auth configure-docker ${REGION}-docker.pkg.dev
         

  3. Inspect the `Dockerfile` in the sample repository:
         
         FROM vllm/vllm-tpu:v0.21.0
         
         ENV VLLM_TARGET_DEVICE=tpu
         ENV VLLM_XLA_CACHE_PATH=/data
         
         USER root
         
         RUN pip install --no-cache-dir -U \
             "https://s3-us-west-2.amazonaws.com/ray-wheels/master/75b85027a859439fae5634e49aa6443f6fbecfeb/ray-3.0.0.dev0-cp312-cp312-manylinux2014_x86_64.whl" && \
             pip install --no-cache-dir --no-deps "ray[llm]"
         
         COPY serve_tpu_multihost.py /home/ray/serve_tpu_multihost.py

  4. Build and push the image to Artifact Registry:
         
         docker build -t ${CUSTOM_IMAGE_URI} .
         docker push ${CUSTOM_IMAGE_URI}
         




## Pre-stage model weights to Cloud Storage

Before deploying the RayCluster, optimize model loading performance and help ensure high availability across your distributed TPU slice by pre-staging the model weights directly in your Cloud Storage bucket by using a standalone Kubernetes Job. This decoupled approach allows for coordinated parallel streaming, accelerating cluster startup times.

  1. The manifest for the downloader job is available in the repository. Review the manifest configuration:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: model-downloader
         spec:
           ttlSecondsAfterFinished: 60
           template:
             metadata:
               annotations:
                 gke-gcsfuse/volumes: "true"
                 gke-gcsfuse/memory-limit: "0"
             spec:
               serviceAccountName: ${KSA_NAME}
               restartPolicy: OnFailure
               containers:
               - name: downloader
                 image: python:3.10-slim
                 command: ["/bin/sh", "-c"]
                 args:
                 - |
                   pip install -U huggingface_hub filelock
         
                   python -c '
                   import filelock
         
                   class DummyLock:
                       def __init__(self, *args, **kwargs): pass
                       def __enter__(self): return self
                       def __exit__(self, *args): pass
                       def acquire(self, *args, **kwargs): pass
                       def release(self, *args, **kwargs): pass
         
                   filelock.FileLock = DummyLock
         
                   from huggingface_hub import snapshot_download
                   snapshot_download(
                       repo_id="google/gemma-4-31B-it", 
                       local_dir="/data/google/gemma-4-31B-it"
                   )
                   '
                 env:
                 - name: HF_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_api_token
                 volumeMounts:
                 - name: gcs-fuse-csi-ephemeral
                   mountPath: /data
               volumes:
               - name: gcs-fuse-csi-ephemeral
                 csi:
                   driver: gcsfuse.csi.storage.gke.io
                   volumeAttributes:
                     bucketName: ${GS_BUCKET}
                     mountOptions: "implicit-dirs"

  2. Create the downloader job by applying the file in the repository:
         
         envsubst < ai-ml/gke-ray/rayserve/llm/tpu/components/model-downloader-job.yaml | kubectl apply -f -
         

  3. Monitor the job until the download stream reports success:
         
         kubectl logs -f job/model-downloader
         




## Create the inference script

The following Python script defines a Ray Serve application powered by Ray Serve's high-level `LLMConfig` wrapper.

  1. Inspect the `serve_tpu_multihost.py` script in the sample repository:
         
         import os
         import ray
         from ray import serve
         from ray.serve.llm import LLMConfig, ModelLoadingConfig, LLMServingArgs, build_openai_app
         
         # Read configurations from environment variables
         MODEL_ID = os.environ.get("MODEL_ID", "google/gemma-4-31B-it")
         MODEL_SOURCE = os.environ.get("MODEL_SOURCE", "/data/google/gemma-4-31B-it")
         
         # TPU hardware options (i.e. TPU-V6E, TPU-V7X etc.)
         ACCELERATOR_TYPE = os.environ.get("ACCELERATOR_TYPE", "TPU-V6E")
         TPU_TOPOLOGY = os.environ.get("TPU_TOPOLOGY", "4x4")
         
         # vLLM engine parameters
         TENSOR_PARALLEL_SIZE = int(os.environ.get("TENSOR_PARALLEL_SIZE", "16"))
         MAX_MODEL_LEN = int(os.environ.get("MAX_MODEL_LEN", "8192"))
         MAX_NUM_BATCHED_TOKENS = int(os.environ.get("MAX_NUM_BATCHED_TOKENS", "4096"))
         
         # Define the multi-host TPU LLM config
         llm_config = LLMConfig(
             model_loading_config=dict(
                 model_id=MODEL_ID,
                 model_source=MODEL_SOURCE
             ),
             accelerator_type=ACCELERATOR_TYPE,
             accelerator_config={"kind": "tpu", "topology": TPU_TOPOLOGY},
             engine_kwargs={
                 "tensor_parallel_size": TENSOR_PARALLEL_SIZE,
                 "max_model_len": MAX_MODEL_LEN,
                 "max_num_batched_tokens": MAX_NUM_BATCHED_TOKENS,
                 "distributed_executor_backend": "ray",
             }
         )
         
         deployment = build_openai_app(
             LLMServingArgs(
                 llm_configs=[llm_config]
             )
         )




### Understand the Ray LLM API

The script leverages Ray Serve's native `ray.serve.llm` library to abstract away the complexity of multi-host TPU orchestration. By wrapping the vLLM engine, Ray Serve LLM provides a high-performance, scalable framework specifically designed for highly distributed inference workloads in production.

Using the Ray LLM API provides several key benefits:

  * **Multi-node deployments:** Ray Serve LLM enables users to serve massive models that span multiple distributed hosts (like a TPU multi-host slice) with automatic placement, coordination, and topology distribution natively.
  * **vLLM compatibility:** Ray Serve LLM provides an OpenAI-compatible API that aligns with vLLM's server. You can also access vLLM's advanced feature set (such as structured output, multimodal capabilities, and reasoning models) while scaling the workload across your Kubernetes cluster.
  * **Production-ready features:** Ray Serve LLM includes enterprise-grade capabilities like built-in autoscaling, custom request routing for maximized cache hits, and built-in integrations for metrics and observability.



In the provided inference script, the deployment is defined by two main components:

  * **`LLMConfig`:** this object defines the serving configuration. It specifies the model source, the engine parameters for vLLM, and the `accelerator_config`. By setting `{"kind": "tpu", "topology": "4x4"}`, Ray Serve LLM automatically provisions a distributed placement group that maps exactly to your physical 16-chip TPU v6e slice.
  * **`build_openai_app`:** this API automatically wraps the configured vLLM engine in an OpenAI-compatible FastAPI server, giving you an industry-standard REST API (like `/v1/chat/completions`) out of the box without writing any custom server code.



## Deploy the RayService

Deploy the Dynamic Resource Allocation (DRA) networking configuration and the `RayService` serving manifest:

  1. Request all available NetDevice interfaces on each node by deploying the `ResourceClaimTemplate` provided in the repository:
         
         apiVersion: resource.k8s.io/v1
         kind: ResourceClaimTemplate
         metadata:
           name: all-netdev
         spec:
           spec:
             devices:
               requests:
               - name: req-netdev
                 exactly:
                   deviceClassName: netdev.google.com
                   allocationMode: All

  2. Apply the template manifest to your cluster:
         
         kubectl apply -f ai-ml/gke-ray/rayserve/llm/tpu/networking/all-netdev-template.yaml
         

  3. The `RayService` serving manifest is available in the repository. Review the manifest configuration:
         
         apiVersion: ray.io/v1
         kind: RayService
         metadata:
           name: vllm-tpu-multihost
           labels:
             ai.gke.io/model: "gemma-4-31B-it"
             ai.gke.io/inference-server: "vllm"
         spec:
           serveConfigV2: |
             http_options:
               host: 0.0.0.0
               port: 8000
             applications:
               - name: llm
                 import_path: ai-ml.gke-ray.rayserve.llm.tpu.serve_tpu_multihost:deployment
                 runtime_env:
                   working_dir: "https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/archive/main.zip"
                   env_vars:
                     # Use local disk to prevent multi-host GCSFuse race conditions
                     VLLM_XLA_CACHE_PATH: "/tmp/vllm_xla_cache"
           rayClusterConfig:
             headGroupSpec:
               rayStartParams: {}
               template:
                 metadata:
                   annotations:
                     gke-gcsfuse/volumes: "true"
                     gke-gcsfuse/cpu-limit: "0"
                     gke-gcsfuse/memory-limit: "0"
                     gke-gcsfuse/ephemeral-storage-limit: "0"
                 spec:
                   serviceAccountName: $KSA_NAME
                   containers:
                   - name: ray-head
                     image: $CUSTOM_IMAGE_URI
                     imagePullPolicy: Always
                     ports:
                     - containerPort: 6379
                       name: gcs
                     - containerPort: 8265
                       name: dashboard
                     - containerPort: 10001
                       name: client
                     - containerPort: 8000
                       name: serve
                     resources:
                       limits:
                         cpu: "2"
                         memory: 16Gi
                       requests:
                         cpu: "2"
                         memory: 16Gi
                     volumeMounts:
                     - name: dshm
                       mountPath: /dev/shm
                     - name: gcs-fuse-csi-ephemeral
                       mountPath: /data
                   volumes:
                   - name: dshm
                     emptyDir:
                       medium: Memory
                   - name: gke-gcsfuse-cache
                     emptyDir:
                       medium: Memory
                   - name: gcs-fuse-csi-ephemeral
                     csi:
                       driver: gcsfuse.csi.storage.gke.io
                       volumeAttributes:
                         bucketName: $GS_BUCKET
                         mountOptions: "implicit-dirs"
             workerGroupSpecs:
             - groupName: tpu-group
               replicas: 1
               minReplicas: 1
               maxReplicas: 1
               numOfHosts: 4
               rayStartParams: {}
               template:
                 metadata:
                   annotations:
                     gke-gcsfuse/volumes: "true"
                     gke-gcsfuse/cpu-limit: "0"
                     gke-gcsfuse/memory-limit: "0"
                     gke-gcsfuse/ephemeral-storage-limit: "0"
                 spec:
                   serviceAccountName: $KSA_NAME
                   containers:
                     - name: ray-worker
                       image: $CUSTOM_IMAGE_URI
                       imagePullPolicy: Always
                       resources:
                         limits:
                           cpu: "20"
                           google.com/tpu: "4"
                           memory: 200Gi
                         requests:
                           cpu: "20"
                           google.com/tpu: "4"
                           memory: 200Gi
                         claims:
                         - name: netdev
                       env:
                         - name: HF_HOME
                           value: "/data/huggingface"
                         - name: HF_TOKEN
                           valueFrom:
                             secretKeyRef:
                               name: hf-secret
                               key: hf_api_token
                         - name: JAX_PLATFORMS
                           value: "tpu,cpu"
                         - name: NODE_IP
                           valueFrom:
                             fieldRef:
                               fieldPath: status.hostIP
                         - name: VBAR_CONTROL_SERVICE_URL
                           value: $(NODE_IP):8353
                         - name: TPU_MULTIHOST_BACKEND
                           value: "ray"
                         - name: TPU_BACKEND_TYPE
                           value: "jax"
                         - name: ENABLE_PJRT_COMPATIBILITY
                           value: "true"
                       volumeMounts:
                       - name: dshm
                         mountPath: /dev/shm
                       - name: gcs-fuse-csi-ephemeral
                         mountPath: /data
                   volumes:
                   - name: dshm
                     emptyDir:
                       medium: Memory
                   - name: gke-gcsfuse-cache
                     emptyDir:
                       medium: Memory
                   - name: gcs-fuse-csi-ephemeral
                     csi:
                       driver: gcsfuse.csi.storage.gke.io
                       volumeAttributes:
                         bucketName: $GS_BUCKET
                         mountOptions: "implicit-dirs"
                   resourceClaims:
                     - name: netdev
                       resourceClaimTemplateName: all-netdev
                   nodeSelector:
                     cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                     cloud.google.com/gke-tpu-topology: 4x4

  4. Deploy the service by using the manifest:

### Autopilot

     1. To deploy the service in an Autopilot cluster, you must first download the manifest and edit it locally to add the opt-in `ComputeClass` `nodeSelector`, which is required for DRANET networking on Autopilot:
            
            curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/kubernetes-engine-samples/main/ai-ml/gke-ray/rayserve/llm/tpu/ray-service.tpu-v6e-multihost.yaml
            

     2. Add the label under the `nodeSelector` field so that it looks like this:
            
            nodeSelector:
              cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
              cloud.google.com/gke-tpu-topology: 4x4
              cloud.google.com/compute-class: dranet-compute-class
            

     3. Then, deploy the service by using the modified local manifest:
            
            envsubst < ray-service.tpu-v6e-multihost.yaml | kubectl apply -f -
            

### Standard

To deploy the service in a Standard cluster, deploy the manifest directly from the repository:
    
    envsubst < ai-ml/gke-ray/rayserve/llm/tpu/ray-service.tpu-v6e-multihost.yaml | kubectl apply -f -
    




### Verification

**Note:** With multi-host TPU topologies, only the TPU coordinator node runs the serving replica. It is expected behavior for the `:8000/healthz` probes on the other worker Pods in the slice to fail. Avoid using individual Pod readiness to determine Serve deployment health. Instead, wait for the overall `RayService` status to become `ready` before sending prompt requests.

  1. Wait for the RayService to be available:
         
         kubectl wait --for=condition=Ready --timeout=1800s rayservice/vllm-tpu-multihost
         

  2. To confirm the model loaded successfully, view the logs from the Ray head Pod:
         
         kubectl logs -f -l ray.io/node-type=head -c ray-head
         




## Serve the model

In this section, you interact with the model. Make sure the model is fully downloaded before proceeding.

### Set up port forwarding

Set up port forwarding to the model by running the following command:
    
    
    kubectl port-forward svc/vllm-tpu-multihost-head-svc 8000:8000 2>&1 >/dev/null &
    

### Interact with the model using curl

This section shows how you can perform a basic smoke test to verify your deployed Gemma 4 model.

In a new terminal session, use `curl` to chat with your model:
    
    
    curl -X POST http://127.0.0.1:8000/v1/chat/completions \
        -H "Content-Type: application/json" \
        -d '{
            "model": "google/gemma-4-31B-it",
            "messages": [
                {
                  "role": "user",
                  "content": "Why is GKE managed DRANET preferred for multi-host TPU networking?"
                }
            ],
            "max_tokens": 256
        }'
    

The output looks similar to the following:
    
    
    {
      "id": "chatcmpl-392692d3-5325-4832-a3a3-0b084c1045b0",
      "object": "chat.completion",
      "created": 1779883255,
      "model": "google/gemma-4-31B-it",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "To understand why GKE-managed **DRANET** (Distributed RANET) is preferred for multi-host TPU networking, it is first necessary to understand the fundamental challenge of TPU pods: **the need for massive, low-latency, all-to-all communication.**\n\nWhen you scale a model across multiple TPU hosts (multi-host), the hosts must synchronize gradients and weights constantly. Standard TCP/IP networking introduces too much overhead (latency and CPU jitter) for these operations.\n\nHere is the detailed breakdown of why GKE-managed DRANET is the preferred architecture:\n\n### 1. Bypassing the Kernel (Zero-Copy Networking)\nStandard networking requires the operating system kernel to handle packets, moving data from the network card to kernel space and then to user space.\n*   **The DRANET Advantage:** DRANET implements a specialized networking stack that allows for **Kernel Bypass**. It enables the TPU hardware/drivers to write data directly into the memory of the destination host. This reduces latency and eliminates the CPU overhead associated with processing network interrupts.\n\n### 2. High-Bandwidth, Low-Latency Interconnect\nMulti-host TPU training relies on a specialized topology (like a 2D or 3D"
          },
          "finish_reason": "length"
        }
      ]
    }
    

**Success:** You've successfully served Gemma by using TPUs on GKE with Ray LLM. You can now interact with the model.

## (Optional) Interact with the model through a Gradio chat interface

In this section, you build a web chat application that lets you interact with your instruction tuned model.

Gradio is a Python library that has a `ChatInterface` wrapper that creates user interfaces for chatbots.

### Deploy the chat interface

The manifest for the chat interface is available in the repository. Review the manifest configuration:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: gradio
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
            image: us-docker.pkg.dev/google-samples/containers/gke/gradio-app:v1.0.7
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
              value: "http://vllm-tpu-multihost-serve-svc:8000"
            - name: LLM_ENGINE
              value: "openai-chat"
            - name: MODEL_ID
              value: "google/gemma-4-31B-it"
            - name: DISABLE_SYSTEM_MESSAGE
              value: "true"
            ports:
            - containerPort: 7860
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: gradio
    spec:
      selector:
        app: gradio
      ports:
      - protocol: TCP
        port: 8080
        targetPort: 7860
      type: ClusterIP

Apply the manifest:
    
    
    kubectl apply -f ai-ml/gke-ray/rayserve/llm/tpu/components/gradio.yaml
    

Wait for the deployment to be available:
    
    
    kubectl wait --for=condition=Available --timeout=900s deployment/gradio
    

### Use the chat interface

In Cloud Shell, run the following command:
    
    
    kubectl port-forward service/gradio 8080:8080
    

This creates a port forward from Cloud Shell to the Gradio service.

Click the **Web Preview** icon ![Web Preview button](https://docs.cloud.google.com/static/kubernetes-engine/images/web-preview.png) which can be found on the top right of the Cloud Shell taskbar. Click **Preview on Port 8080**. A new tab opens in your browser.

Interact with Gemma using the Gradio chat interface. Add a prompt and click **Submit**.

## Observe model performance

To view the dashboards for observability metrics of a model running on KubeRay, you can use the dedicated Ray on GKE dashboards.

For detailed instructions on configuring your cluster and accessing the observability dashboards, see [Collect and view logs and metrics for RayClusters on Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/collect-view-logs-metrics).

### Access the Ray Dashboard

To inspect the status of your Ray actors, view detailed application logs, and monitor node-level utilization natively in Ray, you can access the Ray Dashboard.

  1. Port-forward the Ray head node service to your local machine:
         
         kubectl port-forward svc/vllm-tpu-multihost-head-svc 8265:8265
         

  2. Open your browser and navigate to `http://localhost:8265`. If you are using Cloud Shell, click the **Web Preview** button and select **Preview on port 8265**.

  3. To view your vLLM deployments, model replica health, and query latencies, click the **Serve** tab.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete the resources:

  1. Delete the RayService:
         
         kubectl delete rayservice vllm-tpu-multihost
         

  2. Delete the GKE cluster:
         
         gcloud container clusters delete ${CLUSTER_NAME} --zone=${ZONE}
         




## What's next

  * Learn about [Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html).
  * Learn how to [serve vLLM on GKE with TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu).
  * Learn more [about TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
