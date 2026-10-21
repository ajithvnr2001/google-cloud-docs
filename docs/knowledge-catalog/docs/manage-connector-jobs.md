---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-connector-jobs/
title: Manage connector jobs \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:28.766459+00:00
---

# Manage connector jobs  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-connector-jobs/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage connector jobs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you manage connector jobs that run scheduled and on-demand metadata imports to keep your catalog synchronized with external data sources. You can view job configurations, run history, and logs, update import settings, disable or enable scheduled runs, manually trigger job runs, and delete jobs.

For more information about how connectors work, see [About metadata connectors](https://docs.cloud.google.com/knowledge-catalog/docs/connectors).

## Before you begin

To manage connector jobs, you need the appropriate IAM roles. See [IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles) for details.

  * To view jobs and run history: 
    * [BigQuery User](https://docs.cloud.google.com/iam/docs/understanding-roles#bigquery.user) (`roles/bigquery.user`)
    * Dataplex Viewer (`roles/dataplex.viewer`)
  * To edit, delete, or manually trigger jobs: 
    * [BigQuery Admin](https://docs.cloud.google.com/iam/docs/understanding-roles#bigquery.admin) (`roles/bigquery.admin`)
    * Dataplex Administrator (`roles/dataplex.admin`) or Dataplex Editor (`roles/dataplex.editor`)



You need to [enable the BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/enable-transfer-service#enable-dts).

Additionally, you must grant the BigQuery Data Transfer Service service agent (`service-PROJECT_NUMBER@gcp-sa-bigquerydatatransfer.iam.gserviceaccount.com`) the `dataplex.entryGroups.import` permission or the [Dataplex Entry Group Importer (`roles/dataplex.entryGroupImporter`)](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryGroupImporter) role. This can be granted either at the project level or at the entry group level.

## View connector jobs

  1. In the Google Cloud console, go to the **Knowledge Catalog** page.

[Go to Knowledge Catalog](https://console.cloud.google.com/dataplex)

  2. In the navigation menu, in the **Manage** section, click **Connectors**. The **Connectors** page lists all metadata import jobs in your project.

  3. To view the details, run history, or configuration of a specific job, click its display name in the list.




## View job run history and logs

For any connector job, you can view the history of its runs, including successful and failed runs. Job runs older than 90 days are automatically deleted.

  1. On the **Connectors** page, click the display name of the job you want to view.
  2. Click the **Run history** tab. This tab displays recent job runs.
  3. To view logs for a specific run, find the run in the list and click **View details**.



## Logging and monitoring

Knowledge Catalog metadata connectors export logs and metrics to Cloud Monitoring and Cloud Logging that provide observability into your import configurations. You can use Monitoring to set up dashboards to monitor metadata import configurations, evaluate run performance, and view error messages to troubleshoot run failures. You can use Logging to view logs related to a run or a configuration.

## Update a connector job

You can modify the configuration of an existing job, including its schedule, destination entry group, notification settings, and the source objects to import.

  1. On the **Connectors** page, click the display name of the job you want to update.
  2. Click **Edit**.
  3. Modify the job configuration as needed.
  4. Click **Save**.



## Disable or enable a connector job

When you disable a job, its name is updated with a `disabled` status, and no new job runs are scheduled. Any runs already in progress are completed. Disabling a job does not remove metadata already imported into Knowledge Catalog.

  1. On the **Connectors** page, find the job you want to disable or enable.
  2. Click **Actions** , and then select **Disable** or **Enable**.



## Delete a connector job

When you delete a job, no new runs are scheduled, and any runs in progress are stopped. Deleting a job does not remove metadata already imported into Knowledge Catalog.

  1. On the **Connectors** page, find the job you want to delete.
  2. Click **Actions** , and then select **Delete**.
  3. To confirm, type `delete` and click **Delete**.



## Manually trigger a job

You can start a job run outside of its regular schedule. This is sometimes called a _backfill_.

  1. On the **Connectors** page, click the display name of the job you want to run.
  2. Click **Run transfer now** , and select **Run one time transfer**.

**Note:** Knowledge Catalog connector jobs only support full metadata overwrites for each run.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
