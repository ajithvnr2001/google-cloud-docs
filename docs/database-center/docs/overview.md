---
url: https://docs.cloud.google.com/database-center/docs/overview/
title: Database Center overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:45.542515+00:00
---

# Database Center overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)
  * [ Guides ](https://docs.cloud.google.com/database-center/docs/overview)



Send feedback 

#  Database Center overview Stay organized with collections  Save and categorize content based on your preferences. 

Database Center is an AI-assisted dashboard that gives you one centralized view across your entire database fleet. You can view database fleet health issues and recommendations, and you can ask questions about database fleet health issues, including availability configuration, data protection, security, and industry compliance.

Database Center aggregates and summarizes your fleet's top-level health issues based on data from your Google Cloud projects and Security Command Center and then advises you on how to investigate affected projects or instances. The Database Center dashboard displays the number of issues for each health issue category. For more information about the health issues for supported Google Cloud database products, see [Supported health issues](https://docs.cloud.google.com/database-center/docs/database-health-issues#supported-health-issues).

Data displayed in Database Center is not updated in real time. Data is usually updated within a few minutes, but sometimes data may take up to 24 hours to update.

Database Center supports health issues for the following Google Cloud database products:

  * AlloyDB for PostgreSQL
  * Bigtable
  * Cloud SQL for MySQL
  * Cloud SQL for PostgreSQL
  * Cloud SQL for SQL Server
  * Firestore
  * Memorystore for Redis
  * Memorystore for Redis Cluster
  * MySQL running on a Compute Engine (VM) ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * Oracle Database@Google Cloud
  * PostgreSQL running on a Compute Engine (VM) ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * Spanner
  * SQL Server running on a Compute Engine virtual machine (VM) ([Preview](https://cloud.google.com/products/#product-launch-stages))



While Database Center supports the following database products, it doesn't monitor their health issues.

  * BigQuery: Supports resource inventory monitoring.
  * Memorystore for Valkey: Supports resource inventory and metrics monitoring.



[Gemini](https://docs.cloud.google.com/gemini/docs/overview) chat is available in Database Center to respond to your questions about database fleet health, giving you customized recommendations based on your Google Cloud projects, and helping you identify and implement the right policies for your database fleets.

## Database Center benefits

Database Center is particularly useful if your cloud resources are distributed across many different products and if your organization uses many different projects. For example, database platform teams can use Database Center to identify compliance risks and enforce best practices, while site reliability engineers can use Database Center to help ensure that their database resources are protected against downtime.

Database Center also helps reduce your database governance risks. _Database governance_ is defined as the practices and tools that help you monitor and protect access to sensitive data throughout its lifecycle, from acquisition through use and disposal.

## Types of health issues that you can monitor

You can use Database Center to determine the following about your database fleet's health:

  * Your overall Google Cloud database footprint.
  * The database engines and versions that you're using across your database fleet.
  * Whether your critical databases are optimized for availability. If your databases aren't optimized, Database Center helps you identify which databases are most at risk of downtime.
  * How well your critical databases are protected against disasters and data corruption, if they're regularly backed up. If your databases aren't backed up, Database Center helps you determine which databases aren't protected.
  * Whether your database resources are configured to follow security best practices.
  * Whether your databases are compliant with industry standards, and if not, which databases are out of compliance.



## What's next

  * [Learn about database health issues](https://docs.cloud.google.com/database-center/docs/database-health-issues).
  * [Get started with Database Center](https://docs.cloud.google.com/database-center/docs/set-up-database-center).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
