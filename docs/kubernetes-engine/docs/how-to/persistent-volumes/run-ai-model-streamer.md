---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/run-ai-model-streamer/
title: Accelerate model loading on GKE with Run:ai Model Streamer \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:51.307989+00:00
---

# Accelerate model loading on GKE with Run:ai Model Streamer  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/run-ai-model-streamer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Accelerate model loading on GKE with Run:ai Model Streamer Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to accelerate loading the large AI model weights from [Cloud Storage](https://docs.cloud.google.com/storage) by using [Run:ai Model Streamer](https://github.com/run-ai/runai-model-streamer/blob/master/docs/README.md) with the vLLM inference server on Google Kubernetes Engine (GKE).

The solution in this document assumes that you have your AI model and weights in `safetensors` format already loaded in a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets).

By adding the `--load-format=runai_streamer` flag to your vLLM deployment, you can use the Run:ai Model Streamer to improve model download efficiency for your AI workloads on GKE.

This document is intended for the following users:

  * Machine learning (ML) engineers who need to load large AI models from object storage into GPU/TPU nodes as quickly as possible.
  * Platform admins and operators who automate and optimize model serving infrastructure on GKE.
  * Cloud architects who evaluate specialized data loading tools for AI/ML workloads.



To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Overview

The solution described in this document uses three core components—Run:ai Model Streamer, vLLM, and the `safetensors` file format—to accelerate the process of loading model weights from Cloud Storage onto GPU or TPU nodes.

### Run:ai Model Streamer

