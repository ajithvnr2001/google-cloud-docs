---
url: https://docs.cloud.google.com/bigtable/docs/change-streams-configure/
title: Configure change streams \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:14.691629+00:00
---

# Configure change streams  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/change-streams-configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure change streams

If you want to track data changes made to a Bigtable table, you can enable a change stream for the table and then read it using an application such as Dataflow. Before you read this document, read the [Overview of change streams](https://docs.cloud.google.com/bigtable/docs/change-streams-overview). In particular, make sure that you are aware of the costs incurred when streaming changes.

This page describes how to enable, disable, and change the retention period for a change stream.

For instructions on creating a new table with a change stream enabled, see [Create a table](https://docs.cloud.google.com/bigtable/docs/managing-tables#create-table).

## Required role

To get the permissions that you need to enable, disable, or modify a Bigtable change stream, ask your administrator to grant you the following IAM role.

  * Bigtable Administrator ([`roles/bigtable.admin`](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.admin)) on the Bigtable instance that contains the table you plan to stream changes from



## Enable a change stream

To enable a change stream on an existing table, complete the following steps:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance containing the table that you want to enable a change stream for.

  3. Click **Tables** in the left pane.

The Tables page displays a list of tables in the instance.

  4. Click **Edit** for the table for which you want to enable a change stream.

  5. Click **Enable change stream**.

  6. In the **Expiration time** field, enter a number from 1 to 7 to configure the number of days that data stream records should be retained.

  7. Click **Save**.




###  gcloud 

To enable a change stream on a table, use the [`gcloud bigtable instances tables update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/update) command.
    
    
      gcloud bigtable instances tables update TABLE_ID \
            --instance=INSTANCE_ID \
            --project=PROJECT_ID \
            --change-stream-retention-period=CHANGE_STREAM_RETENTION_PERIOD
    

Replace the following:

  * `TABLE_ID`: the ID for the table whose changes you want to stream
  * `INSTANCE_ID`: the instance that contains the table
  * `PROJECT_ID`: the project that contains the instance
  * `CHANGE_STREAM_RETENTION_PERIOD`: the length of time that Bigtable should keep change stream data for the table. Must be no less than one day and no more than seven days, expressed as a number and a letter for the unit. Acceptable units are days (d), hours (h), minutes (m), and seconds (s). Example: `5d`



## Disable a change stream

You can disable a table's change stream at any time. Data stream records that were created before you disable the change stream continue to consume storage until the next [compaction](https://docs.cloud.google.com/bigtable/docs/overview#compactions), but you are no longer charged for that storage. You can't read a change stream after you disable it, including changes recorded before you disable the stream.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose tables you want to view.

  3. Click **Tables** in the left pane.

The Tables page displays a list of tables in the instance.

  4. Click **Edit** for the table whose change stream configuration you want to disable.

  5. Clear the checkmark from **Enable change stream**.

  6. Click **Save**.




###  gcloud 

To disable a change stream on a table, use the [`gcloud bigtable instances tables update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/update) command.
    
    
      gcloud bigtable instances tables update TABLE_ID \
            --instance=INSTANCE_ID \
            --project=PROJECT_ID \
            --clear-change-stream-retention-period
    

Replace the following:

  * `TABLE_ID`: the ID for the table whose changes you want to stream
  * `INSTANCE_ID`: the instance that contains the table
  * `PROJECT_ID`: the project that contains the instance



## Modify a change stream's retention time

You can modify the number of days that Bigtable keeps your change stream records. If you reduce the number of days, records that were streamed before the configuration change continue to consume storage until the next [compaction](https://docs.cloud.google.com/bigtable/docs/overview#compactions). After the configuration change, you can only stream changes from the newly specified time period.

If you increase the retention time, it's not retroactive — change streams are kept for the increased number of days starting when you modify the configuration.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose tables you want to view.

  3. Click **Tables** in the left pane.

The Tables page displays a list of tables in the instance.

  4. Click **Edit** for the table whose change stream configuration you want to modify.

  5. In the Expiration time field, enter a number from 1 to 7 for the number of days that data stream records should be retained.

  6. Click **Save**.




###  gcloud 

To change the retention period for a table's change stream, use the [`gcloud bigtable instances tables update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/update) command.
    
    
      gcloud bigtable instances tables update TABLE_ID \
            --instance=INSTANCE_ID \
            --project=PROJECT_ID \
            --change-stream-retention-period=CHANGE_STREAM_RETENTION_PERIOD
    

Replace the following:

  * `TABLE_ID`: the ID for the table whose changes you want to stream
  * `INSTANCE_ID`: the instance that contains the table
  * `PROJECT_ID`: the project that contains the instance
  * `CHANGE_STREAM_RETENTION_PERIOD`: the length of time that Bigtable should keep change stream data for the table. Must be from one to seven days, expressed as a number and a letter for the unit. Acceptable units are days (d), hours (h), minutes (m), and seconds (s). Example: `5d`



## What's next

  * [Read a change stream with Dataflow.](https://docs.cloud.google.com/bigtable/docs/change-streams-use-dataflow)
  * [Review Bigtable pricing.](https://cloud.google.com/bigtable/pricing)
  * [Complete a quickstart to learn how to enable a change stream and view changes.](https://docs.cloud.google.com/bigtable/docs/change-streams-quickstart)
  * [Use the Cloud Bigtable client library for Java to read change streams.](https://docs.cloud.google.com/bigtable/docs/change-streams-read-java)
  * [Work through a tutorial about processing a change stream.](https://docs.cloud.google.com/bigtable/docs/change-streams-tutorial)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
