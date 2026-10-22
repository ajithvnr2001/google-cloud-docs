---
url: https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods/
title: Network connectivity for standard homogeneous PostgreSQL migrations \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:26.686168+00:00
---

# Network connectivity for standard homogeneous PostgreSQL migrations  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Network connectivity for standard homogeneous PostgreSQL migrations Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of concepts associated with configuring network connectivity for standard homogeneous PostgreSQL migrations to Cloud SQL for PostgreSQL. For information about quick-start migration connectivity, see the [ Use quick-start migrations](https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide) guide.

  * Network components describes the end-to-end network configuration for homogeneous PostgreSQL migrations.

  * Method availability explains which methods are available depending on your scenario.

  * Method comparison provides a comparison table for available connectivity methods.

  * Dedicated section for each available connectivity method:

    * IP allowlist describes network connectivity to the public IP of your source database.

    * Reverse-SSH tunnel provides an overview for dedicated Secure Shell (SSH) tunnels.

    * Private connectivity with Private Service Connect interfaces describes how to connect to your source private IP with network attachments.

    * _For Cloud SQL for PostgreSQL sources only_ :  Specialized VPC peering describes a networking method tailored for migrating between two PSA Cloud SQL instances.

    * Private connectivity with VPC peering describes how you can establish a connection to the private IP of your source database over peered VPC networks.




After you familiarize yourself with different connectivity methods and their requirements, you can use the  decision tree diagram to pick the right solution for your scenario.

## Network components involved in the migration process

For homogeneous PostgreSQL migrations to Cloud SQL, Database Migration Service connects to the _destination_ Cloud SQL for PostgreSQL instance and then manages the migration process on its behalf. It's the destination instance that establishes the connection to your source instance, while Database Migration Service oversees the process.

![PostgreSQL migration flow overview](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/pgsql/pgsql_hmm_end2end_flow.svg) **Figure 1.** Data movement during Database Migration Service for PostgreSQL migrations. (click to enlarge) ![PostgreSQL migration flow overview](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/pgsql/pgsql_hmm_end2end_flow.svg)

When you plan the network connectivity setup for your migration, it's important to carefully consider the infrastructure requirements, including what limitations your networking decisions might introduce to the end state of the migrated database instance. For example, if you want to use a private connection for your network connectivity, you need to use a destination Cloud SQL instance with private IP enabled.

## Connectivity methods availability

Different connectivity methods are available for different source databases depending on whether you are migrating to a new or to an existing destination instance. The following table provides an overview of which scenario supports which method:

Source database offering | Methods for migrations to new destination instances | Methods for migrations to existing destination instances  
---|---|---  
Self-hosted, Amazon Aurora, Amazon RDS, Azure Database for PostgreSQL | IP allowlist, reverse-SSH tunnel, VPC peering | IP allowlist, reverse-SSH tunnel, VPC peering (requires a PSA destination instance), PSC interfaces (requires a PSC-enabled destination instance)   
Cloud SQL for PostgreSQL | IP allowlist (not recommended), Specialized VPC peering | IP allowlist (not recommended), Specialized VPC peering, PSC interfaces (requires a PSC-enabled destination instance)   
  
## Connectivity methods comparison

Every connectivity method comes with different benefits and requirements. Use the following tables to compare them at a glance, and then learn more details in the sections dedicated for each method.

Networking method | Advantages | Disadvantages  
---|---|---  
IP allowlist | 

  * The easiest connectivity method to set up.
  * Useful when your source database can't be reached through private networks in Google Cloud. 

| 

  * Requires that you expose an IPv4 address of your source database server to the public internet. This requires extra security measures. For example, we recommend that you use TLS certificates and firewall rules for securing the connection. 
  * Configuring the firewall rules may require assistance from the network security or IT department. 

  
Reverse-SSH tunnel | 

  * More secure than connecting over public IP with an IP allowlist. The initial connection is established through Secure Shell (SSH) ports over the public internet. Once the connection is active, all traffic travels over a secure, private tunnel to PostgreSQL port 5432. 
  * Useful when your source database can't be reached through private networks in Google Cloud, but you don't want to expose your source database server directly to the public internet. 

| 

  * Using an intermediate server (the reverse-SSH tunnel machine) for connectivity might introduce additional latency. 
  * You must set up and maintain the reverse-SSH host server. The server must remain online for the whole duration of your migration. 

  
Private Service Connect interfaces | 

  * Establishes connections to your source private IP by using a network attachment. This method doesn't consume peering quota in your VPC. 
  * The easiest and recommended source private connectivity method to configure.

| 

  * Supported only for migrations to existing Cloud SQL for PostgreSQL destinations. If you want to use this method, you need to create the destination instance directly in Cloud SQL. 
  * Requires setting up a network attachment and adjusting firewall rules.
  * You can't modify the network attachment after you establish the connection. 

  
