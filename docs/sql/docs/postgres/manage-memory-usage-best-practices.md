---
url: https://docs.cloud.google.com/sql/docs/postgres/manage-memory-usage-best-practices/
title: Best practices for managing memory usage \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:36.743579+00:00
---

# Best practices for managing memory usage  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/manage-memory-usage-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Best practices for managing memory usage Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes how to configure memory usage for a Cloud SQL instance.

## Introduction

When you create a Cloud SQL instance, you select an amount of memory for the instance. As a PostgreSQL database's workload increases, the instance's memory usage increases. Instances that consume lots of memory can create a performance bottleneck that can sometimes lead to out-of-memory issues.

When a Cloud SQL instance runs out of memory because of an increased demand, it can cause database downtime. Therefore, it's important to configure the instance memory and the memory-related database flags properly and monitor the memory usage so that the instance operates in a healthy state.

PostgreSQL memory components are broadly divided into two sections:

  * **Global memory:** this is shared across all processes to execute queries; for example, `shared_buffers` and `max_connections`.
  * **Local memory:** this is dedicated memory assigned to each connection; for example, `work_mem`, `maintenance_work_mem`, and `temp_buffers`.



For other configuration considerations, see [General best practices](https://docs.cloud.google.com/sql/docs/postgres/best-practices) and [Operational guidelines](https://docs.cloud.google.com/sql/docs/postgres/operational-guidelines).

## Memory usage and flags

Whenever there's high memory usage by Cloud SQL instances, the following questions might arise:

  * Which query or process is using high memory?
  * Are the memory settings adequate for the database activity?
  * How do you change the memory settings?



When a PostgreSQL database operates, most memory usage occurs in a few areas: 

  * **Shared buffer:** this is the shared memory that PostgreSQL allocates to hold table data for `read` and `write` operations. For the `read` operation, any data that's requested from disk is first fetched to RAM and then it's given to the client. Similarly, in PostgreSQL, when the data is requested (for example, `SELECT * from emp`), it's first fetched from disk to [`shared_buffers`](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-SHARED-BUFFERS) for caching, and then it's given to the client. The same thing happens with the `write` operation.

Shared buffer is also the shared memory area for all processes and connections for database activities such as data caching, connection caching, and Data Manipulation Language (DML) operations. The maximum that this area can allocate is specified by the `shared_buffers` flag and the default is 33% of the instance's memory. If the value of `shared_buffers` is high, the size of the data cached in memory is high.

  * **Query work memory:** as a query is run, PostgreSQL allocates local memory for each operation such as sorting and hashing. The maximum it can allocate for each operation of a query before writing to temporary disk files is configured by the [`work_mem`](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-WORK-MEM) flag, and the default value is 4 MB. If the value of `work_mem` is high, the amount of data that can be sorted in the memory is high.
  * **Maintenance work memory:** some maintenance operations such as `VACUUM`, `CREATE INDEX`, `ALTER TABLE`, and `ADD FOREIGN KEY` require separate local memory that PostgreSQL allocates. The maximum amount for the back-end process that these operations use can be configured by the [`maintenance_work_mem`](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM) flag and the default value is 64 MB. Note that autovacuum workers also use maintenance work memory and the maximum can be overridden by the [`autovacuum_work_mem`](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-AUTOVACUUM-WORK-MEM) flag. If the value of `maintenance_work_mem` is high, the performance speed of the `VACUUM` operation is high.
  * **Temporary buffers:** when a temporary table is used in a database session, PostgreSQL allocates temporary buffers to hold the session-local temporary table. The maximum amount can be specified by the [`temp_buffers`](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-TEMP-BUFFERS) flag and the default value is 8 MB.
  * **Database connection:** when a client connects to the database, PostgreSQL creates a back-end process to serve the client session. Besides the memory to run the query, PostgreSQL allocates additional memory to maintain information such as system catalog cache and prepared query plans. The maximum number of concurrent connections allowed to the database server can be configured by the [`max_connections`](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-MAX-CONNECTIONS) flag. Each idle connection uses approximately 2 MB to 3 MB of shared memory. If the value of `max_connections` is high, the instance can make more connections, but at the cost of the memory.



For the complete list of memory components in PostgreSQL, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY). To change or modify the flags listed in this section, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

## Monitor memory usage

