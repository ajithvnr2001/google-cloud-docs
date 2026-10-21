---
url: https://docs.cloud.google.com/data-fusion/docs/troubleshoot-replication/
title: Troubleshoot replication jobs \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:39.301891+00:00
---

# Troubleshoot replication jobs  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/troubleshoot-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Troubleshoot replication jobs Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues related to Cloud Data Fusion replication jobs.

## Exception: Unable to create staging bucket

When the bucket naming convention is violated, the replication job might fail with the following error in the pipeline log:
    
    
    Caused by: java.io.IOException: Unable to create staging bucket
    BUCKET_NAME in project PROJECT_NAME.
    

You can optionally provide the staging bucket name. If not provided, the replication job generates one by appending a suffix to the job name. In some cases, you can use a shorter job name to resolve this issue. For more information, see [Bucket names](https://docs.cloud.google.com/storage/docs/buckets#naming).

## MySQL `CONVERT_TO_NULL` value not in set

If you are using an earlier version of MySQL Connector/J, such as version 5, the replication job fails with the following error:
    
    
    The connection property 'zeroDateTimeBehavior' only accepts values of the form:
    'exception', 'round' or 'convertToNull'. The value 'CONVERT_TO_NULL' is not in
    this set.
    

The accepted values for `zeroDateTimeBehavior` are incompatible between different versions of MySQL Connector/J.

To resolve this issue, use MySQL Connector/J version 8 or later.

## Replication and SQL Server Always On databases

A Microsoft SQL Server source can capture changes from an [Always On](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver15) read-only replica. For this setup, you must pass the runtime argument `source.connector.database.applicationIntent=ReadOnly` to the replication job. Without this runtime argument, the job fails with the following error:
    
    
    Producer failure
    java.lang.RuntimeException: com.microsoft.sqlserver.jdbc.SQLServerException:
    Failed to update database "DATABASE_NAME" because the database is read-only.
    

To resolve this issue, set `source.connector.database.applicationIntent=ReadOnly` as a [runtime argument](https://docs.cloud.google.com/data-fusion/docs/how-to/pass-runtime-args-in-replication#debezium-arguments). This internally sets `snapshot.isolation.mode` to `snapshot`.

## Replication error on Managed Service for Apache Spark static cluster

When you run a replication job, SSL connection from Managed Service for Apache Spark cluster nodes might fail with a `java.lang.NullPointerException` or `Connection reset` error:
    
    
    ERROR [SparkRunnerphase-1:i.c.c.i.a.r.ProgramControllerServiceAdapter@93] -
    Spark program 'phase-1' failed with error: The driver could not establish a
    secure connection to SQL Server by using Secure Sockets Layer (SSL) encryption.
    Error: "Connection reset ClientConnectionId:ID"
    

This error occurs due to the [Conscrypt SSL provider](https://github.com/google/conscrypt) configured for use in the JDK version installed on Managed Service for Apache Spark.

To resolve this issue, use the default SSL provider for Java JDK by disabling the Conscrypt SSL provider. To disable the Conscrypt SSL provider, set the following [cluster property](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/cluster-properties) when starting the Managed Service for Apache Spark cluster:
    
    
    --properties dataproc:dataproc.conscrypt.provider.enable=false
    

**Note:** Ensure that the self-signed certification is properly generated and formatted.

## Replication for SQL Server doesn't replicate all columns for changed tables

When you replicate data from a table in SQL Server, if your Replication source table has a newly added column, it isn't automatically added to the Change Data Capture (CDC) table. You must manually add it to the underlying CDC table.

To resolve this issue, follow these steps:

  1. Disable the CDC instance:
         
         EXEC sp_cdc_disable_table
         @source_schema = N'dbo',
         @source_name = N'myTable',
         @capture_instance = 'dbo_myTable'
         GO
         

  2. Enable the CDC instance again:
         
         EXEC sp_cdc_enable_table
         @source_schema = N'dbo',
         @source_name = N'myTable',
         @role_name = NULL,
         @capture_instance = 'dbo_myTable'
         GO
         

  3. Create a new replication job.




For more information, see [Handling changes to source tables](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server?view=sql-server-ver15#handling-changes-to-source-table).

## Roles and permissions errors

The following issues occur with access control.

### Cloud Data Fusion service account permission issue

When running a replication job using Oracle Database, retrieving a table list might fail with the following error:
    
    
    Error io.grpc.StatusRuntimeException: PERMISSION_DENIED: Permission
    'datastream.streams.get' denied on 'projects/PROJECT_NAME/locations/REGION/streams/STREAM_NAME'
    

When you run a replication job with an Oracle Database, Cloud Data Fusion uses the Datastream service in the backend. To get the permissions that you need to use the Datastream service, ask your administrator to grant you the [Datastream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.admin) (`roles/datastream.admin`) IAM role on the Cloud Data Fusion service account.

### Permission not granted to view Change Data Capture

When replicating data from SQL Server, you might see the following error in the pipeline log:
    
    
    No whitelisted table has enabled CDC, whitelisted table list does not contain any
    table with CDC enabled or no table match the white/blacklist filter(s)
    

This issue occurs if the user provided in the source connection properties doesn't have permissions to view the Change Data Capture (CDC) for the replicated table. This is controlled by the `role_name` parameter when enabling CDC on the table, using `sys.sp_cdc_enable_table`.

For more information about granting required permissions to view CDC, see [Enable CDC on table](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/964952171/Microsoft+SQL+Server+Replication+Source#Enable-CDC-on-Table) and [sys.sp_cdc_enable_table](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sys-sp-cdc-enable-table-transact-sql?source=recommendations&view=sql-server-ver16#syntax).

### User Defined Type permission issue

If the database user used by the replication job doesn't have permissions on the User Defined Type (UDT), you might see the following error in the pipeline log:
    
    
    java.lang.IllegalArgumentException: The primary key cannot reference a non-existent
    column'oid' in table TABLE_NAME
    

In this error message, the `oid` column might be a UDT.

To resolve this issue, grant access to the user by running the following command in the database:
    
    
    GRANT EXECUTE ON TYPE::UDT_NAME to YOUR_USER
    

## SQL Server Agent isn't running

If the SQL Server Agent isn't running, you might see the following error in the pipeline log:
    
    
    No maximum LSN recorded in the database; please ensure that the SQL Server Agent
    is running [io.debezium.connector.sqlserver.SqlServerStreamingChangeEventSource]
    

To resolve this issue, start the SQL Server Agent. For more information, refer to the following documentation depending on the Operating System you are using:

  * Windows: [Start the SQL Server Browser or an instance of the SQL Server Agent](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/start-stop-pause-resume-restart-sql-server-services?view=sql-server-ver16#start-stop-pause-resume-or-restart-the-sql-server-browser-or-an-instance-of-the-sql-server-agent)
  * Linux: [Enable the SQL Server Agent](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup-sql-agent?view=sql-server-ver16#EnableAgentAfterCU4)



## SQL Server Replication pipeline version isn't the latest

If the SQL Server Replication pipeline version isn't the latest, the following error appears in the pipeline log:
    
    
    Method io/cdap/delta/sqlserver/SqlServerDeltaSource.configure(Lio/cdap/delta/api/SourceConfigurer;) is abstract
    

This error occurs if an earlier version of the source plugin is working with a relatively new version of the delta app. In such cases, the new interface defined by the new version of delta app isn't implemented.

To resolve this issue, follow these steps:

  1. Retrieve information about the replication job by submitting an HTTP GET request:
         
         GET v3/namespaces/NAMESPACE_ID/apps/REPLICATOR_NAME
         

For more information, see [View replication job details](https://docs.cloud.google.com/data-fusion/docs/reference/replication-ref#replication-job-details).

  2. Check the versions of the plugin and the delta app used by the replication job.

  3. Retrieve the list of available artifacts by submitting an HTTP GET request:
         
         GET /v3/namespaces/NAMESPACE_ID/artifacts
         

For more information, see [List Available Artifacts](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692148/Artifact+Microservices#List-Available-Artifacts).


**Note:** The `USER` scope plugin overrides the `SYSTEM` scope plugin regardless of the plugin version used in the replication job configuration (response from the first API call). You must remove the earlier version of the plugin that is already uploaded. For more information, see [Delete Artifact Properties](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692148/Artifact+Microservices#Delete-Artifact-Properties).

## Static Managed Service for Apache Spark cluster with insufficient authentication scope

If you are using a static Managed Service for Apache Spark cluster that was created with insufficient authentication scope, you might see the following error in the pipeline log:
    
    
    ERROR [worker-DeltaWorker-0:i.c.c.i.a.r.ProgramControllerServiceAdapter@92] - Worker
    Program 'DeltaWorker' failed.
    Caused by: io.grpc.StatusRuntimeException: PERMISSION_DENIED: Request had
    insufficient authentication scopes.
    

To resolve this issue, [create a new static Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#console) and enable the `cloud-platform` scope for this cluster in the same project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
