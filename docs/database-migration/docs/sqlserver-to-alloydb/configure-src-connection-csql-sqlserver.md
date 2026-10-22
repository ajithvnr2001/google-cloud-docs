---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-src-connection-csql-sqlserver/
title: Configure network connectivity to Cloud SQL for SQL Server sources \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:57.456299+00:00
---

# Configure network connectivity to Cloud SQL for SQL Server sources  |  Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-src-connection-csql-sqlserver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for AlloyDB ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

#  Configure network connectivity to Cloud SQL for SQL Server sources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure network connectivity to Cloud SQL for SQL Server sources for heterogeneous SQL Server to AlloyDB for PostgreSQL migrations with Database Migration Service.

There are several methods you can use to configure the necessary network connectivity for migrations from Cloud SQL for SQL Server sources:

  * Public IP allowlist

  * Private IP connectivity with Private Service Connect interfaces




For Cloud SQL sources, it is possible to configure connectivity over a forward-SSH tunnel, but we don't recommend this method. If you want to use a connection over private networks, use the _Private IP connectivity with Private Service Connect interfaces_ method. To learn more about source database network connectivity, see [ Source networking methods overview](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-source).

## Configure IP allowlist connectivity

To configure IP allowlist connectivity for Cloud SQL for SQL Server sources, follow these steps:

  1. Enable public IP for your source Cloud SQL for SQL Server instance and add Database Migration Service public IP ranges to the list of authorized networks. Make sure authorize Database Migration Service public IP addresses for the region where you use Database Migration Service. 

For more information, see the following pages:

     * [ Enable public IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip#add) in the Cloud SQL documentation. 
     * [ List of Database Migration Service public IP addresses](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/ip-allowlists-and-regions). 
  2. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), do the following: 
     1. In the **Define connection details** section, enter your Cloud SQL instance public IP. 
     2. In the **Define connectivity method** section, select **IP allowlist**. 



## Configure connectivity over a forward-SSH tunnel

Forward-SSH tunnels work well if you want to create a connection that is more secure than a public IP connection, but your source private IP can't be reached directly from the Google Cloud network to create a Virtual Private Cloud peering connection. Cloud SQL for SQL Server sources reside within Google Cloud networks, so if you want to use a private connection, we recommend that you  configure private connectivity for your source instead.

