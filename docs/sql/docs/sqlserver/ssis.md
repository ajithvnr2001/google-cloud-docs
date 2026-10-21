---
url: https://docs.cloud.google.com/sql/docs/sqlserver/ssis/
title: SQL Server Integration Services (SSIS) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:35.285734+00:00
---

# SQL Server Integration Services (SSIS)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/ssis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  SQL Server Integration Services (SSIS) Stay organized with collections  Save and categorize content based on your preferences. 

Cloud SQL supports the [SQL Server Integration Services (SSIS)](https://learn.microsoft.com/en-us/sql/integration-services/sql-server-integration-services?view=sql-server-ver16) component. SSIS doesn't need any configuration to work with Cloud SQL. It works with any managed SQL Server instance. 

This page provides the prerequisites, limitations, and recommendations for using SSIS on Cloud SQL.

## Prerequisites

Before using SSIS on Cloud SQL, you must have the following:

  1. A host where you install and run Microsoft SQL Server Integration Services. It can be either a Compute Engine VM or a host that doesn't use Compute Engine. For installation instructions, see [Install Integration Services (SSIS)](https://learn.microsoft.com/en-us/sql/integration-services/install-windows/install-integration-services?view=sql-server-ver16).
  2. If you plan to use Windows Authentication, you must use either Managed Service for Microsoft Active Directory or customer-managed Active Directory to join the SQL Server instance and the host running SSIS. For more information, see [Configure Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad) or [Configure customer-managed Active Directory](https://docs.cloud.google.com/sql/docs/sqlserver/configure-cmad).



## Limitations

  * You can't host SSIS packages on or execute them from Cloud SQL.

  * Cloud SQL doesn't support the SSISDB catalog. However, you can deploy SSISDB catalogs to a SQL Server instance that is not on Cloud SQL and manage them from there.




## Recommendations

Cloud Data Fusion provides an interface that lets you deploy code-free ETL (extract, transform, load) and ELT (extract, load, transform) data pipelines. We recommend that your solution include ETL/ELT data pipelines because they provide a library of over 150 preconfigured connectors and transformations, with no additional cost. For more information about using Cloud Data Fusion with SQL Server, see [Reading from a SQL Server table](https://cloud.google.com/data-fusion/docs/how-to/reading-from-sqlserver).

## What's next

To learn how to author and execute SSIS packages, see [Create a project and basic package with SSIS](https://learn.microsoft.com/en-us/sql/integration-services/lesson-1-create-a-project-and-basic-package-with-ssis).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
