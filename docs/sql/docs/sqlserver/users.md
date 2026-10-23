---
url: https://docs.cloud.google.com/sql/docs/sqlserver/users/
title: About SQL Server users \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:58.543700+00:00
---

# About SQL Server users  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  About SQL Server users Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/users "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/users "View this page for the PostgreSQL database engine") | SQL Server

This page describes how Cloud SQL works with SQL Server users and roles. SQL Server roles enable you to control the access and capabilities of users who access a SQL Server instance.

For information about creating and managing Cloud SQL users, see [Creating and managing users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users).

**Note:** See Other SQL Server users for additional information about users you create using Cloud SQL.

## SQL Server roles and users

SQL Server roles can be a single role, or they can function as a group of roles.

A user is a role with the ability to log in (the role has the `LOGIN` permission). All roles created by Cloud SQL have the `LOGIN` permission, so Cloud SQL uses the terms "role" and "user" interchangeably. However, if you create a role with any client tool that is compatible with SQL Server, then the role doesn't necessarily receive the `LOGIN` permission.

Cloud SQL for SQL Server restricts access to certain server roles that provide advanced privileges. Examples of these roles are `DbRootRole`, `serveradmin`, `securityadmin`, `setupadmin`, `diskadmin`, and `dbcreator`.

All SQL Server users must have a password. Thus, you can't log in with a user that lacks a password.

## Superusers and system stored procedures

Cloud SQL for SQL Server is a managed service, so it restricts access to certain system stored procedures and tables that require advanced privileges. In Cloud SQL, you cannot create or have access to users with superuser permissions.

**Note:** The `sysadmin` role is not supported. Therefore, you cannot run system stored procedures that require the `sysadmin` role. For example, you cannot run the `sp_OADestroy` stored procedure because it requires the `sysadmin` role. However, to export SQL Server logins, password hashes, and SIDs without requiring the `sysadmin` role, you can enable the [`cloud sql enable sp_help_revlogin`](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins) database flag to use the `sp_help_revlogin` stored procedure.

## Default SQL Server users

When you create a new Cloud SQL for SQL Server instance, the default `sqlserver` user is already created for you, although you must set its password.

The `sqlserver` user is part of the `CustomerDbRootRole` role, and its permissions (privileges) include the following:

  * `ALTER ANY CONNECTION`
  * `ALTER ANY LOGIN`
  * `ALTER ANY SERVER ROLE`
  * `ALTER SERVER STATE`
  * `ALTER TRACE`
  * `CONNECT SQL`
  * `CREATE ANY DATABASE`
  * `CREATE SERVER ROLE`
  * `VIEW ANY DATABASE`
  * `VIEW ANY DEFINITION`
  * `VIEW SERVER STATE`



You can also add [`cloudsql enable linked servers`](https://docs.cloud.google.com/sql/docs/sqlserver/linked-servers) to your instance if you want to use it with linked servers. This flag grants the following permission to your server:

  * `ALTER ANY LINKED SERVER`



If you want to export SQL Server logins, password hashes, and SIDs, then you can also add [`cloud sql enable sp_help_revlogin`](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins) to your instance. This flag installs the `sp_help_revlogin` stored procedure in the `msdb` database and grants the `sqlserver` user permission to run it.

**Note:** Cloud SQL for SQL Server doesn't support the `sysadmin` and `dbcreator` roles. Therefore, due to unavailable permissions, automated schema deployment using a [DACPAC](https://docs.microsoft.com/en-us/sql/relational-databases/data-tier-applications/data-tier-applications?view=sql-server-ver16) isn't supported.

## Granting server permissions

When you grant privileges using any [`GRANT` command](https://docs.microsoft.com/sql/t-sql/statements/grant-server-permissions-transact-sql?view=sql-server-ver15), you must pass `CustomerDbRootRole` as, for example, the value of `grantor_principal`.

The following `GRANT ALTER ANY LOGIN` example is **valid** :
    
    
    GRANT ALTER ANY LOGIN TO [Account] AS CustomerDbRootRole

The following `GRANT ALTER ANY LOGIN` example is **invalid** :
    
    
    GRANT ALTER ANY LOGIN TO [Account]

## Other SQL Server users

You can [create other SQL Server users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users) or roles. All users you create using Cloud SQL are granted the same database permissions as the `sqlserver` login. However, if you use a different process to create a user (rather than creating it using Cloud SQL), the user won't have the same permissions as the customer administrator accounts or the `sqlserver` user. For example, if you use the [create login](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-login-transact-sql?view=sql-server-ver16) process, and add the login to the `CustomerDbRootRole` server role, the user won't have the same permissions as the customer administrator accounts or the `sqlserver` user. Therefore, you can use Cloud SQL to create a user if you intend the user to have the same database permissions as the `sqlserver` login. To validate the difference in permissions between any two accounts, you can use the following function: [ sys.fn_my_permissions](https://learn.microsoft.com/en-us/sql/relational-databases/system-functions/sys-fn-my-permissions-transact-sql?view=sql-server-ver16).

**Note:** For reading audit files, Cloud SQL grants specific permissions to the `sqlserver` login, and that user can grant those permissions to other users. See [ Creating server audits](https://docs.cloud.google.com/sql/docs/sqlserver/db-audit#create-server-audits).

### Database imports: owner permissions

When you import a database, the treatment of the owner varies as follows, based on the type of owner:

  * **For an existing login that isn't`sa`:** Cloud SQL keeps that owner and creates a user called `sqlserver` that maps to the login `sqlserver`. Cloud SQL grants the `CONTROL` and `ALTER ANY USER` permissions to that `sqlserver` user.
  * **For unknown logins, or logins that were system-created:** Cloud SQL transfers ownership of the database to the `sqlserver` login.



### Changing permissions for users

The [ALTER ROLE](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-role-transact-sql) command is available for changing user permissions. If you create a new user with a client, you can associate it with a different role or provide different permissions.

## Troubleshooting

### Error accessing database

When trying to access to a database you created, as a user you created, you get the following error:
    
    
    The server principal USERNAME is not able to access the
    database DATABASE_NAME under the current security context.

#### The issue might be

The user is not a member of the database.

#### Things to try

Connect to the database as the `sqlserver` user and add the new user, then [ give the new user the `db_owner` role](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addrolemember-transact-sql?view=sql-server-2017) for the database. For example:
    
    
    EXEC sp_adduser 'user';
    EXEC sp_addrolemember 'db_owner', 'user'

## What's next

  * [Configure the user for your instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users#user-root).
  * [Create and manage users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users).
  * [Create and manage databases](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-databases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
