---
url: https://docs.cloud.google.com/sql/docs/sqlserver/built-in-authentication/
title: Cloud SQL built-in database authentication \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:29.833349+00:00
---

# Cloud SQL built-in database authentication  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/built-in-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Cloud SQL built-in database authentication Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/built-in-authentication "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication "View this page for the PostgreSQL database engine") | SQL Server

This page describes how built-in authentication works on Cloud SQL instances.

## Introduction

Authentication is the process of verifying the identity of a user who is attempting to access an instance. Cloud SQL uses the following types of authentication for database users:

  * The database's built-in authentication uses a username and a password to authenticate local database users. For more information, see the following resources: 
    * [Create and manage users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users)
    * [About SQL Server users](https://docs.cloud.google.com/sql/docs/sqlserver/users)
  * [Authentication using Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/sql/docs/sqlserver/ad).
  * [Authentication using customer-managed Microsoft AD](https://docs.cloud.google.com/sql/docs/sqlserver/cmad).
  * [Authentication using Microsoft Entra ID](https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id).



Although Active Directory or Microsoft Entra ID authentication can be more secure and reliable, you might prefer to use built-in authentication or a hybrid authentication model that includes different authentication types.

## Limitations

  * Cloud SQL for SQL Server doesn't support the following capabilities: 
    * Custom password policies
    * IAM database authentication
    * IAM authentication for database operations
  * Cloud SQL for SQL Serversupports IAM authentication for instance and backup operations only. For more information, see [IAM authentication](https://docs.cloud.google.com/sql/docs/sqlserver/iam-authentication).



## What's next

  * [Create an instance and set the password policy](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).
  * [Create users with built-in authentication](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
