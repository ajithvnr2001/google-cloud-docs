---
url: https://docs.cloud.google.com/saas-runtime/docs/deploy-saas-offering/
title: Deploy an App offering \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:38:10.035753+00:00
---

# Deploy an App offering  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/saas-runtime/docs/deploy-saas-offering/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Deploy an App offering Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to deploy an App offering, which means that App Lifecycle Manager provisions the Google Cloud resources and deploys the SaaS application in the regions specified in the App offering resource.

To deploy the App offering, App Lifecycle Manager creates the unit by deploying the resources associated with a unit kind.

## Before you begin

Ensure you have created the following:

  1. An [App offering resource](https://docs.cloud.google.com/app-lifecycle-manager/create-saas-offering) for your SaaS application.
  2. Unit kinds to [model the App offering](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering).



### Deploy the App offering

To deploy the App offering, App Lifecycle Manager provisions the resources that are part of a unit kind. The term in App Lifecycle Manager for the provisioned resources or deployed application is a _unit_.

When you create a unit, App Lifecycle Manager provisions the resources defined in the unit kind. Units are provisioned in each region that is part of the App offering.

For example, if you had a unit kind for a single VM, then when you create a unit, App Lifecycle Manager provisions the VM in the regions defined in the App offering.

  1. Create a unit:

     1. In Google Cloud console, go to **App Lifecycle Manager** > **Units**.

[Go to Units](https://console.cloud.google.com/saas/units)

     2. Select **Create**.

     3. On the **Unit details** page:

        1. For **Unit name** , type a name for the unit. The name must contain only lowercase letters, numbers, or hyphens.

        2. Under **App offering** , select the App offering resource that you created earlier.

        3. Under **Region** , select the region where you want to deploy the resources or application.

        4. Under **Unit kind** , select the unit kind that defines the resources or application that you want to deploy.

        5. Under **Management mode** , select **User**.

           * **Unspecified** if you don't want to set a management mode.
           * **User** to have units deprovisioned manually. Units are not deprovisioned automatically by App Lifecycle Manager.
           * **System** to have App Lifecycle Manager deprovision dependent units when they are no longer needed.
        6. Optional: Add a label to the resources that you are deploying. For more details about labels, see the [Labels overview](https://docs.cloud.google.com/resource-manager/docs/labels-overview).

To add a label:

           1. Under **Labels** select **Add labels**.

           2. For **Key 1** and for **Value 1** , enter the key-value pair.

           3. Repeat steps 1 to 2 for each label that you want add.

        7. Select **Create**.

  2. To provision the resources or deploy the application:

     1. On the **Units** > **Create a unit** page, select **Provision**.

     2. For the release field, select the release for the versions of the unit kind you want to deploy.

     3. For the **Service account** , select the service account.

     4. Optional: Add a tenant project:

        1. Select **Add tenant project variables**.
        2. Define the input variables: 
           1. For **Name** , enter a string identifier for the variable.
           2. For **Variable type** , select the variable type.
           3. For **Variable value** type the variable value.
           4. Repeat these steps for each input variable.
     5. Select **Provision**.




## View the deployed unit

You have now used App Lifecycle Manager to create a unit, which deploys the resources or application in the associated unit kind.

To view the resources that you deployed:

  1. In console, go to the **App Lifecycle Manager** > **Units** > **Unit details** page.

[Go to Units](https://console.cloud.google.com/saas/units)

  2. Click the name of your unit.

  3. On the **Unit details** page:

     1. See that the **State** is **Ready** (or the state might be **Provisioning** while the operation is still in progress).
     2. Expand the **Variables** section.
     3. In the **Output variables** , you can see details related to any output variables specified in the unit kind. For more details about variables, see [Variables and variable mapping](https://docs.cloud.google.com/app-lifecycle-manager/variables).



## What's next

  * To learn more about App Lifecycle Manager, see the [App Lifecycle Manager overview](https://docs.cloud.google.com/app-lifecycle-manager/overview).
  * For more details about the service accounts needed when using App Lifecycle Manager, see [service accounts](https://docs.cloud.google.com/app-lifecycle-manager/service-accounts).
  * For the steps to update the release, see [Rollout a release](https://docs.cloud.google.com/app-lifecycle-manager/update-saas-offering).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
