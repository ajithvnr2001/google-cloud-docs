---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-ray-torchtpu/
title: Serve LLMs on multi-host TPUs with Ray and TorchTPU \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:44.100098+00:00
---

# Serve LLMs on multi-host TPUs with Ray and TorchTPU  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-ray-torchtpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Serve LLMs on multi-host TPUs with Ray and TorchTPU Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to serve a Mixture-of-Experts (MoE) [Gemma 4 26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it) large language model (LLM) with tensor parallelism and expert parallelism on multi-host [Cloud TPU](https://docs.cloud.google.com/tpu) slices in Google Kubernetes Engine (GKE) by using [Ray Serve LLM](https://docs.ray.io/en/latest/serve/llm/index.html), [vLLM](https://docs.vllm.ai/en/latest/), and [vLLM-TorchTPU](https://github.com/vllm-project/vllm-torchtpu).

**Tip:** For production deployments on GKE, you can use [Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart) to get tailored configurations for your model inference.

This tutorial is intended for machine learning (ML) engineers, platform admins and operators, and data and AI specialists who use Kubernetes container orchestration to serve AI and ML workloads on distributed, multi-host TPU slices. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before starting this tutorial, ensure that you're familiar with the following:

  * [About GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)
  * [Multi-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host)
  * [About Ray on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview)



## Background

This section describes the key technologies used in this tutorial.

### TPUs

