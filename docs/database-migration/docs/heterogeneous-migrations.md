---
url: https://docs.cloud.google.com/database-migration/docs/heterogeneous-migrations/
title: Heterogeneous migrations \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:23.100399+00:00
---

# Heterogeneous migrations  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/heterogeneous-migrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/overview)



Send feedback 

#  Heterogeneous migrations Stay organized with collections  Save and categorize content based on your preferences. 

A heterogeneous migration moves data between different database technologies. The database engine of the source, such as Oracle differs from the database engine of the destination, such as PostgreSQL.

Heterogeneous migrations are more complex than homogeneous migrations due to differences in schema structure, data types, and metadata components between the source database and the destination database. Database Migration Service provides tools, such as Gemini-assisted schema and code conversion, that help you convert the schema and objects from your source database into a format that is compatible with your destination database.

Heterogeneous migrations use replication based on Change Data Capture (CDC) to process ongoing changes.

For more information, see supported scenarios.

## Supported scenarios

Database Migration Service supports the following heterogeneous migrations:

  * [ Migrate from Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)
  * [ Migrate from Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)
  * [ Migrate from SQL Server to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)
  * [ Migrate from SQL Server to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
