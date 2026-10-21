---
url: https://docs.cloud.google.com/deep-learning-containers/docs/getting-started-local/
title: Get started with a local deep learning container \u00a0|\u00a0 Deep Learning Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:55:16.194419+00:00
---

# Get started with a local deep learning container  |  Deep Learning Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-containers/docs/getting-started-local/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Deep Learning Containers ](https://docs.cloud.google.com/deep-learning-containers/docs)
  * [ Guides ](https://docs.cloud.google.com/deep-learning-containers/docs/overview)



Send feedback 

#  Get started with a local deep learning container Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and set up a local deep learning container. This guide expects you to have basic familiarity with [Docker](https://www.docker.com/).

## Before you begin

Complete the following steps to set up a Google Cloud account, enable the required APIs, and install and activate the required software.

  1. In the Google Cloud Console, go to the **Manage resources** page and select or create a project.

**Note:** If you don't plan to keep the resources you create in this tutorial, create a new project instead of selecting an existing project. After you finish, you can delete the project, removing all resources associated with the project and tutorial.

[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs).

  3. [Install Docker](https://docs.docker.com/install/).

If you're using a Linux-based operating system, such as Ubuntu or Debian, add your username to the `docker` group so that you can run Docker without using `sudo`:
         
         sudo usermod -a -G docker ${USER}
         

**Caution:** The `docker` group is equivalent to the `root` user. See [Docker's documentation](https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface) for details on how this affects the security of your system.

You may need to restart your system after adding yourself to the `docker` group.

  4. Open Docker. To ensure that Docker is running, run the following Docker command, which returns the current time and date:
         
         docker run busybox date
         

  5. Use `gcloud` as the credential helper for Docker:
         
         gcloud auth configure-docker
         

  6. **Optional** : If you want to run the container using GPU locally, install [`nvidia-docker`](https://github.com/NVIDIA/nvidia-docker#quickstart).




## Create your container

Follow these steps to create your container.

  1. To view a list of containers available:
         
         gcloud container images list \
           --repository="gcr.io/deeplearning-platform-release"
         

You may want to go to [Choosing a container](https://docs.cloud.google.com/deep-learning-containers/docs/choosing-container) to help you select the container that you want.

  2. If you don't need to use a GPU-enabled container, enter the following code example. Replace tf-cpu.1-13 with the name of the container that you want to use.
         
         docker run -d -p 8080:8080 -v /path/to/local/dir:/home/jupyter \
           gcr.io/deeplearning-platform-release/tf-cpu.1-13
         

If you want to use a GPU-enabled container, enter the following code example. Replace tf-gpu.1-13 with the name of the container that you want to use.
         
         docker run --runtime=nvidia -d -p 8080:8080 -v /path/to/local/dir:/home/jupyter \
           gcr.io/deeplearning-platform-release/tf-gpu.1-13
         




This command starts up the container in detached mode, mounts the local directory `/path/to/local/dir` to `/home/jupyter` in the container, and maps port 8080 on the container to port 8080 on your local machine. The container is preconfigured to start a JupyterLab server, which you can visit at `http://localhost:8080`.

## What's next

  * Learn more about how to work with containers in the [Docker documentation](https://docs.docker.com).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
