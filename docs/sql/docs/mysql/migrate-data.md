---
url: https://docs.cloud.google.com/sql/docs/mysql/migrate-data/
title: Migrate data from Cloud SQL to an external server \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:35.604998+00:00
---

# Migrate data from Cloud SQL to an external server  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/migrate-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Migrate data from Cloud SQL to an external server Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes how you can move the location of your primary instance to an external, self-managed server with a minimum of downtime.

## Migrate data to an external server

To migrate the primary copy of your data from Cloud SQL to an external server with the least downtime, you set up your external server as an external replica, then demote the Cloud SQL instance to become the replica of the external server.

This procedure requires you to complete the following high-level steps:

  1. Create an external replica for your Cloud SQL instance, following the steps in [Configuring External Replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica).
  2. When the replica is fully synchronized with the Cloud SQL primary, take your applications offline, and update the applications to point to the external server.
  3. Follow the instructions provided in [Demoting the primary instance of an external replica](https://docs.cloud.google.com/sql/docs/replication/configure-external-replica#demote) to demote the Cloud SQL primary instance. Demoting the primary instance also promotes the external server, making it the new primary instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
