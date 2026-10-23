---
url: https://docs.cloud.google.com/resource-manager/docs/delete-standalone-org/
title: Delete, restore, and rename standalone organizations \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:04.390299+00:00
---

# Delete, restore, and rename standalone organizations  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/delete-standalone-org/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Delete, restore, and rename standalone organizations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage the lifecycle of a standalone organization.

## Delete a standalone organization

To delete a standalone organization, you must be the Organization Owner. For information about this role, see [Organization Owner](https://docs.cloud.google.com/resource-manager/docs/standalone-organization-overview#organization-owner-responsibilities).

Before deleting the standalone organization, ensure the following:

  * Delete all projects and folders that you created under that organization. For more information, see [Shut down projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).
  * Remove any active resources, such as access tags, hierarchical firewall rules, or access policies.



The organization deletion process has two stages:

  * A 30-day soft-delete phase, during which you can recover your organization.
  * A purge phase, which occurs 30 days after soft delete. After this phase, the system permanently deletes your organization.



To delete your organization, follow these steps:

  1. In the Google Cloud console, go to the **Organization details** page.

[Go to Organization details](https://console.cloud.google.com/organizations/details)

  2. Click **Delete**.

  3. Enter the Organization ID in the confirmation dialog, and then click **Delete**. This process might take a few minutes. The system sends a confirmation email to all organization owners after the organization is deleted.




## Restore a deleted organization

You can restore an organization within 30 days of its deletion. You must have the Organization Administrator role to view organizations pending deletion.

To restore a deleted organization, follow these steps:

  1. In the Google Cloud console, go to the **My organizations** page.

[Go to My organizations](https://console.cloud.google.com/organizations/list)

  2. Select the organization that you want to restore.

  3. In the **Organization details** page, click **Restore**.

  4. In the confirmation dialog that appears, click **Restore**. Organization restoration might take a few minutes.




## Rename an organization

To rename an organization, follow these steps:

  1. In the Google Cloud console, go to the **Organization details** page.

[Go to Organization details](https://console.cloud.google.com/organizations/details)

  2. Click **Rename**.

  3. In the dialog, enter the new name for your organization. Ensure that the new organization name meets the following requirements:

     * Contains only letters, numbers, or hyphens.
     * Doesn't use a domain name. Domain names are reserved for Cloud Identity and Google Workspace organizations only.
     * Doesn't contain common words such as 'Google Cloud'.
  4. Click **Rename** to save your changes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
