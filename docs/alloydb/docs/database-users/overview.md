---
url: https://docs.cloud.google.com/alloydb/docs/database-users/overview/
title: About database user management in AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:24.028136+00:00
---

# About database user management in AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/database-users/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  About database user management in AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview about how to manage database users in AlloyDB for PostgreSQL, and enable Identity and Access Management (IAM) authentication for those database users.

## How database user management works

AlloyDB shares the same concepts of roles, users, and groups as [PostgreSQL](https://www.postgresql.org/docs/17/user-manag.html). For a brief explanation, see the following descriptions:

  * **Role:** the top-level designation that describes both database users and groups of database users across a cluster. Roles provide, and restrict, access to database objects, such as tables and functions.

  * **User:** the role that's given the [`LOGIN`](https://www.postgresql.org/docs/17/role-attributes.html#ROLE-ATTRIBUTES) attribute. Users can authenticate and sign into AlloyDB database clusters.

  * **Group:** the role that's granted to one or more users. The purpose of groups is to control the privileges that many users have as a whole.




## How database authentication works

To authenticate and sign into your AlloyDB database clusters, you have two options:

  * [Built-in PostgreSQL password-based authentication](https://www.postgresql.org/docs/17/auth-password.html#AUTH-PASSWORD): to verify user identity, AlloyDB compares the provided credentials against stored, hashed passwords. The supported methods include `md5`, `scram-sha-256`, and `password`.
  * [IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth): lets database users authenticate using IAM. This provides enhanced security and centralizes access control across other Google Cloud services.



## Predefined roles

PostgreSQL provides [predefined roles](https://www.postgresql.org/docs/17/predefined-roles.html#PREDEFINED-ROLES) with various privileges. In addition to these predefined roles, AlloyDB provides several more predefined user and group roles.

The following tables lists the roles, and role privileges, that AlloyDB provides:

Role name | Privileges  
---|---  
`alloydbsuperuser` | `CREATEROLE`, `CREATEDB`, and `LOGIN`.  
`postgres` | `CREATEROLE`, `CREATEDB`, and `LOGIN`.  
`alloydbimportexport` | `CREATEROLE` and `CREATEDB`.  
`alloydbagent` | `CREATEROLE` and `CREATEDB`.  
`alloydbreplica` | `REPLICATION`  
`alloydbiamuser` | By default, this role doesn't have any privileges.  
  
The following subsections explain the uses of these roles.

### `alloydbsuperuser` group role

`alloydbsuperuser` lets you set up your database system and perform other superuser tasks. This role has the following privileges:

  * Create extensions that require superuser privileges
  * Create event triggers
  * Create replication users
  * Create replication publications and subscriptions



As a managed service, AlloyDB doesn't let you grant users the PostgreSQL `superuser` role. Instead, you can give any database user AlloyDB superuser privileges if you grant them the `alloydbsuperuser` role.

### `postgres` user role

The `postgres` user role is part of `alloydbsuperuser`. When you create an AlloyDB cluster, you can assign a password to `postgres` so that you can sign in to your system using `postgres` to perform tasks, such as to create databases or additional roles.

**Note:** If you don't set a password for `postgres` when creating a cluster, then you can't sign in to the cluster. To sign in, either set a password for `postgres` or create an additional user. For more information, see [Manage PostgreSQL users with built-in authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-roles).

### `alloydbimportexport` user role

When you create an AlloyDB cluster, AlloyDB creates `alloydbimportexport` with the minimal set of privileges it requires for import and export operations.

You have the option to create your own users to perform these operations. If you don't create a custom `alloydbimportexport` user, the system uses the default `alloydbimportexport` user for import and export operations.

`alloydbimportexport` is a system user. This means that you can't directly use `alloydbimportexport` user to sign in or perform other operations in your PostgreSQL databases.

### `alloydbagent` user role

The `alloydbagent` role is an internal AlloyDB system role. The AlloyDB service manages the role and you can't manually grant it to database accounts. This management ensures that the database and its features function correctly.

### `alloydbreplica` user role

The `alloydbreplica` role is an internal AlloyDB system role. The AlloyDB service manages the role and you can't manually grant it to database accounts. This management ensures that the database and its features function correctly.

### `alloydbiamuser` group role

Database users within the `alloydbiamuser` group authenticate with an AlloyDB instance by using IAM, instead of using built-in PostgreSQL [password-based authentication](https://www.postgresql.org/docs/17/auth-password.html#AUTH-PASSWORD).

AlloyDB doesn't let you grant `alloydbiamuser` to users using the `GRANT` PostgreSQL command or similar methods. Instead, you can use AlloyDB administrative tools to create and manage IAM-based database users. For more information, see [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth).

## What's next

  * Learn how to [manage PostgreSQL roles, users, and groups](https://docs.cloud.google.com/alloydb/docs/database-users/manage-roles) for AlloyDB using built-in authentication.

  * Learn how to [manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
