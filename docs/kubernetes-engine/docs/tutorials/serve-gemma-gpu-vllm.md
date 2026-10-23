---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm/
title: Serve Gemma open models using GPUs on GKE with vLLM \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:12.891132+00:00
---

# Serve Gemma open models using GPUs on GKE with vLLM  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Serve Gemma open models using GPUs on GKE with vLLM Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

To serve [Gemma 4](https://ai.google.dev/gemma/docs/core) large language models (LLMs) on Google Kubernetes Engine (GKE) with [vLLM](https://github.com/vllm-project/vllm) framework using GPUs, you must provision a GKE cluster with supported accelerators, such as NVIDIA B200, H100, RTX Pro 6000, or L4 GPUs.

To obtain the Gemma 4 model weights, you can configure the prebuilt vLLM container to download them from the Hugging Face repository. Alternatively, the container can load model weights from existing persistent storage—such as by caching your Cloud Storage model buckets on a Google Cloud Managed Lustre instance.

Once the weights are loaded, the vLLM container exposes an OpenAI-compatible API endpoint for high-throughput inference.

**Tip:** For production deployments on GKE, we strongly recommend using [Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart) to get tailored best practices and configurations for your model inference.

This tutorial is intended for Machine learning (ML) engineers, Platform admins and operators, and for Data and AI specialists who are interested in using Kubernetes container orchestration capabilities for serving AI/ML workloads on H200, H100, A100, and L4 GPU hardware. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

If you need a unified managed AI platform that's designed to rapidly build and serve ML models cost effectively, we recommend that you try our [Vertex AI](https://docs.cloud.google.com/vertex-ai) deployment solution.

Before reading this page, ensure that you're familiar with the following:

  * [Autopilot mode and Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [Current GPU version availability](https://docs.cloud.google.com/compute/docs/gpus)
  * [GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)



## Background

This section describes the key technologies used in this guide. 

### GPUs

GPUs let you accelerate specific workloads running on your nodes, such as machine learning and data processing. GKE provides a range of machine type options for node configuration, including machine types with NVIDIA H200, H100, L4, and A100 GPUs.

### vLLM

vLLM is a highly optimized open source LLM serving framework that can increase serving throughput on GPUs, with features such as the following:

  * Optimized transformer implementation with [PagedAttention](https://huggingface.co/docs/text-generation-inference/en/conceptual/paged_attention)
  * Continuous batching to improve the overall serving throughput
  * Tensor parallelism and distributed serving on multiple GPUs



For more information, refer to the [vLLM documentation](https://docs.vllm.ai/en/latest/).

**Note:** To serve Gemma 4 on TPUs, use the [`vllm-tpu:gemma4`](https://hub.docker.com/r/vllm/vllm-tpu/tags) Docker images and follow the vision and text recipes for [TPU Trillium (v6e)](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/inference/trillium/vLLM/Gemma4) and [Ironwood (TPU7x)](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/inference/ironwood/vLLM/Gemma4).

## Objectives

This tutorial provides a foundation for understanding and exploring practical LLM deployment for inference in a managed Kubernetes environment.

  1. Prepare your environment with a GKE cluster in Autopilot or Standard mode.
  2. Deploy a vLLM container to your cluster.
  3. Use vLLM to serve the Gemma 4 model through curl and a web chat interface.



## Before you begin

  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  * Make sure that you have the following role or roles on the project: roles/container.admin, roles/iam.serviceAccountAdmin 

#### Check for the roles

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
    2. Select the project. 
    3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

    4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
    2. Select the project. 
    3. Click person_add **Grant access**. 
    4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

    5. Click **Select a role** , then search for the role. 
    6. To grant additional roles, click add **Add another role** and add each additional role. 
    7. Click **Save**. 


  * Ensure your project has sufficient quota for L4 GPUs. For more information, see [About GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#gpu-quota) and [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).



### Prepare your environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) and [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To set up your environment with Cloud Shell, follow these steps:

  1. In the Google Cloud console, launch a Cloud Shell session by clicking ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** in the [Google Cloud console](http://console.cloud.google.com). This launches a session in the bottom pane of Google Cloud console.

  2. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         gcloud config set billing/quota_project PROJECT_ID
         export PROJECT_ID=$(gcloud config get project)
         export REGION=REGION
         export ZONE=ZONE
         export CLUSTER_NAME=CLUSTER_NAME
         

Replace the following values:

     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `REGION`: a region that supports the accelerator type you want to use, for example, `us-central1` for L4 GPU. You can find [which region has which GPUs available](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `ZONE`: a zone that supports the accelerator type you want to use, for example, `us-central1-b` and `us-central1-f` for RTX PRO 6000 GPU. You can find [which zone has which GPUs available](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `CLUSTER_NAME`: the name of your cluster.



### Create and configure Google Cloud resources

Follow these instructions to create the required resources.

**Note:** You might need to create a capacity reservation to use of some accelerators. To learn how to reserve and consume reserved resources, see [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).

### Create a GKE cluster and node pool

You can serve Gemma on GPUs in a GKE Autopilot or Standard cluster. We recommend that you use a Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot

In Cloud Shell, run the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --project=PROJECT_ID \
        --location=CONTROL_PLANE_LOCATION \
        --release-channel=rapid
    

Replace the following values:

  * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region that supports the accelerator type you want to use, for example, `us-central1` for L4 GPU.
  * `CLUSTER_NAME`: the name of your cluster.



GKE creates an Autopilot cluster with CPU and GPU nodes as requested by the deployed workloads.

### Standard

  1. In Cloud Shell, run the following command to create a Standard cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --project=PROJECT_ID \
             --location=CONTROL_PLANE_LOCATION \
             --workload-pool=PROJECT_ID.svc.id.goog \
             --release-channel=rapid \
             --num-nodes=1
         

Replace the following values:

     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region that supports the accelerator type you want to use, for example, `us-central1` for L4 GPU.
     * `CLUSTER_NAME`: the name of your cluster.

The cluster creation might take several minutes.

  2. To create a [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) for your cluster with the appropriate disk size, run the following command:
         
         gcloud container node-pools create gpupool \
               --accelerator type=nvidia-rtx-pro-6000,count=1,gpu-driver-version=latest \
               --project=PROJECT_ID \
               --location=REGION \
               --node-locations=ZONE \
               --cluster=CLUSTER_NAME \
               --machine-type=g4-standard-48 \
               --num-nodes=1
         

GKE creates a single node pool containing an RTX PRO. 6000 GPU for each node.




## Deploy Gemma 4 models on vLLM using Hugging Face weights

To deploy Gemma 4 models using Hugging Face weights, apply a Kubernetes Deployment manifest for your selected model size. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster.. 

### Procedure

Applying this manifest pulls the vLLM container image, requests an NVIDIA GPU, and automatically downloads the weights from Hugging Face to start the vLLM inference engine.

### Gemma 4 E2B-it

Follow these instructions to deploy the Gemma 4 E2B instruction tuned model (text-only input).

  1. Create the following `vllm-4-e2b-it.yaml` manifest:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: vllm-gemma-deployment
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: gemma-server
           template:
             metadata:
               labels:
                 app: gemma-server
                 ai.gke.io/model: gemma-4-e2b-it
                 ai.gke.io/inference-server: vllm
                 examples.ai.gke.io/source: user-guide
             spec:
               containers:
               - name: inference-server
                 image: us-docker.pkg.dev/vertex-ai/vertex-vision-model-garden-dockers/pytorch-vllm-serve:gemma4
                 resources:
                   requests:
                     cpu: "2"
                     memory: "10Gi"
                     ephemeral-storage: "10Gi"
                     nvidia.com/gpu: "1"
                   limits:
                     cpu: "2"
                     memory: "10Gi"
                     ephemeral-storage: "10Gi"
                     nvidia.com/gpu: "1"
                 command: ["python3", "-m", "vllm.entrypoints.api_server"]
                 args:
                   - --model=$(MODEL_ID)
                   - --host=0.0.0.0
                   - --port=8000
                   - --tensor-parallel-size=1
                   - --enable-log-requests
                   - --enable-chunked-prefill
                   - --enable-prefix-caching
                   - --enable-auto-tool-choice
                   - --generation-config=auto
                   - --tool-call-parser=gemma4
                   - --dtype=bfloat16
                   - --max-num-seqs=16
                   - --max-model-len=32768
                   - --gpu-memory-utilization=0.95
                   - --reasoning-parser=gemma4
                   - --trust-remote-code
                 env:
                 - name: LD_LIBRARY_PATH
                   value: ${LD_LIBRARY_PATH}:/usr/local/nvidia/lib64
                 - name: MODEL_ID
                   value: google/gemma-4-E2B-it
                 volumeMounts:
                 - mountPath: /dev/shm
                   name: dshm
               volumes:
               - name: dshm
                 emptyDir:
                     medium: Memory
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-rtx-pro-6000
                 cloud.google.com/gke-gpu-driver-version: latest
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: llm-service
         spec:
           selector:
             app: gemma-server
           type: ClusterIP
           ports:
             - protocol: TCP
               port: 8000
               targetPort: 8000
         

  2. Apply the manifest:
         
         kubectl apply -f vllm-4-e2b-it.yaml
         




### Gemma 4 E4B-it

Follow these instructions to deploy the Gemma 4 E4B instruction tuned model.

  1. Create the following `vllm-4-e4b-it.yaml` manifest:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: vllm-gemma-deployment
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: gemma-server
           template:
             metadata:
               labels:
                 app: gemma-server
                 ai.gke.io/model: gemma-4-e4b-it
                 ai.gke.io/inference-server: vllm
                 examples.ai.gke.io/source: user-guide
             spec:
               containers:
               - name: inference-server
                 image: us-docker.pkg.dev/vertex-ai/vertex-vision-model-garden-dockers/pytorch-vllm-serve:gemma4
                 resources:
                   requests:
                     cpu: "4"
                     memory: "20Gi"
                     ephemeral-storage: "20Gi"
                     nvidia.com/gpu: "1"
                   limits:
                     cpu: "4"
                     memory: "20Gi"
                     ephemeral-storage: "20Gi"
                     nvidia.com/gpu: "1"
                 command: ["python3", "-m", "vllm.entrypoints.api_server"]
                 args:
                   - --model=$(MODEL_ID)
                   - --host=0.0.0.0
                   - --port=8000
                   - --tensor-parallel-size=1
                   - --enable-log-requests
                   - --enable-chunked-prefill
                   - --enable-prefix-caching
                   - --enable-auto-tool-choice
                   - --generation-config=auto
                   - --tool-call-parser=gemma4
                   - --dtype=bfloat16
                   - --max-num-seqs=16
                   - --max-model-len=32768
                   - --gpu-memory-utilization=0.95
                   - --reasoning-parser=gemma4
                   - --trust-remote-code
                 env:
                 - name: LD_LIBRARY_PATH
                   value: ${LD_LIBRARY_PATH}:/usr/local/nvidia/lib64
                 - name: MODEL_ID
                   value: google/gemma-4-E4b-it
                 volumeMounts:
                 - mountPath: /dev/shm
                   name: dshm
               volumes:
               - name: dshm
                 emptyDir:
                     medium: Memory
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-rtx-pro-6000
                 cloud.google.com/gke-gpu-driver-version: latest
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: llm-service
         spec:
           selector:
             app: gemma-server
           type: ClusterIP
           ports:
             - protocol: TCP
               port: 8000
               targetPort: 8000
         

  2. Apply the manifest:
         
         kubectl apply -f vllm-4-E4b-it.yaml
         

In our example, we limit the context window by 32 K using vLLM option `--max-model-len=32768`. If you want a larger context window size (up to 128 K), adjust your manifest and the node-pool configuration with more GPU capacity.




### Gemma 4 26B-A4B-it

Follow these instructions to deploy the Gemma 4 26B-A4B instruction tuned model.

  1. Create the following `vllm-4-26b-a4b-it.yaml` manifest:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: vllm-gemma-deployment
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: gemma-server
           template:
             metadata:
               labels:
                 app: gemma-server
                 ai.gke.io/model: gemma-4-26b-a4b-it
                 ai.gke.io/inference-server: vllm
                 examples.ai.gke.io/source: user-guide
             spec:
               containers:
               - name: inference-server
                 image: us-docker.pkg.dev/vertex-ai/vertex-vision-model-garden-dockers/pytorch-vllm-serve:gemma4
                 resources:
                   requests:
                     cpu: "20"
                     memory: "80Gi"
                     ephemeral-storage: "80Gi"
                     nvidia.com/gpu: "1"
                   limits:
                     cpu: "20"
                     memory: "80Gi"
                     ephemeral-storage: "80Gi"
                     nvidia.com/gpu: "1"
                 command: ["python3", "-m", "vllm.entrypoints.api_server"]
                 args:
                   - --model=$(MODEL_ID)
                   - --host=0.0.0.0
                   - --port=8000
                   - --tensor-parallel-size=1
                   - --enable-log-requests
                   - --enable-chunked-prefill
                   - --enable-prefix-caching
                   - --enable-auto-tool-choice
                   - --generation-config=auto
                   - --tool-call-parser=gemma4
                   - --dtype=bfloat16
                   - --max-num-seqs=16
                   - --max-model-len=16384
                   - --gpu-memory-utilization=0.95
                   - --reasoning-parser=gemma4
                   - --trust-remote-code
                 env:
                 - name: LD_LIBRARY_PATH
                   value: ${LD_LIBRARY_PATH}:/usr/local/nvidia/lib64
                 - name: MODEL_ID
                   value: google/gemma-4-26B-A4B-it
                 volumeMounts:
                 - mountPath: /dev/shm
                   name: dshm
               volumes:
               - name: dshm
                 emptyDir:
                     medium: Memory
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-rtx-pro-6000
                 cloud.google.com/gke-gpu-driver-version: latest
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: llm-service
         spec:
           selector:
             app: gemma-server
           type: ClusterIP
           ports:
             - protocol: TCP
               port: 8000
               targetPort: 8000
         

  2. Apply the manifest:
         
         kubectl apply -f vllm-4-26b-a4b-it.yaml
         

In our example, we limit the context window size by 16 K using vLLM option `--max-model-len=16384`. If you want a larger context window size (up to 128 K), adjust your manifest and node-pool configuration with more GPU capacity.




### Gemma 4 31B-it

Follow these instructions to deploy the Gemma 4 31B instruction tuned model.

  1. Create the following `vllm-4-31b-it.yaml` manifest:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: vllm-gemma-deployment
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: gemma-server
           template:
             metadata:
               labels:
                 app: gemma-server
                 ai.gke.io/model: gemma-4-31b-it
                 ai.gke.io/inference-server: vllm
                 examples.ai.gke.io/source: user-guide
             spec:
               containers:
               - name: inference-server
                 image: us-docker.pkg.dev/vertex-ai/vertex-vision-model-garden-dockers/pytorch-vllm-serve:gemma4
                 resources:
                   requests:
                     cpu: "22"
                     memory: "100Gi"
                     ephemeral-storage: "80Gi"
                     nvidia.com/gpu: "1"
                   limits:
                     cpu: "22"
                     memory: "100Gi"
                     ephemeral-storage: "80Gi"
                     nvidia.com/gpu: "1"
                 command: ["python3", "-m", "vllm.entrypoints.api_server"]
                 args:
                   - --model=$(MODEL_ID)
                   - --host=0.0.0.0
                   - --port=8000
                   - --tensor-parallel-size=1
                   - --enable-log-requests
                   - --enable-chunked-prefill
                   - --enable-prefix-caching
                   - --enable-auto-tool-choice
                   - --generation-config=auto
                   - --tool-call-parser=gemma4
                   - --dtype=bfloat16
                   - --max-num-seqs=16
                   - --max-model-len=16384
                   - --gpu-memory-utilization=0.95
                   - --reasoning-parser=gemma4
                   - --trust-remote-code
                 env:
                 - name: LD_LIBRARY_PATH
                   value: ${LD_LIBRARY_PATH}:/usr/local/nvidia/lib64
                 - name: MODEL_ID
                   value: google/gemma-4-31B-it
                 volumeMounts:
                 - mountPath: /dev/shm
                   name: dshm
               volumes:
               - name: dshm
                 emptyDir:
                     medium: Memory
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-rtx-pro-6000
                 cloud.google.com/gke-gpu-driver-version: latest
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: llm-service
         spec:
           selector:
             app: gemma-server
           type: ClusterIP
           ports:
             - protocol: TCP
               port: 8000
               targetPort: 8000
         

  2. Apply the manifest:
         
         kubectl apply -f vllm-4-31b-it.yaml
         

In our example, we limit the context window size by 16 K using vLLM option `--max-model-len=16384`. If you want a larger context window size (up to 128K), adjust your manifest and the node-poolconfiguration with more GPU capacity.




### Verification

  1. Wait for the Deployment to be available:
         
         kubectl wait --for=condition=Available --timeout=1800s deployment/vllm-gemma-deployment
         

  2. View the logs from the running Deployment:
         
         kubectl logs -f -l app=gemma-server
         

The Deployment resource downloads the Gemma model data. This process can take a few minutes. The output is similar to the following:
         
         ...
           ...
           (APIServer pid=1) INFO:     Started server process [1]
           (APIServer pid=1) INFO:     Waiting for application startup.
           (APIServer pid=1) INFO:     Application startup complete.
         




After the Hugging Face deployment is available, set up port forwarding to interact with the model.

## Deploy fine-tuned Gemma from Managed Lustre

To serve a finetuned Gemma model (such as Gemma 3 27B) that is already stored on a Google Cloud Managed Lustre instance, you must mount the corresponding `PersistentVolumeClaim` (PVC) to the vLLM container.

### Prerequisites

Ensure you have an existing PVC in your GKE cluster that connects to your Lustre instance. In this example, the PVC is named `gemma-lustre-pvc`.

To learn how to create a PVC and PersistentVolume (PV) for an existing instance, see [Access an existing Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-existing-instance#access).

### Procedure

  1. Save the following YAML manifest as `vllm-lustre-gemma.yaml`. In this example, the Deployment mounts the Lustre PVC to `/data` and instructs vLLM to load the model weights from that local path.
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: vllm-gemma-lustre
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: gemma-server
           template:
             metadata:
               labels:
                 app: gemma-server
             spec:
               containers:
               - name: vllm
                 image: vllm/vllm-openai:latest
                 command: ["python3", "-m", "vllm.entrypoints.openai.api_server"]
                 args:
                 - --model=/data/gemma-3-27b
                 - --tensor-parallel-size=1
                 resources:
                   limits:
                     nvidia.com/gpu: "1"
                 volumeMounts:
                 - name: model-weights
                   mountPath: /data
               volumes:
               - name: model-weights
                 persistentVolumeClaim:
                   claimName: gemma-lustre-pvc
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-l4
                 cloud.google.com/gke-gpu-driver-version: latest
         

  2. Apply the manifest to the GKE cluster:
         
         kubectl apply -f vllm-lustre-gemma.yaml
         




### Verification

To confirm the model loaded successfully from the Lustre volume, check the Pod logs for the vLLM startup sequence:
    
    
    kubectl logs -l app=gemma-server
    

## Serve the model

In this section, you interact with the model. Make sure the model is fully downloaded before proceeding.

### Set up port forwarding

Run the following command to set up port forwarding to the model:
    
    
    kubectl port-forward service/llm-service 8000:8000
    

The output is similar to the following:
    
    
    Forwarding from 127.0.0.1:8000 -> 8000
    

### Interact with the model using curl

This section shows how you can perform a basic smoke test to verify your deployed Gemma 4 instruction-tuned models. For other models, replace `gemma-4-e4b-it` with the name of the respective model.

This example shows how to test the Gemma 4 E4B instruction tuned model with text-only input.

In a new terminal session, use `curl` to chat with your model:
    
    
    curl http://127.0.0.1:8000/v1/chat/completions \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{
        "model": "google/gemma-4-26B-A4B-it",
        "messages": [
            {
              "role": "user",
              "content": "Why is the sky blue?"
            }
        ],
        "chat_template_kwargs": {
             "enable_thinking": true
        },
        "skip_special_tokens": false
    }'
    

The output looks similar to the following:
    
    
    {
      "id": "chatcmpl-be75ccfcbdf753d1",
      "object": "chat.completion",
      "created": 1775006187,
      "model": "google/gemma-4-26B-A4B-it",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "The short answer is a phenomenon called **Rayleigh scattering**.\n\nTo understand how it works, you have to look at three things: sunlight, the Earth's atmosphere, and how light travels.\n\n### 1. Sunlight is a Rainbow\nAlthough sunlight looks white to us, it is actually made up of all the colors of the rainbow (red, orange, yellow, green, blue, indigo, and violet). Light travels as **waves**, and each color has a different wavelength:\n*   **Red light** travels in long, lazy, wide waves.\n*   **Blue and violet light** travel in short, choppy, tight waves.\n\n### 2. The Atmosphere is an Obstacle Course\nEarth's atmosphere is filled with gases (mostly nitrogen and oxygen). As sunlight travels through the atmosphere, it strikes the molecules of these gases. \n\nBecause the gas molecules are very small, they affect the colors differently based on their wavelength:\n*   The **long waves** (reds and yellows) pass through the atmosphere mostly straight, without hitting much. They are like large ocean waves that roll right over small pebbles.\n*   The **short waves** (blues and violets) strike the gas molecules and get scattered in every direction. They are like small ripples that hit a pebble and splash everywhere.\n\nBecause this blue light is being scattered in every direction by the air, when you look up, your eyes are catching that scattered blue light coming from every part of the sky.\n\n### 3. Why isn't the sky violet?\nIf violet light has an even shorter wavelength than blue light, you might wonder why the sky doesn't look purple. There are two main reasons:\n1.  **The Sun's output:** The Sun emits much more blue light than violet light.\n2.  **Human Biology:** Human eyes are much more sensitive to blue than to violet. Our eyes interpret the scatter of mixed blue and violet light simply as pale blue.\n\n---\n\n### Bonus: Why are sunsets red?\nWhen the sun is setting, it is much lower on the horizon. This means the sunlight has to travel through a much **thicker** layer of the atmosphere to reach your eyes. \n\nBy the time the light gets to you, the blue light has been scattered away completely로. Only the long-wavelength colors—the reds, oranges, and pinks—are able to make it through that thick layer of air without being scattered away, creating the beautiful colors of a sunset.",
            "refusal": null,
            "annotations": null,
            "audio": null,
            "function_call": null,
            "tool_calls": [],
            "reasoning": "\"Why is the sky blue?\"\nScience/Physics (Atmospheric scattering).\nExplain the phenomenon clearly, accurately, and engagingly.\n\n    *   Sunlight (white light) is made of a spectrum of colors (ROYGBIV).\n    *   Earth's atmosphere is filled with gases (nitrogen, oxygen) and particles.\n    *   Rayleigh Scattering: Shorter wavelengths (blue/violet) scatter more easily than longer wavelengths (red/yellow) when hitting small gas molecules.\n    *   The human eye's sensitivity: Why isn't it violet?\n\n    A good scientific explanation should follow a logical flow:\n    *   *Direct Answer:* The core mechanism (Rayleigh Scattering).\n    *   *The Components:* Sunlight and the Atmosphere.\n    *   *The Mechanism:* How light interacts with gas molecules.\n    *   *The Wavelength Factor:* Comparing colors.\n    *   *The \"Wait, why not violet?\" question:* Addressing human perception.\n    *   *Bonus/Related concept:* Why sunsets are red.\n\n        *   Use the term **Rayleigh Scattering**.\n        *   Summarize: Its how sunlight interacts with the Earth's atmosphere.\n\n        *   Sunlight looks white, but it's actually a mix of all colors (the rainbow).\n        *   Each color travels as a different wavelength. Red = long/lazy waves; Blue/Violet = short/choppy waves.\n\n        *   The atmosphere is mostly Nitrogen and Oxygen.\n        *   When sunlight hits these tiny gas molecules, the light gets scattered in all directions.\n\n        *   Blue light travels in shorter, smaller waves.\n        *   Because these waves are small, they strike the gas molecules more frequently and get scattered more easily than the longer red/yellow waves.\n        *   Result: When you look up, your eyes are catching this \"scattered\" blue light coming from every direction.\n\n        *   *Technically*, violet light has an even shorter wavelength than blue, so it scatters *even more*. Why isn't the sky violet?\n        *   Two reasons: 1. The Sun emits more blue light than violet light. 2. Human eyes are much more sensitive to blue than violet.\n\n        *   Briefly mention sunsets to provide a complete picture.\n        *   At sunset, light travels through *more* atmosphere. The blue is scattered away completely, leaving only the long red/orange waves to reach your eyes.\n\n    *   *Tone Check:* Is it too academic? Use analogies (like waves in water or skipping stones) if needed, but keep it concise.\n    *   *Clarity:* Ensure the distinction between wavelength and scattering is clear."
          },
          "logprobs": null,
          "finish_reason": "stop",
          "stop_reason": 106,
          "token_ids": null
        }
      ],
      "service_tier": null,
      "system_fingerprint": null,
      "usage": {
        "prompt_tokens": 21,
        "total_tokens": 1122,
        "completion_tokens": 1101,
        "prompt_tokens_details": null
      },
      "prompt_logprobs": null,
      "prompt_token_ids": null,
      "kv_transfer_params": null
    }
    

**Success:** You've successfully served Gemma using GPUs on GKE with vLLM. You can now interact with the model.

### (Optional) Interact with the model through a Gradio chat interface

In this section, you build a web chat application that lets you interact with your instruction tuned model. For simplicity, this section describes only the testing approach using the 4B-it model.

[Gradio](https://github.com/gradio-app/gradio) is a Python library that has a `ChatInterface` wrapper that creates user interfaces for chatbots.

#### Deploy the chat interface

  1. In Cloud Shell, save the following manifest as `gradio.yaml`. Change `google/gemma-4-E4B-it` to the Gemma 4 model name you used in your deployment.
         
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
                   value: "http://llm-service:8000"
                 - name: LLM_ENGINE
                   value: "openai-chat"
                 - name: MODEL_ID
                   value: "google/gemma-4-E4B-it"
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
         

  2. Apply the manifest:
         
         kubectl apply -f gradio.yaml
         

  3. Wait for the deployment to be available:
         
         kubectl wait --for=condition=Available --timeout=900s deployment/gradio
         




#### Use the chat interface

  1. In Cloud Shell, run the following command:
         
         kubectl port-forward service/gradio 8080:8080
         

This creates a port forward from Cloud Shell to the Gradio service.

  2. Click the ![Web Preview icon](https://docs.cloud.google.com/static/shell/docs/images/web_preview.svg)**Web Preview** button which can be found on the top right of the Cloud Shell taskbar. Click **Preview on Port 8080**. A new tab opens in your browser.

  3. Interact with Gemma using the Gradio chat interface. Add a prompt and click **Submit**.




## Troubleshoot issues

  * If you get the message `Empty reply from server`, it's possible the container has not finished downloading the model data. Check the Pod's logs again for the `Connected` message which indicates that the model is ready to serve.
  * If you see `Connection refused`, verify that your port forwarding is active.



## Observe model performance

To view the dashboards for observability metrics of a model, follow these steps:

  1. In the Google Cloud console, go to the **Deployed Models** page.

[Go to Deployed Models](https://console.cloud.google.com/kubernetes/aiml/deployments/models)

  2. To view details about the specific deployment, including its metrics, logs, and dashboards, click the model name in the list.

  3. In the model details page, click the **Observability** tab to view the following dashboards. If prompted, click **Enable** to enable metrics collection for the cluster.

     * The **Infrastructure usage** dashboard displays utilization metrics.
     * The **DCGM** dashboard displays DCGM metrics.
     * If you are using vLLM, then the **Model performance** dashboard is available and displays metrics for the vLLM model performance.



You can also view metrics in the vLLM dashboard integration in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). These metrics are aggregated for all vLLM deployments with no pre-set filters

To use the dashboard in Cloud Monitoring, you must enable [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), which collects the metrics from vLLM, in your GKE cluster. vLLM exposes metrics in Prometheus format by default; you don't need to install an additional exporter. For information about using Google Cloud Managed Service for Prometheus to collect metrics from your model, see the [vLLM](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/vllm) observability guidance in the Cloud Monitoring documentation.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the deployed resources

To avoid incurring charges to your Google Cloud account for the resources that you created in this guide, run the following command:
    
    
    gcloud container clusters delete CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following values:

  * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.
  * `CLUSTER_NAME`: the name of your cluster.



## What's next

  * Learn more about [GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus).
  * Learn how to use Gemma with vLLM on other accelerators, including A100 and H100 GPUs, by [viewing the sample code in GitHub](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/llm-serving-gemma/vllm).
  * Learn how to [deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus).
  * Learn how to [deploy GPU workloads in Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus).
  * Explore the vLLM [GitHub repository](https://github.com/vllm-project/vllm) and [documentation](https://docs.vllm.ai/en/latest/).
  * Explore the [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden).
  * Discover how to run optimized AI/ML workloads with [GKE platform orchestration capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
