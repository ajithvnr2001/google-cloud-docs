---
url: https://docs.cloud.google.com/app-lifecycle-manager/blueprints/
title: Blueprints in App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:17.770361+00:00
---

# Blueprints in App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/blueprints/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)



Send feedback 

#  Blueprints in App Lifecycle Manager Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To use App Lifecycle Manager, you need to use a Terraform configuration to define the SaaS application and infrastructure that you want to deploy. 

In App Lifecycle Manager, a **blueprint** is the term used for the packaged Terraform configuration that defines the infrastructure and application that you deploy. The packaged Terraform configurations are Open Container Initiative (OCI) images that are stored in Artifact Registry.

This page describes:

  * The requirements for the Terraform configurations when using App Lifecycle Manager.
  * How you can provide the Terraform configurations to App Lifecycle Manager.
  * How App Lifecycle Manager uses the Terraform configuration.



This page assumes that you are familiar with Terraform. To learn more about Terraform, start with [What is Terraform?](https://developer.hashicorp.com/terraform/intro).

For details about creating an OCI image using a Terraform configuration, See [Create and upload a blueprint](https://docs.cloud.google.com/app-lifecycle-manager/blueprints).

## Blueprint requirements

App Lifecycle Manager uses Infrastructure Manager to deploy the Terraform configurations onto Google Cloud. For details about requirements and constraints, see [Constraints on Terraform configurations](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#constraints).

To use the Terraform configuration, App Lifecycle Manager uses a package of the Terraform configuration. This package is an OCI (Open Container Initiative) image that is stored in Artifact Registry.

You can provide an OCI image that contains the Terraform configuration. Otherwise, you provide the Terraform configuration and App Lifecycle Manager creates the OCI image. For details about how you can provide the Terraform configuration, see the following section [How to provide a blueprint](https://docs.cloud.google.com/app-lifecycle-manager/blueprints#provide_blueprint).

## Terraform variables in blueprints

Your Terraform configurations can use variables to customize deployments. App Lifecycle Manager provides flexible ways to manage these variables, see [manage variables](https://docs.cloud.google.com/app-lifecycle-manager/variables).

## How to provide a blueprint

You can provide the blueprint as a Terraform configuration or an OCI image that packages the Terraform configuration.

You can provide a blueprint to App Lifecycle Manager in the following ways:

  * Terraform configuration stored in an external repository.
  * Terraform configuration stored in a zip archive.
  * Using the Terraform configuration and Cloud Build, build the OCI image yourself and push it to Artifact Registry.
  * Automate the build of the OCI image using the Terraform configuration and Cloud Build. This automated method is useful for CI/CD pipelines.



## How App Lifecycle Manager uses the blueprint

When you use App Lifecycle Manager, the blueprint is stored in Artifact Registry with the [Docker format](https://docs.cloud.google.com/artifact-registry/docs/supported-formats). The blueprint is deployed onto Google Cloud using Infrastructure Manager.

For details about the repository in Artifact Registry, see [Create a repository for App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/create-repository).

### Upload a blueprint

You can provide the blueprint as a Terraform configuration or an OCI image that packages the Terraform configuration.

You upload the blueprint to App Lifecycle Manager when you create a unit kind. You can select the blueprint in one the following ways:

  * Upload the Terraform configuration as a zip archive.
  * Link an external repository.
  * Select an existing image from Artifact Registry.



For more details, see [create a unit kind](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering#create_unit_kinds).

### Provision the blueprint

App Lifecycle Manager provisions the infrastructure described in the blueprint when it [creates a unit](https://docs.cloud.google.com/app-lifecycle-manager/deploy-saas-offering#deploy_the_saas_offering).

App Lifecycle Manager uses Infrastructure Manager to provision the infrastructure. Infrastructure Manager uses Cloud Build as part of its workflow. When App Lifecycle Manager creates a unit, information about the status of the deployment is available from all three services:

  * App Lifecycle Manager
  * Infrastructure Manager
  * Cloud Build



For more details about how Infrastructure Manager deploys Terraform configurations, see [Infrastructure Manager overview](https://docs.cloud.google.com/infrastructure-manager/docs/overview).

### Control versioning

App Lifecycle Manager controls versioning of the blueprint by versioning the OCI image with Artifact Registry, and by using a release in App Lifecycle Manager to point to a specific version of the blueprint in Artifact Registry.

## What's next

  * Try the [quickstart](https://docs.cloud.google.com/app-lifecycle-manager/quickstart) to get started using App Lifecycle Manager.
  * Create a registry in Artifact Registry to store blueprints for App Lifecycle Manager.

  * To learn more about App Lifecycle Manager, see [App Lifecycle Manager Overview](https://docs.cloud.google.com/app-lifecycle-manager/docs/overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
