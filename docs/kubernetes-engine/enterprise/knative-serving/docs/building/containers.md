---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/building/containers/
title: Building containers \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:46.175632+00:00
---

# Building containers  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/building/containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Building containers Stay organized with collections  Save and categorize content based on your preferences. 

Knative serving accepts container images built with any tool capable of building container images, as long as they respect the [container contract](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/reference/container-contract). In particular, your code must listen for HTTP requests on the port defined by the `PORT` environment variable. This `PORT` environment variable is automatically injected by Knative serving into your container.

This page describes several ways to build container images:

  * Using a Dockerfile
  * Using Buildpacks



## Building using a Dockerfile

If you use Dockerfiles, you can use either of the following methods to build:

  * Build using Cloud Build
  * Build locally using Docker



### Building using Cloud Build

To build your image on Google Cloud:

  1. Navigate to the folder containing your sources and Dockerfile.

  2. Run the command:
         
         gcloud builds submit --tag IMAGE_URL

Replace IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.




For detailed Cloud Build instructions, see [Deploying to Knative serving](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run#building_and_deploying_a_container).

For tips on improving build performance, see [Speeding up your Builds](https://docs.cloud.google.com/build/docs/speeding-up-builds)

### Building locally and pushing using Docker

If you have Docker [installed locally](https://docs.docker.com/install/), you can use [`docker build`](https://docs.docker.com/engine/reference/commandline/build/) instead of using Cloud Build or Buildpacks.

Before building your sources into a container image ("containerizing") using Docker, you need a [Dockerfile](https://docs.docker.com/engine/reference/builder/) to be present along your sources. The following instructions use Container Registry as the image registry.

**Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).

To build your container image using Docker:

  1. Navigate to the folder containing your sources and `Dockerfile`.

  2. Run the command:
         
         docker build . --tag IMAGE_URL

Replace IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.

  3. If you have not yet configured Docker to use the Google Cloud CLI to authenticate requests to Container Registry, do so now using the command:
         
         gcloud auth configure-docker

You need to do this before you can push or pull images using Docker. You only need to do it once.

  4. Push the container image to Container Registry:
         
         docker push IMAGE_URL

Replace IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.




To exclude local files from this process, follow the [`.dockerignore` configuration file](https://docs.docker.com/engine/reference/builder/#dockerignore-file) instructions.

## Building using Buildpacks

For complete information on Buildpacks, see the [Buildpacks](https://buildpacks.io/) website. Google provides a set of [CNCF-compatible Buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview) that build source code into container images designed to run on Google Cloud container platforms, including Knative serving.

These platforms are currently supported:

  * Go
  * Node.js
  * Python
  * Java
  * .NET Core



### Building with Buildpacks using Cloud Build

To build with a Buildpack:

  1. Navigate to the folder containing your sources.

  2. Run the command:
         
         gcloud builds submit --pack image=IMAGE_URL

Replace IMAGE_URL with the container image URL, for example, `gcr.io/myproject/myservice`.

  3. Wait for the build to complete.




### Building with Buildpack using the `pack` command line

To build using the [pack command](https://github.com/buildpacks/pack):

  1. If you haven't already done so, [install Docker](https://docs.docker.com/install/).

  2. If you have not yet configured Docker to use the Google Cloud CLI to authenticate requests to Container Registry, do so now using the command:
         
         gcloud auth configure-docker

You need to do this before you can push or pull images using Docker. You only need to do it once.

  3. If you haven't already done so, [install `pack`](https://buildpacks.io/docs/tools/pack/cli/install/).

  4. Navigate to the folder containing your sources.

  5. Run the following command to build and push to your container registry:
         
         pack build --publish IMAGE_URL

Replace IMAGE_URL with a reference to the container image, for example, `gcr.io/cloudrun/hello`.

  6. Wait for `pack` to finish.




For more information, read the instructions under [Building an Application](https://docs.cloud.google.com/docs/buildpacks/build-application).

## What's next

  * To learn more about the contract your containers must respect to be deployed to Knative serving, see [Container Contract](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/reference/container-contract).

  * To deploy your built containers to Knative serving, follow [Deploying Services](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploying).

  * To automate the builds and deployments of your Knative serving services using Cloud Build Triggers, [set up Continuous Deployment](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/continuous-deployment-with-cloud-build).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
