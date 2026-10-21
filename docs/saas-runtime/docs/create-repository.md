---
url: https://docs.cloud.google.com/saas-runtime/docs/create-repository/
title: Create a repository for App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:09:07.301232+00:00
---

# Create a repository for App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/saas-runtime/docs/create-repository/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)



Send feedback 

#  Create a repository for App Lifecycle Manager Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To use App Lifecycle Manager, you need a repository in Artifact Registry to store the blueprint.

The blueprint defines the SaaS application and infrastructure that you deploy with App Lifecycle Manager. For more details about blueprints, see [Blueprints in App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/blueprints).

## Before you begin

Ensure you have [enabled App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/enable-service).

## Creating a repository

To create the repository, review the following details specific to App Lifecycle Manager. Then, follow the instructions to [create standard repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) in the Artifact Registry documentation.

### Details about repositories for App Lifecycle Manager

As you set up a repository in Artifact Registry, take into account the following details:

  * When you configure the repository details:

    * For **Format** , select **Docker**. Even though we're storing Terraform configurations, App Lifecycle Manager uses the OCI (Open Container Initiative) image format to package the Terraform configurations. OCI images are compatible with Docker tooling.
    * For **mode** , select standard.
    * For the region of the repository, you can choose any region that is supported by Artifact Registry. This region does not need to match the regions where App Lifecycle Manager provisions the SaaS application and infrastructure.

However, if you plan to use Cloud Build in the same Google Cloud project to build and push blueprints, it can be helpful to choose the same region for your Cloud Build jobs, Artifact Registry repository and Developer Connect.




## What's next

  * Try the [quickstart](https://docs.cloud.google.com/app-lifecycle-manager/quickstart) to get started using App Lifecycle Manager.
  * [Learn more about the blueprints](https://docs.cloud.google.com/app-lifecycle-manager/blueprints) that define the SaaS application and infrastructure.
  * To learn more about App Lifecycle Manager, see [App Lifecycle Manager Overview](https://docs.cloud.google.com/app-lifecycle-manager/app-lifecycle-manager/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
