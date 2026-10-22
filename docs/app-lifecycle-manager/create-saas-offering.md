---
url: https://docs.cloud.google.com/app-lifecycle-manager/create-saas-offering/
title: Create an App offering \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:29.786866+00:00
---

# Create an App offering  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/create-saas-offering/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Create an App offering Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to create an App offering, which lets you deploy and manage the infrastructure and application that are needed for a SaaS application.

After creating an App offering, you then model and package the deployable units, and then you provision and deploy these units.

## Before you begin

  1. Ensure you have [Enabled App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/enable-service).
  2. Identify the resources and SaaS application to deploy. For more details about the required artifacts, see [Blueprints in App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/artifacts).
  3. Ensure you set up the required [service accounts](https://docs.cloud.google.com/app-lifecycle-manager/overview#saas-service-accounts).



## Create an App offering

###  Console 

  1. In the console, go to **App Lifecycle Manager** > **App offering**.

[Go to App offering](https://console.cloud.google.com/saas/saasOfferings)

  2. Click **Create**.

  3. In the **Name of the App offering** field, type a name for the App offering.

  4. In the **Region** field:

     1. Select all of the regions where you want to host the deployments of your App offering. See [locations](https://docs.cloud.google.com/app-lifecycle-manager/locations) for the full list of available regions.
     2. Click **Ok**.
  5. Optional: In **Labels** , you can add labels to the App offering resource. For more details about labels, see the [Labels overview](https://docs.cloud.google.com/resource-manager/docs/labels-overview).

To add a label:

     1. Under **Labels** select **Add labels**.

     2. For **Key 1** and for **Value 1** , enter the chosen key-value pair.

     3. Repeat the steps for each label that you want to add.

  6. Click **Create** to create the App offering.




The regions that you selected for the App offering are where App Lifecycle Manager deploys the App offering, meaning that this is where the resources are provisioned and the application is deployed.

If you have end-users accessing the deployed App offering, they access it from the regions you specify here.

###  gcloud 
    
    
    gcloud beta app-lifecycle-manager saas create SAAS_OFFERING_NAME --location=global --locations=name=REGION_1 --locations=name=REGION_2
    

Replace the following:

  * SAAS_OFFERING_NAME: a name for the App offering.
  * REGION_1: a region where you want to host the deployments of the App offering. For available regions, see [App Lifecycle Manager locations](https://docs.cloud.google.com/app-lifecycle-manager/locations).
  * REGION_2: optionally, a second region to host the deployments. If you want to host the deployments in more than one region, follow this pattern to add each region to the command.



The regions that you selected for the App offering are where App Lifecycle Manager deploys the App offering, meaning that this is where the resources are provisioned and the application is deployed.

If you have end-users accessing the deployed App offering, they access it from the regions you specify here.

## What's next

  * Next you need to [model and package units of deployment](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering).
  * After you have modeled the units of deployment, you can [deploy a unit](https://docs.cloud.google.com/app-lifecycle-manager/deploy-saas-offering).
  * To learn more about App Lifecycle Manager, see the [App Lifecycle Manager overview](https://docs.cloud.google.com/app-lifecycle-manager/overview).
  * For more details about the service accounts needed when using App Lifecycle Manager, see [service accounts](https://docs.cloud.google.com/app-lifecycle-manager/overview#saas-service-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
