---
url: https://docs.cloud.google.com/sql/docs/mysql/resource-groups/
title: Manage CPU allocation with MySQL resource groups \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:39.195957+00:00
---

# Manage CPU allocation with MySQL resource groups  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/resource-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Manage CPU allocation with MySQL resource groups Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This document describes how you can configure and use [MySQL resource groups](https://dev.mysql.com/doc/refman/8.0/en/resource-groups.html) in Cloud SQL for MySQL to manage and prioritize the CPU resource allocation of your different data processing needs.

## Overview

MySQL resource groups, introduced in MySQL 8.0, let you manage and prioritize CPU resource allocation among different threads running on a single database instance. This is useful for mitigating the "noisy neighbor" problem where low-priority tasks, such as daily analytics or batch reports, can spike CPU usage and degrade the performance of critical, high-priority client connections, such as online transaction processing (OLTP).

Resource groups are supported on all Cloud SQL for MySQL 8.0 and later instances, both Cloud SQL Enterprise edition and Cloud SQL Enterprise Plus edition.

**Note:** To use MySQL resource groups, you must have maintenance version [`MYSQL_VERSION.R20260320.00_20`](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog) or later installed on your instance.

## Differences between community MySQL and Cloud SQL resource groups

Cloud SQL for MySQL is a fully managed service. To help ensure instance reliability and protect Cloud SQL's internal processes, the following differences and restrictions apply compared to community MySQL behavior:

  * CPU core affinity isn't supported
  * Prohibited system resource groups
  * Automatic binlogging and replication of resource group DDLs
  * Administrative privileges pre-granted



### CPU core affinity isn't supported

Specifying core-level CPU pinning isn't supported. For example, you can't specify `VCPU = 2-3` or `VCPU = 0` when you create a resource group in Cloud SQL for MySQL. Since the underlying VM core topology is abstracted, any attempt to use the `VCPU` clause in a `CREATE RESOURCE GROUP` or `ALTER RESOURCE GROUP` statement fails with the following access denied error. 

`ERROR 1227 (42000): Access denied; This operation (CPU clause) is not allowed on the Cloud SQL environment. Only THREAD_PRIORITY allowed;`

### Prohibited system resource groups

Creating system resource groups isn't supported in Cloud SQL. Only user-level resource groups (`TYPE = USER`) are allowed, with thread priorities ranging from `0` (highest user priority) to `19` (lowest user priority).

System resource groups are prohibited to prevent user workloads from starving critical Cloud SQL background jobs such as backups, monitoring, and replication.

Running the `CREATE RESOURCE GROUP` command with `TYPE = SYSTEM` will fail with the following error: 

`ERROR 1227 (42000): Access denied; This operation (TYPE=SYSTEM) is not allowed on the Cloud SQL environment. Only TYPE=USER is allowed;`

### Automatic binary logging and replication of resource group DDLs

In community MySQL, resource group operations such as `CREATE`, `ALTER`, and `DROP RESOURCE GROUP` are never written to the binary log. Cloud SQL overrides this default behavior so that all resource group definition commands are written to the binary log.

This ensures that resource groups automatically replicate to read replicas, which lets you use query optimizer hints (or `RESOURCE_GROUP` hints) on replicas to help avoid query failures due to missing groups. Group definitions are also captured in the binary log stream for point-in-time recovery (PITR).

Thread session assignments such as `SET RESOURCE GROUP` are not written to the binary logs.

### Administrative privileges are granted to `cloudsqlsuperuser`

To work with resource groups, you need the following administrative database privileges:

  * `RESOURCE_GROUP_ADMIN`: create, alter, and drop resource groups
  * `RESOURCE_GROUP_USER`: assign threads or use hints in queries



In Cloud SQL both privileges are granted by default to the `cloudsqlsuperuser` role.

MySQL administrators can also grant the `RESOURCE_GROUP_USER` or `RESOURCE_GROUP_ADMIN` database privilege to other users.

## Manage resource groups in Cloud SQL

You can configure and manage user-level resource groups in Cloud SQL to optimize resource allocation on your database. Doing so lets you control and prioritize the CPU resource allocation amongst various database session workloads on the instance.

