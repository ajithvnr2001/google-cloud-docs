---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/create-custom-container/
title: Create a custom container image for training \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:43:10.487999+00:00
---

# Create a custom container image for training  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/create-custom-container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Create a custom container image for training Stay organized with collections  Save and categorize content based on your preferences. 

Using a custom container image provides the most flexibility for training on Gemini Enterprise Agent Platform. To learn how using a custom container image differs from [using a Python training application with a prebuilt container](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/create-python-pre-built-container), read [Training code requirements](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/code-requirements).

The guide walks through the following steps:

  1. Creating a custom container: 
     1. Writing a Dockerfile that sets up your container to work with Agent Platform and includes dependencies needed for your training application.
     2. Building and running your Docker container locally.
  2. Pushing the container image to Artifact Registry.

**Note:** Agent Platform supports Gemini Enterprise Agent Platform serverless training with container images on Artifact Registry or Docker Hub. This guide focuses on using Artifact Registry with Agent Platform.

## Before you begin

To configure an Artifact Registry API repository and set up Docker in your development environment, follow [Artifact Registry's Quickstart for Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/quickstart#before-you-begin). Specifically, make sure to complete the following steps of the quickstart:

  * Before you begin
  * Choose a shell
  * Create a Docker repository
  * Configure authentication



## Create a custom container image

We recommend two possible workflows for creating a custom container image:

  * Write your training code. Then, [use the gcloud CLI's `local-run` command to build and test a custom container image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/containerize-run-code-local) based on your training code without writing a Dockerfile yourself.

This workflow can be more straightforward if you are not familiar with Docker. If you follow this workflow, you can skip the rest of this section.

  * Write your training code. Then, write a Dockerfile and build a container image based on it. Finally, test the container locally.

This workflow offers more flexibility, because you can customize your container image as much as you want.




The rest of this section walks through an example of the latter workflow.

### Training code

You can write training code using any dependencies in any programming language. Make sure your code meets the [training code requirements](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/code-requirements). If you plan to use hyperparameter tuning, GPUs, or distributed training, make sure to read the corresponding sections of that document; these sections describe specific considerations for using the features with custom containers.

### Create a Dockerfile

Create a [Dockerfile](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) to specify all the instructions needed to build your container image.

This section walks through creating a generic example of a Dockerfile to use for serverless training. To learn more about creating a container image, read the [Docker documentation's quickstart](https://docs.docker.com/get-started/).

For use with Agent Platform, your Dockerfile needs to include commands that cover the following tasks:

  * Choose a base image
  * Install additional dependencies
  * Copy your training code to the image
  * Configure the entrypoint for Agent Platform to invoke your training code



Your Dockerfile can include additional logic, depending on your needs. For more information about each specific instruction, see the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).

Dockerfile command | Description | Example(s) | `FROM image:tag` | Specifies a basic image and its tag. | Example base images with tags:

  * `pytorch/pytorch:latest`
  * `tensorflow/tensorflow:nightly`
  * `python:2.7.15-jessie`
  * `nvidia/cuda:9.0-cudnn7-runtime`

  
---|---|---  
`WORKDIR /path/to/directory` | Specifies the directory on the image where subsequent instructions are run. | `/root`  
`RUN pip install pkg1 pkg2 pkg3` | Installs additional packages using `pip`.  
Note: if your base image does not have `pip`, you must include a command to install it before you install other packages. | Example packages:

  * `google-cloud-storage`
  * `cloudml-hypertune`
  * `pandas`

  
`COPY src/training-app.py dest/training-app.py` | Copies the code for your training application into the image. Depending on how your training application is structured, this likely includes multiple files.  | Example names of files in your training application:

  * `model.py`
  * `task.py`
  * `data_utils.py`

  
`ENTRYPOINT ["exec", "file"]` | Sets up the entry point to invoke your training code to run. When you start serverless training, you can override this entrypoint by specifying the `command` field in your [`ContainerSpec`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/CustomJobSpec#ContainerSpec). You can also specify the `args` field in the `ContainerSpec` to provide additional arguments to the entrypoint (and override the container image's [`CMD` instruction](https://docs.docker.com/engine/reference/builder/#cmd) if it has one). | `["python", "task.py"]`  
  
The logic in your Dockerfile may vary according to your needs, but in general it resembles this:
    
    
    # Specifies base image and tag
    FROM image:tag
    WORKDIR /root
    
    # Installs additional packages
    RUN pip install pkg1 pkg2 pkg3
    
    # Downloads training data
    RUN curl https://example-url/path-to-data/data-filename --output /root/data-filename
    
    # Copies the trainer code to the docker image.
    COPY your-path-to/model.py /root/model.py
    COPY your-path-to/task.py /root/task.py
    
    # Sets up the entry point to invoke the trainer.
    ENTRYPOINT ["python", "task.py"]

#### (Optional) Adjust your Dockerfile for TPU VMs

If you want to train on Agent Platform using a TPU VM, then you must adjust your Dockerfile to install specially built versions of the `tensorflow` and `libtpu` libraries. Learn more about [adjusting your container for use with a TPU VM](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/configure-compute#tpu-requirements).

### Build the container image

Create the correct image URI by using environment variables, and then build the Docker image:
    
    
    export PROJECT_ID=$(gcloud config list project --format "value(core.project)")
    export REPO_NAME=REPOSITORY_NAME
    export IMAGE_NAME=IMAGE_NAME
    export IMAGE_TAG=IMAGE_TAG
    export IMAGE_URI=us-central1-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG}
    
    docker build -f Dockerfile -t ${IMAGE_URI} ./
    

In these commands replace the following:

  * REPOSITORY_NAME: the name of the Artifact Registry repository that you created in the Before you begin section.
  * IMAGE_NAME: a name of your choice for your container image.
  * IMAGE_TAG: a tag of your choice for this version of your container image.



Learn more about [Artifact Registry's requirements for naming your container image](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling#tag).

### Run the container locally (optional)

Verify the container image by running it as a container locally. You likely want to run your training code on a smaller dataset or for a shorter number of iterations than you plan to run on Agent Platform. For example, if the entrypoint script in your container image accepts an `--epochs` flag to control how many [epochs](https://developers.google.com/machine-learning/glossary#epoch) it runs for, you might run the following command:
    
    
    docker run ${IMAGE_URI} --epochs 1
    

## Push the container to Artifact Registry

If the local run works, you can push the container to Artifact Registry.

First, run [`gcloud auth configure-docker us-central1-docker.pkg.dev`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/configure-docker) if you have not already done so in your development environment. Then run the following command:
    
    
    docker push ${IMAGE_URI}
    

Models, prediction containers, and training containers are code. It's important to isolate less trusted code from sensitive models and data. Deploy endpoints and training stages in their own projects, use a dedicated service account with very limited permissions, and use VPC Service Controls to isolate them and reduce the impact of access granted to such containers and models. 

### Artifact Registry permissions

If you are using an Artifact Registry image from the same Google Cloud project where you're using Agent Platform, then there is no further need to configure permissions. You can immediately [create a serverless training job](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/create-custom-job) that uses your container image.

However, if you have pushed your container image to Artifact Registry in a different Google Cloud project from the project where you plan to use Agent Platform, then you must grant the Agent Platform Service Agent for your Agent Platform project permission to pull the image from the other project. [Learn more about the Agent Platform Service Agent and how to grant it permissions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#service-agents).

###  Artifact Registry 

To learn how to grant your Agent Platform Service Agent access to your Artifact Registry repository, read the Artifact Registry documentation about [granting repository-specific permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant-repo).

## What's next

  * Learn more about [the concepts involved in using containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/containers-overview).
  * Learn about additional [training code requirements](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/code-requirements) for serverless trainingg.
  * Learn how to [create a serverless training job](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/create-custom-job) or a [training pipeline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/create-training-pipeline) that uses your custom container.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
