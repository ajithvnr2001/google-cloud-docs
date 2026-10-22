---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-dst-connection-public-ip/
title: Configure public IP connectivity for AlloyDB for PostgreSQL destinations \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:32.710520+00:00
---

# Configure public IP connectivity for AlloyDB for PostgreSQL destinations  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-dst-connection-public-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  Configure public IP connectivity for AlloyDB for PostgreSQL destinations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use public IP connectivity for the destination database connection in heterogeneous Oracle to AlloyDB for PostgreSQL migrations with Database Migration Service.

To use public IP connectivity, follow these steps:

  1. Consider the requirements for public IP connectivity. See [ Destination database connectivity methods overview](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-destination). 
  2. When you [ create and configure the destination cluster](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-your-destination-postgresql-database), make sure you create it with public IP enabled. If you already created your destination cluster, you can still [ enable a public IP for it](https://docs.cloud.google.com/alloydb/docs/connect-public-ip#enable-ip). 
  3. At a later stage, when you [ create the destination connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-destination-connection-profile), do the following: 
     1. In the **Define connection details** section, enter your AlloyDB for PostgreSQL instance public IP. 
     2. In the **Define connectivity method** section, select **IP allowlist**. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
