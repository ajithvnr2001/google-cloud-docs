---
url: https://docs.cloud.google.com/sql/docs/mysql/users/
title: About MySQL users \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:09.244709+00:00
---

# About MySQL users  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  About MySQL users Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/users "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/users "View this page for the SQL Server database engine")

This page describes how Cloud SQL works with MySQL users. MySQL user accounts provide security by controlling access to MySQL databases.

For complete documentation about users in MySQL, see [Access Control and Account Management](https://dev.mysql.com/doc/refman/8.4/en/access-control.html) in the MySQL documentation. For information about creating and managing Cloud SQL users in Cloud SQL, see [Create and manage users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users).

## Why you need MySQL user accounts

MySQL user accounts enable you to log in to and administer your Cloud SQL instance. User accounts are also required for applications to access your instance.

## Superuser restrictions

In Cloud SQL, customers cannot create or access users with superuser attributes.

Because Cloud SQL for MySQL is a managed service, it restricts access to certain system procedures and tables.

Data Manipulation Language (DML) and Data Definition Language (DDL) privileges are restricted on some schema tables.

Here's the list of MySQL 5.6 system tables in the _mysql_ schema that require write permissions:

  * `audit_log_rules_expanded`
  * `audit_log_supported_ops`
  * `audit_log_rules`
  * `cloudsql_replica_index`
  * `db`
  * `event`
  * `func`
  * `heartbeat`
  * `plugin`
  * `proc`
  * `user`
  * `tables_priv`



For MySQL 5.7, here's the list:

  * `audit_log_rules_expanded`
  * `audit_log_supported_ops`
  * `audit_log_rules`
  * `cloudsql_replica_index`
  * `db`
  * `event`
  * `func`
  * `gtid_executed`
  * `heartbeat`
  * `plugin`
  * `proc`
  * `user`
  * `tables_priv`



For related information about MySQL 8.0 and MySQL 8.4, see MySQL 8.0 user privileges (cloudsqlsuperuser) and MySQL 8.4 user privileges (cloudsqlsuperuser).

## MySQL user account format

MySQL user accounts have two components: a username and a hostname. The username identifies the user, and the hostname specifies what hosts that user can connect from. The username and hostname are combined to create a user account:
    
    
    '<user_name>'@'<host_name>'
    

You can specify a specific IP address or address range for hostname, or use the percent character ("%") to leave the hostname unrestricted.

If you connect to your instance using a public IP address, you must add your client public IP address as an [Authorized Address](https://docs.cloud.google.com/sql/docs/mysql/configure-ip), even if your user's hostname is unrestricted.

User accounts are defined by _both_ the username and the hostname. For example, `'user'@'%'` is a different user account than `'user'@'localhost'`.

## Default MySQL user

Upon creation, MySQL instances have one default user account: `'root'@'%'`. You use this account to connect to and manage the database instance for the first time. The default user has all database privileges except for [SUPER](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_super) and [FILE](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_file). In Cloud SQL, you can't rename `'root'@'%'`.

The default for `root'@'%` is no password, and MySQL does not require you to use a password for `root'@'%`. However, because `root'@'%` exists on most MySQL installations, the `root'@'%` user is a common target for unauthorized access. Any person or program that gains access to your instance has almost unlimited access to, and control over, your instance and data. For this reason, we recommend you configure your `root'@'%` user with a strong password or delete this user. For help with configuring the default user account, see [Configure the default user account](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#user-root).

## System users

Cloud SQL supports the following system users:

  * `root@localhost`, `root@127.0.0.1`, `root@::1`

Used to provide the managed database service.

  * `cloudsqlreplica@%`

Used as a replication user for replicas.

  * `cloudsqlimport@localhost`, `cloudsqlimport@127.0.0.1`

Used for data imports.

  * `cloudsqlexport@localhost`, `cloudsqlexport@127.0.0.1`

Used for data exports.

  * `cloudsqloneshot`

Used for other database operations.

  * `cloudsqlapplier@localhost`

Used for replication operations in external server replica or cross major version replication.

  * `cloudsqlobservabilityadmin`

Used for database observability.

  * `cloudiamgroup@'%'`

Used for the IAM group authentication.

  * `cloudsqlreadonly`

Used to execute read-only operations on system tables.

  * `cloudsqlreplicaindex`

Used to manage secondary indexes on replicas.




You can't delete, modify, or assign database roles to these users.

## Other MySQL user accounts

You can also create other MySQL user accounts. This is a good practice because it lets you use different MySQL user accounts for different purposes.

You can create a user account with a restricted hostname, or use SQL commands to limit privileges on your user accounts.

For more information about user account names, see [Specifying Account Names](https://dev.mysql.com/doc/refman/8.4/en/account-names.html) in the MySQL documentation. To create a new MySQL user in Cloud SQL, see [Create a user](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating).

### MySQL 5.6 and 5.7 user privileges

MySQL provides fine-grained privileges you can grant or remove for a user. This lets you control what a user can do on your instance.

Users created using Cloud SQL have the same privileges as the default MySQL user. You can change their privileges by using the [`GRANT`](https://dev.mysql.com/doc/refman/8.4/en/grant.html) or [`REVOKE`](https://dev.mysql.com/doc/refman/8.4/en/revoke.html) statements.

When you use the `mysql` client to create a user, you must explicitly grant that user privileges with the [`GRANT`](https://dev.mysql.com/doc/refman/8.4/en/grant.html) statement.

For more information about the privileges supported by MySQL, see [Privileges Provided by MySQL](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html).

### MySQL 8.0 user privileges (`cloudsqlsuperuser`)

In Cloud SQL for MySQL 8.0, when you create a new user who uses built-in authentication, the user is automatically granted the `cloudsqlsuperuser` role. The `cloudsqlsuperuser` role is a Cloud SQL role that contains a number of MySQL privileges. This role gives the user all of the MySQL [static privileges](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#privileges-provided-static), except for [`SUPER`](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_super) and [`FILE`](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_file).

The `cloudsqlsuperuser` role only supports the following [dynamic privileges](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#privileges-provided-dynamic) based on MySQL 8.0 minor versions:

### MySQL 8.0.18

  * [`APPLICATION_PASSWORD_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_application-password-admin)
  * [`CONNECTION_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_connection-admin)
  * [`ROLE_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_role-admin)
  * [`SET_USER_ID`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_set-user-id)
  * [`XA_RECOVER_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_xa-recover-admin)
  * [`CLOUDSQL_SPECIAL_VARIABLES_ADMIN`](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-option-set)



### MySQL 8.0.26

  * [`APPLICATION_PASSWORD_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_application-password-admin)
  * [`CONNECTION_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_connection-admin)
  * [`ROLE_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_role-admin)
  * [`SET_USER_ID`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_set-user-id)
  * [`XA_RECOVER_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_xa-recover-admin)
  * [`CLOUDSQL_SPECIAL_VARIABLES_ADMIN`](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-option-set)
  * [`FLUSH_OPTIMIZER_COSTS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-optimizer-costs)
  * [`FLUSH_STATUS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-status)
  * [`FLUSH_TABLES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-tables)
  * [`FLUSH_USER_RESOURCES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-user-resources)
  * [`INNODB_REDO_LOG_ENABLE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_innodb-redo-log-enable)
  * [`SHOW_ROUTINE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_show-routine)



### MySQL 8.0.27

  * [`APPLICATION_PASSWORD_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_application-password-admin)
  * [`CONNECTION_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_connection-admin)
  * [`ROLE_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_role-admin)
  * [`SET_USER_ID`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_set-user-id)
  * [`XA_RECOVER_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_xa-recover-admin)
  * [`CLOUDSQL_SPECIAL_VARIABLES_ADMIN`](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-option-set)
  * [`FLUSH_OPTIMIZER_COSTS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-optimizer-costs)
  * [`FLUSH_STATUS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-status)
  * [`FLUSH_TABLES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-tables)
  * [`FLUSH_USER_RESOURCES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-user-resources)
  * [`INNODB_REDO_LOG_ENABLE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_innodb-redo-log-enable)
  * [`SHOW_ROUTINE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_show-routine)
  * [`AUTHENTICATION_POLICY_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_authentication-policy-admin)
  * [`GROUP_REPLICATION_STREAM`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_group-replication-stream)
  * [`PASSWORDLESS_USER_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_passwordless-user-admin)



### MySQL 8.0.28

  * [`APPLICATION_PASSWORD_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_application-password-admin)
  * [`CONNECTION_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_connection-admin)
  * [`ROLE_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_role-admin)
  * [`SET_USER_ID`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_set-user-id)
  * [`XA_RECOVER_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_xa-recover-admin)
  * [`CLOUDSQL_SPECIAL_VARIABLES_ADMIN`](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-option-set)
  * [`FLUSH_OPTIMIZER_COSTS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-optimizer-costs)
  * [`FLUSH_STATUS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-status)
  * [`FLUSH_TABLES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-tables)
  * [`FLUSH_USER_RESOURCES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-user-resources)
  * [`INNODB_REDO_LOG_ENABLE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_innodb-redo-log-enable)
  * [`SHOW_ROUTINE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_show-routine)
  * [`AUTHENTICATION_POLICY_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_authentication-policy-admin)
  * [`GROUP_REPLICATION_STREAM`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_group-replication-stream)
  * [`PASSWORDLESS_USER_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_passwordless-user-admin)
  * [`AUDIT_ABORT_EXEMPT`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_audit-abort-exempt)



### MySQL 8.0.29 (deprecated)

  * [`APPLICATION_PASSWORD_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_application-password-admin)
  * [`CONNECTION_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_connection-admin)
  * [`ROLE_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_role-admin)
  * [`SET_USER_ID`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_set-user-id)
  * [`XA_RECOVER_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_xa-recover-admin)
  * [`CLOUDSQL_SPECIAL_VARIABLES_ADMIN`](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-option-set)
  * [`FLUSH_OPTIMIZER_COSTS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-optimizer-costs)
  * [`FLUSH_STATUS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-status)
  * [`FLUSH_TABLES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-tables)
  * [`FLUSH_USER_RESOURCES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-user-resources)
  * [`INNODB_REDO_LOG_ENABLE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_innodb-redo-log-enable)
  * [`SHOW_ROUTINE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_show-routine)
  * [`AUTHENTICATION_POLICY_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_authentication-policy-admin)
  * [`GROUP_REPLICATION_STREAM`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_group-replication-stream)
  * [`PASSWORDLESS_USER_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_passwordless-user-admin)
  * [`AUDIT_ABORT_EXEMPT`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_audit-abort-exempt)
  * [`SENSITIVE_VARIABLES_OBSERVER`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_sensitive-variables-observer)



### MySQL 8.0.30 and later

  * [`APPLICATION_PASSWORD_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_application-password-admin)
  * [`CONNECTION_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_connection-admin)
  * [`ROLE_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_role-admin)
  * [`SET_USER_ID`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_set-user-id)
  * [`XA_RECOVER_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_xa-recover-admin)
  * [`CLOUDSQL_SPECIAL_VARIABLES_ADMIN`](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-option-set)
  * [`FLUSH_OPTIMIZER_COSTS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-optimizer-costs)
  * [`FLUSH_STATUS`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-status)
  * [`FLUSH_TABLES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-tables)
  * [`FLUSH_USER_RESOURCES`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_flush-user-resources)
  * [`INNODB_REDO_LOG_ENABLE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_innodb-redo-log-enable)
  * [`SHOW_ROUTINE`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_show-routine)
  * [`AUTHENTICATION_POLICY_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_authentication-policy-admin)
  * [`GROUP_REPLICATION_STREAM`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_group-replication-stream)
  * [`PASSWORDLESS_USER_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_passwordless-user-admin)
  * [`AUDIT_ABORT_EXEMPT`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_audit-abort-exempt)
  * [`SENSITIVE_VARIABLES_OBSERVER`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_sensitive-variables-observer)
  * [`FIREWALL_EXEMPT`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_firewall-exempt)
  * [`RESOURCE_GROUP_ADMIN`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_resource-group-admin)
  * [`RESOURCE_GROUP_USER`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_resource-group-user)



The `cloudsqlsuperuser` role doesn't support any Data Definition Language (DDL) operations on the `mysql` system database.

To see a complete list of privileges granted to the `cloudsqlsuperuser` role, execute the [`SHOW GRANTS`](https://dev.mysql.com/doc/refman/8.0/en/show-grants.html) statement in the `mysql` client:
    
    
    SHOW GRANTS FOR 'cloudsqlsuperuser'
    

### MySQL 8.4 user privileges (`cloudsqlsuperuser`)

Similar to Cloud SQL for MySQL 8.0, in Cloud SQL for MySQL 8.4, when you create a new user who uses built-in authentication, the user is automatically granted the `cloudsqlsuperuser` role.

In MySQL 8.4, the`cloudsqlsuperuser` role has the same privileges as MySQL 8.0.x. However, MySQL 8.4 has the following main differences with MySQL 8.0.x:

  * Removes the [`SET_USER_ID`](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_set-user-id) privilege and replaces it with the newly introduced [`ALLOW_NONEXISTENT_DEFINER`](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_allow-nonexistent-definer) and [`SET_ANY_DEFINER`](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_set-any-definer) privileges.
  * Grants [`FLUSH_PRIVILEGES`](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_flush-privileges) as a subset of the [`RELOAD`](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_reload) privilege. This grant isn't a replacement for the `RELOAD` privilege, and the `RELOAD` privilege is still granted for backwards compatibility.
  * Grants the new [`OPTIMIZE_LOCAL_TABLE`](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_optimize-local-table) privilege.



In addition, Cloud SQL for MySQL 8.4 doesn't grant the [`TRANSACTION_GTID_TAG`](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_transaction-gtid-tag) or [`TELEMETRY_LOG_ADMIN`](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html#priv_telemetry-log-admin) privileges introduced in MySQL 8.4.

### MySQL 9.7 user privileges (`cloudsqlsuperuser`)

In Cloud SQL for MySQL 9.7, similar to Cloud SQL for MySQL 8.0 and Cloud SQL for MySQL 8.4, when you create a new user who uses built-in authentication, the user is automatically granted the `cloudsqlsuperuser` role.

In MySQL 9.7, the `cloudsqlsuperuser` role has the same privileges as it does in MySQL 8.4. However, MySQL 9.7 adds the following privilege to `cloudsqlsuperuser`:

  * [`CREATE_SPATIAL_REFERENCE_SYSTEM`](https://dev.mysql.com/doc/refman/9.7/en/privileges-provided.html#priv_create-spatial-reference-system)



## MySQL roles

If you're using MySQL 8.0 or later, then you can create custom roles to help you organize and assign database privileges to your MySQL users. You can use roles to provide initial database privileges for users when you create a Cloud SQL instance.

For more information about creating and using roles in MySQL, see [Using roles](https://dev.mysql.com/doc/refman/8.4/en/roles.html).

When you create a built-in MySQL user in Cloud SQL for MySQL and don't assign any database roles, the built-in MySQL user is granted the `cloudsqlsuperuser` role automatically. Alternatively, you can create a new MySQL user and assign a different custom role or roles with more fine-grained privileges. For more information about assigning roles to users in Cloud SQL for MySQL, see [Manage users with built-in authentication](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users).

### Mandatory roles for MySQL users

In MySQL, [mandatory roles](https://dev.mysql.com/doc/refman/9.7/en/server-system-variables.html#sysvar_mandatory_roles) are roles that you want to grant to every database user. However, the roles don't take effect unless the roles are activated. You can activate mandatory roles by enabling either the [`activate_all_roles_on_login`](https://dev.mysql.com/doc/refman/9.7/en/server-system-variables.html#sysvar_activate_all_roles_on_login) flag or the [`activate_mandatory_roles`](https://dev.mysql.com/doc/refman/9.7/en/server-system-variables.html#sysvar_activate_mandatory_roles) flag.

In Cloud SQL for MySQL 9.7, the `activate_mandatory_roles` flag is set to `on` by default.

**Caution:** Because the `activate_mandatory_roles` flag is set to `on` by default in MySQL 9.7, any roles that you specify in the [`mandatory_roles`](https://dev.mysql.com/doc/refman/9.7/en/server-system-variables.html#sysvar_mandatory_roles) flag are activated automatically.

For more information, see [Activating roles](https://dev.mysql.com/doc/refman/9.7/en/roles.html#roles-activating).

## IAM users and database roles

When you create an IAM user account in Cloud SQL for MySQL and don't assign any database roles, the user isn't granted any database roles automatically.

You can grant the `cloudsqlsuperuser` role and custom database roles to IAM users, service accounts or groups by assigning those database roles when you create or update the IAM accounts on the instance.

For more information about granting roles to IAM users, see [Assign database roles while adding an IAM account to an instance](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#add-db-roles).

## What's next

  * [Configure the `root` user account](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#user-root) for your instance.
  * [Create and manage users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users).
  * [Create and manage databases](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases).
  * See the [MySQL documentation about MySQL users](https://dev.mysql.com/doc/refman/8.4/en/access-control.html).
  * See the [MySQL documentation about privileges provided by MySQL](https://dev.mysql.com/doc/refman/8.4/en/privileges-provided.html).
  * Learn about [options for connecting to your instance](https://docs.cloud.google.com/sql/docs/mysql/external-connection-methods).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
