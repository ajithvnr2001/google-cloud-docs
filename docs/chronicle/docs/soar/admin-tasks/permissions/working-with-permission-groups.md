---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups/
title: Permission groups overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:13.932191+00:00
---

# Permission groups overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Permission groups overview

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** If you've migrated to Google Cloud, this page is replaced by IAM permissions. For more information, see [Migrate to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp).

Google Security Operations lets you create groups of users and assign different permission levels to various modules.  
The platform includes seven predefined permission groups:

  * Readers
  * Admins
  * Basic
  * View-Only
  * Collaborators
  * Managed User
  * Managed-Plus User



The built-in administrator group automatically has edit access to all environments, letting its members view data from every environment in the system. When you create a new permission group, carefully consider whether to grant edit access to all environments.

## Edit a permission group

To edit an existing permission group, follow these steps:

  1. Go to **Settings > Organizations > Permissions**.
  2. Select the permission group you want to edit.
  3. Each module appears with a toggle to grant or deny a user access:
     * If the toggle is turned on, configure permissions for each feature you want to enable.
     * If the toggle is turned off, the module doesn't appear.
  4. When finished, click **Save**.



## Add a new permission group

To add a new permission group, follow these steps:

  1. Go to **Settings** > **Organizations** > **Permissions**.
  2. Click **Add Permission Group**.
  3. Complete the following areas on the screen: 
     1. Your cursor is automatically placed next to the title of New Group. Delete the words New Group and enter your own name for the new Group. For example, Tier One.
     2. From the list, select the License Type you want.  

     3. Select the Landing Page that you want this User Group to be directed to when they first sign in. 
     4. Select the permissions you want for each module.
  4. When finished, click **Save** ; the new permission group is added to the list. Note that at any time, you can make changes and click **Save** again. To simplify editing, click  content_copy **Duplicate** to create a copy of the permission group.  




## Restrict Actions

You can apply Restrict Actions to a permission group to prevent access to certain types of actions. For example, as a Managed Security Service Provider (MSSP), you might have separate SOC Manager groups for separate environments.

  1. In **Settings > Organizations > Permissions**, select the permission group to prevent access.
  2. In the **Restrict Actions** section, click add **Add** , and select the actions to restrict for this permission group.
  3. Click **Add** > **Save**.  




Learn how to [ control access to the platform](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/control-access-to-platform).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
