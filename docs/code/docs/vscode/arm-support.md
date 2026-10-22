---
url: https://docs.cloud.google.com/code/docs/vscode/arm-support/
title: Cloud Code support for Arm and mixed-architecture GKE clusters \u00a0|\u00a0 Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:37.260025+00:00
---

# Cloud Code support for Arm and mixed-architecture GKE clusters  |  Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/arm-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Cloud Code support for Arm and mixed-architecture GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines Cloud Code's support for deploying to Arm and mixed-architecture [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine) clusters, as well as [minikube](https://kubernetes.io/docs/tasks/tools/#minikube) clusters.

To learn more about Arm workloads, see [Managing Arm workloads](https://skaffold.dev/docs/workflows/handling-platforms/).

**Note:** minikube does not emulate a platform that isn't your client's platform. For example, you can only build and run an Arm image for minikube if you are on an Arm client.

## Arm and mixed-architecture support tables

Refer to the following table for support based on the workstation you're developing on:

###  x86 workstations 

This table refers to developers using x86 workstations which are deploying to either Arm or mixed-architecture GKE clusters. All of the actions listed under **Actions** are supported for deployments to both Arm and mixed-architecture GKE clusters, except for locally building an Arm image using buildpacks:

Actions | Arm GKE cluster | Mixed-architecture  
GKE cluster  
---|---|---  
Use Cloud Code to locally build an Arm image using [Jib](https://github.com/GoogleContainerTools/jib) |  |   
Use Cloud Code to locally build an Arm image using [Dockerfiles](https://docs.docker.com/engine/reference/builder/) |  |   
Use Cloud Code to locally build an Arm image using buildpacks |  |   
Deploy your Arm image without manual intervention and run or debug your application |  |   
**Note:** Docker Engine on Linux does not come with [QEMU](https://www.qemu.org) emulators installed by default, which is required by Cloud Code's use of Docker BuildX for cross-platform builds. To setup QEMU for Docker builds, see the instructions in [Docker BuildX](https://docs.docker.com/buildx/working-with-buildx/#build-multi-platform-images).

###  Arm workstations 

This table refers to developers using Arm workstations which are deploying to either Arm or mixed-architecture GKE clusters. All of the actions listed under **Actions** are supported for deployments to both Arm and mixed-architecture GKE clusters, as well as minikube clusters, except for locally building an Arm image using buildpacks:

Actions | Arm GKE cluster | Mixed-architecture  
GKE cluster | minikube cluster  
---|---|---|---  
Use Cloud Code to locally build an Arm image using [Jib](https://github.com/GoogleContainerTools/jib) |  |  |   
Use Cloud Code to locally build an Arm image using [Dockerfiles](https://docs.docker.com/engine/reference/builder/) |  |  |   
Use Cloud Code to locally build an Arm image using buildpacks |  |  |   
Deploy your Arm image without manual intervention and run or debug your application |  |  |   
  
To learn more about how you can specify the platform you want to build your images for and override Cloud Code's automatic image building logic, see [Deploy your applications to Arm or mixed-architecture GKE clusters](https://docs.cloud.google.com/code/docs/vscode/deploy-to-arm-amd-mixed-arch)

## Get Support

To send feedback, ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=cloud-code-vscode). If you are a Google Cloud customer, you can file tickets through [standard Google Cloud support channels](https://cloud.google.com/support?e=48754805). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
