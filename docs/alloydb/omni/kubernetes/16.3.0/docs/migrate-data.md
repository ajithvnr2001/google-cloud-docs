---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/migrate-data/
title: Migrate data to AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:36.549798+00:00
---

# Migrate data to AlloyDB Omni  |  AlloyDB Omni for Kubernetes: 16.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/migrate-data/

This page documents AlloyDB Omni version **16.3.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/overview)



Send feedback 

#  Migrate data to AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.3.0keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/migrate-data)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/migrate-data)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/migrate-data)

This page outlines the process to migrate data from PostgreSQL or Oracle to AlloyDB Omni. 

  * PostgreSQL to AlloyDB Omni

  * Oracle to AlloyDB Omni




## PostgreSQL to AlloyDB Omni

Use the following tools based on your migration complexity and downtime to migrate data from PostgreSQL to AlloyDB Omni:

Migration type | Tool  
---|---  
Simple migration with sufficient downtime | [pg_dump](https://www.postgresql.org/docs/16/app-pgdump.html) to backup the existing database and [pg_restore](https://www.postgresql.org/docs/16/app-pgrestore.html) to restore the backup to the new database.  
Complex migration with sufficient downtime | [pgloader](https://pgloader.readthedocs.io/en/latest/) to stream data from the source to the destination.  
Complex migration with minimal downtime | [pglogical](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/about-pglogical) to replicate data from the source to the destination.  
  
## Oracle to AlloyDB Omni

If you have sufficient downtime to move the volume of data in Oracle and convert all Oracle resident application logic to PostgreSQL, use [Ora2Pg](https://ora2pg.darold.net/) for schema conversion, data movement, and code conversion.

If you have minimal downtime for the migration, use the following tools:

To migrate | Use  
---|---  
Code and schema | [Google Cloud Database Migration Service](https://cloud.google.com/database-migration) to migrate the schema and code  
Ora2Pg for schema conversion, data movement, and code conversion  
Change Data Capture (CDC) tool as required to identify and captures data from, Oracle relational tables, and makes the change data available for use by applications.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
