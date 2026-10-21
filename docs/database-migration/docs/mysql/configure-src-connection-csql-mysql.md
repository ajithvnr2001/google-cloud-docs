---
url: https://docs.cloud.google.com/database-migration/docs/mysql/configure-src-connection-csql-mysql/
title: Configure network connectivity for Cloud SQL for MySQL sources \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:54.301285+00:00
---

# Configure network connectivity for Cloud SQL for MySQL sources  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/configure-src-connection-csql-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Configure network connectivity for Cloud SQL for MySQL sources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure network connectivity for Cloud SQL for MySQL sources for homogeneous migrations to Cloud SQL for MySQL migrations with Database Migration Service. There are two different methods you can use:

  * Private IP connectivity with Private Service Connect interfaces

  * Private IP connectivity with specialized Virtual Private Cloud peering

  * Public IP allowlist




For homogeneous migrations between two Cloud SQL for MySQL instances with Database Migration Service, we don't recommend using the reverse-SSH tunnel connectivity method.

## Configure Private Service Connect interfaces

This connectivity method lets you connect to the private IP of your source database without consuming [ VPC peering quota](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering). Private Service Connect interfaces are only available when you [ migrate to an existing instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance).

To use private connectivity with Private Service Connect interfaces, follow these steps:

  1. In your project, ensure you have a Virtual Private Cloud network with [ Virtual Private Cloud network with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). 

This is the network that you peer with Database Migration Service and your source database server. You need to have enough space to allocate IP ranges for both components. 

  2. Make sure your source Cloud SQL instance is configured with a private IP and Private Service Access (PSA) with the VPC network described in the previous step. For more information, see [ Use private IP](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#configure_an_instance_to_use_private_ip) in the Cloud SQL documentation. 
  3. Create a destination Cloud SQL instance enabled for Private Service Connect. See [ Create a Private Service Connect-enabled instance](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#create-cloud-sql-instance-psc-enabled-2) in the Cloud SQL documentation. 
  4. Configure Private Service Connect for outbound connectivity on your destination instance. At a high level, this process involves: 
     1. Creating a network attachment in the VPC network where your source instance has a private IP address with PSA. Note that the subnet range reserved for the network attachment must be within RFC 1918 range. 
     2. Assigning the network attachment to your destination Cloud SQL for MySQL instance. 

For the full process, see [ Configure outbound connectivity](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#configure-outbound-connectivity) in the Cloud SQL documentation. 

  5. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/mysql/create-connection-profiles) use the private IP address of your source Cloud SQL for MySQL instance. 
  6. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/about-migration-jobs) select **PSC interface** for your connectivity method. 



## Configure specialized VPC peering

Private connectivity with Cloud SQL for MySQL sources for heterogeneous migrations uses Virtual Private Cloud (VPC) peering to create a connection between Database Migration Service and your source database over VPC networks in Google Cloud. Transitive peering isn't supported, so for this connectivity method to work, you need to set up a reverse proxy Virtual Machine (VM) in your Virtual Private Cloud network.

To use private connectivity with VPC peering, follow these steps:

  1. In your project, ensure you have a Virtual Private Cloud network with [ Virtual Private Cloud network with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). 

This is the network that you peer with Database Migration Service and your source database server. You need to have enough space to allocate IP ranges for both components. 

  2. Make sure your source Cloud SQL instance is configured with a private IP and Private Service Access (PSA) with the VPC network described in the previous step. For more information, see [ Use private IP](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#configure_an_instance_to_use_private_ip) in the Cloud SQL documentation. 
  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/mysql/create-connection-profiles), do the following: 
     1. In the **Define connection details** section, enter the private IP of your source Cloud SQL instance. 

You can view your instance's **private IP address** when you [ view instance summary information](https://docs.cloud.google.com/sql/docs/mysql/instance-info). 

     2. In the **Define connectivity method** section, select **Private connectivity**. 
     3. From the drop-down menu, select the private connectivity configuration you created in the previous step. 



## Configure IP allowlist connectivity

To configure IP allowlist connectivity for Cloud SQL for MySQL sources, follow these steps:

  1. Enable public IP for your source Cloud SQL instance and add the outbound public IP of your destination instance to the list of authorized networks. For more information, see [ Enable public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) in the Cloud SQL documentation. 

If you are migrating to a new destination instance, make sure to create the destination with a public IP enabled. 

  2. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/mysql/create-connection-profiles) use the public IP address of your source instance. 
  3. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/about-migration-jobs) select **IP allowlist** for your connectivity method. 



## What's next

  * To learn more about database network connectivity in Database Migration Service, see [ Networking methods overview](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods).

  * To get a complete, step-by-step migration walkthrough, see [ Get started with Cloud SQL for MySQL migrations](https://docs.cloud.google.com/database-migration/docs/mysql/get-started-with-mysql-migrations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
