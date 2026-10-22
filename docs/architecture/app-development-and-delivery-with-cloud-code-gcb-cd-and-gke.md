---
url: https://docs.cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke/
title: CI/CD pipeline for developing and delivering containerized apps \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:13.526892+00:00
---

# CI/CD pipeline for developing and delivering containerized apps  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  CI/CD pipeline for developing and delivering containerized apps Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2022-11-18 UTC

This document describes an integrated set of Google Cloud tools to set up a system for development, for continuous integration (CI), and for continuous delivery (CD) that you can use to develop and deploy applications to [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine). This reference architecture document is intended for both software developers and operators. It assumes that you're familiar with running `gcloud` commands on Google Cloud and with deploying application containers to GKE.

## Architecture

The following diagram shows the resources that are used in this architecture:

![Develop and deploy system with Cloud Code, Cloud Build, Artifact Registry, Cloud Deploy, and GKE](https://docs.cloud.google.com/static/architecture/images/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke.svg)

This architecture includes the following components:

  1. **Cloud Code** as a development workspace. As part of this workspace, you can see changes in the development cluster, which runs on [minikube](https://minikube.sigs.k8s.io/docs/). You run Cloud Code and the minikube cluster in [Cloud Shell](https://docs.cloud.google.com/shell). Cloud Shell is an online development environment accessible from your browser. It has compute resources, memory, an integrated development environment, (IDE), and it also has Cloud Code installed.
  2. **Cloud Build** to build and test the application—the "CI" part of the pipeline

This part of the pipeline includes the following actions:

     * Cloud Build monitors changes to the source repository, using a Cloud Build trigger.
     * When a change is committed into the main branch, the Cloud Build trigger does the following: 
       * Rebuilds the application container.
       * Places build artifacts in a Cloud Storage bucket.
       * Places the application container in Artifact Registry.
       * Runs tests on the container.
       * Calls Cloud Deploy to deploy the container to the staging environment. In this example, the staging environment is a Google Kubernetes Engine cluster.
     * If the build and tests are successful, you can then use Cloud Deploy to promote the container from staging to production.
  3. **Cloud Deploy** to manage the deployment—the "CD" part of the pipeline. In this part of the pipeline, Cloud Deploy does the following:

     * Registers a [delivery pipeline](https://docs.cloud.google.com/deploy/docs/terminology#delivery_pipeline) and [targets](https://docs.cloud.google.com/deploy/docs/terminology#target). The targets represent the staging and production clusters.
     * Creates a Cloud Storage bucket and stores the Skaffold rendering source and rendered manifests in that bucket.
     * Generates a new [release](https://docs.cloud.google.com/deploy/docs/terminology#release) for each source code change.
     * Deploys the application to the production environment. For this deployment to production, an operator (or other designated person) manually approves the deployment. In this architecture, the production environment is a Google Kubernetes Engine cluster.



In this architecture, configuration is shared among the development, staging, and production environments through [Skaffold](https://skaffold.dev/), a command-line tool that facilitates continuous development for Kubernetes-native applications.

Google Cloud stores the application's source code in GitHub.

This architecture uses Google Cloud products for most of the components of the system, with Skaffold enabling the integration of the system. Because Skaffold is open source, you can use these principles to create a similar system using a combination of Google Cloud, in-house, and third-party components. The modularity of this solution means that you can adopt it incrementally as part of your development and deployment pipeline.

## Use cases

The following are the key features of this integrated system:

  * **Develop and deploy faster**.

The development loop is efficient because you can validate changes in the developer workspace. Deployment is fast because the automated CI/CD system and increased parity across the environments allow you to detect more issues when you deploy changes to production.

  * **Benefit from increased parity** across development, staging, and production.

The components of this system use a common set of Google Cloud tools.

  * **Reuse configurations** across the different environments.

This reuse is done with [Skaffold](https://skaffold.dev/), which allows a common configuration format for the different environments. It also allows developers and operators to update and use the same configuration.

  * **Apply governance** early in the workflow.

This system applies validation tests for governance at production and in the CI system and development environment. Applying governance in the development environment allows problems to be found and fixed earlier.

  * Let **opinionated tooling** manage your software delivery.

Continuous delivery is fully managed, separating the stages of your CD pipeline from the details of rendering and deploying.




## Deployment

To deploy this architecture, see [Develop and deploy containerized apps using a CI/CD pipeline](https://docs.cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke/deployment).

## What's next

  * To learn how to deploy into a private GKE instance, see [Deploying to a private cluster on a Virtual Private Cloud network](https://docs.cloud.google.com/deploy/docs/execution-environment#deploying_to_a_private_cluster_on_a_network).
  * For information about how to implement, improve, and measure deployment automation, see [Deployment automation](https://dora.dev/devops-capabilities/technical/deployment-automation/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2022-11-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2022-11-18 UTC."],[],[]] 
