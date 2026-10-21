---
url: https://docs.cloud.google.com/sql/docs/postgres/pg-audit/
title: Audit for PostgreSQL using pgAudit \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:32.127346+00:00
---

# Audit for PostgreSQL using pgAudit  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/pg-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Audit for PostgreSQL using pgAudit Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes database auditing using the [pgAudit](https://www.pgaudit.org/) extension, which helps you configure many of the logs often required to comply with government, financial, and ISO certifications.

**Important:** Audit logs are temporarily written to the disk of their instance, taking up disk space. Disk space is affected before logs are sent to Cloud Logging, as described on this page. Therefore, before using this feature, review the Limitations section.

For general information about PostgreSQL extensions in Cloud SQL, see [PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

## Overview

Database auditing in Cloud SQL for PostgreSQL is available through the open-source pgAudit extension.

Using this extension, you can selectively record and track SQL operations performed against a given database instance. The extension provides you with auditing capabilities to monitor and record a select subset of operations.

The pgAudit extension applies to executed SQL commands and queries. In contrast, [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) should be used to audit administrative and maintenance operations done on a Cloud SQL instance.

See the [Audit logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging#overview) page for more information about audit logging in Cloud SQL.

## Set up database auditing in Cloud SQL

**Note:** Enabling the pgAudit extension can lead to increased data storage requirements if a service disruption occurs. To ensure durability of pgAudit log records in the event of unexpected storage issues, we recommend that you [enable automatic storage increases](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-2ndgen) when using pgAudit.

The steps for audit logging using the pgAudit extension include:

  1. Enabling the `cloudsql.enable_pgaudit` flag in Cloud SQL.
  2. Running a command to create the pgAudit extension.
  3. Setting values for the `pgaudit.log` flag.



**Important:** Cloud SQL doesn't support using Terraform to create the pgAudit extension. Use a psql client to create this extension.

The default value for the `pgaudit.log` flag is `none`. To use the pgAudit extension, you must set values for this flag.

After you set up database auditing, you can view the logs and, if necessary, disable logging.

### Set up auditing

This section describes the basics of setting up database auditing operations.

#### Initial flag to enable auditing

In Cloud SQL, you use database flags for many operations, including adjusting PostgreSQL parameters and configuring an instance. The `cloudsql.enable_pgaudit` flag enables auditing for a given database instance. You can change the value of the `cloudsql.enable_pgaudit` flag through the Google Cloud console or through the `gcloud` command.

**Note:** Changing the value of the `cloudsql.enable_pgaudit` flag [restarts](https://docs.cloud.google.com/sql/docs/postgres/start-stop-restart-instance#restart) the instance.

Use the [standard instructions for flags](https://docs.cloud.google.com/sql/docs/postgres/flags) to enable the `cloudsql.enable_pgaudit` flag, setting the value to `on`. For example, to use the `gcloud` command, specify the following, substituting your instance name for `[INSTANCE_NAME]`:
    
    
    gcloud sql instances patch [INSTANCE_NAME] --database-flags cloudsql.enable_pgaudit=on

The `cloudsql.enable_pgaudit` flag is listed with the other [supported flags](https://docs.cloud.google.com/sql/docs/postgres/flags#list-flags-postgres) and it is specific to Cloud SQL.

#### Run the command to create the pgAudit extension

After enabling the database flag, run the `CREATE EXTENSION` command using a compatible psql client. The following command creates the pgAudit extension for all databases in a Cloud SQL instance:
    
    
    CREATE EXTENSION pgaudit;
    

#### Set values for the `pgaudit.log` flag

Use the [standard instructions for flags](https://docs.cloud.google.com/sql/docs/postgres/flags) to set values for the `pgaudit.log` flag.

For example, to turn on auditing for all database operations on an instance, you can use the following `gcloud` command:
    
    
      gcloud sql instances patch [INSTANCE_NAME] --database-flags \
      cloudsql.enable_pgaudit=on,pgaudit.log=all
    

#### Configure other settings for the database

To configure auditing settings for the database, follow the procedures under the Customizing database audit logging section.

### View database audit logs

To view audit logs, [enable](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) Data Access audit logs for your project. The generated pgAudit logs for a given instance are sent to Cloud Logging as [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access). Users can view the generated pgAudit logs through the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) application.

In the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) application, the pgAudit logs can be viewed by selecting the **cloudaudit.googleapis.com/data_access** log filter.

Alternatively, you can use the following query to show all pgAudit logs for a given Cloud SQL project:
    
    
    resource.type="cloudsql_database"
    logName="projects/<your-project-name>/logs/cloudaudit.googleapis.com%2Fdata_access"
    protoPayload.request.@type="type.googleapis.com/google.cloud.sql.audit.v1.PgAuditEntry"
    

#### Log format for pgAudit

Each pgAudit log entry in the [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access) has fields representing the information collected for a query.

Here is an example:
    
    
    {
      protoPayload: {
        @type: "type.googleapis.com/google.cloud.audit.AuditLog"
        methodName: "cloudsql.instances.query"
        request: {
          @type: "type.googleapis.com/google.cloud.sql.audit.v1.PgAuditEntry"
          auditClass: "READ"
          auditType: "SESSION"
          chunkCount: "1"
          chunkIndex: "1"
          command: "SELECT"
          database: "finance"
          databaseSessionId: 2209692
          parameter: "[not logged]"
          statement: "SELECT * FROM revenue"
          statementId: 2
          substatementId: 1
          user: "alice"
        }
      }
    }
    

The following are descriptions of the fields in the Data Access audit logs:

  * **auditClass**. The type of the statement that is logged. Possible values are `READ`, `WRITE`, `FUNCTION`, `ROLE`, `DDL`, `MISC`, and `MISC_SET`.
  * **auditType**. `SESSION` or `OBJECT`.
  * **chunkCount**. Chunking can occur on the data provided in the `parameter` and `statement` fields. The `chunkCount` field indicates the total number of chunks. Also see the description of the `chunkIndex` field.
  * **chunkIndex**. Specifies the index number of the data chunks in the `parameter` and `statement` fields (in the current `request` container). The initial number is `1`. Also see the description of the `chunkCount` field.
  * **command**. For example, `ALTER TABLE` or `SELECT`.
  * **parameter**. The `chunkIndex` field can determine the contents of this field; see the description of the `chunkIndex` field. If the value for `pgaudit.log_parameter` is set, the `parameter` field can contain the statement parameters as quoted CSV data. If there are no parameters, this field contains `[none]`. Otherwise, this field contains `[not logged]`.
  * **statement**. Statement that was executed on the backend. The `chunkIndex` field can determine the contents of the `statement` field; see the description of the `chunkIndex` field.
  * **statementId**. Unique statement ID for this session. Each statement ID represents a backend call. Statement IDs are sequential, even if some statements are not logged.
  * **substatementId**. Sequential ID for each sub-statement within the main statement.



Some of these fields also are described in the [pgAudit documentation](https://github.com/pgaudit/pgaudit/blob/master/README.md#format).

### Disable auditing

To disable database auditing, set the value of the `cloudsql.enable_pgaudit` flag to `off`. The value can be changed through the Google Cloud console or through the `gcloud` command. Use the [standard instructions for flags](https://docs.cloud.google.com/sql/docs/postgres/flags) to disable the `cloudsql.enable_pgaudit` flag.

**Note:** Changing the value of the `cloudsql.enable_pgaudit` flag causes a [restart](https://docs.cloud.google.com/sql/docs/postgres/start-stop-restart-instance#restart) of the instance.

Additionally, run the `DROP EXTENSION` command, using a compatible psql client, to remove the extension state:
    
    
    DROP EXTENSION pgaudit;
    

## Customize database audit logging in Cloud SQL

This section describes ways to customize the auditing behavior of a database instance.

**Important:** Before using procedures in this section, ensure that you initially followed the steps for setting up database auditing, including running the command to create the pgAudit extension.

For additional capabilities of the extension, review the [pgAudit documentation](https://github.com/pgaudit/pgaudit/blob/master/README.md/).

### Requirement for superuser privileges

In Cloud SQL, extensions can only be created by users that are part of the `cloudsqlsuperuser` role. When you create a new PostgreSQL instance, the default PostgreSQL user is created for you (although you must set the user's password). The default PostgreSQL user is part of the `cloudsqlsuperuser` role. For more information, see [PostgreSQL users](https://docs.cloud.google.com/sql/docs/postgres/users).

### Configure auditing for all database operations on the instance

To configure auditing for all databases in an instance, you must apply pgAudit settings at the system level. The system-level audit parameters can be set only as database flags through the Google Cloud console or the `gcloud` command. For example, to turn on auditing for all database operations on an instance, you can use the following `gcloud` command:
    
    
      gcloud sql instances patch [INSTANCE_NAME] --database-flags \
      cloudsql.enable_pgaudit=on,pgaudit.log=all
    

### Configure specific operations on all instance databases

For auditing on all instance databases, you can use the Google Cloud console or the `gcloud` command. For example, to turn on auditing for only read and write operations on the instance, you can use the following `gcloud` command. This example uses a [list-based syntax](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping) for specifying multiple values:
    
    
      gcloud sql instances patch [INSTANCE_NAME] \
      --database-flags ^:^cloudsql.enable_pgaudit=on:pgaudit.log=read,write
    

The command overwrites the existing database flags.

**Note:** To add new flags while retaining the existing ones, specify the values for all of the flags. Any flags not specified are set to their default values. For information about setting flags, including through the Google Cloud console, see [Setting a database flag](https://docs.cloud.google.com/sql/docs/postgres/flags#setting_a_database_flag).

### Configure auditing for a specific database

To configure auditing for a specific database, set the pgAudit parameters at the database-level. For example, the following SQL command can be used to turn on read and write auditing for a database named `finance`:
    
    
    finance=> ALTER DATABASE finance SET pgaudit.log = 'read,write';
    

### Configure auditing for a relation

Auditing for a relation is narrower than auditing for a specific database.

When you audit for a relation, a unique auditor role is assigned to the `pgaudit.role` parameter. Any object or relation that is granted to this role is logged.

For example, to configure auditing for all `SELECT` queries on the `salary` relation within the `employee` database, you can use these commands:
    
    
    employee=> CREATE ROLE auditor WITH NOLOGIN;
    employee=> ALTER DATABASE employee SET pgaudit.role = 'auditor';
    employee=> GRANT SELECT ON salary TO auditor;
    

You also can audit a subset of columns for a given relation.

For example, the following command configures audit logging to occur only when the columns `income` and `tax_status` are accessed from the `salary` relation:
    
    
    employee=> GRANT SELECT(income, tax_status) ON salary TO auditor;
    

### Configure auditing for a database user

You can turn on auditing for a specific user by setting the `pgaudit.log` parameter on a per `ROLE` level.

For example, the following SQL command sets auditing for all database operations executed by the user `Alice`:
    
    
    finance=> ALTER ROLE alice SET pgaudit.log = 'all';
    

## Mask sensitive data in audit logs

To enhance data privacy and security, you can configure pgAudit to mask [literal](https://en.wikipedia.org/wiki/Literal_\(computer_programming\)) values within the SQL statements being logged using the `cloudsql.pgaudit_mask_literals` flag. When this feature is enabled, string constants, numbers, and other literal values are replaced with positional placeholders in the audit logs. This lets you audit the structure of queries and the operations performed without logging potentially sensitive data values.

### Benefits

  * Prevents sensitive data that might be embedded in queries from appearing in audit logs, including the following examples: 
    * Passwords
    * Personal information
    * Secrets
  * Helps meet compliance and regulatory requirements regarding data privacy.



### How it works

When the `cloudsql.pgaudit_mask_literals` flag is set to `on`, the pgAudit extension processes the SQL statement before writing it to the audit log. If the extension identifies literal values in the query, then it replaces them before logging the query:

  * **Original statement:**
        
        INSERT INTO users (id, email) VALUES (123, 'sensitive@example.com');
        

  * **Statement in audit log, with masking enabled:**
        
        INSERT INTO users (id, email) VALUES ($1, $2);
        




Notice that the literal values for the ID and email are replaced in the returned audit log.

### Requirements

  * The `cloudsql.pgaudit_mask_literals` flag is supported in Cloud SQL for PostgreSQL versions 14 and later.
  * The `cloudsql.enable_pgaudit` flag is disabled by default and must be set to `on` to use.



### Enable masking

To enable literal masking, set the `cloudsql.pgaudit_mask_literals` database flag to `on`. You can set database flags using the Google Cloud console, gcloud CLI, or the Cloud SQL Admin API.

For more information, see [Configure database flags](https://cloud.google.com/sql/docs/postgres/flags).
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --database-flags cloudsql.enable_pgaudit=on,cloudsql.pgaudit_mask_literals=on
    

Replace INSTANCE_NAME with the name of your instance.

### Disable masking

To disable literal masking, set the `cloudsql.pgaudit_mask_literals` flag to `off`.
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --database-flags cloudsql.enable_pgaudit=on,cloudsql.pgaudit_mask_literals=off
    

Replace INSTANCE_NAME with the name of your instance.

## Tips for audit management in Cloud SQL

When you customize audit behavior, remember the following:

  * When the database flag `cloudsql.enable_pgaudit` is turned off, audit logging is immediately stopped. However, the applied pgAudit settings (for example, the `pgaudit.log` parameter settings) are preserved, unless they are explicitly removed.
  * The database instance is restarted whenever the database flag value for `cloudsql.enable_pgaudit` is changed.
  * Database users created through explicit `CREATE ROLE` commands lack the privilege to modify audit settings. Only database users created through the Google Cloud console and the `gcloud` command can modify audit settings.
  * When you enable both session audit logging and object audit logging, statements pertaining to both are added to logs. Session logging and object logging don't cancel or modify each other.



## Limitations of the pgAudit extension in Cloud SQL for PostgreSQL

Audit logs are temporarily written to the disk of their instance, taking up disk space before the logs are sent to Cloud Logging. Therefore, review all of the following information before using this feature:

  * The log ingestion rate is 4 MB per second. When the load from log generation exceeds the ingestion rate, the following can occur: 
    * Unwanted growth in disk usage can occur.
    * Disk space can be exhausted.
  * If you have enabled this feature and you run many queries that meet your audit criteria, disk usage can grow too fast.
  * Before using this feature, plan to: 
    * [Enable automatic storage increases](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-2ndgen).
    * Monitor the overall disk usage; the load from log generation cannot separately be monitored. Use the **cloudsql.googleapis.com/database/disk/utilization** metric in the [Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer).
    * If necessary, reduce disk usage by running fewer queries or reducing auditing.
  * If the available disk space is exhausted, audit logs for some queries may be lost.



## What's next

  * [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
