---
url: https://docs.cloud.google.com/build/docs/configuring-builds/use-community-and-custom-builders/
title: Using community-contributed builders and custom builders \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:02.521334+00:00
---

# Using community-contributed builders and custom builders  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/configuring-builds/use-community-and-custom-builders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Using community-contributed builders and custom builders Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use [community-contributed builders](https://github.com/GoogleCloudPlatform/cloud-builders-community) and custom builders in Cloud Build. The Cloud Build developer community provides [open-source builders](https://github.com/GoogleCloudPlatform/cloud-builders-community) that you can use to execute your tasks. If the task you want to perform requires capabilities that are not provided by an existing image, you can build your own custom image and use it in a build step. To learn about the different types of builders, see [Cloud Builders](https://docs.cloud.google.com/build/docs/cloud-builders).

If you're new to Cloud Build, read the [quickstarts](https://docs.cloud.google.com/build/docs/quickstarts) and the [Build configuration overview](https://docs.cloud.google.com/build/docs/build-config) first.

## Using community-contributed builders

Prebuilt images are not available for community-contributed builders; to use these builders in a Cloud Build config file, you must first build the image and push it to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) in your project.

To use a community-contributed builder:

  1. Build and push the builder:

     1. Navigate to your project root directory.

     2. Clone the [cloud-builders-community](https://github.com/GoogleCloudPlatform/cloud-builders-community) repository:
            
            git clone https://github.com/GoogleCloudPlatform/cloud-builders-community.git
            

     3. Navigate to the builder image you want to use, where builder-name is the directory that contains the builder:
            
            cd cloud-builders-community/builder-name
            

     4. Submit the builder to your project:
            
            gcloud builds submit .
            

     5. Navigate back to your project root directory:
            
            cd ../..
            

     6. Remove the repository from your root directory:
            
            rm -rf cloud-builders-community/
            

  2. In your Cloud Build config file, use the builder in a build step:

###  YAML 
         
         steps:
         - name: 'gcr.io/project-id/builder-name'
           args: ['arg1', 'arg2', ...]
         ...
         

###  JSON 
         
         {
           "steps": [
           {
             "name": "gcr.io/project-id/builder-name",
             "args": [
               "arg1",
               "arg2",
               ...
             ]
             ...
           }
           ]
         }
         

  3. Use the build config file to start the [build manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or [build using triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).




For examples on using community-contributed builders, see [Deploy to Firebase](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-firebase) and [Build VM images using Packer](https://docs.cloud.google.com/build/docs/building/build-vm-images-with-packer).

## Creating a custom builder

If the task you want to perform requires capabilities that are not provided by [a public image, a supported builder, or a community-contributed builder](https://docs.cloud.google.com/build/docs/cloud-builders), you can build your own image and use it in a build step.

Some examples of when you might want to use a custom builder image are:

  * Downloading source code or packages from external locations.
  * Using an external tool chain.
  * Caching any necessary libraries.
  * Pre-building source (with Cloud Build responsible only for potentially packaging the build into an image).



Like any other builder, a custom builder runs with the source mounted under `/workspace`, and is run with a working directory in `/workspace`. Any files left in `/workspace` by a given build step are available to other build steps.

Your custom builder can push to or pull from a repository in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) (hosted at `gcr.io/$PROJECT-NAME/`) to which your [build service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) has access.

The following steps show how to create and use a custom builder with an example `Dockerfile`:

  1. Create a custom builder image:

     1. Create the `Dockerfile` for the custom builder. The following code shows an example `Dockerfile`:
            
            FROM alpine
              RUN apk add curl
              CMD curl https://httpbin.org/ip -s > myip.txt; echo "*** My IP is: $(cat myip.txt)"
            

     2. Build and push the custom builder to the Artifact Registry in your project, replacing values for project-id and image-name:
            
            gcloud builds submit --tag gcr.io/project-id/image-name
            

  2. Use the custom builder image in Cloud Build by specifying the builder in the `name` field of a build step:

###  YAML 
         
         steps:
             - name: 'gcr.io/project-id/image-name'
               id: Determine IP of this build worker
         

###  JSON 
         
         {
               "steps": [
               {
                 "name": "gcr.io/project-id/image-name",
                 "id": "Determine IP of this build worker"
               }
               ]
             }
         

  3. Use the build config file to start the [build manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or [build using triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).


**Note:** Users can specify a working directory using the `dir` field in a build config file. Because your custom builder's users may specify any `dir` value, the builder should avoid hard-coding `/workspace` if possible. Instead, use the current working directory and relative paths.

## What's next

  * Learn how to [run bash scripts in build steps](https://docs.cloud.google.com/build/docs/configuring-builds/run-bash-scripts).
  * Learn how to [configure build step order](https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order).
  * Learn how to [write a basic build config file](https://docs.cloud.google.com/build/docs/configuring-builds/create-basic-configuration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
