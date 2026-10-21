---
url: https://docs.cloud.google.com/code/docs/vscode/develop-k8s-remote-dev/
title: Develop a Kubernetes app with remote development \u00a0|\u00a0 Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:13.383864+00:00
---

# Develop a Kubernetes app with remote development  |  Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/develop-k8s-remote-dev/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Develop a Kubernetes app with remote development Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Cloud Code for VS Code [Remote Development](https://code.visualstudio.com/docs/remote/ssh), that is, to open your codebase in a remote container where your application is built, debugged, and deployed. This creates an application that's portable, regardless of the OS of your development machine.

**Note:** For steps to set up remote debugging on Chrome OS, see [Build a dev workflow with Cloud Code on a Pixelbook](https://cloud.google.com/blog/products/application-development/build-a-dev-workflow-with-cloud-code-on-a-pixelbook).

## Prerequisites

In addition to the setup described in [Install the Cloud Code extension](https://docs.cloud.google.com/code/docs/vscode/install), install the [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) VS Code extension pack.

## Setup

  1. To set up a `.devcontainer` folder with a Dockerfile and `Devcontainer.json` file configured for the language you're using, click ![Open a remote window](https://docs.cloud.google.com/static/code/docs/vscode/images/remote-status-bar-icon.png)**Open a Remote Window** > **Add Dev Container Config Files**. Alternatively, you can follow the steps in [Remote development in Containers](https://code.visualstudio.com/docs/remote/containers-tutorial).

After you follow the prompts, your workspace will include:

     * Dockerfile — defines a container image that holds the developer tools to install in a remote development container.

     * `Devcontainer.json` — Instructs the VS Code Remote Tools extension how to run the remote development container.

  2. Open the Dockerfile and add instructions to install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/downloads-interactive) and [Skaffold](https://skaffold.dev/docs/install/). For up-to-date commands, see the installation guides.

  3. In the Dockerfile, add instructions to copy localhost's gcloud CLI and Skaffold configs before the `>> $HOME/.bashrc` command. Alternatively, you can rewrite the commands to install the gcloud CLI and Skaffold.
         
         # Copy localhost's ~/.kube/config file into the container and swap out localhost
         # for host.docker.internal whenever a new shell starts to keep them in sync.
         RUN echo '\n\
         if [ "$SYNC_LOCALHOST_KUBECONFIG" == "true" ]; then\n\
           mkdir -p $HOME/.kube\n\
           cp -r $HOME/.kube-localhost/* $HOME/.kube\n\
           sed -i -e "s/localhost/host.docker.internal/g" $HOME/.kube/config\n\
         \n\
         fi' \
         if [ "$SYNC_LOCALHOST_GCLOUD" == "true" ]; then\n\
          mkdir -p $HOME/.config/gcloud\n\
          cp -r $HOME/.gcloud-localhost/* $HOME/.config/gcloud\n\
         \n\
         fi' \
         

  4. Open the `Devcontainer.json` file and add the following run arguments to copy the gcloud CLI and Skaffold configs from localhost:
         
         "-e", "SYNC_LOCALHOST_KUBECONFIG=true",
           "-e", "SYNC_LOCALHOST_GCLOUD=true",
         

  5. After your files have the required contents, click ![](https://docs.cloud.google.com/static/code/docs/vscode/images/remote-status-bar-icon.png)**Open a Remote Window**.




## Sample devcontainer.json file

The `devcontainer.json` file tells the Remote Container extension which ports to expose in the container, how to mount drives, and which extensions to install in the remote container. The following sample `devcontainer.json` file specifies that the Remote Container extension should install the Cloud Code for VS Code extension:
    
    
       "runArgs": [
             "-v","/var/run/docker.sock:/var/run/docker.sock",
             "--mount", "type=bind,source=${env:HOME}${env:USERPROFILE}/.kube,target=/root/.kube-localhost",
             "--mount", "type=bind,source=${env:HOME}${env:USERPROFILE}/.config/gcloud,target=/root/.gcloud-localhost",
             "-e", "SYNC_LOCALHOST_KUBECONFIG=true",
             "-e", "SYNC_LOCALHOST_GCLOUD=true",
             "--cap-add=SYS_PTRACE", "--security-opt", "seccomp=unconfined"
          ]
    

## What's next

  * Read the Visual Studio docs on [remote development using SSH](https://code.visualstudio.com/docs/remote/ssh).
  * Take a tutorial to [run Visual Studio Code in a docker container](https://code.visualstudio.com/docs/devcontainers/tutorial). using the Dev containers extension.



## Get Support

To send feedback, ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=cloud-code-vscode). If you are a Google Cloud customer, you can file tickets through [standard Google Cloud support channels](https://cloud.google.com/support?e=48754805). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
