---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/about-connection-profiles/
title: About connection profiles \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:36:36.353421+00:00
---

# About connection profiles  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/about-connection-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  About connection profiles Stay organized with collections  Save and categorize content based on your preferences. 

Connection profiles capture identifiers for your data sources and destination databases. Each connection profile contains the minimum required amount of information Database Migration Service needs to facilitate data movement between the data source and destination.

That information includes:

  * **Connection profile name** : A human-readable name for your connection profile. This value is displayed in Database Migration Service in the Google Cloud console.

  * **Connection profile ID** : A machine-readable identifier for your connection profile. This value is used when you work with connection profiles by using Database Migration Service Google Cloud CLI commands or API.

  * **Region** : The region where your connection profile is saved. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases) must be saved in a single region. For more information on region requirements in Database Migration Service, see [ Product overview](https://docs.cloud.google.com/database-migration/docs/overview) in the main Database Migration Service documentation set.

  * For source connection profiles: **Backup files location** : The Cloud Storage bucket where you store the SQL Server backup and transaction log files that Database Migration Service transfers to your destination database. For Cloud SQL for SQL Server sources, this is the location where Database Migration Service automatically exports the backup files. For other sources, this is the location where you upload the backup files.

  * For destination connection profiles:

    * **Destination instance ID** : The identifier of your Cloud SQL for SQL Server destination instance where Database Migration Service transfers the data from the backup files stored in the Cloud Storage bucket.

    * **Username** and **password** for the migration database user in your destination instance. For more information on this user account, see [ Create and configure the Cloud SQL for SQL Server destination instance](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-cloud-sql-destination-instance).




## What's next

  * [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-source-connection-profile)
  * [ Create a destination connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-destination-connection-profile)
  * [ Manage connection profiles](https://docs.cloud.google.com/database-migration/docs/sqlserver/manage-connection-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
