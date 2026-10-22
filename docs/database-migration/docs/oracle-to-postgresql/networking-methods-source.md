---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-source/
title: Networking methods for source database connectivity \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:31.195629+00:00
---

# Networking methods for source database connectivity  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  Networking methods for source database connectivity Stay organized with collections  Save and categorize content based on your preferences. 

To move data from your source database server into the destination Cloud SQL for PostgreSQL instance, Database Migration Service needs to connect to your source instance. That connection can be established over the public internet, or through a series of private connections in your project's Virtual Private Cloud (VPC).

This page provides an overview of each available source database connectivity method, as well as a recommendation section to help you choose the right solution for your migration:

  * Method comparison provides a comparison table for available source connectivity methods.

  * IP allowlist describes network connectivity to the public IP of your source database.

  * Forward-SSH tunnel provides an overview for dedicated Secure Shell (SSH) tunnels.

  * Private connectivity with Private Service Connect interfaces describes how to connect to your source private IP with network attachments.

  * Private connectivity with VPC peering describes how you can establish a connection to the private IP of your source database over peered VPC networks.




After you familiarize yourself with different connectivity methods and their requirements, you can use the  decision tree diagram to pick the right solution for your scenario.

## Method comparison

Every connectivity method comes with different benefits and requirements. Use the following table to compare them at a glance, and then learn more details in the sections dedicated for each method.

Networking method | Advantages | Disadvantages  
---|---|---  
IP allowlist | 

  * The easiest connectivity method to set up.
  * Useful when your source database can't be reached through private networks in Google Cloud. 

| 

  * Requires that you expose an IPv4 address of your source database server to the public internet. This requires extra security measures. For example, we recommend that you use TLS certificates and firewall rules for securing the connection. 
  * Configuring the firewall rules may require assistance from the IT department. 
  * Database Migration Service doesn't support direct connectivity to databases using the Single Client Access Name (SCAN) feature in Oracle Real Application Clusters (RAC) environments. For potential solutions to using public IP allowlist connectivity with such environments, see [ Troubleshoot Oracle SCAN errors](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/diagnose-issues#troubleshoot-scan). 

  
Forward SSH tunnel | 

  * More secure than connecting over public IP with an IP allowlist. The initial connection is established through Secure Shell (SSH) ports over the public internet. Once the connection is active, all traffic travels over a secure, private connection. 
  * Useful when your source database can't be reached through private networks in Google Cloud, but you don't want to expose your source database server directly to the public internet. 

| 

  * Using an intermediate server (the forward-SSH tunnel machine) for connectivity might introduce additional latency. 
  * You must set up and maintain the forward-ssh host server. The server must be online for the whole duration of your migration. 

  
Private Service Connect interfaces | 

  * Establishes connections to your source private IP by using a network attachment. This method doesn't consume peering quota in your VPC. 
  * The easiest source private connectivity method to configure.

| 

  * Requires setting up a network attachment and adjusting firewall rules.
  * You can't modify the network attachment after you establish the connection. 

  
