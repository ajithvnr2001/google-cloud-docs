---
url: https://docs.cloud.google.com/sql/docs/sqlserver/db-versions/
title: Database versions and version policies \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:54.637719+00:00
---

# Database versions and version policies  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/db-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/sqlserver/resources)



Send feedback 

#  Database versions and version policies Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/db-versions "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/db-versions "View this page for the PostgreSQL database engine") | SQL Server

This page describes Cloud SQL's database version support policies.

## Database versions supported by Cloud SQL

The database engines supported by Cloud SQL include multiple versions. The versions can vary in capabilities and in the types of issues that arise. While performing an upgrade can impact your users, providing up-to-date database features and important patches is also critical. Cloud SQL keeps your instances up-to-date with patches and minor version updates automatically.

## Major and minor versions supported by Cloud SQL

Cloud SQL supports the following database versions.

The mainstream end date and the Microsoft extended support end dates follow the [Microsoft SQL Server support lifecycle](https://learn.microsoft.com/en-us/lifecycle/products/). These dates are different than the Cloud SQL extended support dates that apply to Cloud SQL for PostgreSQL and Cloud SQL for MySQL.

While Cloud SQL does charge for extended support for MySQL and PostgreSQL, Cloud SQL doesn't charge for extended support for Microsoft SQL Server.

Major version| Minor version| Support start date| Mainstream support  
end date| Extended support  
end date  
---|---|---|---|---  
SQL Server 2025 Standard| CU2| November 18, 2025| [January 6, 2031](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2025)| January 6, 2036  
SQL Server 2025 Enterprise| CU2| November 18, 2025| [January 6, 2031](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2025)| January 6, 2036  
SQL Server 2025 Express| CU2| November 18, 2025| [January 6, 2031](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2025)| January 6, 2036  
SQL Server 2022 Standard| CU19| June 26, 2023| [January 11, 2028](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2022)| January 11, 2033  
SQL Server 2022 Enterprise| CU19| June 26, 2023| [January 11, 2028](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2022)| January 11, 2033  
SQL Server 2022 Express| CU19| June 26, 2023| [January 11, 2028](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2022)| January 11, 2033  
SQL Server 2022 Web| CU19| June 26, 2023| [January 11, 2028](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2022)| January 11, 2033  
SQL Server 2019 Standard| CU32| June 24, 2021| [February 28, 2025](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2019)| January 8, 2030  
SQL Server 2019 Enterprise| CU32| June 24, 2021| [February 28, 2025](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2019)| January 8, 2030  
SQL Server 2019 Express| CU32| June 24, 2021| [February 28, 2025](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2019)| January 8, 2030  
SQL Server 2019 Web| CU32| June 24, 2021| [February 28, 2025](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2019)| January 8, 2030  
SQL Server 2017 Standard1| CU31| February 19, 2020| [October 11, 2022](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2017)| October 13, 2027  
SQL Server 2017 Enterprise1| CU31| February 19, 2020| [October 11, 2022](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2017)| October 13, 2027  
SQL Server 2017 Express1| CU31| February 19, 2020| [October 11, 2022](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2017)| October 13, 2027  
SQL Server 2017 Web1| CU31| February 19, 2020| [October 11, 2022](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2017)| October 13, 2027  
  
1: Beginning April 12, 2027, you won't be able to create new instances of Cloud SQL for SQL Server 2017. Starting on October 13, 2027, SQL Server 2017 will reach end of life (EOL) and Microsoft will stop releasing [security updates](https://learn.microsoft.com/en-us/sql/sql-server/end-of-support/sql-server-end-of-support-overview?view=sql-server-ver17#understand-the-sql-server-lifecycle). Cloud SQL for SQL Server will stop supporting SQL Server 2017 after this date.

## Cloud SQL database version format

For SQL Server, the year provides the major version number and the minor version is the supported Cumulative Update (CU). For example, for SQL Server 2022 Enterprise CU11, **2022 Enterprise** is the major version number and **CU11** is the minor version number. 

### How to identify the database version of your Cloud SQL instance

You specify the database version when you create a Cloud SQL instance. If you don't specify a database version, then Cloud SQL uses the default database version.

To view the database version of a Cloud SQL instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name.
  3. In the **Configuration** card, view the **Database version**.



To filter instances by a specific database version within your Cloud SQL project, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. In the **Filter** field, select **Type**. The database versions that are within your project are listed.
  3. To filter the instances, select a database version within your project.



To view all Cloud SQL instances and their database versions in your organization, use [Database Center](https://docs.cloud.google.com/database-center/docs/overview). You can also switch views in Database Center from project to folders or organizations to get a complete list of all your Cloud SQL instances. For more information, see [Filter resources and export fleet inventory information](https://docs.cloud.google.com/database-center/docs/filter-resources-export-fleet-inventory-information).

## Minor version support

Cloud SQL supports new minor versions within three months of their general availability release by the database engine developer community. After Cloud SQL supports a new minor version, Cloud SQL provisions new instances on the new version automatically. During the next scheduled maintenance rollout, Cloud SQL upgrades existing instances to the new version. 

Cloud SQL determines the target minor version for each database engine. When the target minor version is different from the minor version for a Cloud SQL instance, Cloud SQL upgrades that version during the next maintenance cycle. You can control the day and time when maintenance restarts occur by [setting a maintenance window](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window) for your instance.

**Note:** Cloud SQL might not support each new minor version released by the database engine developer. For example, Cloud SQL might not support a minor version that's found not to work well with Cloud SQL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
