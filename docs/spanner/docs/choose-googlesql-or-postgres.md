---
url: https://docs.cloud.google.com/spanner/docs/choose-googlesql-or-postgres/
title: Choosing the Right Dialect for Your Spanner Database \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:17.411977+00:00
---

# Choosing the Right Dialect for Your Spanner Database  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/choose-googlesql-or-postgres/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Choosing the Right Dialect for Your Spanner Database Stay organized with collections  Save and categorize content based on your preferences. 

When creating a Spanner database, you can choose between two SQL dialects: GoogleSQL and PostgreSQL. Both dialects offer the same core Spanner features, performance, and scalability. Requirements of applications, developers, and the ecosystem in which you work should inform your choice of dialect. This page lists the deciding factors between using GoogleSQL and PostgreSQL interface dialect databases.

**Key Considerations:**

  * **Portability** : if you choose PostgreSQL, you have the option of migrating from Spanner to another PostgreSQL database.
  * **Familiarity:** if your team is already familiar with either PostgreSQL or GoogleSQL syntax and tools, choosing that dialect can streamline development and reduce the learning curve.
  * **Ecosystem:** consider the tools and libraries available for each dialect. GoogleSQL is well-integrated with Google Cloud services, while PostgreSQL has a vast open-source ecosystem.
  * **Application requirements:** assess your application's specific requirements regarding SQL syntax, data types, and potential future needs.
  * **Migration:** if you are migrating from an existing database, choosing the dialect closer to your current environment might simplify the migration process.



If portability is your highest priority, giving you the option to move away from Google Cloud, choose PostgreSQL. If you want the tightest integration with Google Cloud (for example, to use BigQuery), then choose GoogleSQL.

**Spanner implementation of GoogleSQL and the PostgreSQL interface:**

  * **Feature parity:** Both GoogleSQL and PostgreSQL dialects provide equivalent support for Spanner's unique features, such as interleaved tables and query hints.
  * **Underlying engine:** Both dialects share the same underlying distributed storage and query processing engine, ensuring consistent performance, scalability, and reliability.
  * **Management and development:** You can manage and develop applications for both dialects using the same Spanner tools, APIs, and client libraries.



## What's next

  * Learn about [dialect parity between GoogleSQL and PostgreSQL](https://docs.cloud.google.com/spanner/docs/reference/dialect-differences).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
