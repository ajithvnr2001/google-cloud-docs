---
url: https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering/
title: Model and package units of deployment \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:47.310833+00:00
---

# Model and package units of deployment  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Model and package units of deployment Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to model and package units of deployment for an App offering. In App Lifecycle Manager, a unit of deployment is called a _unit kind_.

Create one unit kind for each component of the App offering that you want to manage independently. For more details, see [Determine the model of the App offering](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering#saas-model).

You can also create an App offering using a single unit kind for the entire App offering.

Unit kinds are defined in Application Design Center composite templates. Use App Design Center to model the unit kinds of your App offering using composite templates.

## Before you begin

  1. Ensure you have created an [App offering](https://docs.cloud.google.com/app-lifecycle-manager/create-saas-offering) for your SaaS application.
  2. Ensure you have the service accounts with the required permissions. For details, see [App Lifecycle Manager service accounts](https://docs.cloud.google.com/app-lifecycle-manager/overview#saas-service-accounts).
  3. For each App offering you create, ensure you have a composite template. For details, see the following section [Determine the model of the App offering](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering#saas-model).



## Determine the model of the App offering

To model the App offering, you need to determine how many unit kinds to create, and the relationship between these unit kinds.

For example, you might create two unit kinds: one unit kind for the infrastructure such as a VM, and one unit kind for the application deployed onto the infrastructure.

To decide how to model the App offering using unit kinds, consider the following:

  * Review the dependencies between components of the App offering. For example, if an App offering includes an application deployed onto a shared Kubernetes cluster, then consider using a unit kind to model this shared cluster.
  * Consider the release and maintenance cycle of the components of the App offering. If there are components that are managed together, such as the infrastructure, then consider modeling these components with one unit kind.



Once you have determined this model, you need to model each unit kind in your composite template for each unit kind.

## Create a unit kind

You can create a unit kind by using composite templates.

## Create a new composite template

You can manage unit kinds using App Design Center composite templates.

To create a new composite template using App Lifecycle Manager:

  1. In Google Cloud console, go to to **App Lifecycle Manager** > **App offerings**.

[Go to App offerings](https://console.cloud.google.com/saas/saasOfferings)

  2. Click **Create new template**.

  3. On the **Create a new composite template** page:

     1. In the **Template ID** box, enter an identifier for your template.

**Note:** **Template ID** must start with a lowercase letter followed by up to 30 lowercase letters, numbers, or hyphens, and cannot end with a hyphen.
     2. Optional: In the **Template name** box, enter a name for the template.

     3. Optional: In the **Description** box, enter a short description of the template.

     4. Click **Create template**. App Lifecycle Manager will take a few minutes create the template.

  4. When the template has been created successfully, you'll see your template's details in the **Connected application template** section of the **App offering details** page.

You've successfully created a composite template using App Lifecycle Manager.




## Populate unit kinds using an existing composite template

You can populate unit kinds by using App Design Center composite templates.

To populate unit kinds from an existing composite template: 

  1. In Google Cloud console, go to to **App Lifecycle Manager** > **App offerings**.

[Go to App offerings](https://console.cloud.google.com/saas/saasOfferings)

  2. Click **Connect existing template**.

  3. On the **Connect a composite application template** page, set up the template connection:

     1. In the **Space** drop-down, select the App Design Center space with your composite template.
     2. In the **Composite application template** drop-down, choose a composite template.
     3. In the **Revision** drop-down, choose the template revision you want to populate your App offering's unit kinds.
     4. Click **Connect**.
  4. App Lifecycle Manager will take a few minutes to import the composite template from App Design Center. Once App Lifecycle Manager imports the template correctly, the **Unit kinds** tab will be populated by the unit kinds defined in your composite template.

You've successfully populated your App offering's unit kinds using a composite template.




## What's next

  * After you have modeled the App offering, you can [deploy a unit instance](https://docs.cloud.google.com/app-lifecycle-manager/deploy-saas-offering).
  * To learn more about App Lifecycle Manager, see the [App Lifecycle Manager overview](https://docs.cloud.google.com/app-lifecycle-manager/overview).
  * For more details about the service accounts needed when using App Lifecycle Manager, see [service accounts](https://docs.cloud.google.com/app-lifecycle-manager/service-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
