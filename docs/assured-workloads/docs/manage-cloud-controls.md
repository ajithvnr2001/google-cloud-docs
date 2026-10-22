---
url: https://docs.cloud.google.com/assured-workloads/docs/manage-cloud-controls/
title: Manage cloud controls in Assured Workloads and Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:08.471525+00:00
---

# Manage cloud controls in Assured Workloads and Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/manage-cloud-controls/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage cloud controls in Assured Workloads and Audit Manager

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

_Applicable only for[Assured Workloads frameworks](https://docs.cloud.google.com/assured-workloads/docs/frameworks-overview)_

Assured Workloads frameworks includes many built-in cloud controls that you can add to custom frameworks and deploy in your environment. If required, you can create and manage your own custom cloud controls and update built-in cloud controls.

## Before you begin

  * To get the permissions that you need to manage cloud controls frameworks, ask your administrator to grant you the following IAM roles on your folder or project: 

    * [Compliance Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.admin) (`roles/cloudsecuritycompliance.admin`)
    * To create or modify cloud controls that are based on organization policies, one of: 
      * [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`)
      * [Assured Workloads Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) (`roles/assuredworkloads.admin`)
      * [Assured Workloads Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.editor) (`roles/assuredworkloads.editor`)
    * To create or modify cloud controls that are based on project policies: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## View cloud controls

Complete the following steps to view built-in cloud controls and any custom cloud controls that you already created.

  1. In the Google Cloud console, go to the **Frameworks** page.

[Go to Frameworks](https://console.cloud.google.com/compliance/configure/frameworks)

  2. If prompted, select your organization.

  3. Click the **Cloud Controls** tab. The list of available cloud controls is shown.

The dashboard includes information about which frameworks include the cloud control and the number of resources (organization, folders, and projects) that the cloud control is applied to.

  4. To view details about a cloud control, click the control name.




## Create a custom cloud control

A custom cloud control applies to only one [resource type](https://docs.cloud.google.com/asset-inventory/docs/asset-types#resource-types). The only supported data type is Cloud Asset Inventory resources. Custom cloud controls don't support parameters.

  1. In the Google Cloud console, go to the **Frameworks** page.

[Go to Frameworks](https://console.cloud.google.com/compliance/configure/frameworks)

  2. If prompted, select your organization.

  3. Click the **Cloud Controls** tab. The list of available cloud controls is shown.

  4. Create a cloud control, either with Gemini or manually:




###  Use Gemini 

  1. Ask Gemini to generate a cloud control for you. Based on your prompt, Gemini provides a unique identifier, a name, associated detection logic, and possible remediation steps.

  2. Review the recommendations and make any required changes.

  3. Save your custom cloud control.




###  Create manually 

  1. In **Cloud control ID** , provide a unique identifier for your control.

  2. Enter a name and description to help users in your organization understand the purpose of the custom cloud control.

  3. Optional: Select the categories for the control. Click **Continue**.

  4. Select an available resource type for your custom cloud control. Assured Workloads frameworks support all resource types. To find the name for a resource, see [Asset types](https://docs.cloud.google.com/asset-inventory/docs/asset-types).

  5. Provide the detection logic for your cloud control, in Common Expression Language (CEL) format.

CEL expressions let you define how you want to evaluate the properties of a resource. For more information and examples, see [Write rules for custom cloud controls](https://docs.cloud.google.com/assured-workloads/docs/write-rules-cloud-controls). Click **Continue**.

If your evaluation rule isn't valid, an error is displayed.

  6. Select an appropriate findings severity.

  7. Write your remediation instructions so that incident responders and administrators in your organization can resolve any findings for the cloud control. Click **Continue**.

  8. Review your entries, and then click **Create**.




## Edit a custom cloud control

After you create a cloud control, you can change its name, description, rules, remediation steps, and severity level. You can't change the cloud control category.

  1. In the Google Cloud console, go to the **Frameworks** page.

[Go to Frameworks](https://console.cloud.google.com/compliance/configure/frameworks)

  2. If prompted, select your organization.

  3. Click the **Cloud Controls** tab. The list of available cloud controls is shown.

  4. Click the cloud control that you want to edit.

  5. In the **Cloud controls details** page, verify that the cloud control isn't included in a framework. If required, [edit the framework to remove the cloud control](https://docs.cloud.google.com/assured-workloads/docs/manage-frameworks#update-custom-framework).

  6. Click **Edit**.

  7. In the **Edit custom cloud control** page, change the name and description as required. Click **Continue**.

  8. Update the rules, finding severity, and remediation steps. Click **Continue**.

  9. Review your changes and click **Save**.




## Update a built-in cloud control to a newer release

Google publishes regular updates to its built-in cloud controls as services deploy new features or as new best practices emerge. Updates can include new controls or changes to existing controls.

You can view the releases of built-in cloud controls in the cloud controls dashboard in the **Configure** tab or in the cloud control details page.

Google notifies you in the release notes when the following items are updated:

  * Cloud control name
  * Finding category
  * Change in the detective or preventive logic in a rule
  * Underlying logic of a rule



To update a cloud control after you receive a notification, you must unassign and redeploy the frameworks that include the cloud control. For instructions, see [Update a framework to a newer release](https://docs.cloud.google.com/assured-workloads/docs/manage-frameworks#update-framework-version).

## Delete a custom cloud control

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Delete a cloud control when it's no longer required. You can only delete cloud controls that you create. You can't delete built-in cloud controls.

  1. In the Google Cloud console, go to the **Frameworks** page.

[Go to Frameworks](https://console.cloud.google.com/compliance/configure/frameworks)

  2. If prompted, select your organization.

  3. Click the **Cloud Controls** tab. The list of available cloud controls is shown.

  4. Click the cloud control that you want to delete.

  5. In the **Cloud controls details** page, verify that the cloud control isn't included in a framework. If required, [edit the framework to remove the cloud control](https://docs.cloud.google.com/assured-workloads/docs/manage-frameworks#update-custom-framework).

  6. Click **Delete**.

  7. In the **Delete** window, review the message. Type `Delete` and click **Confirm**.




## What's next

  * Learn more about [Assured Workloads frameworks](https://docs.cloud.google.com/assured-workloads/docs/configuration-overview).
  * Learn how to [manage frameworks](https://docs.cloud.google.com/assured-workloads/docs/manage-frameworks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
