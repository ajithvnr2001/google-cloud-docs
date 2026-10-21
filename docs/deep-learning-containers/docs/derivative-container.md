---
url: https://docs.cloud.google.com/deep-learning-containers/docs/derivative-container/
title: Create a derivative container \u00a0|\u00a0 Deep Learning Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:33.851521+00:00
---

# Create a derivative container  |  Deep Learning Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-containers/docs/derivative-container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Deep Learning Containers ](https://docs.cloud.google.com/deep-learning-containers/docs)
  * [ Guides ](https://docs.cloud.google.com/deep-learning-containers/docs/overview)



Send feedback 

#  Create a derivative container Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a derivative container based on one of the standard available Deep Learning Containers images.

To complete the steps in this guide, you can use either [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) or any environment where the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) is installed.

## Before you begin

Before you begin, make sure you have completed the following steps.

  1. Complete the set up steps in the Before you begin section of [Getting started with a local deep learning container](https://docs.cloud.google.com/deep-learning-containers/docs/getting-started-local).

  2. Make sure that billing is enabled for your Google Cloud project.

[Learn how to enable billing](https://cloud.google.com/billing/docs/how-to/modify-project)

  3. Enable the Artifact Registry API.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com)




## The Process

To create a derivative container, you'll use a process similar to this:

  1. Create the initial Dockerfile and run modification commands.

To start, you create a Deep Learning Containers container using one of the [available image types](https://docs.cloud.google.com/deep-learning-containers/docs/choosing-container). Then use conda, pip, or Jupyter commands to modify the container image for your needs.

  2. Build and push the container image.

Build the container image, and then push it to somewhere that is accessible to your Compute Engine service account.




## Create the initial Dockerfile and run modification commands

Use the following commands to select a Deep Learning Containers image type and make a small change to the container image. This example shows how to start with a TensorFlow image and updates the image with the latest version of TensorFlow. Write the following commands to the Dockerfile:
    
    
    FROM us-docker.pkg.dev/deeplearning-platform-release/gcr.io/tf-gpu:latest
    # Uninstall the container's TensorFlow version and install the latest version
    RUN pip install --upgrade pip && \
        pip uninstall -y tensorflow && \
        pip install tensorflow

## Build and push the container image

Use the following commands to build and push the container image to Artifact Registry, where it can be accessed by your Google Compute Engine service account.

Create and authenticate the repository:
    
    
    export PROJECT=$(gcloud config list project --format "value(core.project)")
    gcloud artifacts repositories create REPOSITORY_NAME \
        --repository-format=docker \
        --location=LOCATION
    gcloud auth configure-docker LOCATION-docker.pkg.dev

Replace the following:

  * `LOCATION`: The regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories#locations) of the repository, for example `us`. To view a list of supported locations, run the command `gcloud artifacts locations list`.
  * `REPOSITORY_NAME`: The name of the repository that you want to create, for example `my-tf-repo`.



Then, build and push the image:
    
    
    export IMAGE_NAME="LOCATION-docker.pkg.dev/${PROJECT}/REPOSITORY_NAME/tf-custom:v1"
    docker build . -t $IMAGE_NAME
    docker push $IMAGE_NAME

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
