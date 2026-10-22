---
url: https://docs.cloud.google.com/colab/docs/gemini-in-colab/turn-off-gemini/
title: Turn off Gemini in Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:28.951693+00:00
---

# Turn off Gemini in Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/gemini-in-colab/turn-off-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Turn off Gemini in Colab Enterprise

This document explains how to turn off Gemini in Colab Enterprise.

## Before you begin

  * To update a Gemini in Colab Enterprise subscription, make sure you have the `billing.subscriptions.update` Identity and Access Management (IAM) permission. The `billing.subscriptions.update` permission is included in the [`roles/billing.admin`](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin) IAM role, or you can add the permission to a custom role.



## Turn off Gemini in Colab Enterprise

To turn off Gemini in Colab Enterprise, you can remove access for specific users or turn off features within Colab Enterprise.

### Remove access for specific users

You can use the [Policy Analyzer feature](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#principal-query-all) in the Cloud Asset Inventory to find all users with any of the permissions included in the **Gemini for Google Cloud User** role and the **Service Usage Consumer** role. The most direct way to achieve this is to run a Policy Analyzer query that checks for the specific role itself, as the role implicitly contains the set of permissions.

  1. Use the Policy Analyzer to see which users have the **Gemini for Google Cloud User** role and the **Service Usage Consumer** role, or the individual equivalent permissions.

###  Query by roles 

     1. Go to the **Policy Analyzer** page.

[Go to Policy Analyzer](https://console.cloud.google.com/projectselector/iam-admin/analyzer?supportedpurview=)

     2. In the **Analyze policies** section, click **Create custom query**.

     3. In the **Select query scope field** , choose the Organization, Folder, or Project you want to analyze. This defines the resources (and their IAM policies) that will be checked.

     4. Set the parameter to **Role**.

        1. In the **Parameter 1** field, select **Role** from the drop-down menu.

        2. In the corresponding **Select a role** field, select or type the name of the role: **Gemini for Google Cloud User**. Note that the full role ID is `roles/cloudaicompanion.user`.

        3. In the **Parameter 2** field, select **Role** from the drop-down menu.

        4. In the corresponding **Select a role** field, select or type the name of the role: **Service Usage Consumer**. Note that the full role ID is `roles/serviceusage.serviceUsageConsumer`.

     5. Click **Analyze (or Run Query)**. The results table shows all principals (users, service accounts, groups) that have been granted the **Gemini for Google Cloud User** role and the **Service Usage Consumer** role on any resource within your defined scope, whether directly or inherited from a parent resource.

###  Query by permissions 

     1. Go to the **Policy Analyzer** page.

[Go to Policy Analyzer](https://console.cloud.google.com/projectselector/iam-admin/analyzer?supportedpurview=)

     2. In the **Analyze policies** section, click **Create custom query**.

     3. In the **Select query scope field** , choose the Organization, Folder, or Project you want to analyze. This defines the resources (and their IAM policies) that will be checked.

     4. Set the parameter to **Permission**.

        1. In the **Parameter 1** field, select **Permission** from the drop-down menu.

        2. In the corresponding field, enter `cloudaicompanion.companions.generateChat`.

        3. In the **Parameter 2** field, select **Permission** from the drop-down menu.

        4. In the corresponding field, enter `cloudaicompanion.companions.generateCode`.

     5. Click **Analyze (or Run Query)**. The results table will show all principals that have any of the listed permissions granted on resources within the scope, regardless of the role they were granted through (such as a predefined role, a custom role, or another predefined role that coincidentally includes those permissions).

  2. Remove all applicable user Identity and Access Management roles or permissions for Gemini in Colab Enterprise:

     1. Go to the **IAM & Admin** page.

[Go to IAM & Admin](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=)

     2. In the **Principal** column, find a principal for which you want to remove access to Gemini in Colab Enterprise, and then click edit **Edit principal** in that row.

     3. In the **Edit access** pane, do the following:

###  Remove predefined roles 

        1. Locate the **Gemini for Google Cloud User** role, and then click delete **Delete role**.

        2. Locate the **Service Usage Consumer** role, and then click delete **Delete role**.

###  Remove custom or alternate roles 

        1. Locate the roles that include the `cloudaicompanion.companions.generateChat` and `cloudaicompanion.companions.generateCode` permissions, and then click delete **Delete role**.

     4. Click **Save**.




### Turn off features within Colab Enterprise

You can also turn off Gemini features from the **Colab Enterprise Notebooks** page:

  1. In the Google Cloud console, go to the **Colab Enterprise Notebooks** page.

[Go to Colab Enterprise Notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. Open a notebook.

  3. In the **Colab Enterprise** toolbar, click pen_spark **Help me code**.

  4. Clear the Gemini features that you want to turn off.

  5. Optional: If you are disabling all Gemini for Google Cloud products, then turn off the Gemini for Google Cloud API.




## Optional: Turn off the Gemini for Google Cloud API

After you turn off all other Gemini for Google Cloud products for your project, turn off the Gemini for Google Cloud API (`cloudaicompanion.googleapis.com`). For more information, see [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
