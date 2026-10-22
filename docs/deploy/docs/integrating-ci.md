---
url: https://docs.cloud.google.com/deploy/docs/integrating-ci/
title: Integrating Cloud Deploy with your CI system \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:46.379970+00:00
---

# Integrating Cloud Deploy with your CI system  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/integrating-ci/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Integrating Cloud Deploy with your CI system Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to invoke your Cloud Deploy delivery pipeline from your continuous integration (CI) system.

Integrating Cloud Deploy with your CI system is as simple as adding a call to the Cloud Deploy `gcloud` [CLI](https://docs.cloud.google.com/sdk/gcloud/reference/deploy). This call occurs at the point in your CI pipeline at which your application is ready to be deployed.

**Note:** Your CI process is responsible for building and placing images, so that Cloud Deploy can reference them for deployment.

## Before you begin

The instructions on this page assume you already meet the following conditions:

  * You have [enabled the applicable APIs](https://console.cloud.google.com/apis/enableflow?apiid=clouddeploy.googleapis.com,cloudbuild.googleapis.com,storage-component.googleapis.com,container.googleapis.com&redirect=https://cloud.google.com/deploy/docs/deploy-app-gke&_ga=2.88599711.504283000.1626992575-1788689322.1622287630)

  * You have at least one delivery pipeline [defined](https://docs.cloud.google.com/deploy/docs/config-files) and [registered](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets#register_the_delivery_pipeline_and_targets) with Cloud Deploy.

  * You have at least one [target defined](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions), and your delivery pipeline references that target.




## Calling Cloud Deploy from your CI pipeline

**Note:** the principal calling this command must use [the `clouddeploy.releaser` IAM role](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions#predefined_roles) or an equivalent set of permissions, and must have [`actAs` permission](https://docs.cloud.google.com/iam/docs/service-accounts-actas) for the [service account](https://docs.cloud.google.com/deploy/docs/execution-environment#defaults) used to deploy to the first target and the service account used to perform the [render](https://docs.cloud.google.com/deploy/docs/terminology#render) operation.

The following command creates a new release, thus invoking a delivery pipeline instance:
    
    
    gcloud deploy releases create RELEASE_NAME \
      --delivery-pipeline=PIPELINE_NAME \
      --region=REGION \
      --annotations=[KEY=VALUE,...] \
      --images=[IMAGE_LIST]
    

Where...

  * RELEASE_NAME

is a name you give to this release. This value is required.

You can specify dynamic release names by including `'$DATE'` or `'$TIME'` or both. For example, if you invoke this command at 3:07pm UTC, `'rel-$TIME'` resolves to `rel-1507`. `'$DATE'` and `'$TIME'` must be in single-quotes.

  * PIPELINE_NAME

is the name of your [registered delivery pipeline](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets). This value is required.

  * REGION

is the region in which you're creating this release. The region doesn't need to be the same region in which you're ultimately deploying your application.

  * [KEY=VALUE,...]

is an optional list of one or more annotations to apply to the release, in the form of key-value pairs.

You can use annotations to track release provenance, for example, by passing an annotation like `commitId=0065ca0`. All annotations on the release are returned when you `list` or `get` the release, and are displayed with the release in the Google Cloud console, so you can see release provenance there too.

  * [IMAGE_LIST]

is a comma-separated list of image-name-to-image-path replacements. For example: `--images=image1=path/to/image1:v1@sha256:45db24,image2=path/to/image2:v1@sha256:55xy18`.

This value isn't required if you pass `--build-artifacts`, which identifies a Skaffold build artifacts output file.

When Cloud Deploy renders the manifest, the image name in the unrendered manifest is replaced with the full image reference in the rendered manifest. That is, `image1`, from this example, is in the unrendered manifest and is replaced in the rendered manifest with `path/to/image1:v1@sha256:45db24`.




### Example using direct image reference

The following command creates a new release, passing an image reference directly, rather than a build artifacts file:
    
    
    gcloud deploy releases create my-release \
      --delivery-pipeline=web-app \
      --region=us-central1 \
      --images=image1=path/to/image1:v1@sha256:45db24
    

In this example, `my-release` is the release name. If you want to generate a release name based on date or time, you can include `'$DATE'` or `'TIME'` or both. Time is UTC time on the machine where you invoke the command. `'$DATE'` and `'$TIME'` must be in single quotes.

Here's an example:
    
    
    gcloud deploy releases create rel-'$DATE'-'$TIME' \
      --delivery-pipeline=web-app \
      --region=us-central1 \
      --images=image1=path/to/image1:v1@sha256:45db24
    

In this example, the command generates a release name with the prefix `rel-`, plus the date and time, for example: `rel-20220131-1507`.

It's also common to use the Git SHA in a release name. See the Cloud Build and Docker examples in this document.

### Build artifacts versus images

On the `gcloud deploy releases create` command, you can pass either a set of image references or a build artifacts file reference.

  * Use `--images=[NAME=TAG,...]` to refer to one or more individual container images.

This value is a reference to a collection of individual image name to image full path replacements. Here's an example:

`gcloud deploy releases create my-release --images=image1=path/to/image1:v1@sha256:45db24`

  * Use `--build-artifacts=` to point to a Skaffold build artifacts output file.




### Cloud Build examples, passing a build artifacts file

**Note:** the service account running the Cloud Build trigger must use [the `clouddeploy.releaser` IAM role](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions#predefined_roles) or an equivalent set of permissions, and must have [`actAs` permission](https://docs.cloud.google.com/iam/docs/service-accounts-actas) to deploy to the first target.

#### Docker build example

The following YAML file demonstrates Cloud Build for a [Docker build](https://docs.docker.com/engine/reference/commandline/build/) image push, and ultimately creates a Cloud Deploy release.

This example builds and pushes an image to an artifact repository and constructs a command to create a release, with a release name based on the short commit SHA. This example must be used as a Cloud Build SCM [trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers) because it relies on the `$COMMIT_SHA` variable.

This example pushes an image to a Docker tag that's the same as the commit hash of the source repo. Then the same commit hash, as a Docker tag, is referenced from the release-command arguments.
    
    
    steps:
    # Build and tag using commit sha
    - name: 'gcr.io/cloud-builders/docker'
      args: ['build', '.', '-t', 'REPO_LOCATION/$PROJECT_ID/IMAGE_NAME:${COMMIT_SHA}', '-f', 'Dockerfile']
    # Push the container image
    - name: 'gcr.io/cloud-builders/docker'
      args: ['push', 'REPO_LOCATION/$PROJECT_ID/IMAGE_NAME:${COMMIT_SHA}']
    # Create release in Google Cloud Deploy
    - name: gcr.io/google.com/cloudsdktool/cloud-sdk
      entrypoint: gcloud
      args:
        [
          "deploy", "releases", "create", "rel-${SHORT_SHA}",
          "--delivery-pipeline", "PIPELINE_NAME",
          "--region", "us-central1",
          "--annotations", "commitId=${REVISION_ID}",
          "--images", "IMAGE_NAME=REPO_LOCATION/$PROJECT_ID/IMAGE_NAME:${COMMIT_SHA}"
        ]
    

Note that the image name at the end of this example, `"--images", "IMAGE_NAME=` is substituted in the rendered manifest with the full image reference.

#### An example Cloud Build configuration using Skaffold

The following YAML file is the content of a Cloud Build build configuration that includes a call to Cloud Deploy to create a release, with a release name based on the date. This example also shows Skaffold used for the build.
    
    
    steps:
    - name: gcr.io/k8s-skaffold/skaffold
      args:
        - skaffold
        - build
        - '--interactive=false'
        - '--file-output=/workspace/artifacts.json'
    - name: gcr.io/google.com/cloudsdktool/cloud-sdk
      entrypoint: gcloud
      args:
        [
          "deploy", "releases", "create", "rel-${SHORT_SHA}",
          "--delivery-pipeline", "PIPELINE_NAME",
          "--region", "us-central1",
          "--annotations", "commitId=${REVISION_ID}",
          "--build-artifacts", "/workspace/artifacts.json"
        ]
    

**Note:** in the `gcloud` command included in this example, the release name is passed as `rel-${SHORT_SHA}`. This dynamic naming ensures a unique release name per committed change.

## Connect GitHub Actions to Cloud Deploy

If you're using GitHub Actions for continuous integration or other software delivery-related activities, you can connect to Cloud Deploy for continuous delivery using the [`create-cloud-deploy-release`](https://github.com/marketplace/actions/create-cloud-deploy-release) GitHub Action.

## Connect GitLab to Cloud Deploy

If you use GitLab for continuous integration, you can use the GitLab Cloud Deploy component [create-cloud-deploy-release](https://gitlab.com/google-gitlab-components/cloud-deploy) to create a Cloud Deploy release.

You can also try the [end-to-end tutorial](https://docs.gitlab.com/ee/tutorials/set_up_gitlab_google_integration/) for using GitLab with Google Cloud.

## Using annotations to track the release's provenance

The `--annotations=` flag lets you apply one or more arbitrary key-value pairs to the release that this command creates. You would add this flag to the `gcloud deploy releases create` command.

For example, you can use the following key-value pairs to track the source of the image to be deployed.

Here's an example:
    
    
    gcloud deploy releases create web-app-1029rel \
      --delivery-pipeline=web-app \
      --region=us-central1 \
      --annotations=commitId=0065ca0,author=user@company.com \
      --images=image1=path/to/image1:v1@sha256:45db24
    

You could also create an annotation whose value is the URL pointing to the pull request, for example. For more information, see [Using labels and annotations with Cloud Deploy](https://docs.cloud.google.com/deploy/docs/labels-annotations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
