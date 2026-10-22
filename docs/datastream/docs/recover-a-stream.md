---
url: https://docs.cloud.google.com/datastream/docs/recover-a-stream/
title: Recover a stream \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:28.008170+00:00
---

# Recover a stream  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/recover-a-stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Recover a stream Stay organized with collections  Save and categorize content based on your preferences. 

You can recover a permanently failed stream without having to create a new stream. You can do this by specifying the position from which Datastream attempts to resume reading changes from the source.

## Stream recovery overview

A running stream can encounter some unrecoverable errors and change its state to `FAILED_PERMANENTLY`. Such errors prevent the stream from continuing to run, and might cause data loss.

You can recover a permanently failed stream by setting it to ignore the error and keep reading the ongoing events instead of recreating the stream and backfilling the historical data. To recover a permanently failed stream, you reset the replication to start reading from a different replication position. Each supported source type has its own definition of what a replication position is:

  * For Oracle sources, a replication position is a [redo log file](https://docs.cloud.google.com/datastream/docs/work-with-oracle-database-redo-log-files) in the database and the system change number (SCN) in this file.
  * For MySQL sources, a replication position is the database binary log (binlog) file and the position in this file (for binlog-based replication), or a set of global transaction identifiers called a [GTID set](https://dev.mysql.com/doc/refman/8.0/en/replication-gtids-concepts.html#replication-gtids-concepts-gtid-sets) (for GTID-based replication, supported only in the Datastream API).
  * For SQL Server sources, a replication position is the log sequence number (LSN) in the transaction logs or change tables.
  * For PostgreSQL sources (including AlloyDB for PostgreSQL), a replication position is the log sequence number (LSN) in the replication slot. During recovery, the stream starts reading from the first LSN in the replication slot.
  * For MongoDB sources, a replication position is a timestamp in the MongoDB operations log (oplog).



## Recover a stream for a MySQL or an Oracle source

To recover a stream for a MySQL (binlog-based replication) or Oracle source, you have the following options:

  * **Retry from the current position (recommended)** : select this option to attempt streaming from the current position, where the stream last failed. You need to fix the log file or recover it from backup first. This is the recommended option.

  * **Skip the current position and stream from the next available position** : if one or more log files are missing, select this option to skip these files and resume streaming from the first position in the subsequent available file. The changes from the missing log files are lost, but you can recover them by performing a backfill.

  * **Skip the current position and stream from the most recent position** : if one or more log files are missing, select this option to skip these files and resume streaming from the most recent position in the most up-to-date log file. The changes from the missing log files are lost, but you can recover them by performing a backfill.

  * **Resume from your preferred streaming file and position** : select this option to resume the stream from a specific log file and log position. Some changes might be lost if the specified log position doesn't overlap with or immediately follow the lost log position. You can recover these changes by performing a backfill.




To recover a permanently failed stream for a MySQL or an Oracle source, perform the following steps:

  1. Go to the **Streams** page in Google Cloud.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click **Recover** in the row with the name of the stream that you want to recover.

  3. The **Choose a recovery strategy** pane opens. Select an option. If you select **Resume from your preferred streaming file and position** , enter the following:

     * For a MySQL source: the log filename in the **File name** field and the log position in the **Position** field. If you don't specify the position, the stream resumes from the first position in the indicated log file.
     * For an Oracle source: the system change number (SCN) in the **System Change Number (SCN)** field. This field is mandatory.
  4. Click **Apply**.

  5. When the stream is recovered, a timestamp appears in the **Recovered** column in the **Streams** page.


**Note:** For information about how to recover a permanently failed MySQL stream using GTID-based replication, see [Manage streams using the API](https://docs.cloud.google.com/datastream/docs/manage-streams#recover-mysql-oracle).

## Recover a stream for a PostgreSQL source

To recover a stream for a PostgreSQL source, you need to provide the replication slot name. The server uses this replication slot to send events to Datastream. The replication slot name can be the same as the slot used for the failed stream or different:

  * If the new replication slot has a different name, then provide the new replication slot name to Datastream.
  * If you don't provide a replication slot name, Datastream uses the replication slot name specified in the source configuration.

For more information about replication slots, see [Configure a source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database#publication-and-replication-slots).




Any change events to the source that occurred between the log position loss and the first LSN in the new replication slot are lost. You can recover these changes by performing a backfill.

To recover a permanently failed stream for a PostgreSQL source, perform the following steps:

  1. Go to the **Streams** page in Google Cloud.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click **Recover** in the row with the name of the stream that you want to recover.

  3. The **Define a new replication slot** pane opens.

  4. In the **Replication slot name** field, provide the name of a new replication slot from which the stream will attempt to recover. If you recreated the replication slot using the same name, or you want to reuse the slot you specified when you configured your source, you can leave this field empty.

  5. Click **Apply**.

  6. When the stream is recovered, a timestamp appears in the **Recovered** column in the **Streams** page.




You can also recover permanently failed streams from the **Stream details** page. To do this, click **Recover stream** when viewing detailed information about your stream.

**Note:** For information about how to recover a stream using the Datastream API, see [Manage streams](https://docs.cloud.google.com/datastream/docs/manage-streams#recoverastream).

## Recover a stream for a SQL Server source

To recover a stream for a SQL Server source, you have the following options:

  * **Resume from the first available position** : select this option if the log was truncated or some records are missing from change tables, and you want to resume from the first event available in the logs or change tables.

**Warning:** Use this option with caution. By selecting this, Datastream skips all events between the point of failure and the first LSN it can find in the current logs or change tables. This results in data loss for the skipped period, including any Data Manipulation Language (DML) changes and Data Definition Language (DDL) changes, such as added columns that occurred during that time. You must perform a backfill on the affected tables to ingest the missed data.
  * **Resume from your preferred log sequence number (LSN)** : select this option to resume the stream from a specific LSN in the transaction logs or change tables. This is the **recommended method** to ensure data integrity if you need to recover past a point of failure, especially if a table was dropped and recreated, or if maintenance occurred. To avoid data loss, choose an LSN that is _earlier_ than the event that caused the stream to fail or the period when changes were made. For example, if DDL changes were applied during a maintenance window, you should use an LSN from before the maintenance started.

**Finding a suitable LSN:**

    * Consult your SQL Server database logs to correlate times with LSNs.
    * If you know the approximate time, you can query system functions or tables to find an LSN close to that time. For example, you can use `sys.fn_dblog(NULL, NULL)`. Use this function with caution on a production system, as it reads the active transaction log. You can also examine CDC system tables like `cdc.lsn_time_mapping` in each change-tracked database.
    * The LSN in both the transaction logs and change tables contains 20 hexadecimal characters, but for transaction logs, it's separated by a delimiter. For example: 
      * LSN in transaction logs: `0000123C:0000BA78:0004`
      * LSN in change tables: `0000123C0000BA780004`

Some events might still be lost if the specified LSN doesn't overlap with or immediately follow the last LSN that Datastream was able to retrieve, but you have more control with this method. You can recover any missing events by performing a backfill.




To recover a permanently failed stream for a SQL Server source, perform the following steps:

  1. Go to the **Streams** page in Google Cloud.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click **Recover** in the row with the name of the stream that you want to recover.

  3. The **Choose a recovery strategy** pane opens. Select an option.

  4. Click **Apply**.

  5. When the stream is recovered, a timestamp appears in the **Recovered** column in the **Streams** page.




## Recover a stream for a MongoDB source

Stream recovery for MongoDB sources is available using the Datastream API. You can recover a MongoDB stream using the following options:

  * **Most recent start position** : select this option if you want to resume your stream from the current timestamp in the MongoDB oplog. The missing events are lost, but you can recover them by performing a backfill.

  * **Specific start position** : select this option to resume the stream from a selected timestamp. The timestamp that you use in your request must be valid, meaning that it can't be earlier than the earliest position available in the MongoDB oplog, and it can't be in the future.




For information about how to create a request to recover a MongoDB stream, see the Datastream API [reference documentation](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams/run#cdcstrategy).

For information about the MongoDB operations log, see the [MongoDB documentation](https://www.mongodb.com/docs/manual/core/replica-set-oplog/).

## Use stream recovery for a MySQL source in a manual failover scenario

You can perform a manual failover and use stream recovery to avoid recreating your streams from scratch during maintenance or primary instance failure. Generally, Datastream doesn't support failovers to replicas because they break the binlog continuity, but you can follow these steps to recover the stream and ensure your change data is captured:

  1. Stop all writes to the primary instance.
  2. Make sure that data freshness metric is set to 0. This means that Datastream captured all changes and there are no new events to read from the source. For more information, see [Monitor a stream](https://docs.cloud.google.com/datastream/docs/monitor-a-stream).
  3. Fail over to the new database instance.
  4. If needed, update the stream's connection profile to the new database instance (for example, you might need to change the database hostname or IP address). For more information, see [Modify connection profiles](https://docs.cloud.google.com/datastream/docs/modify-connection-profiles).
  5. Recover the stream from a specific position on the failover instance to ensure CDC continuity.



## What's next

  * To learn more about stream states, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).
  * To learn how to view information about your stream, see [View a stream](https://docs.cloud.google.com/datastream/docs/view-a-stream).
  * To learn how to monitor a stream, see [Monitor a stream](https://docs.cloud.google.com/datastream/docs/monitor-a-stream).
  * To learn how to manage backfill for a stream, see [Manage backfill for the objects of a stream](https://docs.cloud.google.com/datastream/docs/manage-backfill-for-the-objects-of-a-stream).
  * To learn how to delete an existing stream, see [Delete a stream](https://docs.cloud.google.com/datastream/docs/delete-a-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
