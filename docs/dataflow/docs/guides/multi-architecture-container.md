---
url: https://docs.cloud.google.com/dataflow/docs/guides/multi-architecture-container/
title: Build multi-architecture container images for Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:15.767333+00:00
---

# Build multi-architecture container images for Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/multi-architecture-container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Build multi-architecture container images for Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

If you use a custom container in Dataflow, the container must match the architecture of the worker VMs. This document describes how to create multi-architecture containers that are compatible with both x86 and Arm VMs.

You can use the Docker CLI or [Cloud Build](https://docs.cloud.google.com/build/docs/overview) to build the container image.

## Use Docker to build the image

  1. Create a Dockerfile. Use the `FROM` instruction to specify a multi-architecture base image.
         
         FROM apache/beam_python3.10_sdk:2.50.0
         
         # Make your customizations here, for example:
         ENV FOO=/bar
         COPY path/to/myfile ./
         

  2. Install the [Buildx](https://docs.docker.com/build/architecture/) tool. To check whether the tool is installed, run the following command:
         
         docker buildx version
         

  3. Run the following command to create a builder instance that uses the `docker-container` driver. This driver is required to build multi-architecture images.
         
         docker buildx create --driver=docker-container --use
         

The `--use` flag sets the new builder instance as the current builder.

  4. Run the following command to configure Docker to authenticate requests to Artifact Registry.
         
         gcloud auth configure-docker REGION-docker.pkg.dev
         

Replace REGION with the region of the Artifact Registry repository.

  5. Run the following command to build and push the container image to Artifact Registry:
         
         docker buildx build \
           --platform=linux/amd64,linux/arm64 \
           -t REGISTRY/IMAGE:TAG  \
           --push .
         

Replace the following:

     * REGISTRY: the Docker repository
     * IMAGE: the image name
     * TAG: the image tag



## Use Cloud Build to build the image

  1. Create a Dockerfile. Use the `FROM` instruction to specify a multi-architecture base image.
         
         FROM apache/beam_python3.10_sdk:2.50.0
         
         # Make your customizations here, for example:
         ENV FOO=/bar
         COPY path/to/myfile ./
         

  2. In the same directory that contains the Dockerfile, create a file named `docker_buildx.yaml`. Paste in the following text:
         
         steps:
         - name: 'docker'
           args: ['buildx', 'create', '--driver', 'docker-container', '--name', 'container', '--use']
         - name: 'docker'
           args: ['buildx', 'build', '--platform', 'linux/amd64,linux/arm64', '-t', 'REGISTRY/IMAGE:TAG', '--push', '.']
         

Replace the following:

     * REGISTRY: the Docker repository
     * IMAGE: the image name
     * TAG: the image tag
  3. To build and push the image, run the [`gcloud builds submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit):
         
         gcloud builds submit --region=REGION --config docker_buildx.yaml
         

Replace REGION with the region of the Cloud Build service to use.




For more information, see [Build and push a Docker image with Cloud Build](https://docs.cloud.google.com/build/docs/build-push-docker-image).

## Verify the container image

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click the repository with the container image.

  3. Click the image to see its versions.

  4. Click a version.

  5. Click **Manifest**.

  6. In the manifest file, the `platform` section should have entries for `arm64` and `amd64`. For example:
         
         {
             "schemaVersion": 2,
             "mediaType": "application/vnd.docker.distribution.manifest.list.v2+json",
             "manifests": [
                 {
                   "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
                   "digest": "sha256:441d5438885049e2b388523a8cb5b77ea829c3c3f53326fb221fe185abd67f07",
                   "size": 3074,
                   "platform": {
                       "architecture": "amd64",
                       "os": "linux"
                   }
                 },
                 {
                   "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
                   "digest": "sha256:d3b98b0f8f3f555f5453c79b240bd2b862d4f52d853fe81bae55f01a663de29c",
                   "size": 3073,
                   "platform": {
                       "architecture": "arm64",
                       "os": "linux"
                   }
                 }
             ]
           }
         




## What's next

  * [Use Arm VMs on Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/use-arm-vms)
  * [Run a Dataflow job in a custom container](https://docs.cloud.google.com/dataflow/docs/guides/run-custom-container)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
