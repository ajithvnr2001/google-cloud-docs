---
url: https://docs.cloud.google.com/database-migration/docs/postgres/about-migration-jobs/
title: About migration jobs \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:30.065775+00:00
---

# About migration jobs  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/about-migration-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  About migration jobs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the migration jobs available in Database Migration Service with homogeneous migrations: for pre-existing destination instances, and ones that Database Migration Service creates on your behalf during the migration job configuration.

Migration jobs represent data movement managed by Database Migration Service. They let you configure settings specific to a particular migration process, monitor the progress, and safely finalize the data movement. Migration jobs progress differently depending on their type (continuous or one-time), features used, and whether you migrate to a new or an existing Cloud SQL instance.

## Destination instances created by Database Migration Service

When you want to migrate to a new Cloud SQL for PostgreSQL instance, Database Migration Service can create it for you as a part of the migration job creation flow. If you want Database Migration Service to create the destination database for you, follow the guidance in [ Create a migration job to a new destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job).

## Destination instances created outside Database Migration Service

You can create your destination database instance outside of Database Migration Service before you configure the migration job. This approach is especially useful when you plan to utilize Terraform or other infrastructure as code tools to manage your infrastructure.

There are certain limitations that you should consider when you want to migrate to a destination instance created outside of Database Migration Service. For more information, see [ Known Limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations#existing-instance-limitations).

If you want to migrate to a destination database created outside of Database Migration Service, follow the guidance in [ Create a migration job to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job-existing-instance).

## What's next

To get a complete, step-by-step migration walkthrough for homogeneous Cloud SQL for PostgreSQL migrations, see [ Get started with Cloud SQL for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
