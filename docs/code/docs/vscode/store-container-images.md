---
url: https://docs.cloud.google.com/code/docs/vscode/store-container-images/
title: Store your container images in Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:57.450099+00:00
---

# Store your container images in Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/store-container-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Store your container images in Cloud Code for VS Code Stay organized with collections  Save and categorize content based on your preferences. 

To run or debug an application on a remote Kubernetes cluster, you'll need to define the container image repository for your project. You can use any image repository provider, including [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs).

## Specify where container images are stored

If you're logged into Google Cloud in your IDE and you have a default project defined, Cloud Code automatically uses your default container image repository **gcr.io/ PROJECT_ID**, where PROJECT_ID references your default project.

**Note:** If you are running on a local cluster like minikube or Docker Desktop, you do not need to specify these configurations.

If you'd like to update the image repository where the project images are pushed, follow these instructions:

  1. Open the Command Palette (press `Ctrl`/`Cmd`+`Shift`+`P`) and then run the **Cloud Code: Run on Kubernetes** command.
  2. Confirm whether to use the current [Kubernetes context](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/#context) to run the app in (or switch to a preferred one).
  3. You are prompted to select an image registry.
  4. Enter the image repository you want to store your images in.

If your project has [Artifact Registry API enabled](https://docs.cloud.google.com/artifact-registry/docs/enable-service) and at least one [Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/manage-repos), you can browse to and select an existing Artifact Registry repository. 




See the common image repository formats section for examples of how to specify where container images are stored for some common registries.

### Image name creation

Cloud Code concatenates the image registry with the image name specified in the Kubernetes manifests to generate the final image repository name.

For more information, see the [image registry handling guide](https://skaffold.dev/docs/environment/image-registries).

This choice is stored in your `cloudcode.kubernetes` launch configuration (found in .vscode/launch.json). 

Cloud Code builds your containers, pushes them to the registry, applies Kubernetes configurations to the cluster, and waits for the rollout.

### Common image repository formats

Here are examples of how to specify where container images are stored for some common registries:

Docker Hub  | **docker.io/ ACCOUNT**  
  
---|---  
Artifact Registry  | **REGION -docker.pkg.dev/PROJECT_ID/REPO_PATH**  
AWS Elastic Container Registry (ECR)  | **AWS_ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/MY_APP**  
Azure Container Registry (ACR)  | **MY_ACR_NAME.azurecr.io/MY_APP**  
  
## What's next

  * [Create and configure a GKE cluster](https://docs.cloud.google.com/code/docs/vscode/create-configure-gke-cluster).
  * Learn more about [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview).



## Get Support

To send feedback, ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=cloud-code-vscode). If you are a Google Cloud customer, you can file tickets through [standard Google Cloud support channels](https://cloud.google.com/support?e=48754805). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
