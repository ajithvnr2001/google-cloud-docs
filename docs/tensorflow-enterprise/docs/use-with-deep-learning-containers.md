---
url: https://docs.cloud.google.com/tensorflow-enterprise/docs/use-with-deep-learning-containers/
title: Use TensorFlow Enterprise with a local Deep Learning Containers instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:55.983476+00:00
---

# Use TensorFlow Enterprise with a local Deep Learning Containers instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tensorflow-enterprise/docs/use-with-deep-learning-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ TensorFlow Enterprise ](https://docs.cloud.google.com/tensorflow-enterprise/docs)
  * [ Guides ](https://docs.cloud.google.com/tensorflow-enterprise/docs/getting-started)



Send feedback 

#  Use TensorFlow Enterprise with a local Deep Learning Containers instance Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a brief overview of [Deep Learning Containers](https://docs.cloud.google.com/deep-learning-containers/docs) and describes how to get started using TensorFlow Enterprise with a local Deep Learning Containers instance.

In this example, you create and run a TensorFlow Enterprise Deep Learning Containers instance on your local machine. Then you open a JupyterLab notebook (included by default in the container instance) and run a classification tutorial on using neural networks with Keras.

## Overview of Deep Learning Containers

Deep Learning Containers are a set of Docker containers with key data science frameworks, libraries, and tools pre-installed. These containers provide you with performance-optimized, consistent environments that can help you prototype and implement workflows quickly.

## Before you begin

Complete the following steps to install the Google Cloud CLI and Docker, and then set up your local machine.

### Install gcloud CLI and Docker

Complete these steps to install the gcloud CLI and Docker on your local machine.

  1. [Download and install gcloud CLI](https://docs.cloud.google.com/sdk/docs) on your local machine. You can use the gcloud CLI to interface with your instance.

  2. [Download and install Docker](https://docs.docker.com/get-docker/).




### Set up your local machine

Complete these steps to set up your local machine.

  1. If you're using a Linux-based operating system, such as Ubuntu or Debian, use the following command to add your username to the `docker` group so that you can run Docker without using `sudo`. Replace USERNAME with your username.
         
         sudo usermod -a -G docker USERNAME
         

**Caution:** The `docker` group is equivalent to the `root` user. See [Docker's documentation](https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface) for details on how this affects the security of your system.

You may need to restart your system after adding yourself to the `docker` group.

  2. Open Docker. To ensure that Docker is running, run the following Docker command, which returns the current time and date:
         
         docker run busybox date
         

  3. Use `gcloud` as the credential helper for Docker:
         
         gcloud auth configure-docker
         

  4. **Optional** : If you want to use the GPU-enabled containers, make sure you have a CUDA 10 compatible GPU, the associated driver, [`nvidia-docker`](https://github.com/NVIDIA/nvidia-docker#quickstart) installed.




## Create a Deep Learning Containers instance

To create a TensorFlow Enterprise Deep Learning Containers instance, complete the following for the type of local container that you want to make.

If you don't need to use a GPU-enabled container, use the following command. Replace /path/to/local/dir with the path to your local directory that you want to use.
    
    
    docker run -d -p 8080:8080 -v /path/to/local/dir:/home \
      gcr.io/deeplearning-platform-release/tf2-cpu.2-3
    

If you want to use a GPU-enabled container, use the following command. Replace /path/to/local/dir with the path to your local directory that you want to use.
    
    
    docker run --runtime=nvidia -d -p 8080:8080 -v /path/to/local/dir:/home \
      gcr.io/deeplearning-platform-release/tf2-gpu.2-3
    

This command starts up the container in detached mode, mounts the local directory `/path/to/local/dir` to `/home` in the container, and maps port 8080 on the container to port 8080 on your local machine.

## Open a JupyterLab notebook and run a classification tutorial

The container is preconfigured to start a JupyterLab server. Complete these steps to open a JupyterLab notebook and run a classification tutorial.

  1. In your local browser, visit http://localhost:8080 to access a JupyterLab notebook.

  2. On the left, double-click **tutorials** to open the folder, and navigate to and open **tutorials/tf2_course/01_neural_nets_with_keras.ipynb**.

  3. Click the run button play_arrow to run cells of the tutorial.




## Running your Deep Learning Containers instance on Google Cloud

To run your TensorFlow Enterprise Deep Learning Containers instance in a cloud environment, [learn more about options for running containers on Google Cloud](https://docs.cloud.google.com/container-options). For example, you may want to [run your container on a Google Kubernetes Engine cluster](https://docs.cloud.google.com/deep-learning-containers/docs/kubernetes-container).

## What's next

  * Learn more about [Deep Learning Containers](https://docs.cloud.google.com/deep-learning-containers/docs).
  * [Learn more about the Deep Learning Containers community](https://docs.cloud.google.com/deep-learning-containers/docs/getting-support#get_support_from_the_community), where you can discuss and ask questions about Deep Learning Containers.
  * Get started [using TensorFlow Enterprise with Deep Learning VM](https://docs.cloud.google.com/tensorflow-enterprise/docs/use-with-deep-learning-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
