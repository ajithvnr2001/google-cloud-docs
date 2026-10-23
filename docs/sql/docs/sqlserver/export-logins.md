---
url: https://docs.cloud.google.com/sql/docs/sqlserver/export-logins/
title: Export SQL Server logins \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:38.095153+00:00
---

# Export SQL Server logins  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/export-logins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Export SQL Server logins Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This document describes how to export SQL Server logins, security identifiers (SIDs), and password hashes from a Cloud SQL for SQL Server instance by using the [`sp_help_revlogin`](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/security/transfer-logins-passwords-between-instances#transfer-logins-and-passwords-by-using-sp_help_revlogin) stored procedure.

When you migrate databases, set up database synchronization, or maintain read replicas and disaster recovery (DR) replicas, you must re-create user logins on the destination instance with matching SIDs and password hashes. This helps to ensure that database users remain mapped to their corresponding server logins and retain their permissions.

**Tip:** We recommend exporting and re-creating logins on the destination instance before restoring your databases. Re-creating logins with matching SIDs first prevents orphaned database users. If logins or passwords change during migration, run the export again during the cutover window before redirecting application traffic.

Cloud SQL for SQL Server provides the `sp_help_revlogin` stored procedure in the `msdb` database to generate Transact-SQL (T-SQL) scripts for recreating user logins.

## Before you begin

### Required roles

To get the permission that you need to configure database flags, ask your administrator to grant you the following IAM roles on the project: 

  * [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)
  * [Cloud SQL Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `cloudsql.instances.update` permission, which is required to configure database flags. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Database permissions

Ensure that you have access to the default `sqlserver` SQL Server user role.

## Enable the database flag

To install the `sp_help_revlogin` stored procedure in the `msdb` database, enable the `cloud sql enable sp_help_revlogin` database flag on your instance.

### Google Cloud console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page. 

[Go to Cloud SQL instances](https://console.cloud.google.com/sql/instances)

  2. Click the instance name to open its **Overview** page.
  3. Click **Edit**.
  4. In the **Customize your instance** section, expand **Flags**.
  5. Click **Add flag**.
  6. Select **cloud sql enable sp_help_revlogin** from the list of available flags.
  7. Set the flag value to **on**.
  8. Click **Save**.



### gcloud CLI

Enable the flag by using the gcloud CLI:
    
    
    gcloud sql instances patch INSTANCE_NAME \
        --database-flags="cloud sql enable sp_help_revlogin=on"

Replace INSTANCE_NAME with the name of your Cloud SQL instance.

**Note:** Enabling or disabling this flag doesn't require an instance restart.

## Connect using a supported client tool

The `sp_help_revlogin` stored procedure outputs generated `CREATE LOGIN` scripts using T-SQL `PRINT` statements (informational messages) rather than tabular result sets (`SELECT` statements).

**Note:** Cloud SQL Studio only renders tabular query results. Running `sp_help_revlogin` in Cloud SQL Studio succeeds but displays an empty results pane. To view and export the generated scripts, connect by using SQL Server Management Studio (SSMS), Visual Studio Code with the MSSQL extension, or `sqlcmd`.

Connect to your Cloud SQL instance by using one of the following tools:

  * **SQL Server Management Studio (SSMS)** : connect to the instance, execute the procedure, and view the generated scripts in the **Messages** tab. Alternatively, press Control+T to switch the execution output mode to **Results to Text** before executing the query.
  * **Visual Studio Code** : connect by using the MSSQL extension, execute the procedure, and view the generated scripts in the **Messages** tab.
  * **sqlcmd utility** : connect to the instance and output the generated scripts directly to a SQL file:
        
        sqlcmd -S INSTANCE_IP \
            -U USERNAME \
            -P PASSWORD -d msdb \
            -Q "EXEC dbo.sp_help_revlogin" -o output_logins.sql
        

Replace the following:

    * `INSTANCE_IP`: the IP address of your Cloud SQL instance.
    * `USERNAME`: your administrative database username (such as `sqlserver`).
    * `PASSWORD`: your database user password.



## Export logins by using sp_help_revlogin

Connect to the `msdb` database and run the `sp_help_revlogin` stored procedure.

  * To export all customer logins:
        
        EXEC msdb.dbo.sp_help_revlogin;
        

  * To export a specific login:
        
        EXEC msdb.dbo.sp_help_revlogin
            @login_name = 'LOGIN_NAME';
        

Replace `LOGIN_NAME` with the name of the login to export.




## Re-create logins on the destination instance

  1. Copy the generated `CREATE LOGIN` statements from the query output.
  2. Connect to your destination SQL Server instance.
  3. Execute the generated statements in a query window or by using `sqlcmd`.



The generated statements create the logins on the destination instance with their original SIDs, default databases, and password hashes. For more information about considerations when transferring logins across instances, see the Microsoft documentation on [Transferring logins and passwords between instances of SQL Server](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/security/transfer-logins-passwords-between-instances#transfer-logins-and-passwords-by-using-sp_help_revlogin).

### Synchronize logins with read replicas

When Cloud SQL creates a read replica or disaster recovery (DR) replica, it copies existing logins from the primary instance. However, logins created on the primary instance after replica creation aren't automatically replicated.

Although user databases on a read replica are read-only, you can connect to a read replica and execute the `CREATE LOGIN` statements generated by `sp_help_revlogin` in the replica's `master` database.

We recommend that you routinely export new logins from your primary instance and re-create them on your read replicas and DR replicas. Routine synchronization ensures that users can authenticate to read replicas and that applications can reconnect immediately after a [switchover, replica failover](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery), or [replica promotion](https://docs.cloud.google.com/sql/docs/sqlserver/replication/manage-replicas#promote-replica).

## Limitations and excluded logins

`sp_help_revlogin` automatically excludes the following types of logins from the export:

  * Google Cloud service accounts and internal management accounts.
  * Internal SQL Server system accounts (logins prefixed with `##`).
  * Logins assigned to the `sysadmin` fixed server role.
  * Logins assigned to restricted administrative server roles.



## Disable the database flag

If you no longer need the stored procedure, then set the flag to `off` (or remove the flag from the instance):

### Google Cloud console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page. 

[Go to Cloud SQL instances](https://console.cloud.google.com/sql/instances)

  2. Click the instance name to open its **Overview** page.
  3. Click **Edit**.
  4. In the **Customize your instance** section, expand **Flags**.
  5. Find **cloud sql enable sp_help_revlogin** and set its value to **off** (or click **Delete** delete to remove the flag).
  6. Click **Save**.



### gcloud CLI
    
    
    gcloud sql instances patch INSTANCE_NAME \
        --database-flags="cloud sql enable sp_help_revlogin=off"

When set to `off` or removed, Cloud SQL automatically drops `dbo.sp_help_revlogin` from the `msdb` database.

## What's next

  * For more information about SQL Server users, see [SQL Server users](https://docs.cloud.google.com/sql/docs/sqlserver/users).
  * For more information about configuring database flags, see [Configure database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).
  * For more information about supported stored procedures, see [SQL Server stored procedures](https://docs.cloud.google.com/sql/docs/sqlserver/stored-procedures).
  * For more information about transferring logins and passwords, see [Transferring logins and passwords between instances of SQL Server](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/security/transfer-logins-passwords-between-instances#transfer-logins-and-passwords-by-using-sp_help_revlogin).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
