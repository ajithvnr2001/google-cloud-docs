---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-overview/
title: Network connectivity for heterogeneous Oracle to AlloyDB for PostgreSQL migrations \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:10:17.556703+00:00
---

# Network connectivity for heterogeneous Oracle to AlloyDB for PostgreSQL migrations  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  Network connectivity for heterogeneous Oracle to AlloyDB for PostgreSQL migrations Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of concepts associated with configuring network connectivity for heterogeneous Oracle to AlloyDB for PostgreSQL migrations:

  * Network components describes how the source and destination connectivity make up the end-to-end network configuration for migrations.

  * The examples sections show different combinations for public and private source and destination connectivity:

    * Public IP source connectivity and private IP destination connectivity

    * Private IP source connectivity and public IP destination connectivity




After you've considered the high-level relations between Google Cloud services involved in the migration process, you can proceed to learn more about [ source database connectivity methods](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source) and [ destination database connectivity methods](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-destination).

## Network components involved in the migration process

From a networking point of view, Database Migration Service and Cloud SQL are _service producers_ that reside in their own dedicated networks (known as _service networks_), outside the Virtual Private Cloud (VPC) networks that you use in your Google Cloud project. The goal of configuring network connectivity for a migration process with Database Migration Service is to ensure that Database Migration Service can reach your source Oracle database server and the destination AlloyDB for PostgreSQL cluster.

![](https://docs.cloud.google.com/static/database-migration/docs/images/htm/oracle-to-alloydb/overall_htm_connectivity_diagram.svg) **Figure 1.** Simplified view of heterogeneous migration networking (click to enlarge) ![](https://docs.cloud.google.com/static/database-migration/docs/images/htm/oracle-to-alloydb/overall_htm_connectivity_diagram.svg)

When you plan the network connectivity setup for your migration, it's important to carefully consider the infrastructure requirements, including what limitations your networking decisions might introduce to the end state of the migrated database cluster. For example, if you want to use a private connection for the destination database connectivity, you need to create your destination AlloyDB for PostgreSQL cluster with private IP enabled. You can't later disable the private IP on your AlloyDB for PostgreSQL cluster.

There are multiple different methods you can use to establish the necessary network connections. Both [ source](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source) and [ destination](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-destination) connectivity can be established with the use of public or private IP addresses. You can combine any source and destination connectivity methods to best match your infrastructure requirements.

## Example: public IP source connectivity and private IP destination connectivity

In this example, you have the following databases:

  * A self-hosted source Oracle database server with a public IP address.
  * An AlloyDB for PostgreSQL destination cluster with a private IP address enabled.

![](https://docs.cloud.google.com/static/database-migration/docs/images/htm/oracle-to-alloydb/public-src-private-dst-connectivity_v3.svg) **Figure 2.** Migration networking example: public IP source connectivity with private IP destination connectivity (click to enlarge) ![](https://docs.cloud.google.com/static/database-migration/docs/images/htm/oracle-to-alloydb/public-src-private-dst-connectivity_v3.svg)

For the source database connectivity, you use the [ IP allowlist method](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source#ip-allowlist) to establish a connection over the public internet. You secure this connection with an SSL/TLS certificate.

For the destination database connectivity, you use [ Private Service Connect](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-destination#private-ip) to establish a private connection over the Google Cloud network. This internal connection is automatically encrypted by Database Migration Service.

## Example: private IP connectivity for source database hosted outside Google Cloud

In this example, you have the following components:

  * An Oracle source instance hosted in another cloud and a VPN gateway
  * A Cloud VPN instance in your Google Cloud VPC
  * An AlloyDB for PostgreSQL destination cluster with a public IP address enabled

![](https://docs.cloud.google.com/static/database-migration/docs/images/htm/oracle-to-alloydb/private_src_psci_public_dst.svg) **Figure 2.** Migration networking example: private IP source connectivity and public IP destination connectivity (click to enlarge) ![](https://docs.cloud.google.com/static/database-migration/docs/images/htm/oracle-to-alloydb/private_src_psci_public_dst.svg)

For the [ source database connectivity](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source), you use a [ private connectivity configuration](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-private-connectivity-configuration#create-psci-config) to establish a Private Service Connect connection between Database Migration Service and the VPC where you have your Cloud VPN instance. You use Cloud VPN to create an IPsec tunnel between Google Cloud and the cloud network where you have the source Oracle database.

For the destination database connectivity, you use the [ public IP connectivity method](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-destination#public-ip) to establish a connection over the public internet. Database Migration Service automatically secures this connection with SSL/TLS.

## What's next

There are many different connectivity methods you can use. Each method can be further adjusted with proxy servers, ssh tunnels, and bastion VMs.

  * Learn more about [ source database connectivity methods](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source).
  * Learn more about [ destination database connectivity methods](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-destination).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
