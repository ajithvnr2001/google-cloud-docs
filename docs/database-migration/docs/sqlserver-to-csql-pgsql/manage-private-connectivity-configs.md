---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/manage-private-connectivity-configs/
title: View a private connectivity configuration for the source database \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:17.939005+00:00
---

# View a private connectivity configuration for the source database  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/manage-private-connectivity-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  View a private connectivity configuration for the source database Stay organized with collections  Save and categorize content based on your preferences. 

In this section, you learn how to view high-level and detailed information about a private connectivity configuration.

## View high-level information

High-level information about a private connectivity configuration includes:

  * The name of the private connectivity configuration.
  * The status of the configuration (`Active` or `Inactive`). If the status is `Active`, then the number of connection profiles to which the configuration is assigned appears.
  * When the configuration was created.
  * The region where the configuration is established.
  * The VPC network that you selected for the configuration when you [ created it](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-private-connectivity-configuration).
  * The subnet on your VPC network that's assigned to this configuration.



## View detailed information

In addition to viewing high-level information about a private connectivity configuration, you can click a configuration to see additional information, including:

  * The ID of the private connectivity configuration.
  * A link to the VPC network.
  * Additional information about the connection profiles that use the private connectivity configuration.


  1. In the Google Cloud console, go to the **Private connectivity configurations** page. 

[ Go to Private connectivity configurations](https://console.cloud.google.com/dbmigration/private-connections)

  2. Click the configuration for which you want to see detailed information. This information appears on the **Private connectivity configuration details** page. 
  3. After you verify the information about a private connectivity configuration, you can use it to [ create a source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-source-connection-profile). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
