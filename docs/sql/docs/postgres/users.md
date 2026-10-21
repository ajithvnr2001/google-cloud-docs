---
url: https://docs.cloud.google.com/sql/docs/postgres/users/
title: About PostgreSQL users and roles \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:52.045336+00:00
---

# About PostgreSQL users and roles  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  About PostgreSQL users and roles Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/users "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/users "View this page for the SQL Server database engine")

This page describes how Cloud SQL works with PostgreSQL users and roles. PostgreSQL roles enable you to control the access and capabilities of users who access a PostgreSQL instance.

For complete documentation about PostgreSQL roles, see [Database Roles](https://www.postgresql.org/docs/current/static/database-roles.html) in the PostgreSQL documentation. For information about creating and managing Cloud SQL users, see [Create and manage users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users).

## Difference between users and roles

PostgreSQL roles can be a single role, or they can function as a group of roles. A user is a role with the ability to log in (the role has the `LOGIN` attribute). Because all roles Cloud SQL creates have the `LOGIN` attribute, Cloud SQL uses the terms _role_ and _user_ interchangeably. However, if you create a role with the `psql` client, the role does not necessarily have the `LOGIN` attribute.

All PostgreSQL users must have a password. You cannot log in with a user that lacks a password.

## Superuser restrictions and privileges

Cloud SQL for PostgreSQL is a managed service, so it restricts access to certain system procedures and tables that require advanced privileges. In Cloud SQL, customers cannot create or have access to users with superuser attributes.

You can't create database users that have superuser privileges. However, you can create database users with the `cloudsqlsuperuser` role, which has some superuser privileges, including:

  * Creating extensions that require superuser privileges.
  * Creating event triggers.
  * Creating replication users.
  * Creating replication publications and subscriptions.
  * Performing the `CREATE CAST` and `DROP CAST` statements as a database user with the `cloudsqlsuperuser` role. However, this user must have the `USAGE` privilege on both the source and target data types. For example, a user can create a cast that converts the source `int` data type to the target `boolean` data type.

**Note:** Cloud SQL doesn't support the `WITHOUT FUNCTION` cast method.
  * Having full access to the [ `pg_largeobject` catalog table.](https://www.postgresql.org/docs/current/static/catalog-pg-largeobject.html)

**Note:** For information about using the [`pg_shadow`](https://www.postgresql.org/docs/current/static/view-pg-shadow.html) view, see Access to the `pg_shadow` view and the `pg_authid` table.

## Default PostgreSQL users

When you create a new Cloud SQL for PostgreSQL instance, the default admin user `postgres` is created but not its password. You need to set a password for this user before you can log in. You can do this either in the Google Cloud console or by using the following `gcloud` command:
    
    
    gcloud sql users set-password postgres \
    --instance=INSTANCE_NAME \
    --password=PASSWORD

The `postgres` user is part of the `cloudsqlsuperuser` role, and has the following attributes (privileges): `CREATEROLE`, `CREATEDB`, and `LOGIN`. It does not have the `SUPERUSER` or `REPLICATION` attributes.

A default `cloudsqlimportexport` user is created with the minimal set of privileges needed for CSV import and export operations. You can create your own users to perform these operations, but if you don't, then the default `cloudsqlimportexport` user is used. The `cloudsqlimportexport` user is a system user, and you can't use it directly.

## Cloud SQL system users and roles

Cloud SQL uses system users and roles to support Cloud SQL features. You can't delete or modify Cloud SQL system roles or users. You can't assign system roles except the `cloudsqlsuperuser` role to database users. You can't assign database roles to system users.

  * System roles

    * `cloudsqliamgroup`

Used to designate a non-login IAM group authentication account that's used for IAM group authentication.

    * `cloudsqlinactiveuser`

Used to designate an IAM group authentication account as inactive.

    * `cloudsqliamgroupserviceaccount`

Used to designate a IAM service account that authenticates using IAM group authentication.

    * `cloudsqliamgroupuser`

Used to designate an IAM user who authenticates using IAM group authentication.

    * `cloudsqliamserviceaccount`

Used to designate an IAM service account that authenticates using IAM database authentication.

    * `cloudsqliamuser`

Used to designate an IAM user who authenticates using IAM database authentication.

    * `cloudsqlsuperuser`

Role granted to users with limited superuser privileges. The `cloudsqlsuperuser` role is granted automatically to new PostgreSQL users who use built-in authentication.

  * System users

    * `cloudsqladmin`

System user with superuser privileges on the database.

    * `cloudsqlagent`

Used for monitoring databases.

    * `cloudsqlconnpooladmin`

Used for [Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling).

    * `cloudsqlimportexport`

Used for data import and export.

    * `cloudsqllogical`

Used for building logical replication.

    * `cloudsqlobservability`

Used for database observability such as the [index advisor](https://docs.cloud.google.com/sql/docs/postgres/use-index-advisor) and [active queries](https://docs.cloud.google.com/sql/docs/postgres/monitor-active-queries).

    * `cloudsqlreplica`

Used for replication.




## Cloud SQL IAM users for IAM authentication

Identity and Access Management (IAM) is integrated with Cloud SQL in a feature called [IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/authentication#iam-db-auth). When you create instances using this feature, IAM users can sign in to the instance using their IAM usernames and passwords. The advantage to using IAM authentication is that you can use a user's existing IAM credentials when granting them access to a database. When the user leaves the organization, their IAM account is suspended, removing their access automatically.

## Other PostgreSQL users

You can [create other PostgreSQL users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users) or roles. [Users created using Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating) that aren't created using [IAM](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user) are created as part of the `cloudsqlsuperuser` role, and have the same set of attributes as the `postgres` user: `CREATEROLE`, `CREATEDB`, and `LOGIN`. You can change the attributes of any user using the [ALTER ROLE](https://www.postgresql.org/docs/current/static/sql-alterrole.html) command.

If you create a new user with the `psql` client, you can choose to associate it with a different role, or give it different attributes.

## PostgreSQL roles

You can create custom roles in PostgreSQL to help you organize and assign database privileges for your PostgreSQL users. You can use roles to provide initial database privileges for users when you create a Cloud SQL instance.

For more information about creating and using roles in PostgreSQL, see [Database roles](https://www.postgresql.org/docs/current/static/user-manag.html).

When you create a built-in PostgreSQL user in Cloud SQL for PostgreSQL and don't assign any database roles, the user is granted the `cloudsqlsuperuser` role automatically. Alternatively, you can create a new PostgreSQL user and assign a different custom role or roles with more fine-grained privileges. For more information about assigning roles to users in Cloud SQL for PostgreSQL, see [Manage users with built-in authentication](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating).

## Secure search path

To prevent [search path hijacking](https://wiki.postgresql.org/wiki/A_Guide_to_CVE-2018-1058%3A_Protect_Your_Search_Path), ensure that high-privileged users have the `search_path` parameter set to `pg_catalog`. This ensures that the search path is secured and untrusted schemas like `public` are bypassed.

To set this permanently for a user, run the following command:

`ALTER ROLE <var>USER_NAME</var> SET search_path = pg_catalog;`

To set it _for the current session_ , run the following command:

`SET search_path TO pg_catalog;`

For more information, see the [PostgreSQL documentation on secure schema usage](https://www.postgresql.org/docs/current/ddl-schemas.html#DDL-SCHEMAS-PATTERNS) and the [CVE-2018-1058 guide](https://wiki.postgresql.org/wiki/A_Guide_to_CVE-2018-1058%3A_Protect_Your_Search_Path).

## IAM users and database roles

When you create an IAM user account in Cloud SQL for PostgreSQL and don't assign any database roles, the user isn't granted any database roles automatically.

You can grant the `cloudsqlsuperuser` role and custom database roles to IAM users, service accounts or groups by assigning database roles when you create or update the IAM accounts on the instance.

For more information about granting roles to IAM users, see [Assign database roles while adding an IAM account to an instance](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#add-db-roles).

## Access to the `pg_shadow` view and the `pg_authid` table

You can use the [`pg_shadow`](https://www.postgresql.org/docs/current/static/view-pg-shadow.html) view to work with the properties of roles that are marked as `rolcanlogin` in the [`pg_authid`](https://www.postgresql.org/docs/current/static/catalog-pg-authid.html) catalog table.

The `pg_shadow` view contains hashed passwords and other properties of the roles (users) allowed to log in to a cluster. The `pg_authid` catalog table contains hashed passwords and other properties for all database roles.

In Cloud SQL, customers can't access the `pg_shadow` view or the `pg_authid` table using the default privileges. However, access to role names and hashed passwords is useful in certain situations, including:

  * Setting up proxies or load balancing with existing users and passwords
  * Migrating users without changes in passwords
  * Implementing custom solutions for password policy management



### Setting the flags for the `pg_shadow` view and the `pg_authid` table

To access the `pg_shadow` view, set the `cloudsql.pg_shadow_select_role` flag to a PostgreSQL role name. To access the `pg_authid` table, set the `cloudsql.pg_authid_select_role` flag to a PostgreSQL role name.

If the `cloudsql.pg_shadow_select_role` exists, then it has read-only (`SELECT`) access to the `pg_shadow` view. If the `cloudsql.pg_authid_select_role` exists, then it has `SELECT` access to the `pg_authid` table.

If either role doesn't exist, then the settings have no effect, but no error occurs. However, an error is logged when a user tries to access the view or the table. The error is logged in the PostgreSQL database log: `cloudsql.googleapis.com/postgres.log`. For information about viewing this log, see [View instance logs](https://docs.cloud.google.com/sql/docs/postgres/logging).

Ensure that the configured roles exist and that there isn't a typo in the value of either the `cloudsql.pg_shadow_select_role` flag or the `cloudsql.pg_authid_select_role` flag. You also can use the `pg_has_role` function to verify that a user is a member of these roles. Information about this function is available on the [System Information Functions and Operators](https://www.postgresql.org/docs/current/static/functions-info.html) page.

You can use the `cloudsql.pg_shadow_select_role` flag or the `cloudsql.pg_authid_select_role` flag with [PostgreSQL role membership](https://www.postgresql.org/docs/current/static/role-membership.html) to manage `pg_shadow` or `pg_authid` access for multiple users.

Changes to either flag don't require a database restart.

For more information about supported flags, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

### Choose a password storage format

Cloud SQL for PostgreSQL stores user passwords in a hashed format. You can use the `password_encryption` flag to set the encryption algorithm to `md5` or `scram-sha-256`. The `md5` algorithm provides the broadest compatibility, whereas `scram-sha-256` is more secure but might be incompatible with older clients.

When enabling `pg_shadow` access to export role properties from a Cloud SQL instance, consider using the most secure algorithm supported by your clients.

In the PostgreSQL documentation, also see:

  * [Password Authentication](https://www.postgresql.org/docs/current/static/auth-password.html)
  * [The `password_encryption` flag](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION)



## What's next

  * [Create and manage users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users).
  * [Create and manage databases](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases).
  * See the [PostgreSQL documentation about roles](https://www.postgresql.org/docs/current/static/database-roles.html).
  * Learn about [options for connecting to your instance](https://docs.cloud.google.com/sql/docs/postgres/external-connection-methods).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
