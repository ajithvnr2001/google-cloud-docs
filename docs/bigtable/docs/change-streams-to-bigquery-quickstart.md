---
url: https://docs.cloud.google.com/bigtable/docs/change-streams-to-bigquery-quickstart/
title: Quickstart: Stream changes to BigQuery using a Dataflow template \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:15.454231+00:00
---

# Quickstart: Stream changes to BigQuery using a Dataflow template  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/change-streams-to-bigquery-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the Bigtable change stream to BigQuery template

In this quickstart, you learn how to set up a Bigtable table with a change stream enabled, run a change stream pipeline, make changes to your table, and then see the changes streamed.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Dataflow, Cloud Bigtable API, Cloud Bigtable Admin API, and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataflow.googleapis.com,bigtable.googleapis.com,bigtableadmin.googleapis.com,bigquery.googleapis.com)

  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)




## Create a BigQuery dataset

Use the Google Cloud console to create a dataset that stores the data.

  1. In the Google Cloud console, go to the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, click your project name.

  3. Expand the more_vert **Actions** option and click **Create dataset**.

  4. On the **Create dataset** page, do the following:

     1. For **Dataset ID** , enter `bigtable_bigquery_quickstart`.
     2. Leave the remaining default settings as they are, and click **Create dataset**.



## Create a table with a change stream enabled

  1. In the Google Cloud console, go to the Bigtable **Instances** page.

[Go to Instances](https://console.cloud.google.com/bigtable/instances)

  2. Click the ID of the instance that you are using for this quickstart.

If you don't have an instance available, [create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance) with the default configurations in a region near you.

  3. In the left navigation pane, click **Tables**.

  4. Click **Create a table**.

  5. Name the table `bigquery-changestream-quickstart`.

  6. Add a column family named `cf`.

  7. Select **Enable change stream**.

  8. Click **Create**.

  9. On the Bigtable **Tables** page, find your table `bigquery-changestream-quickstart`.

  10. In the **Change stream** column, click **Connect**.

  11. In the dialog, select **BigQuery**.

  12. Click **Create Dataflow job**.

  13. In the provided parameter fields, enter your parameter values. You don't need to provide any optional parameters.

     1. Set the Bigtable application profile ID to `default`.
     2. Set the BigQuery dataset to `bigtable_bigquery_quickstart`.
  14. Click **Run job**.

  15. Wait until the job status is **Starting** or **Running** before proceeding. It takes around 5 minutes once the job is queued.

  16. Keep the job open in a tab, so you can stop the job when cleaning up your resources.




## Write some data to Bigtable

  1. In the Cloud Shell, write a few rows to Bigtable so the change log can write some data to BigQuery. As long as you write the data after the job is created, the changes appear. You don't have to wait for the job status to become `running`.

**Note:** To install cbt CLI if not already installed, see [Install the cbt CLI](https://docs.cloud.google.com/bigtable/docs/cbt-overview#installing).
         
         cbt -instance=BIGTABLE_INSTANCE_ID -project=PROJECT_ID \
             set bigquery-changestream-quickstart user123 cf:col1=abc
         cbt -instance=BIGTABLE_INSTANCE_ID -project=PROJECT_ID \
             set bigquery-changestream-quickstart user546 cf:col1=def
         cbt -instance=BIGTABLE_INSTANCE_ID -project=PROJECT_ID \
             set bigquery-changestream-quickstart user789 cf:col1=ghi
         

Replace the following:

     * PROJECT_ID: the ID of the project that you are using
     * BIGTABLE_INSTANCE_ID: the ID of the instance that contains the `bigquery-changestream-quickstart` table



## View the change logs in BigQuery

  1. In the Google Cloud console, go to the **BigQuery** page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, expand your project and the dataset `bigtable_bigquery_quickstart`.

  3. Click the table `bigquery-changestream-quickstart_changelog`.

  4. To see the change log, click **Preview**.

![Change log preview in BigQuery](https://docs.cloud.google.com/bigtable/img/bigquery-change-log-quickstart.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Disable the change stream on the table:
         
         gcloud bigtable instances tables update bigquery-changestream-quickstart \
         --project=PROJECT_ID --instance=BIGTABLE_INSTANCE_ID \
         --clear-change-stream-retention-period
         

  2. Delete the table `bigquery-changestream-quickstart`:
         
         cbt --instance=BIGTABLE_INSTANCE_ID --project=PROJECT_ID deletetable bigquery-changestream-quickstart
         

  3. Stop the change stream pipeline:

     1. In the Google Cloud console, go to the Dataflow **Jobs** page.

[ Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

     2. Select your streaming job from the job list.

     3. In the navigation, click **Stop**.

     4. In the **Stop job** dialog, select **Cancel** , and then click **Stop job.**

  4. Delete the BigQuery dataset:

     1. In the Google Cloud console, go to the BigQuery page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery)

     2. In the **Explorer** panel, find the dataset `bigtable_bigquery_quickstart` and click it.

     3. Click **Delete** , type `delete`, and then click **Delete** to confirm.

  5. Optional: Delete the instance if you created a new one for this quickstart:
         
         cbt deleteinstance BIGTABLE_INSTANCE_ID
         




## What's next

  * [Learn how to write queries for the change log.](https://docs.cloud.google.com/bigtable/docs/query-change-log)
  * [Refer to the Bigtable change stream to BigQuery template reference page.](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-bigtable-change-streams-to-bigquery)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
