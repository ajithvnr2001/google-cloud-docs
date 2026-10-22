---
url: https://docs.cloud.google.com/database-migration/docs/postgres/networking-considerations/
title: Plan your networking configuration \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:26.751282+00:00
---

# Plan your networking configuration  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/networking-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Plan your networking configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a high-level overview of what you need to consider when you plan network connectivity for your migration.

From a networking point of view, Database Migration Service and Cloud SQL are _service producers_ that reside in their own dedicated networks (known as _service networks_), outside the Virtual Private Cloud (VPC) networks that you use in your Google Cloud project.

Depending on whether you choose a **standard migration** or a **quick-start migration** , Database Migration Service uses different networking architectures to connect to your databases. This page focuses primarily on networking considerations for **standard migrations**.

## Standard migration connectivity

For standard homogeneous PostgreSQL migrations to Cloud SQL, Database Migration Service connects to the _destination_ Cloud SQL for PostgreSQL instance and manages the migration process on its behalf. It's the destination instance that establishes the direct network connection to your source instance, while Database Migration Service oversees the process.

The goal of configuring network connectivity for a standard migration is to ensure that the destination Cloud SQL for PostgreSQL instance can route to and reach your source database server over the network.

Different connectivity methods are available depending on your source database offering and your destination Cloud SQL for PostgreSQL network configuration:

  * **IP allowlist** : Connects over the public internet by adding the destination outbound IP address to the source firewall or allowlist.
  * **Reverse SSH tunnel** : Routes replication traffic through an intermediate Compute Engine bastion host over an encrypted SSH tunnel.
  * **Private connectivity with VPC peering** : Connects to the private IP address of your source database across peered VPC networks (for Private Services Access destination instances).
  * **Private connectivity with Private Service Connect interfaces** : Connects to the private IP address of your source database using network attachments (for PSC-enabled destination instances).



Before you configure your source instance for migration, see the [ Networking overview](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods) page to evaluate the end-to-end networking landscape and pick the best method for your scenario.

## Quick-start migrations connectivity

Quick-start migrations use a mediated networking model where Database Migration Service acts as an intermediary sitting _between_ your source database and the destination Cloud SQL for PostgreSQL instance:

  * **Source connectivity** : Database Migration Service connects to your source database using Private Service Connect interfaces and private connectivity configurations. Your source database must have a private IP address assigned within a Google Cloud VPC network. If your source database is hosted outside Google Cloud, you must connect it to your VPC network using a Cloud VPN or Cloud Interconnect connection. Other methods (such as public IP allowlists or reverse SSH tunnels) aren't supported.
  * **Destination connectivity** : Database Migration Service fully manages network communication to your destination instance. The destination instance must be enabled for Private Service Connect.



For a comprehensive explanation of the quick-start networking architecture, component diagrams, and limitations, see [ Network connectivity for quick-start migrations](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations) in the main Database Migration Service documentation.

## What's next

  * For standard migration walkthroughs, see [ Get started with Cloud SQL for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations).
  * To learn how to run a quick-start migration, see [ Use quick-start migrations to migrate to Cloud SQL](https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
