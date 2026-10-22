---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-considerations/
title: Plan your networking configuration \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:53.607484+00:00
---

# Plan your networking configuration  |  Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for AlloyDB ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

#  Plan your networking configuration Stay organized with collections  Save and categorize content based on your preferences. 

From a networking point of view, Database Migration Service and AlloyDB for PostgreSQL are _service producers_ that reside in their own dedicated networks (known as _service networks_), outside the Virtual Private Cloud (VPC) networks that you use in your Google Cloud project. The goal of configuring network connectivity for a migration process is to ensure that Database Migration Service can reach your source SQL Server database and the destination AlloyDB for PostgreSQL cluster.

Before you configure the source or destination databases, we recommend that you consider what networking methods you can use to establish the necessary network connections. See the following pages:

  * [ Networking overview](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-overview) describes the high-level, end-to-end migration networking landscape.

  * [ Source networking methods](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-source) focuses on the source database connectivity.

  * [ Destination networking methods](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-destination) focuses on the destination database connectivity.




For a complete, step-by-step migration walkthrough, see [ SQL Server to AlloyDB for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/guide).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
