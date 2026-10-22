---
url: https://docs.cloud.google.com/database-migration/docs/mysql/networking-considerations/
title: Plan your networking configuration \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:02.743155+00:00
---

# Plan your networking configuration  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/networking-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Plan your networking configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a high-level overview of what you need to consider when you plan network connectivity for your migration.

From a networking point of view, Database Migration Service and Cloud SQL are _service producers_ that reside in their own dedicated networks (known as _service networks_), outside the Virtual Private Cloud (VPC) networks that you use in your Google Cloud project.

For homogeneous MySQL migrations to Cloud SQL, Database Migration Service connects to the _destination_ Cloud SQL instance and then manages the migration process on its behalf. It's the destination instance that establishes the connection to your source instance, but Database Migration Service oversees the process. The goal of configuring network connectivity for a migration process is to ensure that the destination Cloud SQL can reach your source database server over the network.

Different connectivity methods are available for different source database offerings and destination Cloud SQL for MySQL configurations. Before you configure your source instance for the migration, we recommend that you consider what networking methods you can use to establish the necessary connections. See the [ Networking overview](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods) page to understand the end-to-end networking landscape for Database Migration Service migrations.

## What's next

For complete, step-by-step migration walkthroughs, see [ Get started with Cloud SQL for MySQL migrations](https://docs.cloud.google.com/database-migration/docs/mysql/get-started-with-mysql-migrations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
