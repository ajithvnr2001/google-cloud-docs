---
url: https://docs.cloud.google.com/datastream/docs/create-spanner-stream-automated/
title: Create a Spanner stream using the automated flow \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:04.431704+00:00
---

# Create a Spanner stream using the automated flow  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/create-spanner-stream-automated/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Create a Spanner stream using the automated flow Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a Spanner stream using the automated setup flow.

The automated stream setup simplifies the process of moving data from Spanner databases to destinations such as BigQuery by reducing the number of steps that you need to perform. The flow lets you create a stream directly from the overview page of your Spanner instance or database. Datastream automates securing the connection between the stream and the source database, creating database configurations and stream connection resources.

## Free Tier

Datastream lets you stream from Spanner to BigQuery using the Free Tier, providing up to 100 GiB of change data capture data free every month. For more information, see [Datastream pricing](https://docs.cloud.google.com/datastream/pricing).

## Before you begin

Before you configure a Datastream stream for Spanner, verify that your environment meets the following prerequisites:

  1. Enable the required APIs in your Google Cloud project: 
     * Datastream API (`datastream.googleapis.com`)
     * Cloud Spanner API (`spanner.googleapis.com`)
     * BigQuery API (`bigquery.googleapis.com`).
  2. Ensure that you have the required Identity and Access Management (IAM) permissions to create and manage Datastream resources. For more information, see Required permissions.
  3. Review Spanner source limitations:

     * `PROTO` and `ENUM` data type columns aren't supported.
     * Arrays of `DATE` or `TIMESTAMP` data types aren't supported.
     * Ensure that you configured your change stream retention window correctly. If Datastream falls behind the retention window, you might lose data, and the stream might fail.



## Required permissions

To use the automated stream creation flow, ensure that the user or service account configuring the stream has the following IAM roles or permissions:

  * **Datastream Administrator** (`roles/datastream.admin`) or **Datastream Editor** (`roles/datastream.editor`) to create and manage the stream and connection profiles.
  * **Spanner Database Reader** (`roles/spanner.databaseReader`) or **Spanner Admin** (`roles/spanner.admin`) on the source database to access data and track changes.
  * **BigQuery Data Editor** on the destination dataset.



## Create and start the stream

To create and start a stream using the automated flow, perform the following steps:

### Console

  1. In Google Cloud console, go to the **Spanner Instances** page.



[Go to Spanner Instances](https://console.cloud.google.com/spanner)

  1. Select the Spanner instance and database from which you want to stream data.
  2. Create and start your stream automatically, in one of the following ways:

     * In the instances overview page, click **Start stream** under **Data replication to BigQuery**.
     * In the database overview page, on the **Integrations** tab, click **Create stream** under **Replicate data to BigQuery**.
  3. The **Start stream to replicate data** pane opens.

  4. Under **Stream settings** , review the default settings for the stream that you create.

  5. If you create your stream from the instances overview page, you can change the source database by expanding the corresponding drop-down and selecting a different value.

  6. You can change a stream by expanding the **Change stream** drop-down and selecting a different value.

  7. When you're ready to create and start your stream, click **Start stream**.




## Monitor the stream

To monitor basic stream details from your source Spanner database overview page in Google Cloud console, click the **Change streams** tab, and then click the stream that you want to view.

## Delete the stream

When you delete a stream created using the automated flow, Datastream deletes the stream object and associated connection profiles created for the stream.

However, you must manually delete any Spanner change streams or destination resources that were created independently if they're no longer needed.

## What's next

  * Learn more about [Stream data from Spanner sources](https://docs.cloud.google.com/datastream/docs/sources-spanner).
  * Learn how to [Configure a source Spanner database](https://docs.cloud.google.com/datastream/docs/configure-spanner).
  * Learn more about [Datastream overview](https://docs.cloud.google.com/datastream/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
