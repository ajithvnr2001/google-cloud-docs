---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-ray/
title: Serve an LLM using TPUs on GKE with KubeRay \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:16.668268+00:00
---

# Serve an LLM using TPUs on GKE with KubeRay  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-ray/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Serve an LLM using TPUs on GKE with KubeRay Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows how to serve a large language model (LLM) using Tensor Processing Units (TPUs) on Google Kubernetes Engine (GKE) with the [Ray Operator add-on](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview), and the [vLLM](https://docs.vllm.ai/en/latest/) serving framework.

In this tutorial, you can serve LLM models on TPU v5e or TPU Trillium (v6e) as follows:

  * [Llama 3 8B instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on a single-host TPU v5e.
  * [Mistral 7B instruct v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) on a single-host TPU v5e.
  * [Llama 3.1 70B](https://huggingface.co/meta-llama/Llama-3.1-70B) on a single-host TPU Trillium (v6e).
  * [Google Gemma 4 E4B-it](https://huggingface.co/google/gemma-4-e4b-it) composed with Llama 3 8B on a single-host TPU v5e or TPU Trillium (v6e).

**Note:** To serve Gemma 4 on TPUs, you can also use the [`vllm-tpu:gemma4`](https://hub.docker.com/r/vllm/vllm-tpu/tags) Docker images and follow the recipes for [TPU Trillium (v6e)](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/inference/trillium/vLLM/Gemma4) and [Ironwood (TPU7x)](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/inference/ironwood/vLLM/Gemma4).**Note:** We don't recommend using base models like Llama 3 8B for production chatbots due to safety concerns. For more information about best practices, see [System instructions for safety](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/safety-system-instructions).

This guide is for generative AI customers, new and existing GKE users, ML engineers, MLOps (DevOps) engineers, or platform administrators interested in using Kubernetes container orchestration capabilities to serve models using Ray, on TPUs with vLLM.

## Background

This section describes the key technologies used in this guide.

### GKE managed Kubernetes service

Google Cloud offers a wide range of services, including GKE, which is well-suited to deploying and managing AI/ML workloads. GKE is a managed Kubernetes service that simplifies deploying, scaling, and managing containerized applications. GKE provides the necessary infrastructure, including scalable resources, distributed computing, and efficient networking, to handle the computational demands of LLMs.

To learn more about key Kubernetes concepts, see [Start learning about Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes). To learn more about the GKE and how it helps you scale, automate, and manage Kubernetes, see [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).

### Ray operator

The Ray Operator add-on on GKE provides an end-to-end AI/ML platform for serving, training, and fine-tuning machine learning workloads. In this tutorial, you use [Ray Serve](https://docs.ray.io/en/latest/serve/index.html), a framework in Ray, to serve popular LLMs from Hugging Face.

### TPUs

TPUs are Google's custom-developed application-specific integrated circuits (ASICs) used to accelerate machine learning and AI models built using frameworks such as [TensorFlow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/), and [JAX](https://github.com/google/jax).

This tutorial covers serving LLM models on TPU v5e or TPU Trillium (v6e) nodes with TPU topologies configured based on each model requirements for serving prompts with low latency.

### vLLM

vLLM is a highly optimized open source LLM serving framework that can increase serving throughput on TPUs, with features such as:

  * Optimized transformer implementation with [PagedAttention](https://huggingface.co/docs/text-generation-inference/en/conceptual/paged_attention)
  * Continuous batching to improve the overall serving throughput
  * Tensor parallelism and distributed serving on multiple GPUs



To learn more, refer to the [vLLM documentation](https://docs.vllm.ai/en/latest/).

## Objectives

This tutorial covers the following steps:

  1. Create a GKE cluster with a TPU node pool.
  2. Deploy a [RayCluster](https://ray-project.github.io/kuberay/reference/api/#rayservice) custom resource with a single-host TPU slice. GKE deploys the RayCluster custom resource as Kubernetes Pods.
  3. Serve an LLM.
  4. Interact with the models.



You can optionally configure the following model serving resources and techniques that the Ray Serve framework supports:

  * Deploy a RayService custom resource.
  * Compose multiple models with model composition.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Create a [Hugging Face](https://huggingface.co/) account, if you don't already have one.
  * Ensure that you have a [Hugging Face token](https://huggingface.co/docs/hub/security-tokens).
  * Ensure that you have access to the Hugging Face model that you want to use. You usually gain this access by signing an agreement and requesting access from the model owner on the Hugging Face model page.
  * Ensure that you have the following [IAM roles](https://docs.cloud.google.com/iam/docs/roles-permissions): 
    * `roles/container.admin`
    * `roles/iam.serviceAccountAdmin`
    * `roles/container.clusterAdmin`
    * `roles/artifactregistry.writer`



## Prepare your environment

  1. Check that you have enough quota in your Google Cloud project for a single-host TPU v5e or a single-host TPU Trillium (v6e). To manage your quota, see [TPU quotas](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-quota).

  2. In the Google Cloud console, start a Cloud Shell instance:   
[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Clone the sample repository:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
         cd kubernetes-engine-samples
         

  4. Navigate to the working directory:
         
         cd ai-ml/gke-ray/rayserve/llm
         

  5. Set the default environment variables for the GKE cluster creation:

###  Llama-3-8B-Instruct 
         
         export PROJECT_ID=$(gcloud config get project)
         export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
         export CLUSTER_NAME=vllm-tpu
         export COMPUTE_REGION=REGION
         export COMPUTE_ZONE=ZONE
         export HF_TOKEN=HUGGING_FACE_TOKEN
         export GSBUCKET=vllm-tpu-bucket
         export KSA_NAME=vllm-sa
         export NAMESPACE=default
         export MODEL_ID="meta-llama/Meta-Llama-3-8B-Instruct"
         export VLLM_IMAGE=docker.io/vllm/vllm-tpu:866fa4550d572f4ff3521ccf503e0df2e76591a1
         export SERVICE_NAME=vllm-tpu-head-svc
         

Replace the following:

     * `HUGGING_FACE_TOKEN`: your Hugging Face access token.
     * `REGION`: the region where you have TPU quota. Ensure that the TPU version that you want to use is available in this region. To learn more, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability-autopilot).
     * `ZONE`: the zone with available TPU quota.
     * `VLLM_IMAGE`: the vLLM TPU image. You can use the public `docker.io/vllm/vllm-tpu:866fa4550d572f4ff3521ccf503e0df2e76591a1` image or build your own TPU image.

###  Mistral-7B 
    
    export PROJECT_ID=$(gcloud config get project)
    export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
    export CLUSTER_NAME=vllm-tpu
    export COMPUTE_REGION=REGION
    export COMPUTE_ZONE=ZONE
    export HF_TOKEN=HUGGING_FACE_TOKEN
    export GSBUCKET=vllm-tpu-bucket
    export KSA_NAME=vllm-sa
    export NAMESPACE=default
    export MODEL_ID="mistralai/Mistral-7B-Instruct-v0.3"
    export TOKENIZER_MODE=mistral
    export VLLM_IMAGE=docker.io/vllm/vllm-tpu:866fa4550d572f4ff3521ccf503e0df2e76591a1
    export SERVICE_NAME=vllm-tpu-head-svc
    

Replace the following:

     * `HUGGING_FACE_TOKEN`: your Hugging Face access token.
     * `REGION`: the region where you have TPU quota. Ensure that the TPU version that you want to use is available in this region. To learn more, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability-autopilot).
     * `ZONE`: the zone with available TPU quota.
     * `VLLM_IMAGE`: the vLLM TPU image. You can use the public `docker.io/vllm/vllm-tpu:866fa4550d572f4ff3521ccf503e0df2e76591a1` image or build your own TPU image.

###  Llama 3.1 70B 
    
    export PROJECT_ID=$(gcloud config get project)
    export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
    export CLUSTER_NAME=vllm-tpu
    export COMPUTE_REGION=REGION
    export COMPUTE_ZONE=ZONE
    export HF_TOKEN=HUGGING_FACE_TOKEN
    export GSBUCKET=vllm-tpu-bucket
    export KSA_NAME=vllm-sa
    export NAMESPACE=default
    export MODEL_ID="meta-llama/Llama-3.1-70B"
    export MAX_MODEL_LEN=8192
    export VLLM_IMAGE=docker.io/vllm/vllm-tpu:866fa4550d572f4ff3521ccf503e0df2e76591a1
    export SERVICE_NAME=vllm-tpu-head-svc
    

Replace the following:

     * `HUGGING_FACE_TOKEN`: your Hugging Face access token.
     * `REGION`: the region where you have TPU quota. Ensure that the TPU version that you want to use is available in this region. To learn more, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability-autopilot).
     * `ZONE`: the zone with available TPU quota.
     * `VLLM_IMAGE`: the vLLM TPU image. You can use the public `docker.io/vllm/vllm-tpu:866fa4550d572f4ff3521ccf503e0df2e76591a1` image or build your own TPU image.

  6. Pull down the vLLM container image:
         
         sudo usermod -aG docker ${USER}
         newgrp docker
         docker pull ${VLLM_IMAGE}
         




### Create a cluster

You can serve an LLM on TPUs with Ray in a GKE Autopilot or Standard cluster by using the Ray Operator add-on.

**Best practices** : 

Use an Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

Use Cloud Shell to create an Autopilot or Standard cluster:

###  Autopilot 

  1. Create a GKE Autopilot cluster with the Ray Operator add-on enabled:
         
         gcloud container clusters create-auto ${CLUSTER_NAME}  \
             --enable-ray-operator \
             --release-channel=rapid \
             --location=${COMPUTE_REGION}
         




###  Standard 

  1. Create a Standard cluster with the Ray Operator add-on enabled:
         
         gcloud container clusters create ${CLUSTER_NAME} \
             --release-channel=rapid \
             --location=${COMPUTE_ZONE} \
             --workload-pool=${PROJECT_ID}.svc.id.goog \
             --machine-type="n1-standard-4" \
             --addons=RayOperator,GcsFuseCsiDriver
         

  2. Create a single-host TPU slice node pool:

###  Llama-3-8B-Instruct 
         
         gcloud container node-pools create tpu-1 \
             --location=${COMPUTE_ZONE} \
             --cluster=${CLUSTER_NAME} \
             --machine-type=ct5lp-hightpu-8t \
             --num-nodes=1
         

GKE creates a TPU v5e node pool with a `ct5lp-hightpu-8t` machine type.

###  Mistral-7B 
         
         gcloud container node-pools create tpu-1 \
             --location=${COMPUTE_ZONE} \
             --cluster=${CLUSTER_NAME} \
             --machine-type=ct5lp-hightpu-8t \
             --num-nodes=1
         

GKE creates a TPU v5e node pool with a `ct5lp-hightpu-8t` machine type.

###  Llama 3.1 70B 
         
         gcloud container node-pools create tpu-1 \
             --location=${COMPUTE_ZONE} \
             --cluster=${CLUSTER_NAME} \
             --machine-type=ct6e-standard-8t \
             --num-nodes=1
         

GKE creates a TPU v6e node pool with a `ct6e-standard-8t` machine type.




### Configure kubectl to communicate with your cluster

To configure kubectl to communicate with your cluster, run the following command:

###  Autopilot 
    
    
    gcloud container clusters get-credentials ${CLUSTER_NAME} \
        --location=${COMPUTE_REGION}
    

###  Standard 
    
    
    gcloud container clusters get-credentials ${CLUSTER_NAME} \
        --location=${COMPUTE_ZONE}
    

### Create a Kubernetes Secret for Hugging Face credentials

To create a Kubernetes Secret that contains the Hugging Face token, run the following command:
    
    
    kubectl create secret generic hf-secret \
        --from-literal=hf_api_token=${HF_TOKEN} \
        --dry-run=client -o yaml | kubectl --namespace ${NAMESPACE} apply -f -
    

### Create a Cloud Storage bucket

To accelerate the vLLM deployment startup time and minimize required disk space per node, use the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver) to mount the downloaded model and compilation cache to the Ray nodes.

In Cloud Shell, run the following command:
    
    
    gcloud storage buckets create gs://${GSBUCKET} \
        --uniform-bucket-level-access
    

This command creates a Cloud Storage bucket to store the model files you download from Hugging Face.

### Set up a Kubernetes ServiceAccount to access the bucket

  1. Create the Kubernetes ServiceAccount:
         
         kubectl create serviceaccount ${KSA_NAME} \
             --namespace ${NAMESPACE}
         

  2. Grant the Kubernetes ServiceAccount read-write access to the Cloud Storage bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://${GSBUCKET} \
             --member "principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/${NAMESPACE}/sa/${KSA_NAME}" \
             --role "roles/storage.objectUser"
         

GKE creates the following resources for the LLM:

     1. A Cloud Storage bucket to store the downloaded model and the compilation cache. A [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver) reads the content of the bucket.
     2. [Volumes with file caching enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver#file-cache) and the [parallel download](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver#parallel-download) feature of Cloud Storage FUSE.
**Best practice** : 

Use a file cache backed by `[tmpfs](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir)` or `[Hyperdisk / Persistent Disk](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver)` depending on the expected size of the model contents, for example, weight files. In this tutorial, you use Cloud Storage FUSE file cache backed by RAM.




## Deploy a RayCluster custom resource

Deploy a RayCluster custom resource, which typically consists of one system Pod and multiple worker Pods.

###  Llama-3-8B-Instruct 

Create the RayCluster custom resource to deploy the Llama 3 8B instruction tuned model by completing the following steps:

  1. Inspect the `ray-cluster.tpu-v5e-singlehost.yaml` manifest:
         
         apiVersion: ray.io/v1
         kind: RayCluster
         metadata:
           name: vllm-tpu
         spec:
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
                     image: $VLLM_IMAGE
                     imagePullPolicy: IfNotPresent
                     resources:
                       limits:
                         cpu: "2"
                         memory: 8G
                       requests:
                         cpu: "2"
                         memory: 8G
                     env:
                       - name: HUGGING_FACE_HUB_TOKEN
                         valueFrom:
                           secretKeyRef:
                             name: hf-secret
                             key: hf_api_token
                       - name: VLLM_XLA_CACHE_PATH
                         value: "/data"
                     ports:
                       - containerPort: 6379
                         name: gcs
                       - containerPort: 8265
                         name: dashboard
                       - containerPort: 10001
                         name: client
                       - containerPort: 8000
                         name: serve
                       - containerPort: 8471
                         name: slicebuilder
                       - containerPort: 8081
                         name: mxla
                     volumeMounts:
                     - name: gcs-fuse-csi-ephemeral
                       mountPath: /data
                     - name: dshm
                       mountPath: /dev/shm
                 volumes:
                 - name: gke-gcsfuse-cache
                   emptyDir:
                     medium: Memory
                 - name: dshm
                   emptyDir:
                     medium: Memory
                 - name: gcs-fuse-csi-ephemeral
                   csi:
                     driver: gcsfuse.csi.storage.gke.io
                     volumeAttributes:
                       bucketName: $GSBUCKET
                       mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
           workerGroupSpecs:
           - groupName: tpu-group
             replicas: 1
             minReplicas: 1
             maxReplicas: 1
             numOfHosts: 1
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
                     image: $VLLM_IMAGE
                     imagePullPolicy: IfNotPresent
                     resources:
                       limits:
                         cpu: "100"
                         google.com/tpu: "8"
                         ephemeral-storage: 40G
                         memory: 200G
                       requests:
                         cpu: "100"
                         google.com/tpu: "8"
                         ephemeral-storage: 40G
                         memory: 200G
                     env:
                       - name: VLLM_XLA_CACHE_PATH
                         value: "/data"
                       - name: HUGGING_FACE_HUB_TOKEN
                         valueFrom:
                           secretKeyRef:
                             name: hf-secret
                             key: hf_api_token
                     volumeMounts:
                     - name: gcs-fuse-csi-ephemeral
                       mountPath: /data
                     - name: dshm
                       mountPath: /dev/shm
                 volumes:
                 - name: gke-gcsfuse-cache
                   emptyDir:
                     medium: Memory
                 - name: dshm
                   emptyDir:
                     medium: Memory
                 - name: gcs-fuse-csi-ephemeral
                   csi:
                     driver: gcsfuse.csi.storage.gke.io
                     volumeAttributes:
                       bucketName: $GSBUCKET
                       mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                   cloud.google.com/gke-tpu-topology: 2x4

  2. Apply the manifest:
         
         envsubst < tpu/ray-cluster.tpu-v5e-singlehost.yaml | kubectl --namespace ${NAMESPACE} apply -f -
         

The `envsubst` command replaces the environment variables in the manifest.




GKE creates a RayCluster custom resource with a `workergroup` that contains a TPU v5e single-host in a `2x4` topology.

###  Mistral-7B 

Create the RayCluster custom resource to deploy the Mistral-7B model by completing the following steps:

  1. Inspect the `ray-cluster.tpu-v5e-singlehost.yaml` manifest:
         
         apiVersion: ray.io/v1
         kind: RayCluster
         metadata:
           name: vllm-tpu
         spec:
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
                     image: $VLLM_IMAGE
                     imagePullPolicy: IfNotPresent
                     resources:
                       limits:
                         cpu: "2"
                         memory: 8G
                       requests:
                         cpu: "2"
                         memory: 8G
                     env:
                       - name: HUGGING_FACE_HUB_TOKEN
                         valueFrom:
                           secretKeyRef:
                             name: hf-secret
                             key: hf_api_token
                       - name: VLLM_XLA_CACHE_PATH
                         value: "/data"
                     ports:
                       - containerPort: 6379
                         name: gcs
                       - containerPort: 8265
                         name: dashboard
                       - containerPort: 10001
                         name: client
                       - containerPort: 8000
                         name: serve
                       - containerPort: 8471
                         name: slicebuilder
                       - containerPort: 8081
                         name: mxla
                     volumeMounts:
                     - name: gcs-fuse-csi-ephemeral
                       mountPath: /data
                     - name: dshm
                       mountPath: /dev/shm
                 volumes:
                 - name: gke-gcsfuse-cache
                   emptyDir:
                     medium: Memory
                 - name: dshm
                   emptyDir:
                     medium: Memory
                 - name: gcs-fuse-csi-ephemeral
                   csi:
                     driver: gcsfuse.csi.storage.gke.io
                     volumeAttributes:
                       bucketName: $GSBUCKET
                       mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
           workerGroupSpecs:
           - groupName: tpu-group
             replicas: 1
             minReplicas: 1
             maxReplicas: 1
             numOfHosts: 1
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
                     image: $VLLM_IMAGE
                     imagePullPolicy: IfNotPresent
                     resources:
                       limits:
                         cpu: "100"
                         google.com/tpu: "8"
                         ephemeral-storage: 40G
                         memory: 200G
                       requests:
                         cpu: "100"
                         google.com/tpu: "8"
                         ephemeral-storage: 40G
                         memory: 200G
                     env:
                       - name: VLLM_XLA_CACHE_PATH
                         value: "/data"
                       - name: HUGGING_FACE_HUB_TOKEN
                         valueFrom:
                           secretKeyRef:
                             name: hf-secret
                             key: hf_api_token
                     volumeMounts:
                     - name: gcs-fuse-csi-ephemeral
                       mountPath: /data
                     - name: dshm
                       mountPath: /dev/shm
                 volumes:
                 - name: gke-gcsfuse-cache
                   emptyDir:
                     medium: Memory
                 - name: dshm
                   emptyDir:
                     medium: Memory
                 - name: gcs-fuse-csi-ephemeral
                   csi:
                     driver: gcsfuse.csi.storage.gke.io
                     volumeAttributes:
                       bucketName: $GSBUCKET
                       mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                   cloud.google.com/gke-tpu-topology: 2x4

  2. Apply the manifest:
         
         envsubst < tpu/ray-cluster.tpu-v5e-singlehost.yaml | kubectl --namespace ${NAMESPACE} apply -f -
         

The `envsubst` command replaces the environment variables in the manifest.




GKE creates a RayCluster custom resource with a `workergroup` that contains a TPU v5e single-host in a `2x4` topology.

###  Llama 3.1 70B 

Create the RayCluster custom resource to deploy the Llama 3.1 70B model by completing the following steps:

  1. Inspect the `ray-cluster.tpu-v6e-singlehost.yaml` manifest:
         
         apiVersion: ray.io/v1
         kind: RayCluster
         metadata:
           name: vllm-tpu
         spec:
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
                     image: $VLLM_IMAGE
                     imagePullPolicy: IfNotPresent
                     resources:
                       limits:
                         cpu: "2"
                         memory: 8G
                       requests:
                         cpu: "2"
                         memory: 8G
                     env:
                       - name: HUGGING_FACE_HUB_TOKEN
                         valueFrom:
                           secretKeyRef:
                             name: hf-secret
                             key: hf_api_token
                       - name: VLLM_XLA_CACHE_PATH
                         value: "/data"
                     ports:
                       - containerPort: 6379
                         name: gcs
                       - containerPort: 8265
                         name: dashboard
                       - containerPort: 10001
                         name: client
                       - containerPort: 8000
                         name: serve
                       - containerPort: 8471
                         name: slicebuilder
                       - containerPort: 8081
                         name: mxla
                     volumeMounts:
                     - name: gcs-fuse-csi-ephemeral
                       mountPath: /data
                     - name: dshm
                       mountPath: /dev/shm
                 volumes:
                 - name: gke-gcsfuse-cache
                   emptyDir:
                     medium: Memory
                 - name: dshm
                   emptyDir:
                     medium: Memory
                 - name: gcs-fuse-csi-ephemeral
                   csi:
                     driver: gcsfuse.csi.storage.gke.io
                     volumeAttributes:
                       bucketName: $GSBUCKET
                       mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
           workerGroupSpecs:
           - groupName: tpu-group
             replicas: 1
             minReplicas: 1
             maxReplicas: 1
             numOfHosts: 1
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
                     image: $VLLM_IMAGE
                     imagePullPolicy: IfNotPresent
                     resources:
                       limits:
                         cpu: "100"
                         google.com/tpu: "8"
                         ephemeral-storage: 40G
                         memory: 200G
                       requests:
                         cpu: "100"
                         google.com/tpu: "8"
                         ephemeral-storage: 40G
                         memory: 200G
                     env:
                       - name: HUGGING_FACE_HUB_TOKEN
                         valueFrom:
                           secretKeyRef:
                             name: hf-secret
                             key: hf_api_token
                       - name: VLLM_XLA_CACHE_PATH
                         value: "/data"
                     volumeMounts:
                     - name: gcs-fuse-csi-ephemeral
                       mountPath: /data
                     - name: dshm
                       mountPath: /dev/shm
                 volumes:
                 - name: gke-gcsfuse-cache
                   emptyDir:
                     medium: Memory
                 - name: dshm
                   emptyDir:
                     medium: Memory
                 - name: gcs-fuse-csi-ephemeral
                   csi:
                     driver: gcsfuse.csi.storage.gke.io
                     volumeAttributes:
                       bucketName: $GSBUCKET
                       mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                   cloud.google.com/gke-tpu-topology: 2x4

  2. Apply the manifest:
         
         envsubst < tpu/ray-cluster.tpu-v6e-singlehost.yaml | kubectl --namespace ${NAMESPACE} apply -f -
         

The `envsubst` command replaces the environment variables in the manifest.




GKE creates a RayCluster custom resource with a `workergroup` that contains a TPU v6e single-host in a `2x4` topology.

## Connect to the RayCluster custom resource

After the RayCluster custom resource is created, you can connect to the RayCluster resource and start serving the model.

  1. Verify that GKE created the RayCluster Service:
         
         kubectl --namespace ${NAMESPACE} get raycluster/vllm-tpu \
             --output wide
         

The output is similar to the following:
         
         NAME       DESIRED WORKERS   AVAILABLE WORKERS   CPUS   MEMORY   GPUS   TPUS   STATUS   AGE   HEAD POD IP      HEAD SERVICE IP
         vllm-tpu   1                 1                   ###    ###G     0      8      ready    ###   ###.###.###.###  ###.###.###.###
         

Wait until the `STATUS` is `ready` and the `HEAD POD IP` and `HEAD SERVICE IP` columns have an IP address.

  2. Establish `port-forwarding` sessions to the Ray head:
         
         pkill -f "kubectl .* port-forward .* 8265:8265"
         pkill -f "kubectl .* port-forward .* 10001:10001"
         kubectl --namespace ${NAMESPACE} port-forward service/${SERVICE_NAME} 8265:8265 2>&1 >/dev/null &
         kubectl --namespace ${NAMESPACE} port-forward service/${SERVICE_NAME} 10001:10001 2>&1 >/dev/null &
         

  3. Verify that the Ray client can connect to the remote RayCluster custom resource:
         
         docker run --net=host -it ${VLLM_IMAGE} \
         ray list nodes --address http://localhost:8265
         

The output is similar to the following:
         
         ======== List: YYYY-MM-DD HH:MM:SS.NNNNNN ========
         Stats:
         ------------------------------
         Total: 2
         
         Table:
         ------------------------------
             NODE_ID    NODE_IP          IS_HEAD_NODE  STATE    STATE_MESSAGE    NODE_NAME          RESOURCES_TOTAL                   LABELS
         0  XXXXXXXXXX  ###.###.###.###  True          ALIVE                     ###.###.###.###    CPU: 2.0                          ray.io/node_id: XXXXXXXXXX
                                                                                                    memory: #.### GiB
                                                                                                    node:###.###.###.###: 1.0
                                                                                                    node:__internal_head__: 1.0
                                                                                                    object_store_memory: #.### GiB
         1  XXXXXXXXXX  ###.###.###.###  False         ALIVE                     ###.###.###.###    CPU: 100.0                       ray.io/node_id: XXXXXXXXXX
                                                                                                    TPU: 8.0
                                                                                                    TPU-v#e-8-head: 1.0
                                                                                                    accelerator_type:TPU-V#E: 1.0
                                                                                                    memory: ###.### GiB
                                                                                                    node:###.###.###.###: 1.0
                                                                                                    object_store_memory: ##.### GiB
                                                                                                    tpu-group-0: 1.0
         




## Deploy the model with vLLM

To deploy a specific model with vLLM, follow these instructions.

###  Llama-3-8B-Instruct 
    
    
    docker run \
        --env MODEL_ID=${MODEL_ID} \
        --net=host \
        --volume=./tpu:/workspace/vllm/tpu \
        -it \
        ${VLLM_IMAGE} \
        serve run serve_tpu:model \
        --address=ray://localhost:10001 \
        --app-dir=./tpu \
        --runtime-env-json='{"env_vars": {"MODEL_ID": "meta-llama/Meta-Llama-3-8B-Instruct"}}'
    

###  Mistral-7B 
    
    
    docker run \
        --env MODEL_ID=${MODEL_ID} \
        --env TOKENIZER_MODE=${TOKENIZER_MODE} \
        --net=host \
        --volume=./tpu:/workspace/vllm/tpu \
        -it \
        ${VLLM_IMAGE} \
        serve run serve_tpu:model \
        --address=ray://localhost:10001 \
        --app-dir=./tpu \
        --runtime-env-json='{"env_vars": {"MODEL_ID": "mistralai/Mistral-7B-Instruct-v0.3", "TOKENIZER_MODE": "mistral"}}'
    

###  Llama 3.1 70B 
    
    
    docker run \
        --env MAX_MODEL_LEN=${MAX_MODEL_LEN} \
        --env MODEL_ID=${MODEL_ID} \
        --net=host \
        --volume=./tpu:/workspace/vllm/tpu \
        -it \
        ${VLLM_IMAGE} \
        serve run serve_tpu:model \
        --address=ray://localhost:10001 \
        --app-dir=./tpu \
        --runtime-env-json='{"env_vars": {"MAX_MODEL_LEN": "8192", "MODEL_ID": "meta-llama/Meta-Llama-3.1-70B"}}'
    

### View the Ray Dashboard

You can view your Ray Serve deployment and relevant logs from the Ray Dashboard.

  1. Click the ![Web Preview icon](https://docs.cloud.google.com/static/shell/docs/images/web_preview.svg)**Web Preview** button, which can be found on the top right of the Cloud Shell taskbar.
  2. Click **Change port** and set the port number to `8265`.
  3. Click **Change and Preview**.
  4. On the Ray Dashboard, click the **Serve** tab.



After the Serve deployment has a `HEALTHY` status, the model is ready to begin processing inputs.

## Serve the model

This guide highlights models that support text generation, a technique that allows text content creation from a prompt.

###  Llama-3-8B-Instruct 

  1. Set up port forwarding to the server:
         
         pkill -f "kubectl .* port-forward .* 8000:8000"
         kubectl --namespace ${NAMESPACE} port-forward service/${SERVICE_NAME} 8000:8000 2>&1 >/dev/null &
         

  2. Send a prompt to the Serve endpoint:
         
         curl -X POST http://localhost:8000/v1/generate -H "Content-Type: application/json" -d '{"prompt": "What are the top 5 most popular programming languages? Be brief.", "max_tokens": 1024}'
         




Expand the following section to see an example of the output.
    
    
    {"prompt": "What
    are the top 5 most popular programming languages? Be brief.", "text": " (Note:
    This answer may change over time.)\n\nAccording to the TIOBE Index, a widely
    followed measure of programming language popularity, the top 5 languages
    are:\n\n1. JavaScript\n2. Python\n3. Java\n4. C++\n5. C#\n\nThese rankings are
    based on a combination of search engine queries, web traffic, and online
    courses. Keep in mind that other sources may have slightly different rankings.
    (Source: TIOBE Index, August 2022)", "token_ids": [320, 9290, 25, 1115, 4320,
    1253, 2349, 927, 892, 9456, 11439, 311, 279, 350, 3895, 11855, 8167, 11, 264,
    13882, 8272, 6767, 315, 15840, 4221, 23354, 11, 279, 1948, 220, 20, 15823,
    527, 1473, 16, 13, 13210, 198, 17, 13, 13325, 198, 18, 13, 8102, 198, 19, 13,
    356, 23792, 20, 13, 356, 27585, 9673, 33407, 527, 3196, 389, 264, 10824, 315,
    2778, 4817, 20126, 11, 3566, 9629, 11, 323, 2930, 14307, 13, 13969, 304, 4059,
    430, 1023, 8336, 1253, 617, 10284, 2204, 33407, 13, 320, 3692, 25, 350, 3895,
    11855, 8167, 11, 6287, 220, 2366, 17, 8, 128009]}

###  Mistral-7B 

  1. Set up port forwarding to the server:
         
         pkill -f "kubectl .* port-forward .* 8000:8000"
         kubectl --namespace ${NAMESPACE} port-forward service/${SERVICE_NAME} 8000:8000 2>&1 >/dev/null &
         

  2. Send a prompt to the Serve endpoint:
         
         curl -X POST http://localhost:8000/v1/generate -H "Content-Type: application/json" -d '{"prompt": "What are the top 5 most popular programming languages? Be brief.", "max_tokens": 1024}'
         




Expand the following section to see an example of the output.
    
    
    {"prompt": "What are the top 5 most popular programming languages? Be brief.",
    "text": "\n\n1. JavaScript: Widely used for web development, particularly for
    client-side scripting and building dynamic web page content.\n\n2. Python:
    Known for its simplicity and readability, it's widely used for web
    development, machine learning, data analysis, and scientific computing.\n\n3.
    Java: A general-purpose programming language used in a wide range of
    applications, including Android app development, web services, and
    enterprise-level applications.\n\n4. C#: Developed by Microsoft, it's often
    used for Windows desktop apps, game development (Unity), and web development
    (ASP.NET).\n\n5. TypeScript: A superset of JavaScript that adds optional
    static typing and other features for large-scale, maintainable JavaScript
    applications.", "token_ids": [781, 781, 29508, 29491, 27049, 29515, 1162,
    1081, 1491, 2075, 1122, 5454, 4867, 29493, 7079, 1122, 4466, 29501, 2973,
    7535, 1056, 1072, 4435, 11384, 5454, 3652, 3804, 29491, 781, 781, 29518,
    29491, 22134, 29515, 1292, 4444, 1122, 1639, 26001, 1072, 1988, 3205, 29493,
    1146, 29510, 29481, 13343, 2075, 1122, 5454, 4867, 29493, 6367, 5936, 29493,
    1946, 6411, 29493, 1072, 11237, 22031, 29491, 781, 781, 29538, 29491, 12407,
    29515, 1098, 3720, 29501, 15460, 4664, 17060, 4610, 2075, 1065, 1032, 6103,
    3587, 1070, 9197, 29493, 3258, 13422, 1722, 4867, 29493, 5454, 4113, 29493,
    1072, 19123, 29501, 5172, 9197, 29491, 781, 781, 29549, 29491, 1102, 29539,
    29515, 9355, 1054, 1254, 8670, 29493, 1146, 29510, 29481, 3376, 2075, 1122,
    9723, 25470, 14189, 29493, 2807, 4867, 1093, 2501, 1240, 1325, 1072, 5454,
    4867, 1093, 2877, 29521, 29491, 12466, 1377, 781, 781, 29550, 29491, 6475,
    7554, 29515, 1098, 26434, 1067, 1070, 27049, 1137, 14401, 12052, 1830, 25460,
    1072, 1567, 4958, 1122, 3243, 29501, 6473, 29493, 9855, 1290, 27049, 9197,
    29491, 2]}

###  Llama 3.1 70B 

  1. Set up port forwarding to the server:
         
         pkill -f "kubectl .* port-forward .* 8000:8000"
         kubectl --namespace ${NAMESPACE} port-forward service/${SERVICE_NAME} 8000:8000 2>&1 >/dev/null &
         

  2. Send a prompt to the Serve endpoint:
         
         curl -X POST http://localhost:8000/v1/generate -H "Content-Type: application/json" -d '{"prompt": "What are the top 5 most popular programming languages? Be brief.", "max_tokens": 1024}'
         




Expand the following section to see an example of the output.
    
    
    {"prompt": "What are
    the top 5 most popular programming languages? Be brief.", "text": " This is a
    very subjective question, but there are some general guidelines to follow when
    selecting a language. For example, if you\u2019re looking for a language
    that\u2019s easy to learn, you might want to consider Python. It\u2019s one of
    the most popular languages in the world, and it\u2019s also relatively easy to
    learn. If you\u2019re looking for a language that\u2019s more powerful, you
    might want to consider Java. It\u2019s a more complex language, but it\u2019s
    also very popular. Whichever language you choose, make sure you do your
    research and pick one that\u2019s right for you.\nThe most popular programming
    languages are:\nWhy is C++ so popular?\nC++ is a powerful and versatile
    language that is used in many different types of software. It is also one of
    the most popular programming languages, with a large community of developers
    who are always creating new and innovative ways to use it. One of the reasons
    why C++ is so popular is because it is a very efficient language. It allows
    developers to write code that is both fast and reliable, which is essential
    for many types of software. Additionally, C++ is very flexible, meaning that
    it can be used for a wide range of different purposes. Finally, C++ is also
    very popular because it is easy to learn. There are many resources available
    online and in books that can help anyone get started with learning the
    language.\nJava is a versatile language that can be used for a variety of
    purposes. It is one of the most popular programming languages in the world and
    is used by millions of people around the globe. Java is used for everything
    from developing desktop applications to creating mobile apps and games. It is
    also a popular choice for web development. One of the reasons why Java is so
    popular is because it is a platform-independent language. This means that it
    can be used on any type of computer or device, regardless of the operating
    system. Java is also very versatile and can be used for a variety of different
    purposes.", "token_ids": [1115, 374, 264, 1633, 44122, 3488, 11, 719, 1070,
    527, 1063, 4689, 17959, 311, 1833, 994, 27397, 264, 4221, 13, 1789, 3187, 11,
    422, 499, 3207, 3411, 369, 264, 4221, 430, 753, 4228, 311, 4048, 11, 499,
    2643, 1390, 311, 2980, 13325, 13, 1102, 753, 832, 315, 279, 1455, 5526, 15823,
    304, 279, 1917, 11, 323, 433, 753, 1101, 12309, 4228, 311, 4048, 13, 1442,
    499, 3207, 3411, 369, 264, 4221, 430, 753, 810, 8147, 11, 499, 2643, 1390,
    311, 2980, 8102, 13, 1102, 753, 264, 810, 6485, 4221, 11, 719, 433, 753, 1101,
    1633, 5526, 13, 1254, 46669, 4221, 499, 5268, 11, 1304, 2771, 499, 656, 701,
    3495, 323, 3820, 832, 430, 753, 1314, 369, 499, 627, 791, 1455, 5526, 15840,
    15823, 527, 512, 10445, 374, 356, 1044, 779, 5526, 5380, 34, 1044, 374, 264,
    8147, 323, 33045, 4221, 430, 374, 1511, 304, 1690, 2204, 4595, 315, 3241, 13,
    1102, 374, 1101, 832, 315, 279, 1455, 5526, 15840, 15823, 11, 449, 264, 3544,
    4029, 315, 13707, 889, 527, 2744, 6968, 502, 323, 18699, 5627, 311, 1005, 433,
    13, 3861, 315, 279, 8125, 3249, 356, 1044, 374, 779, 5526, 374, 1606, 433,
    374, 264, 1633, 11297, 4221, 13, 1102, 6276, 13707, 311, 3350, 2082, 430, 374,
    2225, 5043, 323, 15062, 11, 902, 374, 7718, 369, 1690, 4595, 315, 3241, 13,
    23212, 11, 356, 1044, 374, 1633, 19303, 11, 7438, 430, 433, 649, 387, 1511,
    369, 264, 7029, 2134, 315, 2204, 10096, 13, 17830, 11, 356, 1044, 374, 1101,
    1633, 5526, 1606, 433, 374, 4228, 311, 4048, 13, 2684, 527, 1690, 5070, 2561,
    2930, 323, 304, 6603, 430, 649, 1520, 5606, 636, 3940, 449, 6975, 279, 4221,
    627, 15391, 3S74, 264, 33045, 4221, 430, 649, 387, 1511, 369, 264, 8205, 315,
    10096, 13, 1102, 374, 832, 315, 279, 1455, 5526, 15840, 15823, 304, 279, 1917,
    323, 374, 1511, 555, 11990, 315, 1274, 2212, 279, 24867, 13, 8102, 374, 1511,
    369, 4395, 505, 11469, 17963, 8522, 311, 6968, 6505, 10721, 323, 3953, 13,
    1102, 374, 1101, 264, 5526, 5873, 369, 3566, 4500, 13, 3861, 315, 279, 8125,
    3249, 8102, 374, 779, 5526, 374, 1606, 433, 374, 264, 5452, 98885, 4221, 13,
    1115, 3445, 430, 433, 649, 387, 1511, 389, 904, 955, 315, 6500, 477, 3756, 11,
    15851, 315, 279, 10565, 1887, 13, 8102, 374, 1101, 1633, 33045, 323, 649, 387,
    1511, 369, 264, 8205, 315, 2204, 10096, 13, 128001]}

**Success:** You have deployed an LLM with a [RayCluster](https://ray-project.github.io/kuberay/reference/api/#rayservice) custom resource in a single-host TPU slice.

## Additional configuration

You can optionally configure the following model serving resources and techniques that the Ray Serve framework supports:

  * Deploy a RayService custom resource. In the preceding steps of this tutorial, you use RayCluster instead of RayService. We recommend RayService for production environments.
  * Compose multiple models with model composition. Configure model multiplexing and model composition that are supported by the [Ray Serve](https://docs.ray.io/en/latest/serve/index.html) framework. Model composition lets you chain together inputs and outputs across multiple LLMs and scale your models as a single application.
  * Build and deploy your own TPU image. We recommend this option if you need finer-grained control over the contents of your Docker image.



### Deploy a RayService

You can deploy the same models from this tutorial by using a [RayService](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview#rayservice) custom resource.

  1. Delete the RayCluster custom resource that you created in this tutorial:
         
         kubectl --namespace ${NAMESPACE} delete raycluster/vllm-tpu
         

  2. Create the RayService custom resource to deploy a model:

###  Llama-3-8B-Instruct 

     1. Inspect the `ray-service.tpu-v5e-singlehost.yaml` manifest:
            
            apiVersion: ray.io/v1
            kind: RayService
            metadata:
              name: vllm-tpu
            spec:
              serveConfigV2: |
                applications:
                  - name: llm
                    import_path: ai-ml.gke-ray.rayserve.llm.tpu.serve_tpu:model
                    deployments:
                    - name: VLLMDeployment
                      num_replicas: 1
                    runtime_env:
                      working_dir: "https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/archive/main.zip"
                      env_vars:
                        MODEL_ID: "$MODEL_ID"
                        MAX_MODEL_LEN: "$MAX_MODEL_LEN"
                        DTYPE: "$DTYPE"
                        TOKENIZER_MODE: "$TOKENIZER_MODE"
                        TPU_CHIPS: "8"
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
                        image: $VLLM_IMAGE
                        imagePullPolicy: IfNotPresent
                        ports:
                        - containerPort: 6379
                          name: gcs
                        - containerPort: 8265
                          name: dashboard
                        - containerPort: 10001
                          name: client
                        - containerPort: 8000
                          name: serve
                        env:
                        - name: HUGGING_FACE_HUB_TOKEN
                          valueFrom:
                            secretKeyRef:
                              name: hf-secret
                              key: hf_api_token
                        - name: VLLM_XLA_CACHE_PATH
                          value: "/data"
                        resources:
                          limits:
                            cpu: "2"
                            memory: 8G
                          requests:
                            cpu: "2"
                            memory: 8G
                        volumeMounts:
                        - name: gcs-fuse-csi-ephemeral
                          mountPath: /data
                        - name: dshm
                          mountPath: /dev/shm
                      volumes:
                      - name: gke-gcsfuse-cache
                        emptyDir:
                          medium: Memory
                      - name: dshm
                        emptyDir:
                          medium: Memory
                      - name: gcs-fuse-csi-ephemeral
                        csi:
                          driver: gcsfuse.csi.storage.gke.io
                          volumeAttributes:
                            bucketName: $GSBUCKET
                            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                workerGroupSpecs:
                - groupName: tpu-group
                  replicas: 1
                  minReplicas: 1
                  maxReplicas: 1
                  numOfHosts: 1
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
                          image: $VLLM_IMAGE
                          imagePullPolicy: IfNotPresent
                          resources:
                            limits:
                              cpu: "100"
                              google.com/tpu: "8"
                              ephemeral-storage: 40G
                              memory: 200G
                            requests:
                              cpu: "100"
                              google.com/tpu: "8"
                              ephemeral-storage: 40G
                              memory: 200G
                          env:
                            - name: JAX_PLATFORMS
                              value: "tpu"
                            - name: HUGGING_FACE_HUB_TOKEN
                              valueFrom:
                                secretKeyRef:
                                  name: hf-secret
                                  key: hf_api_token
                            - name: VLLM_XLA_CACHE_PATH
                              value: "/data"
                          volumeMounts:
                          - name: gcs-fuse-csi-ephemeral
                            mountPath: /data
                          - name: dshm
                            mountPath: /dev/shm
                      volumes:
                      - name: gke-gcsfuse-cache
                        emptyDir:
                          medium: Memory
                      - name: dshm
                        emptyDir:
                          medium: Memory
                      - name: gcs-fuse-csi-ephemeral
                        csi:
                          driver: gcsfuse.csi.storage.gke.io
                          volumeAttributes:
                            bucketName: $GSBUCKET
                            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                      nodeSelector:
                        cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                        cloud.google.com/gke-tpu-topology: 2x4

     2. Apply the manifest:
            
            envsubst < tpu/ray-service.tpu-v5e-singlehost.yaml | kubectl --namespace ${NAMESPACE} apply -f -
            

The `envsubst` command replaces the environment variables in the manifest.

GKE creates a RayService with a `workergroup` that contains a TPU v5e single-host in a `2x4` topology.

###  Mistral-7B 

     1. Inspect the `ray-service.tpu-v5e-singlehost.yaml` manifest:
            
            apiVersion: ray.io/v1
            kind: RayService
            metadata:
              name: vllm-tpu
            spec:
              serveConfigV2: |
                applications:
                  - name: llm
                    import_path: ai-ml.gke-ray.rayserve.llm.tpu.serve_tpu:model
                    deployments:
                    - name: VLLMDeployment
                      num_replicas: 1
                    runtime_env:
                      working_dir: "https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/archive/main.zip"
                      env_vars:
                        MODEL_ID: "$MODEL_ID"
                        MAX_MODEL_LEN: "$MAX_MODEL_LEN"
                        DTYPE: "$DTYPE"
                        TOKENIZER_MODE: "$TOKENIZER_MODE"
                        TPU_CHIPS: "8"
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
                        image: $VLLM_IMAGE
                        imagePullPolicy: IfNotPresent
                        ports:
                        - containerPort: 6379
                          name: gcs
                        - containerPort: 8265
                          name: dashboard
                        - containerPort: 10001
                          name: client
                        - containerPort: 8000
                          name: serve
                        env:
                        - name: HUGGING_FACE_HUB_TOKEN
                          valueFrom:
                            secretKeyRef:
                              name: hf-secret
                              key: hf_api_token
                        - name: VLLM_XLA_CACHE_PATH
                          value: "/data"
                        resources:
                          limits:
                            cpu: "2"
                            memory: 8G
                          requests:
                            cpu: "2"
                            memory: 8G
                        volumeMounts:
                        - name: gcs-fuse-csi-ephemeral
                          mountPath: /data
                        - name: dshm
                          mountPath: /dev/shm
                      volumes:
                      - name: gke-gcsfuse-cache
                        emptyDir:
                          medium: Memory
                      - name: dshm
                        emptyDir:
                          medium: Memory
                      - name: gcs-fuse-csi-ephemeral
                        csi:
                          driver: gcsfuse.csi.storage.gke.io
                          volumeAttributes:
                            bucketName: $GSBUCKET
                            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                workerGroupSpecs:
                - groupName: tpu-group
                  replicas: 1
                  minReplicas: 1
                  maxReplicas: 1
                  numOfHosts: 1
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
                          image: $VLLM_IMAGE
                          imagePullPolicy: IfNotPresent
                          resources:
                            limits:
                              cpu: "100"
                              google.com/tpu: "8"
                              ephemeral-storage: 40G
                              memory: 200G
                            requests:
                              cpu: "100"
                              google.com/tpu: "8"
                              ephemeral-storage: 40G
                              memory: 200G
                          env:
                            - name: JAX_PLATFORMS
                              value: "tpu"
                            - name: HUGGING_FACE_HUB_TOKEN
                              valueFrom:
                                secretKeyRef:
                                  name: hf-secret
                                  key: hf_api_token
                            - name: VLLM_XLA_CACHE_PATH
                              value: "/data"
                          volumeMounts:
                          - name: gcs-fuse-csi-ephemeral
                            mountPath: /data
                          - name: dshm
                            mountPath: /dev/shm
                      volumes:
                      - name: gke-gcsfuse-cache
                        emptyDir:
                          medium: Memory
                      - name: dshm
                        emptyDir:
                          medium: Memory
                      - name: gcs-fuse-csi-ephemeral
                        csi:
                          driver: gcsfuse.csi.storage.gke.io
                          volumeAttributes:
                            bucketName: $GSBUCKET
                            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                      nodeSelector:
                        cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                        cloud.google.com/gke-tpu-topology: 2x4

     2. Apply the manifest:
            
            envsubst < tpu/ray-service.tpu-v5e-singlehost.yaml | kubectl --namespace ${NAMESPACE} apply -f -
            

The `envsubst` command replaces the environment variables in the manifest.

GKE creates a RayService with a `workergroup` containing a TPU v5e single-host in a `2x4` topology.

###  Llama 3.1 70B 

     1. Inspect the `ray-service.tpu-v6e-singlehost.yaml` manifest:
            
            apiVersion: ray.io/v1
            kind: RayService
            metadata:
              name: vllm-tpu
            spec:
              serveConfigV2: |
                applications:
                  - name: llm
                    import_path: ai-ml.gke-ray.rayserve.llm.tpu.serve_tpu:model
                    deployments:
                    - name: VLLMDeployment
                      num_replicas: 1
                    runtime_env:
                      working_dir: "https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/archive/main.zip"
                      env_vars:
                        MODEL_ID: "$MODEL_ID"
                        MAX_MODEL_LEN: "$MAX_MODEL_LEN"
                        DTYPE: "$DTYPE"
                        TOKENIZER_MODE: "$TOKENIZER_MODE"
                        TPU_CHIPS: "8"
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
                        image: $VLLM_IMAGE
                        imagePullPolicy: IfNotPresent
                        ports:
                        - containerPort: 6379
                          name: gcs
                        - containerPort: 8265
                          name: dashboard
                        - containerPort: 10001
                          name: client
                        - containerPort: 8000
                          name: serve
                        env:
                        - name: HUGGING_FACE_HUB_TOKEN
                          valueFrom:
                            secretKeyRef:
                              name: hf-secret
                              key: hf_api_token
                        - name: VLLM_XLA_CACHE_PATH
                          value: "/data"
                        resources:
                          limits:
                            cpu: "2"
                            memory: 8G
                          requests:
                            cpu: "2"
                            memory: 8G
                        volumeMounts:
                        - name: gcs-fuse-csi-ephemeral
                          mountPath: /data
                        - name: dshm
                          mountPath: /dev/shm
                      volumes:
                      - name: gke-gcsfuse-cache
                        emptyDir:
                          medium: Memory
                      - name: dshm
                        emptyDir:
                          medium: Memory
                      - name: gcs-fuse-csi-ephemeral
                        csi:
                          driver: gcsfuse.csi.storage.gke.io
                          volumeAttributes:
                            bucketName: $GSBUCKET
                            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                workerGroupSpecs:
                - groupName: tpu-group
                  replicas: 1
                  minReplicas: 1
                  maxReplicas: 1
                  numOfHosts: 1
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
                          image: $VLLM_IMAGE
                          imagePullPolicy: IfNotPresent
                          resources:
                            limits:
                              cpu: "100"
                              google.com/tpu: "8"
                              ephemeral-storage: 40G
                              memory: 200G
                            requests:
                              cpu: "100"
                              google.com/tpu: "8"
                              ephemeral-storage: 40G
                              memory: 200G
                          env:
                            - name: JAX_PLATFORMS
                              value: "tpu"
                            - name: HUGGING_FACE_HUB_TOKEN
                              valueFrom:
                                secretKeyRef:
                                  name: hf-secret
                                  key: hf_api_token
                            - name: VLLM_XLA_CACHE_PATH
                              value: "/data"
                          volumeMounts:
                          - name: gcs-fuse-csi-ephemeral
                            mountPath: /data
                          - name: dshm
                            mountPath: /dev/shm
                      volumes:
                      - name: gke-gcsfuse-cache
                        emptyDir:
                          medium: Memory
                      - name: dshm
                        emptyDir:
                          medium: Memory
                      - name: gcs-fuse-csi-ephemeral
                        csi:
                          driver: gcsfuse.csi.storage.gke.io
                          volumeAttributes:
                            bucketName: $GSBUCKET
                            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                      nodeSelector:
                        cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                        cloud.google.com/gke-tpu-topology: 2x4

     2. Apply the manifest:
            
            envsubst < tpu/ray-service.tpu-v6e-singlehost.yaml | kubectl --namespace ${NAMESPACE} apply -f -
            

The `envsubst` command replaces the environment variables in the manifest.

GKE creates a RayCluster custom resource where the Ray Serve application is deployed and the subsequent RayService custom resource is created.

  3. Verify the status of the RayService resource:
         
         kubectl --namespace ${NAMESPACE} get rayservices/vllm-tpu
         

Wait for the Service status to change to `Running`:
         
         NAME       SERVICE STATUS   NUM SERVE ENDPOINTS
         vllm-tpu   Running          1
         

  4. Retrieve the name of the RayCluster head service:
         
         SERVICE_NAME=$(kubectl --namespace=${NAMESPACE} get rayservices/vllm-tpu \
             --template={{.status.activeServiceStatus.rayClusterStatus.head.serviceName}})
         

**Note:** If the RayCluster head service value is not retrieved, manually update the `SERVICE_NAME` value by running the `kubectl get services --namespace ${NAMESPACE}` command.
  5. Establish `port-forwarding` sessions to the Ray head to view the Ray dashboard:
         
         pkill -f "kubectl .* port-forward .* 8265:8265"
         kubectl --namespace ${NAMESPACE} port-forward service/${SERVICE_NAME} 8265:8265 2>&1 >/dev/null &
         

  6. View the Ray Dashboard.

  7. Serve the model.

  8. Clean up the RayService resource:
         
         kubectl --namespace ${NAMESPACE} delete rayservice/vllm-tpu
         




### Compose multiple models with model composition

[Model composition](https://docs.ray.io/en/latest/serve/model_composition.html) is a technique for composing multiple models into a single application.

In this section, you use a GKE cluster to compose two models, Llama 3 8B IT and Gemma 4 E4B-it, into a single application:

  * The first model is the assistant model that answers questions asked in the prompt.
  * The second model is the summarizer model. The output of the assistant model is chained into the input of the summarizer model. The final result is the summarized version of the response from the assistant model.


  1. Ensure that you have access to the [Gemma 4 E4B-it model on Hugging Face](https://huggingface.co/google/gemma-4-e4b-it). Accept the model license terms on Hugging Face if you haven't done so already. Ensure that you have created the Kubernetes Secret for Hugging Face credentials.

  2. Set up your environment:
         
         export ASSIST_MODEL_ID=meta-llama/Meta-Llama-3-8B-Instruct
         export SUMMARIZER_MODEL_ID=google/gemma-4-e4b-it
         

  3. For Standard clusters, create an additional single-host TPU slice node pool:
         
         gcloud container node-pools create tpu-2 \
           --location=${COMPUTE_ZONE} \
           --cluster=${CLUSTER_NAME} \
           --machine-type=MACHINE_TYPE \
           --num-nodes=1
         

Replace `MACHINE_TYPE` with any of the following machine types:

     * `ct5lp-hightpu-8t` to provision TPU v5e.
     * `ct6e-standard-8t` to provision TPU v6e.

Autopilot clusters automatically provision the required nodes.

  4. Deploy the RayService resource based on the TPU version that you want to use:

###  TPU v5e 

     1. Inspect the `ray-service.tpu-v5e-singlehost.yaml` manifest:
            
            apiVersion: ray.io/v1
            kind: RayService
            metadata:
              name: vllm-tpu
            spec:
              serveConfigV2: |
                applications:
                - name: llm
                  route_prefix: /
                  import_path:  ai-ml.gke-ray.rayserve.llm.model-composition.serve_tpu:multi_model
                  deployments:
                  - name: MultiModelDeployment
                    num_replicas: 1
                  runtime_env:
                    working_dir: "https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/archive/main.zip"
                    env_vars:
                      ASSIST_MODEL_ID: "$ASSIST_MODEL_ID"
                      SUMMARIZER_MODEL_ID: "$SUMMARIZER_MODEL_ID"
                      TPU_CHIPS: "16"
                      TPU_HEADS: "2"
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
                        image: $VLLM_IMAGE
                        resources:
                          limits:
                            cpu: "2"
                            memory: 8G
                          requests:
                            cpu: "2"
                            memory: 8G
                        ports:
                        - containerPort: 6379
                          name: gcs-server
                        - containerPort: 8265
                          name: dashboard
                        - containerPort: 10001
                          name: client
                        - containerPort: 8000
                          name: serve
                        env:
                          - name: HUGGING_FACE_HUB_TOKEN
                            valueFrom:
                              secretKeyRef:
                                name: hf-secret
                                key: hf_api_token
                          - name: VLLM_XLA_CACHE_PATH
                            value: "/data"
                        volumeMounts:
                        - name: gcs-fuse-csi-ephemeral
                          mountPath: /data
                        - name: dshm
                          mountPath: /dev/shm
                      volumes:
                      - name: gke-gcsfuse-cache
                        emptyDir:
                          medium: Memory
                      - name: dshm
                        emptyDir:
                          medium: Memory
                      - name: gcs-fuse-csi-ephemeral
                        csi:
                          driver: gcsfuse.csi.storage.gke.io
                          volumeAttributes:
                            bucketName: $GSBUCKET
                            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                workerGroupSpecs:
                - replicas: 2
                  minReplicas: 1
                  maxReplicas: 2
                  numOfHosts: 1
                  groupName: tpu-group
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
                      - name: llm
                        image: $VLLM_IMAGE
                        env:
                          - name: HUGGING_FACE_HUB_TOKEN
                            valueFrom:
                              secretKeyRef:
                                name: hf-secret
                                key: hf_api_token
                          - name: VLLM_XLA_CACHE_PATH
                            value: "/data"
                        resources:
                          limits:
                            cpu: "100"
                            google.com/tpu: "8"
                            ephemeral-storage: 40G
                            memory: 200G
                          requests:
                            cpu: "100"
                            google.com/tpu: "8"
                            ephemeral-storage: 40G
                            memory: 200G
                        volumeMounts:
                        - name: gcs-fuse-csi-ephemeral
                          mountPath: /data
                        - name: dshm
                          mountPath: /dev/shm
                      volumes:
                      - name: gke-gcsfuse-cache
                        emptyDir:
                          medium: Memory
                      - name: dshm
                        emptyDir:
                          medium: Memory
                      - name: gcs-fuse-csi-ephemeral
                        csi:
                          driver: gcsfuse.csi.storage.gke.io
                          volumeAttributes:
                            bucketName: $GSBUCKET
                            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                      nodeSelector:
                        cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                        cloud.google.com/gke-tpu-topology: 2x4

     2. Apply the manifest:
            
            envsubst < model-composition/ray-service.tpu-v5e-singlehost.yaml | kubectl --namespace ${NAMESPACE} apply -f -
            

###  TPU v6e 

     1. Inspect the `ray-service.tpu-v6e-singlehost.yaml` manifest:
            
            apiVersion: ray.io/v1
            kind: RayService
            metadata:
              name: vllm-tpu
            spec:
              serveConfigV2: |
                applications:
                - name: llm
                  route_prefix: /
                  import_path:  ai-ml.gke-ray.rayserve.llm.model-composition.serve_tpu:multi_model
                  deployments:
                  - name: MultiModelDeployment
                    num_replicas: 1
                  runtime_env:
                    working_dir: "https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/archive/main.zip"
                    env_vars:
                      ASSIST_MODEL_ID: "$ASSIST_MODEL_ID"
                      SUMMARIZER_MODEL_ID: "$SUMMARIZER_MODEL_ID"
                      TPU_CHIPS: "16"
                      TPU_HEADS: "2"
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
                        image: $VLLM_IMAGE
                        resources:
                          limits:
                            cpu: "2"
                            memory: 8G
                          requests:
                            cpu: "2"
                            memory: 8G
                        ports:
                        - containerPort: 6379
                          name: gcs-server
                        - containerPort: 8265
                          name: dashboard
                        - containerPort: 10001
                          name: client
                        - containerPort: 8000
                          name: serve
                        env:
                          - name: HUGGING_FACE_HUB_TOKEN
                            valueFrom:
                              secretKeyRef:
                                name: hf-secret
                                key: hf_api_token
                          - name: VLLM_XLA_CACHE_PATH
                            value: "/data"
                        volumeMounts:
                        - name: gcs-fuse-csi-ephemeral
                          mountPath: /data
                        - name: dshm
                          mountPath: /dev/shm
                      volumes:
                      - name: gke-gcsfuse-cache
                        emptyDir:
                          medium: Memory
                      - name: dshm
                        emptyDir:
                          medium: Memory
                      - name: gcs-fuse-csi-ephemeral
                        csi:
                          driver: gcsfuse.csi.storage.gke.io
                          volumeAttributes:
                            bucketName: $GSBUCKET
                            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                workerGroupSpecs:
                - replicas: 2
                  minReplicas: 1
                  maxReplicas: 2
                  numOfHosts: 1
                  groupName: tpu-group
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
                      - name: llm
                        image: $VLLM_IMAGE
                        env:
                          - name: HUGGING_FACE_HUB_TOKEN
                            valueFrom:
                              secretKeyRef:
                                name: hf-secret
                                key: hf_api_token
                          - name: VLLM_XLA_CACHE_PATH
                            value: "/data"
                        resources:
                          limits:
                            cpu: "100"
                            google.com/tpu: "8"
                            ephemeral-storage: 40G
                            memory: 200G
                          requests:
                            cpu: "100"
                            google.com/tpu: "8"
                            ephemeral-storage: 40G
                            memory: 200G
                        volumeMounts:
                        - name: gcs-fuse-csi-ephemeral
                          mountPath: /data
                        - name: dshm
                          mountPath: /dev/shm
                      volumes:
                      - name: gke-gcsfuse-cache
                        emptyDir:
                          medium: Memory
                      - name: dshm
                        emptyDir:
                          medium: Memory
                      - name: gcs-fuse-csi-ephemeral
                        csi:
                          driver: gcsfuse.csi.storage.gke.io
                          volumeAttributes:
                            bucketName: $GSBUCKET
                            mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:parallel-downloads-per-file:100,file-cache:max-parallel-downloads:-1,file-cache:download-chunk-size-mb:10,file-cache:max-size-mb:-1"
                      nodeSelector:
                        cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                        cloud.google.com/gke-tpu-topology: 2x4

     2. Apply the manifest:
            
            envsubst < model-composition/ray-service.tpu-v6e-singlehost.yaml | kubectl --namespace ${NAMESPACE} apply -f -
            

  5. Wait for the status of the RayService resource to change to `Running`:
         
         kubectl --namespace ${NAMESPACE} get rayservice/vllm-tpu
         

The output is similar to the following:
         
         NAME       SERVICE STATUS   NUM SERVE ENDPOINTS
         vllm-tpu   Running          2
         

In this output, the `RUNNING` status indicates the RayService resource is ready.

  6. Confirm that GKE created the Service for the Ray Serve application:
         
         kubectl --namespace ${NAMESPACE} get service/vllm-tpu-serve-svc
         

The output is similar to the following:
         
         NAME                 TYPE        CLUSTER-IP        EXTERNAL-IP   PORT(S)    AGE
         vllm-tpu-serve-svc   ClusterIP   ###.###.###.###   <none>        8000/TCP   ###
         

  7. Establish `port-forwarding` sessions to the Ray head:
         
         pkill -f "kubectl .* port-forward .* 8265:8265"
         pkill -f "kubectl .* port-forward .* 8000:8000"
         kubectl --namespace ${NAMESPACE} port-forward service/vllm-tpu-serve-svc 8265:8265 2>&1 >/dev/null &
         kubectl --namespace ${NAMESPACE} port-forward service/vllm-tpu-serve-svc 8000:8000 2>&1 >/dev/null &
         

  8. Send a request to the model:
         
         curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d '{"prompt": "What is the most popular programming language for machine learning and why?", "max_tokens": 1000}'
         

The output is similar to the following:
         
         {"text": [" used in various data science projects, including building machine learning models, preprocessing data, and visualizing results.\n\nSure, here is a single sentence summarizing the text:\n\nPython is the most popular programming language for machine learning and is widely used in data science projects, encompassing model building, data preprocessing, and visualization."]}
         




### Build and deploy the TPU image

This tutorial uses hosted TPU images from [vLLM](https://hub.docker.com/r/vllm/vllm-tpu/tags). vLLM provides a `Dockerfile.tpu` image that builds vLLM on top of the required PyTorch XLA image that includes TPU dependencies. However, you can also build and deploy your own TPU image for finer-grained control over the contents of your Docker image.

**Note:** You need to be granted the [roles/artifactregistry.admin role](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) to create and manage Artifact Registry repositories.

  1. Create a Docker repository to store the container images for this guide:
         
         gcloud artifacts repositories create vllm-tpu --repository-format=docker --location=${COMPUTE_REGION} && \
         gcloud auth configure-docker ${COMPUTE_REGION}-docker.pkg.dev
         

  2. Clone the vLLM repository:
         
         git clone https://github.com/vllm-project/vllm.git
         cd vllm
         

  3. Build the image:
         
         docker build -f ./docker/Dockerfile.tpu . -t vllm-tpu
         

  4. Tag the TPU image with your Artifact Registry name:
         
         export VLLM_IMAGE=${COMPUTE_REGION}-docker.pkg.dev/${PROJECT_ID}/vllm-tpu/vllm-tpu:TAG
         docker tag vllm-tpu ${VLLM_IMAGE}
         

Replace `TAG` with the name of the tag that you want to define. If you don't specify a tag, Docker applies the default latest tag.

  5. Push the image to Artifact Registry:
         
         docker push ${VLLM_IMAGE}
         




## Delete the individual resources

If you used an existing project and you don't want to delete it, you can delete the individual resources.

  1. Delete the RayCluster custom resource:
         
         kubectl --namespace ${NAMESPACE} delete rayclusters vllm-tpu
         

  2. Delete the Cloud Storage bucket:
         
         gcloud storage rm -r gs://${GSBUCKET}
         

  3. Delete the Artifact Registry repository:
         
         gcloud artifacts repositories delete vllm-tpu \
             --location=${COMPUTE_REGION}
         

  4. Delete the cluster:
         
         gcloud container clusters delete ${CLUSTER_NAME} \
             --location=LOCATION
         

Replace `LOCATION` with any of the following environment variables:

     * For Autopilot clusters, use `COMPUTE_REGION`.
     * For Standard clusters, use `COMPUTE_ZONE`.



## Delete the project

If you deployed the tutorial in a new Google Cloud project, and if you no longer need the project, then delete it by completing the following steps:

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Discover how to run optimized AI/ML workloads with [GKE platform orchestration capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra).
  * Learn how to use Ray Serve on GKE, by viewing the [sample code in GitHub](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/rayserve).
  * Learn how to collect and view metrics for Ray clusters running on GKE, by completing the steps in [Collect and view logs and metrics for Ray clusters on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/collect-view-logs-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
