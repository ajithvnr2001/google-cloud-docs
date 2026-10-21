---
url: https://docs.cloud.google.com/build/docs/develop/
title: Developing for Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:03.196301+00:00
---

# Developing for Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/develop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Developing for Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Build enables you to continuously build and test your code and deploy it on any target. You can develop your application in the programming language of your choice and store the source code in any of the popular source code management systems such as GitHub. This page describes the things to know to get started in developing an application to use with Cloud Build.

## Supported programming language

Cloud Build allows you to write code in any programming language of your choice. For examples on building and testing applications, see [Building Java applications](https://docs.cloud.google.com/build/docs/building/build-java), [Building Go applications](https://docs.cloud.google.com/build/docs/building/build-go), [Building Python applications](https://docs.cloud.google.com/build/docs/building/build-python), and [Building Node.js applications](https://docs.cloud.google.com/build/docs/building/build-nodejs).

## Build configuration file

To build your application using Cloud Build, you must provide a build configuration file along with your application source code. The build config file contains instructions for Cloud Build to perform tasks based on your specifications. You can write the build config file in YAML or JSON. For information on the fields and schema of the build config file, see [Build config overview](https://docs.cloud.google.com/build/docs/build-config). For instructions on creating a simple build config file, see [Create a basic build config file](https://docs.cloud.google.com/build/docs/configuring-builds/create-basic-configuration).

## Supported source code repositories

Cloud Build integrates with a number of repositories such as GitHub, Bitbucket, and Gitlab. You can store your application source code in any of these repositories and use Cloud Build to automate building, testing, and deploying your code. For instructions on connecting to various repositories, see [Creating GitHub app triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-github-app-triggers), [Building hosted repos on Bitbucket server](https://docs.cloud.google.com/build/docs/automating-builds/build-hosted-repos-bitbucket-server), [Building hosted repos on Bitbucket Cloud](https://docs.cloud.google.com/build/docs/automating-builds/build-hosted-repos-bitbucket-cloud), and [Building hosted repos on Gitlab](https://docs.cloud.google.com/build/docs/automating-builds/build-hosted-repos-gitlab).

You can also [specify any Git repositories as dependencies](https://docs.cloud.google.com/build/docs/building/manage-dependencies) to your build, if those repositories are public or are [connected using Developer Connect](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo).

## Storing built artifacts

Artifact Registry is a Google Cloud service that enables you to centrally store artifacts and build dependencies. You can use [Artifact Registry in conjunction with Cloud Build](https://docs.cloud.google.com/artifact-registry/docs/configure-cloud-build) to store build artifacts. In addition to Artifact Registry, you can store artifacts in other storage systems such as [Cloud Storage](https://docs.cloud.google.com/build/docs/building/store-build-artifacts#store-artifact-storage) and [Docker](https://docs.cloud.google.com/build/docs/interacting-with-dockerhub-images#pushing_images_to_docker_hub).

## Supported deployment platforms

Cloud Build supports deployments to most popular deployment platforms. For instructions on deploying to specific platforms, see [Deploying on Cloud Run](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run), [Deploying on Google Kubernetes Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-gke), [Deploying on App Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-appengine), and [Deploying on Firebase](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-firebase).

## What's next

  * Once you have your source code and build config file, learn how to start a build using [CLI, API](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually), or [build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
