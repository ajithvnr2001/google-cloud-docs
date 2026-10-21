---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/train-models-tpu-ray-torchtpu/
title: Fine-tune models on multi-host TPUs with Ray and TorchTPU \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:21:59.656276+00:00
---

# Fine-tune models on multi-host TPUs with Ray and TorchTPU  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/train-models-tpu-ray-torchtpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Fine-tune models on multi-host TPUs with Ray and TorchTPU Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to run distributed PyTorch workloads and fine-tune a [Gemma 4](https://huggingface.co/google/gemma-4-E2B-it) model on multi-host [Cloud TPU](https://docs.cloud.google.com/tpu) slices in Google Kubernetes Engine (GKE) by using [Ray Core](https://docs.ray.io/en/latest/ray-core/walkthrough.html), [Ray Train](https://docs.ray.io/en/latest/train/train.html), [PyTorch Fully Sharded Data Parallel (FSDP2)](https://docs.pytorch.org/docs/stable/distributed.fsdp.fully_shard.html), and [TorchTPU](https://github.com/google-pytorch/torch_tpu).

This tutorial is intended for machine learning (ML) engineers, platform admins and operators, and data and AI specialists who want to orchestrate distributed PyTorch training workloads on multi-host TPU slices in Kubernetes. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before starting this tutorial, ensure that you're familiar with the following:

  * [About GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)
  * [Multi-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host)
  * [About Ray on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview)



## Background

This section describes the key technologies used in this tutorial.

### TPUs