For more details on MySQL resource group configuration, and reference behavior, see [Resource Groups](https://dev.mysql.com/doc/refman/8.0/en/resource-groups.html) in the MySQL documentation.

To manage resource groups in Cloud SQL, you can do the following:

  * **Create a resource group:** create user-level resource groups and specify custom thread priorities.
  * **Modify a resource group's priority:** adjust the CPU scheduling priority of an existing user-level resource group.
  * **Drop a resource group:** remove a resource group when it's no longer needed.
  * **Assign connections and queries to a resource group:** map active sessions, database users, or specific queries to a resource group.
  * **Monitor resource groups:** check configured resource groups and thread allocations.



### Before you begin

Before you create a resource group, verify the following:

  * You are logged in to the database with a user account that has the `RESOURCE_GROUP_ADMIN` privilege. The default `root` user and any database accounts assigned the `cloudsqlsuperuser` role have this privilege by default.

  * Your Cloud SQL instance is running MySQL 8.0 or higher.




### Create a resource group

Create user-level resource groups with a thread priority between `0` (highest priority) and `19` (lowest priority). The default thread priority for standard connections is `0`.

To create a resource group, run the following statement:
    
    
    CREATE RESOURCE GROUP GROUP_NAME
      TYPE = USER
      THREAD_PRIORITY = PRIORITY_VALUE;

Replace the following:

  * `GROUP_NAME`: the name of the resource group you want to create.
  * `PRIORITY_VALUE`: the CPU scheduling priority for the resource group, from `0` (highest priority) to `19` (lowest priority).



### Modify a resource group's priority

To modify the CPU scheduling priority of an existing resource group, run the following statement:
    
    
    ALTER RESOURCE GROUP GROUP_NAME
      THREAD_PRIORITY = PRIORITY_VALUE;

Replace the following:

  * `GROUP_NAME`: the name of the resource group you want to modify.
  * `PRIORITY_VALUE`: the new CPU scheduling priority.



### Drop a resource group

To drop a resource group, run the following statement:
    
    
    DROP RESOURCE GROUP GROUP_NAME;

Replace the following:

  * `GROUP_NAME`: the name of the resource group you want to drop.



### Assign connections and queries to a resource group

To enforce resource constraints on a workload, assign active connections or specific queries to your user resource groups.

To assign session connections to a group:

  1. Grant permission to the workload user:
         
         GRANT RESOURCE_GROUP_USER ON *.* TO 'USERNAME'@'%';

Replace the following:

     * `USERNAME`: the database user you want to grant the privilege to.
  2. When the user connects, run:
         
         SET RESOURCE GROUP GROUP_NAME;

Replace the following:

     * `GROUP_NAME`: the name of the resource group you want to assign the connection to.

Or specify a specific thread ID:
    
    SET RESOURCE GROUP GROUP_NAME FOR THREAD_ID;

Replace the following:

     * `GROUP_NAME`: the name of the resource group you want to assign the connection to.
     * `THREAD_ID`: the ID of the specific database thread you want to assign.



To assign a single query to a group (via an optimizer hint):

Use the `RESOURCE_GROUP` optimizer comment hint within your DML or `SELECT` statement:
    
    
    SELECT /*+ RESOURCE_GROUP(GROUP_NAME) */
      COLUMN_NAME_1,
      SUM(COLUMN_NAME_2)
    FROM TABLE_NAME
    GROUP BY COLUMN_NAME_1;

Replace the following:

  * `GROUP_NAME`: the name of the resource group you want to run the query under.
  * `COLUMN_NAME_1`: the column you want to group your results by.
  * `COLUMN_NAME_2`: the column value you want to sum.
  * `TABLE_NAME`: the table you want to query.



### Monitor resource groups

To inspect configured resource groups:
    
    
    SELECT * FROM INFORMATION_SCHEMA.RESOURCE_GROUPS;
    

To view active connection threads and their assigned resource groups, run the following query:
    
    
    SELECT THREAD_ID, NAME, TYPE, RESOURCE_GROUP
      FROM performance_schema.threads;
    

## What's next

  * [Monitor Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance)
  * [Use system insights to improve system performance](https://docs.cloud.google.com/sql/docs/mysql/use-system-insights)
  * [Optimize high CPU usage](https://docs.cloud.google.com/sql/docs/mysql/optimize-cpu-usage)
  * [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights)
  * [Monitor active queries](https://docs.cloud.google.com/sql/docs/mysql/monitor-active-queries)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
