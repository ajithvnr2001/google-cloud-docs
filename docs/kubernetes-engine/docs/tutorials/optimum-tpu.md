---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/optimum-tpu/
title: Serve open source models using TPUs on GKE with Optimum TPU \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:47:37.549642+00:00
---

# Serve open source models using TPUs on GKE with Optimum TPU  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/optimum-tpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Serve open source models using TPUs on GKE with Optimum TPU Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to serve large language model (LLM) open source [models](https://github.com/huggingface/optimum-tpu?tab=readme-ov-file#supported-model-and-tasks), using Tensor Processing Units (TPUs) on Google Kubernetes Engine (GKE) with the [Optimum TPU](https://github.com/huggingface/optimum-tpu) serving framework from [Hugging Face](https://huggingface.co/). In this tutorial, you download open source models from Hugging Face and deploy the models on a GKE [Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode#why-standard) cluster using a container that runs Optimum TPU.

This guide provides a starting point if you need the granular control, scalability, resilience, portability, and cost-effectiveness of managed Kubernetes when deploying and serving your AI/ML workloads.

This tutorial is intended for Generative AI customers in the Hugging Face ecosystem, new or existing users of GKE, ML Engineers, MLOps (DevOps) engineers, or platform administrators who are interested in using Kubernetes container orchestration capabilities for serving LLMs.

Google Cloud products like GKE, Vertex AI, and Compute Engine support various serving libraries, such as JetStream, vLLM, and other partner offerings. For example, you can use JetStream to get the latest optimizations from the project. If you prefer Hugging Face options, you can use Optimum TPU.

Optimum TPU supports the following features:

  * Continuous batching
  * Token streaming
  * Greedy search and multinomial sampling using transformers.



## Objectives

  1. Prepare a GKE Standard cluster with the recommended TPU topology based on the model characteristics.
  2. Deploy Optimum TPU on GKE.
  3. Use Optimum TPU to serve the supported models through curl.



