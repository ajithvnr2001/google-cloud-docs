---
url: https://docs.cloud.google.com/spanner/docs/fgac-models/
title: Fine-grained access control for models \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:35.357868+00:00
---

# Fine-grained access control for models  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/fgac-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Fine-grained access control for models Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how [fine-grained access control](https://docs.cloud.google.com/spanner/docs/fgac-about) works with Spanner models.

For fine-grained access control users, you can control access to MODEL entities with the following privilege:

  * Grant `EXECUTE` on the model to allow [machine learning functions](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/ml-functions) to use it.

###  GoogleSQL 
        
        GRANT EXECUTE ON MODEL MODEL_NAME TO ROLE ROLE_NAME;
        




## `INFORMATION_SCHEMA` views for models

The following views show the database roles and privileges information for models:

  * GoogleSQL-dialect databases: [`INFORMATION_SCHEMA.MODEL_PRIVILEGES`](https://docs.cloud.google.com/spanner/docs/information-schema#model-privileges)



The rows in this view are filtered based on the current database role's privileges on models. This ensures that principals can view only the roles, privileges, and models that they have access to.

Row filtering also applies to the following model-related views:

###  GoogleSQL 

  * [`INFORMATION_SCHEMA.MODELS`](https://docs.cloud.google.com/spanner/docs/information-schema#models)
  * [`INFORMATION_SCHEMA.MODEL_OPTIONS`](https://docs.cloud.google.com/spanner/docs/information-schema#model-options)
  * [`INFORMATION_SCHEMA.MODEL_COLUMNS`](https://docs.cloud.google.com/spanner/docs/information-schema#model-columns)
  * [`INFORMATION_SCHEMA.MODEL_COLUMN_OPTIONS`](https://docs.cloud.google.com/spanner/docs/information-schema#model-column-options)



The system role `spanner_info_reader` and its members always see an unfiltered `INFORMATION_SCHEMA`.

## More information

  * [About models](https://docs.cloud.google.com/spanner/docs/ml)
  * [Create and manage models](https://docs.cloud.google.com/spanner/docs/ml-tutorial)
  * [About fine-grained access control](https://docs.cloud.google.com/spanner/docs/fgac-about)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
