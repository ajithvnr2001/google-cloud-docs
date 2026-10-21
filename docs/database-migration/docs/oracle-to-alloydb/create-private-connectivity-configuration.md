---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-private-connectivity-configuration/
title: Create a private connectivity configuration for the source database \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:34.965775+00:00
---

# Create a private connectivity configuration for the source database  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-private-connectivity-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  Create a private connectivity configuration for the source database Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a private connectivity configuration. Private connectivity configuration is a Database Migration Service construct that helps establish connectivity between Database Migration Service service network and your project's Virtual Private Cloud (VPC) network. You create private connectivity configurations to establish private connections to source Oracle databases.

You can create two types of private connectivity configurations:

  * For  Private Service Connect interfaces connectivity
  * For  VPC peering connectivity



For more information about network connectivity in Database Migration Service, see [ Network connectivity for heterogeneous Oracle migrations](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-overview) and [ Source networking methods overview](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source).

## Before you begin

  1. Ensure you have a Virtual Private Cloud network that meets the following requirements: 
     * The VPC network doesn't have any [ peering restrictions](https://docs.cloud.google.com/vpc/docs/vpc-peering#restrictions). 
     * It's the same network where your source database is peered. For more information, see the requirements section in [ Private connectivity with VPC peering](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source#private-connectivity). 
     * The VPC network has an available IP range with a CIDR block of `/29`. Database Migration Service uses this IP range to create a subnet so that it can communicate with the source database. 
  2. Enable the Database Migration Service and Compute Engine APIs. 

[ Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,datamigration.googleapis.com)




### Required roles

To get the permissions that you need to create a private connectivity configuration, ask your administrator to grant you the required IAM roles on your project:

  * To create a network attachment and manage private connectivity configurations:

    * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
    * [ Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) 
  * If you need to create a private connectivity configuration using a network attachment or its underlying subnetwork in a different project than Database Migration Service (for example, if you use a Shared VPC host project), then you need to grant the following role to the **Database Migration Service service account** (`service-PROJECT_NUMBER@gcp-sa-datamigration.iam.gserviceaccount.com`):

    * [ Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) 

Alternatively, if the Database Migration Service project is already on the network attachment's accepted projects list, then granting the [ Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) role is sufficient.




For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation. 

These predefined roles contain the permissions required to create a private connectivity configuration in Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform heterogeneous Oracle migrations with Database Migration Service: 

  * User account that creates the connectivity: 
    * `datamigration.* `
    * `compute.networks.list`
  * Database Migration Service service account: 
    * `compute.networkAttachments.get`
    * `compute.networkAttachments.update`
    * `compute.subnetworks.get`
    * `compute.subnetworks.list`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

## Create a configuration for Private Service Connect interfaces

To create a private connectivity configuration to use with Private Service Connect interfaces, follow these steps:

  1. Make sure you first create a network attachment in your VPC network. Use a subnet with at least 6 free usable IP addresses for Database Migration Service (that is, a `/29` range). For more information, see [ Private connectivity with Private Service Connect interfaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source#private-connectivity-psci). 
  2. In the Google Cloud console, go to the **Private connectivity configurations** page. 

[ Go to Private connectivity configurations](https://console.cloud.google.com/dbmigration/private-connections)

  3. Click **Create configuration**.
  4. In the **Configure private connectivity** section, enter the display name for the configuration and select the region. 

Make sure you use the same region where your project Virtual Private Cloud network resides. It must be the same region where you intend to create the migration job and connection profiles. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region. 

  5. From the **Connectivity method** menu, select **PSC interfaces**.
  6. Click **Create**.

Database Migration Service automatically adds the producer project to the **Accepted projects** list of your network attachment. 




This private connectivity configuration is now ready for use with a [ source connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-source-connection-profile).

## Create a configuration for VPC peering

To create a private connectivity configuration to use with VPC peering, follow these steps:

  1. In the Google Cloud console, go to the **Private connectivity configurations** page. 

[ Go to Private connectivity configurations](https://console.cloud.google.com/dbmigration/private-connections)

  2. Click **Create configuration**.
  3. In the **Configure private connectivity** section, enter the display name for the configuration and select the region. 

Make sure you use the same region where your project Virtual Private Cloud network resides. It must be the same region where you intend to create the migration job and connection profiles. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region. 

  4. From the **Authorized VPC network** drop-down menu, select the VPC that you want Database Migration Service to have private connectivity access. This VPC needs to be the network where your source Oracle has a private IP assigned. 
  5. In the **Allocate an IP range** field, enter an IP range with a CIDR block of `/29`. For example: `10.72.149.40/29`. 

Database Migration Service creates a subnet based on that IP range in your selected VPC. We recommend that you consult your network administrator to acquire a suitable IP range. 

For testing purposes, you can also try to generate an IP range with Virtual Private Cloud private services access interface. Note that this automatic allocation isn't intended for Database Migration Service private connectivity configurations. You need to release the automatically allocated range before you use it in Database Migration Service. Expand the following section for more information. 

#### Example: generate an IP range with private services access

You can generate an unoccupied IP range in your VPC network when you create a private services access setup. You can later release this range in the VPC configuration and use it for the Database Migration Service private connectivity configuration. 

To generate an unoccupied IP range, follow these steps:

     1. In the Google Cloud console, go to the **VPC networks** page. 

[ Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

     2. From the list of networks in your project, select the one where your source Oracle database has a private IP assigned. 
     3. Go to the **Private services access** tab and click **Allocate IP range**. 
     4. In the **Allocate an internal IP range** window, enter the following: 
        1. A display name in the **Name** field.
        2. Select the **Automatic** option and enter `29` for the prefix
        3. length.

**Result** : Your VPC network allocates an empty IP range for private services access in your project. 

     5. Check the **Internal IP range** value of the new allocated range. Note it down for later use in Database Migration Service. 
     6. Select your new IP range from the list, and click **Release**.
     7. The generated IP range is now free for use in another subnet. Enter the range you noted down in the **Allocate an IP range** field when you create the private connectivity configuration in Database Migration Service. 

  6. Click **Create**.



This private connectivity configuration is now ready for use with a [ source connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-source-connection-profile).

## What's next

  * Learn about destination database connectivity. See [ Destination database connectivity overview](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-destination).

  * To get a complete, step-by-step migration walkthrough, see [ Oracle to AlloyDB for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