Private connectivity with Virtual Private Cloud peering | The connection is established to the private IP address of your source database over VPC peerings. If your VPC doesn't have enough peering quota, it might be difficult to use this connectivity method. In most cases, we recommend that you use  Private connectivity with Private Service Connect interfaces instead.  | 

  * For sources outside your Google Cloud VPC, you might need to use additional network components, such as Cloud VPN or a reverse proxy VM. 
  * You need a [ Virtual Private Cloud with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) to use Virtual Private Cloud peering. 
  * This setup consumes [ peering quota](https://docs.cloud.google.com/vpc/docs/vpc-peering#peering-limits) on your VPC network. 

  
  
## IP allowlist for source database connectivity

When you use the IP allowlist connectivity method, Database Migration Service attempts to establish a connection to a publicly available IP address of your source database server.

![A networking diagram that shows a high-level public IP connectivity
      setup.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_public_ip_src_oracle.svg) **Figure 1.** Migration networking example: public IP source connectivity. (click to enlarge) ![A networking diagram that shows a high-level public IP connectivity
      setup.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_public_ip_src_oracle.svg)

### Requirements for IP allowlist connectivity

At a high level, to use this connectivity method you need to ensure the following:

  * You must expose your source's IP address to the public internet (either directly, or with a publicly recognized hostname through a _Domain Name Server_ (DNS)).

  * Database Migration Service doesn't support direct connectivity to databases using the Single Client Access Name (SCAN) feature in Oracle Real Application Clusters (RAC) environments. For potential solutions to using public IP allowlist connectivity with such environments, see [ Troubleshoot Oracle SCAN errors](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/diagnose-issues#troubleshoot-scan).
  * You need to allow incoming connections from [ Database Migration Service public IP addresses](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/ip-allowlists-and-regions).

  * Optional: IP allowlist connectivity uses unencrypted connections by default. We recommend that you use TLS certificates to secure your connection. Database Migration Service offers support for different TLS types so that you can pick the best solution depending on what your source database can support. For more information, see [ Use SSL/TLS certificates to encrypt network connections](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/encrypt-connections-with-certificates).


**Note:** SSL/TLS encryption is supported for Oracle version 12 and later. 

### Configure IP allowlist connectivity

Configuring public IP connectivity requires different steps depending on you source database type. For more information, see:

  * [ Configure IP allowlist connectivity for self-hosted sources](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-self-hosted#ip-allowlist)

  * [ Configure IP allowlist connectivity for sources in Amazon Web Services](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-aws-rds-oracle#ip-allowlist)




## Forward-SSH tunnel for source database connectivity

This connectivity method is a mixture of public and private network connectivity. The connection itself is established through _Secure Shell_ (SSH) ports to the public IP address of the tunnel host server. Once the connection is active, all traffic travels over a secure tunnel to the private IP address of your source database.

![A networking diagram that shows a high-level connectivity
      setup over a dedicated SSH tunnel server.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_ssh_tunnel_src_oracle.svg) **Figure 2.** Migration networking example: source connectivity over an SSH tunnel. (click to enlarge) ![A networking diagram that shows a high-level connectivity
      setup over a dedicated SSH tunnel server.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_ssh_tunnel_src_oracle.svg)

### Requirements for forward-SSH tunnels

To create the connection, you need to expose SSH ports to the public internet on your tunnel server. When connectivity is established, all traffic is routed through the private tunnel connection.

It's possible to terminate the tunnel on the same server where you host your source database, but we recommend that you use a dedicated tunnel server. This way you aren't exposing your source database directly to the public internet. The tunnel server can be any Unix or Linux host that can be reached from the internet using SSH, and can access your source database.

For certain connectivity scenarios, we recommend that you use the  private connectivity with Virtual Private Cloud peering networking method instead of a forward-SSH tunnel:

  * For self-hosted sources that reside inside inside Google Cloud, Database Migration Service can access the private IP of your source database with the private connectivity configuration. You don't need to set up a separate SSH server to establish the connection.



### Configure forward-SSH tunnel connectivity

Configuring connectivity through a forward-SSH tunnel requires different steps depending on you source database type. For more information, see:

  * [ Configure connectivity over a forward-SSH tunnel for self-hosted sources](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-self-hosted#forward-ssh)

  * [ Configure IP allowlist connectivity for sources in Amazon Web Services](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-aws-rds-oracle#forward-ssh)




## Private connectivity with Private Service Connect interfaces

[ Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) let Database Migration Service initiate connections to the private IP of your source database without consuming peering quota for its own IP addresses. Instead, this connectivity method utilizes network attachments you create in your VPC.  ![A networking diagram that shows a high-level connectivity
      setup over a dedicated SSH tunnel server and Private Service
      Connect interfaces..](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_psci_3rd_party_cloud_source_oracle.svg) **Figure 3.** Migration networking example: private IP source connectivity with Private Service Connect interfaces and Cloud VPN for sources that reside in other cloud offerings. (click to enlarge) ![A networking diagram that shows a high-level connectivity
      setup over a dedicated SSH tunnel server and Private Service
      Connect interfaces.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_psci_3rd_party_cloud_source_oracle.svg)

### Requirements for Private Service Connect interfaces

This connectivity method requires that you create a network attachment in the VPC network where your source database can be reached. The subnet for the network attachment must have 6 usable IP addresses (meaning, you have to use the `/29` range for a total of 8 IP addresses). You can use the same network attachment for multiple migration jobs, provided that you have enough addresses to accommodate your migration scenarios:

Destination| Number of required IP addresses  
---|---  
Cloud SQL zonal instance | 1 address  
Cloud SQL high availability (HA) instance | 2 addresses  
  
### Configure private IP connectivity with Private Service Connect interfaces

To use private IP connectivity with Private Service Connect interfaces, your source database private IP must be reachable from the Virtual Private Cloud where you create the network attachment. To learn more about configuring this private IP connectivity method for different database sources, see:

  * For self-hosted sources: See [ Configure private IP connectivity with Private Service Connect interfaces for self-hosted sources](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-self-hosted#private-psc-interfaces).

  * For Amazon RDS for Oracle: You need Cloud VPN or Cloud Interconnect to create the connection to the private IP of your source database. See: [ Configure private IP connectivity with Private Service Connect interfaces for Amazon RDS sources](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-aws-rds-oracle#private-psc-interfaces).




## Private connectivity with VPC peering

**Important:** Database Migration Service uses peering to connect to the VPC where your source database can be reached. If your VPC doesn't have enough peering quota, it might be difficult to use this connectivity method. In most cases, we recommend that you use  Private connectivity with Private Service Connect interfaces instead. 

This method lets you connect to your source through the private IP addresses in your Virtual Private Cloud (VPC). You don't need to expose any interfaces to the public internet to use this method, but it requires that your source database IP address or hostname can be reached from your Google Cloud VPC.

Depending on what source database you have, this connectivity method might require you to set up additional network components (such as Cloud VPN or a reverse proxy VM):

![A networking diagram that shows a high-level connectivity
      setup over a dedicated SSH tunnel server.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_vpc_3rd_party_cloud_source_oracle.svg) **Figure 4.** Migration networking example: private IP source connectivity with Virtual Private Cloud peering and Cloud VPN for managed sources that reside outside Google Cloud. (click to enlarge) ![A networking diagram that shows a high-level connectivity
      setup over a dedicated SSH tunnel server.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_vpc_3rd_party_cloud_source_oracle.svg)

### Requirements for private IP connectivity

This connectivity method is best suited for sources whose private IP address can be reached from your Google Cloud VPC network. For self-hosted sources that reside in Google Cloud, you can establish direct peering connections with a [ _private connectivity configuration_ in Database Migration Service](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-private-connectivity-configuration). For other types of sources you might need additional network components such as such as Cloud VPN or [ a reverse proxy VM](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy) (or both).

Private IP connectivity requires the following:

  * You need to have a [ Virtual Private Cloud network with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).

This is the network that you peer with Database Migration Service and your source database server. You need to have enough space to allocate IP ranges for both components.

  * For Amazon RDS for Oracle: You need to have a Cloud VPN or Cloud Interconnect configured in the same VPC network where you intend to create the private connectivity configuration for Database Migration Service. If you can't create the private connectivity configuration in the same VPC network, you need to [ set up a reverse proxy Virtual Machine (VM) on Compute Engine](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy).


**Note:** To create the VPC peering connection for Database Migration Service, you use the dedicated _private connectivity configuration_ that you create and manage in Database Migration Service. This configuration works like a VPC peering connection, but it's easier to configure and manage.

### Configure private IP connectivity with VPC peering

To use private IP connectivity with Virtual Private Cloud peering, your source database private IP must be reachable from your Virtual Private Cloud. Depending on your network architecture, you might need to use additional components such as a reverse proxy VM or Cloud VPN.

To learn more about configuring private IP connectivity for different database sources, see:

  * For self-hosted sources: See [ Configure private IP connectivity with Virtual Private Cloud peering for self-hosted sources](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-self-hosted#private-psc-interfaces).

  * For Amazon RDS for Oracle: You need Cloud VPN or Cloud Interconnect to create the connection to the private IP of your source database. See: [ Configure private IP connectivity with Virtual Private Cloud peering for Amazon RDS sources](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-aws-rds-oracle#private-vpc-peering).


**Note:** For scenarios where your source can be reached from a **different VPC** than the one where you can create a private connectivity configuration for Database Migration Service, you can use private connectivity with a reverse proxy.

## Source network connectivity decision tree

When you are familiar with all supported source connectivity methods and their requirements, you can follow the questions in the diagram to help you pick the right connectivity method for your scenario.

![A decision tree diagram with guiding questions to help you
        pick the right connectivity method.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/networking_source_decision_tree.svg)**Figure 5.** Source network connectivity decision tree. 

## What's next

  * Learn about destination database connectivity. See [ Networking methods for destination database connectivity](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-destination).

  * To get a complete, step-by-step migration walkthrough, see [ Oracle to Cloud SQL for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
