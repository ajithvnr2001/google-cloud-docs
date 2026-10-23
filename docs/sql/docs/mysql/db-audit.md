---
url: https://docs.cloud.google.com/sql/docs/mysql/db-audit/
title: MySQL database auditing \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:44.551680+00:00
---

# MySQL database auditing  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/db-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  MySQL database auditing Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/db-audit "View this page for the SQL Server database engine")

This topic describes Cloud SQL for MySQL database auditing and the Cloud SQL for MySQL Audit Plugin. To use database auditing now, see [Use MySQL database auditing](https://docs.cloud.google.com/sql/docs/mysql/use-db-audit).

## What is database auditing?

Database auditing lets you track specific user actions in the database, such as table updates, read queries, user privilege grants, and others. Database auditing is useful for organizations that need to have a trail of user activity for security reasons or to comply with various financial, governmental, and ISO regulations. Database auditing is supported for Cloud SQL for MySQL 5.7, 8.0, and 8.4.

### Cloud SQL for MySQL Audit Plugin

Database auditing is enabled by the Cloud SQL for MySQL Audit Plugin, or `cloudsql_mysql_audit`. This plugin uses the open [MySQL audit API](https://dev.mysql.com/doc/extending-mysql/8.0/en/writing-audit-plugins.html) to monitor and log activity in MySQL. The plugin sends logs to [Cloud Logging Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access). Data Access audit logs are disabled by default because audit logs can be quite large. You must explicitly [enable the logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) to use the plugin.

When the plugin is active, the existing audit rules that you have created are applied to generate audit logs for the database. When the plugin is deactivated, no audit logs are generated.

For more information about MySQL plugins, see [MySQL Server Plugins](https://dev.mysql.com/doc/refman/8.4/en/server-plugins.html).

## Who uses database auditing?

There are three types of users who are involved with database auditing:

  * **Administrators** \- Users who administer the database. Administrators are audit users responsible for enabling and disabling auditing on the instance and for creating new users. They also grant auditing permission to auditors. Administrators may also create, delete, and update audit rules.
  * **Auditors** \- Users who have permission to create, delete, and update the audit rules. They are granted access by administrators.
  * **Clients** \- Users whose activity is audited through the audit rules but who aren't audit users and have no administrative or auditing privileges themselves. Their access is governed by administrators.



Administrators and auditors are also referred to as audit users.

**Note:** These user types are different from the operational [ROLES](https://dev.mysql.com/doc/refman/8.0/en/roles.html) introduced in MySQL 8.0. 

## Audit rules

Database auditing uses _audit rules_ to define combinations of users, databases, objects, operations, and statuses that should trigger the creation of an audit log. An audit rule contains the following information:

  * **Id** \- Autonumeric rule identifier. Each audit rule has an audit ID automatically assigned to it when the rule is created. The audit ID isn't changeable once created.
  * **Username** \- Comma-separated list of users and/or wildcard patterns. You can use asterisks (`*`) as wildcards for both the user and the host. Use the asterisk as a suffix, a prefix, or both. In addition, users can use the wildcard character % only for the host. The maximum is 2048 characters.
  * **Dbname** \- Comma-separated list of database names and/or wildcard patterns. You can use asterisks (`*`) as wildcards for both the user and the host. Use the asterisk as a suffix, a prefix, or both. Maximum is 2048 characters.
  * **Object** : Comma-separated list of database objects (tables, functions, stored procedures, etc.) names and/or wildcard patterns. You can use asterisks (`*`) as wildcards for both the user and the host. Use the asterisk as a suffix, a prefix, or both. Maximum is 2048 characters.
  * **Operation** \- Comma-separated list of database operations. The plugin supports group operations (such as DDL, DML, etc.), single operations (such as update, delete, etc.) and wildcards (`*`) for all operations. See the [Full list of supported operations](https://docs.cloud.google.com/sql/docs/mysql/db-audit-operations). The plugin also supports operation groups that you can use to audit a group of operations. Maximum is 2048 characters.
  * **Op_result** \- Result of the operation.

    * `S` for auditing successful operations
    * `U` for auditing unsuccessful operations
    * `B` for tracking both successful and unsuccessful operations
    * `E` for creating exclusive rules

**Note:** Exclusive rules take precedence over inclusive rules. If a query matches both inclusive and exclusive rules, then it won't be audited. 

## Operation types

_Operation types_ are the multiple types of activities or operations that you can audit in the database:

  * `DQL` \- Read data from the database (that is, `SELECT` statements)
  * `DML` \- Add, delete, or modify data
  * `DDL` \- Create or modify the structure of database objects in the database
  * `DCL` \- Manage privileges for users in the database
  * `Show` \- Describe database objections or provide the status of the database
  * `Call` \- Invoke a stored procedure



## Considerations affecting audit logging

### Backups

When restoring an instance from a backup or point-in-time recovery (PITR), the audit rules also roll back to the time of the backup or the PITR. This happens because the audit rules are part of the data stored in the database, as are the targets (the users and objects) the rule is auditing.

### Read replicas

Audit rules are automatically replicated from a primary instance to its read replicas. Customers can't add, remove, or modify audit rules on read replicas. If you want to change audit rules for a replica, you need to update the primary instance's audit rules.

If you update audit log rules on the primary instance, you need to reload the audit rule on the replica in order to ensure the new audit rules are updated on the read replicas as well. The following command reloads the audit rule:
    
    
    CALL mysql.cloudsql_reload_audit_rule(1)
    

Users can enable audit logging on replicas independently of the primary instance. After making changes on the primary instance, you need to run the reload command or restart the replica instance to make the audit log rules effective.

### Database availability during audit log failure

If an audit operation fails, Cloud SQL doesn't stop the database activity from completing. For example, when an instance runs out of disk space and Cloud SQL can't generate an audit log, the database still lets the user perform read queries, even if this activity would normally generate an audit log.

### Read-only instances

If an instance has the `read_only` flag set to `true`, you can't add or update audit rules, because they are stored in the tables. Before you can create, update, or delete rules, you need to remove the `read_only` flag.

## Limitations and known issues

### Log ingestion rate

Before Cloud SQL sends audit logs to Cloud Logging, they are temporarily written to the disk of the instance, using disk space. Logs are uploaded to Cloud Logging and removed from the disk at a rate of 4 MB per second. When the load from log generation exceeds the upload rate, the instance undergoes an increase in disk usage, which can cause your database to run out of disk and crash. Even if automatic disk storage increases are enabled, the increase in disk usage increases costs.

While using this feature, we recommend that you:

  * [Enable automatic storage increases](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen).
  * Monitor the overall disk usage. You can't monitor the load from log generation separately. Use the **cloudsql.googleapis.com/database/disk/utilization** metric in the [Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer).
  * If necessary, reduce the log generation rate by limiting database activity or reducing auditing.

**Note:** If the available disk space is depleted, audit logs for some queries might be lost. 

### Audit unsuccessful operations

If your audit rules include auditing for unsuccessful operations (`op_result` is set to `U` for unsuccessful operations or `B` for both unsuccessful and successful operations), some users might be able to overload your database instance with audit logs by continuously executing unsuccessful operations. If the log generation speed exceeds the log ingestion rate, unwanted growth in disk usage can occur, depleting disk space. Instead, when auditing unsuccessful operations:

  * Control access at the [instance-level](https://docs.cloud.google.com/sql/docs/mysql/instance-access-control).
  * Set up a monitoring or alerting system for the abnormal increase of the unsuccessful operation logs.



### Audit rules

You can't create more than a total of 1000 audit rule combinations per database instance. An audit rule combination is a unique set of a user, database, object, and operations. For example, an audit rule auditing `user1,user2`, `db1,db2`, `table1,table2`, `select,delete` generates 2 x 2 x 2 x 2 = 16 combinations. Creating or updating audit rules fails if the total number of audit rule combinations exceeds 1000.

**Note:** As you increase the number of audit rule combinations, database auditing takes a longer time to match the query, thereby reducing the performance of the database. 

## Unsupported operations

Currently the following operations are not supported.

  * The following functions are unsupported, when used as described:

    * Within `SELECT` queries with `UNION`, `INTERSECT`, the `WHERE` clause, nested queries, subqueries, etc.
    * In `UPDATE`, `DELETE`, `INSERT`, `REPLACE` statements.

For example, if you have an audit rule to audit object `func1`, the following aren't audited:

    * `SELECT func1() FROM table;`
    * `SELECT * FROM table WHERE a = func1();`
    * `SELECT func1() != 0;`
    * `SELECT func1() > 0;`
    * `SET @x = func1();`

A function called directly by `SELECT` without any operators and without a `WHERE` clause is audited:

    * `SELECT func1();`
    * `SELECT db.func1();`
  * Filtering by IP address isn't supported at this time.




## What's next

  * Learn about how to [use MySQL database auditing](https://docs.cloud.google.com/sql/docs/mysql/use-db-audit).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