## Before you begin

  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

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

  * If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)



  * Create a [Hugging Face](https://huggingface.co/) account, if you don't already have one.
  * [Ensure your project has sufficient quota](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-quota) for Cloud TPU in GKE.



### Required roles

To get the permissions that you need to configure clusters and workloads, ask your administrator to grant you the following IAM roles on the project: 

  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * Manage GKE clusters: [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) 
  * Build and push images to Artifact Registry: [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Prepare the environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with the software you'll need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) and [ gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To set up your environment with Cloud Shell, follow these steps:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         export PROJECT_ID=$(gcloud config get project)
         export CLUSTER_NAME=CLUSTER_NAME
         export REGION=REGION_NAME
         export ZONE=ZONE
         export HF_TOKEN=HF_TOKEN
         

Replace the following values:

     * PROJECT_ID: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * CLUSTER_NAME: the name of your GKE cluster.
     * REGION_NAME: the region where your GKE cluster, Cloud Storage bucket, and TPU nodes are located. The region contains zones where TPU v5e machine types are available (for example, `us-west1`, `us-west4`, `us-central1`, `us-east1`, `us-east5`, or `europe-west4`).
     * (Standard cluster only) ZONE: the zone where the [TPU resources are available](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#availability) (for example, `us-west4-a`). For Autopilot clusters, you don't need to specify the zone, only the region.
     * HF_TOKEN: your HuggingFace token.
  3. Clone the Optimum TPU repository:
         
         git clone https://github.com/huggingface/optimum-tpu.git
         




## Get access to the model

You can use the Gemma 2B or Llama3 8B models. This tutorial focuses on these two models, but [Optimum TPU](https://github.com/huggingface/optimum-tpu/tree/main?tab=readme-ov-file#supported-model-and-tasks) supports more models.

### Gemma 2B

To get access to the Gemma models for deployment to GKE, you must first sign the license consent agreement then generate a Hugging Face access token.

### Sign the license consent agreement

You must sign the consent agreement to use Gemma. Follow these instructions:

  1. Access the [model consent page](https://huggingface.co/google/gemma-2b).
  2. Verify consent using your Hugging Face account.
  3. Accept the model terms.



### Generate an access token

Generate a new [Hugging Face token](https://huggingface.co/docs/hub/security-tokens) if you don't already have one:

  1. Click **Your Profile > Settings > Access Tokens**.
  2. Click **New Token**.
  3. Specify a Name of your choice and a Role of at least `Read`.
  4. Click **Generate a token**.
  5. Copy the generated token to your clipboard.



### Llama3 8B

You must sign the consent agreement to use Llama3 8b in the [Hugging Face Repo](https://huggingface.co/meta-llama/Meta-Llama-3-8B)

### Generate an access token

Generate a new [Hugging Face token](https://huggingface.co/docs/hub/security-tokens) if you don't already have one:

  1. Click **Your Profile > Settings > Access Tokens**.
  2. Select **New Token**.
  3. Specify a Name of your choice and a Role of at least `Read`.
  4. Select **Generate a token**.
  5. Copy the generated token to your clipboard.



## Create a GKE cluster

Create a GKE Standard cluster with 1 CPU node:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --project=PROJECT_ID \
        --num-nodes=1 \
        --location=REGION_NAME
    

## Create TPU node pool

Create a v5e TPU node pool with 1 node and 8 chips:
    
    
    gcloud container node-pools create tpunodepool \
        --location=REGION_NAME \
        --num-nodes=1 \
        --machine-type=ct5lp-hightpu-8t \
        --node-locations=ZONE \
        --cluster=CLUSTER_NAME
    

If TPU resources are available, GKE provisions the node pool. If TPU resources are temporarily unavailable, the output shows a `GCE_STOCKOUT` error message. To troubleshoot resource availability errors, refer to [Insufficient TPU resources to satisfy the TPU request](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/tpus#insufficient-tpu).

## Build the container

Run the make command to build the image
    
    
    cd optimum-tpu && make tpu-tgi
    

### Push the image to the Artifact Registry
    
    
    gcloud artifacts repositories create optimum-tpu --repository-format=docker --location=REGION_NAME && \
    gcloud auth configure-docker REGION_NAME-docker.pkg.dev && \
    docker image tag huggingface/optimum-tpu REGION_NAME-docker.pkg.dev/PROJECT_ID/optimum-tpu/tgi-tpu:latest && \
    docker push REGION_NAME-docker.pkg.dev/PROJECT_ID/optimum-tpu/tgi-tpu:latest
    

## Create a Kubernetes Secret for Hugging Face credentials

Create a Kubernetes Secret that contains the Hugging Face token:
    
    
    kubectl create secret generic hf-secret \
      --from-literal=hf_api_token=${HF_TOKEN} \
      --dry-run=client -o yaml | kubectl apply -f -
    

## Deploy Optimum TPU

To deploy Optimum TPU, this tutorial uses a Kubernetes Deployment. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster..

### Gemma 2B

  1. Save the following Deployment manifest as `optimum-tpu-gemma-2b-2x4.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: tgi-tpu
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: tgi-tpu
           template:
             metadata:
               labels:
                 app: tgi-tpu
             spec:
               nodeSelector:
                 cloud.google.com/gke-tpu-topology: 2x4
                 cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
               containers:
               - name: tgi-tpu
                 image: REGION_NAME-docker.pkg.dev/PROJECT_ID/optimum-tpu/tgi-tpu:latest
                 args:
                 - --model-id=google/gemma-2b
                 - --max-concurrent-requests=4
                 - --max-input-length=8191
                 - --max-total-tokens=8192
                 - --max-batch-prefill-tokens=32768
                 - --max-batch-size=16
                 securityContext:
                     privileged: true
                 env:
                   - name: HF_TOKEN
                     valueFrom:
                       secretKeyRef:
                         name: hf-secret
                         key: hf_api_token
                 ports:
                 - containerPort: 80
                 resources:
                   limits:
                     google.com/tpu: 8
                 livenessProbe:
                   httpGet:
                     path: /health
                     port: 80
                   initialDelaySeconds: 300
                   periodSeconds: 120
         
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: service
         spec:
           selector:
             app: tgi-tpu
           ports:
             - name: http
               protocol: TCP
               port: 8080
               targetPort: 80
         

This manifest describes an Optimum TPU deployment with an internal load balancer on TCP port 8080.

  2. Apply the manifest
         
         kubectl apply -f optimum-tpu-gemma-2b-2x4.yaml
         




### Llama3 8B

  1. Save the following manifest as `optimum-tpu-llama3-8b-2x4.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: tgi-tpu
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: tgi-tpu
           template:
             metadata:
               labels:
                 app: tgi-tpu
             spec:
               nodeSelector:
                 cloud.google.com/gke-tpu-topology: 2x4
                 cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
               containers:
               - name: tgi-tpu
                 image: REGION_NAME-docker.pkg.dev/PROJECT_ID/optimum-tpu/tgi-tpu:latest
                 args:
                 - --model-id=meta-llama/Meta-Llama-3-8B
                 - --max-concurrent-requests=4
                 - --max-input-length=8191
                 - --max-total-tokens=8192
                 - --max-batch-prefill-tokens=32768
                 - --max-batch-size=16
                 env:
                   - name: HF_TOKEN
                     valueFrom:
                       secretKeyRef:
                         name: hf-secret
                         key: hf_api_token
                 ports:
                 - containerPort: 80
                 resources:
                   limits:
                     google.com/tpu: 8
                 livenessProbe:
                   httpGet:
                     path: /health
                     port: 80
                   initialDelaySeconds: 300
                   periodSeconds: 120
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: service
         spec:
           selector:
             app: tgi-tpu
           ports:
             - name: http
               protocol: TCP
               port: 8080
               targetPort: 80
         

This manifest describes an Optimum TPU deployment with an internal load balancer on TCP port 8080.

  2. Apply the manifest
         
         kubectl apply -f optimum-tpu-llama3-8b-2x4.yaml
         




View the logs from the running Deployment:
    
    
    kubectl logs -f -l app=tgi-tpu
    

The output should be similar to the following:
    
    
    2024-07-09T22:39:34.365472Z  WARN text_generation_router: router/src/main.rs:295: no pipeline tag found for model google/gemma-2b
    2024-07-09T22:40:47.851405Z  INFO text_generation_router: router/src/main.rs:314: Warming up model
    2024-07-09T22:40:54.559269Z  INFO text_generation_router: router/src/main.rs:351: Setting max batch total tokens to 64
    2024-07-09T22:40:54.559291Z  INFO text_generation_router: router/src/main.rs:352: Connected
    2024-07-09T22:40:54.559295Z  WARN text_generation_router: router/src/main.rs:366: Invalid hostname, defaulting to 0.0.0.0
    

Make sure the model is fully downloaded before proceeding to the next section.

## Serve the model

Set up port forwarding to the model:
    
    
    kubectl port-forward svc/service 8080:8080
    

### Interact with the model server using curl

Verify your deployed models:

In a new terminal session, use `curl` to chat with the model:
    
    
    curl 127.0.0.1:8080/generate     -X POST     -d '{"inputs":"What is Deep Learning?","parameters":{"max_new_tokens":40}}'     -H 'Content-Type: application/json'
    

The output should be similar to the following:
    
    
    {"generated_text":"\n\nDeep learning is a subset of machine learning that uses artificial neural networks to learn from data.\n\nArtificial neural networks are inspired by the way the human brain works. They are made up of multiple layers"}
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the deployed resources

To avoid incurring charges to your Google Cloud account for the resources that you created in this guide, run the following command:
    
    
    gcloud container clusters delete CLUSTER_NAME \
      --location=REGION_NAME
    

## What's next

  * Explore the Optimum TPU [documentation](https://huggingface.co/docs/optimum-tpu/en/index).
  * Discover how you can run [Gemma models on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra#serve-open-models-on-gke) and how to run optimized AI/ML workloads with [GKE platform orchestration capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra).
  * Learn more about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
