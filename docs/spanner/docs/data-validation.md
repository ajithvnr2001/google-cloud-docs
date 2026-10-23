---
url: https://docs.cloud.google.com/spanner/docs/data-validation/
title: Validate your data migration \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:58.461674+00:00
---

# Validate your data migration  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/data-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Validate your data migration Stay organized with collections  Save and categorize content based on your preferences. 

Data validation is the process of comparing data from both the source and the destination database tables to ensure they match.

The [Data Validation Tool (DVT)](https://pypi.org/project/google-pso-data-validator/#:%7E:text=The%20Data%20Validation%20Tool%20is,with%20multi%2Dleveled%20validation%20functions) is an open source tool that can connect to data stores and perform checks between your source database and Spanner. We recommend using it to perform basic validations as a part of your migration, such as the following:

  * Check that all tables were created and that all schema mappings are correct.
  * Match the total number of rows for each table.
  * Extract random rows to verify consistency.
  * Validate your columns, for example, use `count`, `sum`, `avg`, `min`, `max`, or `group by`.
  * Compare any cyclic redundancy checks or hash functions at the row level.



To perform more specific validations, build custom checks during migration.

[ Previous arrow_back  Migrate your data  ](https://docs.cloud.google.com/spanner/docs/data-migration)

[ Next Configure fallback and cutover  arrow_forward  ](https://docs.cloud.google.com/spanner/docs/cutover-fallback)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
