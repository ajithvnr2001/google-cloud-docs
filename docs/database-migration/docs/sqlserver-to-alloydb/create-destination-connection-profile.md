---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-destination-connection-profile/
title: Create a destination connection profile \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:21.481925+00:00
---

# Create a destination connection profile  |  Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-destination-connection-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for AlloyDB ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

#  Create a destination connection profile Stay organized with collections  Save and categorize content based on your preferences. 

The connection details you need to provide can differ depending on what destination connectivity you use. This page describes how to create destination connection profiles for each available connectivity method:

  * Destination connection profile for public IP connectivity

  * Destination connection profile for private IP connectivity




## Before you begin

Before you create a destination connection profile, make sure you do the following:

  1. Consider in which region you want to create the destination connection profile.

Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region.

  2. [ Configure your destination database and create a dedicated migration user account](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-destination-database).

  3. [ Choose and configure the destination connectivity method](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-destination).

Destination database connections are always encrypted by Database Migration Service. You don't need to configure additional certificates for those connections.




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

## For public IP connectivity

To create a destination connection profile that uses the [ public IP connectivity method](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-destination#public-ip), follow these steps:

  1. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click **Create profile**.
  3. On the **Create a connection profile** page, from the **Profile role** list, select **Destination**. 
  4. From the **Database engine** list, select **AlloyDB for PostgreSQL**. 
  5. In the **Specify connection profile details** section, provide the connection profile name, identifier, and region. 
  6. In the **Connection details** section, do the following: 
     1. From the **Cluster ID** drop-down menu, select your AlloyDB for PostgreSQL destination cluster identifier. 
     2. In the **Hostname and IP** field, enter your destination instance's public IP address. 
     3. In the remaining fields, enter the port number and the login details for the dedicated migration user account (name and password). 
  7. In the **Define connectivity method** section, from the **Connectivity method** drop-down menu, select **Public IP**. 
  8. (Optional) In the **Test connection profile** section, click **Run test**. 

Database Migration Service performs a quick check to verify that the connection details you supplied are sufficient to reach your data. 

  9. Click **Create** at the bottom of the page. 

The **Connection profiles** page appears, and the newly created connection profile is displayed.




## For private IP connectivity

To create a destination connection profile that uses the [ private IP with Private Service Connect connectivity method](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-destination#private-ip), follow these steps:

  1. In the Google Cloud console, go to the **Connection profiles** page. 

[ Go to Connection profiles](https://console.cloud.google.com/dbmigration/connection-profiles)

  2. Click **Create profile**.
  3. On the **Create a connection profile** page, from the **Profile role** list, select **Destination**. 
  4. From the **Database engine** list, select **AlloyDB for PostgreSQL**. 
  5. In the **Define connection settings** section, provide the connection profile name, identifier, and region. 
  6. In the **Connection details** section, do the following: 
     1. From the **Cluster ID** drop-down menu, select your AlloyDB for PostgreSQL destination cluster identifier. 
     2. Use the **Hostname and IP** field to enter one of the following values: 
        * **For psc-enabled clusters** : Use the [ DNS name configured for your cluster](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect#dns_names_and_records). If your cluster only has a private IP configured, the **Hostname and IP** field is automatically populated with the required DNS name. If your cluster has both the public and private IP addresses assigned, click the **Hostname and IP** field and select the DNS record from the menu. 
        * **For non-psc-enabled clusters** : Enter the private IP assigned for your destination cluster. 
     3. In the remaining fields, enter the port number and the login details for the dedicated migration user account (name and password). 
  7. In the **Define connectivity method** section, do the following: 
     1. From the **Connectivity method** drop-down menu, select **Private IP**. 
     2. **For non-psc-enabled clusters** : From the **Service attachment name** select the service attachment [ you created for the destination cluster Private Service Connect connection](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-dst-connection-private-ip#non-psc). 
  8. (Optional) In the **Test connection profile** section, click **Run test**. 

Database Migration Service performs a quick check to verify that the connection details you supplied are sufficient to reach your data. 

  9. Click **Create** at the bottom of the page. 

The **Connection profiles** page appears, and the newly created connection profile is displayed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
