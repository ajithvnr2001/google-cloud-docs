---
url: https://docs.cloud.google.com/sql/docs/postgres/assessments-overview/
title: Assess recommendations for Cloud SQL in Database Center \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:43.304517+00:00
---

# Assess recommendations for Cloud SQL in Database Center  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/assessments-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Assess recommendations for Cloud SQL in Database Center Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview — Assessments of a recommendation**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use assessments in [Database Center](https://docs.cloud.google.com/database-center/docs/overview) to assess and test the performance impact of database recommendations before you apply them to your production Cloud SQL for PostgreSQL instances.

To assess a recommendation, the assessment workflow performs these operations:

  * Clones your database instance.

  * Runs benchmarking simulation tests on the clone.

  * Compares the baseline performance of the clone against the performance after you apply the recommended configuration changes.




## How it works

When you assess a recommendation, the assessment workflow creates a step-by-step test plan that walks you through the assessment process.

After you've selected an instance for evaluation, the assessment can help measure the potential performance impact of the following kinds of changes:

  * **Machine type** : scale the [machine type](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview) up to better meet your specific workload needs.
  * **Edition type** : upgrade the [edition type](https://docs.cloud.google.com/sql/docs/postgres/editions-intro) from Enterprise or Enterprise Plus to access more robust features.
  * **Data cache** : enable [data caching](https://docs.cloud.google.com/sql/docs/postgres/data-cache) on your Enterprise Plus instances to access more storage for faster reads.



When you assess a recommendation, it does the following:

  1. To test the impact of these changes, the feature creates a temporary clone of the instance and runs a baseline benchmark test.

The clone is a copy of your instance that uses synthetic data in the form of [pgbench](https://www.postgresql.org/docs/current/pgbench.html) tables to abstract your data. [Data manipulation language (DML)](https://en.wikipedia.org/wiki/Data_manipulation_language) is used to help simulate traffic, and the parameters available in pgbench let you indicate the workload type and duration.

For example, you can indicate that you want the clone to run using the following parameters:

     * 10 database client connections.
     * 1,000 transactions per client.
     * Simple query mode.

Given these parameters, the assessments workflow can first measure performance of the clone with the instance's current configuration, and then compare it with a version of the clone where the recommended modifications are applied. Measured performance metrics include the following temporary results:

     * Scorecard/Table: Average latency, number of transactions
     * Charts: CPU utilization, memory usage
  2. The assessments workflow applies the recommended changes to the clone through a patch operation and runs the benchmark again. Depending on instance capacity and the type of modifications made, changes to configuration settings can take 45 minutes or longer to complete.

  3. The assessments workflow records performance metrics and compares them to the previously recorded baseline.




By using assessments, you can safely validate the recommended changes to a clone in a test environment before applying them manually to its corresponding production instance.

If you're satisfied with the benchmark results, then you can manually apply the recommendation changes to your production instance.

After 48 hours, the assessment plan and the results are deleted.

The clone instance is deleted as soon as the workflow completes.

If the assessment plan is cancelled or interrupted, then you must delete the clone manually.

For more information, see [Create an assessment of a recommendation](https://docs.cloud.google.com/database-center/docs/assessments).

## Limitations

  * The results from the assessment plan, and any resources the clone requires, are available for 48 hours before being deleted. Resources accrue charges until deletion.

  * If you cancel or interrupt the assessment session, or the assessment fails, you must delete the clone manually to prevent ongoing charges.

  * Database Center assessments are available only for Cloud SQL for PostgreSQL instances.




## What's next

  * [Learn how to run assessments in Database Center](https://docs.cloud.google.com/database-center/docs/assessments)
  * [Database Center overview](https://docs.cloud.google.com/database-center/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