[Run:ai Model Streamer](https://docs.vllm.ai/en/stable/models/extensions/runai_model_streamer.html) is an open-source Python SDK that speeds up loading large AI models onto accelerators. It streams model weights directly from storage, like Cloud Storage buckets, to your GPU or TPU memory. The model streamer is particularly suitable for accessing `safetensors` files located in Cloud Storage.

### safetensors

[`safetensors`](https://huggingface.co/docs/safetensors/index) is a file format to store tensors, the core data structures in AI models, in a way that enhances both security and speed. `safetensors` is designed as an alternative to Python's pickle format, and it enables fast loading times through a _zero-copy_ approach. This approach lets the tensors be directly accessible from the source without needing to load the entire file into the local memory first.

### vLLM

[vLLM](https://docs.vllm.ai/en/stable/index.html) is an open-source library for LLM inference and serving. It's a high-performance inference server that's optimized for rapidly loading large AI models. In this document, vLLM is the core engine that runs your AI model on GKE and handles incoming inference requests. Run:ai Model Streamer's built-in authentication support for Cloud Storage requires vLLM version 0.11.1 or later for GPUs, and 0.18.0 or later for TPUs.

## How Run:ai Model Streamer accelerates model loading

When you start an LLM-based AI application for inference, a significant delay often occurs before the model is ready to use. This delay, known as a _cold start_ , happens because the entire multi-gigabyte model file must be downloaded from a storage location, like a Cloud Storage bucket, to your machine's local disk. The file is then loaded into your accelerator's memory. During this loading period, the expensive accelerator is sitting idle, which is inefficient and costly.

Instead of the download-then-load process, the model streamer streams the model directly from your Cloud Storage to the GPU or TPU memory. The streamer uses a high-performance backend to read multiple parts of the model, called _tensors_ , in parallel. Reading tensors concurrently is significantly faster than loading the file sequentially.

### Architecture overview

The Run:ai Model Streamer integrates with vLLM on GKE to accelerate model loading by streaming model weights directly from Cloud Storage to accelerator memory, bypassing local disk.

The following diagram shows this architecture:

[ ![Architecture of Run:ai Model Streamer loading model weights from Cloud Storage to vLLM on GKE.](https://docs.cloud.google.com/static/kubernetes-engine/images/runai_model-streamer.png)](https://docs.cloud.google.com/static/kubernetes-engine/images/runai_model-streamer.png) Run:ai Model Streamer architecture with vLLM and Cloud Storage.

This architecture includes the following components and workflow:

  * **Cloud Storage bucket** : stores the AI model weights in `safetensors` format.
  * **GKE Pod with GPUs or TPUs** : runs the vLLM inference server.
  * **vLLM inference server** : configured with the `--load-format=runai_streamer` flag, which enables the model streamer functionality.
  * **Run:ai Model Streamer** : when vLLM starts, the model streamer reads model weights from the specified `gs://` path in the Cloud Storage bucket. Instead of downloading files to disk, it streams tensor data directly into the accelerator memory of the GKE Pod, where it's immediately available to vLLM for inference.
  * **Cloud Storage Rapid Cache (Optional)** : if enabled, Rapid Cache caches bucket data in the same zone as the GKE nodes, further accelerating data access for the streamer.



## Benefits

  * **Reduced cold start times:** the model streamer significantly reduces the time it takes for models to start. It loads the model weights up to six times faster compared to conventional methods. For more information, see [Run:ai Model Streamer benchmarks](https://github.com/run-ai/runai-model-streamer/blob/master/docs/src/benchmarks.md)
  * **Enhanced accelerator utilization:** by minimizing model loading delays, accelerators like GPUs and TPUs can dedicate more time to actual inference tasks, boosting overall efficiency and processing capacity.
  * **Streamlined workflow:** the solution described in this document integrates with GKE, enabling inference servers like vLLM or SGLang to directly access models in Cloud Storage buckets.



## Before you begin

Make sure to complete the following prerequisites.

### Select or create a project and enable the APIs

* Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
* In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

* [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

* Enable the Kubernetes Engine, Cloud Storage, Compute Engine, IAM APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,compute.googleapis.com,storage.googleapis.com,iam.googleapis.com)

* In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

* [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

* Enable the Kubernetes Engine, Cloud Storage, Compute Engine, IAM APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,compute.googleapis.com,storage.googleapis.com,iam.googleapis.com)

### Set up Cloud Shell

This document uses the Google Cloud CLI and `kubectl` commands to create and manage the resources required for this solution. You can run these commands in Cloud Shell by clicking **Activate Cloud Shell** at the top of the Google Cloud console.

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

Alternatively, you can [install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) in your local shell environment to run the commands. If you want to use a local shell terminal, run the `gcloud auth login` command to authenticate with Google Cloud.

### Grant IAM roles

Ensure that your Google Cloud account has the following [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles) on your project so you can create a GKE cluster and manage Cloud Storage:

  * `roles/container.admin`
  * `roles/storage.admin`



To grant these roles, run the following commands:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:$(gcloud config get-value account)" \
        --role="roles/container.admin"
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:$(gcloud config get-value account)" \
        --role="roles/storage.admin"
    

Replace `PROJECT_ID` with your project ID.

## Prepare your environment

This section guides you through setting up your GKE cluster and configuring permissions to access your model in Cloud Storage.

**Note:** You must have your AI model in `safetensors` format stored in a Cloud Storage bucket.

### Create a GKE cluster

The Run:ai Model Streamer can be used with both GKE Autopilot and Standard clusters. Choose the cluster mode that best suits your needs.

  1. Set variables for your project and cluster name:
         
         export PROJECT_ID=PROJECT_ID
         export CLUSTER_NAME=CLUSTER_NAME
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID. You can find your project ID by running the `gcloud config get-value project` command.
     * `CLUSTER_NAME`: The name of your cluster. For example, `run-ai-test`.
  2. Create either an Autopilot or a Standard cluster:

### Autopilot

Follow these steps to create a GKE Autopilot cluster:

     1. Set the region for your cluster:
            
            export REGION=REGION
            

Replace `REGION` with the region where you want to create your cluster. For optimal performance, use the same region as your Cloud Storage bucket.

     2. Create the cluster:
            
            gcloud container clusters create-auto $CLUSTER_NAME \
                --project=$PROJECT_ID \
                --location=$REGION
            

Autopilot clusters automatically provision nodes based on workload requirements. When you deploy the vLLM server in a later step, Autopilot will provision the GPU or TPU nodes if required. For more information, see [About node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning).

### Standard

Follow these steps to create a GKE Standard cluster:

     1. Set the zone for your cluster:
            
            export ZONE=ZONE
            

Replace `ZONE` with the zone where you want to create your cluster. For optimal performance, use a zone in the same region as your Cloud Storage bucket.

     2. Create the cluster:
            
            gcloud container clusters create $CLUSTER_NAME \
                --project=$PROJECT_ID \
                --zone=$ZONE \
                --workload-pool=$PROJECT_ID.svc.id.goog \
                --num-nodes=1
            




### Create a node pool

If you created a Standard cluster, you must create a node pool with GPUs or TPUs. Autopilot clusters automatically provision nodes based on workload requirements. Create a node pool based on the accelerator that you want to use:
    
    
    *   {GPU}
    
        Create a node pool with one G2 machine (NVIDIA L4 GPU):
    
        ```sh
        gcloud container node-pools create g2-gpu-pool \
            --cluster=$CLUSTER_NAME \
            --zone=$ZONE \
            --machine-type=g2-standard-16 \
            --num-nodes=1 \
            --accelerator=type=nvidia-l4
        ```
    
    *   {TPU}
    
        Create a node pool with TPU v7x nodes:
    
        ```sh
        gcloud container node-pools create tpu7x-pool \
            --cluster=$CLUSTER_NAME \
            --zone=$ZONE \
            --machine-type=tpu7x-standard-4t \
            --num-nodes=1
        ```
    

### Configure Workload Identity Federation for GKE

Configure Workload Identity Federation for GKE to allow your GKE workloads to securely access the model in your Cloud Storage bucket.

  1. Set variables for your Kubernetes service account and namespace:
         
         export KSA_NAME=KSA_NAME
         export NAMESPACE=NAMESPACE
         

Replace the following:

     * `NAMESPACE`: the namespace that you want your workloads to run on. Make sure to use the same namespace to create all the resources in this document.
     * `KSA_NAME`: the name of the Kubernetes service account that your Pod can use to authenticate to Google Cloud APIs.
  2. Create a Kubernetes namespace:
         
         kubectl create namespace $NAMESPACE
         

  3. Create a Kubernetes service account (KSA):
         
         kubectl create serviceaccount $KSA_NAME \
             --namespace=$NAMESPACE
         

**Caution:** To adhere to the principle of least privileges, avoid reusing this Kubernetes service account in other Pods within the same namespace. Any workload using this service account will unintentionally have access to the specified Cloud Storage bucket.
  4. Grant your KSA the necessary permissions:

     1. Set the environment variables:
            
            export BUCKET_NAME=BUCKET_NAME
            export PROJECT_ID=PROJECT_ID
            export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID \
                --format 'get(projectNumber)')
            

Replace the following:

        * `BUCKET_NAME`: the name of your Cloud Storage bucket that contains your `safetensors` files.
        * `PROJECT_ID`: your Google Cloud project ID.

The `PROJECT_NUMBER`, `PROJECT_ID`, `NAMESPACE`, and `KSA_NAME` will be used to construct the Workload Identity Federation for GKE principal identifier for your project in the following steps.

     2. Grant the `roles/storage.bucketViewer` role to your KSA to view objects in your Cloud Storage bucket:
            
            gcloud storage buckets add-iam-policy-binding gs://$BUCKET_NAME \
                --member="principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$PROJECT_ID.svc.id.goog/subject/ns/$NAMESPACE/sa/$KSA_NAME" \
                --role="roles/storage.bucketViewer"
            

     3. Grant the `roles/storage.objectUser` role to your KSA to read, write, and delete objects in your Cloud Storage bucket:
            
            gcloud storage buckets add-iam-policy-binding gs://$BUCKET_NAME \
                --member="principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$PROJECT_ID.svc.id.goog/subject/ns/$NAMESPACE/sa/$KSA_NAME" \
                --role="roles/storage.objectUser"
            




You have now set up a GKE cluster with GPUs or TPUs and configured Workload Identity Federation for GKE, granting a Kubernetes Service Account the necessary permissions to access your AI model in Cloud Storage. With the cluster and permissions in place, you are ready to deploy the vLLM inference server, which will use this service account to stream model weights with the Run:ai Model Streamer.

## Deploy vLLM with the Run:ai Model Streamer

Deploy a Pod that runs the vLLM OpenAI-compatible server, and is configured with the `--load-format=runai_streamer` flag to use the Run:ai Model Streamer. The vLLM version must be 0.11.1 or later for GPUs, and 0.18.0 or later for TPUs.

The following sample manifests show how to configure vLLM with the model streamer enabled for a small size model, like `gemma-2-9b-it`.

The `--model-loader-extra-config={"distributed":true}` flag enables distributed loading of model weights and is a recommended setting for improving model loading performance from object storage.

For more information, see [Tensor parallelism](https://huggingface.co/docs/text-generation-inference/en/conceptual/tensor_parallelism) and [Tunable parameters](https://docs.vllm.ai/en/latest/models/extensions/runai_model_streamer/#tunable-parameters).

  1. Select the sample manifest based on the accelerator that you want to use:

### GPU

The following sample manifest uses a single NVIDIA L4 GPU. If you're using a large model that requires multiple GPUs, increase the `--tensor-parallel-size` value to the required number of GPUs.

Save the following manifest as `vllm-deployment.yaml`. The manifest is designed for flexibility across both Autopilot and Standard clusters.
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: vllm-streamer-deployment
           namespace: NAMESPACE
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: vllm-streamer
           template:
             metadata:
               labels:
                 app: vllm-streamer
             spec:
               serviceAccountName: KSA_NAME
               containers:
                 - name: vllm-container
                   image: vllm/vllm-openai:v0.11.1
                   command:
                     - python3
                     - -m
                     - vllm.entrypoints.openai.api_server
                   args:
                     - --model=gs://BUCKET_NAME/PATH_TO_MODEL
                     - --load-format=runai_streamer
                     - --model-loader-extra-config={"distributed":true}
                     - --host=0.0.0.0
                     - --port=8000
                     - --disable-log-requests
                     - --tensor-parallel-size=1
                   ports:
                     - containerPort: 8000
                       name: api
                   # startupProbe allows for longer startup times for large models
                   startupProbe:
                     httpGet:
                       path: /health
                       port: 8000
                     failureThreshold: 60  # 60 * 10s = 10 minutes timeout
                     periodSeconds: 10
                     initialDelaySeconds: 30
                   readinessProbe:
                     httpGet:
                       path: /health
                       port: 8000
                     failureThreshold: 3
                     periodSeconds: 10
                   resources:
                     limits:
                       nvidia.com/gpu: "1"
                     requests:
                       nvidia.com/gpu: "1"
                   volumeMounts:
                   - mountPath: /dev/shm
                     name: dshm
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-l4
               volumes:
               - emptyDir:
                   medium: Memory
                 name: dshm
         

Replace the following:

     * `NAMESPACE`: your Kubernetes namespace.
     * `KSA_NAME`: your Kubernetes service account name.
     * `BUCKET_NAME`: your Cloud Storage bucket name.
     * `PATH_TO_MODEL`: the path to your model directory within the bucket, for example, `models/my-llama`.

### TPU

The following sample manifest uses TPU v7x nodes.

Save the following manifest as `vllm-deployment.yaml`.
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: tpu-vllm
      namespace: NAMESPACE
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: tpu-vllm
      template:
        metadata:
          labels:
            app: tpu-vllm
        spec:
          serviceAccountName: KSA_NAME
          containers:
          - name: vllm-container
            image: vllm/vllm-tpu:v0.18.0
            resources:
              limits:
                google.com/tpu: "4"
            command: ["sh", "-c"]
            args:
            - >-
              python3 -m vllm.entrypoints.openai.api_server
              --model=gs://BUCKET_NAME/PATH_TO_MODEL
              --load-format=runai_streamer
              --tensor-parallel-size=8
              --port=8000
            ports:
            - containerPort: 8000
            env:
            - name: VLLM_XLA_CACHE_PATH
              value: "gs://BUCKET_NAME/PATH_TO_CACHE"
          nodeSelector:
            cloud.google.com/gke-tpu-accelerator: tpu7x
            cloud.google.com/gke-tpu-topology: 2x2x1
    

Replace the following:

     * `NAMESPACE`: your Kubernetes namespace.
     * `KSA_NAME`: your Kubernetes service account name.
     * `BUCKET_NAME`: your Cloud Storage bucket name.
     * `PATH_TO_MODEL`: the path to your model directory within the bucket, for example, `models/my-llama`.
     * `PATH_TO_CACHE`: the path to your XLA compilation cache directory within the bucket, for example, `models/xla-cache`.

  2. Apply the manifest to create the Deployment:
         
         kubectl create -f vllm-deployment.yaml
         




You can generate more vLLM manifests using the [GKE Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart) tool.

## Verify the Deployment

  1. Check the status of the Deployment:
         
         kubectl get deployments -n NAMESPACE
         

  2. Get the Pod name:
         
         kubectl get pods -n NAMESPACE | grep vllm-streamer
         

Note the name of the Pod starting with `vllm-streamer-deployment`.

  3. To check if the model streamer downloads the model and weights, view the Pod logs:
         
         kubectl logs -f POD_NAME -n NAMESPACE
         

Replace `POD_NAME` with the name of the Pod from the previous step. Successful streaming logs look similar to the following:
         
         [RunAI Streamer] Overall time to stream 15.0 GiB of all files: 13.4s, 1.1 GiB/s
         


**Success:** You have successfully deployed a vLLM inference server on GKE, leveraging the Run:ai Model Streamer to accelerate model loading directly from Cloud Storage.

## Optional: Boost performance with Rapid Cache

[Cloud Storage Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) can further accelerate model loading by caching data closer to your GKE nodes. Caching is especially beneficial when scaling out multiple nodes in the same zone.

You enable Rapid Cache for a specific Cloud Storage bucket in a specific Google Cloud zone. To improve performance, the cache's zone must match the zone where your GKE inference Pods run. Your approach depends on whether your Pods run in predictable zones.

  * For GKE Standard zonal clusters, where you know which zone your Pods will run in, enable Rapid Cache for that specific zone.

  * For regional GKE clusters (both Autopilot and Standard), where Pods can be scheduled across multiple zones, you have the following options:

    * **Enable caching in all zones** : Enable Rapid Cache in every zone within the cluster's region. This ensures a cache is available regardless of where GKE schedules your Pods. Note that you incur costs for each zone where caching is enabled. For more information, see [Rapid Cache pricing](https://cloud.google.com/storage/pricing#rapid-cache).
    * **Place Pods into a specific zone** : Use a `nodeSelector` or `nodeAffinity` rule in your workload manifest to [constrain your Pods to a single zone](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gke-zonal-topology). You can then enable Rapid Cache in only that zone. This is a more cost-effective approach if your workload tolerates being restricted to a single zone.



To enable Rapid Cache for the zone where your GKE cluster resides, run the following commands:
    
    
    # Enable the cache
    gcloud storage buckets anywhere-caches create gs://$BUCKET_NAME $ZONE
    
    # Check the status of the cache
    gcloud storage buckets anywhere-caches describe $BUCKET_NAME/$ZONE
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this document, either delete the project that contains the resources, or keep the project and delete the individual resources.

To delete the individual resources, follow these steps:

  1. Delete the GKE cluster. This action removes all nodes and workloads.
         
         gcloud container clusters delete CLUSTER_NAME --location=ZONE_OR_REGION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `ZONE_OR_REGION`: the zone or region of your cluster.
  2. Disable Rapid Cache, if you enabled it, to avoid ongoing costs. For more information, see [Disable a cache](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#disable-cache).




## What's next

  * Learn how to [Load Hugging Face Models into Cloud Storage (experimental)](https://gke-ai-labs.dev/docs/tutorials/storage/hf-gcs-transfer/)
  * Learn how to [Serve an LLM with multiple GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multiple-gpu).
  * Learn more about [GPUs available on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus).
  * Learn more about [TPUs available on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Read the [GKE Storage overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview).
  * Learn about [Configuring Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
