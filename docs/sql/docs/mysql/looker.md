---
url: https://docs.cloud.google.com/sql/docs/mysql/looker/
title: Use Looker with Cloud SQL \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:53.122119+00:00
---

# Use Looker with Cloud SQL  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/looker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use Looker with Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/looker "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/looker "View this page for the SQL Server database engine")

This page gives a short overview of Looker and describes the benefits of using it with Cloud SQL. To use Looker with Cloud SQL now, see the [instructions for connecting Looker to Cloud SQL](https://docs.looker.com/setup-and-management/database-config/google-cloud-sql).

Looker is an enterprise platform for business intelligence, data applications, and embedded analytics. Looker helps you explore, share, and visualize your company's data so that you can make better business decisions.

## How Looker works

Looker lets data experts at each organization describe their data using a lightweight modeling language called LookML. LookML tells Looker how to query data, so everyone in the organization can create easy-to-read reports and dashboards to explore patterns of data. Looker offers additional features for creating custom data applications and experiences.

Looker's platform works with transactional databases and analytical datastores. Looker lets you create consistent data models on top of all your data with speed and accuracy. It also offers a unified surface to access all of an organization's data.

## Restrictions

Cloud SQL doesn't support the following [Looker features](https://docs.looker.com/setup-and-management/database-config/google-cloud-sql#feature_support):

  * Persistent Native Derived Tables
  * Stable views
  * Case sensitive
  * Oauth credentials
  * Connection pooling
  * HLL sketches
  * Incremental PDTS
  * Materialized views
  * Approximate count distinct



Google Cloud SQL doesn't support `CREATE TABLE AS SELECT` statements, so you must use the [`create_process`](https://docs.looker.com/reference/view-params/create_process) LookML parameter to define Persistent Native Derived Tables (PDTs).

## Looker integration with Cloud SQL

Looker supports hosting in Google Cloud. Because Looker is platform independent, it connects to data in Cloud SQL and other public clouds.

If you already have a Looker instance running, see the [instructions for connecting Looker to Cloud SQL](https://docs.looker.com/setup-and-management/database-config/google-cloud-sql).

## What's next

There are many options related to administering Looker, customizing its data model, and exposing data to users. For more information, see the following resources:

  * [Looker Documentation](https://docs.looker.com/)
  * [Looker Help Center](https://help.looker.com/)
  * [Looker Training](https://training.looker.com/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
