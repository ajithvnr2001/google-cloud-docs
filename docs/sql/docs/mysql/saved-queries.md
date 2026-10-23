---
url: https://docs.cloud.google.com/sql/docs/mysql/saved-queries/
title: Saved queries overview \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:34.846656+00:00
---

# Saved queries overview  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/saved-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Saved queries overview Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/saved-queries "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/saved-queries "View this page for the SQL Server database engine")

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To store, reuse, and share frequently run database statements without rewriting them for each session, you can use saved queries in Cloud SQL for MySQL .

You can use Cloud SQL Studio to create, save, and manage SQL scripts as saved queries. The saved queries capability is available only in the console; you cannot run or manage saved queries through an API or other means.

Saved queries have the following characteristics:

  * Google-owned and Google-managed encryption keys encrypt all queries at rest.
  * A saved query is a child of a project.
  * Saved queries are deleted when the project is deleted. If you delete the instance or database, you can still access saved queries in the project using the [**Saved queries** page](https://docs.cloud.google.com/sql/docs/mysql/create-manage-saved-queries) in the Google Cloud console.
  * You must have the correct [Identity and Access Management (IAM) role or permissions](https://docs.cloud.google.com/sql/docs/mysql/create-manage-saved-queries#required-roles) to view and manage saved queries.
  * You can only access saved queries using Cloud SQL Studio or by navigating to the **Saved queries** page in the Google Cloud console. Saved queries aren't accessible through the API.



## Storage location

Cloud SQL for MySQL attempts to store queries in the same location as the database. However, storage for saved queries is available in a limited number of locations, so it might select another region by default. To view and update the location where your saved queries are stored, first click **Show Advanced Options** from the save subtask. Then, from the **Region** list, select an available location.

## Limitations

Saved queries has the following limitations:

  * There is a rate limit of 20 queries per second (QPS) per user per project, including both read and write. This quota is not trackable or overridable.
  * You can't create more than 10,000 saved queries in a project—including saved queries for other Google Cloud products. For more information, see [Quotas and limits](https://docs.cloud.google.com/sql/docs/quotas) .
  * You can't use [customer-managed encryption keys](https://docs.cloud.google.com/spanner/docs/cmek) for instances with saved queries.



## Pricing

There is no additional charge for using or storing saved queries.

## What's next

  * Learn how to [create and manage saved queries](https://docs.cloud.google.com/sql/docs/mysql/create-manage-saved-queries) . 
  * Learn how to [manage data using the Google Cloud console](https://docs.cloud.google.com/sql/docs/mysql/manage-data-using-studio). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