[Monitor your instance's memory](https://docs.cloud.google.com/sql/docs/postgres/monitor-instance) in [Cloud Monitoring](https://docs.cloud.google.com/sql/docs/postgres/monitor-instance#cloud-monitoring) regularly and keep it below the memory limit. A good practice is to [set an alert](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy) in Cloud Monitoring to alert when the usage exceeds 90% of the limit for 6 hours. This alert can warn you when your memory usage is close to the limit constantly.

Additionally, monitor for out-of-memory incidents. To do that, set up a [log-based metric](https://docs.cloud.google.com/logging/docs/logs-based-metrics) for the `server process .* was terminated by signal 9: Killed` message in Cloud Monitoring to count the out-of-memory events, and then alert each time such an event happens.

If your instance operates constantly above 90% of the memory's limit or an out-of-memory event occurs, you can increase the instance's memory. Alternatively, you can reduce the memory usage by limiting the number of database connections or lowering database flags such as `shared_buffers`, `work_mem`, or `max_connections`. Lowering these flags can limit the performance of your instance.

## Out of memory

When there's insufficient memory to handle the database workload, as a last resort, the underlying Linux operating system uses the [`out-of-memory (OOM) killer`](https://linux-mm.org/OOM_Killer) to end a process to release memory. Cloud SQL is configured so that the `OOM killer` targets only the PostgreSQL worker processes. The postmaster process is preserved in this situation so that it only has to end all existing database connections and run a recovery to protect the integrity of the database. If this happens, there are moments of service disruption and downtime to the database. In the PostgreSQL database log, messages like the following appear:
    
    
    2021-10-24 23:34:22.265 UTC [7]: [663-1] db=,user= LOG: server process (PID 1255039) was terminated by signal 9: Killed
    2021-10-24 23:34:22.265 UTC [7]: [664-1] db=,user= DETAIL: Failed process was running: SELECT * FROM tab ORDER BY col
    2021-10-24 23:34:22.277 UTC [7]: [665-1] db=,user= LOG: terminating any other active server processes
    2021-10-24 23:34:22.278 UTC [1255458]: [1-1] db=postgres,user=postgres WARNING: terminating connection because of crash of another server process
    2021-10-24 23:34:22.278 UTC [1255458]: [2-1] db=postgres,user=postgres DETAIL: The postmaster has commanded this server process to roll back the current transaction and exit, because another server process exited abnormally and possibly corrupted shared memory.
    2021-10-24 23:34:22.278 UTC [1255458]: [3-1] db=postgres,user=postgres HINT: In a moment you should be able to reconnect to the database and repeat your command.
    2021-10-24 23:34:22.278 UTC [1255458]: [4-1] db=postgres,user=postgres CONTEXT: while updating tuple (27,18) in relation "tab"
    ...
    2021-10-24 23:34:22.558 UTC [1255477]: [1-1] db=postgres,user=postgres FATAL: the database system is in recovery mode
    ...
    2021-10-24 23:34:25.579 UTC [7]: [666-1] db=,user= LOG: all server processes terminated; reinitializing
    ...
    2021-10-24 23:34:25.691 UTC [1255482]: [1-1] db=,user= LOG: database system was interrupted; last known up at 2021-10-24 23:31:53 UTC
    2021-10-24 23:34:25.776 UTC [1255482]: [2-1] db=,user= LOG: database system was not properly shut down; automatic recovery in progress
    2021-10-24 23:34:25.789 UTC [1255482]: [3-1] db=,user= LOG: redo starts at 227/AB359400
    2021-10-24 23:34:38.957 UTC [1255482]: [4-1] db=,user= LOG: redo done at 229/4621F508
    2021-10-24 23:34:38.959 UTC [1255482]: [5-1] db=,user= LOG: last completed transaction was at log time 2021-10-24 23:34:18.5535+00
    2021-10-24 23:34:39.290 UTC [7]: [667-1] db=,user= LOG: database system is ready to accept connections

## Cancelled queries due to high memory usage

When a Cloud SQL database query uses a lot of memory, Cloud SQL proactively detects high memory usage and works to terminate the connection executing that query to prevent an out-of-memory (OOM) failure. This prevents database downtime due to the high memory usage.

You can identify a query cancelled due to high memory usage by looking at the log message for a query in your PostgreSQL database log. For example, a cancelled query's log will show the following message:
    
    
    (...timestamp….) [PID]:  db=postgres,user=$user_id LOG: Process [PID] received SIGTERM
    (...timestamp….) [PID]:  db=postgres,user=$user_id DETAIL: Cloud SQL cancelled this query owing to its excessive memory usage which can cause the PostgreSQL instance to crash.
    (...timestamp….) [PID]:  db=postgres,user=$user_id HINT:  To avoid future interruptions, consider increasing instance memory or optimizing this query.
    

If your database is using [query insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights), you can [view query details for a specific query](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights#specific-query) to find additional information about the cancelled query. Use these logs to identify the cancelled query and [optimize high-memory usage](https://docs.cloud.google.com/sql/docs/postgres/optimize-high-memory-usage) for your database by understanding and addressing the underlying causes for the cancelled query.

## What's next

  * Learn more about [configuring memory usage](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY) in PostgreSQL.
  * [Tuning your PostgreSQL server](https://wiki.postgresql.org/wiki/Tuning_Your_PostgreSQL_Server).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
