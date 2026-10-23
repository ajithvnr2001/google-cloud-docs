---
url: https://docs.cloud.google.com/datastream/docs/modify-a-stream/
title: Modify a stream \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:42.371030+00:00
---

# Modify a stream  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/modify-a-stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Modify a stream Stay organized with collections  Save and categorize content based on your preferences. 

After you create a stream in Datastream, you can update its settings to match changes in your replication requirements. You can modify high-level stream details, such as the display name and labels, or update the source configuration to change replicated objects and backfill settings. For the destination configuration, you can adjust encryption, staleness limits, or output settings.

You can't change the source database type for an existing stream. To use a different database type, you must [create a new stream](https://docs.cloud.google.com/datastream/docs/create-a-stream).

## Modify high-level information

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream that you want to modify.

  3. On the **Stream details** page, click **EDIT**.

  4. Select **Edit stream settings** from the menu that appears.

  5. Modify the display name or labels for the stream. For more information about the stream's display name or labels, see [Define settings for the stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#definestreamsettings).

  6. After making your changes, click **SAVE**.




## Modify configuration information about the source database

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream that you want to modify.

  3. On the **Stream details** page, click **EDIT**.

  4. Select **Edit source configuration** from the menu that appears.

  5. In the **Select objects to include** section, use the **Objects to include** drop-down menu to change the tables and schemas in the source database that Datastream will transfer to the destination.

  6. Optionally, expand the **Select objects to exclude** node. In the **Objects to exclude** field, modify the tables and schemas in the source database that you want to restrict Datastream from transferring into the destination. If tables are added to this list, then they're no longer pulled into the destination. However, they're not removed from the destination. For more information about the **Objects to include** menu or the **Objects to exclude** field, see [Configure information about the source database for the stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#configuresourcedbinfo).

  7. Note that for Oracle sources, you can't modify the CDC method. However, you can change the database directories details, if you selected this log file access type.

  8. Optionally, expand the **Choose backfill mode for historical data** node to modify whether Datastream backfills the destination with current and future data from the source, or streams only changes to this data.

     * Select the **Automatic** option to stream all existing data, in addition to changes to the data, from the source into the destination.

If you select this option, then in the **Objects excluded from automatic backfill** field, you can modify the tables and schemas in the source database that you want to restrict Datastream from backfilling into the destination.

     * Select the **Manual** option to stream only changes to the data.

For more information about the **Choose backfill mode for historical data** node, see [Configure information about the source database for the stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#configuresourcedbinfo).
  9. After making your changes, click **SAVE**.




## Modify configuration information about the destination

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream that you want to modify.

  3. On the **Stream details** page, click **EDIT**.

  4. Select **Edit destination configuration** from the menu that appears.

  5. Depending on the destination that you selected, adjust the following settings as required:

**BigQuery** destinations:

     * Under **Encryption** , change the type of encryption that you want to use: Google-managed encryption key or Cloud Key Management Service key.
     * Under **Balance data staleness and BigQuery costs** , change the **Staleness limit** option.
**Caution:** The current staleness limit configuration is applied only to new BigQuery tables created by Datastream. Your tables might have a different staleness limitation depending on the date that they were created. To make sure that you apply the correct staleness limit to your existing tables, consider recreating the corresponding stream or modify each table using an [`ALTER TABLE` statement](https://docs.cloud.google.com/bigquery/docs/change-data-capture#modify-max-staleness).

**Apache Iceberg tables** destinations:

     * Under **Encryption** , change the type of encryption that you want to use: Google-managed encryption key or Cloud Key Management Service key.

**Cloud Storage** destinations:

     * In the **Stream path prefix** field, modify the folder of the destination into which Datastream will transfer schemas, tables, and data from the source database. If you change the folder, then all new files will be written to the new folder. Also, for more information about the **Stream path prefix** field, see [Configure information about the destination for the stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#configuredestinfo).
     * From the **Output format** menu: 
       * Choose the format of files written to Cloud Storage. Datastream supports two output formats: Avro and JSON.
       * If you select the JSON format, then select or clear the **Include a Unified Types schema file in the file path** and **Enable gzip compression** check boxes. For more information about these check boxes, see [Configure information about the destination for the stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#configuredestinfo).
  6. Click **SAVE** to apply your changes and [start your stream](https://docs.cloud.google.com/datastream/docs/run-a-stream#startastream). Any modifications that you make to streams that are running are updated by Datastream automatically.




## What's next

  * To learn more about streams, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).
  * To learn how to monitor a stream, see [Monitor a stream](https://docs.cloud.google.com/datastream/docs/monitor-a-stream).
  * To learn how to view information about your stream, see [View a stream](https://docs.cloud.google.com/datastream/docs/view-a-stream).
  * To learn how to recover a failed stream, see [Recover a stream](https://docs.cloud.google.com/datastream/docs/recover-a-stream).
  * To learn how to delete an existing stream, see [Delete a stream](https://docs.cloud.google.com/datastream/docs/delete-a-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
