---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-sdxl-tpu/
title: Serve Stable Diffusion XL (SDXL) using TPUs on GKE with MaxDiffusion \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:35.350906+00:00
---

# Serve Stable Diffusion XL (SDXL) using TPUs on GKE with MaxDiffusion  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-sdxl-tpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Serve Stable Diffusion XL (SDXL) using TPUs on GKE with MaxDiffusion Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to serve a [SDXL](https://stablediffusionxl.com/) image generation model using Tensor Processing Units (TPUs) on Google Kubernetes Engine (GKE) with [MaxDiffusion](https://github.com/google/maxdiffusion). In this tutorial, you download the model from [Hugging Face](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) and deploy it on a [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode#why-autopilot) or [Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode#why-standard) cluster using a container that runs MaxDiffusion.

This guide is a good starting point if you need the granular control, customization, scalability, resilience, portability, and cost-effectiveness of managed Kubernetes when deploying and serving your AI/ML workloads. If you need a unified managed AI platform to rapidly build and serve ML models cost effectively, we recommend that you try our [Vertex AI](https://docs.cloud.google.com/vertex-ai) deployment solution.

## Background

By serving SDXL using TPUs on GKE with MaxDiffusion, you can build a robust, production-ready serving solution with all the benefits of managed [Kubernetes](https://kubernetes.io/), including cost-efficiency, scalability and higher availability. This section describes the key technologies used in this tutorial.

### Stable Diffusion XL (SDXL)

[Stable Diffusion XL (SDXL)](https://arxiv.org/abs/2307.01952) is a type of [latent diffusion model (LDM)](https://github.com/CompVis/latent-diffusion) supported by MaxDiffusion for inference. For generative AI, you can use LDMs to generate high-quality images from text descriptions. LDMs are useful for applications such as image search and image captioning.

SDXL supports single or multi-host inference with sharding annotations. This lets SDXL be trained and run across multiple machines, which can improve efficiency.

To learn more, see the [Generative Models by Stability AI repository](https://github.com/Stability-AI/generative-models) and the [SDXL](https://arxiv.org/abs/2307.01952) paper.

### TPUs

TPUs are Google's custom-developed application-specific integrated circuits (ASICs) used to accelerate machine learning and AI models built using frameworks such as [TensorFlow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/), and [JAX](https://github.com/google/jax).

Before you use TPUs in GKE, we recommend that you complete the following learning path:

  1. Learn about current TPU version availability with the [Cloud TPU system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  2. Learn [about TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).



This tutorial covers serving the SDXL model. GKE deploys the model on single-host TPU v5e nodes with TPU topologies configured based on the model requirements for serving prompts with low latency. In this guide, the model uses a TPU v5e chip with a `1x1` topology.

### MaxDiffusion

MaxDiffusion is a collection of reference implementations, written in Python and Jax, of various latent diffusion models that run on XLA devices, including TPUs and GPUs. MaxDiffusion is a starting point for Diffusion projects for both research and production.

To learn more, refer to the [MaxDiffusion repository](https://github.com/google/maxdiffusion).

## Objectives

This tutorial is intended for generative AI customers who use JAX, new or existing users of SDXL, and any ML Engineers, MLOps (DevOps) engineers, or platform administrators who are interested in using Kubernetes container orchestration capabilities for serving LLMs.

This tutorial covers the following steps:

  1. Create a GKE Autopilot or Standard cluster with the recommended TPU topology, based on the model characteristics.
  2. Build a SDXL inference container image.
  3. Deploy the SDXL inference server on GKE.
  4. Serve and interact with the model through a web app.



## Architecture

This section describes the GKE architecture used in this tutorial. The architecture consists of a GKE Autopilot or Standard cluster that provisions TPUs and hosts MaxDiffusion components. GKE uses these components to deploy and serve the models.

The following diagram shows you the components of this architecture:

![Example architecture of serving MaxDiffusion with TPU v5e on GKE.](https://docs.cloud.google.com/static/kubernetes-engine/images/sdxl-maxdiffusion-arch.svg)

This architecture includes the following components:

  * A GKE Autopilot or Standard regional cluster.
  * One single-host TPU slice node pool that hosts the SDXL model on the MaxDiffusion deployment.
  * The Service component with a load balancer of type `ClusterIP`. This Service distributes inbound traffic to all `MaxDiffusion HTTP` replicas.
  * The `WebApp HTTP` server with an external `LoadBalancer` Service that distributes inbound traffic and redirect model serving traffic to `ClusterIP` Service.



## Before you begin

  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,cloudbuild.googleapis.com)

  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,cloudbuild.googleapis.com)

  * Make sure that you have the following role or roles on the project: roles/container.admin, roles/iam.serviceAccountAdmin, roles/artifactregistry.admin, roles/cloudbuild.builds.editor 

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


  * Check that you have sufficient quota for TPU v5e PodSlice Lite chips. In this tutorial, you use [on-demand instances](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-quota).



## Prepare the environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with the software you'll need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) and [ gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To set up your environment with Cloud Shell, follow these steps:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         gcloud config set billing/quota_project PROJECT_ID
         export PROJECT_ID=$(gcloud config get project)
         export CLUSTER_NAME=CLUSTER_NAME
         export CLUSTER_VERSION=CLUSTER_VERSION
         export REGION=REGION_NAME
         export ZONE=ZONE
         

Replace the following values:

     * PROJECT_ID: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * CLUSTER_NAME: the name of your GKE cluster.
     * CLUSTER_VERSION : the GKE version. You must specify a GKE version that supports TPU Trillium (v6e). For more information, see [Validate TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
     * REGION_NAME: the region where your GKE cluster, Cloud Storage bucket, and TPU nodes are located. The region contains zones where TPU v5e machine types are available (for example, `us-west1`, `us-west4`, `us-central1`, `us-east1`, `us-east5`, or `europe-west4`).
     * (Standard cluster only) ZONE: the zone where the [TPU resources are available](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability) (for example, `us-west4-a`). For Autopilot clusters, you don't need to specify the zone, only the region.
  3. Clone the example repository and open the tutorial directory:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         cd kubernetes-engine-samples/ai-ml/maxdiffusion-tpu
         WORK_DIR=$(pwd)
         gcloud artifacts repositories create gke-llm --repository-format=docker --location=$REGION
         gcloud auth configure-docker $REGION-docker.pkg.dev
         




## Create and configure Google Cloud resources

Follow these instructions to create the required resources.

**Note:** You may need to create a capacity reservation for usage of some accelerators. To learn how to reserve and consume reserved resources, see [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).

### Create a GKE cluster

You can serve SDXL on TPUs in a GKE Autopilot or Standard cluster. We recommend that you use a Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot

  1. In Cloud Shell, run the following command:
         
         gcloud container clusters create-auto ${CLUSTER_NAME} \
           --project=${PROJECT_ID} \
           --location=${REGION} \
           --release-channel=rapid \
           --cluster-version=${CLUSTER_VERSION}
         

GKE creates an Autopilot cluster with CPU and TPU nodes as requested by the deployed workloads.

  2. Configure `kubectl` to communicate with your cluster:
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} --location=${REGION}
         




### Standard

  1. Create a regional GKE Standard cluster that uses [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).
         
         gcloud container clusters create ${CLUSTER_NAME} \
             --enable-ip-alias \
             --machine-type=n2-standard-4 \
             --num-nodes=2 \
             --workload-pool=${PROJECT_ID}.svc.id.goog \
             --location=${REGION}
         

The cluster creation might take several minutes.

  2. Run the following command to create a [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) for your cluster:
         
         gcloud container node-pools create maxdiffusion-tpu-nodepool \
           --cluster=${CLUSTER_NAME} \
           --machine-type=ct5lp-hightpu-1t \
           --num-nodes=1 \
           --location=${REGION} \
           --node-locations=${ZONE} \
           --spot
         

GKE creates a TPU v5e node pool with a `1x1` topology and one node.

To create node pools with different topologies, learn how to [Plan your TPU configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#plan-tpu-configuration). Make sure that you update the sample values in this tutorial, such as `cloud.google.com/gke-tpu-topology` and `google.com/tpu`.

  3. Configure `kubectl` to communicate with your cluster:
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} --location=${REGION}
         




## Build the SDXL inference container

Follow these instructions to build a container image for the SDXL inference server.

  1. Open the `build/server/cloudbuild.yaml` manifest:
         
         steps:
         - name: 'gcr.io/cloud-builders/docker'
           args: [ 'build', '-t', '$LOCATION-docker.pkg.dev/$PROJECT_ID/gke-llm/max-diffusion:latest', '.' ]
         images:
         - '$LOCATION-docker.pkg.dev/$PROJECT_ID/gke-llm/max-diffusion:latest'

  2. Execute the build and create inference container image.
         
         cd $WORK_DIR/build/server
         gcloud builds submit . --region=$REGION
         

The output contains the path of the container image.




## Deploy the SDXL inference server

In this section, you deploy the SDXL inference server. To deploy the server, this tutorial uses a Kubernetes Deployment. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster..

  1. Explore the `serve_sdxl_v5e.yaml` manifest.
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: stable-diffusion-deployment
         spec:
           selector:
             matchLabels:
               app: max-diffusion-server
           replicas: 1  # number of nodes in node-pool
           template:
             metadata:
               labels:
                 app: max-diffusion-server
             spec:
               nodeSelector:
                 cloud.google.com/gke-tpu-topology: 1x1 #  target topology
                 cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                 #cloud.google.com/gke-spot: "true"
               volumes:
               - name: dshm
                 emptyDir:
                       medium: Memory
               containers:
               - name: serve-stable-diffusion
                 image: REGION-docker.pkg.dev/PROJECT_ID/gke-llm/max-diffusion:latest
                 env:
                 - name: MODEL_NAME
                   value: 'stable_diffusion'
                 ports:
                 - containerPort: 8000
                 resources:
                   requests:
                     google.com/tpu: 1  # TPU chip request
                   limits:
                     google.com/tpu: 1  # TPU chip request
                 volumeMounts:
                     - mountPath: /dev/shm
                       name: dshm
         
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: max-diffusion-server
           labels:
             app: max-diffusion-server
         spec:
           type: ClusterIP
           ports:
             - port: 8000
               targetPort: 8000
               name: http-max-diffusion-server
               protocol: TCP
           selector:
             app: max-diffusion-server

  2. Update the project ID in the manifest.
         
         cd $WORK_DIR
         perl -pi -e 's|PROJECT_ID|PROJECT_ID|g' serve_sdxl_v5e.yaml
         perl -pi -e 's|REGION|REGION_NAME|g' serve_sdxl_v5e.yaml
         

  3. Apply the manifest:
         
         kubectl apply -f serve_sdxl_v5e.yaml
         

The output is similar to the following:
         
         deployment.apps/max-diffusion-server created
         

  4. Verify the status of the model:
         
         kubectl get deploy --watch
         

The output is similar to the following:
         
         NAME                          READY   UP-TO-DATE   AVAILABLE   AGE
         stable-diffusion-deployment   1/1     1            1           8m21s
         

  5. Retrieve the `ClusterIP` address:
         
         kubectl get service max-diffusion-server
         

The output contains an `ClusterIP` field. Make a note of the **CLUSTER-IP** value.

  6. Validate the Deployment:
         
         export ClusterIP=CLUSTER_IP
          kubectl run curl --image=curlimages/curl \
             -it --rm --restart=Never \
             -- "$ClusterIP:8000"
         

Replace the CLUSTER_IP with the **CLUSTER-IP** value that you noted previously. The output is similar to the following:
         
         {"message":"Hello world! From FastAPI running on Uvicorn with Gunicorn."}
         pod "curl" deleted
         

  7. View the logs from the Deployment:
         
         kubectl logs -l app=max-diffusion-server
         

When the Deployment finishes, the output is similar to the following:
         
         2024-06-12 15:45:45,459 [INFO] __main__: replicate params:
         2024-06-12 15:45:46,175 [INFO] __main__: start initialized compiling
         2024-06-12 15:45:46,175 [INFO] __main__: Compiling ...
         2024-06-12 15:45:46,175 [INFO] __main__: aot compiling:
         2024-06-12 15:45:46,176 [INFO] __main__: tokenize prompts:2024-06-12 15:48:49,093 [INFO] __main__: Compiled in 182.91802048683167
         INFO:     Started server process [1]
         INFO:     Waiting for application startup.
         INFO:     Application startup complete.
         




## Deploy the webapp client

In this section, you deploy the webapp client to serve the SDXL model.

  1. Explore the `build/webapp/cloudbuild.yaml` manifest.
         
         steps:
         - name: 'gcr.io/cloud-builders/docker'
           args: [ 'build', '-t', '$LOCATION-docker.pkg.dev/$PROJECT_ID/gke-llm/max-diffusion-web:latest', '.' ]
         images:
         - '$LOCATION-docker.pkg.dev/$PROJECT_ID/gke-llm/max-diffusion-web:latest'

  2. Execute the build and create the client container image under the `build/webapp` directory.
         
         cd $WORK_DIR/build/webapp
         gcloud builds submit . --region=$REGION
         

The output contains the path of the container image.

  3. Open the `serve_sdxl_client.yaml` manifest:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: max-diffusion-client
         spec:
           selector:
             matchLabels:
               app: max-diffusion-client
           template:
             metadata:
               labels:
                 app: max-diffusion-client
             spec:
               containers:
               - name: webclient
                 image: REGION-docker.pkg.dev/PROJECT_ID/gke-llm/max-diffusion-web:latest
                 env:
                   - name: SERVER_URL
                     value: "http://ClusterIP:8000"
                 resources:
                   requests:
                     memory: "128Mi"
                     cpu: "250m"
                   limits:
                     memory: "256Mi"
                     cpu: "500m"
                 ports:
                 - containerPort: 5000
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: max-diffusion-client-service
         spec:
           type: LoadBalancer
           selector:
             app: max-diffusion-client
           ports:
           - port: 8080
             targetPort: 5000

  4. Edit the project ID in the manifest:
         
         cd $WORK_DIR
         perl -pi -e 's|PROJECT_ID|PROJECT_ID|g' serve_sdxl_client.yaml
         perl -pi -e 's|ClusterIP|CLUSTER_IP|g' serve_sdxl_client.yaml
         perl -pi -e 's|REGION|REGION_NAME|g' serve_sdxl_client.yaml
         

  5. Apply the manifest:
         
         kubectl apply -f serve_sdxl_client.yaml
         

  6. Retrieve the `LoadBalancer` IP address:
         
         kubectl get service max-diffusion-client-service
         

The output contains an `LoadBalancer` field. Make a note of the **EXTERNAL-IP** value.


**Success:** You've successfully deployed the SDXL model using MaxDiffusion and TPU v5e in GKE.

## Interact with the model by using the web page

  1. Access to the following URL from a web browser:
         
         http://EXTERNAL_IP:8080
         

Replace the EXTERNAL_IP with the `EXTERNAL_IP` value that you noted previously.

  2. Interact with SDXL using the chat interface. Add a prompt and click **Submit**. For example:
         
         Create a detailed image of a fictional historical site, capturing its unique architecture and cultural significance
         




The output is a model-generated image similar to the following example:

![SDXL-generated image](https://docs.cloud.google.com/static/kubernetes-engine/images/ai-maxdiffusion-image.png)

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resources

Keep the project and delete the individual resources, as described in the following section. Run the following commands and follow the prompts:
    
    
    gcloud container clusters delete ${CLUSTER_NAME} --location=${REGION}
    

## What's next

  * Configure the tutorial with other TPU topologies. To learn more about other TPU topologies, see [Plan your TPU configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#plan-tpu-configuration).
  * Explore the MaxDiffusion inference server sample code in [the sample repository that you cloned in this tutorial](https://github.com/GoogleCloudPlatform/ai-on-gke/blob/36fa5c8d31c85e70b7035353bcd591ec3c3066fc/tutorials-and-examples/inference-servers/maxdiffusion/build/server/main.py).
  * Learn more about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Explore the JetStream [GitHub repository](https://github.com/google/JetStream).
  * Explore the [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
