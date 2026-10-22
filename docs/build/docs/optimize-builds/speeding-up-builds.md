---
url: https://docs.cloud.google.com/build/docs/optimize-builds/speeding-up-builds/
title: Best practices for speeding up builds \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:03.538155+00:00
---

# Best practices for speeding up builds  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/optimize-builds/speeding-up-builds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Best practices for speeding up builds Stay organized with collections  Save and categorize content based on your preferences. 

This page provides best practices for speeding up Cloud Build builds.

## Building leaner containers

When you containerize an application, files that are not needed at runtime, such as build-time dependencies and intermediate files, can be inadvertently included in the container image. These unneeded files can increase the size of the container image and add extra time and cost as the image moves between your container image registry and your container runtime.

To help reduce the size of your container image, separate the building of the application, along with the tools used to build it, from the assembly of the runtime container.

For more information, see [Building leaner containers](https://docs.cloud.google.com/build/docs/building-leaner-containers).

## Using a cached Docker image

The easiest way to increase the speed of your Docker image build is by specifying a cached image that can be used for subsequent builds. You can specify the cached image by adding the `--cache-from` argument in your build config file, which will instruct Docker to build using that image as a cache source.

Each Docker image is made up of stacked layers. Using `--cache-from` rebuilds all the layers from the changed layer until the end of the build; therefore using `--cache-from` is not beneficial if you change a layer in the earlier stages of your Docker build.

It is recommended that you always use `--cache-from` for your builds, but keep the following caveats in mind:

  * You need a previously built Docker image to cache from.
  * You can use `--cache-from` only for Docker builds; you cannot use it for builders that create other kind of artifacts.
  * The cached image must be retrieved from a registry, which may add to the time it takes to build.



The following steps explain how to build using a previously cached image:

###  YAML 

  1. In your build config, add instructions to:

     * Pull the cached image from Artifact Registry. The `docker pull` build step sets the `entrypoint` to `bash`, which lets you run the command and ignore the returned error. This configuration is required when you build an image for the first time, and `docker pull` doesn't have an existing image to pull.
     * Add a `--cache-from` argument to use that image for rebuilds.
           
           steps:
           - name: 'gcr.io/cloud-builders/docker'
             entrypoint: 'bash'
             args: ['-c', 'docker pull ${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/${_IMAGE}:latest || exit 0']
           - name: 'gcr.io/cloud-builders/docker'
             args: [
                       'build',
                       '-t', '${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/${_IMAGE}:latest',
                       '--cache-from', '${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/${_IMAGE}:latest'
                       '.'
                   ]
           images: ['${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/${_IMAGE}:latest']
           

  2. Build your image using the previous build config:
         
         gcloud builds submit --config cloudbuild.yaml .
         




###  JSON 

  1. In your build config, add instructions to:

     * Pull the cached image from Artifact Registry. The `docker pull` build step sets the `entrypoint` to `bash`, which lets you run the command and ignore the returned error. This configuration is required when you build an image for the first time, and `docker pull` doesn't have an existing image to pull.
     * Add a `--cache-from` argument to use that image for rebuilds.
    
    {
        "steps": [
        {
            "name": "gcr.io/cloud-builders/docker",
            "entrypoint": "bash",
            "args": ["-c", "docker pull ${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/${_IMAGE}:latest || exit 0"]
        },
        {
            "name": "gcr.io/cloud-builders/docker",
            "args": [
                "build",
                "-t",
                "${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/${_IMAGE}:latest",
                "--cache-from",
                "${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/${_IMAGE}:latest",
                "."
            ]
        }
        ],
        "images": ["${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/${_IMAGE}:latest"]
    }
    
    
    where [IMAGE] is the name of your image.
    

  2. Build your image using the previous build config:
         
         gcloud builds submit --config cloudbuild.json .
         




## Caching directories with Google Cloud Storage

To increase the speed of a build, reuse the results from a previous build. You can copy the results of a previous build to a Cloud Storage bucket, use the results for faster calculation, and then copy the new results back to the bucket. Use this method when your build takes a long time and produces a small number of files that does not take time to copy to and from Cloud Storage

Unlike `--cache-from`, which is only for Docker builds, Cloud Storage caching can be used for [any builder supported by Cloud Build](https://github.com/GoogleCloudPlatform/cloud-builders).

Use the following steps to cache directories using Cloud Storage:

###  YAML 

  1. In your build config file, add instructions to:

     * Copy the results of a previous build from the Cloud Storage bucket.
     * Use the results for the current build.
     * Copy the new results back into the bucket.
           
           steps:
           - name: gcr.io/cloud-builders/gcloud
               args: ['storage', 'cp', 'gs://mybucket/results.zip', 'previous_results.zip']
           # operations that use previous_results.zip and produce new_results.zip
           - name: gcr.io/cloud-builders/gcloud
               args: ['storage', 'cp', 'new_results.zip', 'gs://mybucket/results.zip']
           

  2. Build your code using the previous build config:
         
         gcloud builds submit --config cloudbuild.yaml .
         




###  JSON 

  1. In your build config file, add instructions to:

     * Copy the results of a previous build from the Cloud Storage bucket.
     * Use the results for the current build.
     * Copy the new results back into the bucket.
           
           {
               "steps": [
               {
                   "name": "gcr.io/cloud-builders/gcloud",
                   "args": ["storage", "cp", "gs://mybucket/results.zip", "previous_results.zip"]
               },
               {
                   // operations that use previous_results.zip and produce new_results.zip
               },
               {
                   "name": "gcr.io/cloud-builders/gcloud",
                   "args": ["storage", "cp", "new_results.zip", "gs://mybucket/results.zip"]
               }
               ]
           }
           

  2. Build your code using the previous build config:
         
         gcloud builds submit --config cloudbuild.json .
         




## Avoiding the upload of unnecessary files

When a build is triggered from a [Cloud Build trigger](https://docs.cloud.google.com/build/docs/triggers), your code directory is uploaded for use by Cloud Build.

You can exclude files not needed by your build with a [`.gcloudignore`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) file to optimize the upload time.

Examples of commonly excluded files include:

  * Documentation and sample code for project developers
  * Generated scaffolding code, binaries, `*.jar` files, or compiled web assets used for development.
  * Vendor-owned, third-party dependencies for local development



To prepare a `.gcloudignore` file to address these cases, create a file in your project root with contents such as:
    
    
    .git
    dist
    node_modules
    vendor
    *.jar
    

Excluding compiled code and third-party dependencies also results in a more consistent build process and a reduced risk of accidental deployment of code that is still under active development.

## What's next

  * Learn how to [increase vCPU for builds](https://docs.cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
