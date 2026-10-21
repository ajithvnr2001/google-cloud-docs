---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-destination/
title: Networking methods for destination database connectivity \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:47.174673+00:00
---

# Networking methods for destination database connectivity  |  Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-destination/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for AlloyDB ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

#  Networking methods for destination database connectivity Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service can connect to your destination cluster's public or private IP address. This page provides an overview of each available destination database connectivity method, as well as a recommendation section to help you choose the right solution for your migration:

  * Method comparison provides a comparison table for available destination connectivity methods.

  * Public IP connectivity describes destination connectivity over public internet.

  * Private IP connectivity explains how Database Migration Service uses Private Service Connect to connect to the private IP of your destination cluster.




After you familiarize yourself with different connectivity methods and their requirements, you can use the  decision tree diagram to pick the right solution for your scenario.

## Method comparison

Every destination connectivity method comes with different benefits and requirements. Use the following table to compare them at a glance, and then learn more details in the sections dedicated for each method.

Networking method | Advantages | Disadvantages  
---|---|---  
Public IP | 

  * The easiest connectivity method to set up.
  * Built-in security with Database Migration Service. 
  * Configuring an AlloyDB for PostgreSQL destination cluster with a public IP doesn't have any additional limitations. 

| 

  * Your traffic goes through the public internet. It might not be desireable for organizations with specific compliance policies. 

  
Private IP | 

  * The connection is fully private. All traffic travels through private networks. 
  * Uses Private Service Connect for ease of configuration and security. 

| 

  * PSC-enabled AlloyDB for PostgreSQL clusters come with certain functionality limitations. Make sure such configurations meet your requirements. See [ Private Service Connect limitations](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#limitations) in AlloyDB for PostgreSQL documentation. 
  * You can use private IP connectivity without a PSC-enabled AlloyDB for PostgreSQL instance, but such configuration requires that you use an additional bastion Virtual Machine (VM) to forward traffic between Database Migration Service and your destination. 

  
  
## Public IP connectivity

When you use the public IP connectivity method, Database Migration Service attempts to establish a connection to the public IP address of your destination AlloyDB for PostgreSQL instance. This connection is encrypted and secured by Database Migration Service.

![A networking diagram that shows a high-level public IP connectivity
      setup.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/sqlserver-to-alloydb/htm_public_ip_dst.svg) **Figure 1.** Migration networking example: public IP destination connectivity. (click to enlarge) ![A networking diagram that shows a high-level public IP connectivity
      setup.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/sqlserver-to-alloydb/htm_public_ip_dst.svg)

### Requirements for public IP connectivity

To use this connectivity method you need to ensure that your destination AlloyDB for PostgreSQL instance has a public IP address enabled. For more information, see [ Configure public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip#enable-ip) in the AlloyDB for PostgreSQL documentation.

### Configure IP allowlist connectivity

Configuring public IP connectivity is covered in [ Configure public IP connectivity](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-dst-connection-public-ip).

## Private IP connectivity

Database Migration Service uses [ Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to connect to your destination AlloyDB for PostgreSQL instance using a private IP address. With Private Service Connect, you can expose your destination database to incoming secure connections, and control who can access the database. This connection is encrypted by Database Migration Service.

Network architecture setup for Private Service Connect differs depending on whether you use a PSC-enabled or a non-PSC-enabled destination AlloyDB for PostgreSQL instance.

### For PSC-enabled AlloyDB for PostgreSQL clusters

The easiest way to use private IP connectivity for destination AlloyDB for PostgreSQL instances is to create a PSC-enabled AlloyDB for PostgreSQL instance.

![A networking diagram that shows a high-level public IP connectivity
      setup.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/sqlserver-to-alloydb/htm_private_ip_dst_psc_enabled.svg) **Figure 2.** Migration networking example: public IP source connectivity. (click to enlarge) ![A networking diagram that shows a high-level public IP connectivity
      setup.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/sqlserver-to-alloydb/htm_private_ip_dst_psc_enabled.svg)

#### Requirements for PSC-enabled clusters

To use PSC-enabled AlloyDB for PostgreSQL clusters, you need to create the destination instance with PSC enabled. The following limitations apply:

  * **Functionality limitations**

PSC-enabled AlloyDB for PostgreSQL clusters come with certain functionality limitations. Make sure such configurations meet your requirements. See [ Private Service Connect limitations](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#limitations) in AlloyDB for PostgreSQL documentation. 

  * **Creation limitations**

You can create PSC-enabled AlloyDB for PostgreSQL clusters only with `gcloud` or the AlloyDB for PostgreSQL API. 




#### Configure private connectivity for PSC-enabled clusters

Configuring private IP connectivity is covered in [ Configure private IP connectivity for PSC-enabled clusters](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-dst-connection-private-ip#psc-enabled).

### For non-PSC-enabled clusters

You can use private IP connectivity even if you can't use a PSC-enabled AlloyDB for PostgreSQL instance as your destination database. The configuration is more complex, as it requires an additional bastion virtual machine (VM) in your network to forward traffic between Database Migration Service and your destination's private IP.

![A networking diagram that shows a high-level public IP connectivity
      setup.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/sqlserver-to-alloydb/htm_private_ip_dst_non_psc_enabled.svg) **Figure 3.** Migration networking example: public IP source connectivity. (click to enlarge) ![A networking diagram that shows a high-level public IP connectivity
      setup.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/sqlserver-to-alloydb/htm_private_ip_dst_non_psc_enabled.svg)

#### Requirements for non-PSC-enabled clusters

Private IP connectivity for non-PSC-enabled AlloyDB for PostgreSQL clusters requires the following:

  * You need to have a [ Virtual Private Cloud network with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).

This is the network that you peer with your AlloyDB for PostgreSQL destination cluster.

  * Your destination AlloyDB for PostgreSQL must have private IP enabled.

  * Additionally, you need to be able to create the following network components in your project:

    * A service attachment: A network resource that exposes destination AlloyDB for PostgreSQL private IP to other services in a Google Cloud VPC network. The Google Cloud project where you create the service attachment is the _service producer_. The _service consumer_ is Database Migration Service.

    * PSC forwarding rules: A rule that routes the incoming traffic from the service attachment to the dedicated bastion VM.

    * A bastion VM: A Compute Engine VM with two network interface controllers (NICs). One is attached to the dedicated service attachment network; the other, to the network where AlloyDB for PostgreSQL is peered. The bastion VM runs a Dante SOCKS server to forward the connections.




#### Configure private connectivity for non-PSC-enabled clusters

Configuring private IP connectivity is covered in [ Configure private IP connectivity for non-PSC enabled instances](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-dst-connection-private-ip#non-psc).

## Destination network connectivity decision tree

When you are familiar with all supported destination connectivity methods and their requirements, you can follow the questions in the diagram to help you pick the right connectivity method for your scenario.

![A decision tree diagram with guiding questions to help you
        pick the right connectivity method.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/networking_destination_decision_tree.svg)**Figure 4.** Destination network connectivity decision tree. 

## What's next

  * Learn about source database connectivity. See [ Networking methods for source database connectivity](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-source).

  * To get a complete, step-by-step migration walkthrough, see [ SQL Server to AlloyDB for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
