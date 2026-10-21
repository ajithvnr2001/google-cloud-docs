---
url: https://docs.cloud.google.com/spanner/docs/application-migration/
title: Migrate your application code \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:54.598876+00:00
---

# Migrate your application code  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/application-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Migrate your application code Stay organized with collections  Save and categorize content based on your preferences. 

A typical application uses a client, such as a low-level driver or an object-relational mapper (ORM) to connect to the database. Spanner supports clients in multiple languages that let you use common libraries, such as JDBC, across developer environments. For more information, see [Overview of drivers](https://docs.cloud.google.com/spanner/docs/drivers-overview).

In addition to managing how your application connects to Spanner, you also have to manage which queries are sent and which syntax the queries are using. Spanner supports two SQL dialects, both based on ANSI SQL standard. You can choose to use GoogleSQL or PostgreSQL interface for Spanner based on the ecosystem you want to operate in. For more information, see [Choosing the right dialect for your Spanner database](https://docs.cloud.google.com/spanner/docs/choose-googlesql-or-postgres). Because of the architectural differences between the Spanner database and your source database, the syntax used in Spanner might not align with the syntax of your source database.

Complete the following steps manually to migrate your application to Spanner:

  * Spanner doesn't support running user code in the database, so you need to move any procedures and triggers stored at the database level into the application.

  * Use Spanner client libraries and ORMs. For more information, see [Overview of APIs, client libraries, and ORM drivers](https://docs.cloud.google.com/spanner/docs/api-libraries-overview).

  * Take note of [Spanner partitioned DML](https://docs.cloud.google.com/spanner/docs/dml-partitioned), [read-only transactions](https://docs.cloud.google.com/spanner/docs/transactions#read-only_transactions), [commit timestamps](https://docs.cloud.google.com/spanner/docs/commit-timestamp), and read timestamps and how they can optimize application performance.

  * You also might need to make changes to transaction handling. Consider the following:

    * The mutations per commit limit is 80,000. Each secondary index on a table is an additional mutation per row. To modify data using mutations, see [Insert, update, and delete data using mutations](https://docs.cloud.google.com/spanner/docs/modify-mutation-api). To modify a large amount of data, use [partitioned DML](https://docs.cloud.google.com/spanner/docs/dml-partitioned).



[ Previous arrow_back  Migrate your schema  ](https://docs.cloud.google.com/spanner/docs/schema-migration)

[ Next Optimize your schema and application performance  arrow_forward  ](https://docs.cloud.google.com/spanner/docs/optimize-schema-performance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
