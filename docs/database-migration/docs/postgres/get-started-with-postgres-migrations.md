---
url: https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations/
title: Get started with PostgreSQL homogeneous migrations \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:27.868301+00:00
---

# Get started with PostgreSQL homogeneous migrations  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Get started with PostgreSQL homogeneous migrations Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service provides a lot of flexibility for your homogeneous PostgreSQL migrations to Cloud SQL for PostgreSQL. Depending on your database size, downtime requirements, and networking setup, there are different workflows available to best meet your scenario. Detailed networking and other prerequisites are described in each migration guide.

The following table provides an overview of each migration flow:

Migration workflow | Best suited for | Description  
---|---|---  
[Migrate to a new destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/guide-to-new-instance) | Standard migrations where you want to create a clean target instance tailored for the migration workload. | Database Migration Service automatically provisions a new destination instance using configuration options you select, and migrates the source schemas and data.  
[Migrate to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/guide-to-existing-instance) | Scenarios where target instance parameters must be pre-configured, or when using custom private IP configurations or Terraform-managed instances. | Migrate data into a Cloud SQL instance that you have already created and configured. The destination instance must be empty.  
[Use quick-start migrations (Preview)](https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide) | Rapid setup and streamlined migrations with `pgnative` replication and Private Service Connect network attachments to simplify network configuration. | Perform an automated migration using predefined configurations and private connectivity to migrate your PostgreSQL databases to Cloud SQL. Learn more in [ About quick-start migrations](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
