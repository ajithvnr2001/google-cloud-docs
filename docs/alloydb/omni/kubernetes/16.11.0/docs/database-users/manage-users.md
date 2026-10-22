---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/database-users/manage-users/
title: Manage AlloyDB Omni users and roles \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 16.11.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:32.895749+00:00
---

# Manage AlloyDB Omni users and roles  |  AlloyDB Omni using the container orchestrator: 16.11.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/database-users/manage-users/

This page documents AlloyDB Omni version **16.11.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/overview)



Send feedback 

#  Manage AlloyDB Omni users and roles Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.11.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/database-users/manage-users)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/database-users/manage-users)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/database-users/manage-users)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/database-users/manage-users)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/database-users/manage-users)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/database-users/manage-users)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/database-users/manage-users)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/database-users/manage-users)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/database-users/manage-users)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/database-users/manage-users)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/database-users/manage-users)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/database-users/manage-users)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/database-users/manage-users)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/database-users/manage-users)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/database-users/manage-users)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/database-users/manage-users)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/database-users/manage-users)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/database-users/manage-users)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/database-users/manage-users)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/database-users/manage-users)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/database-users/manage-users)

This page describes how to create and manage AlloyDB Omni users and roles. 

In addition to the default users and roles that come with PostgreSQL, you can create other PostgreSQL users or roles. These users have the same set of privileges as the `postgres` user: `CREATE ROLE`, `CREATEDB`, and `LOGIN`. For more information about these privileges, see [`CREATE ROLE`](https://www.postgresql.org/docs/16/sql-createrole.html).

You can change the privileges of any user by using the [`ALTER ROLE`](https://www.postgresql.org/docs/16/sql-alterrole.html) command. If you create a new user with the `psql` client, you can choose to associate it with a different role, or assign different privileges.

## Before you begin

To use PostgreSQL commands to manage users on a cluster, you need the following:

  * Access to the `psql` client
  * Access to the `postgres` database user, or another user with the appropriate administrative privileges



## Create a database user

To create a database user that authenticates with the database directly using a username and password—also known as _built-in authentication_ — use the following command:
    
    
      CREATE USER USERNAME WITH PASSWORD 'PASSWORD';
    

Replace the following:

  * `USERNAME`: The user role's username.

  * `PASSWORD`: The new password to assign to the user role.




For more information about how to create and define database users, see [`CREATE USER`](https://www.postgresql.org/docs/16/sql-createuser.html).

After you create a user or a role, you can change its privileges by using the [`ALTER ROLE`](https://www.postgresql.org/docs/16/sql-alterrole.html) command in the `psql` client.

## Grant roles to a database user

To grant roles to a database user, use the following command:
    
    
    GRANT ROLE to USERNAME;
    

Replace the following:

  * `ROLE`: The role to grant to the database user.

  * `PASSWORD`: The new password to assign to the user role.




To give a user superuser privileges, grant that user the `alloydbsuperuser` role.

## Change the password of a database user

To set a new password for a standard PostgreSQL database user, use the following command:
    
    
    ALTER USER USERNAME WITH PASSWORD 'PASSWORD';
    

Replace the following:

  * `USERNAME`: The database user's username.

  * `PASSWORD`: The new password to assign to the user role.




For more information about changing a user's password, see [`ALTER ROLE`](https://www.postgresql.org/docs/16/sql-alterrole.html).

## Revoke a role from a database user

To revoke a previously granted privilege from one or more roles, or to revoke a user's membership in a role, use the following command:
    
    
      REVOKE ROLE FROM USERNAME;
    

To remove a user's superuser privileges, revoke the `alloydbsuperuser` role from that user.

## View a list of database users

To view a table of all database users and their group memberships, use the following command:
    
    
      \du
    

## Delete a database user

Before deleting a user, you must drop all the objects it owns or reassign their ownership, and revoke any privileges the role has been granted on other objects.

To delete a user, use the following command:
    
    
      DROP ROLE USERNAME;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
