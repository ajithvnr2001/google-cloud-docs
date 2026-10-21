---
url: https://docs.cloud.google.com/oracle/database/docs/iam-roles/
title: Apply IAM roles \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:26:10.757051+00:00
---

# Apply IAM roles  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/iam-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Apply IAM roles Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to grant Oracle Database@Google Cloud Identity and Access Management (IAM) permissions to a user or account.

You can grant IAM permissions for an entire Google Cloud project to a principal on the IAM page of the Google Cloud console. Principals are users, groups, domains, or service accounts. For more information on principals, see [Principals](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity). Adding permissions at the project level grants the IAM permissions to a principal for all the instances, clusters, or databases in the project.

For more information about how IAM works with Oracle Database@Google Cloud, see [IAM overview](https://docs.cloud.google.com/oracle/database/docs/iam-overview).

## Verify that you can add permissions

Before you attempt to apply project-level permissions, check that you have sufficient permissions to apply roles to another account. You need either the `Owner` or `Admin` role for the project you're trying to grant permissions for.

To confirm your permissions, complete the following steps:

  1. Go to your project's **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **View by Principals** option.

  3. Find your account in the list. If your account is listed as **Owner** or **Admin** in the **Role** column, you have sufficient permissions.




If you don't have sufficient permissions at the project level, ask the project's owner to grant you additional permissions.

## Grant roles to new principals

To grant a role to a principal, complete the following steps:

  1. Go to your project's **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **View by Principals** option.

  3. Click **GRANT ACCESS**.

  4. In the **Grant access** window, complete the following:

     1. Confirm the **Resource** name.

     2. In the **Add principals** section, add the new principal that you'd like to grant permissions to in the **New principals** field. You can add one principal or multiple principals.

     3. In the **Assign roles** section, select the role you want to grant to the new principal(s) from the drop-down. For more information on available roles, see [IAM overview](https://docs.cloud.google.com/oracle/database/docs/iam-overview).

To grant additional roles, click **ADD ANOTHER ROLE**.

     4. Click **Save** to grant roles to your selected principals.




## Modify roles of existing principals

To add or remove roles to an existing principal in your project, complete the following steps:

  1. Go to your project's **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **View by Principals** option.

  3. Find the principal you want to update in the list and click **Edit**.

  4. In the **Edit access** window, you can either add new roles or delete existing roles.

To add a new role, click **Add another role** , then select the role from the drop-down.

To delete an existing role, press **Delete** next to the role you want to delete.

  5. Click **Save** to update roles.




## Remove access for existing principals

To remove access for an existing principal, complete the following steps:

  1. Go to your project's **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **View by Principals** option.

  3. Find the principal you want to remove in the list and select the checkbox next to the name. To remove access for multiple principals, select the checkboxes for all principals you want to remove.

  4. Click **REMOVE ACCESS**.

  5. In the **Remove principal** window, click **Confirm** to remove access for the selected principals.




## What's next

  * Learn more about how IAM works in the [IAM overview](https://docs.cloud.google.com/oracle/database/docs/iam-overview).
  * [Learn more about Oracle Database@Google Cloud](https://docs.cloud.google.com/oracle/database/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
