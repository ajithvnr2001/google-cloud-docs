---
url: https://docs.cloud.google.com/app-hub/docs/create-reusable-template/
title: Create a reusable template from a running application \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:13.389015+00:00
---

# Create a reusable template from a running application  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/create-reusable-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Create a reusable template from a running application Stay organized with collections  Save and categorize content based on your preferences. 

When an App Hub application is already running successfully, you can create a reusable [template](https://docs.cloud.google.com/app-hub/docs/key-concepts#template) from it with [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview). This practice lets developer teams self-serve their deployments in a way that is consistent and compliant with your organization's standards.

This guide shows you how to standardize the architecture of an existing, registered application by creating a governed, reusable template.

This workflow is suitable for promoting [best practices](https://docs.cloud.google.com/app-hub/docs/best-practices) and supporting a consistent and secure deployment process. For example, use the architecture of a running `translator_v4.0` application to create a template for an upcoming `translator_v5.0` application.

## Before you begin

You must complete the following steps before creating templates from existing applications:

  * **For administrators** :

    1. [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub). Application Design Center requires a [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project).
    2. [Set up Application Design Center](https://docs.cloud.google.com/application-design-center/docs/setup). You must configure Application Design Center to let users create application templates.
    3. [Grant access to users](https://docs.cloud.google.com/resource-manager/docs/manage-applications#assign-roles). Assign appropriate IAM roles based on user's responsibilities in the application lifecycle.
  * **For developers and operators** :

    1. Confirm with your administrator that the initial setup is finalized.
    2. [Make sure you have the necessary IAM roles](https://docs.cloud.google.com/resource-manager/docs/manage-applications#assign-roles) for the tasks you want to perform.
    3. Open your [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) in the Google Cloud console.



## Identify and review the source application

Use App Hub to get a clear blueprint of the existing application's architecture:

  1. Navigate to the **Applications** page from App Hub:

[Go to Applications](https://console.cloud.google.com/apphub/applications)

  2. In the list of applications, find the running application you want to use as a source model. Then, click its name.

  3. In the application details page, review its registered services and workloads. This view serves as the source of truth for the application's architecture.




## Generate and parametrize the template

With the application blueprint from App Hub, build a flexible, reusable template in Application Design Center:

  1. [Design an application template](https://docs.cloud.google.com/application-design-center/docs/design-application-templates), mapping the inventory of services and workloads from your source application onto the [design canvas](https://docs.cloud.google.com/app-hub/docs/key-concepts#canvas).
  2. Identify any configuration values within the components that developers must customize for each deployment, such as region, machine sizes, or instance counts. Define these as input parameters in the template. This practice lets template users specify settings and maintain the core architecture.
  3. Add a detailed description, version number, and other relevant metadata to the template.



## Publish and validate the template

When you finish designing and parametrizing the template, publish it to a [catalog](https://docs.cloud.google.com/app-hub/docs/key-concepts#catalog) to make it available to other teams:

  1. [Verify your template](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#verify_your_template).
  2. [Share the template to a catalog](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#share-template-to-catalog).
  3. As a final validation, verify that the architecture of a test application matches the original source application.



Developers can now reuse the template for applications that are consistent and compliant with your organization's standards.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