If you can't use Virtual Private Cloud peering, consider using the  IP allowlist connectivity method. We don't recommend forward-SSH tunnels for Cloud SQL for SQL Server source connectivity. Adding an SSH server to your architecture can increase the complexity of your migration configuration, but in the case of Cloud SQL for SQL Server sources it doesn't increase security. You still need to expose the SSH server to the internet, but can't secure it with the [ authorized networks feature](https://docs.cloud.google.com/alloydb/docs/connect-public-ip#update-network) like you can if you set up Cloud SQL for SQL Server for public IP connectivity.

## Configure private connectivity with Private Service Connect interfaces

This connectivity method lets you connect to the private IP of your source database without consuming [ VPC peering quota](https://docs.cloud.google.com/vpc/docs/vpc-peering#peering-limits). Private Service Connect interfaces are the recommended method for private IP connectivity.

To get the permissions that you need to configure Private Service Connect interfaces ask your administrator to grant the required IAM roles on your project for the following [ accounts involved in the migration process](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/access-control)

  * User account that performs the migration: 
    * To create and manage network attachments: [ Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) 
    * To create and manage private connectivity configurations: [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * If you need to create a network attachment or its underlying subnetwork in a different project than Database Migration Service (for example, if you use a Shared VPC host project), then you need to grant the following role to the **Database Migration Service service account** (`service-PROJECT_NUMBER@gcp-sa-datamigration.iam.gserviceaccount.com`): [ Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) 




For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to perform homogeneous SQL Server migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform homogeneous SQL Server migrations with Database Migration Service: 

  * User account that performs the migration: 
    * `datamigration.*`
    * `compute.networkAttachments.create`
    * `compute.networkAttachments.get`
    * `compute.networkAttachments.list`
    * `compute.networkAttachments.update`
    * `compute.networkAttachments.delete`
  * Database Migration Service service account: 
    * `compute.networkAttachments.get`
    * `compute.networkAttachments.update`
    * `compute.subnetworks.get`
    * `compute.subnetworks.list`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

To use Private Service Connect interface connectivity, do the following:

  1. Ensure your source Cloud SQL instance has a private IP enabled.

When you enable a private IP for a Cloud SQL instance, you select a VPC network to peer with. Make sure you choose the network where you later intend to create the network attachment. You can't later disable private IP for the Cloud SQL instance. For more information, see [ Enable private IP for Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip). 

  2. Create a network attachment in the VPC where your source resides. Follow these steps: 
     1. In the Google Cloud console, go to the **Network attachments** page. 

[ Go to Network attachments](https://console.cloud.google.com/net-services/psc/list/networkAttachments)

     2. Click **Create network attachment**.
     3. Enter a name for the attachment.
     4. From the **Network** menu, select the VPC where your source resides. 
     5. For the region, use the same region where you plan to create the destination database. 

Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region. 

     6. From the **Subnetwork** menu, select a subnet where you have at least 6 free usable IP addresses for Database Migration Service (that is, a `/29` range). 
     7. In **Connection preference** select **Accept connections for selected projects**. 

Database Migration Service automatically adds the producer project to the **Accepted projects** list when you later [ create the private connectivity configuration](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-private-connectivity-configuration#create-psci-config). 

**Caution:** The **Automatically accept connections for all projects** option is less secure because it allows any service to obtain IP addresses from your subnet. We don't recommend using this option. 
     8. Don't add **Accepted projects** or **Rejected projects**.
     9. Click **Create network attachment**.


* In Database Migration Service, [ create a private connectivity configuration for Private Service Connect interfaces](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-private-connectivity-configuration#create-psci-config). 
* At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), do the following: 

  1. In the **Define connection details** section, enter the private IP of your source Cloud SQL instance. 

You can view your instance's **private IP address** when you [ view instance summary information](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info). 

  2. In the **Define connectivity method** section, select **Private connectivity**. 
  3. From the drop-down menu, select the private connectivity configuration you created in the previous step. 



## Configure private connectivity with VPC peering

Private connectivity with Cloud SQL for SQL Server sources for heterogeneous migrations uses Virtual Private Cloud (VPC) peering to create a connection between Database Migration Service and your source database over VPC networks in Google Cloud. Transitive peering isn't supported, so for this connectivity method to work, you need to set up a reverse proxy Virtual Machine (VM) in your Virtual Private Cloud network.

To use private connectivity with VPC peering, follow these steps:

  1. In your project, ensure you have a Virtual Private Cloud network with [ Virtual Private Cloud network with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). 

This is the network that you peer with Database Migration Service and your source database server. You need to have enough space to allocate IP ranges for both components. 

  2. Ensure your source Cloud SQL for SQL Server instance has a private IP enabled.

When you enable a private IP for a Cloud SQL for SQL Server instance, you select a VPC network to peer with. Make sure you choose the network where you later intend to create the Database Migration Service private connectivity configuration. You can't later disable private IP for the Cloud SQL instance. For more information, see [ Enable private IP for Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip). 

  3. In your Virtual Private Cloud network, create and configure a reverse proxy VM. For more information, see [ Establish private connectivity using proxies](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-src-connection-reverse-proxy). 
  4. In Database Migration Service, [ create a private connectivity configuration](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-private-connectivity-configuration) to peer with the VPC network where your Cloud SQL has the private IP assigned. 
  5. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), do the following: 
     1. In the **Define connection details** section, enter the private IP of your source Cloud SQL for SQL Server instance. 

You can view your instance's **private IP address** when you [ view instance summary information](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info). 

     2. In the **Define connectivity method** section, select **Private connectivity**. 
     3. From the drop-down menu, select the private connectivity configuration you created in the previous step. 



## What's next

  * Learn about source connection profiles. See [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile).

  * To get a complete, step-by-step migration walkthrough, see [ SQL Server to AlloyDB for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
