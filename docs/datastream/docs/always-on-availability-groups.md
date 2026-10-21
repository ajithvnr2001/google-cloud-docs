---
url: https://docs.cloud.google.com/datastream/docs/always-on-availability-groups/
title: Work with Always On availability groups \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:50.927841+00:00
---

# Work with Always On availability groups  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/always-on-availability-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Work with Always On availability groups Stay organized with collections  Save and categorize content based on your preferences. 

  


This page describes what Always-On availability groups in SQL Server are and how Datastream supports them for failover and data recovery scenarios.

## Overview of Always On availability groups

In SQL Server, Always On availability groups are a high-availability solution that lets you prepare your databases for disaster recovery scenarios.

Always On availability groups maximize database availability for businesses. Availability groups support a replicated environment for a selected set of databases, known as availability databases. Each group includes one set of primary databases for read and write tasks, and up to eight sets of corresponding secondary databases. The secondary databases can optionally allow read-only access or backup operations.

For more information about Always On availability groups, see [What is an Always On availability group?](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server) in the SQL Server documentation.

For information about Always On Availability group prerequisites for a SQL Server instance, see the [SQL Server documentation](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/prereqs-restrictions-recommendations-always-on-availability?view=sql-server-ver17&source=recommendations#ServerInstance).

## Configure Datastream for use with Always On availability groups

Datastream supports _synchronous-commit_ availability mode with the change tables CDC method. Under this mode, the secondary database stays synchronised with the corresponding primary until data synchronization stops. The confirmation of a transaction is only sent to the client when the secondary replica writes the incoming transaction log records to a disk.

For information about availability modes, see [Differences between availability modes for an Always On availability group](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server).

To configure your SQL Server instance for use with Always On availability groups, you need to enable SQL Server Agent to capture logs when there's a failover, and then run a clean up job. Before you can do this, you need to modify the CDC Agent job steps to check if the current replica is actually the primary. This is done using the `sys.fn_hadr_is_primary_replica` function.

Use the following commands to set up your instance:
    
    
      -- Check if the current replica is a primary for the corresponding database.
      USE [DATABASE_NAME];
      DECLARE @DatabaseName SYSNAME = DB_NAME();
      IF (SELECT sys.fn_hadr_is_primary_replica(@DatabaseName)) = 1
      BEGIN
      -- If the replica isn't a primary, the code block that follows is skipped
      EXECUTE sys.sp_cdc_add_job @job_type = 'capture';
      EXECUTE sys.sp_cdc_add_job @job_type = 'cleanup';
      END
    

## Known limitations

Known limitations for using Datastream with Always On availability groups include:

  * Datastream doesn't support private DNS resolution based on listener IP addresses. You must manually switch over the IP addresses for the replicas.
  * After an availability group failover, you must manually ensure that the SQL Server Agent capture and cleanup jobs are running on the new primary. Failure to do so might result in data loss if the transaction logs are truncated before Datastream can read the changes.
  * If a replica is created earlier than the primary, then you must add the `always_on_availability: true` label to your stream to prevent data integrity issues. For information about adding labels to your stream, see [Define settings for the stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#definestreamsettings).



## What's next

  * Learn more about how Datastream works with [SQL Server sources](https://docs.cloud.google.com/datastream/docs/sources-sqlserver).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
