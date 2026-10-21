---
url: https://docs.cloud.google.com/database-center/docs/set-up-database-center/
title: Set up Database Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:57.823954+00:00
---

# Set up Database Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/set-up-database-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)
  * [ Guides ](https://docs.cloud.google.com/database-center/docs/overview)



Send feedback 

#  Set up Database Center Stay organized with collections  Save and categorize content based on your preferences. 

You can grant Identity and Access Management (IAM) permissions for an entire Google Cloud project to a principal on the IAM page of the Google Cloud console. Principals are users, groups, domains, or service accounts. For more information on principals, see [Principals](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity). Adding permissions at the project level grants the IAM permissions to a principal for all the instances, clusters, or databases in the project.

To use Database Center, you need to grant specific IAM permissions to your principals. Permission levels determine the database resources that Database Center principals can view. Permissions can be granted at the organization, folder, or project level. To let principals access all database resources for your organization, we recommend that you grant organization-level permissions.

For more information about how IAM works at Google Cloud, see [IAM documentation](https://docs.cloud.google.com/iam/docs).

The following IAM roles are available for the Database Center:

  * `roles/databasecenter.viewer`: grants view access to all instances in the Google Cloud project for which Database Center is enabled.

  * (Optional) `roles/recommender.viewer`: grants view access to recommender-related health issues in the Google Cloud project for which Database Center is enabled.




Additional IAM privileges might be required for recommendations related to Gemini in Databases or Security Command Center. For more information, see Enable Gemini Cloud Assist or Enable Security Command Center.

## Grant IAM permissions

To use Database Center, you must be granted IAM permissions for Database Center. Use the following topics to make sure that you and your team have the correct IAM permissions.

### Verify that you can add permissions

Before you attempt to apply project-level permissions, check that you have sufficient permissions to apply roles to another account. You need either the `Owner` or `Admin` role for the project you're trying to grant permissions for.

To confirm your permissions, complete the following steps:

  1. Go to your project's **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **View by Principals** option.

  3. Find your account in the list. If your account is listed as **Owner** or **Admin** in the **Role** column, you have sufficient permissions.




If you don't have sufficient permissions at the project level, ask the project's owner to grant you additional permissions.

### Grant roles to new users

To grant a role to a user, complete the following steps:

  1. Go to your project's **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **View by Principals** option.

  3. Click **GRANT ACCESS**.

  4. In the **Grant access** window, complete the following:

     1. Confirm the **Resource** name.

     2. In the **Add principals** section, add the new principal that you'd like to grant permissions to in the **New principals** field. You can add one principal or multiple principals.

     3. In the **Assign roles** section, select the role you want to grant to the new principal(s) from the drop-down.

To grant additional roles, click **ADD ANOTHER ROLE**.

     4. Click **Save** to grant roles to your selected principals.




### Modify roles of existing principals

To add or remove roles to an existing principal in your project, complete the following steps:

  1. Go to your project's **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **View by Principals** option.

  3. Find the principal you want to update in the list and click **Edit**.

  4. In the **Edit access** window, you can either add new roles or delete existing roles.

To add a new role, click **Add another role** , then select the role from the drop-down.

To delete an existing role, press **Delete** next to the role you want to delete.

  5. Click **Save** to update roles.




### Remove access for existing principals

To remove access for an existing principal, complete the following steps:

  1. Go to your project's **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **View by Principals** option.

  3. Find the principal you want to remove in the list and select the checkbox next to the name. To remove access for multiple principals, select the checkboxes for all principals you want to remove.

  4. Click **REMOVE ACCESS**.

  5. In the **Remove principal** window, click **Confirm** to remove access for the selected principals.




## Enable Gemini Cloud Assist

You can use Gemini Cloud Assist to track health issues in Database Center, and [Gemini Cloud Assist chat](https://docs.cloud.google.com/database-center/docs/learn-database-products-using-gemini#use-gemini-learn-database-fleet-health-issues) to learn more about your database fleet and inventory. You can access Gemini Cloud Assist chat at the Google Cloud project level and the folder level.

To learn about data privacy in Gemini Cloud Assist, see [How Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance). The [`roles/databasecenter.viewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/databasecenter#databasecenter.viewer) IAM role grants access to the metadata of a managed database but not to its data.

To enable Gemini Cloud Assist, complete all the steps in the [Before you begin using Gemini Cloud Assist](https://docs.cloud.google.com/database-center/docs/learn-database-products-using-gemini#before-you-begin).

## Enable Security Command Center

To track security-related health issues in Database Center, you need to activate Security Command Center (SCC). Security Command Center offers _Built-in_ and _Premium_ tiers. To gain access to basic security issues, enable Security Command Center _Built-in_. To gain access to all health issues supported by Security Command Center, enable Security Command Center _Premium_.

For more information about Security Command Center tiers and pricing, see [Security Command Center pricing](https://cloud.google.com/security-command-center/pricing).

For more information about the security issues supported in Database Center, see [Security issues supported by Security Command Center pricing tiers](https://docs.cloud.google.com/database-center/docs/database-health-issues#supported-security-issues).

Once you have selected your preferred tier, [Activate Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview) to use with Database Center.

## What's next

  * [Customize your database fleet health view](https://docs.cloud.google.com/database-center/docs/customize-database-fleet-view).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
