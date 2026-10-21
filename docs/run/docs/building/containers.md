---
url: https://docs.cloud.google.com/run/docs/building/containers/
title: Build sources to containers \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:28.406022+00:00
---

# Build sources to containers  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/building/containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Build sources to containers Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run supports [directly deploying source code](https://docs.cloud.google.com/run/docs/deploying-source-code), however, you can also build your source code into a container image and then deploy this container image to Cloud Run. You can use container images for any Cloud Run resource.

Common use cases for decoupling build and deploy operations:

  * **Continuous Integration and Delivery** : Developers author and push code to a source repository, a CI/CD system automatically builds this source code into a container, runs tests, and automatically deploys it to a staging environment.
  * **Infrastructure as Code** : Cloud Run resources that are managed using YAML or Terraform reference a container image URL. The source code written by developers need to be built into a container image.



You can use any system you want to build a container. This page describes the following ways to use Cloud Build to build container images:

  * Using a Dockerfile
  * Using Google Cloud's buildpacks



## Requirements for Cloud Run services

For Cloud Run services, you can use container images built with any tool capable of building container images, as long as they respect the [container contract](https://docs.cloud.google.com/run/docs/reference/container-contract). In particular, your code must listen for HTTP requests on the port defined by the `PORT` environment variable. This `PORT` environment variable is automatically injected by Cloud Run into your container.

## Before you begin

  * You need the [Google Cloud CLI](https://docs.cloud.google.com/run/docs/setup) to run some of the commands in this page.

  * Create a repository at a [supported container registry](https://docs.cloud.google.com/run/docs/deploying#images). To [create an Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#create), run:
        
        gcloud artifacts repositories create REPOSITORY \
                --repository-format=docker \
                --location=LOCATION \
                --description="DESCRIPTION" \
                --immutable-tags \
                --async
        

  * You can configure Docker to get access to Artifact Registry using the [gcloud CLI credential helper](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication#gcloud-helper): 
        
        gcloud auth configure-docker LOCATION-docker.pkg.dev

Replace `LOCATION` with the region name of your container repository, for example, `us-west2`. 



## Build using a Dockerfile

**Caution:** Don't include the file `~/.config/gcloud/gce` in your image. This file is generated if you run Google Cloud CLI commands as part of your image build. It can cause authentication issues when the image runs in Cloud Run.

Before building your sources into a container image ("containerizing") locally using Docker or using Cloud Build, you need a [Dockerfile](https://docs.docker.com/engine/reference/builder/) to be present along with your sources. The [Hello World samples](https://github.com/GoogleCloudPlatform/cloud-run-samples/blob/main/README.md) contain sample applications and Dockerfiles in many popular languages.

If you use Dockerfiles, you can use either of the following methods to build:

  * Build using Cloud Build
  * Build locally using Docker



### Build using Cloud Build

You can build your image on Google Cloud by using [Cloud Build](https://docs.cloud.google.com/build/docs):

  1. Navigate to the folder containing your sources and Dockerfile.

  2. Run the command:
         
         gcloud builds submit --tag IMAGE_URL

Replace `IMAGE_URL` with a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .




For tips on improving build performance, see [Speeding up your builds](https://docs.cloud.google.com/build/docs/speeding-up-builds)

### Build locally and push using Docker

If you have Docker [installed locally](https://docs.docker.com/install/), you can use [`docker build`](https://docs.docker.com/engine/reference/commandline/build/) instead of using Cloud Build or Google Cloud's buildpacks.

To build your container image using Docker:

  1. Navigate to the folder containing your sources and `Dockerfile`.

  2. Run the command:
         
         docker build . --tag IMAGE_URL

Replace `IMAGE_URL` with a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .

Note that if you are using a Mac with Apple silicon, you must specify `--platform linux/amd64` in the command line.

  3. Push the container image to a supported container registry:
         
         docker push IMAGE_URL

Replace `IMAGE_URL` with a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .




To exclude local files from this process, follow the [`.dockerignore` configuration file](https://docs.docker.com/engine/reference/builder/#dockerignore-file) instructions.

## Build using Google Cloud's buildpacks

[Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/builders) is a set of [CNCF-compatible Buildpacks](https://buildpacks.io) that build source code into container images designed to run on Google Cloud container platforms, including Cloud Run.

For a list of supported languages, refer to the [Google Cloud's buildpacks documentation](https://docs.cloud.google.com/docs/buildpacks/builders)

### Build with Google Cloud's buildpacks using Cloud Build

To build with a Google Cloud's buildpacks:

  1. Navigate to the folder containing your sources.

  2. Run the command:
         
         gcloud builds submit --pack image=IMAGE_URL

Replace `IMAGE_URL` with a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .

  3. Wait for the build to complete.




### Build with Google Cloud's buildpacks using the `pack` command line

To build using the [pack command](https://docs.cloud.google.com/docs/buildpacks/build-application):

  1. If you haven't already done so, [install Docker](https://docs.docker.com/install/).

  2. If you haven't already done so, [install `pack`](https://buildpacks.io/docs/tools/pack/cli/install/).

  3. Navigate to the folder containing your sources.

  4. Run the following command to build and push to your supported container registry:
         
         pack build --publish IMAGE_URL

Replace `IMAGE_URL` with a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .

  5. Wait for `pack` to finish.




For more information, read the instructions under [Building an Application](https://docs.cloud.google.com/docs/buildpacks/build-application).

## What's next

  * To deploy your built containers to Cloud Run, follow [Deploying services](https://docs.cloud.google.com/run/docs/deploying).

  * Learn how to [create and update Cloud Run jobs](https://docs.cloud.google.com/run/docs/create-jobs) from your built container image.

  * After your container has been built, you can test locally before deploying to Cloud Run; see [Testing a Cloud Run service locally](https://docs.cloud.google.com/run/docs/testing/local) to learn more.

  * After you create or update a job using the built container, see how to [execute the job](https://docs.cloud.google.com/run/docs/execute/jobs) as a one-off, on a schedule, or as part of a [workflow](https://docs.cloud.google.com/run/docs/triggering/invoke-jobs-with-workflows).

  * To automate the builds and deployments of your Cloud Run services using Cloud Build Triggers, [set up continuous deployment](https://docs.cloud.google.com/run/docs/continuous-deployment).

  * To perform optimal container builds for Java application, see [Building Java containers with Jib](https://docs.cloud.google.com/java/getting-started/jib).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