_For Cloud SQL for PostgreSQL sources only_ :  Specialized VPC peering | This connectivity method is specialized for migrating between PSA Cloud SQL for PostgreSQL instances without using a shared VPC.  | Requires that both instances are PSA instances with private IP enabled. Not supported for PSC-enabled destinations.   
Private connectivity with Virtual Private Cloud peering | The connection is established to the private IP address of your source database over VPC peerings. If your VPC doesn't have enough peering quota, it might be difficult to use this connectivity method. For most scenarios where you migrate from a Cloud SQL for PostgreSQL source, we recommend that you use  Private connectivity with Private Service Connect interfaces instead.  | 

  * For sources outside your Google Cloud VPC, you might need to use additional network components, such as Cloud VPN or Cloud Interconnect. 
  * You need a [ Virtual Private Cloud with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) to use Virtual Private Cloud peering. 
  * This setup consumes [ peering quota](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering) on your VPC network. 

  
  
## IP allowlist for source database connectivity

When you use the IP allowlist connectivity method, Cloud SQL attempts to establish a connection to a publicly available IP address of your source database server on PostgreSQL port `5432`.

![Diagram that shows public IP allowlist connectivity for homogeneous
        migrations.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/pgsql/pgsql_hmm_public_ip.svg) **Figure 2.** IP allowlist network connectivity diagram for homogeneous PostgreSQL migrations. (click to enlarge) ![Diagram that shows public IP allowlist connectivity for homogeneous migrations.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/pgsql/pgsql_hmm_public_ip.svg)

### Requirements for IP allowlist connectivity

At a high level, to use this connectivity method you need to ensure the following:

  * You must expose your source database IP address to the public internet (either directly, or with a publicly recognized hostname through a _Domain Name Server_ (DNS)).

  * Your destination Cloud SQL instance must have a public IP enabled. Your source database must allow incoming connections from the outbound public IP of the destination instance.




### Configure IP allowlist connectivity

