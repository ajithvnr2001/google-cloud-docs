---
url: https://docs.cloud.google.com/database-migration/docs/mysql/configure-src-connection-aws/
title: Configure network connectivity for Amazon Aurora and Amazon RDS sources \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:15.155156+00:00
---

# Configure network connectivity for Amazon Aurora and Amazon RDS sources  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/configure-src-connection-aws/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Configure network connectivity for Amazon Aurora and Amazon RDS sources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure network connectivity for Amazon Aurora and Amazon RDS sources for homogeneous migrations to Cloud SQL for MySQL migrations with Database Migration Service. There are several methods you can use:

  * Private IP connectivity with Private Service Connect interfaces

  * Private IP connectivity with Virtual Private Cloud peering

  * Public IP allowlist




## Configure Private Service Connect interfaces

To use private connectivity with Private Service Connect interfaces for Amazon RDS or Amazon Aurora sources, follow these steps:

  1. Set up direct connectivity with Cloud VPN from Google Cloud to your source VPC. 

Depending on your network architecture, you might need to set up additional VPN gateways in your system. For more information, see [ Create HA VPN connections between Google Cloud and AWS](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws) in the Cloud VPN documentation. 

  2. Create a destination Cloud SQL instance enabled for Private Service Connect. See [ Create a Private Service Connect-enabled instance](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#create-cloud-sql-instance-psc-enabled-2) in the Cloud SQL documentation. 
  3. Configure Private Service Connect for outbound connectivity on your instance. At a high level, this process involves: 
     1. Creating a network attachment in the VPC network where you set up your Cloud VPN. Note that the subnet range reserved for the network attachment must be within RFC 1918 range. 
     2. Assigning the network attachment to your destination Cloud SQL for MySQL instance. 

For the full process, see [ Configure outbound connectivity](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#configure-outbound-connectivity) in the Cloud SQL documentation. 

  4. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/mysql/create-connection-profiles) use the private IP address of your source database instance. 
  5. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/about-migration-jobs) select **PSC interface** for your connectivity method. 



## Configure VPC peering

To use private connectivity with Virtual Private Cloud peering for Amazon RDS or Amazon Aurora sources, follow these steps:

  1. Set up direct connectivity with Cloud VPN from Google Cloud to your source VPC. 

Depending on your network architecture, you might need to set up additional VPN gateways in your system. For more information, see [ Create HA VPN connections between Google Cloud and AWS](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws) in the Cloud VPN documentation. 

Ensure the Virtual Private Cloud network is configured for private services access. For more information, see [ Configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). 

  2. Make sure your destination Cloud SQL instance is configured with a private IP and Private Service Access (PSA). For more information, see [ Use private IP](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#configure_an_instance_to_use_private_ip) in the Cloud SQL documentation. 
  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/mysql/create-connection-profiles) use the private IP address of your source database instance. 
  4. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/about-migration-jobs) select **VPC Peering** for your connectivity method. 



## Configure IP allowlist connectivity

To use the public IP allowlist connectivity method, follow these steps:

  1. Enable public IP for your destination Cloud SQL instance. [ Enable public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip) in the Cloud SQL documentation. 

If you are migrating to a new destination instance, make sure to create the destination with a public IP enabled. 

  2. In the AWS Management Console, perform the following steps: 
     1. Ensure that your source Amazon RDS database is configured for public IP connections. 
     2. Identify the endpoint name and port number. You need to enter these values when you create the connection profile. 
  3. Create a security group that allows traffic from the public IP of your destination Cloud SQL instance to your Amazon RDS or Amazon Aurora VPC. See [ Provide access to your DB instance in your VPC by creating a security group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SettingUp.html#CHAP_SettingUp.SecurityGroup). 

  4. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/mysql/create-connection-profiles) use endpoint name for the source database IP. 
  5. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/about-migration-jobs) select **IP allowlist** for your connectivity method. 



## What's next

  * To learn more about database network connectivity in Database Migration Service, see [ Networking methods overview](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods).

  * To get a complete, step-by-step migration walkthrough, see [ Get started with Cloud SQL for MySQL migrations](https://docs.cloud.google.com/database-migration/docs/mysql/get-started-with-mysql-migrations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
