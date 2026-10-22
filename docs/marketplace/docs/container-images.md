---
url: https://docs.cloud.google.com/marketplace/docs/container-images/
title: Deploying container images from Google Cloud Marketplace to Kubernetes or Docker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:45.725479+00:00
---

# Deploying container images from Google Cloud Marketplace to Kubernetes or Docker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/container-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Deploying container images from Google Cloud Marketplace to Kubernetes or Docker Stay organized with collections  Save and categorize content based on your preferences. 

This page is a supplemental guide to the container readme for each [Google Cloud Marketplace container product](https://console.cloud.google.com/marketplace/browse?filter=solution-type:container). It provides additional information for deploying a container to a brand new Google Kubernetes Engine cluster or to a local Minikube cluster. It also provides links for using Docker.

As of July 18, 2018, the container registry `launcher.gcr.io` and its alias `l.gcr.io` are deprecated. Docker images in `launcher.gcr.io` remain available, but are no longer updated.

If you are currently pulling images from `launcher.gcr.io`, you must:

  * Change all your references to `marketplace.gcr.io`. 
  * Set up [authentication](https://docs.cloud.google.com/container-registry/docs/advanced-authentication) for Container Registry, using the following command: 
        
        gcloud auth configure-docker
            




# Deploy a container

The following sections describe how to deploy to Kubernetes and to Docker.

## Deploy to Kubernetes

There are two methods to deploy containers to Kubernetes. You can deploy to Google Kubernetes Engine, or locally to your machine using Minikube. Both methods are described below.

### Deploy to Google Kubernetes Engine

  1. **Install the required tools**  
Follow the steps in the [Quickstart for Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster). These steps will help you setup your environment with `gcloud` and `kubectl`.

  2. **Verify that`kubectl` can connect to the clusters**  
After your environment is set up, verify `kubectl` can reach the clusters you created. You can run the following to see if your nodes are running:
         
         kubectl get nodes
         

  3. **Follow the getting started documentation for the container in the Kubernetes section**  
Each container product on Cloud Marketplace contains a getting started guide. You can access the container getting started document by selecting the container you want to deploy from [the Google Cloud console](https://console.cloud.google.com/marketplace/browse?filter=solution-type:container), and then clicking the **Get Started with {**_product name_**}** button near the top of the page.




### Deploy to Minikube

  1. **Install the required tools**  
Follow the steps in the [Minikube Setup guide](https://kubernetes.io/docs/getting-started-guides/minikube/). These steps will help you setup a local Minikube environment. After **minikube start** in the linked instructions, you can then follow the instructions below.

  2. **Verify that`kubectl` can connect to the clusters**  
While Minikube is running (after running `minikube start`), you can use the following command to check if your nodes are running:
         
         kubectl get nodes
         

  3. **Follow the getting started documentation for the container in the Kubernetes section**

Each container product on Cloud Marketplace contains a getting started guide. You can access the container getting started document by selecting the container you want to deploy from [the Google Cloud console](https://console.cloud.google.com/marketplace/browse?filter=solution-type:container), and then clicking the **Get Started with [product_name]** button near the top of the page.




## Deploy to Docker

  1. **Install Docker**

To deploy a container to Docker, first install Docker on your local machine or virtual machine. The Docker installation guide is available from the Docker [website](https://docs.docker.com/engine/installation/).

  2. **Follow the steps in the getting started guide**

Each container product on Cloud Marketplace contains a getting started guide. You can access the container's getting started guide by selecting the container you want to deploy from [the Google Cloud console](https://console.cloud.google.com/marketplace/browse?filter=solution-type:container) and then clicking the **Get Started with [product_name]** button near the top of the page.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
