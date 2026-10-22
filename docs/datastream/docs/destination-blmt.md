---
url: https://docs.cloud.google.com/datastream/docs/destination-blmt/
title: Configure Apache Iceberg tables in BigQuery \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:53.633706+00:00
---

# Configure Apache Iceberg tables in BigQuery  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/destination-blmt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure Apache Iceberg tables in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Datastream for replication to Apache Iceberg tables in BigQuery.

Apache Iceberg tables offer the same fully managed experience as standard BigQuery tables, but store data in customer-owned Cloud Storage buckets in the Apache Iceberg table format and Parquet file format. You can query and analyse data using BigQuery capabilities while keeping the data in your own storage buckets.

**Note:** Streaming to Apache Iceberg tables is supported only in the **append-only** write mode. For more information, see [Configure write mode](https://docs.cloud.google.com/datastream/docs/destination-bigquery#configure-write-mode).

### Table metadata

Datastream appends a `STRUCT` column named `datastream_metadata` to each table that's written to the BigQuery destination.

The `datastream_metadata` column contains the following fields:

  * `UUID`: This field has the `STRING` data type.
  * `SOURCE_TIMESTAMP`: This field has the `INTEGER` data type.
  * `CHANGE_SEQUENCE_NUMBER`: This field has the `STRING` data type. It's an internal sequence number used by Datastream for each change event.
  * `CHANGE_TYPE`: This field has the `STRING` data type. It indicates the type of the change event. For the append-only write mode the value is `INSERT`.
  * `SORT_KEYS`: This field contains an array of `STRING` values. You can use the values to sort the change events.



## Configure streaming to Apache Iceberg tables

To set up your stream to ingest data into Apache Iceberg tables:

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) where you want to store your data.
  2. Create a Cloud resource connection in BigQuery. For information about how to create this type of connection, see [Create and set up a Cloud resource connection](https://docs.cloud.google.com/bigquery/docs/create-cloud-resource-connection).
  3. Get the identifier of the connection service account:
         
         bq show --location=LOCATION --connection --project_id=PROJECT_ID
         CONNECTION_NAME
         

  4. Grant your Cloud resource connection access to the Cloud Storage bucket that you created. To do this, add the `storage.admin` IAM permission to the connection service account:
         
         gcloud storage buckets add-iam-policy-binding gs://YOUR_GCS_BUCKET \
         --member=serviceAccount:YOUR_SERVICE_ACCOUNT_ID \
         --role=roles/storage.admin
         

  5. Create an Apache Iceberg tables stream.

For information about how to create an Apache Iceberg tables stream using the Google Cloud console, see [Create a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream).

For information about how to create a request to stream data to Apache Iceberg tables using REST, `Google Cloud CLI` or Terraform, see [Manage streams using the API](https://docs.cloud.google.com/datastream/docs/manage-streams#createastream-blmt).


**Note:** The Cloud Storage bucket, BigQuery dataset, and the Datastream connection must all be in the same region.

## What's next

  * To learn more about streams, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).
  * To learn how to create a stream, see [Create a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream).
  * To learn how to create a connection profile that you can use with an Apache Iceberg tables stream, see [Create a connection profile for BigQuery](https://docs.cloud.google.com/datastream/docs/create-connection-profiles#cp4bigquery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
