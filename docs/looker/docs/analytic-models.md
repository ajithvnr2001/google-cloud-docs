---
url: https://docs.cloud.google.com/looker/docs/analytic-models/
title: In-database analytic models \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:43.910727+00:00
---

# In-database analytic models  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/analytic-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  In-database analytic models Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms](https://cloud.google.com/terms/service-terms#1) section of the Service Specific Terms. Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

If you encounter an issue during the Public Preview of Looker support of in-database analytic models, report it to [database_analytic_models_feedback@google.com](mailto:database_analytic_models_feedback@google.com).

Looker integrates with in-database analytic models, such as [BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-overview) and [Snowflake semantic views](https://docs.snowflake.com/en/user-guide/views-semantic/overview), so that you can keep your semantic definitions consistent across Looker and other BI tools, applications, or workloads that interface with your data warehouse.

Looker lets you manage your in-database analytic models by using the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide), [version control](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes), and [Continuous Integration](https://docs.cloud.google.com/looker/docs/continuous-integration). You can also use Looker to query your analytic models that are stored in your database directly from Looker Explores and visualizations.

Looker supports three methods for integrating with in-database analytic models:

  1. **Database-managed analytic model:** You first define and manage the analytic model directly in your database, and then you create a LookML view in Looker so that you can use Looker to query your analytic model. For information about setting up a database-managed analytic model, see the [`sql_analytic_model_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-analytic-model-name) documentation page.

  2. **Looker-managed, SQL-based analytic model:** You define the analytic model in Looker by using SQL commands. Looker then creates and maintains the analytic model within your database based on your definition. For information about setting up a Looker-managed, SQL-based analytic model, see the [SQL-based derived analytic models](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-analytic-model#sql-based-derived-analytic-models) section on the [`derived_analytic_model`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-analytic-model) documentation page.

  3. **Looker-managed, LookML-based derived analytic model:** You define the analytic model by referencing an existing LookML Explore with the `model_source` parameter. Looker automatically translates your Explore topology, joins, dimensions, and measures into database-native analytic model DDL statements (such as node and edge tables for BigQuery Graph or tables and relationships for Snowflake semantic views) and creates and manages the model in your database. For information about setting up Looker-managed, LookML-based derived analytic model, see the [LookML-based derived analytic models](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-analytic-model#lookml-based-derived-analytic-models) section on the [`derived_analytic_model`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-analytic-model) documentation page.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
