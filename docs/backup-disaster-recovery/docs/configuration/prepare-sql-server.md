---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sql-server/
title: Prepare SQL Server databases for Backup and DR on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:51.708526+00:00
---

# Prepare SQL Server databases for Backup and DR on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sql-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Prepare SQL Server databases for Backup and DR on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Microsoft SQL Server requires specific user roles to perform specific operations. To perform Backup and DR capture, restore, unmount, delete, and virtual application mount operations on a SQL Server database, you must provide credentials for a Windows user—a local user or a domain user—who has a role with sufficient SQL privileges to perform the operation.

This section details the user roles required to perform capture, restore, unmount, delete, and virtual application mount operations from a backup/recovery appliance. The recommended roles presented in this section are based on Microsoft's best practices for accessing SQL Server databases.

Before you begin, it's a good idea to review [Backup and DR for SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sql-intro).

**Note:** Creating users and assigning roles must be done by qualified system and database administrators. If users are improperly defined, or roles are improperly applied, the result can lead to Backup and DR job failure, security violations, and possible data loss.

## Windows local administrator user

To perform capture, restore, unmount delete, and virtual application mounts, the Backup and DR agent must be installed with the credentials of a Microsoft Windows user who has sufficient privileges in the SQL environment. The Windows user must be assigned a specific role or roles. The Microsoft Windows user can be a newly created or existing user.

## Required SQL roles for the Windows user

A Windows local administrator user assigned to the `sysadmin` server role has all necessary permissions to perform Backup and DR capture, restore and virtual application mounts.

If the `sysadmin` server role is deemed too liberal, then assign a Windows user the following roles:

  * `dbcreator` server role

  * `db_backupoperator` database role

  * `db_owner` database role




In addition, such users must also be assigned the following securables:

  * View any database

  * Create any database

  * Alter any database

  * Connect SQL




The following sections detail where to enter the Windows local admin's username and password to perform specific Backup and DR SQL related operations.

**Note:** In the following procedures, when entering user names, in most cases the domain name and user name—domain or username—format is sufficient. In rare cases, entering the domain name or username returns the error `Logon failure: unknown user name or bad password [1326]` In such cases, use the fully qualified domain name format `(username@fqdn</span>_)` to address the problem.

### Credentials for capturing SQL Server database logs

When applying a backup plan policy template to a SQL Server database, if the template contains a policy that captures database logs you must enter credentials of a Windows user assigned the proper roles in the management console in the application's backup plan application details and settings.

**Note:** Credentials are required for logs; they are not required if only databases are being captured.

### Credentials for restoring a Microsoft SQL Server database

When restoring SQL Server databases from the appliance management console, in the **Restore** dialog, enter credentials of a Windows user assigned the proper roles.

### Credentials for mounting a SQL Server database as a virtual application

A virtual application mount mounts a SQL Server database as a virtual application. When performing a virtual application mount of a SQL Server database from a backup/recovery appliance, the user must be assigned a role that allows both the ability to mount and unmount—detach—the SQL Server database.

When performing a virtual application mount, in the **Mount** dialog **Advanced options** , enter the credentials of a Windows user assigned the proper roles.

## The Backup and DR Microsoft SQL Server DBA guide

This page is one in a series of pages specific to protecting and recovering Microsoft SQL Server databases with Backup and DR. You can find additional information at:

  * [Backup and DR for Microsoft SQL Server Databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sql-server)
  * [Prepare SQL Server databases for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sql-server)
  * [Add a SQL Server database host and discover databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sql-server)
  * [Configure backup plans for Microsoft SQL Server instances and databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sql-server)
  * [Application details and settings for Microsoft SQL Server instances and databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sql-server)
  * [Mount a SQL Server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sql-server)
  * [Mount databases into SQL Always On Availability Groups](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sql-server-aag)
  * [Manage an active mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts)
  * [Migrate a SQL Server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-sql-server-2)
  * [Clone SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-sql-server)
  * [Recover SQL Server backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sql-server)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
