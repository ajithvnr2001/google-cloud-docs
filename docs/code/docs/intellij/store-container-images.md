---
url: https://docs.cloud.google.com/code/docs/intellij/store-container-images/
title: Store your container images in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:21:34.365897+00:00
---

# Store your container images in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/store-container-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Store your container images in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

To run or debug an application on a remote Kubernetes cluster, you'll need to define the container image repository for your project. You can use any image repository provider, including [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs).

## Specify where container images are stored

If you're logged into Google Cloud in your IDE and you have a default project defined, Cloud Code automatically uses your default container image repository **gcr.io/ PROJECT_ID**, where PROJECT_ID references your default project.

**Note:** If you are running on a local cluster like minikube or Docker Desktop, you do not need to specify these configurations.

If you'd like to update the image repository where the project images are pushed, follow these instructions:

  1. Navigate to the Run/Debug configuration selector in the Navigation bar or the top-level main menu: **Run** > **Edit Configurations** > **Develop on Kubernetes** > **Image repository**.

  2. Fill in the **Image repository** field.




See the common image repository formats section for examples of how to specify where container images are stored for some common registries.

### Image name creation

Cloud Code concatenates the image registry with the image name specified in the Kubernetes manifests to generate the final image repository name.

For more information, see the [image registry handling guide](https://skaffold.dev/docs/environment/image-registries).

Cloud Code builds your containers, pushes them to the registry, applies Kubernetes configurations to the cluster, and waits for the rollout.

### Common image repository formats

Here are examples of how to specify where container images are stored for some common registries:

Docker Hub  | **docker.io/ ACCOUNT**  
  
---|---  
Artifact Registry  | **REGION -docker.pkg.dev/PROJECT_ID/REPO_PATH**  
AWS Elastic Container Registry (ECR)  | **AWS_ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/MY_APP**  
Azure Container Registry (ACR)  | **MY_ACR_NAME.azurecr.io/MY_APP**  
  
## What's next

  * [Create and configure a GKE cluster](https://docs.cloud.google.com/code/docs/intellij/create-configure-gke-cluster).
  * Learn more about [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview).



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
