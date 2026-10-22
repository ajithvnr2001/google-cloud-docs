---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/manage-data-agents/
title: Manage context sets in Firestore Studio \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:49.616037+00:00
---

# Manage context sets in Firestore Studio  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/manage-data-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Manage context sets in Firestore Studio Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create context sets in Firestore Studio using a context set file. Context set names must be unique within a database.

To learn about context sets, see [Context sets overview](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/context-sets-overview). 

## Before you begin

Complete the following prerequisites before creating an agent.

### Enable required services

Enable the following services for your project: 

  * [Data Analytics API with Gemini](https://console.cloud.google.com/apis/library/geminidataanalytics.googleapis.com)
  * [Gemini for Google Cloud API](https://console.cloud.google.com/apis/library/cloudaicompanion.googleapis.com)
  * [Knowledge Catalog API](https://console.cloud.google.com/apis/library/dataplex.googleapis.com)



### Prepare a Firestore database

Make sure that you have a Firestore Enterprise edition database with MongoDB compatibility.

If you're trying the examples on this page, we recommend that you create a new database for this purpose. For more information, see [Create and manage databases](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/create-databases).

### Required roles and permissions

  * Grant the `roles/datastore.viewer` and `roles/geminidataanalytics.queryDataUser` roles to the IAM user at the project level. For more information, see [Add IAM policy binding for a project](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding). 



## Create a context set

To create a context set, perform the following steps:

  1. In the Google Cloud console, go to the Firestore page.

[Go to Firestore](https://console.cloud.google.com/firestore)

  2. Select a database from the list. The database must be of the type **Firestore with MongoDB compatibility**.

  3. In the navigation menu, click **Firestore Studio**. 

  4. In the **Explorer pane** , next to **Context sets** , click **View actions**.

  5. Click **Create context set**.

  6. In **Context set name** , provide a unique context set name. The context set name is case-sensitive and can contain letters, numbers, hyphens, and underscores.

  7. Optional. In **Context set description** , add a description for your context set.

  8. Click **Create**.


**Note:** Creating the first context set in a project can take several minutes.

## Build context sets

After creating a context set, follow the steps in [Build context sets using the context engineering agent](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/build-context-sets) to create a context set file. You can then edit your context set to upload the context set file.

## Edit a context set

To edit a context set, perform the following steps:

  1. In the Google Cloud console, go to the Firestore page.

[Go to Firestore](https://console.cloud.google.com/firestore)

  2. Select the database from the list.

  3. In the navigation menu, click **Firestore Studio**. 

  4. In the **Explorer pane** , next to **Context sets** , click **View actions**.

  5. Click **Edit context set**.

  6. Optional. Edit **Context set description**.

  7. Click **Browse** in the **Upload context set file** section, and select the context set file.

  8. Click **Save**.




## Delete a context set

To delete a context set, perform the following steps:

  1. In the Google Cloud console, go to the Firestore page.

[Go to Firestore](https://console.cloud.google.com/firestore)

  2. Select the database from the list.

  3. In the navigation menu, click **Firestore Studio**. 

  4. In the **Explorer pane** , next to **Context sets** , click **View actions**.

  5. Click **Delete context set**.

  6. In the **Delete context set** confirmation dialog, enter the name of the context set.

  7. Click **Confirm** to delete the context set.


**Note:** Before you delete a database, you must delete all context sets associated with that database.

## What's next

  * Learn more about [context sets](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/context-sets-overview).
  * Learn how to [test a context set](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/inspect-data-agent).
  * Learn how to [build contexts using Gemini CLI](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/build-context-sets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
