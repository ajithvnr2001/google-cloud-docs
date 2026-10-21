---
url: https://docs.cloud.google.com/lakehouse/docs/table-rules/
title: Table management and security rules \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:56.861492+00:00
---

# Table management and security rules  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/table-rules/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Table management and security rules Stay organized with collections  Save and categorize content based on your preferences. 

When creating and managing tables in the Apache Iceberg REST catalog endpoint, the following location, permission, and security hardening rules apply:

## Table location

Table paths must be nested within the parent namespace path (for example, `gs://{namespace_path}/.../{table_name}`). This constraint is enforced to help with security and catalog hardening.

**Behavior change for table paths:** Note that the resulting table location (under which the `metadata/` folder is created) automatically has a random string attached as a suffix to prevent conflicts and improve security:

  * If no specific location is provided, the resulting location is `gs://{namespace_path}/{table_name}/{random_suffix}`.
  * If a specific location is provided (for example, `gs://{namespace_path}/.../{table_name}`), the resulting location is `gs://{namespace_path}/.../{table_name}/{random_suffix}`.



## Table registration permissions

Both multiple-bucket and single-bucket catalogs require the `biglake.tables.register` permission to register a table. This permission is restricted to the BigLake Admin (`roles/biglake.admin`) role to ensure only administrators can perform table registration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
