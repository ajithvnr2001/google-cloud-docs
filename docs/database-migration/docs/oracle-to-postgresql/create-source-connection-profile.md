---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-source-connection-profile/
title: Create a source connection profile \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:03.909095+00:00
---

# Create a source connection profile  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-source-connection-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  Create a source connection profile Stay organized with collections  Save and categorize content based on your preferences. 

The connection details you need to provide can differ depending on what source connectivity you use. This page describes how to create source connection profiles for each available connectivity method:

  * Source connection profile for public IP allowlist connectivity

  * Source connection profile for forward-SSH tunnel connectivity

  * Source connection profile for private IP connectivity




## Before you begin

Before you create a source connection profile, make sure you do the following:

  1. Consider in which region you want to create the source connection profile.

Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region.

  2. [ Configure your source database and create a dedicated migration user account](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-source-database).

  3. [ Choose and configure the source connectivity method](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-source).




### Required roles

To get the permissions that you need to create a connection profile, ask your administrator to grant you the [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) IAM role on your project.

For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation.

This predefined role contains the permissions required to to create a connection profile, in Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a connection profile in Database Migration Service: 

  * `datamigration.connectionprofiles.create`
  * `datamigration.connectionprofiles.delete`
  * `datamigration.connectionprofiles.get`
  * `datamigration.connectionprofiles.getIamPolicy`
  * `datamigration.connectionprofiles.list`
  * `datamigration.connectionprofiles.setIamPolicy`
  * `datamigration.connectionprofiles.update`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

## For public IP allowlist connectivity

