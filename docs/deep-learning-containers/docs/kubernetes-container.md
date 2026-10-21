---
url: https://docs.cloud.google.com/deep-learning-containers/docs/kubernetes-container/
title: Train in a container using Google Kubernetes Engine \u00a0|\u00a0 Deep Learning Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:17:49.785756+00:00
---

# Train in a container using Google Kubernetes Engine  |  Deep Learning Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-containers/docs/kubernetes-container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Deep Learning Containers ](https://docs.cloud.google.com/deep-learning-containers/docs)
  * [ Guides ](https://docs.cloud.google.com/deep-learning-containers/docs/overview)



Send feedback 

#  Train in a container using Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to run a training job in a Deep Learning Containers instance, and run that container image on a Google Kubernetes Engine cluster.

## Before you begin

Before you begin, make sure you have completed the following steps.

  1. Complete the set up steps in the Before you begin section of [Getting started with a local deep learning container](https://docs.cloud.google.com/deep-learning-containers/docs/getting-started-local).

  2. Make sure that billing is enabled for your Google Cloud project.

[Learn how to enable billing](https://cloud.google.com/billing/docs/how-to/modify-project)

  3. Enable the Google Kubernetes Engine, Compute Engine, and Artifact Registry APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,compute_component,artifactregistry.googleapis.com)




## Open your command line tool

You can follow this guide using [Cloud Shell](https://cloud.google.com/shell) or command line tools locally. Cloud Shell comes preinstalled with the `gcloud`, `docker`, and `kubectl` command-line tools used in this tutorial. If you use Cloud Shell, you don't need to install these command-line tools on your workstation.

###  Cloud Shell 

To use Cloud Shell, complete the following steps.

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).

  2. Click the **Activate Cloud Shell** button at the top of the console window.

![Google Cloud Platform console](https://docs.cloud.google.com/static/shell/docs/images/shell_icon.png)

A Cloud Shell session opens inside a new frame at the bottom of the console and displays a command-line prompt.

![Cloud Shell session](https://docs.cloud.google.com/static/shell/docs/images/new-console.png)




###  Local command line 

To use your local command line, complete the following steps.

  1. Using the gcloud CLI, install the [Kubernetes](https://kubernetes.io/) command-line tool. `kubectl` is used to communicate with Kubernetes, which is the cluster orchestration system of Deep Learning Containers clusters:
         
         gcloud components install kubectl
         

When you completed the [getting started steps](https://docs.cloud.google.com/deep-learning-containers/docs/getting-started-local), you installed the Google Cloud CLI and [Docker](https://docs.docker.com/engine/installation/).




## Create a GKE cluster

Run the following command to create a two-node cluster in GKE named `pytorch-training-cluster`:
    
    
    gcloud container clusters create pytorch-training-cluster \
        --num-nodes=2 \
        --zone=us-west1-b \
        --accelerator="type=nvidia-tesla-p100,count=1" \
        --machine-type="n1-highmem-2" \
        --scopes="gke-default,storage-rw"
    

For more information on these settings, see the [documentation on creating clusters for running containers](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create).

It may take several minutes for the cluster to be created.

Alternatively, instead of creating a cluster, you can use an existing cluster in your Google Cloud project. If you do this, you may need to run the following command to make sure the `kubectl` command-line tool has the proper credentials to access your cluster:
    
    
    gcloud container clusters get-credentials YOUR_EXISTING_CLUSTER
    

Next, [install the NVIDIA GPU device drivers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers).

## Create the Dockerfile

There are many ways to build a container image. These steps will show you how to build one to run a Python script named `trainer.py`.

To view a list of container images available:
    
    
    gcloud container images list \
        --repository="us-docker.pkg.dev/deeplearning-platform-release/gcr.io"
    

You may want to go to [Choosing a container](https://docs.cloud.google.com/deep-learning-containers/docs/choosing-container) to help you select the container that you want.

The following example will show you how to place a Python script named `trainer.py` into a specific PyTorch deep learning container type.

To create the dockerfile, write the following commands to a file named `Dockerfile`. This step assumes that you have code to train a machine learning model in a directory named `model-training-code` and that the main Python module in that directory is named `trainer.py`. In this scenario, the container will be removed once the job completes, so your training script should be configured to output to Cloud Storage (see [an example of a script that outputs to Cloud Storage](https://github.com/GoogleCloudPlatform/cloudml-samples/blob/master/pytorch/containers/quickstart/mnist/trainer/mnist.py)) or to output to [persistent storage](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes).
    
    
    FROM us-docker.pkg.dev/deeplearning-platform-release/gcr.io/pytorch-gpu
    COPY model-training-code /train
    CMD ["python", "/train/trainer.py"]
    

## Build and upload the container image

To build and upload the container image to Artifact Registry, use the following commands:
    
    
    export PROJECT_ID=$(gcloud config list project --format "value(core.project)")
    export IMAGE_REPO_NAME=pytorch_custom_container
    export IMAGE_TAG=$(date +%Y%m%d_%H%M%S)
    export IMAGE_URI=us-docker.pkg.dev/$PROJECT_ID/$IMAGE_REPO_NAME:$IMAGE_TAG
    
    docker build -f Dockerfile -t $IMAGE_URI ./
    
    docker push $IMAGE_URI
    

## Deploy your application

Create a file named pod.yaml with the following contents, replacing IMAGE_URI with your image's URI.
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: gke-training-pod
    spec:
      containers:
      - name: my-custom-container
        image: IMAGE_URI
        resources:
          limits:
            nvidia.com/gpu: 1
    

Use the `kubectl` command-line tool to run the following command and deploy your application:
    
    
    kubectl apply -f ./pod.yaml
    

To track the pod's status, run the following command:
    
    
    kubectl describe pod gke-training-pod
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
