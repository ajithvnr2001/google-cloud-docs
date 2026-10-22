---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/change-schemas-in-replication/
title: Change schemas in a SQL Server replication job \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:43.509446+00:00
---

# Change schemas in a SQL Server replication job  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/change-schemas-in-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)



Send feedback 

#  Change schemas in a SQL Server replication job Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to change schemas in Cloud Data Fusion when you replicate data from a Microsoft SQL Server database to a BigQuery table. To ensure the replication job continues to replicate data from a SQL Server source after the schema changes, perform these steps.

**Note:** This process to change the schema is only required for SQL Server replication jobs due to the way [CDC is implemented](https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server?view=sql-server-ver15#handling-changes-to-source-table) in SQL Server.

## Change the schema

  1. Go to your instance: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the Cloud Data Fusion web interface, click **Replication**.

  3. Stop the replication job.

  4. Apply a [supported schema change](https://docs.cloud.google.com/data-fusion/docs/reference/replication-schema-changes) to the source table, such as **Add nullable column**.

  5. Create a new capture table using `sys.sp_cdc_enable_table` procedure with a unique value for parameter `@capture_instance`.

  6. Apply the same schema change on the target table in BigQuery.

  7. Restart the replication job.

  8. Optional: When the job starts streaming new changes that occur after you stop the job, you can drop the old capture table using the `sys.sp_cdc_disable_table` stored procedure. Set the parameter `@capture_instance` to the old capture instance name.




After you apply a schema change to the source table and before you create a new capture table (as you did in the previous steps), all changes are captured by the old capture with the old schema. If you added a column, any change event during that time doesn't contain data for the new column. If your application cannot handle such a transition, follow these steps:

  1. Suspend all applications generating database records.

  2. Ensure that the replication job has processed all existing events.

  3. Stop the replication job.

  4. Apply the schema change to the source table, such as **Add nullable column**.

  5. Create a new capture table using the `sys.sp_cdc_enable_table` procedure with a unique value for parameter `@capture_instance`.

  6. Resume the applications you suspended in the first step.

  7. Apply the same schema change on the target table in BigQuery.

  8. Restart the replication job.

  9. Optional: When the job starts streaming new changes that occur after you created the new capture table in the previous step, you can drop the old capture table using the `sys.sp_cdc_disable_table` stored procedure. Set the parameter `@capture_instance` to the old capture instance name.




## What's next

  * Learn more about [Replication](https://docs.cloud.google.com/data-fusion/docs/concepts/replication).
  * Refer to the supported [schema changes](https://docs.cloud.google.com/data-fusion/docs/reference/replication-schema-changes).
  * Refer to the [Replication API](https://docs.cloud.google.com/data-fusion/docs/reference/replication-ref).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
