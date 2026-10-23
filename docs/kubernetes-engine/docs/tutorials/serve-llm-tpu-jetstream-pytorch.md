---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-jetstream-pytorch/
title: Serve an LLM using TPUs on GKE with JetStream and PyTorch \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:27.099869+00:00
---

# Serve an LLM using TPUs on GKE with JetStream and PyTorch  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-jetstream-pytorch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Serve an LLM using TPUs on GKE with JetStream and PyTorch Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Note:** vLLM is now the recommended solution for serving LLMs on TPUs in GKE. To get started, see [Serve an LLM using TPU Trillium on GKE with vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu).

This guide shows you how to serve a large language model (LLM) using Tensor Processing Units (TPUs) on Google Kubernetes Engine (GKE) with [JetStream](https://github.com/google/JetStream) through [PyTorch](https://github.com/google/jetstream-pytorch). In this guide, you download model weights to Cloud Storage and deploy them on a GKE [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode#why-autopilot) or [Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode#why-standard) cluster using a container that runs JetStream.

If you need the scalability, resilience, and cost-effectiveness offered by Kubernetes features when deploying your model on JetStream, this guide is a good starting point.

This guide is intended for Generative AI customers who use PyTorch, new or existing users of GKE, ML Engineers, MLOps (DevOps) engineers, or platform administrators who are interested in using Kubernetes container orchestration capabilities for serving LLMs.

## Background

By serving an LLM using TPUs on GKE with JetStream, you can build a robust, production-ready serving solution with all the benefits of managed [Kubernetes](https://kubernetes.io/), including cost-efficiency, scalability and higher availability. This section describes the key technologies used in this tutorial.

### About TPUs

TPUs are Google's custom-developed application-specific integrated circuits (ASICs) used to accelerate machine learning and AI models built using frameworks such as [TensorFlow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/), and [JAX](https://github.com/google/jax).

Before you use TPUs in GKE, we recommend that you complete the following learning path:

  1. Learn about current TPU version availability with the [Cloud TPU system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  2. Learn [about TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).



This tutorial covers serving various LLM models. GKE deploys the model on single-host TPUv5e nodes with TPU topologies configured based on the model requirements for serving prompts with low latency.

### About JetStream

[JetStream](https://github.com/google/JetStream) is an open source inference serving framework developed by Google. JetStream enables high-performance, high-throughput, and memory-optimized inference on TPUs and GPUs. JetStream provides advanced performance optimizations, including continuous batching, KV cache optimizations, and quantization techniques, to facilitate LLM deployment. JetStream enables PyTorch/XLA and JAX TPU serving to achieve optimal performance.

**Continuous Batching**

Continuous batching is a technique that dynamically groups incoming inference requests into batches, reducing latency and increasing throughput.

**KV cache quantization**

KV cache quantization involves compressing the key-value cache used in attention mechanisms, reducing memory requirements.

**Int8 weight quantization**

Int8 weight quantization reduces the precision of model weights from 32-bit floating point to 8-bit integers, leading to faster computation and reduced memory usage.

To learn more about these optimizations, refer to the [JetStream PyTorch](https://github.com/google/jetstream-pytorch) and [JetStream MaxText](https://github.com/google/JetStream) project repositories.

### About PyTorch

PyTorch is an open source machine learning framework developed by Meta and now part of the Linux Foundation umbrella. PyTorch provides high-level features such as tensor computation and deep neural networks.

## Objectives

  1. Prepare a GKE Autopilot or Standard cluster with the recommended TPU topology based on the model characteristics.
  2. Deploy JetStream components on GKE.
  3. Get and publish your model.
  4. Serve and interact with the published model.



## Architecture

This section describes the GKE architecture used in this tutorial. The architecture includes a GKE Autopilot or Standard cluster that provisions TPUs and hosts JetStream components to deploy and serve the models.

The following diagram shows you the components of this architecture:

![Architecture of GKE cluster with single-host TPU node pools containing the JetStream-PyTorch and JetStream HTTP components.](https://docs.cloud.google.com/static/kubernetes-engine/images/llm-tpu-jetstream-pytorch.svg)

This architecture includes the following components:

  * A GKE Autopilot or Standard regional cluster.
  * Two single-host TPU slice node pools that host the JetStream deployment.
  * The Service component spreads inbound traffic to all `JetStream HTTP` replicas.
  * `JetStream HTTP` is an HTTP server which accepts requests as a wrapper to JetStream's required format and sends it to [JetStream's GRPC client](https://github.com/google/JetStream/blob/main/jetstream/core/proto/jetstream_pb2_grpc.py).
  * `JetStream-PyTorch` is a JetStream server that performs inferencing with continuous batching.



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


  * Check that you have sufficient quota for eight TPU v5e PodSlice Lite chips. In this tutorial, you use [on-demand instances](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-quota).
  * Create a [Hugging Face token](https://huggingface.co/docs/hub/security-tokens), if you don't already have one.



## Get access to the model

Get access to various models on Hugging Face for deployment to GKE

### Gemma 7B-it

To get access to the Gemma model for deployment to GKE, you must first sign the license consent agreement.

  1. Access the [Gemma model consent page](https://huggingface.co/google/gemma-7b-it-pytorch) on Hugging Face
  2. Login to Hugging Face if you haven't done so already.
  3. Review and accept the model **Terms and Conditions**.



### Llama 3 8B

To get access to the Llama 3 model for deployment to GKE, you must first sign the license consent agreement.

  1. Access the [Llama 3 model consent page](https://huggingface.co/meta-llama/Meta-Llama-3-8B) on Hugging Face
  2. Login to Hugging Face if you haven't done so already.
  3. Review and accept the model **Terms and Conditions**.



## Prepare the environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with the software you'll need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) and [ gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To set up your environment with Cloud Shell, follow these steps:

  1. In the Google Cloud console, launch a Cloud Shell session by clicking ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** in the [Google Cloud console](http://console.cloud.google.com). This launches a session in the bottom pane of Google Cloud console.

  2. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         gcloud config set billing/quota_project PROJECT_ID
         export PROJECT_ID=$(gcloud config get project)
         export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
         export CLUSTER_NAME=CLUSTER_NAME
         export CONTROL_PLANE_LOCATION=CONTROL_PLANE_LOCATION
         export NODE_LOCATION=NODE_LOCATION
         export CLUSTER_VERSION=CLUSTER_VERSION
         export BUCKET_NAME=BUCKET_NAME
         

Replace the following values:

     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. The region must contain zones where TPU v5e machine types are available (for example, `us-west1`, `us-west4`, `us-central1`, `us-east1`, `us-east5`, or `europe-west4`). For Autopilot clusters, ensure that you have sufficient [TPU v5e zonal resources](https://docs.cloud.google.com/tpu/docs/regions-zones) for your region of choice.
     * (Standard cluster only) `NODE_LOCATION`: the zone where the [TPU resources are available](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#availability) (for example, `us-west4-a`). For Autopilot clusters, you don't need to specify this value.
     * `CLUSTER_VERSION`: the GKE version, which must support the machine type that you want to use. Note that the default GKE version might not have availability for your target TPU. For a list of minimum GKE versions available by TPU machine type, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#availability).
     * `BUCKET_NAME`: the name of your Cloud Storage bucket with [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled, used to store the JAX compilation cache.



## Create and configure Google Cloud resources

Follow these instructions to create the required resources.

**Note:** You may need to create a capacity reservation for usage of some accelerators. To learn how to reserve and consume reserved resources, see [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).

### Create a GKE cluster

You can serve Gemma on TPUs in a GKE Autopilot or Standard cluster. We recommend that you use a Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot

Create an Autopilot GKE cluster:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --project=PROJECT_ID \
        --location=CONTROL_PLANE_LOCATION \
        --cluster-version=CLUSTER_VERSION
    

Replace `CLUSTER_VERSION` with the appropriate [cluster version](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions). For a Autopilot GKE cluster, use a regular release channel version.

### Standard

  1. Create a regional GKE Standard cluster that uses [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity):
         
         gcloud container clusters create CLUSTER_NAME \
             --enable-ip-alias \
             --machine-type=e2-standard-4 \
             --num-nodes=2 \
             --cluster-version=CLUSTER_VERSION \
             --workload-pool=PROJECT_ID.svc.id.goog \
             --location=CONTROL_PLANE_LOCATION
         

The cluster creation might take several minutes.

Replace `CLUSTER_VERSION` with the appropriate [cluster version](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions).

  2. Create a TPU v5e [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) with a `2x4` topology and two nodes:
         
         gcloud container node-pools create tpu-nodepool \
           --cluster=CLUSTER_NAME \
           --machine-type=ct5lp-hightpu-8t \
           --project=PROJECT_ID \
           --num-nodes=2 \
           --location=CONTROL_PLANE_LOCATION \
           --node-locations=NODE_LOCATION
         




### Generate your Hugging Face CLI token in Cloud Shell

Generate a new [Hugging Face token](https://huggingface.co/docs/hub/security-tokens) if you don't already have one:

  1. Click **Your Profile > Settings > Access Tokens**.
  2. Click **New Token**.
  3. Specify a Name of your choice and a Role of at least `Read`.
  4. Click **Generate a token**.
  5. Edit permissions to your access token to have read access to your model's Hugging Face repository.
  6. Copy the generated token to your clipboard.



### Create a Kubernetes Secret for Hugging Face credentials

In Cloud Shell, do the following:

  1. Configure `kubectl` to communicate with your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME --location=CONTROL_PLANE_LOCATION
         

  2. Create a Secret to store the Hugging Face credentials:
         
         kubectl create secret generic huggingface-secret \
             --from-literal=HUGGINGFACE_TOKEN=HUGGINGFACE_TOKEN
         

Replace `HUGGINGFACE_TOKEN` with your Hugging Face token.




### Configure your workloads access using Workload Identity Federation for GKE

Grant the `default` [Kubernetes ServiceAccount](https://kubernetes.io/docs/concepts/security/service-accounts/) in the `default` namespace the required IAM roles (`roles/storage.objectUser` and `roles/storage.insightsCollectorService`) to manage Cloud Storage:
    
    
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/default/sa/default" \
        --role="roles/storage.objectUser" \
        --condition=None
    
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/default/sa/default" \
        --role="roles/storage.insightsCollectorService" \
        --condition=None
    

## Deploy JetStream

Deploy the JetStream container to serve your model. This tutorial uses Kubernetes Deployment manifests. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster..

Save the following manifest as `jetstream-pytorch-deployment.yaml`:

### Gemma 7B-it
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: jetstream-pytorch-server
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: jetstream-pytorch-server
      template:
        metadata:
          labels:
            app: jetstream-pytorch-server
        spec:
          nodeSelector:
            cloud.google.com/gke-tpu-topology: 2x4
            cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
          containers:
          - name: jetstream-pytorch-server
            image: us-docker.pkg.dev/cloud-tpu-images/inference/jetstream-pytorch-server:v0.2.4
            args:
            - --model_id=google/gemma-7b-it
            - --override_batch_size=30
            - --enable_model_warmup=True
            volumeMounts:
            - name: huggingface-credentials
              mountPath: /huggingface
              readOnly: true
            ports:
            - containerPort: 9000
            resources:
              requests:
                google.com/tpu: 8
              limits:
                google.com/tpu: 8
            startupProbe:
              httpGet:
                path: /healthcheck
                port: 8000
                scheme: HTTP
              periodSeconds: 60
              initialDelaySeconds: 90
              failureThreshold: 50
            livenessProbe:
              httpGet:
                path: /healthcheck
                port: 8000
                scheme: HTTP
              periodSeconds: 60
              failureThreshold: 30
            readinessProbe:
              httpGet:
                path: /healthcheck
                port: 8000
                scheme: HTTP
              periodSeconds: 60
              failureThreshold: 30
          - name: jetstream-http
            image: us-docker.pkg.dev/cloud-tpu-images/inference/jetstream-http:v0.2.3
            ports:
            - containerPort: 8000
          volumes:
          - name: huggingface-credentials
            secret:
              defaultMode: 0400
              secretName: huggingface-secret
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: jetstream-svc
    spec:
      selector:
        app: jetstream-pytorch-server
      ports:
      - protocol: TCP
        name: jetstream-http
        port: 8000
        targetPort: 8000

### Llama 3 8B
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: jetstream-pytorch-server
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: jetstream-pytorch-server
      template:
        metadata:
          labels:
            app: jetstream-pytorch-server
        spec:
          nodeSelector:
            cloud.google.com/gke-tpu-topology: 2x4
            cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
          containers:
          - name: jetstream-pytorch-server
            image: us-docker.pkg.dev/cloud-tpu-images/inference/jetstream-pytorch-server:v0.2.4
            args:
            - --model_id=meta-llama/Meta-Llama-3-8B
            - --override_batch_size=30
            - --enable_model_warmup=True
            volumeMounts:
            - name: huggingface-credentials
              mountPath: /huggingface
              readOnly: true
            ports:
            - containerPort: 9000
            resources:
              requests:
                google.com/tpu: 8
              limits:
                google.com/tpu: 8
            startupProbe:
              httpGet:
                path: /healthcheck
                port: 8000
                scheme: HTTP
              periodSeconds: 60
              initialDelaySeconds: 90
              failureThreshold: 50
            livenessProbe:
              httpGet:
                path: /healthcheck
                port: 8000
                scheme: HTTP
              periodSeconds: 60
              failureThreshold: 30
            readinessProbe:
              httpGet:
                path: /healthcheck
                port: 8000
                scheme: HTTP
              periodSeconds: 60
              failureThreshold: 30
          - name: jetstream-http
            image: us-docker.pkg.dev/cloud-tpu-images/inference/jetstream-http:v0.2.3
            ports:
            - containerPort: 8000
          volumes:
          - name: huggingface-credentials
            secret:
              defaultMode: 0400
              secretName: huggingface-secret
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: jetstream-svc
    spec:
      selector:
        app: jetstream-pytorch-server
      ports:
      - protocol: TCP
        name: jetstream-http
        port: 8000
        targetPort: 8000

The manifest sets the following key properties:

  * `model_id`: the model name from Hugging Face (`google/gemma-7b-it`, `meta-llama/Meta-Llama-3-8B`) (see the [supported models](https://github.com/AI-Hypercomputer/jetstream-pytorch?tab=readme-ov-file#list-out-supported-models)).
  * `override_batch_size`: the decoding batch size per device, where one TPU chip equals one device. This value defaults to `30`.
  * `enable_model_warmup`: this setting enables model warmup after the model server has started. This value defaults to `False`.



You can optionally set these properties:

  * `max_input_length`: the maximum input sequence length. This value defaults to `1024`.
  * `max_output_length`: the maximum output decode length, this value defaults to `1024`.
  * `quantize_weights`: whether the checkpoint is quantized. This value defaults to `0`; set it to 1 to enable `int8` quantization.
  * `internal_jax_compilation_cache`: the directory for the JAX compilation cache. This value defaults to `~/jax_cache`; set it to `gs://BUCKET_NAME/jax_cache` for remote caching.



In the manifest, a [startup probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-startup-probes) is configured to ensure that the model server is labeled `Ready` after the model has been loaded and warmup has completed. [Liveness](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-liveness-http-request) and [readiness](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-readiness-probes) probes are configured to ensure the healthiness of the model server.

  1. Apply the manifest:
         
         kubectl apply -f jetstream-pytorch-deployment.yaml
         

  2. Verify the Deployment:
         
         kubectl get deployment
         

The output is similar to the following:
         
         NAME                              READY   UP-TO-DATE   AVAILABLE   AGE
         jetstream-pytorch-server          0/2     2            0           ##s
         

For Autopilot clusters, it may take a few minutes to provision the required TPU resources.

  3. View the JetStream-PyTorch server logs to check that the model weights have been loaded and model warmup has completed. It might take the server a few minutes to complete this operation.
         
         kubectl logs deploy/jetstream-pytorch-server -f -c jetstream-pytorch-server
         

The output is similar to the following:
         
         Started jetstream_server....
         2024-04-12 04:33:37,128 - root - INFO - ---------Generate params 0 loaded.---------
         

  4. Verify the Deployment is ready:
         
         kubectl get deployment
         

The output is similar to the following:
         
         NAME                              READY   UP-TO-DATE   AVAILABLE   AGE
         jetstream-pytorch-server          2/2     2            2           ##s
         

It might take several minutes for the `healthcheck` endpoint to register.




## Serve the model

In this section, you interact with the model.

### Set up port forwarding

You can access the JetStream Deployment through the [ClusterIP Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#services_of_type_clusterip) that you created in the preceding step. The ClusterIP Services are only reachable from within the cluster. Therefore, to access the Service from outside the cluster, complete the following steps:

To establish a port forwarding session, run the following command:
    
    
    kubectl port-forward svc/jetstream-svc 8000:8000
    

### Interact with the model using curl

  1. Verify that you can access the JetStream HTTP server by opening a new terminal and running the following command:
         
         curl --request POST \
         --header "Content-type: application/json" \
         -s \
         localhost:8000/generate \
         --data \
         '{
             "prompt": "What are the top 5 programming languages",
             "max_tokens": 200
         }'
         

The initial request can take several seconds to complete due to model warmup. The output is similar to the following:
         
         {
             "response": " for data science in 2023?\n\n**1. Python:**\n- Widely used for data science due to its readability, extensive libraries (pandas, scikit-learn), and integration with other tools.\n- High demand for Python programmers in data science roles.\n\n**2. R:**\n- Popular choice for data analysis and visualization, particularly in academia and research.\n- Extensive libraries for statistical modeling and data wrangling.\n\n**3. Java:**\n- Enterprise-grade platform for data science, with strong performance and scalability.\n- Widely used in data mining and big data analytics.\n\n**4. SQL:**\n- Essential for data querying and manipulation, especially in relational databases.\n- Used for data analysis and visualization in various industries.\n\n**5. Scala:**\n- Scalable and efficient for big data processing and machine learning models.\n- Popular in data science for its parallelism and integration with Spark and Spark MLlib."
         }
         
         




You've successfully done the following:

  1. Deployed the JetStream-PyTorch model server on GKE using TPUs.
  2. Served and interacted with the model.



## Observe model performance

To observe the model performance, you can use the JetStream dashboard integration in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). With this dashboard, you can view critical performance metrics like token throughput, request latency, and error rates.

To use the JetStream dashboard, you must enable [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), which collects the metrics from JetStream, in your GKE cluster.

You can then view the metrics by using the JetStream dashboard. For information about using Google Cloud Managed Service for Prometheus to collect metrics from your model, see the [JetStream](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/jetstream) observability guidance in the Cloud Monitoring documentation. 

## Troubleshoot issues

  * If you get the message `Empty reply from server`, it's possible the container has not finished downloading the model data. Check the Pod's logs again for the `Connected` message which indicates that the model is ready to serve.
  * If you see `Connection refused`, verify that your port forwarding is active.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the deployed resources

To avoid incurring charges to your Google Cloud account for the resources that you created in this guide, run the following commands and follow the prompts:
    
    
    gcloud container clusters delete CLUSTER_NAME --location=CONTROL_PLANE_LOCATION
    

## What's next

  * Discover how you can run [Gemma models on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra#serve-open-models-on-gke) and how to run optimized AI/ML workloads with [GKE platform orchestration capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra).
  * Learn more about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Explore the JetStream [GitHub repository](https://github.com/google/JetStream).
  * Explore the [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
