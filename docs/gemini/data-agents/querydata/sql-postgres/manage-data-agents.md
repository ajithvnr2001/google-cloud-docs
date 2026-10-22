---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/manage-data-agents/
title: Manage context sets in Cloud SQL Studio \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:16.260647+00:00
---

# Manage context sets in Cloud SQL Studio  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/manage-data-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Manage context sets in Cloud SQL Studio Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create context sets in Cloud SQL for PostgreSQL Studio using a context set file. Context set names must be unique within a database.

To learn about context sets, see [Context sets overview](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/context-sets-overview). 

## Before you begin

Complete the following prerequisites before creating an agent.

### Enable required services

Enable the following services for your project: 

  * [Data Analytics API with Gemini](https://console.cloud.google.com/apis/library/geminidataanalytics.googleapis.com)
  * [Gemini for Google Cloud API](https://console.cloud.google.com/apis/library/cloudaicompanion.googleapis.com)
  * [Knowledge Catalog API](https://console.cloud.google.com/apis/library/dataplex.googleapis.com)



### Prepare a Cloud SQL instance

Make sure that you have access to an existing Cloud SQL instance or create a new one. For more information, see [Create instances for Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/create-instance).  
  
This tutorial requires you to have a database in your Cloud SQL instance. For more information, see [Create a database on the Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases#create)

### Required roles and permissions

  * Add an IAM user or service account to the instance. For more information, see [Manage users with IAM database authentication for Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users).
  * Grant the `cloudsql.studioUser`, `cloudsql.instanceUser`, and `geminidataanalytics.queryDataUser` roles to the IAM user at the project level. For more information, see [Add IAM policy binding for a project](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).
  * To create, upload, and manage context sets, grant the Dataplex Catalog Editor (`roles/dataplex.catalogEditor`) or Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`) role to the IAM user at the project level. For more information, see [Context sets permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions).
  * You must also grant read-only database privileges to an IAM user or service account by logging in as a user with superuser privileges, such as the `postgres` user.   
  
`GRANT SELECT ON ALL TABLES IN SCHEMA public TO USER_NAME;`   
  
Replace USER_NAME with the email address for the user. You must use quotes around the email because it contains special characters (@ and .).  
  
For more information, see [Grant database privileges to an individual IAM user or service account](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#grant-db-privileges).



### Grant `executesql` permission to Cloud SQL instance

To grant the `executesql` permission to Cloud SQL instance and enable the Cloud SQL Data API, run the following command: 
    
    
    gcloud config set project PROJECT_ID
    gcloud components update
    gcloud beta sql instances patch INSTANCE_ID --data-api-access=ALLOW_DATA_API
    

Replace the following: 

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `INSTANCE_ID`: The ID of your Cloud SQL instance.

To perform steps in this tutorial, sign in to [Google Cloud](https://console.cloud.google.com/), and then authenticate to the database using IAM authentication. 

## Create a context set

To create a context set, perform the following steps:

  1. In the Google Cloud console, go to the Cloud SQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Cloud SQL Studio**. 

  4. Sign in to **Studio** using IAM authentication. 

  5. In the **Explorer pane** , next to **Context sets** , click **View actions**.

  6. Click **Create context set**.

  7. In **Context set name** , provide a unique context set name. The context set name is case-sensitive and can contain letters, numbers, hyphens, and underscores.

  8. Optional. In **Context set description** , add a description for your context set.

  9. Click **Create**.


**Note:** Creating the first context set in a project can take several minutes.

## Build context sets

After creating a context set, follow the steps in [Build contexts using Gemini CLI](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/build-context-sets) to create a context set file. You can then edit your context set to upload the context set file.

## Edit a context set

To edit a context set, perform the following steps:

  1. In the Google Cloud console, go to the Cloud SQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Cloud SQL Studio**. 

  4. Sign in to **Studio** using IAM authentication. 

  5. In the **Explorer pane** , next to **Context sets** , click **View actions**.

  6. Click **Edit context set**.

  7. Optional. Edit **Context set description**.

  8. Click **Browse** in the **Upload context set file** section, and select the context set file.

  9. Click **Save**.




## Delete a context set

To delete a context set, perform the following steps:

  1. In the Google Cloud console, go to the Cloud SQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Cloud SQL Studio**. 

  4. Sign in to **Studio** using IAM authentication. 

  5. In the **Explorer pane** , next to **Context sets** , click **View actions**.

  6. Click **Delete context set**.

  7. In the **Delete context set** confirmation dialog, enter the name of the context set.

  8. Click **Confirm** to delete the context set.


**Note:** Before you delete a database, you must delete all context sets associated with that database.

## What's next

  * Learn more about [context sets](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/context-sets-overview).
  * Learn how to [test a context set](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent).
  * Learn how to [build contexts using Gemini CLI](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/build-context-sets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
