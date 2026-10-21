---
url: https://docs.cloud.google.com/dataflow/docs/deprecations/dataflow-sql/
title: Dataflow SQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:20.489820+00:00
---

# Dataflow SQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/deprecations/dataflow-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Resources ](https://docs.cloud.google.com/dataflow/docs/resources)



Send feedback 

#  Dataflow SQL Stay organized with collections  Save and categorize content based on your preferences. 

Dataflow has ended support for Dataflow SQL. This is a breaking change. 

  * As of July 31, 2024, you can't access Dataflow SQL in the Google Cloud console.
  * As of January 31, 2025, you can't use Dataflow SQL in the Google Cloud CLI.



## Replacement: Beam SQL

[Beam SQL](https://docs.cloud.google.com/dataflow/docs/guides/notebook-advanced#beam-sql) lets you query bounded and unbounded `PCollections` with SQL statements. If you're working in an Apache Beam notebook, you can use the IPython [custom magic](https://ipython.readthedocs.io/en/stable/config/custommagics.html) `beam_sql` to speed up your pipeline development.

Beam SQL provides similar functionality as Dataflow SQL, using SQL statements to query `PCollections`.

## Migration

We recommend that you begin migrating your Dataflow SQL query to Beam SQL as soon as possible.

Moving to Beam SQL is a breaking change that affects any Dataflow SQL job or query. **You will need to rebuild these jobs and queries.**

With this change, you can't create new Dataflow SQL jobs. However, this change doesn't affect Dataflow SQL jobs that are already running.

For information about creating queries in Beam SQL, see [Beam SQL and `beam_sql` magic](https://docs.cloud.google.com/dataflow/docs/guides/notebook-advanced#beam-sql) and [Beam SQL overview](https://beam.apache.org/documentation/dsls/sql/overview/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
