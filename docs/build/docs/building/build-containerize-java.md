---
url: https://docs.cloud.google.com/build/docs/building/build-containerize-java/
title: Build, test, and containerize Java applications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:54.232377+00:00
---

# Build, test, and containerize Java applications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/building/build-containerize-java/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Build, test, and containerize Java applications Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Cloud Build to build, test, and containerize Java-based applications, upload your container images to Artifact Registry, and generate build provenance.

## Before you begin

  * Be familiar with creating Java-based applications.
  * Have your Java project ready, including a `Dockerfile`.
  * Have a Docker repository in Artifact Registry, or [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  * Be familiar with [how to write a Cloud Build configuration file](https://docs.cloud.google.com/build/docs/build-config).
  * To run the `gcloud` commands in this page, install the [Google Cloud CLI](https://docs.cloud.google.com/sdk).



## Using the `maven` or `gradle` image

You can configure Cloud Build to build Java applications using the [`maven` image](https://hub.docker.com/_/maven) or the [`gradle` image](https://hub.docker.com/_/gradle) from Docker Hub.

###  maven 

To execute your tasks in the `maven` image, add a step to your build config with the following fields:

  * `name`: Set the value of this field to `maven` or `maven:<tag>`, where the tag represents the version. If you don't specify the image tag, Cloud Build uses the `latest` image by default.
  * `entrypoint`: Setting this field overrides the default entry point of the image referenced in `name`. Set the value of this field to `mvn` to invoke `mvn` as the entrypoint of the build step and run `mvn` commands.
  * `args`: The `args` field of a build step takes a list of arguments and passes them to the image referenced by the `name` field.



The following build step specifies the `entrypoint` for the `maven` image tagged as `3.3-jdk-8` and prints the build tool version:
    
    
    steps:
    - name: maven:3.3-jdk-8
      entrypoint: mvn
      args: ['--version']
    

###  gradle 

To execute your tasks in the `gradle` image, add a step to your build config with the following fields:

  * `name`: Set the value of this field to `gradle` or `gradle:<tag>`, where the tag represents the version. If you don't specify the image tag, Cloud Build uses the `latest` image by default.
  * `entrypoint`: Setting this field overrides the default entry point of the image referenced in `name`. Set the value of this field to `gradle` to invoke `gradle` as the entrypoint of the build step and run `gradle` commands.
  * `args`: The `args` field of a build step takes a list of arguments and passes them to the image referenced by the `name` field.



The following build step specifies the `entrypoint` for the `gradle` image tagged as `5.6.2-jdk8` and prints the build tool version:
    
    
    steps:
    - name: gradle:5.6.2-jdk8
      entrypoint: gradle
      args: ['--version']
    

## Configuring `Java` builds

  1. In your project root directory, create a build config file named `cloudbuild.yaml`.

  2. **Run tests** : `maven` and `gradle` provide `maven test` and `gradle test`, which downloads dependencies, builds the applications, and runs any tests specified in your source code. The `args` field of a build step takes a list of arguments and passes them to the image referenced by the `name` field.

In your build config file, add `test` to the `args` field to invoke `test` within `maven` and `gradle`:

###  maven 
         
         steps:
         - name: maven:3.3-jdk-8
           entrypoint: mvn
           args: ['test']
         

###  gradle 
         
         steps:
         - name: gradle:5.6.2-jdk8
           entrypoint: gradle
           args: ['test']
         

  3. **Package application** : To package your application into a JAR file for your `maven` image, specify the `package` command in the `args` field. The `package` command builds a JAR file in `/workspace/target/`.

To package your application into a JAR file for your `gradle` image, specify the `assemble` command in the `args` field. The `assemble` command builds a JAR file in `workspace/build/libs`.

The following build step packages your Java application:

###  maven 
         
         steps:
         - name: maven:3.3-jdk-8
           entrypoint: mvn
           args: ['package','-Dmaven.test.skip=true']
         

**Note:** The `package` command re-runs tests. Adding `-Dmaven.test.skip=true` to the `args` field will skip tests.

###  gradle 
         
         steps:
         - name: gradle:5.6.2-jdk8
           entrypoint: gradle
           args: ['assemble']
         

  4. **Containerize application** : Cloud Build provides a [prebuilt Docker image](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/docker) that you can use to containerize your Java application. To containerize your Java application, in your build config file:

     * Add a `name` field and specify the prebuilt Docker image at `gcr.io/cloud-builders/docker`.
     * Add an `args` field and specify the `build` arguments, including the name of the container image to build, and the path to your build artifact.
     * Add an `images` field to push the built container image to Artifact Registry.
     * Optional: Add [`requestedVerifyOption: VERIFIED`](https://docs.cloud.google.com/build/docs/build-config-file-schema#options) within the `options` field in your build config file to enable [Supply chain Levels for Software Artifacts (SLSA)](https://slsa.dev/) provenance generation.

**Note:** If you use a `docker push` build step to upload images to Artifact Registry rather than using the `images` field, then your build won't have provenance information.

The following build step containerizes your application, pushes your container image to Artifact Registry, and generates build provenance information:

###  maven 
    
    steps:
    - name: gcr.io/cloud-builders/docker
      args: ['build', '-t', 'location-docker.pkg.dev/project-id/repository/image', '--build-arg=JAR_FILE=target/build-artifact', '.']
    images: ['location-docker.pkg.dev/project-id/repository/image']
    

###  gradle 
    
    steps:
    - name: gcr.io/cloud-builders/docker
      args: ['build', '-t', 'location-docker.pkg.dev/project-id/repository/image', '--build-arg=JAR_FILE=build/libs/build-artifact', '.']
    images: ['location-docker.pkg.dev/project-id/repository/image']
    

Where:

     * location: the regional or multi-regional location for your repository.
     * project-id: the ID of your Google Cloud project.
     * repository: the name of your repository Artifact Registry.
     * image: the name of your container image.
     * build-artifact: the name of your JAR file created from your build step.
  5. **Start your build** : When you have your build config file ready, start your build by entering the following command in your terminal:
         
         gcloud builds submit --region=REGION --config config-file-path source-directory
         

Where:

     * config-file-path: the path to your build config file. In this example, the build config file is named `cloudbuild.yaml`.
     * source-directory: the path or URL to your source code.
     * `REGION`: one of the [supported build regions](https://docs.cloud.google.com/build/docs/locations).

If you don't specify a config-file-path and source-directory in the `gcloud builds submit` command, Cloud Build assumes that the config file and the source code are in the current working directory.

Once your build completes, you can [view repository details](https://docs.cloud.google.com/artifact-registry/docs/repositories/list-repos) in Artifact Registry.

You can also [view build provenance metadata](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance#view) and [validate provenance](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance#validate_provenance).




## Code examples

Here are some example repositories you can use to build Java apps, each of which contain a sample application and a build config file to build and test that application:

  * [maven-example](https://github.com/GoogleCloudPlatform/cloud-build-samples/tree/main/maven-example): A Java app and an example build config file to build and test the app with `mvn`.
  * [gradle-example](https://github.com/GoogleCloudPlatform/cloud-build-samples/tree/main/gradle-example): A Java app and an example build config file to build and test the app with `gradle`.



## What's next

  * Learn how to [view build results](https://docs.cloud.google.com/build/docs/view-build-results).
  * Learn how to [safeguard builds](https://docs.cloud.google.com/software-supply-chain-security/docs/safeguard-builds).
  * Learn how to [build standalone Java applications](https://docs.cloud.google.com/build/docs/building/build-java).
  * Learn how to [deploy an application on Cloud Run](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run).
  * Learn how to [deploy an application on GKE](https://docs.cloud.google.com/build/docs/building/build/docs/deploying-builds/deploy-gke).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
