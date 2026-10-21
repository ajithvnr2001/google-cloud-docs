---
url: https://docs.cloud.google.com/spanner/docs/databases/
title: Databases overview \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:13.189989+00:00
---

# Databases overview  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Databases overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Spanner databases and their properties.

## Overview

A Spanner database is a container for your tables, views, and indexes. Each Spanner instance can have multiple databases.

In the Spanner hierarchy, a database is a child of an [instance](https://docs.cloud.google.com/spanner/docs/instances), and the parent of a [schema](https://docs.cloud.google.com/spanner/docs/schema-and-data-model).

A database inherits properties from its parent instance, such as its configuration (regional or multi-region), the available [compute capacity](https://docs.cloud.google.com/spanner/docs/compute-capacity), and the available storage.

Properties that are set on the database are:

  * The [dialect](https://docs.cloud.google.com/spanner/docs/postgresql-interface#choosing_between_and). Spanner supports GoogleSQL and PostgreSQL. All of the tables in a database must use the same dialect.
  * An [IAM policy](https://docs.cloud.google.com/spanner/docs/grant-permissions#database-level_permissions). The access rules defined by this policy are applied to the tables and data inside the database.
  * The type of encryption key to use. The default is a Google-owned and Google-managed encryption key; a [customer-managed encryption key](https://docs.cloud.google.com/spanner/docs/cmek) is also supported.
  * [Database deletion protection](https://docs.cloud.google.com/spanner/docs/prevent-database-deletion) to prevent accidental deletion of databases.
  * Database policies such as the default leader region, query optimizer version, query optimizer statistics package version, and version retention period, can be set or modified with DDL statements. See the DDL reference for [GoogleSQL](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#alter-database) or [PostgreSQL](https://docs.cloud.google.com/spanner/docs/reference/postgresql/data-definition-language#alter-database).



Database limits, including the number of databases allowed per instance, and the number of tables allowed per database, are defined on the [Quotas and limits](https://docs.cloud.google.com/spanner/quotas) page.

## Considerations

Before creating a database, consider the implications of your schema design. Read [Schema design best practices](https://docs.cloud.google.com/spanner/docs/schema-design), as well as the [Schema and data model](https://docs.cloud.google.com/spanner/docs/schema-and-data-model) document, particularly the section on [Designing for multi-tenancy](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#multitenancy).

## What's next

  * [Create and manage databases](https://docs.cloud.google.com/spanner/docs/create-manage-databases)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
