---
url: https://docs.cloud.google.com/alloydb/docs/database-users/manage-roles/
title: Manage PostgreSQL users with built-in authentication \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:08.004132+00:00
---

# Manage PostgreSQL users with built-in authentication  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/database-users/manage-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Manage PostgreSQL users with built-in authentication Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create, manage, and remove both PostgreSQL and AlloyDB for PostgreSQL roles, users, and groups using the password-based PostgreSQL built-in authentication methods.

## Create PostgreSQL users in AlloyDB

When you create PostgreSQL users, they only start with the `LOGIN` privilege. For more information about these privileges, see [`CREATE USER`](https://www.postgresql.org/docs/17/sql-createuser.html).

You can change the privileges of any user by using the [`ALTER ROLE`](https://www.postgresql.org/docs/17/sql-alterrole.html) command. If you create a new user with the `psql` client, you can choose to associate it with a different role, or assign different privileges.

## Manage users

You can create and manage AlloyDB users with the Google Cloud CLI, or by using PostgreSQL commands. The following sections demonstrate common user management tasks using either method.

### Before you begin

To use PostgreSQL commands to manage users on a cluster, you need the following:

  * Access to [the `psql` client](https://docs.cloud.google.com/alloydb/docs/connect-psql)
  * Access to `postgres` database user, or another user role with the appropriate administrative privileges



To use the Google Cloud console or Google Cloud CLI to manage users on a cluster, that cluster must have a primary instance. If your cluster doesn't have a primary instance, then you must [create one](https://docs.cloud.google.com/alloydb/docs/instance-primary-create) before you can manage users.

### Create a database user

To create a database user that authenticates with the database directly using a username and password, also known as _built-in authentication_ , follow the steps in this section.

To instead create a database user that uses Identity and Access Management (IAM) to authenticate, see [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth).

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of the cluster where you want to add a user.

  3. Click **Users**.

  4. Click **Add user account**.

  5. Leave **Built-in authentication** selected.

If you want to use IAM to authenticate and sign into your database clusters, you must complete additional steps to prepare your project and grant appropriate permissions to your new user. For more information, see [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth).

  6. Enter a username and password for the new user.

  7. To assign roles other than the default `alloydbsuperuser` to the user, follow these steps:

     1. Enter the name of the role in **Roles**.
     2. To add the role, press `Enter` or `Tab`.
     3. Select **x** for any role that you want to remove for that user.

For more information, see [Predefined roles](https://docs.cloud.google.com/alloydb/docs/database-users/overview#predefined-roles).

  8. Click **Add**.




### psql
    
    
    CREATE USER USERNAME WITH PASSWORD PASSWORD;
    

For more information about how to create and define database users, see [`CREATE USER`](https://www.postgresql.org/docs/17/sql-createuser.html).

After you create a user, you can change its privileges by using the [`ALTER ROLE`](https://www.postgresql.org/docs/17/sql-alterrole.html) command in the `psql` client.

### gcloud

Use the following [`gcloud alloydb users create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/create) command:
    
    
    gcloud alloydb users create USERNAME \
    --password=PASSWORD \
    --cluster=CLUSTER_ID \
    --region=REGION_ID

Replace the following variables:

  * `USERNAME`: User's username. `USERNAME` must follow the rules for SQL identifiers: without any special characters, or wrapped in double quotes. For example, `db_user_1`.

  * `PASSWORD`: User's password. To create the user without a password, omit this argument.

  * `CLUSTER_ID`: ID of the cluster to add the user to.

  * `REGION_ID`: ID of the region where the cluster resides. For example, `us-central1`.




After you create a user, you can change its privileges by using the [`gcloud alloydb users set-roles`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/set-roles) command.

Additionally, you can grant roles or superuser privileges to a user while you create it. To do this, include the `--db-roles` or `--superuser` arguments, as the following section describes.

### Grant roles to a database user

### Console

To grant roles to a database user, use `psql` or the gcloud CLI, instead of the Google Cloud console.

### psql
    
    
    GRANT ROLE to USERNAME;
    

Replace the following variables:

  * `USERNAME`: User's username.
  * `ROLE`: Role to grant the user. For example, to give the user superuser privileges, grant them `alloydbsuperuser`.

**Note:** You can't use this method to grant users the `alloydbiamuser` role. For more information, see [About database user management in AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/database-users/overview#alloydbiamuser).

### gcloud

Use the following [`gcloud alloydb users set-roles`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/set-roles) command to specify all the roles that you want the user to possess:
    
    
    gcloud alloydb users set-roles USERNAME \
    --db-roles=ROLES \
    --cluster=CLUSTER_ID \
    --region=REGION_ID

Replace the following variables:

  * `USERNAME`: User's username.

  * `ROLES`: Comma-separated list of all the roles you want the user to possess. Make sure that you list all roles, which includes existing and new roles.

To find the list of existing roles assigned to the user, run the following command:
        
        gcloud alloydb users list --cluster=CLUSTER_ID --region=REGION_ID

Replace the following variables:

    * `CLUSTER_ID`: ID of the cluster containing the user.

    * `REGION_ID`: ID of the region where the cluster resides. For example, `us-central1`.

To give a user superuser privileges, you can either manually grant that user the `alloydbsuperuser` role using `psql`, or you can run the [`gcloud alloydb users set-superuser`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/set-superuser) command with the `--superuser=true` argument:
    
    gcloud alloydb users set-superuser USERNAME \
    --superuser=true \
    --cluster=CLUSTER_ID \
    --region=REGION_ID

Replace the following variables:

    * `CLUSTER_ID`: ID of the cluster containing the user.

    * `REGION_ID`: ID of the region where the cluster resides. For example, `us-central1`.




### Change the password of a database user

To set a new password for a standard PostgreSQL database user, follow the steps in this section.

You can't change or set the password of an IAM-based user because IAM users don't use passwords to authenticate. For more information, see [Connect using an IAM account](https://docs.cloud.google.com/alloydb/docs/connect-iam).

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of the cluster that contains the database user.

  3. Click **Users**.

  4. On the row that represents the user, click more_vert **Open actions for this user**.

  5. Select **Change password**.

  6. Specify a password:

     * To set a new password for this user, type the password into the **Password** field.

     * To set no password for this user, select the **No password** checkbox.

  7. Click **OK**.




### psql
    
    
    ALTER USER USERNAME WITH PASSWORD PASSWORD;
    

For more information about how to change a user's password, see [`ALTER ROLE`](https://www.postgresql.org/docs/17/sql-alterrole.html).

### gcloud

Use the following [`gcloud alloydb users set-password`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/set-password) command:
    
    
    gcloud alloydb users set-password USERNAME \
    --password=PASSWORD \
    --cluster=CLUSTER_ID \
    --region=REGION_ID

Replace the following variables:

  * `USERNAME`: User's username.

  * `PASSWORD`: New password to assign to the user.

  * `CLUSTER_ID`: ID of the cluster that the user belongs to.

  * `REGION_ID`: ID of the region where the cluster resides. For example, `us-central1`.




### Revoke a role from a database user

### Console

To revoke roles from a user, use `psql` or the gcloud CLI, instead of the Google Cloud console.

### psql

You can revoke previously granted privileges from one or more roles or revoke a user's membership in a role, as shown:
    
    
    REVOKE ROLE FROM USERNAME;
    

To remove a user's superuser privileges, revoke the `alloydbsuperuser` role from that user.

### gcloud

To revoke a role with the Google Cloud CLI, use the following [`gcloud alloydb users set-roles`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/set-roles) command to specify all the roles that you want the user to possess, and to omit roles to revoke from the user:
    
    
    gcloud alloydb users set-roles USERNAME \
    --db-roles=ROLES \
    --cluster=CLUSTER_ID \
    --region=REGION_ID

Replace the following variables:

  * `USERNAME`: User's username.

  * `ROLES`: Comma-separated list of all the roles you want the user to possess. Make sure that you list all roles, including existing and new roles.

To find the list of existing roles assigned to the user, run the following command:
        
        gcloud alloydb users list --cluster=CLUSTER_ID --region=REGION_ID

  * `CLUSTER_ID`: ID of the cluster containing the user.

  * `REGION_ID`: ID of the region where the cluster resides. For example, `us-central1`.




To revoke superuser privileges, you can either manually remove a user's `alloydbsuperuser` role using `psql`, or you can run the [`gcloud alloydb users set-superuser`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/set-superuser) command with the `--superuser=false` argument.

### View a list of database users

**Note:** When listing users using the Google Cloud console or gcloud CLI, users or roles configured with `NOLOGIN` are filtered out of the returned list. If you temporarily disable a user using `ALTER ROLE ... NOLOGIN`, they get hidden from these control plane listings. To view all roles, [connect to your instance using `psql`](https://docs.cloud.google.com/alloydb/docs/connect-psql) and query [`pg_roles`](https://www.postgresql.org/docs/18/view-pg-roles.html) directly.

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of the cluster whose users you want to view.

  3. Click **Users**.




### psql

Use the following `\du` command to print a table of all database users, which includes their group memberships:
    
    
    \du
    

### gcloud

Use the following [`gcloud alloydb users list`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/list) command:
    
    
    gcloud alloydb users list \
    --cluster=CLUSTER_ID \
    --region=REGION_ID

Replace the following:

  * `CLUSTER_ID`: ID of the cluster containing the users.

  * `REGION_ID`: ID of the region where the cluster resides. For example, `us-central1`.




### Remove user dependencies

Before you can delete a database user, you must remove all database objects owned by that user and revoke any privileges granted to them. Otherwise, the deletion attempt fails with an error (for example, `ERROR: role "username" cannot be dropped because some objects depend on it`).

To identify and remove these dependencies, connect to your database using the `psql` client as the `postgres` user or any account with `alloydbsuperuser` role, and perform the following steps for each database in your cluster:

  1. Run the following query to list the objects, such as tables, views, schemas, and databases owned by the user you want to delete:
         
         SELECT
             n.nspname AS schema_name,
             c.relname AS object_name,
             CASE c.relkind
               WHEN 'r' THEN 'table'
               WHEN 'v' THEN 'view'
               WHEN 'm' THEN 'materialized view'
               WHEN 'i' THEN 'index'
               WHEN 'S' THEN 'sequence'
               WHEN 't' THEN 'TOAST table'
               WHEN 'f' THEN 'foreign table'
               WHEN 'p' THEN 'partitioned table'
               WHEN 'I' THEN 'partitioned index'
             END as object_type
         FROM pg_catalog.pg_class c
         JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
         WHERE pg_catalog.pg_get_userbyid(c.relowner) = 'USERNAME'
           AND n.nspname NOT IN ('pg_catalog', 'information_schema')
           AND n.nspname !~ '^pg_toast';
         

Replace `USERNAME` with the name of the user you want to delete.

  2. For the objects identified, you must change the ownership for each object.

     * To change the owner of a table or view:
           
           ALTER TABLE SCHEMA_NAME.OBJECT_NAME OWNER TO NEW_OWNER;
           

Replace the following:

       * `NEW_OWNER`: username of the user whom you want to grant ownership to.
     * To change the owner of a database:
           
           ALTER DATABASE DATABASE_NAME OWNER TO NEW_OWNER;
           

  3. Identify and revoke privileges. The user might also have privileges granted on other objects, or role memberships that prevent deletion.

     * To list role memberships for the user:
           
           WITH RECURSIVE cte AS (
           SELECT oid ,oid as member_of,1 as d,''::name as path FROM pg_roles r where r.rolname !~ '^pg_'
               UNION
               SELECT m.roleid,m.member as member_of ,d+1,path||'->'||pg_get_userbyid(cte.oid) as path
               FROM cte
               JOIN pg_auth_members m ON m.member = cte.oid where d<15
           )
           SELECT
           DISTINCT pg_get_userbyid(member_of)::varchar as USERNAME,
           pg_get_userbyid(oid)::varchar as parent_role,
           d::int as depth, substr(path::text||'->'||pg_get_userbyid(oid),3) as path
           FROM cte
           WHERE d > 1
           ORDER BY depth;
           

     * To revoke role membership:
           
           REVOKE ROLE_NAME FROM USERNAME;
           

Replace ROLE_NAME with the role membership you want to revoke.

     * To revoke privileges on a table:

       1. Grant the table owner role to the executing user:
              
              GRANT TABLE_OWNER TO EXECUTOR_USER;
              

Replace the following:

          * `TABLE_OWNER`: username or role that owns the table.
          * `EXECUTOR_USER`: username of the executing user—for example, `postgres`.
       2. Revoke privileges on the table:
              
              REVOKE ALL PRIVILEGES ON TABLE SCHEMA_NAME.TABLE_NAME FROM USERNAME;
              

Replace the following:

          * `SCHEMA_NAME`: name of the schema containing the table.
          * `TABLE_NAME`: name of the table.
          * `USERNAME`: name of the user whose privileges you want to revoke.



### Delete a database user

Before you delete a user, you must drop or reassign all the objects they own, and revoke any privileges the user has been granted on other objects. For details, see Remove user dependencies.

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of the cluster that contains the user.

  3. Click **Users**.

  4. On the row that represents the user, click more_vert **Open actions for this user**.

  5. Select **Remove**.

  6. In the **Remove user account?** dialog, click **Remove**.




### psql

Use the following:
    
    
    DROP ROLE USERNAME;
    

### gcloud

Use the following [`gcloud alloydb users delete`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/delete) command:
    
    
    gcloud alloydb users delete USERNAME \
    --cluster=CLUSTER_ID \
    --region=REGION_ID

Replace the following:

  * `USERNAME`: User's username.

  * `CLUSTER_ID`: ID of the cluster that the user belongs to.

  * `REGION_ID`: ID of the region where the cluster resides. For example, `us-central1`.




## What's next

  * [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
