---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/spanner/manage-data-agents/
title: Manage context sets in Spanner Studio \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:53:00.921589+00:00
---

# Manage context sets in Spanner Studio  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/spanner/manage-data-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Manage context sets in Spanner Studio Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/pJByTWfenZAWbaXo7). 

**PostgreSQL interface note:** The examples in this topic are intended for GoogleSQL-dialect databases. This feature doesn't support PostgreSQL interface. 

This document describes how to create context sets in Spanner Studio using a context set file. Context set names must be unique within a database.

To learn about context sets, see [Context sets overview](https://docs.cloud.google.com/gemini/data-agents/querydata/spanner/context-sets-overview). 

## Before you begin

Complete the following prerequisites before creating an agent.

### Enable required services

Enable the following services for your project: 

  * [Data Analytics API with Gemini](https://console.cloud.google.com/apis/library/geminidataanalytics.googleapis.com)
  * [Gemini for Google Cloud API](https://console.cloud.google.com/apis/library/cloudaicompanion.googleapis.com)
  * [Knowledge Catalog API](https://console.cloud.google.com/apis/library/dataplex.googleapis.com)



### Prepare a Spanner instance

  * Make sure that a Spanner instance is available. For more information, see [Create an instance](https://docs.cloud.google.com/spanner/docs/create-manage-instances).
  * Ensure that you create a database in your instance where you will create the tables. For more information, see [Create a database on the Spanner instance](https://docs.cloud.google.com/spanner/docs/create-manage-databases#create-database)

  
This tutorial requires you to have a database in your Spanner instance. For more information, see [Create a database](https://docs.cloud.google.com/spanner/docs/create-manage-databases#create-database). 

### Required roles and permissions

  * Add an IAM user or service account to the cluster. For more information, see [Apply IAM roles](https://docs.cloud.google.com/spanner/docs/grant-permissions).
  * Grant the `spanner.databaseReader` and `geminidataanalytics.queryDataUser` roles to the IAM user at the project level. For more information, see [Add IAM policy binding for a project](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).
  * To create, upload, and manage context sets, grant the Dataplex Catalog Editor (`roles/dataplex.catalogEditor`) or Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`) role to the IAM user at the project level. For more information, see [Context sets permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions).
  * [Grant roles and permissions](https://docs.cloud.google.com/spanner/docs/grant-permissions#project-level_permissions) to the IAM user at the project-level for the required databases.



## Create a context set

To create a context set, perform the following steps:

  1. In the Google Cloud console, go to the Spanner page.

[Go to Spanner](https://console.cloud.google.com/spanner)

  2. Select an instance from the list, and then select a database.

  3. In the navigation menu, click **Spanner Studio**. 

  4. In the **Explorer pane** , next to **Context sets** , click **View actions**.

  5. Click **Create context set**.

  6. In **Context set name** , provide a unique context set name. The context set name is case-sensitive and can contain letters, numbers, hyphens, and underscores.

  7. Optional. In **Context set description** , add a description for your context set.

  8. Click **Create**.


**Note:** Creating the first context set in a project can take several minutes.

## Build context sets

After creating a context set, follow the steps in [Build contexts using Gemini CLI](https://docs.cloud.google.com/gemini/data-agents/querydata/spanner/build-context-sets) to create a context set file. You can then edit your context set to upload the context set file.

## Edit a context set

To edit a context set, perform the following steps:

  1. In the Google Cloud console, go to the Spanner page.

[Go to Spanner](https://console.cloud.google.com/spanner)

  2. Select an instance from the list, and then select a database.

  3. In the navigation menu, click **Spanner Studio**. 

  4. In the **Explorer pane** , next to **Context sets** , click **View actions**.

  5. Click **Edit context set**.

  6. Optional. Edit **Context set description**.

  7. Click **Browse** in the **Upload context set file** section, and select the context set file.

  8. Click **Save**.




## Delete a context set

To delete a context set, perform the following steps:

  1. In the Google Cloud console, go to the Spanner page.

[Go to Spanner](https://console.cloud.google.com/spanner)

  2. Select an instance from the list, and then select a database.

  3. In the navigation menu, click **Spanner Studio**. 

  4. In the **Explorer pane** , next to **Context sets** , click **View actions**.

  5. Click **Delete context set**.

  6. In the **Delete context set** confirmation dialog, enter the name of the context set.

  7. Click **Confirm** to delete the context set.


**Note:** Before you delete a database, you must delete all context sets associated with that database.

## What's next

  * Learn more about [context sets](https://docs.cloud.google.com/gemini/data-agents/querydata/spanner/context-sets-overview).
  * Learn how to [test a context set](https://docs.cloud.google.com/gemini/data-agents/querydata/spanner/inspect-data-agent).
  * Learn how to [build contexts using Gemini CLI](https://docs.cloud.google.com/gemini/data-agents/querydata/spanner/build-context-sets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
