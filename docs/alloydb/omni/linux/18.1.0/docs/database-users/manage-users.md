---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/database-users/manage-users/
title: Manage AlloyDB Omni users and roles \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:09.779638+00:00
---

# Manage AlloyDB Omni users and roles  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/database-users/manage-users/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)



Send feedback 

#  Manage AlloyDB Omni users and roles Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/database-users/manage-users)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/database-users/manage-users)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/database-users/manage-users)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/database-users/manage-users)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/database-users/manage-users)

This page describes how to create and manage AlloyDB Omni users and roles. 

In addition to the default users and roles that come with PostgreSQL, you can create other PostgreSQL users or roles. These users have the same set of privileges as the `postgres` user: `CREATE ROLE`, `CREATEDB`, and `LOGIN`. For more information about these privileges, see [`CREATE ROLE`](https://www.postgresql.org/docs/18/sql-createrole.html).

You can change the privileges of any user by using the [`ALTER ROLE`](https://www.postgresql.org/docs/18/sql-alterrole.html) command. If you create a new user with the `psql` client, you can choose to associate it with a different role, or assign different privileges.

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




For more information about how to create and define database users, see [`CREATE USER`](https://www.postgresql.org/docs/18/sql-createuser.html).

After you create a user or a role, you can change its privileges by using the [`ALTER ROLE`](https://www.postgresql.org/docs/18/sql-alterrole.html) command in the `psql` client.

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




For more information about changing a user's password, see [`ALTER ROLE`](https://www.postgresql.org/docs/18/sql-alterrole.html).

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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
