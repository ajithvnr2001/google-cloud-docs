---
url: https://docs.cloud.google.com/sql/docs/mysql/view-performance-capture-logs/
title: View performance capture logs \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:31.173716+00:00
---

# View performance capture logs  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/view-performance-capture-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  View performance capture logs Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

Performance capture collects and sends instance metrics data to Cloud Logging in the `mysql-performance-capture.log` file.

For more information about viewing logs in Cloud Logging, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

## Before you begin

To view performance capture logs, you must have the proper permissions to view logs in Cloud Logging for your project and instance.

### Required roles and permissions

To get the permissions that you need to view performance capture logs, ask your administrator to grant you the [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) IAM role on the project of the instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View performance capture logs

To view performance capture logs, do the following:

  1. In the Google Cloud console, go to the **Cloud Logging** page.

[Go to Cloud Logging](https://console.cloud.google.com/logs/query)

  2. Click **All resources** , then select **Cloud SQL Database**.
  3. Select your Cloud SQL instance.
  4. Filter for the log name:
         
         logName="projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fmysql-performance-capture.log"

Replace PROJECT_ID with your project ID.

The log payload is in the string format and contains the output of captured commands like `SHOW ENGINE INNODB STATUS` spanning across multiple log lines.




## Review the data in a performance capture log

Each performance capture log is triggered by a performance event that you defined for your instance. The following table correlates performance capture log entries with the configuring thresholds and provides a description of the performance data report that you can view in the entry log.

Performance capture log entry | Description | Trigger conditions | Report name  
---|---|---|---  
Active queries | Captures database load metrics including connection and transaction counts grouped by state, active query counts bucketed by runtime duration (<2 seconds, 2 to 10 seconds, ≥10 seconds), and detailed information for the top 50 longest-running transactions or queries. This report helps identify periods of high load and pinpoint specific slow queries.   
  
For more information about how to interpret data about InnoDB transactions and processes, see [The `INFORMATION_SCHEMA INNODB_TRX` Table](https://dev.mysql.com/doc/refman/8.4/en/information-schema-innodb-trx-table.html) and [The processlist Table](https://dev.mysql.com/doc/refman/8.4/en/performance-schema-processlist-table.html) in the MySQL documentation.  | 

  * High CPU utilization
  * High memory usage
  * High temp files usage
  * History list length
  * Running threads
  * Semaphore waits
  * Transaction lock waits

| `activequeries`  
InnoDB status | Provides information about the state of the InnoDB storage engine at the time of the performance event. This is critical for diagnosing lock contention, transaction issues, buffer pool problems, and History List Length growth. Keywords to look for:   


  * `TRANSACTIONS` (long-running transactions, lock waits)
  * `SEMAPHORES` (mutex contention)
  * `LATEST DETECTED DEADLOCK`
  * `BUFFER POOL AND MEMORY`
  * `HISTORY LIST LENGTH`

For more information about InnoDB standard monitor output, see [InnoDB Standard Monitor and Lock Monitor Output](https://dev.mysql.com/doc/refman/8.4/en/innodb-standard-monitor.html) in the MySQL documentation.  | `innodbstatus`  
Replication analysis | Contains replication diagnostic information, including the output of `SHOW REPLICA STATUS`, GTID sets, and details from performance schema tools. The report also includes the first five events from the relay log following the execution position at the time of the performance event. This report can be used to diagnose replication errors or delays.   
  
For more information about `SHOW REPLICA STATUS` output and replica applier threads, see [ SHOW REPLICA STATUS Statement](https://dev.mysql.com/doc/refman/8.4/en/show-replica-status.html) and [ Monitoring Replication Applier Worker Threads](https://dev.mysql.com/doc/refman/8.4/en/replication-threads-monitor-worker.html) in the MySQL documentation.  | 

  * Replica SQL I/O thread error
  * Seconds behind source

| `replicastatus`  
Transaction analysis | Details on the long-running transactions being tracked.   
  
For more information about how to interpret data about InnoDB transactions, see [The `INFORMATION_SCHEMA INNODB_TRX` Table](https://dev.mysql.com/doc/refman/8.4/en/information-schema-innodb-trx-table.html) in the MySQL documentation.  |  Long-running transactions  | `LongRunningTransactions`  
Automatically terminated transactions | Details on the long-running transactions terminated in current probing cycle.   
  
|  Auto termination data  | `AutoTerminateTransaction`  
  
## Filter the data in a performance capture log

When performance capture detects an issue based on a threshold configured for your Cloud SQL instance, the monitoring agent sends labeled log entries associated with the instance and type of report to Cloud Logging.

To help you sort through logs and correlate log entries with the performance issues observed for your instance, you can filter the performance capture log entries by label.

Each log entry is labeled with the following two labels:

  * Time of the event, or `labels.EVENT_TIME`: indicates the time of the performance capture entry log. The format is a unique timestamp string `_YYYY_ -_MM_ -_DD_ T _HH_ :_MM_ :_SS_ Z`. For example, `2025-10-16T13:12:07Z`.

  * Filename, or `labels.FILE_NAME`: identifies the type of report and the sequence number of the performance capture log entry triggered by a performance event. The format is `INSTANCE_TYPE_SEQUENCE_NUMBER_REPORT_TYPE`. For example, `primary_1_activequeries`, which is the first performance capture log entry of an active queries report.




## Example filters

This section provides examples of how to filter the `mysql-performance-capture.log` file for specific log entries for analysis.

In the following examples, replace the following:

  * PROJECT_ID: project ID of the Cloud SQL instance
  * TIMESTAMP: timestamp of the triggering performance event in the format `_YYYY_ -_MM_ -_DD_ T _HH_ :_MM_ :_SS_ Z`. For example, `2025-10-16T13:12:07Z`



### Filter by a specific performance event

To filter by a specific performance event, use the `labels.EVENT_TIME` label to find related log entries.

For example, to get reports for a specific performance event, use the following queries in Logging Logs Explorer query builder.

**Get all reports for a specific event**
    
    
    logName="projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fmysql-performance-capture.log"
    labels.EVENT_TIME="TIMESTAMP"

**Get InnoDB report for a specific event**
    
    
    logName="projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fmysql-performance-capture.log"
    labels.EVENT_TIME="TIMESTAMP"
    labels.FILE_NAME=~"innodbstatus"

**Get only the first log entry for all report types for a specific event**
    
    
    logName="projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fmysql-performance-capture.log"
    labels.EVENT_TIME="TIMESTAMP"
    labels.FILE_NAME=~"_1_"

### Filter across filenames

**Get all`activequeries` reports across all events**

This general query is useful for seeing how active queries look during any performance event.
    
    
    logName="projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fmysql-performance-capture.log"
    labels.FILE_NAME=~"activequeries"

Replace the following:

  * PROJECT_ID: project ID of the Cloud SQL instance



**Compare the 1st and 3rd`innodbstatus` reports for a specific event**
    
    
    logName="projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fmysql-performance-capture.log"
    labels.EVENT_TIME="TIMESTAMP"
    (labels.FILE_NAME="primary_1_innodbstatus" OR labels.FILE_NAME="primary_3_innodbstatus")

Replace the following:

  * PROJECT_ID: project ID of the Cloud SQL instance
  * TIMESTAMP: timestamp of the triggering performance event in the format `_YYYY_ -_MM_ -_DD_ T _HH_ :_MM_ :_SS_ Z`. For example, `2025-10-16T13:12:07Z`



**Find the first`activequeries` report for any event that occurred after a certain time**
    
    
    logName="projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fmysql-performance-capture.log"
    labels.FILE_NAME="primary_1_activequeries"
    timestamp > "TIMESTAMP"

Replace the following:

  * PROJECT_ID: project ID of the Cloud SQL instance
  * TIMESTAMP: timestamp in the format `_YYYY_ -_MM_ -_DD_ T _HH_ :_MM_ :_SS_ Z`. For example, `2025-10-16T13:12:07Z`



**Search for specific text within any InnoDB status report**
    
    
    logName="projects/PROJECT_ID/logs/cloudsql.googleapis.com%2Fmysql-performance-capture.log"
    labels.FILE_NAME=~"innodbstatus"
    textPayload:"SEARCH_TEXT"

Replace the following:

  * PROJECT_ID: project ID of the Cloud SQL instance
  * SEARCH_TEXT: the text that you want to search for. For example, `SEMAPHORE WAITS`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