To create a source connection profile that uses the public IP allowlist connectivity method, follow these steps:

  1. Make sure you configure your source database server to accept connections from Database Migration Service public IP addresses for the region where you create the migration job. For more information, see [ Public IP allowlist overview](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-source#ip-allowlist). 
  2. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  3. Click **Create profile**.
  4. On the **Create a connection profile** page, from the **Profile role** list, select **Source**. 
  5. From the **Database engine** list, select **Oracle**.
  6. In the **Specify connection profile details** section, provide the connection profile name, id, and region. 
  7. In the **Define connection details** section, enter the following details: 
     1. Your source database public IP and port number, the name of the database you want to migrate, and login details for the dedicated migration user account (name and password). 
     2. In the **Service name** field, enter the service that ensures that the source Oracle database is protected and monitored. 
        * For Oracle databases, the database service is typically **ORCL**.
        * For pluggable databases, **SID** is the pluggable database name.
  8. In the **Secure your connection** section, choose the encryption type you want to use for the source database connection. 

You can use your own SSL/TLS certificates for additional network security. For more information, see [ Encrypt connections with certificates](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/encrypt-connections-with-certificates). 

**Important:** SSL/TLS encryption is supported for Oracle version 12 and later. 
  9. In the **Define connectivity method** section, select **Public IP allowlist**.
  10. Optional: In the **Test connection profile** section, click **Run test**. 

Database Migration Service performs a quick check to verify that the connection details you supplied are sufficient to reach your source database. 

  11. Click **Create**. 

The **Connection profiles** page appears, and the newly created connection profile is displayed.




## For forward-SSH tunnel connectivity

To create a source connection profile that uses the forward-SSH tunnel connectivity method, follow these steps:

  1. Make sure you set up the forward-SSH tunnel server and adjust all firewall rules in your network. For more information, see [ Forward-SSH tunnel connectivity overview](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-source#forward-ssh-tunnel). 
  2. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  3. Click **Create profile**.
  4. On the **Create a connection profile** page, from the **Profile role** list, select **Source**. 
  5. From the **Database engine** list, select **Oracle**.
  6. In the **Specify connection profile details** section, provide the connection profile name, id, and region. 
  7. In the **Define connection details** section, enter the following details: 
     1. Your source database IP and port number, the name of the database you want to migrate, and login details for the dedicated migration user account (name and password). 

The IP address should be an address that is reachable from the forward-SSH tunnel. 

     2. In the **Service name** field, enter the service that ensures that the source Oracle database is protected and monitored. 
        * For Oracle databases, the database service is typically **ORCL**.
        * For pluggable databases, **SID** is the pluggable database name.
  8. In the **Secure your connection** section, choose the encryption type you want to use for the source database connection. 

You can use your own SSL/TLS certificates for additional network security. For more information, see [ Encrypt connections with certificates](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/encrypt-connections-with-certificates). 

**Important:** SSL/TLS encryption is supported for Oracle version 12 and later. 
  9. In the **Define connectivity method** section, do the following: 
     1. From the **Connectivity method** drop-down menu, select **Forward-SSH tunnel**. 
     2. In the next sections, enter the connection details for the SSH server: IP address or hostname, port number, and login. 
     3. From the **Authentication method** drop-down menu, select how you want Database Migration Service to authenticate with your SSH server. 

You can use a password, or a unique private key. If you decide to use a private key, you can upload the file directly to Database Migration Service, or paste the key in text form in the text box. 

  10. Click **Save**. 

The connectivity details panel closes.

  11. Optional: In the **Test connection profile** section, click **Run test**. 

Database Migration Service performs a quick check to verify that the connection details you supplied are sufficient to reach your source database. 

  12. Click **Create** at the bottom of the page. 

The **Connection profiles** page appears, and the newly created connection profile is displayed.




## For private IP connectivity

There are two private IP connectivity methods you can use in source connection profiles: [ Private Service Connect interfaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-source#private-connectivity-psci) or [ Virtual Private Cloud peering](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-source#private-connectivity). Both methods require that you first [ create a private connectivity configuration](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-private-connectivity-configuration).

To create a source connection profile that uses private IP connectivity, follow these steps:

  1. Make sure you configure your network for private IP connectivity. For more information, see [ Source private connectivity overview](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-source#private-connectivity). 
  2. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  3. Click **Create profile**.
  4. On the **Create a connection profile** page, from the **Profile role** list, select **Source**. 
  5. From the **Database engine** list, select your Oracle source.
  6. In the **Specify connection profile details** section, provide the connection profile name, id, and region. 
  7. In the **Define connection details** section, enter the following details: 
     1. Your source database IP and port number, the name of the database you want to migrate, and login details for the dedicated migration user account (name and password). 

Use the IP address that is appropriate for your networking setup:

        * For sources that reside directly in the Virtual Private Cloud network that you use with the Database Migration Service private connectivity configuration, use the private IP address of your source. 
        * For sources that reside reside outside the Virtual Private Cloud network that you use with the Database Migration Service private connectivity configuration, for example scenarios that include [ a reverse proxy Virtual Machine (VM)](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy), use the private IP address of your NAT VM. 
     2. In the **Service name** field, enter the service that ensures that the source Oracle database is protected and monitored. 
        * For Oracle databases, the database service is typically **ORCL**.
        * For pluggable databases, **SID** is the pluggable database name.
  8. In the **Secure your connection** section, choose the encryption type you want to use for the source database connection. 

You can use your own SSL/TLS certificates for additional network security. For more information, see [ Encrypt connections with certificates](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/encrypt-connections-with-certificates). 

**Important:** SSL/TLS encryption is supported for Oracle version 12 and later. 
  9. In the **Define connectivity method** section, do the following: 
     1. From the **Connectivity method** drop-down menu, select **Private connectivity**. 
     2. From the **Private connectivity configuration** drop-down menu, select the name of the private connectivity configuration you created for your Private Service Connect interfaces or VPC peering. 
  10. Click **Save**. 

The connectivity details panel closes.

  11. Optional: In the **Test connection profile** section, click **Run test**. 

Database Migration Service performs a quick check to verify that the connection details you supplied are sufficient to reach your source database. 

  12. Click **Create** at the bottom of the page. 

The **Connection profiles** page appears, and the newly created connection profile is displayed. 




## What's next

  * Learn about destination connection profiles. See [ Create destination connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-destination-connection-profile).

  * To get a complete, step-by-step migration walkthrough, see [ Oracle to Cloud SQL for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
