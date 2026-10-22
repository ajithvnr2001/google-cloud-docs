---
url: https://docs.cloud.google.com/code/docs/shell/skaffold-modules/
title: Skaffold modules in Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:43.319288+00:00
---

# Skaffold modules in Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/skaffold-modules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Skaffold modules in Cloud Code for Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Code for Cloud Shell uses `skaffold.yaml` configuration files to provide a seamless development experience for Kubernetes applications, automating many of the tasks involved in building and deploying Kubernetes applications. This lets Cloud Code handle the workflow for building, pushing, and deploying your application, and provides building blocks for creating CI/CD pipelines.

Projects usually start using a single `skaffold.yaml` configuration to describe how to build and deploy the application. As a project grows, it can be useful to break the application pipeline into separate parts.

Cloud Code supports defining multiple [configuration dependencies](https://skaffold.dev/docs/design/config/#configuration-dependencies), either placed together in the same `skaffold.yaml` file and separated using YAML document separators (`---`), or placed in separate `skaffold.yaml` files that are referenced from a higher-level `skaffold.yaml` file. A configuration can be made into a _module_ by giving it a name using the `.metadata.name` field.

Using modules allows you to develop and debug parts of the application independently. Dependencies can be defined between configuration files and to specific modules. For steps to use this feature, see [Developing portions of an application independently](https://docs.cloud.google.com/code/docs/vscode/config-dependencies). 

## Debugging applications with modules

You can iteratively develop and debug the entire application or a set of the defined modules. Cloud Code manages the module dependencies and their order of deployment.

## Getting started with a modules sample

To select modules for your application, see [Building select modules and their dependencies](https://docs.cloud.google.com/code/docs/shell/config-dependencies#build-modules).

If you haven't used modules and want to test the feature with a sample, see the [Guestbook sample](https://github.com/GoogleCloudPlatform/cloud-code-samples/tree/master/nodejs/nodejs-guestbook), which is modularized into `frontend` and `backend`.

For a large enterprise application sample, developed using various technologies and languages, and using modules, see the [Bank of Anthos sample](https://github.com/GoogleCloudPlatform/bank-of-anthos).

## Common use cases

This section outlines some common use case examples that demonstrate different scenarios of when and how you can use modules in your IDE.

![](https://docs.cloud.google.com/static/code/docs/intellij/images/skaffold-modules-customer-environment-diagram.png)

### Microservice development

You're a frontend developer mostly working on the `frontend` module. As a microservice, `frontend` doesn't have an explicit code or library dependency on the `backend` repo, but requires `backend` to be deployed and running in the cluster.

You use your project that contains a `frontend` module definition to deploy and debug from a Cloud Code IDE to a shared development cluster where the backend team also deploys their service. The DevOps team maintains this shared cluster.

You don't work with or debug `backend` code or update Kubernetes configs most of the time. Cloud Code builds and deploys other configurations that `frontend` requires. You configure Cloud Code deployment configuration to only iterate on the `frontend` module.

You can also deploy both the `frontend` and `backend` to a local cluster to get a faster iterative experience.

### Cross-boundary microservice development and debugging

When multiple microservices need to be debugged together, you could:

  * Open the parent directory where all sub-directories with modules source code are located relative to each other
  * Select the root `skaffold.yaml` file for deployment (configs)
  * Configure Cloud Code deployment configuration to only iterate on `frontend` and `backend` modules that are available locally (and their respective Kubernetes configuration module when there are changes there).



You could also have a separate root `skaffold.yaml` file for local development that includes a static data server.

### Smart module YAML editing

You're a DevOps engineer building a template repository for the team of microservice developers which uses modules. You want to ensure there are no errors in module definitions. You use Cloud Code IDEs to edit `skaffold.yaml` configuration files.

##  What's next 

  * [Developing portions of an application independently](https://docs.cloud.google.com/code/docs/shell/config-dependencies)
  * [Debugging a Kubernetes application](https://docs.cloud.google.com/code/docs/shell/debug)
  * [Running a Kubernetes application](https://docs.cloud.google.com/code/docs/shell/run-application)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
