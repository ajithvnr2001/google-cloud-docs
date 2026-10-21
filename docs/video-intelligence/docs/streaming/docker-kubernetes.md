---
url: https://docs.cloud.google.com/video-intelligence/docs/streaming/docker-kubernetes/
title: Using Docker & Kubernetes \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:04.878076+00:00
---

# Using Docker & Kubernetes  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/streaming/docker-kubernetes/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Using Docker & Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A [Docker image](https://github.com/google/aistreamer/blob/master/ingestion/env/Dockerfile) is provided for you to evaluate these features. You can download this image as part of the [AIStreamer](https://github.com/google/aistreamer/tree/master/ingestion).

Please note that use of third-party software is solely at your discretion. Google does not own the copyright of third-party software.

## Prerequistes

  * Install [Docker](https://docs.docker.com/install).

  * Install [Google Cloud CLI](https://docs.cloud.google.com/sdk).

  * Install [Kubernetes](https://kubernetes.io/docs/tasks/tools/install-kubectl/#download-as-part-of-the-google-cloud-sdk).




## Build Docker image

Go into the [ingestion directory](https://github.com/google/aistreamer/tree/master/ingestion) and run the following command line on your host machine:
    
    
    $ export DOCKER_IMAGE=gcr.io/gcp-project-name/docker-image-name:version
    $ docker build -t $DOCKER_IMAGE -f env/Dockerfile .

## Try Docker image on your local host

Run following command in the terminal for your host machine:
    
    
    $ docker run -it $DOCKER_IMAGE /bin/bash

The command returns a response similar to the following example.
    
    
    root@e504724e76fc:/#

To open another terminal connecting to Docker, run the following command on the host machine:
    
    
    $ docker exec -it e504724e76fc /bin/bash

Now, you have both host terminals that are in the same Docker container.

## Docker image environment setting

Some environment settings can be customized in the [Docker image](https://github.com/google/aistreamer/blob/master/ingestion/env/Dockerfile).
    
    
    #set up environment for Google Video Intelligence Streaming API
    ENV SRC_DIR /googlesrc  #Source code directory
    ENV BIN_DIR /google     #Binary directory

## Push Docker image to Google Cloud container registry

Run the following command in the terminal for your host machine:
    
    
    $ gcloud docker --verbosity debug -- push $DOCKER_IMAGE

You might need to set access control.

## Deploy to Google Cloud

Run the following commands in the terminal for your host machine:
    
    
    $ export KUBE_ID=any_string_you_like
    $ kubectl run -it $KUBE_ID --image=$DOCKER_IMAGE -- /bin/bash

This returns a response similar to the following:
    
    
    root@$KUBE_ID-215855480-c4sqp:/#

To open another terminal connecting to the same Kubernetes container on Google Cloud, run the following command line on host machine:
    
    
    $ kubectl exec -it $KUBE_ID-215855480-c4sqp -- /bin/bash

Now, you have both host terminals that are in the same Kubernetes container on Google Cloud.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
