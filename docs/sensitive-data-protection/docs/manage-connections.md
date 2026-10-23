---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/manage-connections/
title: Manage connections for use with discovery \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:28.281587+00:00
---

# Manage connections for use with discovery  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/manage-connections/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Manage connections for use with discovery Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to work with the connections that Sensitive Data Protection creates when you configure discovery for Cloud SQL.

## Get the service agent ID

To perform the procedures on this page, you need the ID of the service agent associated with your scan configuration. To get the service agent ID, follow these steps:

  1. Go to the discovery scan configurations list.

[Go to discovery scan configurations](https://console.cloud.google.com/security/sensitive-data-protection/landing/configuration/dataProfiles/configurations;source=7)

  2. On the toolbar, select your organization.
  3. Select your scan configuration.
  4. On the **Scan configuration details** page, copy the value of the **Service agent** field. The service agent ID is in the format of an email address.



## Grant the required IAM roles to your service agent

  1. Make sure that the service agent associated with your scan configuration has the required driver role:

     * If the scope of your discovery operation is the entire organization or a folder, make sure that the service agent has the DLP Organization Data Profiles Driver (`roles/dlp.orgdriver`) role.
     * If the scope of your discovery operation is a single project, make sure that the service agent has the DLP Project Data Profiles Driver (`roles/dlp.projectdriver`) role.
  2. Grant the service agent the Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`) role.




To get your service agent ID, see Get the service agent ID on this page.

For more information, see [Grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents#grant-role) in the Identity and Access Management documentation.

## Create a user for each Cloud SQL instance

For each instance that is in scope for discovery, create a user account that has the privileges required to profile your data.

You can use an existing user account, but you must make sure that that account has the privileges listed in this section.

### Create a user for a Cloud SQL for MySQL instance

This section describes how to create a MySQL user account for use with data profiling. Whether you create a user account or reuse an existing one, the account must have the [`caching_sha2_password` authentication plugin](https://dev.mysql.com/doc/refman/8.4/en/caching-sha2-pluggable-authentication.html).

**Note:** Sensitive Data Protection continues to support connections that are configured with a user account that uses the deprecated [`mysql_native_password authentication` plugin](https://dev.mysql.com/doc/refman/8.4/en/native-pluggable-authentication.html). No changes are required in your existing connections.

This section includes information about how to modify an existing database user account to use this authentication plugin.

**Note:** Alternatively, you can [create a user account through Google Cloud](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating). The resulting user account will have more privileges than are necessary for profiling your data.

  1. [Connect to your instance](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-cloud-shell#connect).
  2. Prepare the database user account.

     * If you want to create a database user, at the `mysql` prompt, run the following command:
           
           CREATE USER 'USERNAME'@'%' IDENTIFIED WITH caching_sha2_password BY 'PASSWORD';
           

Replace the following:

       * `USERNAME`: the username of the user account
       * `PASSWORD`: the password of the user account

For more information, see [CREATE USER Statement](https://dev.mysql.com/doc/refman/8.0/en/create-user.html) in the MySQL documentation.

     * If you want to use an existing database user account that isn't using the `caching_sha2_password` authentication plugin, use the `ALTER USER` command to change that account's authentication plugin:
           
           ALTER USER 'USERNAME'@'%' IDENTIFIED WITH caching_sha2_password BY 'PASSWORD';
           

For more information, see [ALTER USER Statement](https://dev.mysql.com/doc/refman/8.0/en/alter-user.html) in the MySQL documentation.

  3. Grant the `SELECT` and `SHOW VIEW` privileges to the user.
         
         GRANT SELECT, SHOW VIEW ON *.* TO 'USERNAME'@'%';
         

The output is similar to the following:
         
         Query OK, 0 rows affected (0.00 sec)

For more information, see [GRANT Statement](https://dev.mysql.com/doc/refman/8.0/en/grant.html) in the MySQL documentation.

  4. Optional: If you want `performance_schema.log_status` to be profiled, grant the `BACKUP_ADMIN` privilege to the user. For more information, see [MySQL Performance Schema](https://dev.mysql.com/doc/refman/8.0/en/performance-schema.html) in the MySQL documentation.
         
         GRANT BACKUP_ADMIN ON *.* TO 'USERNAME'@'%';
         

  5. In Secret Manager, [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) to store the password. Create the secret in the project that contains the Cloud SQL instance.

Note the resource name of the secret.




### Create a user for a Cloud SQL for PostgreSQL instance

For Cloud SQL for PostgreSQL instances, Sensitive Data Protection supports two types of user accounts:

  * A built-in user account created through PostgreSQL.
  * An IAM principal, specifically, the service agent associated with your scan configuration.



#### Option 1: Create a built-in user account in PostgreSQL

This section describes how to create a built-in user account through PostgreSQL.

**Note:** Alternatively, you can [create a built-in user account through Google Cloud](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating). The resulting user account will have more privileges than are necessary for profiling your data.

  1. [Connect to your instance](https://docs.cloud.google.com/sql/docs/postgres/connect-instance-cloud-shell#connect).
  2. At the `postgres` prompt, run the following command to create the user:
         
         CREATE USER USERNAME WITH PASSWORD 'PASSWORD';
         

Replace the following:

     * `USERNAME`: the username of the user account
     * `PASSWORD`: the password of the user account

The output is similar to the following:
    
    CREATE ROLE

For more information, see [CREATE USER](https://www.postgresql.org/docs/current/sql-createuser.html) in the PostgreSQL documentation.

  3. Grant read access to the tables to be profiled.

**Note:** Sensitive Data Protection can only profile tables that it has read access to. One way to grant full read access is to assign the `pg_read_all_data` role, which is available in PostgreSQL 14 or later. For earlier PostgreSQL versions, see your database documentation.
         
         GRANT pg_read_all_data TO USERNAME;
         

The output is similar to the following:
         
         GRANT ROLE

For more information, see [GRANT](https://www.postgresql.org/docs/current/sql-grant.html) in the PostgreSQL documentation.

  4. In Secret Manager, [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) to store the password. Create the secret in the project that contains the Cloud SQL instance.

Note the resource name of the secret.




#### Option 2: Add the service agent as user in the instance (PostgreSQL only)

Follow these steps only if you're configuring a Cloud SQL for PostgreSQL instance.

  1. Follow the instructions to [add an IAM service account to a database](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user) in the Cloud SQL for PostgreSQL documentation.

The service account that you provide must be the service agent associated with the scan configuration. To get the service agent ID, see Get the service agent ID on this page.

  2. In PostgreSQL, grant read access to the tables to be profiled.

**Note:** Sensitive Data Protection can only profile tables that it has read access to. One way to grant full read access is to assign the `pg_read_all_data` role, which is available in PostgreSQL 14 or later. For earlier PostgreSQL versions, see your database documentation.
         
         GRANT pg_read_all_data TO "TRUNCATED_SERVICE_AGENT_ID";
         

Replace `TRUNCATED_SERVICE_AGENT_ID` with the service agent ID without the `.gserviceaccount.com` suffix—for example, `service-1234567890@dlp-api.iam`.

The output is similar to the following:
         
         GRANT ROLE




## Provide access to your Cloud SQL instances

After you create the scan configuration, Sensitive Data Protection automatically creates default service connections for each instance in scope for discovery. Before profiling can start, you need to edit each service connection to provide the credentials for each Cloud SQL instance.

**Note:** This procedure assumes that you have the database user credentials that you want Sensitive Data Protection to use to profile your instances. You can use an existing user account, but you must make sure that that account has the privileges that Sensitive Data Protection requires. For information about the required privileges, see Create a user for each Cloud SQL instance on this page.

To update a connection, follow these steps:

  1. In the Google Cloud console, go to the **Service connections** page.

[Go to Service connections](https://console.cloud.google.com/security/sensitive-data-protection/landing/dataProfiles/connections;source=7)

Your connections are displayed in a list.

  2. For the connection that you want to update, click more_vert **Actions** > **Edit connection**.

  3. Do one of the following:

     * Provide user account credentials
     * Use the service agent as a user account (supported for Cloud SQL for PostgreSQL instances only)



After you update a connection, Sensitive Data Protection attempts to connect to the instance with the credentials that you provided. If there is an error with a connection, Sensitive Data Protection automatically retries connecting to the instance. For more information, see View connection errors on this page.

### Provide user account credentials

Enter the username and the Secret Manager resource that contains the password. The Secret Manager resource must be in the following format:
    
    
    projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/VERSION_NUMBER
    

Replace the following:

  * `PROJECT_NUMBER`: the numerical ID of your project.
  * `SECRET_NAME`: the name of the secret that contains the password.
  * `VERSION_NUMBER`: the version number of the secret; to provide the latest version, use `latest`.



### Use the service agent as a user account

This option is only available for Cloud SQL for PostgreSQL instances.

To use the service agent as the user account, select **Cloud SQL IAM database authentication**.

**Important:** If you haven't added the service agent to your instance, see Add the service agent as user in the instance (PostgreSQL only) on this page.

## Update the maximum number of concurrent connections to an instance

By default, Sensitive Data Protection uses a maximum of two concurrent connections to minimize the impact of discovery on your Cloud SQL instances. We recommend that you increase this number to an appropriate value based on the instance size and utilization.

For more information, see [Maximum concurrent connections](https://docs.cloud.google.com/sql/docs/quotas#maximum_concurrent_connections) in the Cloud SQL documentation.

To change the maximum connection limit for the discovery service, do the following:

  1. In the Google Cloud console, go to the **Service connections** page.

[Go to Service connections](https://console.cloud.google.com/security/sensitive-data-protection/landing/dataProfiles/connections;source=7)

Your connections are displayed in a list.

  2. For the connection that you want to update, click more_vert **Actions** > **Edit connection**.

  3. In the **Maximum number of connections** field, enter the new limit.

  4. Click **Done**.




## View connection errors

  1. In the Google Cloud console, go to the **Service connections** page.

[Go to Service connections](https://console.cloud.google.com/security/sensitive-data-protection/landing/dataProfiles/connections;source=7)

Your connections are listed. If a connection has an error, it is displayed with an error icon.

  2. For the connection that has an error, click more_vert **Actions** > **View errors**. The associated error messages are listed. Each message includes the name of the scan configuration that requested the connection.

  3. Resolve the error as needed. Depending on the error, the resolution can involve any of the following:

     * Editing the credentials you provided.
     * Updating the password stored in Secret Manager.
     * Logging in to the database and granting the database user the required privileges.
     * Assigning the specified IAM role to the service agent associated with the specified scan configuration.



Sensitive Data Protection automatically retries connecting to the instance. If a reconnection attempt succeeds, the error messages are cleared.

## Allow discovery for instances with no public IP address

To run discovery on a Cloud SQL instance that has no public IP address, select the **Enable private path** option for that instance. This option allows Google Cloud services to access data in a Cloud SQL instance over a private IP connection.

For more information, see the following:

  * Cloud SQL for MySQL: [Configure private IP for an existing instance](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#existing-private-instance)
  * Cloud SQL for PostgreSQL: [Configure private IP for an existing instance](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip#existing-private-instance)



## What's next

  * Learn how to [manage data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-data-profiles). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
