---
url: https://docs.cloud.google.com/docs/buildpacks/build-run-image/
title: Configure your build and run images \u00a0|\u00a0 Buildpacks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:27:05.569211+00:00
---

# Configure your build and run images  |  Buildpacks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/buildpacks/build-run-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Buildpacks ](https://docs.cloud.google.com/docs/buildpacks)
  * [ Guides ](https://docs.cloud.google.com/docs/buildpacks/overview)



Send feedback 

#  Configure your build and run images Stay organized with collections  Save and categorize content based on your preferences. 

Buildpacks uses a default [builder](https://buildpacks.io/docs/for-platform-operators/concepts/builder/), which consists of all the components necessary to execute a build of your service including both a _build_ and _run_ image:

  * **Build image** : Used by the builder image to create the build environment where the buildpacks [lifecycle](https://buildpacks.io/docs/for-platform-operators/concepts/lifecycle/) is executed. This is where your application or function is prepared for containerization.
  * **Run image** : The base image from which the container image of your service is built. This is the image that hosts your built application or function.



Both images can be customized and extended to suit your needs. For example, you can customize images to add the packages that are required for building your service, or to install system packages so they are available when your service runs.

## Before you begin

You use the `pack` CLI to locally build your service into a container image.

### Before you begin

  1. Install [Docker Community Edition (CE)](https://docs.docker.com/engine/installation/) on your workstation. Docker is used by `pack` as an OCI image builder.
  2. Install [Pack CLI](https://buildpacks.io/docs/tools/pack/).
  3. Install the [Git source control](https://git-scm.com/downloads) tool to fetch the sample application from GitHub.



## Customize the build and run images

Buildpacks use a builder image to construct your service into a container image. When the build process is complete, your application or function is inserted into a run image. Learn more about the build process at [Buildpacks Concepts](https://buildpacks.io/docs/for-platform-operators/concepts/).

### Extending the builder image

To customize the default builder image:

  1. Create a custom `builder.Dockerfile` from the default builder image. You must specify the tag for the [version of the builder](https://docs.cloud.google.com/docs/buildpacks/builders) that supports your base image. For example, the `:v1` base image tag is unsupported by the `:google-22` builder tag.

Example:
         
         FROM gcr.io/buildpacks/builder
         USER root
         RUN apt-get update && apt-get install -y --no-install-recommends \
           subversion && \
           apt-get clean && \
           rm -rf /var/lib/apt/lists/*
         USER cnb
         

  2. Build your custom builder image from the `builder.Dockerfile` file:
         
         docker build -t BUILDER_IMAGE_NAME -f builder.Dockerfile .
         

Replace `BUILDER_IMAGE_NAME` with the name that you choose for your custom builder image.

  3. Run the [`pack build` command](https://buildpacks.io/docs/tools/pack/cli/pack_build/) with your custom builder image to build the new container image of your application or function:
         
         pack build SERVICE_IMAGE_NAME --builder BUILDER_IMAGE_NAME
         

Replace:

     * `SERVICE_IMAGE_NAME` with the name that you choose for your application or function image.
     * `BUILDER_IMAGE_NAME` with the name of your custom builder image.



### Extending the run image

To customize the default run container image:

  1. Create a custom `run.Dockerfile` from the default run image. You must specify the tag for the [version of the builder](https://docs.cloud.google.com/docs/buildpacks/builders) that supports your run image. For example, the `:v1` run image tag is unsupported by the `:google-22` builder tag.

Example:
         
         FROM gcr.io/buildpacks/gcp/run
         USER root
         RUN apt-get update && apt-get install -y --no-install-recommends \
           imagemagick && \
           apt-get clean && \
           rm -rf /var/lib/apt/lists/*
         USER 33:33
         

  2. Build your custom run image from the `run.Dockerfile` file:
         
         docker build -t RUN_IMAGE_NAME -f run.Dockerfile .
         

Replace `RUN_IMAGE_NAME` with the name that you choose for your custom run image.

  3. Run the [`pack build` command](https://buildpacks.io/docs/tools/pack/cli/pack_build/) with your custom run image to build the new container image of your application or function:
         
         pack build SERVICE_IMAGE_NAME --builder gcr.io/buildpacks/builder:v1 --run-image RUN_IMAGE
         

Replace:

     * `SERVICE_IMAGE_NAME` with the name that you choose for your application or function image.
     * `RUN_IMAGE_NAME` with the name of your custom run image.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