[Tensor Processing Units](https://docs.cloud.google.com/tpu) (TPUs) are Google custom-designed accelerators for machine learning workloads. This tutorial supports both [TPU Trillium (v6e)](https://docs.cloud.google.com/tpu/docs/v6e) and [Ironwood (TPU7x)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpu-ironwood). In a multi-host TPU slice, multiple TPU hosts communicate directly over a high-speed Inter-Chip Interconnect (ICI) network, providing the aggregate High Bandwidth Memory (HBM) and low-latency collective communication required to serve models that exceed the memory capacity of a single chip or TPU host.

### vLLM and TorchTPU

[vLLM](https://docs.vllm.ai/en/latest/) is an open-source inference and serving engine for LLMs. [TorchTPU](https://github.com/google-pytorch/torch_tpu) is an open-source PyTorch backend for Cloud TPU that provides device management and collective communication over ICI.

[vLLM-TorchTPU](https://github.com/vllm-project/vllm-torchtpu) registers the TPU platform plugin with vLLM and compiles PyTorch model forward passes for Cloud TPU through TorchTPU and the Accelerated Linear Algebra (XLA) compiler. It supports distributed tensor parallelism and expert parallelism across multi-host TPU slices by using Ray.

### Ray Serve LLM on GKE

[Ray Serve LLM](https://docs.ray.io/en/latest/serve/llm/index.html) provides an OpenAI-compatible HTTP ingress for `/v1/chat/completions`, `/v1/completions`, and `/v1/models` endpoints and orchestrates distributed vLLM deployments on GKE. When you enable the [Ray on GKE add-on](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview), the KubeRay operator and its TPU webhook inject slice topology metadata, worker hostnames, and TorchTPU coordination variables into each multi-host TPU worker Pod.

Ray Serve LLM provides the following capabilities for multi-host TPU serving:

  * [Topology-aware slice placement](https://docs.ray.io/en/latest/serve/llm/user-guides/tpu.html) reserves an intact multi-host TPU slice for each model replica when you specify a TPU topology in the `accelerator_config` field, scheduling one vLLM worker per TPU device across the slice.
  * [Prefix-aware routing](https://docs.ray.io/en/latest/serve/llm/user-guides/prefix-aware-routing.html) directs requests with shared system prompts or multi-turn conversation history to the replica that already caches those prefix key-value (KV) blocks in TPU HBM when serving across multiple TPU slice replicas.
  * [Direct token streaming](https://docs.ray.io/en/latest/serve/llm/user-guides/direct-streaming.html) batches outbound token streams across concurrent requests and streams responses directly from model replicas to reduce time-to-first-token (TTFT) and inter-token latency (ITL).
  * [Concurrency-based replica autoscaling](https://docs.ray.io/en/latest/serve/autoscaling-guide.html) scales model replicas in whole-slice increments based on ongoing request concurrency.



## Objectives

This tutorial shows you how to do the following:

  1. Build a container image that layers Ray Serve on top of the prebuilt vLLM-TorchTPU base image and push it to Artifact Registry.
  2. Create a GKE cluster in Autopilot or Standard on TPU Trillium (v6e) or Ironwood (TPU7x).
  3. Deploy a multi-host RayCluster custom resource and verify the TPU topology configuration.
  4. Deploy a Ray Serve LLM application to serve the `google/gemma-4-26B-A4B-it` model with tensor parallelism and expert parallelism across a multi-host TPU slice, or deploy both the cluster and application declaratively with a RayService custom resource.
  5. Send OpenAI-compatible model discovery and chat completion requests to the served model.



## Costs

In this tutorial, you use the following billable components of Google Cloud:

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Cloud TPU](https://docs.cloud.google.com/tpu/pricing)
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

When you finish the tasks that are described in this tutorial, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Artifact Registry API and the Google Kubernetes Engine API. 
[ Enable APIs ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,artifactregistry.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Verify that your project has sufficient quota for TPU Trillium (v6e) or Ironwood (TPU7x) capacity in your selected zone. For more information, see [Cloud TPU quotas](https://docs.cloud.google.com/tpu/docs/quota).
  * Ensure that you have a [Hugging Face account](https://huggingface.co/), accept the license terms on the [`google/gemma-4-26B-A4B-it` model page](https://huggingface.co/google/gemma-4-26B-A4B-it), and generate a Hugging Face [access token](https://huggingface.co/settings/tokens) with `Read` permissions.
  * Ensure that your account has the following [IAM roles](https://docs.cloud.google.com/iam/docs/roles-permissions): 
    * [Kubernetes Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
    * [Artifact Registry Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)



## Prepare your environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) or a local workstation to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with the command-line tools used in this tutorial, including `kubectl`, `docker`, `python3`, and the `gcloud` CLI.

To set up your environment with Cloud Shell, follow these steps:

  1. In the Google Cloud console, launch a Cloud Shell session by clicking ![Cloud Shell activation icon.](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** in the [Google Cloud console](http://console.cloud.google.com). This action launches a session in the bottom pane of Google Cloud console.

  2. Clone the `kubernetes-engine-samples` repository and change to the sample directory for this tutorial:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
         cd kubernetes-engine-samples/ai-ml/gke-ray/rayserve/llm/torchtpu
         

  3. Create and activate a local Python virtual environment with the Ray CLI installed:
         
         python3 -m venv ~/ray-env
         source ~/ray-env/bin/activate
         pip install "ray[default]==2.58.0"
         

  4. Set the environment variables for your Google Cloud project and cluster:
         
         export PROJECT_ID=PROJECT_ID
         export CLUSTER_NAME=CLUSTER_NAME
         export REGION=REGION
         export ZONE=ZONE
         export ARTIFACT_REGISTRY=ARTIFACT_REGISTRY
         export HF_TOKEN=HF_TOKEN
         export IMAGE_URI=${REGION}-docker.pkg.dev/${PROJECT_ID}/${ARTIFACT_REGISTRY}/ray-torchtpu-vllm:latest
         gcloud config set project ${PROJECT_ID}
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `CLUSTER_NAME`: the name of your GKE cluster, such as `ray-serve-torchtpu-cluster`.
     * `REGION`: the region where your Artifact Registry repository and TPU capacity are located, such as `us-east5`.
     * `ZONE`: the zone where your TPU capacity is available, such as `us-east5-b`. For more information, see [Validate TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
     * `ARTIFACT_REGISTRY`: the name of your Artifact Registry Docker repository, such as `ray-torchtpu`.
     * `HF_TOKEN`: your Hugging Face access token with `Read` permissions.



## Build the custom container image

Build a container image that installs the `ray[default,serve]` package on top of the prebuilt vLLM-TorchTPU base image, which includes TorchTPU, vLLM, and the vLLM-TorchTPU plugin.

  1. Review the `Dockerfile` in the `kubernetes-engine-samples/ai-ml/gke-ray/rayserve/llm/torchtpu` directory:
         
         FROM vllm/vllm-torchtpu:v0.29.0
         
         ENV HF_HOME=/dev/shm/huggingface
         ENV RAY_SERVE_DEFAULT_HTTP_HOST=0.0.0.0
         
         # Install wget for KubeRay health probes and pin Ray Serve and transformers
         # versions compatible with vLLM 0.29.0 and multi-host TPUs.
         RUN apt-get update && apt-get install -y --no-install-recommends wget \
             && rm -rf /var/lib/apt/lists/* \
             && pip install --no-cache-dir \
                "ray[default,serve] @ https://s3-us-west-2.amazonaws.com/ray-wheels/master/6b2b414bb7a5b4e2705ed9f4fdab9787b92f3b08/ray-3.0.0.dev0-cp312-cp312-manylinux2014_x86_64.whl" \
                "transformers>=5.18.0"

Multi-host TPU serving with Ray Serve LLM requires Ray version 2.56.0 or later on TPU Trillium (v6e) and Ray version 2.58.0 or later for per-chiplet scheduling on Ironwood (TPU7x).

  2. Create the Artifact Registry Docker repository, build the container image, and push it to Artifact Registry:
         
         gcloud artifacts repositories create ${ARTIFACT_REGISTRY} \
             --repository-format=docker \
             --location=${REGION} \
             --description="Ray and vLLM-TorchTPU container images"
         
         gcloud auth configure-docker ${REGION}-docker.pkg.dev,us-docker.pkg.dev
         docker build -t ${IMAGE_URI} .
         docker push ${IMAGE_URI}
         




## Create a GKE cluster

You can serve LLMs on multi-host TPU slices in a GKE Autopilot or Standard cluster with the managed [Ray operator](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/enable-ray-on-gke) add-on enabled.

  1. Create your GKE cluster and configure credentials for the `kubectl` command-line tool:

### Autopilot

     1. Create a regional GKE Autopilot cluster with the Ray operator add-on enabled:
            
            gcloud container clusters create-auto ${CLUSTER_NAME} \
                --project=${PROJECT_ID} \
                --region=${REGION} \
                --cluster-version=1.36 \
                --enable-ray-operator
            

When you deploy the RayCluster or RayService custom resource in a later step, GKE Autopilot automatically provisions the CPU head node and the multi-host TPU slice that match your Pod resource requests and node selectors.

     2. Configure the `kubectl` command-line tool to communicate with your cluster:
            
            gcloud container clusters get-credentials ${CLUSTER_NAME} \
                --project=${PROJECT_ID} \
                --region=${REGION}
            

### Standard

     1. Create a zonal GKE Standard cluster with a CPU node pool to host the Ray head Pod, [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming), and GKE Dataplane V2 enabled:
            
            gcloud container clusters create ${CLUSTER_NAME} \
                --project=${PROJECT_ID} \
                --zone=${ZONE} \
                --cluster-version=1.36 \
                --machine-type=n2-standard-8 \
                --num-nodes=1 \
                --addons=RayOperator \
                --enable-image-streaming \
                --enable-dataplane-v2
            

**Note:** If you self-manage open-source KubeRay instead of using the GKE `RayOperator` add-on, install [KubeRay](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/kuberay-operator-installation.html) and [KubeRay TPU webhook](https://github.com/ai-on-gke/kuberay-tpu-webhook) version 1.4.0 or later for TorchTPU environment variable injection.
     2. Configure the `kubectl` command-line tool to communicate with your cluster:
            
            gcloud container clusters get-credentials ${CLUSTER_NAME} \
                --project=${PROJECT_ID} \
                --zone=${ZONE}
            

     3. Create a 16-device multi-host TPU slice node pool with a `4x4` topology across four hosts on TPU Trillium (v6e) or a `2x2x2` topology across two hosts on Ironwood (TPU7x):

### Trillium (v6e)
            
            gcloud container node-pools create tpu-multi-host-pool \
                --project=${PROJECT_ID} \
                --cluster=${CLUSTER_NAME} \
                --zone=${ZONE} \
                --machine-type=ct6e-standard-4t \
                --tpu-topology=4x4 \
                --num-nodes=4
            

### Ironwood (TPU7x)
            
            gcloud container node-pools create tpu-multi-host-pool \
                --project=${PROJECT_ID} \
                --cluster=${CLUSTER_NAME} \
                --zone=${ZONE} \
                --machine-type=tpu7x-standard-4t \
                --tpu-topology=2x2x2 \
                --num-nodes=2
            

**Tip:** To [consume a specific TPU reservation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations#consuming-tpu-reservations), append the `--reservation-affinity=specific` and `--reservation=RESERVATION_NAME` flags to the `node-pools create` command, where `RESERVATION_NAME` is the name of your TPU reservation. To use [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms), append the `--spot` flag.

  2. Create a Kubernetes Secret with your Hugging Face token so that Ray Pods can authenticate with Hugging Face when downloading model weights:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_api_token=${HF_TOKEN}
         




## Deploy the multi-host RayCluster custom resource

Deploy a RayCluster custom resource that provisions a CPU head Pod, an in-memory `/dev/shm` volume for the Ray shared-memory object store, and a multi-host TPU worker group.

**Tip:** To deploy both the RayCluster custom resource and the Ray Serve application in a single declarative manifest without running the `ray job submit` command, skip to Deploy declaratively with a RayService custom resource.

  1. Review the RayCluster manifest for your TPU version in the sample repository:

### Trillium (v6e)
         
         apiVersion: ray.io/v1
         kind: RayCluster
         metadata:
           name: ray-serve-torchtpu
         spec:
           headGroupSpec:
             rayStartParams:
               num-cpus: "0"
             template:
               spec:
                 containers:
                 - name: ray-head
                   image: ${IMAGE_URI}
                   env:
                   - name: HF_TOKEN
                     valueFrom:
                       secretKeyRef:
                         name: hf-secret
                         key: hf_api_token
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
                       cpu: "4"
                       memory: "16Gi"
                     requests:
                       cpu: "4"
                       memory: "16Gi"
           workerGroupSpecs:
           - groupName: v6e-16
             replicas: 1
             numOfHosts: 4
             template:
               spec:
                 containers:
                 - name: ray-worker
                   image: ${IMAGE_URI}
                   env:
                   - name: HF_TOKEN
                     valueFrom:
                       secretKeyRef:
                         name: hf-secret
                         key: hf_api_token
                   resources:
                     limits:
                       cpu: "64"
                       memory: "200Gi"
                       google.com/tpu: "4"
                     requests:
                       cpu: "64"
                       memory: "200Gi"
                       google.com/tpu: "4"
                   volumeMounts:
                   - mountPath: /dev/shm
                     name: dshm
                 volumes:
                 - name: dshm
                   emptyDir:
                     medium: Memory
                     sizeLimit: 100Gi
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                   cloud.google.com/gke-tpu-topology: 4x4

### Ironwood (TPU7x)
         
         apiVersion: ray.io/v1
         kind: RayCluster
         metadata:
           name: ray-serve-torchtpu
         spec:
           headGroupSpec:
             rayStartParams:
               num-cpus: "0"
             template:
               spec:
                 containers:
                 - name: ray-head
                   image: ${IMAGE_URI}
                   env:
                   - name: HF_TOKEN
                     valueFrom:
                       secretKeyRef:
                         name: hf-secret
                         key: hf_api_token
                   - name: RAY_TPU_RESOURCE_PER_CHIP
                     value: "2"
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
                       cpu: "4"
                       memory: "16Gi"
                     requests:
                       cpu: "4"
                       memory: "16Gi"
           workerGroupSpecs:
           - groupName: tpu7x-16
             replicas: 1
             numOfHosts: 2
             resources:
               # Advertises 8 logical TPU cores (2 chiplets per physical chip) per host.
               TPU: "8"
             template:
               spec:
                 containers:
                 - name: ray-worker
                   image: ${IMAGE_URI}
                   env:
                   - name: HF_TOKEN
                     valueFrom:
                       secretKeyRef:
                         name: hf-secret
                         key: hf_api_token
                   - name: RAY_TPU_RESOURCE_PER_CHIP
                     value: "2"
                   resources:
                     limits:
                       cpu: "64"
                       memory: "250Gi"
                       google.com/tpu: "4"
                     requests:
                       cpu: "64"
                       memory: "250Gi"
                       google.com/tpu: "4"
                   volumeMounts:
                   - mountPath: /dev/shm
                     name: dshm
                 volumes:
                 - name: dshm
                   emptyDir:
                     medium: Memory
                     sizeLimit: 128Gi
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: tpu7x
                   cloud.google.com/gke-tpu-topology: 2x2x2

On Ironwood (TPU7x), each physical chip contains two chiplets, providing eight logical TPU cores per four-chip host. The manifest sets the value of the `TPU` field to `"8"` in the `resources` section and sets the `RAY_TPU_RESOURCE_PER_CHIP` environment variable to `"2"` to advertise and schedule eight logical `TPU` resources per host.

  2. Apply the manifest to create the RayCluster custom resource:

### Trillium (v6e)
         
         envsubst < ray-cluster.tpu-v6e-multihost.yaml | kubectl apply -f -
         

### Ironwood (TPU7x)
         
         envsubst < ray-cluster.tpu-v7x-multihost.yaml | kubectl apply -f -
         

  3. Wait until the head Pod and all TPU worker Pods reach the `Running` and `1/1 READY` state:
         
         kubectl get pods -l ray.io/cluster=ray-serve-torchtpu
         

The output is similar to the following:

### Trillium (v6e)
         
         NAME                                     READY   STATUS    RESTARTS   AGE
         ray-serve-torchtpu-head-5cj7g            1/1     Running   0          35s
         ray-serve-torchtpu-v6e-16-worker-6x8cg   1/1     Running   0          35s
         ray-serve-torchtpu-v6e-16-worker-79j5l   1/1     Running   0          35s
         ray-serve-torchtpu-v6e-16-worker-psxbl   1/1     Running   0          35s
         ray-serve-torchtpu-v6e-16-worker-rz7dv   1/1     Running   0          35s
         

### Ironwood (TPU7x)
         
         NAME                                       READY   STATUS    RESTARTS   AGE
         ray-serve-torchtpu-head-w7b2v              1/1     Running   0          2m30s
         ray-serve-torchtpu-tpu7x-16-worker-6zlnj   1/1     Running   0          2m30s
         ray-serve-torchtpu-tpu7x-16-worker-cb4zz   1/1     Running   0          2m30s
         

  4. Verify that the KubeRay TPU webhook injected the multi-host slice, worker coordination, and TorchTPU environment variables into the worker Pods:
         
         kubectl get pods -l ray.io/node-type=worker \
             -o=jsonpath='{range .items[0].spec.containers[0].env[*]}{.name}={.value}{"\n"}{end}' \
             | grep -E "TPU_WORKER_ID|TPU_WORKER_HOSTNAMES|TPU_NAME|TORCH_TPU_TOPOLOGY|TORCH_TPU_SLICEBUILDER_ADDRESSES"
         

The output is similar to the following:

### Trillium (v6e)
         
         TPU_WORKER_HOSTNAMES=v6e-16-0-0.ray-serve-torchtpu-headless,v6e-16-0-1.ray-serve-torchtpu-headless,v6e-16-0-2.ray-serve-torchtpu-headless,v6e-16-0-3.ray-serve-torchtpu-headless
         TORCH_TPU_TOPOLOGY=4,4,1
         TORCH_TPU_SLICEBUILDER_ADDRESSES=v6e-16-0-0.ray-serve-torchtpu-headless:8471,v6e-16-0-0.ray-serve-torchtpu-headless:8472,v6e-16-0-0.ray-serve-torchtpu-headless:8473,v6e-16-0-0.ray-serve-torchtpu-headless:8474,v6e-16-0-1.ray-serve-torchtpu-headless:8471,v6e-16-0-1.ray-serve-torchtpu-headless:8472,v6e-16-0-1.ray-serve-torchtpu-headless:8473,v6e-16-0-1.ray-serve-torchtpu-headless:8474,v6e-16-0-2.ray-serve-torchtpu-headless:8471,v6e-16-0-2.ray-serve-torchtpu-headless:8472,v6e-16-0-2.ray-serve-torchtpu-headless:8473,v6e-16-0-2.ray-serve-torchtpu-headless:8474,v6e-16-0-3.ray-serve-torchtpu-headless:8471,v6e-16-0-3.ray-serve-torchtpu-headless:8472,v6e-16-0-3.ray-serve-torchtpu-headless:8473,v6e-16-0-3.ray-serve-torchtpu-headless:8474
         TPU_WORKER_ID=1
         TPU_NAME=v6e-16-0
         

### Ironwood (TPU7x)
         
         TPU_WORKER_HOSTNAMES=tpu7x-16-0-0.ray-serve-torchtpu-headless,tpu7x-16-0-1.ray-serve-torchtpu-headless
         TORCH_TPU_TOPOLOGY=2,2,2,2
         TORCH_TPU_SLICEBUILDER_ADDRESSES=tpu7x-16-0-0.ray-serve-torchtpu-headless:8471,tpu7x-16-0-0.ray-serve-torchtpu-headless:8472,tpu7x-16-0-0.ray-serve-torchtpu-headless:8473,tpu7x-16-0-0.ray-serve-torchtpu-headless:8474,tpu7x-16-0-0.ray-serve-torchtpu-headless:8475,tpu7x-16-0-0.ray-serve-torchtpu-headless:8476,tpu7x-16-0-0.ray-serve-torchtpu-headless:8477,tpu7x-16-0-0.ray-serve-torchtpu-headless:8478,tpu7x-16-0-1.ray-serve-torchtpu-headless:8471,tpu7x-16-0-1.ray-serve-torchtpu-headless:8472,tpu7x-16-0-1.ray-serve-torchtpu-headless:8473,tpu7x-16-0-1.ray-serve-torchtpu-headless:8474,tpu7x-16-0-1.ray-serve-torchtpu-headless:8475,tpu7x-16-0-1.ray-serve-torchtpu-headless:8476,tpu7x-16-0-1.ray-serve-torchtpu-headless:8477,tpu7x-16-0-1.ray-serve-torchtpu-headless:8478
         TPU_WORKER_ID=1
         TPU_NAME=tpu7x-16-0
         

You can inspect the TPU worker nodes and their auto-detected `ray.io/tpu-*` labels in the **Cluster** tab of the Ray Dashboard.

  5. Forward local ports to the Ray Dashboard on port 8265 and the Ray Serve HTTP endpoint on port 8000:
         
         kubectl port-forward svc/ray-serve-torchtpu-head-svc 8265:8265 8000:8000 >/dev/null 2>&1 &
         




## Create and deploy the Ray Serve LLM application

Deploy the Ray Serve LLM application on your RayCluster custom resource to serve the `google/gemma-4-26B-A4B-it` model across the multi-host TPU slice.

  1. Review the `serve_vllm_torchtpu.py` script in the sample repository:
         
         from ray.serve.deployment import Application
         from ray.serve.llm import (
             LLMConfig,
             LLMServingArgs,
             ModelLoadingConfig,
             build_openai_app,
         )
         
         
         def app(args: dict[str, str]) -> Application:
             llm_config = LLMConfig(
                 model_loading_config=ModelLoadingConfig(
                     model_id=args.get("model_id", "google/gemma-4-26B-A4B-it"),
                 ),
                 accelerator_type=args.get("accelerator_type", "TPU-V6E"),
                 accelerator_config={
                     "kind": "tpu",
                     "topology": args.get("topology", "4x4"),
                 },
                 placement_group_config={
                     "bundle_per_worker": {"TPU": 1},
                 },
                 engine_kwargs={
                     "tensor_parallel_size": int(args.get("tensor_parallel_size", "16")),
                     "enable_expert_parallel": True,
                     "enable_prefix_caching": True,
                     "language_model_only": True,
                     "disable_hybrid_kv_cache_manager": True,
                     "max_model_len": int(args.get("max_model_len", "8192")),
                     "max_num_batched_tokens": int(
                         args.get("max_num_batched_tokens", "4096")
                     ),
                 },
                 experimental_configs={
                     "stream_batching_interval_ms": 10,
                 },
                 runtime_env={
                     "env_vars": {
                         "TPU_MULTIHOST_BACKEND": "ray",
                         # Execute Gemma 4 routed expert layers on TPU TensorCores instead of SparseCore.
                         "USE_MOE_SPARSE_CORE": "0",
                         "VLLM_RAY_EXTRA_ENV_VARS_TO_COPY": "USE_MOE_SPARSE_CORE",
                     }
                 },
             )
             return build_openai_app(LLMServingArgs(llm_configs=[llm_config]))

The script configures the `LLMConfig` object with the following settings for multi-host TPU serving:

     * The `accelerator_config` and `placement_group_config` fields reserve a placement group on a single TPU slice and allocate one TPU core per vLLM worker across the slice.
     * The `engine_kwargs` field shards the model across all 16 TPU cores by using tensor parallelism and expert parallelism and enables prefix caching. It also disables multimodal inputs to reserve TPU HBM for text inference, uses a unified KV cache layout for Gemma 4 attention layers, and caps the context length at 8,192 tokens and the prefill batch size at 4,096 tokens.
     * The `experimental_configs` field batches outbound token streams every 10 ms to reduce streaming overhead across concurrent requests.
     * The `runtime_env` field enables the Ray multi-host backend for vLLM-TorchTPU (`TPU_MULTIHOST_BACKEND: "ray"`), runs Gemma 4 MoE expert layers on TPU TensorCores instead of SparseCore, and propagates that setting to all 16 worker actors.
  2. Deploy the Ray Serve application on the RayCluster custom resource by using the `serve run` command. The command streams the deployment logs until the model weights finish loading, XLA graph compilation completes across all 16 TPU devices, and the Serve application reaches the `RUNNING` state:

### Trillium (v6e)
         
         ray job submit \
             --address http://localhost:8265 \
             --working-dir . \
             --runtime-env-json '{"excludes": ["ray-env", ".git", "*.whl"]}' \
             -- serve run --non-blocking serve_vllm_torchtpu:app accelerator_type=TPU-V6E topology=4x4
         

### Ironwood (TPU7x)
         
         ray job submit \
             --address http://localhost:8265 \
             --working-dir . \
             --runtime-env-json '{"excludes": ["ray-env", ".git", "*.whl"]}' \
             -- serve run --non-blocking serve_vllm_torchtpu:app accelerator_type=TPU-V7X topology=2x2x2
         

The output is similar to the following:

### Trillium (v6e)
         
         (ServeController pid=1637) INFO 2026-10-13 10:23:05,160 controller 1637 -- Deploying new version of Deployment(name='LLMServer:google--gemma-4-26B-A4B-it', app='default') (initial target replicas: 1).
         (ServeController pid=1637) INFO 2026-10-13 10:23:05,161 controller 1637 -- Deploying new version of Deployment(name='OpenAiIngress', app='default') (initial target replicas: 1).
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=515, ip=10.72.3.21) INFO 10-13 10:24:06 [__init__.py:318] TPU info: node_name=v6e-16-0 | tpu_type=v6e-16 | worker_id=1 | num_chips=4 | num_cores_per_chip=1
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=515, ip=10.72.3.21) INFO 10-13 10:24:06 [__init__.py:238] Platform plugin torchtpu is activated
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=515, ip=10.72.3.21) (EngineCore pid=1041) INFO 10-13 10:24:08 [core.py:112] Initializing a V1 LLM engine (v0.22.1) with config: model='google/gemma-4-26B-A4B-it', speculative_config=None, tokenizer='google/gemma-4-26B-A4B-it', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=16, pipeline_parallel_size=1, data_parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=True, quantization=None, quantization_config=None, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=tpu, ...
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=515, ip=10.72.3.21) (EngineCore pid=1041) (RayWorkerWrapper pid=1017, ip=10.72.14.21) INFO 10-13 10:24:30 [expert_map_manager.py:245] [EP Rank 4/16] Expert parallelism is enabled. Expert placement strategy: linear. Local/global number of experts: 8/128. Experts local to global index map: 0->32, 1->33, 2->34, 3->35, 4->36, 5->37, 6->38, 7->39.
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=515, ip=10.72.3.21) (EngineCore pid=1041) (RayWorkerWrapper pid=856, ip=10.72.6.21) INFO 10-13 10:27:55 [default_loader.py:397] Loading weights took 12.76 seconds
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=515, ip=10.72.3.21) (EngineCore pid=1041) (RayWorkerWrapper pid=856, ip=10.72.6.21) INFO 10-13 10:32:53 [tpu_worker.py:376] Memory statistics | total_hbm_limit_gb=31.25GiB | total_hbm_limit_cap_gb=28.75GiB | total_hbm_used_gb=3.69GiB | kv_cache_headroom_gb=5.0GiB | kv_connector_hbm_reserve_gb=0.0GiB | total_hbm_avail_gb=20.06GiB
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=515, ip=10.72.3.21) (EngineCore pid=1041) INFO 10-13 10:32:54 [kv_cache_utils.py:1733] GPU KV cache size: 600,832 tokens
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=515, ip=10.72.3.21) (EngineCore pid=1041) INFO 10-13 10:32:54 [kv_cache_utils.py:1734] Maximum concurrency for 8,192 tokens per request: 73.34x
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=515, ip=10.72.3.21) INFO 2026-10-13 10:36:59,851 default_LLMServer:google--gemma-4-26B-A4B-it b2grwv9c -- Started vLLM engine.
         INFO 2026-10-13 10:37:05,997 serve 1456 -- Application 'default' is ready at http://127.0.0.1:8000/.
         2026-10-13 10:37:11,447 SUCC cli.py:66 -- ------------------------------------------
         2026-10-13 10:37:11,447 SUCC cli.py:67 -- Job 'raysubmit_94DTwVzR2pvGQVwR' succeeded
         2026-10-13 10:37:11,447 SUCC cli.py:68 -- ------------------------------------------
         

### Ironwood (TPU7x)
         
         (ServeController pid=2042) INFO 2026-10-13 10:24:38,092 controller 2042 -- Deploying new version of Deployment(name='LLMServer:google--gemma-4-26B-A4B-it', app='default') (initial target replicas: 1).
         (ServeController pid=2042) INFO 2026-10-13 10:24:38,093 controller 2042 -- Deploying new version of Deployment(name='OpenAiIngress', app='default') (initial target replicas: 1).
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=316, ip=172.16.7.5) INFO 10-13 10:24:49 [__init__.py:318] TPU info: node_name=tpu7x-16-0 | tpu_type=tpu7x-16 | worker_id=0 | num_chips=8 | num_cores_per_chip=2
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=316, ip=172.16.7.5) INFO 10-13 10:24:49 [__init__.py:238] Platform plugin torchtpu is activated
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=316, ip=172.16.7.5) (EngineCore pid=719) INFO 10-13 10:25:23 [core.py:112] Initializing a V1 LLM engine (v0.22.1) with config: model='google/gemma-4-26B-A4B-it', speculative_config=None, tokenizer='google/gemma-4-26B-A4B-it', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=16, pipeline_parallel_size=1, data_parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=True, quantization=None, quantization_config=None, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=tpu, ...
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=316, ip=172.16.7.5) (EngineCore pid=719) (RayWorkerWrapper pid=602, ip=172.16.10.6) INFO 10-13 10:25:44 [expert_map_manager.py:245] [EP Rank 8/16] Expert parallelism is enabled. Expert placement strategy: linear. Local/global number of experts: 8/128. Experts local to global index map: 0->64, 1->65, 2->66, 3->67, 4->68, 5->69, 6->70, 7->71.
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=316, ip=172.16.7.5) (EngineCore pid=719) (RayWorkerWrapper pid=762) INFO 10-13 10:29:06 [default_loader.py:397] Loading weights took 11.69 seconds
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=316, ip=172.16.7.5) (EngineCore pid=719) (RayWorkerWrapper pid=604, ip=172.16.10.6) INFO 10-13 10:34:51 [tpu_worker.py:376] Memory statistics | total_hbm_limit_gb=94.75GiB | total_hbm_limit_cap_gb=87.17GiB | total_hbm_used_gb=3.74GiB | kv_cache_headroom_gb=5.0GiB | kv_connector_hbm_reserve_gb=0.0GiB | total_hbm_avail_gb=78.43GiB
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=316, ip=172.16.7.5) (EngineCore pid=719) INFO 10-13 10:34:58 [kv_cache_utils.py:1733] GPU KV cache size: 2,349,568 tokens
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=316, ip=172.16.7.5) (EngineCore pid=719) INFO 10-13 10:34:58 [kv_cache_utils.py:1734] Maximum concurrency for 8,192 tokens per request: 286.81x
         (ServeReplica:default:LLMServer:google--gemma-4-26B-A4B-it pid=316, ip=172.16.7.5) INFO 2026-10-13 10:40:13,586 default_LLMServer:google--gemma-4-26B-A4B-it a15k5cv3 -- Started vLLM engine.
         INFO 2026-10-13 10:40:18,415 serve 1953 -- Application 'default' is ready at http://127.0.0.1:8000/.
         2026-10-13 10:40:24,372 SUCC cli.py:66 -- ------------------------------------------
         2026-10-13 10:40:24,372 SUCC cli.py:67 -- Job 'raysubmit_mzWQDQGDM9QSgcMN' succeeded
         2026-10-13 10:40:24,372 SUCC cli.py:68 -- ------------------------------------------
         




## Query the served model

After the Ray Serve application reaches the `RUNNING` state, verify the registered model endpoint, send an OpenAI-compatible `/v1/chat/completions` request through port 8000, and optionally benchmark throughput and latency.

  1. Verify that the model is registered on the `/v1/models` endpoint:
         
         curl http://localhost:8000/v1/models
         

The output is similar to the following:
         
         {"data":[{"id":"google/gemma-4-26B-A4B-it","object":"model","owned_by":"organization-owner","permission":[],"metadata":{"model_id":"google/gemma-4-26B-A4B-it","input_modality":"text","max_request_context_length":8192}}],"object":"list"}
         

  2. Send a chat completion prompt to the `/v1/chat/completions` endpoint:
         
         curl -X POST http://localhost:8000/v1/chat/completions \
             -H "Content-Type: application/json" \
             -d '{
                 "model": "google/gemma-4-26B-A4B-it",
                 "messages": [
                     {"role": "system", "content": "You are a helpful AI assistant."},
                     {"role": "user", "content": "Explain in one sentence how tensor parallelism and expert parallelism accelerate Mixture-of-Experts LLM inference on TPUs."}
                 ],
                 "max_tokens": 128,
                 "temperature": 0.0
             }'
         

The output on Ironwood (TPU7x) is similar to the following:
         
         {"id":"chatcmpl-ec30e61c-011d-49cd-989a-9ae9f59448a8","object":"chat.completion","created":1791887860,"model":"google/gemma-4-26B-A4B-it","choices":[{"index":0,"message":{"role":"assistant","content":"Tensor parallelism accelerates inference by partitioning large weight matrices across TPU cores to reduce per-device memory and computation, while expert parallelism distributes the specialized MoE layers across different devices to enable massive model scaling and parallelize the processing of different tokens through different experts.","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning":null},"logprobs":null,"finish_reason":"stop","stop_reason":106,"token_ids":null,"routed_experts":null}],"service_tier":null,"system_fingerprint":"vllm-0.22.1-tp16-ep-aaf76e1a","usage":{"prompt_tokens":49,"total_tokens":100,"completion_tokens":51,"prompt_tokens_details":null},"prompt_logprobs":null,"prompt_token_ids":null,"prompt_text":null,"kv_transfer_params":null}
         

  3. Optional: Benchmark serving throughput and latency by using the `vllm bench serve` command. The following command runs the `vllm bench serve` HTTP load-generator client from a Ray TPU worker Pod and sends 64 concurrent requests to the Ray Serve HTTP proxy on port 8000:
         
         WORKER_POD=$(kubectl get pods -l ray.io/node-type=worker -o jsonpath='{.items[0].metadata.name}')
         kubectl exec -it ${WORKER_POD} -- vllm bench serve \
             --backend openai-chat \
             --endpoint /v1/chat/completions \
             --model google/gemma-4-26B-A4B-it \
             --dataset-name random \
             --random-input-len 1024 \
             --random-output-len 512 \
             --max-concurrency 32 \
             --num-prompts 64 \
             --num-warmups 4 \
             --temperature 0.0 \
             --ignore-eos \
             --host ray-serve-torchtpu-head-svc \
             --port 8000
         

The output is similar to the following:

### Trillium (v6e)
         
         ============ Serving Benchmark Result ============
         Successful requests:                     64
         Failed requests:                         0
         Maximum request concurrency:             32
         Benchmark duration (s):                  8.41
         Total input tokens:                      66392
         Total generated tokens:                  32768
         Request throughput (req/s):              7.61
         Output token throughput (tok/s):         3894.26
         Peak output token throughput (tok/s):    4409.00
         Peak concurrent requests:                64.00
         Total token throughput (tok/s):          11784.50
         ---------------Time to First Token----------------
         Mean TTFT (ms):                          414.57
         Median TTFT (ms):                        348.94
         P99 TTFT (ms):                           640.26
         -----Time per Output Token (excl. 1st token)------
         Mean TPOT (ms):                          7.37
         Median TPOT (ms):                        7.29
         P99 TPOT (ms):                           8.24
         ---------------Inter-token Latency----------------
         Mean ITL (ms):                           7.37
         Median ITL (ms):                         0.00
         P99 ITL (ms):                            25.94
         ==================================================
         

### Ironwood (TPU7x)
         
         ============ Serving Benchmark Result ============
         Successful requests:                     64
         Failed requests:                         0
         Maximum request concurrency:             32
         Benchmark duration (s):                  9.65
         Total input tokens:                      66392
         Total generated tokens:                  32768
         Request throughput (req/s):              6.64
         Output token throughput (tok/s):         3397.33
         Peak output token throughput (tok/s):    4574.00
         Peak concurrent requests:                64.00
         Total token throughput (tok/s):          10280.73
         ---------------Time to First Token----------------
         Mean TTFT (ms):                          654.11
         Median TTFT (ms):                        522.30
         P99 TTFT (ms):                           1288.23
         -----Time per Output Token (excl. 1st token)------
         Mean TPOT (ms):                          8.13
         Median TPOT (ms):                        8.08
         P99 TPOT (ms):                           9.69
         ---------------Inter-token Latency----------------
         Mean ITL (ms):                           8.12
         Median ITL (ms):                         9.31
         P99 ITL (ms):                            26.85
         ==================================================
         




## Deploy declaratively with a RayService custom resource

For production deployments, you can manage both the multi-host Ray cluster and the Ray Serve LLM application as a single declarative [RayService](https://docs.ray.io/en/latest/serve/production-guide/kubernetes.html) custom resource instead of submitting a job manually. Because the Ray Serve LLM builder accepts the model configuration directly in the Serve config, you don't need a separate Python script. KubeRay provisions the cluster, deploys the Serve application, monitors replica health, and creates a Kubernetes ClusterIP Service on port 8000 when the application is ready to serve traffic.

  1. If the RayCluster custom resource from the previous section is still running, stop port forwarding and delete the RayCluster custom resource to release the TPU slice:
         
         pkill -f "kubectl port-forward" || true
         kubectl delete raycluster ray-serve-torchtpu --ignore-not-found
         

  2. Review the RayService manifest for your TPU version in the sample repository:

### Trillium (v6e)
         
         apiVersion: ray.io/v1
         kind: RayService
         metadata:
           name: ray-serve-torchtpu
         spec:
           serveConfigV2: |
             applications:
             - name: default
               route_prefix: /
               import_path: ray.serve.llm:build_openai_app
               args:
                 llm_configs:
                 - model_loading_config:
                     model_id: google/gemma-4-26B-A4B-it
                   accelerator_type: TPU-V6E
                   accelerator_config:
                     kind: tpu
                     topology: 4x4
                   placement_group_config:
                     bundle_per_worker:
                       TPU: 1
                   engine_kwargs:
                     tensor_parallel_size: 16
                     enable_expert_parallel: true
                     enable_prefix_caching: true
                     language_model_only: true
                     disable_hybrid_kv_cache_manager: true
                     max_model_len: 8192
                     max_num_batched_tokens: 4096
                   experimental_configs:
                     stream_batching_interval_ms: 10
                   runtime_env:
                     env_vars:
                       TPU_MULTIHOST_BACKEND: "ray"
                       # Execute Gemma 4 routed expert layers on TPU TensorCores instead of SparseCore.
                       USE_MOE_SPARSE_CORE: "0"
                       VLLM_RAY_EXTRA_ENV_VARS_TO_COPY: "USE_MOE_SPARSE_CORE"
           rayClusterConfig:
             headGroupSpec:
               rayStartParams:
                 num-cpus: "0"
               template:
                 spec:
                   containers:
                   - name: ray-head
                     image: ${IMAGE_URI}
                     env:
                     - name: HF_TOKEN
                       valueFrom:
                         secretKeyRef:
                           name: hf-secret
                           key: hf_api_token
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
                         cpu: "4"
                         memory: "16Gi"
                       requests:
                         cpu: "4"
                         memory: "16Gi"
             workerGroupSpecs:
             - groupName: v6e-16
               replicas: 1
               numOfHosts: 4
               template:
                 spec:
                   containers:
                   - name: ray-worker
                     image: ${IMAGE_URI}
                     env:
                     - name: HF_TOKEN
                       valueFrom:
                         secretKeyRef:
                           name: hf-secret
                           key: hf_api_token
                     resources:
                       limits:
                         cpu: "64"
                         memory: "200Gi"
                         google.com/tpu: "4"
                       requests:
                         cpu: "64"
                         memory: "200Gi"
                         google.com/tpu: "4"
                     volumeMounts:
                     - mountPath: /dev/shm
                       name: dshm
                   volumes:
                   - name: dshm
                     emptyDir:
                       medium: Memory
                       sizeLimit: 100Gi
                   nodeSelector:
                     cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                     cloud.google.com/gke-tpu-topology: 4x4

### Ironwood (TPU7x)
         
         apiVersion: ray.io/v1
         kind: RayService
         metadata:
           name: ray-serve-torchtpu
         spec:
           serveConfigV2: |
             applications:
             - name: default
               route_prefix: /
               import_path: ray.serve.llm:build_openai_app
               args:
                 llm_configs:
                 - model_loading_config:
                     model_id: google/gemma-4-26B-A4B-it
                   accelerator_type: TPU-V7X
                   accelerator_config:
                     kind: tpu
                     topology: 2x2x2
                   placement_group_config:
                     bundle_per_worker:
                       TPU: 1
                   engine_kwargs:
                     tensor_parallel_size: 16
                     enable_expert_parallel: true
                     enable_prefix_caching: true
                     language_model_only: true
                     disable_hybrid_kv_cache_manager: true
                     max_model_len: 8192
                     max_num_batched_tokens: 4096
                   experimental_configs:
                     stream_batching_interval_ms: 10
                   runtime_env:
                     env_vars:
                       TPU_MULTIHOST_BACKEND: "ray"
                       # Execute Gemma 4 routed expert layers on TPU TensorCores instead of SparseCore.
                       USE_MOE_SPARSE_CORE: "0"
                       VLLM_RAY_EXTRA_ENV_VARS_TO_COPY: "USE_MOE_SPARSE_CORE"
           rayClusterConfig:
             headGroupSpec:
               rayStartParams:
                 num-cpus: "0"
               template:
                 spec:
                   containers:
                   - name: ray-head
                     image: ${IMAGE_URI}
                     env:
                     - name: HF_TOKEN
                       valueFrom:
                         secretKeyRef:
                           name: hf-secret
                           key: hf_api_token
                     - name: RAY_TPU_RESOURCE_PER_CHIP
                       value: "2"
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
                         cpu: "4"
                         memory: "16Gi"
                       requests:
                         cpu: "4"
                         memory: "16Gi"
             workerGroupSpecs:
             - groupName: tpu7x-16
               replicas: 1
               numOfHosts: 2
               resources:
                 # Advertises 8 logical TPU cores (2 chiplets per physical chip) per host.
                 TPU: "8"
               template:
                 spec:
                   containers:
                   - name: ray-worker
                     image: ${IMAGE_URI}
                     env:
                     - name: HF_TOKEN
                       valueFrom:
                         secretKeyRef:
                           name: hf-secret
                           key: hf_api_token
                     - name: RAY_TPU_RESOURCE_PER_CHIP
                       value: "2"
                     resources:
                       limits:
                         cpu: "64"
                         memory: "250Gi"
                         google.com/tpu: "4"
                       requests:
                         cpu: "64"
                         memory: "250Gi"
                         google.com/tpu: "4"
                     volumeMounts:
                     - mountPath: /dev/shm
                       name: dshm
                   volumes:
                   - name: dshm
                     emptyDir:
                       medium: Memory
                       sizeLimit: 128Gi
                   nodeSelector:
                     cloud.google.com/gke-tpu-accelerator: tpu7x
                     cloud.google.com/gke-tpu-topology: 2x2x2

  3. Apply the RayService manifest:

### Trillium (v6e)
         
         envsubst < ray-service.tpu-v6e-multihost.yaml | kubectl apply -f -
         

### Ironwood (TPU7x)
         
         envsubst < ray-service.tpu-v7x-multihost.yaml | kubectl apply -f -
         

  4. Wait until the RayService custom resource finishes loading model weights and compiling XLA graphs across the TPU slice and reaches the `Running` state:
         
         kubectl get rayservice ray-serve-torchtpu
         kubectl get svc ray-serve-torchtpu-serve-svc
         

The output is similar to the following:
         
         NAME                 SERVICE STATUS   NUM SERVE ENDPOINTS
         ray-serve-torchtpu   Running          3
         NAME                           TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
         ray-serve-torchtpu-serve-svc   ClusterIP   34.118.239.213   <none>        8000/TCP   29s
         

  5. Forward local port 8000 to the `ray-serve-torchtpu-serve-svc` Service and query the model by using the `curl` commands in Query the served model:
         
         kubectl port-forward svc/ray-serve-torchtpu-serve-svc 8000:8000 >/dev/null 2>&1 &
         


**Success:** You have deployed and queried an MoE Gemma 4 model on a multi-host TPU slice in GKE with Ray Serve LLM, vLLM, and TorchTPU.

## Observe model performance

To monitor TPU TensorCore utilization, HBM usage, and Ray cluster metrics in Cloud Monitoring, see [Collect and view logs and metrics for Ray clusters on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/collect-view-logs-metrics) and [View TPU metrics on the Ray Dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/view-tpu-metrics).

### Access the Ray Dashboard

To inspect the status of your Ray Serve deployments, replica actors, node labels, and query latencies in the built-in Ray Dashboard, follow these steps:

  1. If port forwarding to the Ray head service is not already running, start it in the background:
         
         kubectl port-forward svc/ray-serve-torchtpu-head-svc 8265:8265 8000:8000 >/dev/null 2>&1 &
         

  2. In Cloud Shell, click ![Web Preview icon.](https://docs.cloud.google.com/static/shell/docs/images/web_preview.svg)**Web Preview** and select **Preview on port 8265** , or open `http://localhost:8265` in your local browser.

  3. Click the **Serve** , **Cluster** , and **Metrics** tabs to view your vLLM deployments, replica health, auto-detected `ray.io/tpu-*` node labels, request latency metrics, and the **TPU Utilization by Node** graph.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete the RayService or RayCluster custom resource, the GKE cluster, and the Artifact Registry repository:

  1. Stop the background port-forwarding process and delete the Ray custom resources and Kubernetes Secret:
         
         pkill -f "kubectl port-forward" || true
         kubectl delete rayservice ray-serve-torchtpu --ignore-not-found
         kubectl delete raycluster ray-serve-torchtpu --ignore-not-found
         kubectl delete secret hf-secret --ignore-not-found
         

  2. Delete the GKE cluster:

### Autopilot
         
         gcloud container clusters delete ${CLUSTER_NAME} \
             --region=${REGION}
         

### Standard
         
         gcloud container clusters delete ${CLUSTER_NAME} \
             --zone=${ZONE}
         

  3. Delete the Artifact Registry repository:
         
         gcloud artifacts repositories delete ${ARTIFACT_REGISTRY} \
             --location=${REGION}
         




## What's next

  * Learn more about [PyTorch on Cloud TPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu).
  * Explore the [TorchTPU documentation](https://torchtpu.readthedocs.io/).
  * Learn how to [fine-tune models on multi-host TPUs with Ray and TorchTPU](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/train-models-tpu-ray-torchtpu).
  * Learn how to [serve Gemma open models using multi-host TPUs on GKE with Ray](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multi-host-tpu-llm).
  * Learn how to manage Ray Serve deployments declaratively with a [KubeRay RayService](https://docs.ray.io/en/latest/serve/production-guide/kubernetes.html) custom resource.
  * Read [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Explore the [Ray Serve LLM documentation](https://docs.ray.io/en/latest/serve/llm/index.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
