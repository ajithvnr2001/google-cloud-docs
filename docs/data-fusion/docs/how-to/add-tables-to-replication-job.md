---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/add-tables-to-replication-job/
title: Add tables to a replication job \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:35.408881+00:00
---

# Add tables to a replication job  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/add-tables-to-replication-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Add tables to a replication job Stay organized with collections  Save and categorize content based on your preferences. 

After you deploy a replication job, you cannot edit or add tables to it. Instead, add the tables to a new or duplicate replication job.

## Option 1: Create a new replication job

Adding tables to a new job is the simplest approach. It prevents historical reloading of all the tables and prevents data inconsistency issues.

The drawbacks are the increased overhead of managing multiple replication jobs and the consumption of more compute resources, as each job runs on a separate ephemeral Managed Service for Apache Spark cluster by default. The latter can be mitigated to some extent by using a shared static Managed Service for Apache Spark cluster for both jobs.

For more information about creating new jobs, see the [Replication tutorials](https://docs.cloud.google.com/data-fusion/docs/how-to/using-replication).

For more information about using static Managed Service for Apache Spark cluster in Cloud Data Fusion, see [Run a pipeline against an existing Managed Service for Apache Spark cluster](https://docs.cloud.google.com/data-fusion/docs/how-to/running-against-existing-dataproc)

## Option 2: Stop the current replication job and create a duplicate

If you duplicate the replication job to add the tables, consider the following:

  * Enabling the snapshot for the duplicate job results in the historical load of all the tables from scratch. This is recommended if you cannot use the previous option, where you run separate jobs.

  * Disabling the snapshot to prevent the historical load can result in data loss, as there could be missed events between when the old pipeline stops and the new one starts. Creating an overlap to mitigate this issue isn't recommended, as it can also result in data loss—historical data for the new tables isn't replicated.




To create a duplicate replication job, follow these steps:

  1. Stop the existing pipeline.

  2. From the Replication jobs page, locate the job that you want to duplicate, click more_vert and **Duplicate**.

  3. Enable the snapshot:

     1. Go to **Configure source**.
     2. In the **Replicate existing data** field, select **Yes**.
  4. Add tables in the **Select tables and transformations** window and follow the wizard to deploy the replication pipeline.


**Note:** If you run a duplicate replication job against the same target BigQuery dataset as the original job, don't run the original job again, as it can cause data inconsistency.

## What's next

  * Learn more about [Replication](https://docs.cloud.google.com/data-fusion/docs/concepts/replication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