[Tensor Processing Units](https://docs.cloud.google.com/tpu) (TPUs) are Google custom-designed accelerators for machine learning workloads. This tutorial supports both [TPU Trillium (v6e)](https://docs.cloud.google.com/tpu/docs/v6e) and [Ironwood (TPU7x)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpu-ironwood). In a multi-host TPU slice, multiple TPU hosts communicate directly over a high-speed Inter-Chip Interconnect (ICI) network, providing the aggregate High Bandwidth Memory (HBM) and low-latency collective communication required to train models that exceed the memory capacity of a single chip or TPU host.

### TorchTPU

[TorchTPU](https://github.com/google-pytorch/torch_tpu) is an open-source PyTorch backend for Cloud TPU, developed in collaboration between Google and Meta. With TorchTPU, you can run existing PyTorch models on TPU hardware with minimal code changes and scale training and inference workloads from a single chip to multi-slice TPU pods through the Accelerated Linear Algebra (XLA) compiler. TorchTPU uses a one-process-per-device execution model over the TPU ICI network and supports standard PyTorch APIs, including eager execution, `torch.compile`, `torch.distributed`, `DeviceMesh`, `DTensor`, and [Fully Sharded Data Parallel (FSDP2)](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html).

### KubeRay and Ray on TPUs

[KubeRay](https://github.com/ray-project/kuberay) is a Kubernetes operator for deploying and managing Ray applications. Enabling the [Ray on GKE add-on](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview) deploys the managed KubeRay operator and the [KubeRay TPU webhook](https://github.com/ai-on-gke/kuberay-tpu-webhook). When KubeRay creates worker Pods that request `google.com/tpu` resources, the webhook automatically configures the Pod hostnames, headless Service, and TPU environment variables required for multi-host coordination.

Ray detects the TPU topology on each node at startup and schedules distributed workloads across TPU slices. You can orchestrate distributed TorchTPU workloads at two levels:

  * [Ray Core](https://docs.ray.io/en/latest/ray-core/walkthrough.html) provides topology-aware placement groups and actor scheduling for custom distributed execution loops, such as tensor-parallel computation or reinforcement learning (RL) pipelines.
  * [Ray Train](https://docs.ray.io/en/latest/train/train.html) provides managed distributed data-parallel and model-parallel training, including PyTorch Distributed Data Parallel (DDP), PyTorch FSDP2, and JAX single program, multiple data (SPMD), with built-in checkpointing and automatic failure recovery.



## Objectives

This tutorial shows you how to do the following:

  1. Create a GKE cluster in Autopilot or Standard on TPU Trillium (v6e) or Ironwood (TPU7x).
  2. Build a container image that layers Ray and Hugging Face training libraries on top of the TorchTPU base image.
  3. Deploy a RayCluster custom resource to provision the head and TPU worker nodes.
  4. Run distributed tensor-parallel computation with PyTorch `DeviceMesh` and `DTensor` across a TPU slice by using Ray Core.
  5. Fine-tune a Gemma 4 model with PyTorch FSDP2 across a multi-host TPU slice by using Ray Train.



## Costs

In this tutorial, you use the following billable components of Google Cloud:

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Cloud TPU](https://docs.cloud.google.com/tpu/pricing)
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

When you finish the tasks that are described in this tutorial, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Artifact Registry API and the Cloud Storage API and the Google Kubernetes Engine API. 
[ Enable APIs ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,artifactregistry.googleapis.com,storage.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Verify that your project has sufficient quota for TPU Trillium (v6e) or Ironwood (TPU7x) capacity in your selected zone. For more information, see [Cloud TPU quotas](https://docs.cloud.google.com/tpu/docs/quota).
  * Ensure that your account has the following [IAM roles](https://docs.cloud.google.com/iam/docs/roles-permissions): 
    * [Kubernetes Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
    * [Artifact Registry Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)
    * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



## Prepare your environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with the software that you need for this tutorial, including `kubectl`, `docker`, `python3`, and the `gcloud` CLI.

To set up your environment with Cloud Shell, follow these steps:

  1. In the Google Cloud console, launch a Cloud Shell session by clicking ![Cloud Shell activation icon.](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** in the [Google Cloud console](http://console.cloud.google.com). This action launches a session in the bottom pane of Google Cloud console.

  2. Clone the `kubernetes-engine-samples` repository and change to the sample directory for this tutorial:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
         cd kubernetes-engine-samples/ai-ml/gke-ray/raytrain/torchtpu
         

  3. Create and activate a local Python virtual environment with the Ray CLI installed:
         
         python3 -m venv ~/ray-env
         source ~/ray-env/bin/activate
         pip install "ray[default]==2.58.0"
         

  4. To download the Gemma 4 model weights, acknowledge the Google license agreement on Hugging Face:

     1. Go to the [Gemma 4 model page on Hugging Face](https://huggingface.co/google/gemma-4-E2B-it).
     2. Sign in and accept the license terms by clicking **Agree and access repository**.
     3. In your Hugging Face account settings, generate a [user access token](https://huggingface.co/settings/tokens) with `Read` permissions.
  5. Set the environment variables for your Google Cloud project, cluster, Cloud Storage bucket, and Hugging Face token:
         
         export PROJECT_ID=PROJECT_ID
         export CLUSTER_NAME=CLUSTER_NAME
         export REGION=REGION
         export ZONE=ZONE
         export ARTIFACT_REGISTRY=ARTIFACT_REGISTRY
         export BUCKET_NAME=BUCKET_NAME
         export HF_TOKEN=HF_TOKEN
         export IMAGE_URI=${REGION}-docker.pkg.dev/${PROJECT_ID}/${ARTIFACT_REGISTRY}/ray-torchtpu:latest
         gcloud config set project ${PROJECT_ID}
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `CLUSTER_NAME`: the name of your GKE cluster, such as `ray-torchtpu-cluster`.
     * `REGION`: the region where your Artifact Registry repository, Cloud Storage bucket, and TPU capacity are located.
     * `ZONE`: the zone where your TPU capacity is available. For available regions and zones by TPU version, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).
     * `ARTIFACT_REGISTRY`: the name of your Artifact Registry Docker repository, such as `ray-torchtpu`.
     * `BUCKET_NAME`: the name of your Cloud Storage bucket for storing Ray Train checkpoints, such as `PROJECT_ID-ray-torchtpu`.
     * `HF_TOKEN`: your Hugging Face access token.



## Create a GKE cluster

You can run distributed TorchTPU training workloads in a GKE Autopilot or Standard cluster with the managed [Ray operator](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/enable-ray-on-gke) add-on enabled.

  1. Create your GKE cluster and configure credentials for the `kubectl` command-line tool:

### Autopilot

     1. Create a regional GKE Autopilot cluster with the Ray operator add-on enabled:
            
            gcloud container clusters create-auto ${CLUSTER_NAME} \
                --project=${PROJECT_ID} \
                --region=${REGION} \
                --cluster-version=1.36 \
                --enable-ray-operator
            

When you deploy the RayCluster custom resource in a later step, GKE Autopilot automatically provisions the CPU head node and the multi-host TPU slice that match your Pod resource requests and node selectors.

     2. Configure the `kubectl` command-line tool to communicate with your cluster:
            
            gcloud container clusters get-credentials ${CLUSTER_NAME} \
                --project=${PROJECT_ID} \
                --region=${REGION}
            

### Standard

     1. Create a zonal GKE Standard cluster with a CPU node pool to host the Ray head Pod, [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming), GKE Dataplane V2, and Workload Identity Federation for GKE enabled:
            
            gcloud container clusters create ${CLUSTER_NAME} \
                --project=${PROJECT_ID} \
                --zone=${ZONE} \
                --cluster-version=1.36 \
                --machine-type=n2-standard-8 \
                --num-nodes=1 \
                --addons=RayOperator \
                --enable-image-streaming \
                --enable-dataplane-v2 \
                --workload-pool=${PROJECT_ID}.svc.id.goog
            

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

  2. Create a Cloud Storage bucket to store shared Ray Train checkpoints across the multi-host TPU nodes and grant the `default` Kubernetes ServiceAccount resource access to the bucket:
         
         gcloud storage buckets create gs://${BUCKET_NAME} --location=${REGION}
         
         PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
         gcloud storage buckets add-iam-policy-binding gs://${BUCKET_NAME} \
             --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/default/sa/default" \
             --role="roles/storage.objectAdmin"
         

  3. Create a Kubernetes Secret with your Hugging Face access token so that Ray Pods can download the gated Gemma 4 weights:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_api_token=${HF_TOKEN}
         




## Build the container image

Build a container image that installs Ray and the Hugging Face training libraries on top of the prebuilt TorchTPU base image, which includes TorchTPU and the `libtpu` library.

  1. Create an Artifact Registry Docker repository and configure Docker authentication:
         
         gcloud artifacts repositories create ${ARTIFACT_REGISTRY} \
             --repository-format=docker \
             --location=${REGION}
         
         gcloud auth configure-docker ${REGION}-docker.pkg.dev,us-docker.pkg.dev
         

  2. Inspect the `Dockerfile` in the sample directory:
         
         FROM us-docker.pkg.dev/ml-oss-artifacts-transient/torch-tpu-docker-container/torch-tpu:nightly
         
         # Install wget for KubeRay health probes, Ray (Core, Dashboard, and Train), and Hugging Face libraries for fine-tuning
         RUN apt-get update && apt-get install -y --no-install-recommends wget \
             && rm -rf /var/lib/apt/lists/* \
             && pip install --no-cache-dir \
             "ray[default,train]==2.58.0" \
             "transformers>=5.5.0" \
             datasets

Single-slice training with the Ray `TorchTrainer` class and per-chiplet scheduling on Ironwood (TPU7x) require Ray version 2.58.0 or later, and fine-tuning Gemma 4 requires the `transformers` library version 5.5.0 or later.

  3. Build and push the image to Artifact Registry:
         
         docker build -t ${IMAGE_URI} .
         docker push ${IMAGE_URI}
         




## Deploy the RayCluster custom resource

Deploy a RayCluster custom resource that provisions a CPU head Pod, an in-memory `/dev/shm` volume for the Ray shared-memory object store, and a multi-host TPU worker group.

  1. Review the RayCluster manifest for your TPU version in the sample repository:

### Trillium (v6e)
         
         apiVersion: ray.io/v1
         kind: RayCluster
         metadata:
           name: ray-torchtpu-cluster
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
           name: ray-torchtpu-cluster
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
         

  3. Wait until the RayCluster head Pod and all TPU worker Pods reach the `Running` state:
         
         kubectl get pods -l ray.io/cluster=ray-torchtpu-cluster
         

The output is similar to the following:

### Trillium (v6e)
         
         NAME                                         READY   STATUS    RESTARTS   AGE
         ray-torchtpu-cluster-head-pdpk6              1/1     Running   0          2m30s
         ray-torchtpu-cluster-v6e-16-worker-brwpc     1/1     Running   0          2m30s
         ray-torchtpu-cluster-v6e-16-worker-dx4w7     1/1     Running   0          2m30s
         ray-torchtpu-cluster-v6e-16-worker-h4d4w     1/1     Running   0          2m30s
         ray-torchtpu-cluster-v6e-16-worker-t2g24     1/1     Running   0          2m30s
         

### Ironwood (TPU7x)
         
         NAME                                         READY   STATUS    RESTARTS   AGE
         ray-torchtpu-cluster-head-k9x2m              1/1     Running   0          2m30s
         ray-torchtpu-cluster-tpu7x-16-worker-7cwpq   1/1     Running   0          2m30s
         ray-torchtpu-cluster-tpu7x-16-worker-m98r9   1/1     Running   0          2m30s
         

  4. Inspect the environment variables on one of the worker Pods to confirm that the KubeRay TPU webhook injected the multi-host TPU coordination and TorchTPU topology variables:
         
         kubectl get pods -l ray.io/node-type=worker \
             -o=jsonpath='{range .items[0].spec.containers[0].env[*]}{.name}={.value}{"\n"}{end}' \
             | grep -E "TPU_WORKER_ID|TPU_WORKER_HOSTNAMES|TPU_NAME|TORCH_TPU_TOPOLOGY|TORCH_TPU_SLICEBUILDER_ADDRESSES"
         

The output is similar to the following:

### Trillium (v6e)
         
         TPU_WORKER_HOSTNAMES=v6e-16-0-0.ray-torchtpu-cluster-headless,v6e-16-0-1.ray-torchtpu-cluster-headless,v6e-16-0-2.ray-torchtpu-cluster-headless,v6e-16-0-3.ray-torchtpu-cluster-headless
         TORCH_TPU_TOPOLOGY=4,4,1
         TORCH_TPU_SLICEBUILDER_ADDRESSES=v6e-16-0-0.ray-torchtpu-cluster-headless:8471,v6e-16-0-0.ray-torchtpu-cluster-headless:8472,v6e-16-0-0.ray-torchtpu-cluster-headless:8473,v6e-16-0-0.ray-torchtpu-cluster-headless:8474,v6e-16-0-1.ray-torchtpu-cluster-headless:8471,v6e-16-0-1.ray-torchtpu-cluster-headless:8472,v6e-16-0-1.ray-torchtpu-cluster-headless:8473,v6e-16-0-1.ray-torchtpu-cluster-headless:8474,v6e-16-0-2.ray-torchtpu-cluster-headless:8471,v6e-16-0-2.ray-torchtpu-cluster-headless:8472,v6e-16-0-2.ray-torchtpu-cluster-headless:8473,v6e-16-0-2.ray-torchtpu-cluster-headless:8474,v6e-16-0-3.ray-torchtpu-cluster-headless:8471,v6e-16-0-3.ray-torchtpu-cluster-headless:8472,v6e-16-0-3.ray-torchtpu-cluster-headless:8473,v6e-16-0-3.ray-torchtpu-cluster-headless:8474
         TPU_WORKER_ID=3
         TPU_NAME=v6e-16-0
         

### Ironwood (TPU7x)
         
         TPU_WORKER_HOSTNAMES=tpu7x-16-0-0.ray-torchtpu-cluster-headless,tpu7x-16-0-1.ray-torchtpu-cluster-headless
         TORCH_TPU_TOPOLOGY=2,2,2,2
         TORCH_TPU_SLICEBUILDER_ADDRESSES=tpu7x-16-0-0.ray-torchtpu-cluster-headless:8471,tpu7x-16-0-0.ray-torchtpu-cluster-headless:8472,tpu7x-16-0-0.ray-torchtpu-cluster-headless:8473,tpu7x-16-0-0.ray-torchtpu-cluster-headless:8474,tpu7x-16-0-0.ray-torchtpu-cluster-headless:8475,tpu7x-16-0-0.ray-torchtpu-cluster-headless:8476,tpu7x-16-0-0.ray-torchtpu-cluster-headless:8477,tpu7x-16-0-0.ray-torchtpu-cluster-headless:8478,tpu7x-16-0-1.ray-torchtpu-cluster-headless:8471,tpu7x-16-0-1.ray-torchtpu-cluster-headless:8472,tpu7x-16-0-1.ray-torchtpu-cluster-headless:8473,tpu7x-16-0-1.ray-torchtpu-cluster-headless:8474,tpu7x-16-0-1.ray-torchtpu-cluster-headless:8475,tpu7x-16-0-1.ray-torchtpu-cluster-headless:8476,tpu7x-16-0-1.ray-torchtpu-cluster-headless:8477,tpu7x-16-0-1.ray-torchtpu-cluster-headless:8478
         TPU_WORKER_ID=1
         TPU_NAME=tpu7x-16-0
         

  5. Establish a port-forwarding session to the Ray head service:
         
         kubectl port-forward svc/ray-torchtpu-cluster-head-svc 8265:8265 >/dev/null 2>&1 &
         

You can inspect the TPU worker nodes and their auto-detected `ray.io/tpu-*` labels in the **Cluster** tab of the Ray Dashboard.




## Run distributed tensor parallelism with Ray Core

Ray Core provides the [`slice_placement_group`](https://docs.ray.io/en/latest/ray-core/api/doc/ray.util.tpu.slice_placement_group.html) function in the `ray.util.tpu` module to reserve an intact multi-host TPU slice and the [`PlacementGroupSchedulingStrategy`](https://docs.ray.io/en/latest/ray-core/api/doc/ray.util.scheduling_strategies.PlacementGroupSchedulingStrategy.html) class to schedule one Ray actor per logical TPU device across the slice.

  1. Review the `ray_core_collectives.py` script in the sample repository:
         
         import argparse
         import os
         
         import ray
         from ray.util.scheduling_strategies import PlacementGroupSchedulingStrategy
         from ray.util.tpu import (
             get_tpu_version_from_type,
             slice_placement_group,
         )
         import torch
         import torch.distributed as dist
         from torch.distributed.device_mesh import init_device_mesh
         from torch.distributed.tensor.parallel import (
             ColwiseParallel,
             RowwiseParallel,
             parallelize_module,
         )
         import torch.nn as nn
         import torch_tpu  # noqa: F401
         
         RANDOM_SEED = 42
         
         
         class FeedForward(nn.Module):
             """Two-layer feed-forward block for tensor-parallel sharding across a TPU slice."""
         
             def __init__(self, hidden_dim: int):
                 super().__init__()
                 self.w1 = nn.Linear(hidden_dim, 4 * hidden_dim, bias=False)
                 self.act = nn.SiLU()
                 self.w2 = nn.Linear(4 * hidden_dim, hidden_dim, bias=False)
         
             def forward(self, x: torch.Tensor) -> torch.Tensor:
                 return x + self.w2(self.act(self.w1(x)))
         
         
         @ray.remote
         class TorchTPUSliceWorker:
             """Ray actor bound to a single logical TPU device within a slice placement group."""
         
             def __init__(self, devices_per_host: int):
                 self.node_ip = ray.util.get_node_ip_address()
                 hosts = os.environ["TPU_WORKER_HOSTNAMES"].split(",")
                 self.worker_id = int(os.environ.get("TPU_WORKER_ID", "0"))
                 self.local_rank = int(
                     ray.get_runtime_context().get_accelerator_ids()["TPU"][0]
                 )
                 self.rank = self.worker_id * devices_per_host + self.local_rank
                 # Set per-process PyTorch env:// variables from the webhook's host-level
                 # TPU metadata and Ray's assigned local device ID (TorchTrainer sets these
                 # automatically in the Ray Train section below).
                 os.environ.update(
                     {
                         "MASTER_ADDR": hosts[0],
                         "MASTER_PORT": "29500",
                         "WORLD_SIZE": str(len(hosts) * devices_per_host),
                         "RANK": str(self.rank),
                         "LOCAL_RANK": str(self.local_rank),
                         "LOCAL_WORLD_SIZE": str(devices_per_host),
                     }
                 )
         
             def run_tensor_parallel_step(
                 self,
                 batch_size: int = 64,
                 hidden_dim: int = 128,
             ) -> dict:
                 dist.init_process_group(backend="tpu_dist")
                 world_size = dist.get_world_size()
                 device = torch.device("tpu")
         
                 # 1. Compute single-device reference output on CPU with identical seed.
                 torch.manual_seed(RANDOM_SEED)
                 ref_model = FeedForward(hidden_dim).eval()
                 inputs_cpu = torch.randn(batch_size, hidden_dim)
                 with torch.no_grad():
                     ref_output = ref_model(inputs_cpu)
         
                 # 2. Shard the model across all TPU devices in the slice with DTensor TP.
                 torch.manual_seed(RANDOM_SEED)
                 tp_model = FeedForward(hidden_dim).to(device).eval()
                 mesh = init_device_mesh("tpu", (world_size,))
                 tp_model = parallelize_module(
                     tp_model,
                     mesh,
                     {"w1": ColwiseParallel(), "w2": RowwiseParallel()},
                 )
         
                 with torch.no_grad():
                     tp_output = tp_model(inputs_cpu.to(device)).cpu()
         
                 torch.testing.assert_close(tp_output, ref_output, rtol=1e-3, atol=1e-2)
                 max_abs_diff = float((tp_output - ref_output).abs().max().item())
         
                 # 3. Verify direct ICI all_reduce across all ranks in the slice.
                 rank_tensor = torch.full(
                     (4,), float(self.rank + 1), dtype=torch.float32, device=device
                 )
                 dist.all_reduce(rank_tensor, op=dist.ReduceOp.SUM)
                 all_reduce_sum = rank_tensor.cpu().tolist()
         
                 dist.destroy_process_group()
                 return {
                     "rank": self.rank,
                     "local_rank": self.local_rank,
                     "worker_id": self.worker_id,
                     "node_ip": self.node_ip,
                     "all_reduce_sum": all_reduce_sum,
                     "max_abs_diff": max_abs_diff,
                 }
         
         
         def parse_args() -> argparse.Namespace:
             parser = argparse.ArgumentParser(
                 description="Run distributed TorchTPU tensor parallelism across a Ray TPU slice."
             )
             parser.add_argument(
                 "--topology",
                 type=str,
                 default="4x4",
                 help="TPU physical topology.",
             )
             parser.add_argument(
                 "--accelerator-type",
                 type=str,
                 default="TPU-V6E",
                 help="Ray TPU accelerator type (TPU-V6E, TPU-V7X, etc.).",
             )
             return parser.parse_args()
         
         
         def main() -> None:
             args = parse_args()
             ray.init()
         
             slice_handle = slice_placement_group(
                 topology=args.topology,
                 accelerator_version=get_tpu_version_from_type(args.accelerator_type),
                 num_slices=1,
                 resources_per_bundle={"TPU": 1},
             )
             ray.get(slice_handle.placement_group.ready())
         
             devices_per_host = slice_handle.num_bundles // slice_handle.num_hosts
             workers = [
                 TorchTPUSliceWorker.options(
                     resources={"TPU": 1},
                     scheduling_strategy=PlacementGroupSchedulingStrategy(
                         placement_group=slice_handle.placement_group,
                         placement_group_bundle_index=bundle_idx,
                     ),
                 ).remote(devices_per_host)
                 for bundle_idx in range(slice_handle.num_bundles)
             ]
             results = sorted(
                 ray.get([w.run_tensor_parallel_step.remote() for w in workers]),
                 key=lambda r: r["rank"],
             )
         
             expected_sum = sum(range(1, slice_handle.num_bundles + 1))
             for r in results:
                 print(
                     f"Rank {r['rank']:2d} (worker_id={r['worker_id']}, "
                     f"local_rank={r['local_rank']}, ip={r['node_ip']}): "
                     f"all_reduce_sum={r['all_reduce_sum']}"
                 )
                 assert r["all_reduce_sum"] == [float(expected_sum)] * 4
         
             print(
                 f"All {len(results)} TorchTPU ranks verified DTensor TP parity "
                 f"(max_abs_diff={results[0]['max_abs_diff']:.6f}) and "
                 f"all_reduce sum = {expected_sum:.1f}"
             )
             for w in workers:
                 ray.kill(w)
             slice_handle.shutdown()
         
         
         if __name__ == "__main__":
             main()

The script runs distributed tensor parallelism across the TPU slice in three steps:

     1. The `slice_placement_group` function reserves a 16-device TPU slice and schedules one `TorchTPUSliceWorker` actor on each TPU device.
     2. Each actor computes its global rank from its host index and local device ID and then initializes the `tpu_dist` process group.
     3. The `init_device_mesh` and `parallelize_module` functions shard the feed-forward layers across all 16 TPU devices, verify the output against a single-device CPU reference, and run an `all_reduce` collective over ICI.
  2. Submit the Ray Core job for your TPU version:

### Trillium (v6e)
         
         ray job submit \
             --address http://localhost:8265 \
             --working-dir . \
             --runtime-env-json '{"excludes": ["ray-env", ".git", "*.whl"]}' \
             -- python3 ray_core_collectives.py --topology=4x4 --accelerator-type=TPU-V6E
         

### Ironwood (TPU7x)
         
         ray job submit \
             --address http://localhost:8265 \
             --working-dir . \
             --runtime-env-json '{"excludes": ["ray-env", ".git", "*.whl"]}' \
             -- python3 ray_core_collectives.py --topology=2x2x2 --accelerator-type=TPU-V7X
         

The output is similar to the following:

### Trillium (v6e)
         
         Rank  0 (worker_id=0, local_rank=0, ip=10.72.3.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  1 (worker_id=0, local_rank=1, ip=10.72.3.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  2 (worker_id=0, local_rank=2, ip=10.72.3.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  3 (worker_id=0, local_rank=3, ip=10.72.3.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  4 (worker_id=1, local_rank=0, ip=10.72.14.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  5 (worker_id=1, local_rank=1, ip=10.72.14.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  6 (worker_id=1, local_rank=2, ip=10.72.14.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  7 (worker_id=1, local_rank=3, ip=10.72.14.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  8 (worker_id=2, local_rank=0, ip=10.72.7.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  9 (worker_id=2, local_rank=1, ip=10.72.7.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank 10 (worker_id=2, local_rank=2, ip=10.72.7.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank 11 (worker_id=2, local_rank=3, ip=10.72.7.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank 12 (worker_id=3, local_rank=0, ip=10.72.6.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank 13 (worker_id=3, local_rank=1, ip=10.72.6.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank 14 (worker_id=3, local_rank=2, ip=10.72.6.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank 15 (worker_id=3, local_rank=3, ip=10.72.6.20): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         All 16 TorchTPU ranks verified DTensor TP parity (max_abs_diff=0.002470) and all_reduce sum = 136.0
         ------------------------------------------
         Job 'raysubmit_HFTkKrjSnfza3ZFD' succeeded
         ------------------------------------------
         

### Ironwood (TPU7x)
         
         Rank  0 (worker_id=0, local_rank=0, ip=172.16.14.6): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  1 (worker_id=0, local_rank=1, ip=172.16.14.6): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  2 (worker_id=0, local_rank=2, ip=172.16.14.6): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  3 (worker_id=0, local_rank=3, ip=172.16.14.6): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  4 (worker_id=0, local_rank=4, ip=172.16.14.6): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  5 (worker_id=0, local_rank=5, ip=172.16.14.6): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  6 (worker_id=0, local_rank=6, ip=172.16.14.6): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  7 (worker_id=0, local_rank=7, ip=172.16.14.6): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  8 (worker_id=1, local_rank=0, ip=172.16.15.7): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank  9 (worker_id=1, local_rank=1, ip=172.16.15.7): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank 10 (worker_id=1, local_rank=2, ip=172.16.15.7): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank 11 (worker_id=1, local_rank=3, ip=172.16.15.7): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank 12 (worker_id=1, local_rank=4, ip=172.16.15.7): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank 13 (worker_id=1, local_rank=5, ip=172.16.15.7): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank 14 (worker_id=1, local_rank=6, ip=172.16.15.7): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         Rank 15 (worker_id=1, local_rank=7, ip=172.16.15.7): all_reduce_sum=[136.0, 136.0, 136.0, 136.0]
         All 16 TorchTPU ranks verified DTensor TP parity (max_abs_diff=0.002470) and all_reduce sum = 136.0
         ------------------------------------------
         Job 'raysubmit_MrJbAe3hvARBcBN2' succeeded
         ------------------------------------------
         




## Fine-tune a Gemma 4 model with Ray Train and PyTorch FSDP2

The Ray Train [`TorchTrainer`](https://docs.ray.io/en/latest/train/api/doc/ray.train.torch.TorchTrainer.html) class automates TPU slice reservation, worker placement, and `torch.distributed` initialization across a multi-host TPU slice.

  1. Review the `ray_train_llm_finetune.py` script in the sample repository, which fine-tunes the [`google/gemma-4-E2B-it`](https://huggingface.co/google/gemma-4-E2B-it) model on the [`databricks/databricks-dolly-15k`](https://huggingface.co/datasets/databricks/databricks-dolly-15k) instruction dataset:
         
         import argparse
         import os
         import tempfile
         import time
         
         from datasets import load_dataset
         import ray
         import ray.train
         from ray.train import (
             Checkpoint,
             CheckpointConfig,
             RunConfig,
             ScalingConfig,
         )
         from ray.train.torch import TorchConfig, TorchTrainer
         import torch
         from torch.distributed import ReduceOp, all_reduce
         from torch.distributed.checkpoint.state_dict import (
             StateDictOptions,
             get_model_state_dict,
         )
         from torch.distributed.device_mesh import init_device_mesh
         from torch.distributed.fsdp import MixedPrecisionPolicy, fully_shard
         from torch.utils.data import DataLoader
         import torch_tpu  # noqa: F401
         from transformers import (
             AutoModelForCausalLM,
             AutoTokenizer,
             DataCollatorForLanguageModeling,
         )
         
         
         def create_dataloader(
             tokenizer: AutoTokenizer,
             batch_size: int,
             dataset_split: str = "train[:1024]",
             max_seq_len: int = 512,
         ) -> DataLoader:
             """Loads and tokenizes the Dolly 15k dataset for causal LM fine-tuning."""
             dataset = load_dataset(
                 "databricks/databricks-dolly-15k", split=dataset_split
             )
             tokenized = dataset.map(
                 lambda x: tokenizer(
                     f"Instruction: {x['instruction']}\nResponse: {x['response']}",
                     truncation=True,
                     max_length=max_seq_len,
                     padding="max_length",
                 ),
                 remove_columns=dataset.column_names,
             )
             dataloader = DataLoader(
                 tokenized,
                 batch_size=batch_size,
                 shuffle=True,
                 drop_last=True,
                 collate_fn=DataCollatorForLanguageModeling(
                     tokenizer=tokenizer, mlm=False
                 ),
             )
             return ray.train.torch.prepare_data_loader(dataloader)
         
         
         def train_func(config: dict) -> None:
             """Per-worker distributed FSDP2 training loop executed on each logical TPU core."""
             ctx = ray.train.get_context()
             world_rank = ctx.get_world_rank()
             world_size = ctx.get_world_size()
             device = ray.train.torch.get_device()
         
             model_id = config["model_id"]
             dataset_split = config["dataset_split"]
             batch_size = config["batch_size_per_device"]
             num_epochs = config["num_epochs"]
             max_seq_len = 512
         
             tokenizer = AutoTokenizer.from_pretrained(model_id)
             dataloader = create_dataloader(
                 tokenizer=tokenizer,
                 batch_size=batch_size,
                 dataset_split=dataset_split,
                 max_seq_len=max_seq_len,
             )
         
             torch.manual_seed(42)
             model = AutoModelForCausalLM.from_pretrained(
                 model_id,
                 dtype=torch.bfloat16,
                 attn_implementation="eager",
                 vision_config=None,
                 audio_config=None,
             ).to(device)
             model.config.get_text_config().use_cache = False
         
             mesh = init_device_mesh("tpu", (world_size,))
             mp_policy = MixedPrecisionPolicy(
                 param_dtype=torch.bfloat16,
                 reduce_dtype=torch.float32,
             )
             text_model = model.model.language_model
             text_model.embed_tokens_per_layer.requires_grad_(False)
             for layer in text_model.layers:
                 fully_shard(layer.mlp, mesh=mesh, mp_policy=mp_policy)
             fully_shard(
                 model,
                 mesh=mesh,
                 mp_policy=mp_policy,
                 ignored_params=set(text_model.embed_tokens_per_layer.parameters()),
             )
         
             optimizer = torch.optim.AdamW(
                 model.parameters(), lr=2e-5, weight_decay=0.01
             )
             global_batch_size = batch_size * world_size
         
             for epoch in range(num_epochs):
                 dataloader.sampler.set_epoch(epoch)
                 model.train()
                 epoch_start = time.perf_counter()
                 running_loss = torch.zeros(1, device=device, dtype=torch.float32)
         
                 for batch in dataloader:
                     optimizer.zero_grad()
                     outputs = model(
                         input_ids=batch["input_ids"],
                         labels=batch["labels"],
                     )
                     outputs.loss.backward()
                     optimizer.step()
                     running_loss += outputs.loss.detach().float()
         
                 all_reduce(running_loss, op=ReduceOp.AVG)
                 avg_loss = running_loss.item() / len(dataloader)
                 epoch_time = time.perf_counter() - epoch_start
                 tokens_per_sec = (
                     len(dataloader) * global_batch_size * max_seq_len
                 ) / epoch_time
         
                 metrics = {
                     "epoch": epoch + 1,
                     "loss": round(avg_loss, 4),
                     "epoch_time_s": round(epoch_time, 2),
                     "tokens_per_s": round(tokens_per_sec, 1),
                 }
                 if world_rank == 0:
                     print(
                         f"Epoch {epoch + 1}/{num_epochs} | loss={metrics['loss']:.4f} | "
                         f"epoch_time={metrics['epoch_time_s']:.2f}s | "
                         f"tokens/s={metrics['tokens_per_s']:.1f}"
                     )
         
                 full_state_dict = get_model_state_dict(
                     model,
                     options=StateDictOptions(
                         full_state_dict=True,
                         cpu_offload=True,
                         ignore_frozen_params=True,
                     ),
                 )
                 if world_rank == 0:
                     with tempfile.TemporaryDirectory() as tmpdir:
                         torch.save(full_state_dict, os.path.join(tmpdir, "model.pt"))
                         ray.train.report(
                             metrics, checkpoint=Checkpoint.from_directory(tmpdir)
                         )
                 else:
                     ray.train.report(metrics)
         
         
         def parse_args() -> argparse.Namespace:
             parser = argparse.ArgumentParser(
                 description="Fine-tune a Hugging Face CausalLM on TPUs with Ray Train and TorchTPU FSDP2."
             )
             parser.add_argument(
                 "--model-id",
                 type=str,
                 default="google/gemma-4-E2B-it",
                 help="Hugging Face model ID to fine-tune.",
             )
             parser.add_argument(
                 "--topology",
                 type=str,
                 default="4x4",
                 help="TPU slice topology.",
             )
             parser.add_argument(
                 "--accelerator-type",
                 type=str,
                 default="TPU-V6E",
                 help="Ray TPU accelerator type (TPU-V6E, TPU-V7X, etc.).",
             )
             parser.add_argument(
                 "--num-workers",
                 type=int,
                 default=16,
                 help="Total TPU worker processes across the slice.",
             )
             parser.add_argument(
                 "--dataset-split",
                 type=str,
                 default="train[:1024]",
                 help="Hugging Face dataset split to load.",
             )
             parser.add_argument(
                 "--num-epochs",
                 type=int,
                 default=3,
                 help="Number of fine-tuning epochs.",
             )
             parser.add_argument(
                 "--batch-size-per-device",
                 type=int,
                 default=4,
                 help="Per-device training batch size.",
             )
             parser.add_argument(
                 "--storage-path",
                 type=str,
                 default=os.environ.get("STORAGE_PATH"),
                 required="STORAGE_PATH" not in os.environ,
                 help="Cloud Storage or shared file system path for checkpoints.",
             )
             return parser.parse_args()
         
         
         def main() -> None:
             args = parse_args()
             ray.init()
             run_name = f"torchtpu_gemma4_fsdp2_sft_{int(time.time())}"
         
             print(
                 f"Starting Ray Train FSDP2 SFT job: model={args.model_id}, "
                 f"topology={args.topology}, accelerator_type={args.accelerator_type}, "
                 f"num_workers={args.num_workers}"
             )
         
             trainer = TorchTrainer(
                 train_loop_per_worker=train_func,
                 train_loop_config={
                     "model_id": args.model_id,
                     "dataset_split": args.dataset_split,
                     "num_epochs": args.num_epochs,
                     "batch_size_per_device": args.batch_size_per_device,
                 },
                 torch_config=TorchConfig(backend="tpu_dist"),
                 scaling_config=ScalingConfig(
                     use_tpu=True,
                     num_workers=args.num_workers,
                     topology=args.topology,
                     accelerator_type=args.accelerator_type,
                     resources_per_worker={"TPU": 1},
                 ),
                 run_config=RunConfig(
                     name=run_name,
                     storage_path=args.storage_path,
                     checkpoint_config=CheckpointConfig(
                         num_to_keep=1,
                         checkpoint_score_attribute="loss",
                         checkpoint_score_order="min",
                     ),
                 ),
             )
         
             result = trainer.fit()
             print(f"Training completed! Final metrics: {result.metrics}")
             print(f"Saved checkpoint: {result.checkpoint}")
         
         
         if __name__ == "__main__":
             main()

The script configures the [`TorchTrainer`](https://docs.ray.io/en/latest/train/api/doc/ray.train.torch.TorchTrainer.html) class with the following components:

     * The [`ScalingConfig`](https://docs.ray.io/en/latest/train/api/doc/ray.train.ScalingConfig.html) class configures the distributed worker topology for the training job. Setting the `use_tpu=True`, `num_workers=16`, `topology`, and `accelerator_type` parameters reserves a 16-device TPU slice and schedules one worker per TPU core.
     * The [`TorchConfig`](https://docs.ray.io/en/latest/train/api/doc/ray.train.torch.TorchConfig.html) class configures the `torch.distributed` process group across the workers. Setting the `backend="tpu_dist"` parameter connects all 16 workers over the TPU ICI network before the `train_func` function runs.
     * The `create_dataloader` function downloads and tokenizes the instruction dataset, batches the token sequences with a PyTorch [`DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader) object, and calls the `ray.train.torch.prepare_data_loader` function so each worker receives a disjoint shard of each global batch on its assigned TPU device.
     * The `train_func` function loads the model in `bfloat16` precision and calls the PyTorch FSDP2 `fully_shard` function on each feed-forward block and the root model to shard parameters, gradients, and optimizer states across all 16 TPU cores.
     * The [`Checkpoint`](https://docs.ray.io/en/latest/train/api/doc/ray.train.Checkpoint.html) class and [`ray.train.report`](https://docs.ray.io/en/latest/train/api/doc/ray.train.report.html) function gather the full model state dictionary on rank 0 at the end of each epoch and upload the checkpoint to your Cloud Storage bucket.
  2. Submit the `TorchTrainer` FSDP2 fine-tuning job for your TPU version:

### Trillium (v6e)
         
         ray job submit \
             --address http://localhost:8265 \
             --working-dir . \
             --runtime-env-json '{"excludes": ["ray-env", ".git", "*.whl"]}' \
             -- python3 ray_train_llm_finetune.py \
                 --topology=4x4 \
                 --accelerator-type=TPU-V6E \
                 --storage-path=gs://${BUCKET_NAME}/ray_train_torchtpu
         

### Ironwood (TPU7x)
         
         ray job submit \
             --address http://localhost:8265 \
             --working-dir . \
             --runtime-env-json '{"excludes": ["ray-env", ".git", "*.whl"]}' \
             -- python3 ray_train_llm_finetune.py \
                 --topology=2x2x2 \
                 --accelerator-type=TPU-V7X \
                 --storage-path=gs://${BUCKET_NAME}/ray_train_torchtpu
         

**Tip:** By default, the script trains on a 1,024-example subset for three epochs so the job finishes in a few minutes. To train on all 15,011 examples or change the number of epochs, pass the `--dataset-split=train` or `--num-epochs` flag to the `ray_train_llm_finetune.py` script.

The output is similar to the following:

### Trillium (v6e)
         
         Starting Ray Train FSDP2 SFT job: model=google/gemma-4-E2B-it, topology=4x4, accelerator_type=TPU-V6E, num_workers=16
         (TrainController pid=5407) Attempting to start training worker group of size 16 with the following resources: [{'TPU': 1, 'accelerator_type:TPU-V6E': 0.001}] * 16
         (RayTrainWorker pid=19733, ip=10.72.3.20) Setting up process group for: env:// [rank=0, world_size=16]
         (RayTrainWorker pid=19733, ip=10.72.3.20) Epoch 1/3 | loss=3.1402 | epoch_time=28.17s | tokens/s=18613.5
         (RayTrainWorker pid=19733, ip=10.72.3.20) Checkpoint successfully created at: Checkpoint(filesystem=gcs, path=my-project-ray-torchtpu/ray_train_torchtpu/torchtpu_gemma4_fsdp2_sft_1791864427/checkpoint_2026-10-13_04-08-10.762175)
         (RayTrainWorker pid=19733, ip=10.72.3.20) Epoch 2/3 | loss=2.3318 | epoch_time=26.07s | tokens/s=20112.8
         (RayTrainWorker pid=19733, ip=10.72.3.20) Checkpoint successfully created at: Checkpoint(filesystem=gcs, path=my-project-ray-torchtpu/ray_train_torchtpu/torchtpu_gemma4_fsdp2_sft_1791864427/checkpoint_2026-10-13_04-10-02.548088)
         (RayTrainWorker pid=19733, ip=10.72.3.20) Epoch 3/3 | loss=2.2050 | epoch_time=25.52s | tokens/s=20545.2
         (RayTrainWorker pid=19733, ip=10.72.3.20) Checkpoint successfully created at: Checkpoint(filesystem=gcs, path=my-project-ray-torchtpu/ray_train_torchtpu/torchtpu_gemma4_fsdp2_sft_1791864427/checkpoint_2026-10-13_04-11-48.701853)
         Training completed! Final metrics: {'epoch': 3, 'loss': 2.205, 'epoch_time_s': 25.52, 'tokens_per_s': 20545.2}
         Saved checkpoint: Checkpoint(filesystem=gcs, path=my-project-ray-torchtpu/ray_train_torchtpu/torchtpu_gemma4_fsdp2_sft_1791864427/checkpoint_2026-10-13_04-11-48.701853)
         ------------------------------------------
         Job 'raysubmit_zbm4pnFZitA1YECA' succeeded
         ------------------------------------------
         

### Ironwood (TPU7x)
         
         Starting Ray Train FSDP2 SFT job: model=google/gemma-4-E2B-it, topology=2x2x2, accelerator_type=TPU-V7X, num_workers=16
         (TrainController pid=1162) Attempting to start training worker group of size 16 with the following resources: [{'TPU': 1, 'accelerator_type:TPU-V7X': 0.001}] * 16
         (RayTrainWorker pid=257, ip=172.16.26.6) Setting up process group for: env:// [rank=0, world_size=16]
         (RayTrainWorker pid=257, ip=172.16.26.6) Epoch 1/3 | loss=3.1407 | epoch_time=26.28s | tokens/s=19953.3
         (RayTrainWorker pid=257, ip=172.16.26.6) Checkpoint successfully created at: Checkpoint(filesystem=gcs, path=my-project-ray-torchtpu/ray_train_torchtpu/torchtpu_gemma4_fsdp2_sft_1791867004/checkpoint_2026-10-13_04-52-00.026930)
         (RayTrainWorker pid=257, ip=172.16.26.6) Epoch 2/3 | loss=2.3235 | epoch_time=16.68s | tokens/s=31429.9
         (RayTrainWorker pid=257, ip=172.16.26.6) Checkpoint successfully created at: Checkpoint(filesystem=gcs, path=my-project-ray-torchtpu/ray_train_torchtpu/torchtpu_gemma4_fsdp2_sft_1791867004/checkpoint_2026-10-13_04-53-33.533341)
         (RayTrainWorker pid=257, ip=172.16.26.6) Epoch 3/3 | loss=2.1964 | epoch_time=16.98s | tokens/s=30884.6
         (RayTrainWorker pid=257, ip=172.16.26.6) Checkpoint successfully created at: Checkpoint(filesystem=gcs, path=my-project-ray-torchtpu/ray_train_torchtpu/torchtpu_gemma4_fsdp2_sft_1791867004/checkpoint_2026-10-13_04-55-01.508219)
         Training completed! Final metrics: {'epoch': 3, 'loss': 2.1964, 'epoch_time_s': 16.98, 'tokens_per_s': 30884.6}
         Saved checkpoint: Checkpoint(filesystem=gcs, path=my-project-ray-torchtpu/ray_train_torchtpu/torchtpu_gemma4_fsdp2_sft_1791867004/checkpoint_2026-10-13_04-55-01.508219)
         ------------------------------------------
         Job 'raysubmit_zSNnCXhHkwKiSmJh' succeeded
         ------------------------------------------
         

The training output shows the following:

     * Epoch 1 includes initial XLA graph compilation. Epochs 2 and 3 reuse the cached executables from `/dev/shm/torch_tpu_cache`, reaching over 20,000 tokens per second on TPU Trillium (v6e) and 31,000 tokens per second on Ironwood (TPU7x).
     * The global cross-entropy loss synchronized across all 16 FSDP2 worker ranks decreases from 3.14 in Epoch 1 to 2.20 in Epoch 3 across the three fine-tuning epochs on the `databricks/databricks-dolly-15k` instruction dataset.
     * At the end of each epoch, rank 0 gathers the full model state dictionary and uploads the checkpoint to your Cloud Storage bucket, retaining the lowest-loss checkpoint as configured in the `CheckpointConfig(num_to_keep=1, checkpoint_score_attribute="loss", checkpoint_score_order="min")` object.

**Success:** You have run distributed tensor-parallel computation with Ray Core and fine-tuned a Gemma 4 model with PyTorch FSDP2 on TPUs in GKE by using Ray Train and TorchTPU.

## Observe workload performance

To monitor TPU TensorCore utilization, HBM usage, and Ray cluster metrics in Cloud Monitoring, see [Collect and view logs and metrics for Ray clusters on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/collect-view-logs-metrics) and [View TPU metrics on the Ray Dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/view-tpu-metrics).

### Access the Ray Dashboard

To inspect the status of your Ray actors, placement groups, and training jobs in the built-in Ray Dashboard, follow these steps:

  1. If port forwarding to the Ray head service is not already running, start it in the background:
         
         kubectl port-forward svc/ray-torchtpu-cluster-head-svc 8265:8265 >/dev/null 2>&1 &
         

  2. In Cloud Shell, click ![Web Preview icon.](https://docs.cloud.google.com/static/shell/docs/images/web_preview.svg)**Web Preview** and select **Preview on port 8265** , or open `http://localhost:8265` in your local browser.

  3. Click the **Jobs** , **Cluster** , and **Metrics** tabs to inspect worker logs, placement group state, TPU node labels, and the **TPU Utilization by Node** graph.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete the RayCluster custom resource, the GKE cluster, the Cloud Storage bucket, and the Artifact Registry repository:

  1. Stop the background port-forwarding process and delete the RayCluster custom resource and Kubernetes Secret:
         
         pkill -f "kubectl port-forward" || true
         kubectl delete raycluster ray-torchtpu-cluster
         kubectl delete secret hf-secret --ignore-not-found
         

  2. Delete the GKE cluster:

### Autopilot
         
         gcloud container clusters delete ${CLUSTER_NAME} \
             --region=${REGION}
         

### Standard
         
         gcloud container clusters delete ${CLUSTER_NAME} \
             --zone=${ZONE}
         

  3. Delete the Cloud Storage bucket and its checkpoint contents:
         
         gcloud storage rm --recursive gs://${BUCKET_NAME}
         

  4. Delete the Artifact Registry repository:
         
         gcloud artifacts repositories delete ${ARTIFACT_REGISTRY} \
             --location=${REGION}
         




## What's next

  * Learn more about [PyTorch on Cloud TPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu).
  * Explore the [TorchTPU documentation](https://torchtpu.readthedocs.io/).
  * Learn how to [serve LLMs on multi-host TPUs with Ray and TorchTPU](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-ray-torchtpu).
  * Learn how to [optimize AI training on TPUs with DWS and Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/ray-kueue-dws).
  * Read [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Explore the [Ray Train documentation](https://docs.ray.io/en/latest/train/train.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