Configuring public IP connectivity requires different steps depending on your source database type. For more information, see:

  * [ Configure IP allowlist connectivity for self-hosted sources](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-self-hosted#ip-allowlist)

  * [ Configure IP allowlist connectivity for Amazon RDS and Amazon Aurora sources](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-aws#ip-allowlist)

  * [ Configure IP allowlist connectivity for Azure Database for PostgreSQL sources](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-azure#ip-allowlist)

  * [ Configure IP allowlist connectivity for Cloud SQL for PostgreSQL sources](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres#ip-allowlist)




## Reverse-SSH tunnel database connectivity

This connectivity method is a mixture of public and private network connectivity. The connection itself is established through _Secure Shell_ (SSH) ports to the public IP address of the tunnel host server. Once the connection is active, all traffic travels over a secure tunnel to the private IP address of your source database on port `5432`.

For Cloud SQL sources or self-hosted solutions that reside inside Google Cloud, we recommend that you use  private connectivity with Private Service Connect interfaces or  private connectivity with Virtual Private Cloud peering methods.

![A networking diagram that shows a high-level connectivity
      setup over a dedicated SSH server.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/pgsql/pgsql_hmm_reverse_ssh.svg) **Figure 3.** Migration networking example: source connectivity over an SSH tunnel. (click to enlarge) ![A networking diagram that shows a high-level connectivity
      setup over a dedicated SSH server.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/pgsql/pgsql_hmm_reverse_ssh.svg)

### Requirements for reverse-SSH tunnels

To create the connection, you need to expose SSH ports to the public internet on your tunnel server (also known as the _bastion host_). When connectivity is established, all traffic is routed through the private tunnel connection.

This method requires additional network components:

  * A Virtual Machine (VM) in Google Cloud to serve as the reverse-SSH machine.
  * An additional machine on your network that has connectivity to the source database.



### Configure reverse-SSH tunnel connectivity

Database Migration Service can generate a setup script to create the reverse-SSH VM, but the full end-to-end process is different depending on your source database type. For more information, see [ Configure reverse-SSH connectivity](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-reverse-ssh-tunnel).

## Private connectivity with Private Service Connect interfaces

This connectivity method lets you connect to the private IP of your source database without consuming [ VPC peering quota](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering). Private Service Connect interfaces are the recommended method for private IP connectivity, but they are only available when you [ migrate to an existing instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job-existing-instance).

When you use Private Service Connect interfaces, your destination instance doesn't consume more peering quota. Instead, it leverages the Private Service Connect interface to reach the Virtual Private Cloud where the private IP of your source database can be reached. Depending on your network architecture, you might need to use additional components such as Cloud VPN or Cloud Interconnect.

![Diagram showing Private Service Connect connectivity with Cloud VPN
        for homogeneous migrations.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/pgsql/pgsql_hmm_other_src_psci.svg) **Figure 4.** Network connectivity with Private Service Connect interfaces for homogeneous migrations from sources that reside outside Google Cloud. (click to enlarge) ![Diagram showing Private Service Connect connectivity with Cloud VPN
        for homogeneous migrations.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/pgsql/pgsql_hmm_other_src_psci.svg)

For migrations from Cloud SQL for PostgreSQL instances, your source instance needs to be enabled for Private Services Access and peered with the Virtual Private Cloud where you create the network attachment, but the destination Cloud SQL for PostgreSQL instance doesn't consume more peering quota. Instead, it leverages the Private Service Connect interface.

### Requirements for Private Service Connect interfaces

This connectivity method requires the following:

  * Your destination database instance must be a Cloud SQL for PostgreSQL instance with PSC enabled.

  * You need to have a [ Virtual Private Cloud network with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).

This is the network where you create the network attachment. The IP of your source database must be reachable from that Virtual Private Cloud. For example, for Cloud SQL for PostgreSQL sources, this is the network that you peer with the PSA-enabled source Cloud SQL instance.




### Configure private IP connectivity with Private Service Connect interfaces

To use private IP connectivity with Private Service Connect interfaces, your source database private IP must be reachable from your Virtual Private Cloud. Depending on your network architecture, you might need to use additional components such as Cloud VPN or Cloud Interconnect.

To learn more about configuring private IP connectivity for different database sources, see:

  * [ Configure private IP connectivity with Private Service Connect interfaces for self-hosted sources](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-self-hosted#private-psc-interfaces).

  * [ Configure private IP connectivity with Private Service Connect interfaces for Amazon RDS and Amazon Aurora sources](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-aws#psc-interfaces).

  * [ Configure private IP connectivity with Private Service Connect interfaces for Azure Database for PostgreSQL sources](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-azure#psc-interfaces).




## Cloud SQL for PostgreSQL sources only: specialized VPC peering

This method is dedicated for migrations between PSA Cloud SQL for PostgreSQL instances. In standard networking scenarios, connecting two Cloud SQL instances with Virtual Private Cloud peering requires that you use a shared VPC. For homogeneous PostgreSQL migrations with Database Migration Service, you can connect two PSA instances without using a shared VPC.

### Requirements for specialized VPC peering

This connectivity method requires the following:

  * Your source database instance must be a Cloud SQL for PostgreSQL instance with PSA enabled.

  * Your destination database instance must be a Cloud SQL for PostgreSQL instance with PSA enabled.

  * You need to have a [ Virtual Private Cloud network with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).

This is the network that Database Migration Service peers with the destination Cloud SQL instance. You need to have enough space to allocate the required IP ranges.




### Configure private IP connectivity specialized VPC peering

To learn more about configuring specialized VPC peering for source PSA Cloud SQL for PostgreSQL instances, see [ Configure specialized Virtual Private Cloud peering for Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres#private-vpc-peering).

## Private connectivity with VPC peering

**Important:** This method uses peering to connect to the VPC where your source database can be reached. If your VPC doesn't have enough peering quota, it might be difficult to use this connectivity method. In most cases, we recommend that you use  Private connectivity with Private Service Connect interfaces instead. 

This method lets you connect to your source through the private IP addresses in your Virtual Private Cloud (VPC). You don't need to expose any interfaces to the public internet to use this method, but it requires that your source database IP address or hostname can be reached from your Google Cloud VPC. For sources that reside outside Google Cloud, you might need additional network components, such as Cloud VPN or Cloud Interconnect.

![Diagram showing Virtual Private Cloud peering connectivity for homogeneous
        PostgreSQL migrations.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/pgsql/pgsql_hmm_vpc_peering.svg) **Figure 5.** Network connectivity with Virtual Private Cloud peering for homogeneous PostgreSQL migrations. (click to enlarge) ![Diagram showing Virtual Private Cloud peering connectivity for homogeneous
        PostgreSQL migrations.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/pgsql/pgsql_hmm_vpc_peering.svg)

### Requirements for private IP connectivity with VPC peering

Private IP connectivity with VPC peering requires the following:

  * You need to have a [ Virtual Private Cloud network with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). The private IP of your source database must be reachable in that network.



### Configure private IP connectivity with VPC peering

To use private IP connectivity with Virtual Private Cloud peering, your source database private IP must be reachable from your Virtual Private Cloud. Depending on your network architecture, you might need to use additional components such as Cloud VPN or Cloud Interconnect.

To learn more about configuring private IP connectivity for different database sources, see:

  * [ Configure private IP connectivity with Virtual Private Cloud peering for self-hosted sources](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-self-hosted#private-vpc-peering).

  * [ Configure private IP connectivity with Virtual Private Cloud peering for Amazon RDS and Amazon Aurora sources](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-aws#vpc-peering).

  * [ Configure private IP connectivity with Virtual Private Cloud peering for Azure Database for PostgreSQL sources](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-azure#vpc-peering).




## Network connectivity decision tree

When you are familiar with all supported connectivity methods and their requirements, you can follow the questions in the diagram to help you pick the right connectivity method for your scenario.

![A decision tree diagram with guiding questions to help you
        pick the right connectivity method.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/hmm_standard_migration_network_decision_tree.svg)**Figure 6.** Source network connectivity decision tree. 

## What's next

  * For a complete, step-by-step migration walkthrough, see [ Get started with Cloud SQL for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations).

  * To configure your source database prerequisites and replication permissions, see [ Configure source database](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
