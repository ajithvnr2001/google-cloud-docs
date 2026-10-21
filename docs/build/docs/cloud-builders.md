---
url: https://docs.cloud.google.com/build/docs/cloud-builders/
title: Cloud builders \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:02.378180+00:00
---

# Cloud builders  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/cloud-builders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Cloud builders Stay organized with collections  Save and categorize content based on your preferences. 

**Cloud builders** are [container images](https://cloud.google.com/containers) with common languages and tools installed in them. You can [configure Cloud Build](https://docs.cloud.google.com/build/docs/build-config) to run a specific command within the context of these builders.

This page describes the types of builders that you can use with Cloud Build.

## Publicly available images

Cloud Build lets you use any publicly available image to execute your tasks. To use an image, specify the image URL in the `name` field in your config file. Use the `args` field to specify commands that you want to run within the image. The `args` field of a build step takes a list of arguments and passes them to the image referenced by the `name` field.

**Note:** When you pull a public container image from Docker Hub to use in your build config file, Cloud Build automatically checks the caching proxy `mirror.gcr.io` for a cached copy of the container image. If a cached copy is unavailable, Cloud Build pulls your requested image from Docker Hub and the caching proxy might cache the image for future use. For more information, see [Pull cached Docker Hub images](https://docs.cloud.google.com/artifact-registry/docs/pull-cached-dockerhub-images).

The following code snippet shows how to use the public `ubuntu` image from [Docker Hub](https://hub.docker.com/explore/) and execute a command within that image:
    
    
    steps:
    - name: 'ubuntu'
      args: ['echo', 'hello world']
    

Here's another example code snippet that uses the image for Black Duck open source scanner for Cloud Build from [Google Cloud console Launcher](https://console.cloud.google.com/launcher/browse?filter=solution-type:container):
    
    
    steps:
    - name: launcher.gcr.io/blackduck-public/blackducksoftware-containerbuilder-scanner
      ...
    

For more examples on how to use publicly available images from Docker Hub for your tasks, see [Building Node.js applications](https://docs.cloud.google.com/build/docs/building/build-nodejs) and [Building Go applications](https://docs.cloud.google.com/build/docs/building/build-containerize-go).

**Note:** Cloud Build runs its build steps in a Docker container. To use an image from Docker Hub, just specify the name of the image, such as `ubuntu`. To use an image from other registries, specify the full registry path of the image, such as `gcr.io/cloud-builders/gcloud`.

## Supported builder images provided by Cloud Build

Cloud Build provides and maintains prebuilt images that you can reference in your [config file](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#buildstep) to execute your tasks. You can find these prebuilt images in the following location:
    
    
    gcr.io/cloud-builders/...
    

The source code for these builders is available in the [cloud builders GitHub repository](https://github.com/GoogleCloudPlatform/cloud-builders).

For examples on how to use supported prebuilt images, see [Building container images](https://docs.cloud.google.com/build/docs/building/build-containers) and [Deploying to Cloud Run](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run).

The following table lists some examples of supported builder images:

Builder | Name | Example  
---|---|---  
[bazel](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/bazel) | `gcr.io/cloud-builders/bazel` | [bazel example](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/bazel)  
[docker](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/docker) | `gcr.io/cloud-builders/docker` | [docker example](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/docker)  
[git](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/git) | `gcr.io/cloud-builders/git` | [git example](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/git)  
[gcloud](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/gcloud) | `gcr.io/cloud-builders/gcloud` | [gcloud example](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/gcloud)  
[gke-deploy](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/gke-deploy) | `gcr.io/cloud-builders/gke-deploy` | [gke-deploy example](https://github.com/GoogleCloudPlatform/cloud-builders/blob/master/gke-deploy/doc/app/cloudbuild-with-configs.yaml)  
[gradle](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/gradle) | `gcr.io/cloud-builders/gradle` | [gradle example](https://github.com/GoogleCloudPlatform/cloud-builders/blob/master/gradle/examples/spring_boot/cloudbuild.yaml)  
[maven](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/mvn) | `gcr.io/cloud-builders/mvn` | [maven example](https://github.com/GoogleCloudPlatform/cloud-builders/blob/master/mvn/examples/spring_boot/cloudbuild.yaml)  
**[The complete list of supported builders for Cloud Build.](https://github.com/GoogleCloudPlatform/cloud-builders)**  
  
## Community-contributed builders

The Cloud Build developer community provides [open-source builders](https://github.com/GoogleCloudPlatform/cloud-builders-community) that you can use to execute your tasks. Prebuilt images are not available for these builders; to use these builders, download the source code from the [cloud builders community GitHub repository](https://github.com/GoogleCloudPlatform/cloud-builders-community) and then build the image. For an example on how to build a community-contributed builder and then use it for your tasks, see [Building VM images using Packer](https://docs.cloud.google.com/build/docs/building/build-vm-images-with-packer).

The following table lists some examples of community-contributed builders:

Builder | Descriptionp   
---|---  
[`docker-compose`](https://github.com/GoogleCloudPlatform/cloud-builders-community/tree/master/docker-compose) | Runs integration tests on docker images.  
[`harness-chaos`](https://github.com/GoogleCloudPlatform/cloud-builders-community/tree/master/harness-chaos) | Launch chaos experiments and test the resilience of applications with [Harness Chaos Engineering](https://developer.harness.io/docs/chaos-engineering/get-started/overview).  
[`helm`](https://github.com/GoogleCloudPlatform/cloud-builders-community/tree/master/helm) | Manages Kubernetes packages using [Helm](https://docs.helm.sh/).  
[`pack`](https://github.com/GoogleCloudPlatform/cloud-builders-community/tree/master/pack) | Executes your build step using the specified [Cloud Native Buildpack](https://buildpacks.io/).  
[`packer`](https://github.com/GoogleCloudPlatform/cloud-builders-community/tree/master/packer) | Automates the creation of machine images using [Packer](https://www.packer.io/).  
[`remote-builder`](https://github.com/GoogleCloudPlatform/cloud-builders-community/tree/master/remote-builder) | Executes your build step on a configurable Compute Engine VM.  
**[The complete list of community-contributed builders for Cloud Build.](https://github.com/GoogleCloudPlatform/cloud-builders-community)**  
  
Community-contributed builders are maintained by the open-source community at [cloud builders community](https://github.com/GoogleCloudPlatform/cloud-builders-community#contributing). Cloud Build does **not** officially maintain these builders. For information on contributing to a builder, see the [cloud builders community](https://github.com/GoogleCloudPlatform/cloud-builders-community#contributing) GitHub page.

## Writing your own custom builder

You can create your own **custom builder** for use in your builds. A custom builder is a container image that the Cloud Build pulls and runs with your source. Your custom builder can execute any script or binary inside the container; as such it can do anything a container can do. For instructions on creating a custom builder, see [Creating custom build steps](https://docs.cloud.google.com/build/docs/create-custom-build-steps).

## What's next

  * Learn how to [use community-contributed builders and custom builders](https://docs.cloud.google.com/build/docs/configuring-builds/use-community-and-custom-builders).
  * Learn about the structure of a [build configuration file](https://docs.cloud.google.com/build/docs/build-config).
  * Learn how to use a [publicly available `node` image to build `Node.js` applications](https://docs.cloud.google.com/build/docs/building/build-nodejs).
  * Learn how to [use a prebuilt `gcloud` image to deploy to Cloud Run functions](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-functions).
  * Learn how to [use a community-contributed `firebase` image to deploy on Firebase](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-firebase).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
