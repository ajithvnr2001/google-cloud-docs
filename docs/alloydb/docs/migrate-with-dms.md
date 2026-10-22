---
url: https://docs.cloud.google.com/alloydb/docs/migrate-with-dms/
title: Migrate to AlloyDB for PostgreSQL using Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:15.126443+00:00
---

# Migrate to AlloyDB for PostgreSQL using Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/migrate-with-dms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Migrate to AlloyDB for PostgreSQL using Database Migration Service Stay organized with collections  Save and categorize content based on your preferences. 

To migrate your databases to AlloyDB for PostgreSQL with minimal downtime, you can use Database Migration Service. Database Migration Service streamlines networking, manages the initial database snapshot and ongoing replication, and provides status updates throughout the migration process.

Database Migration Service offers multiple migration paths to serve a wide variety of use cases:

  * [Homogeneous migrations](https://docs.cloud.google.com/database-migration/docs/homogeneous-migrations) let you move data without changing your database SQL engine from self-managed or managed offerings (such as Cloud SQL for PostgreSQL, Amazon RDS, or Amazon Aurora). Database Migration Service can help you migrate from backup files (physical or logical), or take the snapshot for you.

  * [Heterogeneous migrations](https://docs.cloud.google.com/database-migration/docs/heterogeneous-migrations) from Oracle and SQL Server sources to AlloyDB for PostgreSQL let you convert your database objects to PostgreSQL with the assistance of Gemini-powered conversion features. These features help ensure your database objects' consistency and quality in the converted PostgreSQL schemas.


![Architecture diagram showing data flow from on-premises or other clouds
    to Google Cloud using Database Migration Service, highlighting key features like
    homogeneous and heterogeneous migrations, minimal downtime,
    and Gemini-powered conversion.](https://docs.cloud.google.com/static/database-migration/docs/images/overview_dms_data_flow.svg) **Figure 1.** Database Migration Service architecture and data flow (click to enlarge). ![](https://docs.cloud.google.com/static/database-migration/docs/images/overview_dms_data_flow.svg)

## Database Migration Service in AlloyDB for PostgreSQL

A special, lightweight migration flow called _quick-start migrations_ is integrated directly into AlloyDB for PostgreSQL to help expedite homogeneous migrations from sources that have a private IP address in your Google Cloud Virtual Private Cloud (such as self-managed databases on Compute Engine, or Cloud SQL for PostgreSQL instances enabled for private networking).

In this flow, Database Migration Service can automatically manage all the networking requirements to connect to your source database.

![This diagram shows network connectivity facilitated by Database Migration Service
        for quick-start migrations from self-hosted databases on Compute Engine.](https://docs.cloud.google.com/static/database-migration/docs/images/quick-start-migrations/gce-src-quick-start-migration-network.svg) **Figure 2.** Network connectivity facilitated by Database Migration Service for quick-start migrations from self-hosted databases on Compute Engine. (click to enlarge) ![This diagram shows network connectivity facilitated by Database Migration Service
        for quick-start migrations from self-hosted databases on Compute Engine.](https://docs.cloud.google.com/static/database-migration/docs/images/quick-start-migrations/gce-src-quick-start-migration-network.svg)

For more information on quick-start migrations in AlloyDB for PostgreSQL, see [Quick-start migrations](https://docs.cloud.google.com/alloydb/docs/quick-start-migrations-guide).

## What's next

  * [ Learn more about Database Migration Service features and available scenarios](https://docs.cloud.google.com/database-migration/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
