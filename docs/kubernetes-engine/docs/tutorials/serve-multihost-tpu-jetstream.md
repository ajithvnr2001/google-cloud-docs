---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multihost-tpu-jetstream/
title: Serve LLMs using multi-host TPUs on GKE with JetStream and Pathways \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:57:40.973826+00:00
---

# Serve LLMs using multi-host TPUs on GKE with JetStream and Pathways  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multihost-tpu-jetstream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Serve LLMs using multi-host TPUs on GKE with JetStream and Pathways Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This guide shows you how to serve state-of-the-art large language models (LLMs) such as [Llama 3.1 405B](https://github.com/meta-llama/llama) on Google Kubernetes Engine (GKE) using tensor processing units (TPUs) across multiple nodes.

This guide demonstrates how to use portable open-source technologies—Kubernetes, [JetStream](https://github.com/AI-Hypercomputer/JetStream), [Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro), and the [LeaderWorkerSet](https://github.com/kubernetes-sigs/lws) (LWS) API—to deploy and serve AI/ML workloads on GKE, by taking advantage of GKE's granular control, scalability, resilience, portability, and cost-effectiveness.

## Background

Large language models have grown in size and they no longer fit on a single host TPU slice. For ML inference, you can use [Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro) to run large scale multi-host inference on GKE across multiple interconnected TPU nodes. In this guide, you will walk through how to provision a GKE cluster with the multi-host TPU slices and use the Pathways on Cloud binaries, launch the [JetStream](https://github.com/AI-Hypercomputer/JetStream) Server with [MaxText](https://github.com/AI-Hypercomputer/maxtext/tree/main/MaxText) framework, and make multi-host inference requests.

By serving an LLM using TPUs on GKE with [JetStream](https://github.com/AI-Hypercomputer/JetStream), [MaxText](https://github.com/AI-Hypercomputer/maxtext/tree/main/MaxText), and [Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro), you can build a robust, production-ready serving solution with all the benefits of managed [Kubernetes](https://kubernetes.io/), including cost-efficiency, scalability, and higher availability. This section describes the key technologies used in this tutorial.

### About TPUs

TPUs are Google's custom-developed application-specific integrated circuits (ASICs) used to accelerate machine learning and AI models that are built using frameworks such as [TensorFlow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/), and [JAX](https://github.com/google/jax).

Before you use TPUs in GKE, we recommend that you complete the following learning path:

  1. Learn about current TPU version availability with the [Cloud TPU system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  2. Learn [about TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).



This tutorial covers serving the Llama 3.1-405B model. GKE deploys the model on multi-host TPU v6e nodes with TPU topologies that are configured based on the model requirements for serving prompts with low latency.

### Pathways on Cloud

[Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro) is a large-scale orchestration layer for accelerators. Pathways is explicitly designed to enable exploration of new systems and ML research ideas, while retaining state of the art performance for current models. Pathways enables a single JAX client process to coordinate computation across one or more large TPU slices, streamlining ML computations that span hundreds or thousands of TPU chips.

### JetStream

[JetStream](https://github.com/google/JetStream) is an open source inference serving framework developed by Google. JetStream enables high-performance, high-throughput, and memory-optimized inference on TPUs and GPUs. JetStream provides advanced performance optimizations, including continuous batching, KV cache optimizations, and quantization techniques, to facilitate LLM deployment. JetStream enables PyTorch/XLA and JAX TPU serving to optimize performance.

### MaxText

[MaxText](https://github.com/google/maxtext) is a performant, scalable, and adaptable JAX LLM implementation, built on open source JAX libraries such as [Flax](https://github.com/google/flax), [Orbax](https://github.com/google/orbax), and [Optax](https://github.com/google-deepmind/optax). MaxText's decoder-only LLM implementation is written in Python. It leverages the XLA compiler heavily to achieve high performance without needing to build custom kernels.

For more information about the latest models and parameter sizes that MaxText supports, see the [MaxText project repository](https://github.com/google/maxtext).

### Llama 3.1 405B

Llama 3.1 405B is a large language model by Meta that's designed for a range of natural language processing tasks, including text generation, translation, and question answering. GKE offers the infrastructure required to support the distributed training and serving needs of models of this scale.

For more information, see the [Llama documentation](https://www.llama.com/).

## Architecture

This section describes the GKE architecture used in this tutorial. The architecture includes a GKE Standard cluster that provisions TPUs and hosts JetStream and Pathways components to deploy and serve the model.

The following diagram shows you the components of this architecture:

![Architecture of GKE cluster with multi-host TPU node pool containing the JetStream and Pathways components.](https://docs.cloud.google.com/static/kubernetes-engine/images/llm-tpu-jetstream-pathways.svg)

This architecture includes the following components:

  * A GKE Standard regional cluster.
  * A [multi-host TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host) that host the JetStream deployment and Pathways components.
  * The `Pathways resource manager` manages accelerator resources and coordinates allocation of accelerators for user jobs.
  * The `Pathways client` coordinates with the `Pathways resource manager` to determine where the compiled programs are placed for execution.
  * The `Pathways worker` runs and performs computations on accelerator machines, and sends data back to your workload over the IFRT proxy server.
  * The `IFRT proxy client` implements the OSS [Interim Framework Runtime (IFRT)](https://github.com/openxla/xla/blob/main/xla/python/ifrt/README.md) API and acts as the communication bridge between your workload and Pathways components.
  * The `IFRT proxy server` receives requests from the `IFRT proxy client` and forwards them to the `Pathways client`, distributing the work.
  * The `JetStream-Pathways` container provides a JAX-based inference server that receives inference requests and delegates its execution processes to the `Pathways workers`
  * The Service component spreads inbound traffic to all `JetStream HTTP` replicas.
  * `JetStream HTTP` is an HTTP server which accepts requests as a wrapper to JetStream's required format and sends it to [JetStream's GRPC client](https://github.com/google/JetStream/blob/main/jetstream/core/proto/jetstream_pb2_grpc.py).



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

  * Make sure that you have the following role or roles on the project: roles/container.admin, roles/iam.serviceAccountAdmin, roles/resourcemanager.projectIamAdmin 

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


  * Ensure that you have sufficient quota for sixteen TPU v6e PodSlice Lite chips. In this tutorial, you use [on-demand instances](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-quota).



## Get access to the model

To get access to the Meta Llama 3.1-405B checkpoint for deployment to GKE, follow these steps:

  1. Sign the license consent agreement.
  2. Access the [Meta Llama downloads page](https://www.llama.com/llama-downloads/).
  3. Review and accept the model **Terms and Conditions** and to obtain the URL needed to download the model.
  4. To download the model checkpoint, find the model ID for the appropriate model. For a list of supported models and their IDs, see the [llama CLI documentation](https://github.com/meta-llama/llama-stack/blob/main/docs/source/references/llama_cli_reference/index.md#downloading-models). For example, use **Llama 3.1-405B-Instruct:bf16-mp16** for the Llama 3.1-405B model.



## Prepare the environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) and [ gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To set up your environment with Cloud Shell, follow these steps:

  1. In the Google Cloud console, launch a Cloud Shell session by clicking ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** in the [Google Cloud console](http://console.cloud.google.com). This launches a session in the bottom pane of Google Cloud console.

  2. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         gcloud config set billing/quota_project PROJECT_ID
         export PROJECT_ID=$(gcloud config get project)
         export CLUSTER_NAME=CLUSTER_NAME
         export BUCKET_NAME=BUCKET_NAME
         export CONTROL_PLANE_LOCATION=CONTROL_PLANE_LOCATION
         export NODE_LOCATION=NODE_LOCATION
         export CLUSTER_VERSION=CLUSTER_VERSION
         export MACHINE_TYPE=ct6e-standard-4t
         export TPU_TYPE=v6e
         export TOPOLOGY=4x4
         export WORKERS_PER_SLICE=4
         

Replace the following values:

     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `BUCKET_NAME`: the name of your Cloud Storage bucket. You don't need to specify the `gs://` prefix.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine region where your GKE cluster, Cloud Storage bucket, and TPU nodes are located. The region contains zones where TPU v6e machine types are available (for example, `us-east1`, `us-east5`, `europe-west4`, `asia-northeast1`, or `us-south1`).
     * `NODE_LOCATION`: the zone where the [TPU resources are available](https://docs.cloud.google.com/tpu/docs/regions-zones) (for example, `us-east1-d`).
     * `CLUSTER_VERSION`: the GKE version, which must support the machine type that you want to use. Note that the default GKE version might not have availability for your target TPU. For a list of minimum GKE versions available by TPU machine type, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#standard_1).
     * `MACHINE_TYPE`: the v6e machine type.
     * `TPU_TYPE`: a prefix used for naming node pools (v6e).
     * `TOPOLOGY`: the TPU v6e topology.
     * `WORKERS_PER_SLICE`: the number of nodes per node pool or TPU slice.



## Create and configure Google Cloud resources

To create the required resources, follow these instructions:

**Note:** You might need to create a capacity reservation to use some accelerators. For more information about how to reserve and consume reserved resources, see [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).

### Create a GKE cluster

  1. Create a regional GKE Standard cluster:
         
         gcloud container clusters create ${CLUSTER_NAME} \
             --project=${PROJECT_ID} \
             --cluster-version=${CLUSTER_VERSION} \
             --location=${CONTROL_PLANE_LOCATION} \
             --scopes=cloud-platform \
             --machine-type=n2-standard-32
         

The cluster creation might take several minutes.

Replace `CLUSTER_VERSION` with the appropriate [cluster version](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions).

  2. Create one TPU v6e [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) with a `4x4` topology and four nodes each:
         
         gcloud container node-pools create multihost-np \
             --project=${PROJECT_ID} \
             --location=${CONTROL_PLANE_LOCATION} \
             --node-locations=${NODE_LOCATION} \
             --cluster=${CLUSTER_NAME} \
             --machine-type=${MACHINE_TYPE} \
             --num-nodes=${WORKERS_PER_SLICE} \
             --tpu-topology=${TOPOLOGY} \
             --scopes cloud-platform \
             --placement-type=COMPACT \
             --workload-metadata=GCE_METADATA
         

**Note:** The `--workload-metadata=GCE_METADATA` denotes that the node pool has Workload Identity Federation for GKE disabled. Node pools that run Pathways with JetStream and MaxText should disable Workload Identity Federation for GKE. 



### Configure a service account for Storage Object access

Configure a Kubernetes service account to act as an IAM service account.

  1. Create an IAM service account for your application:
         
         gcloud iam service-accounts create jetstream-pathways
         

  2. Add an IAM policy binding for your IAM service account to manage Cloud Storage. This is to enable your IAM service account to access the storage bucket where your checkpoint will be stored:
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID} \
           --member "serviceAccount:jetstream-pathways@${PROJECT_ID}.iam.gserviceaccount.com" \
           --role roles/storage.objectUser
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID} \
           --member "serviceAccount:jetstream-pathways@${PROJECT_ID}.iam.gserviceaccount.com" \
           --role roles/storage.insightsCollectorService
         

  3. Annotate the Kubernetes service account with the email address of the IAM service account. 
         
         kubectl annotate serviceaccount default \
         iam.gke.io/gcp-service-account=jetstream-pathways@${PROJECT_ID}.iam.gserviceaccount.com
         




### Configure Docker to authenticate to Artifact Registry

[Configure Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication#gcloud-helper) to authenticate to Artifact Registry so it can pull the allowlisted Pathways images:
    
    
    gcloud auth login
    gcloud auth configure-docker
    

### Checkpoint conversion

To convert a Meta Llama 3.1-405B checkpoint to a MaxText-compatible int8 inference checkpoint, complete the steps in [Checkpoint conversion with Llama3.1-405B](https://github.com/ai-on-gke/tutorials-and-examples/tree/main/inference-servers/checkpoints/examples/llama3.1-405b). Your deployment uses the checkpoint with the `load_parameters_path` flag.

### Create a Cloud Storage bucket to store Pathways temporary files

Create a Cloud Storage bucket to store your Pathways temporary files, like the compilation cache:
    
    
    export PATHWAYS_BUCKET=PATHWAYS_BUCKET
    gcloud storage buckets create gs://$PATHWAYS_BUCKET
    

## Deploy JetStream-MaxText and Pathways

Deploy the JetStream-MaxText and Pathways model server.

### Connect to the GKE cluster
    
    
    gcloud container clusters get-credentials "${CLUSTER_NAME}" --project "${PROJECT_ID}"  \
        --location "${CONTROL_PLANE_LOCATION}"
    

### Deploy the LeaderWorkerSet (LWS) API

LWS is a custom resource designed for deploying and managing stateful, distributed applications, particularly those with a leader-worker architecture. It's especially well-suited for AI/ML workloads where a large model is sharded and served across multiple devices on multiple nodes.
    
    
    VERSION=v0.6.1
    kubectl apply --server-side -f https://github.com/kubernetes-sigs/lws/releases/download/$VERSION/manifests.yaml
    

Wait for the LeaderWorkerSet controller to be fully available:
    
    
    kubectl wait deploy/lws-controller-manager -n lws-system --for=condition=available --timeout=5m
    

The output should be similar to the following:
    
    
    deployment.apps/lws-controller-manager condition met
    

Validate that the LeaderWorkerSet controller is running in the `lws-system` namespace:
    
    
    kubectl get pod -n lws-system
    

The output should be similar to the following:
    
    
    NAME                          READY   STATUS    RESTARTS    AGE
    lws-controller-manager-abcd   1/1     Running   0           40s
    lws-controller-manager-efgh   1/1     Running   0           40s
    

### Deploy the workload manifest

  1. Save the following manifest as `jetstream-pathways-llama-3-1-405b-4x4.yaml`:
         
         apiVersion: leaderworkerset.x-k8s.io/v1
         kind: LeaderWorkerSet
         metadata:
           name: jetstream-pathways
           annotations:
             leaderworkerset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           replicas: 1
           leaderWorkerTemplate:
             leaderTemplate:
               metadata:
                 labels:
                   app: jetstream-pathways
               spec:
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                   cloud.google.com/gke-tpu-topology: 4x4
                 tolerations:
                 - key: "google.com/tpu"
                   operator: "Exists"
                   effect: "NoSchedule"
                 containers:
                 - name: pathways-proxy
                   image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/proxy_server:jax-0.5.3
                   args:
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 38681
                 - name: pathways-rm
                   env:
                   - name: HOST_ADDRESS
                     value: "$(LWS_LEADER_ADDRESS)"
                   - name: TPU_SKIP_MDS_QUERY
                     value: "true"
                   image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/server:jax-0.5.3
                   args:
                   - --server_port=38677
                   - --gcs_scratch_location=PATHWAYS_BUCKET
                   - --node_type=resource_manager
                   - --instance_count=1
                   - --instance_type=tpuv6e:4x4
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 38677
                 - name: jax-tpu
                   image: us-docker.pkg.dev/cloud-tpu-images/inference/jetstream-pathways:v0.2.0
                   env:
                   - name: LOG_LEVEL
                     value: "INFO"
                   args:
                   - MaxText/configs/v5e/inference/llama3_405b_v5e-64.yml
                   - model_name=llama3.1-405b
                   - load_parameters_path=CHECKPOINT_PATH
                   - max_prefill_predict_length=1024
                   - max_target_length=2048
                   - async_checkpointing=false
                   - steps=1
                   - ici_fsdp_parallelism=1
                   - ici_autoregressive_parallelism=2
                   - ici_tensor_parallelism=8
                   - scan_layers=false
                   - weight_dtype=bfloat16
                   - per_device_batch_size=6
                   - enable_single_controller=true
                   - quantization=int8
                   - quantize_kvcache=true
                   - checkpoint_is_quantized=true
                   - enable_model_warmup=true
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 9000
                   startupProbe:
                     httpGet:
                       path: /healthcheck
                       port: 8000
                       scheme: HTTP
                     periodSeconds: 1
                     initialDelaySeconds: 600
                     failureThreshold: 10000
                   livenessProbe:
                     httpGet:
                       path: /healthcheck
                       port: 8000
                       scheme: HTTP
                     periodSeconds: 60
                     failureThreshold: 10
                   readinessProbe:
                     httpGet:
                       path: /healthcheck
                       port: 8000
                       scheme: HTTP
                     periodSeconds: 60
                     failureThreshold: 10
                 - name: jetstream-http
                   image: us-docker.pkg.dev/cloud-tpu-images/inference/jetstream-http:v0.2.3
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 8000
             size: 5
             workerTemplate:
               spec:
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                   cloud.google.com/gke-tpu-topology: 4x4
                 tolerations:
                 - key: "google.com/tpu"
                   operator: "Exists"
                   effect: "NoSchedule"
                 containers:
                 - name: worker
                   args:
                   - --server_port=38679
                   - --resource_manager_address=$(LWS_LEADER_ADDRESS):38677
                   - --gcs_scratch_location=PATHWAYS_BUCKET
                   image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/server:jax-0.5.3
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 38679
                   resources:
                     limits:
                       google.com/tpu: "4"
         --- 
         apiVersion: v1
         kind: Service
         metadata:
           name: jetstream-svc
         spec:
           selector:
             app: jetstream-pathways
           ports:
           - protocol: TCP
             name: jetstream-http
             port: 8000
             targetPort: 8000

  2. Set the value of the `load_parameters_path` field to your checkpoint path that was produced in the checkpoint conversion process.

     * For a bf16 checkpoint, the path should be similar to `gs://OUTPUT_BUCKET_DIRECTORY/bf16/unscanned/checkpoints/0/items`.
     * For an int8 checkpoint, it should be similar to `gs://OUTPUT_BUCKET_DIRECTORY/int8`.

Set the value of the `gcs_scratch_location` field to the Pathways bucket that you created earlier.
    
    perl -pi -e "s|CHECKPOINT_PATH|gs://${BUCKET_NAME}/int8|g" jetstream-pathways-llama-3-1-405b-4x4.yaml
    perl -pi -e "s|PATHWAYS_BUCKET|gs://${PATHWAYS_BUCKET}|g" jetstream-pathways-llama-3-1-405b-4x4.yaml
    

Description for variables and settings.

The following descriptions explain the relevant variables and settings for JetStream, Pathways, and LeaderWorkerSet.

     * Jetstream 
       * This container is built from the [OSS JetStream project](https://github.com/AI-Hypercomputer/JetStream/tree/main). It also encapsulates the gRPC based client library of the IFRT Proxy, which provides a JAX backend that can delegate running TPU programs to the Pathways Proxy server.
       * For more information about JetStream-MaxText flags, see the [JetStream-MaxText Server flag descriptions](https://github.com/AI-Hypercomputer/JetStream/blob/main/docs/online-inference-with-maxtext-engine.md#jetstream-maxtext-server-flag-descriptions).
       * To use a quantized checkpoint, you can set the `quantization`, `quantize_kvcache`, or `checkpoint_is_quantized` flags. If the checkpoint is bf16, you can omit these flags.
     * Pathways: for a description of the relevant Pathways components, see [Pathways components](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro#pathways-components).
     * LeaderWorkerSet: for more information about LeaderWorkerSet settings, see [the API definition](https://github.com/kubernetes-sigs/lws/blob/main/api/leaderworkerset/v1/leaderworkerset_types.go).



### Apply the Deployment manifest

Apply the manifest to deploy the server:
    
    
    kubectl apply -f jetstream-pathways-llama-3-1-405b-4x4.yaml
    

The model server should start.

### Verify model server start

A 405B model might take about 10 to 20 minutes to restore the checkpoint. You might also wait for additional time during model warmup if you enabled the `enable_model_warmup` flag.
    
    
    kubectl logs -f jetstream-pathways-0 -c jax-tpu
    

The output is similar to the following:
    
    
    2025-03-02 02:15:07,682 - JetstreamLogger - INFO - Initializing the driver with 1 prefill engines and 1 generate engines in interleaved mode
    2025-03-02 02:15:07,683 - JetstreamLogger - INFO - Spinning up prefill thread 0.
    2025-03-02 02:15:07,683 - JetstreamLogger - INFO - Spinning up transfer thread 0.
    2025-03-02 02:15:07,684 - JetstreamLogger - INFO - Spinning up generate thread 0.
    2025-03-02 02:15:07,684 - JetstreamLogger - INFO - Spinning up detokenize thread 0.
    2025-03-02 02:15:07,685 - JetstreamLogger - INFO - Driver initialized.
    ...
    ...
    ...
    INFO:     Started server process [7]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://0.0.0.0:9999 (Press CTRL+C to quit)
    

## Serve Llama 3.1-405b

To serve the Llama 3.1-405b model, set up port forwarding:
    
    
    kubectl port-forward svc/jetstream-svc 8000:8000
    

Port forwarding lets you access the Service from outside the cluster. You can access the JetStream-Pathways Deployment through the ClusterIP Service of GKE. The ClusterIP Services are reachable only from within the cluster.

### Interact with the model

In a new terminal, run the following command:
    
    
    curl --request POST \
    --header "Content-type: application/json" \
    -s \
    localhost:8000/generate \
    --data \
    '{
        "prompt": "What are the top 5 programming languages",
        "max_tokens": 200
    }'
    

The initial request can take several seconds to complete due to model warmup. The output should be similar to the following:
    
    
    {
        "response": " for web development?\nThe top 5 programming languages for web development are:\n1. **JavaScript**: JavaScript is the most popular language for web development, used by over 90% of websites for client-side scripting. It's also popular for server-side programming with technologies like Node.js.\n2. **HTML/CSS**: HTML (Hypertext Markup Language) and CSS (Cascading Style Sheets) are not programming languages, but are essential for building websites. HTML is used for structuring content, while CSS is used for styling and layout.\n3. **Python**: Python is a popular language for web development, especially with frameworks like Django and Flask. It's known for its simplicity, flexibility, and large community of developers.\n4. **Java**: Java is a popular language for building enterprise-level web applications, especially with frameworks like Spring and Hibernate. It's known for its platform independence, strong security features, and large community of developers.\n5. **PHP**: PHP is a mature language for web"
    }
    

You've successfully done the following:

  1. Deployed the JetStream model server with MaxText and Pathways on GKE by using TPUs.
  2. Created a Llama 3.1-405B int8 checkpoint at `gs://BUCKET_NAME`.
  3. Served and interacted with the model.



## Disaggregated serving

Disaggregated serving is a technique for serving LLMs while splitting the prefill and decode stages into different hosts. This approach optimizes resource utilization, which can lead to improved throughput and latency. 

  * **Prefill** : a forward pass on the input prompt to initialize the key-value cache.

  * **Decode** : a procedure that generates output tokens incrementally, one token per step, and one KV-cache value per iteration.



  1. Set the default environment variables:
         
         export NODE_POOL_NAME=dis-v6e-8
         export NODE_POOL_SIZE=2
         export MACHINE_TYPE=ct6e-standard-4t
         export TOPOLOGY=2x4
         export WORKERS_PER_SLICE=2
         

  2. Create two node pools that use `v6e-8` nodes:
         
         for i in $(seq 1 ${NODE_POOL_SIZE}); do
           gcloud container node-pools create ${NODE_POOL_NAME}-${i}-np \
           --project=${PROJECT_ID} \
           --cluster=${CLUSTER_NAME} \
           --location=${CONTROL_PLANE_LOCATION} \
           --node-locations=${NODE_LOCATION} \
           --machine-type=${MACHINE_TYPE} \
           --num-nodes=${WORKERS_PER_SLICE} \
           --tpu-topology=${TOPOLOGY} \
           --scopes=cloud-platform \
           --workload-metadata=GCE_METADATA
         done
         




### Checkpoint conversion

To convert a Meta Llama 2-70B checkpoint to a MaxText-compatible int8 inference checkpoint, complete the steps in [Checkpoint conversion with Llama2-70B](https://github.com/ai-on-gke/tutorials-and-examples/tree/main/inference-servers/checkpoints/examples/llama3.1-405b). Select Llama2-70B as your model when you acknowledge the Meta Terms and Conditions. Your deployment uses the checkpoint with the `load_parameters_path` flag.

Replace the following parameters in your `checkpoint-job.yaml` file:
    
    
    - --meta_url=META_URL
    - --model_name=llama-2
    - --model_path=Llama-2-70b-chat
    - --output_directory=gs://BUCKET_NAME/maxtext/llama-2-70b
    

The checkpoint will be used in your deployment with the `load_parameters_path` flag.

### Deploy JetStream Pathways with disaggregated serving

  1. Save the following manifest as `jetstream-pathways-disagg-llama-2-70b-2-2x4.yaml`:
         
         apiVersion: leaderworkerset.x-k8s.io/v1
         kind: LeaderWorkerSet
         metadata:
           name: jetstream-pathways
           annotations:
             leaderworkerset.sigs.k8s.io/subgroup-exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           replicas: 1
           leaderWorkerTemplate:
             subGroupPolicy:
               subGroupSize: 2
             leaderTemplate:
               metadata:
                 labels:
                   app: jetstream-pathways
               spec:
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                   cloud.google.com/gke-tpu-topology: 2x4
                 tolerations:
                 - key: "google.com/tpu"
                   operator: "Exists"
                   effect: "NoSchedule"
                 containers:
                 - name: pathways-proxy
                   image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/proxy_server:jax-0.5.3
                   args:
                   - --resource_manager_address=$(LWS_LEADER_ADDRESS):38677
                   - --server_port=38681
                   - --gcs_scratch_location=gs://cloud-pathways-staging/tmp
                   - --xla_jf_auto_cross_replica_sharding=false
                   - --xla_tpu_enable_windowed_einsum_for_reduce_scatter=false
                   - --xla_tpu_enable_windowed_einsum_for_all_gather=false
                   - --xla_tpu_prefer_latch_optimized_rhs_layouts=true
                   - --xla_tpu_enable_experimental_fusion_cost_model=false
                   - --xla_tpu_dot_dot_fusion_duplicated=false
                   - --xla_tpu_dot_dot_fusion=true
                   - --xla_jf_conv_input_fusion=true
                   - --xla_jf_conv_output_fusion=true
                   - --xla_tpu_rwb_fusion=false
                   - --xla_tpu_copy_fusion_pad_unpad_ratio=0
                   - --xla_tpu_licm_size_inflation_ratio=1
                   - --xla_tpu_copy_elision_analysis_allowance=150000
                   - --xla_tpu_copy_insertion_use_region_analysis_limit=10000
                   - --xla_tpu_order_dot_after_layout=true
                   - --xla_jf_rematerialization_percent_shared_memory_limit=100
                   - --xla_tpu_use_repeated_instance_for_preferred_prefetch_time=true
                   - --xla_tpu_enforce_prefetch_fifo_order=false
                   - --xla_tpu_prefetch_interval_picker_size_override=6000000
                   - --xla_tpu_async_copy_bandwidth_scaling_factor=1
                   - --xla_tpu_nd_short_transfer_max_chunks=-1
                   - --xla_tpu_enable_aggressive_broadcast_priority_update=true
                   - --xla_tpu_alternate_memory_benefit_scaling_factor_for_large_buffers=SQRT
                   - --xla_tpu_memory_bound_loop_optimizer_options=enabled:true
                   - --xla_tpu_enable_copy_fusion=true
                   - --xla_tpu_enable_cross_program_prefetch_freeing=false
                   - --xla_tpu_enable_dot_strength_reduction=true
                   - --xla_tpu_layout_use_dot_grouping=false
                   - --xla_tpu_msa_inefficient_use_to_copy_ratio=0.5
                   - --xla_tpu_reduce_loop_fusion_dup_with_unfusable_user=false
                   - --xla_tpu_vector_load_fusion_window=1024
                   - --xla_tpu_vector_store_fusion_window=256
                   - --xla_jf_conv_reshape_fusion=false
                   - --xla_tpu_input_conv_multi_users=false
                   - --xla_tpu_enable_multi_level_input_dot_dot_fusion=false
                   - --xla_tpu_enable_multi_level_output_dot_dot_fusion=false
                   - --xla_tpu_dot_dot_fusion_separable_convs_only=false
                   - --xla_tpu_enable_multi_level_nested_loop_fusion=true
                   - --xla_tpu_nested_dot_fusion=true
                   - --xla_tpu_enable_multi_level_nested_dot_fusion=false
                   - --xla_jf_enable_multi_output_fusion=true
                   - --xla_tpu_use_lp_llo_scheduler_for_dot_dot_fusions=false
                   - --xla_tpu_enable_flash_attention=true
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 38681
                 - name: pathways-rm
                   env:       
                   - name: HOST_ADDRESS
                     value: "$(LWS_LEADER_ADDRESS)"
                   - name: TPU_SKIP_MDS_QUERY
                     value: "true"
                   image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/server:jax-0.5.3
                   args:
                   - --server_port=38677
                   - --gcs_scratch_location=PATHWAYS_BUCKET
                   - --node_type=resource_manager
                   - --instance_count=2
                   - --instance_type=tpuv6e:2x4
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 38677
                 - name: jax-tpu
                   image: us-docker.pkg.dev/cloud-tpu-images/inference/jetstream-pathways:v0.2.0
                   args:
                   - MaxText/configs/base.yml
                   - tokenizer_path=assets/tokenizer.llama2
                   - load_parameters_path=CHECKPOINT_PATH
                   - max_prefill_predict_length=1024
                   - max_target_length=2048
                   - model_name=llama2-70b
                   - ici_fsdp_parallelism=1
                   - ici_autoregressive_parallelism=1
                   - ici_tensor_parallelism=-1
                   - scan_layers=false
                   - weight_dtype=bfloat16
                   - per_device_batch_size=27
                   - checkpoint_is_quantized=true 
                   - quantization=int8
                   - quantize_kvcache=true
                   - compute_axis_order=0,2,1,3
                   - ar_cache_axis_order=0,2,1,3
                   - stack_prefill_result_cache=True
                   - inference_server=ExperimentalMaxtextDisaggregatedServer_8
                   - inference_benchmark_test=True
                   - enable_model_warmup=True
                   env:
                   - name: LOG_LEVEL
                     value: "INFO"
                   imagePullPolicy: Always
                   securityContext:
                     capabilities:
                       add: ["SYS_PTRACE", "NET_ADMIN", "SYS_TIME"]
                   ports: 
                   - containerPort: 9000
                   startupProbe:
                     httpGet:
                       path: /healthcheck
                       port: 8000
                       scheme: HTTP
                     periodSeconds: 1
                     initialDelaySeconds: 240
                     failureThreshold: 10000
                   livenessProbe:
                     httpGet:
                       path: /healthcheck
                       port: 8000
                       scheme: HTTP
                     periodSeconds: 60
                     failureThreshold: 100
                   readinessProbe:
                     httpGet:
                       path: /healthcheck
                       port: 8000
                       scheme: HTTP
                     periodSeconds: 60
                     failureThreshold: 100
                 - name: jetstream-http
                   image: us-docker.pkg.dev/cloud-tpu-images/inference/jetstream-http:v0.2.3
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 8000
             size: 5
             workerTemplate:
               spec:
                 nodeSelector:
                   cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                   cloud.google.com/gke-tpu-topology: 2x4
                 containers:
                 - name: worker
                   args:
                   - --server_port=38679
                   - --resource_manager_address=$(LWS_LEADER_ADDRESS):38677
                   - --gcs_scratch_location=PATHWAYS_BUCKET
                   image: us-docker.pkg.dev/cloud-tpu-v2-images/pathways/server:jax-0.5.3
                   imagePullPolicy: Always
                   ports:
                   - containerPort: 38679
                   resources:
                     limits:
                       google.com/tpu: "4"
         --- 
         apiVersion: v1
         kind: Service
         metadata:
           name: jetstream-svc
         spec:
           selector:
             app: jetstream-pathways
           ports:
           - protocol: TCP
             name: jetstream-http
             port: 8000
             targetPort: 8000

  2. Set the value of the `load_parameters_path` field to your checkpoint path that was produced in the checkpoint conversion process.

     * For a bf16 checkpoint, the path should be similar to `gs://OUTPUT_BUCKET_DIRECTORY/bf16/unscanned/checkpoints/0/items`.
     * For an int8 checkpoint, it should be similar to `gs://OUTPUT_BUCKET_DIRECTORY/int8`.

Set the value of the `gcs_scratch_location` field to the Pathways bucket that you created earlier.
    
    perl -pi -e "s|CHECKPOINT_PATH|gs://${BUCKET_NAME}/maxtext/llama-2-70b/int8|g" jetstream-pathways-disagg-llama-2-70b-2-2x4.yaml
    perl -pi -e "s|PATHWAYS_BUCKET|gs://${PATHWAYS_BUCKET}|g" jetstream-pathways-disagg-llama-2-70b-2-2x4.yaml
    

  3. Apply the manifest:
         
         kubectl apply -f jetstream-pathways-disagg-llama-2-70b-2-2x4.yaml
         

The model server might take some time to restore the checkpoint, depending on the checkpoint size. A 70B model might take about 8 minutes to restore the checkpoint, including model warmup. You can further observe the logs to determine point of readiness by verifying the model server start and serve the model by setting up port forwarding so you can interact with the model.




You've successfully done the following:

  1. Deployed the JetStream model server with MaxText and Pathways on GKE by using TPUs and disaggregated serving.
  2. Created a Llama 2-70B int8 checkpoint at `gs://BUCKET_NAME`.
  3. Served and interacted with the model.



## Troubleshoot issues

  * If you get the `Empty reply from server` message, it's possible the container hasn't finished downloading the model data. Check the Pod's logs again for the `Connected` message, which indicates that the model is ready to serve.
  * If you see the `Connection refused` message, verify that your port forwarding is active.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the deployed resources

To avoid incurring charges to your Google Cloud account for the resources that you created in this guide, run the following commands and follow the prompts:
    
    
    gcloud container clusters delete ${CLUSTER_NAME} --location=${CONTROL_PLANE_LOCATION}
    
    gcloud iam service-accounts delete jetstream-pathways@${PROJECT_ID}.iam.gserviceaccount.com
    
    gcloud storage rm --recursive gs://${BUCKET_NAME}
    

## What's next

  * Discover how you can run [Gemma models on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra#serve-open-models-using-GKE-gen-ai-capabilities) and how to run optimized AI/ML workloads with [GKE platform orchestration capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra).
  * Learn more about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Explore the JetStream [GitHub repository](https://github.com/google/JetStream).
  * Explore the [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
