---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-connection-profiles/
title: About connection profiles \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:10:49.534286+00:00
---

# About connection profiles  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-connection-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  About connection profiles Stay organized with collections  Save and categorize content based on your preferences. 

Connection profiles capture identifiers for your data sources and destination databases. Each connection profile contains the minimum required amount of information Database Migration Service needs to facilitate data movement between the data source and destination.

That information includes:

  * **Connection profile name** : A human-readable name for your connection profile. This value is displayed in Database Migration Service in the Google Cloud console.

  * **Connection profile ID** : A machine-readable identifier for your connection profile. This value is used when you work with connection profiles by using Database Migration Service Google Cloud CLI commands or API.

  * **Region** : The region where your connection profile is saved. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region. For more information on region requirements in Database Migration Service, see [ Product overview](https://docs.cloud.google.com/database-migration/docs/overview) in the main Database Migration Service documentation set.

  * **Username** and **password** for the dedicated migration user in the source or destination database.

  * **Connectivity information** : IP or hostname, port, migration user account name and password.

Connection details differ depending on what connectivity method you use. Source and destination connection profiles can use different connectivity methods. See [ Networking overview](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/networking-overview).




## What's next

Learn more about how to:

  * [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-source-connection-profile)
  * [ Create a destination connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-destination-connection-profile)
  * [ Manage connection profiles](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/manage-connection-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
