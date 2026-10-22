---
url: https://docs.cloud.google.com/policy-intelligence/docs/export-role-recommendations-data/
title: Export data for role recommendations \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:00.013337+00:00
---

# Export data for role recommendations  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/export-role-recommendations-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Export data for role recommendations Stay organized with collections  Save and categorize content based on your preferences. 

The [IAM role recommender](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview) uses aggregated IAM access data, collected during the usage of services in Google Cloud, to provide recommendations. This data is primarily used for compliance purposes.

This page explains how to export that access data to BigQuery using the [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery-transfer/docs/introduction).

If you want to export a snapshot of your insights and recommendations, see [Export recommendations to BigQuery](https://docs.cloud.google.com/policy-intelligence/docs/export-recommendations).

## Before you begin

  * Enable the IAM, Resource Manager, Recommender, BigQuery, BigQuery Data Transfer Service, and Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,cloudresourcemanager.googleapis.com,recommender.googleapis.com,bigquery.googleapis.com,bigquerydatatransfer.googleapis.com,pubsub.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Read about [role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview).




### Required permissions

To get the permissions that you need to create a data transfer, ask your administrator to grant you the following IAM roles: 

  * [Data Processing Controls Resource Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocessing#dataprocessing.admin) (`roles/dataprocessing.admin`) on your organization
  * [BigQuery Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`) on the project that you will export data to
  * To publish notifications for your transfer to an existing Pub/Sub topic: [Pub/Sub Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.viewer) (`roles/pubsub.viewer`) on the project that you will export data to 
  * To publish notifications for your topic to a new Pub/Sub topic: [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) on the project that you will export data to 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Export aggregated IAM access data

To export your projects' aggregated IAM access history to BigQuery, use the Transparency and Control Center to set up a data transfer:

  1. In the Google Cloud console, go to the **Privacy & Security** page.

[Go to Privacy & Security](https://console.cloud.google.com/projectselector/iam-admin/privacy?supportedpurview=organizationId)

  2. Select your organization from the drop-down list, then click **Select**.

  3. Click **Transparency & control**.

  4. In the **Data processing group** table, click **IAM**.

  5. In the **Data sources** section of the page, click add **Create transfer**.

  6. In the **Project** field, click **Browse** , then select the project that you want to export data to. If the project does not have the BigQuery Data Transfer Service API enabled, click **Enable API** and wait until the API is enabled.

  7. Click **Next**.

  8. Configure the data transfer:

     1. In the **Display name** field, enter a display name for your data transfer.
     2. In **Schedule options** section, choose when the data transfer will start and how often it will run.

        * To choose when to start the transfer, you can leave the default value of **Start now** , or click **Start at a set time**.
        * In the **Repeats** field, choose an option for how often to run the transfer. If you choose an option other than Daily, additional options are available. For example, if you choose **Weekly** , an option appears for you to select the day of the week.
        * For **Start date and run time** , enter the date and time to start the transfer. If you choose **Start now** , this option is disabled.
     3. In the **Dataset ID** field, choose a BigQuery dataset to export the data to.

**Important:** This dataset must have a location of **United States (US)** or **European Union (EU)**. No other regions are supported.

You can export data to an existing dataset, or create a new dataset:

        * To export data to an existing dataset, click the **Dataset ID** field, then select a dataset from the drop-down list.
        * To export data to a new dataset, click the **Dataset ID** field, click **Create new dataset** , and fill out the fields in the **Create dataset** pane:

          1. In the **Dataset ID** field, enter an ID for the dataset. Letters, numbers, and underscores are allowed.
          2. From the **Data location** drop-down list, select either **United States (US)** or **European Union (EU)**.
          3. Optional: Enable [table expiration](https://docs.cloud.google.com/bigquery/docs/managing-tables#updating_a_tables_expiration_time) by selecting **Enable table expiration**.
          4. Optional: Select an encryption method. The default encryption method is **Google-managed encryption key**. If you select **Customer-managed encryption key (CMEK)** , you must also select a [customer-managed key](https://docs.cloud.google.com/kms/docs/cmek).

The transfer you set up will be in the same region as the dataset, and cannot be moved.

     4. In the **project_numbers** field, enter the project numbers for the projects whose aggregated IAM access data you want to export. If you list multiple project numbers, separate the project numbers with commas. You can export data for up to 10 projects at a time.

To find a project's number, do the following:

        1. In the Google Cloud console, go to the **Settings** page.

[Go to Settings](https://console.cloud.google.com/projectselector/iam-admin/settings?supportedpurview=project)

        2. Select your project.

        3. Copy the project ID from the **Project number** field.

     5. Optional: Enable notifications for your transfer:

        * To enable notifications for failed transfer runs, click the **Email notifications** toggle. When you enable this option, the transfer administrator receives an email notification when a transfer run fails.
        * To enable [Pub/Sub notifications for your transfer](https://docs.cloud.google.com/bigquery-transfer/docs/transfer-run-notifications), click **Select a Pub/Sub topic** , then select or create a topic.
  9. Click **Done**.

  10. If prompted, allow **IAM Recommender Aggregated Access Transfers** access to your Google account.




## Manage existing data transfers

You can view and manage your transfers in the Transparency and Control Center, or in BigQuery:

  * To view all aggregated IAM access data transfers for your organization, use the Transparency and Control Center:

    1. In the Google Cloud console, go to the **Privacy & Security** page.

[Go to Privacy & Security](https://console.cloud.google.com/projectselector/iam-admin/privacy?supportedpurview=organizationId)

    2. Select your organization from the drop-down list, then click **Select**.

    3. Click **Transparency & control**.

    4. In the **Data processing group** table, click **IAM**. The **Data transfers** section of the page lists all aggregated IAM access data transfers for your organization.

    5. To manage an individual transfer, click the transfer's display name.

  * To view all data transfers in a project, including aggregated IAM access data transfers, use BigQuery:

    1. In the Google Cloud console, go to the **Data transfers** page.

[Go to Data transfers](https://console.cloud.google.com/projectselector/bigquery/transfers?supportedpurview=project)

    2. Select the project that you exported data to.

    3. The **Data transfers** page shows all data transfers for your project, including aggregated IAM access data transfers.

    4. To manage an individual transfer, click the transfer's display name.




## What's next

  * Learn how to [export a snapshot of your recommendations and insights](https://docs.cloud.google.com/policy-intelligence/docs/export-recommendations).
  * Understand [best practices for using role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-best-practices).
  * Find out how to [review and apply recommendations](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations).
  * Learn how to [disable role recommendations](https://docs.cloud.google.com/recommender/docs/opting-out).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
