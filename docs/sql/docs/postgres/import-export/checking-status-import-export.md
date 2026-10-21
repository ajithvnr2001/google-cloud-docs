---
url: https://docs.cloud.google.com/sql/docs/postgres/import-export/checking-status-import-export/
title: Check the status of import and export operations \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:39.604583+00:00
---

# Check the status of import and export operations  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/import-export/checking-status-import-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Check the status of import and export operations Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/import-export/checking-status-import-export "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/checking-status-import-export "View this page for the SQL Server database engine")

This page describes how to check the status of your Cloud SQL import and export operations.

Each status message includes:

  * A timestamp.
  * A status (pending, running, or done).
  * A message containing the details of the operation.



## Check the status

You can use the Google Cloud console or `gcloud` to check the status of an import or export.

You can also check the status of a cancelled import or export operation. For more information, see [Check the cancelled status](https://docs.cloud.google.com/sql/docs/postgres/import-export/cancel-import-export#check-canceled-status).

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Operations** from the SQL navigation menu. 

The most recent operations are at the top of the list. Look for "Import" or "Export" in the **Type** field.




Note: If your export fails, you can get information about the failure in the instance operations log. [Learn more.](https://docs.cloud.google.com/sql/docs/postgres/logging#logs)

### gcloud

To view the status of an import or export operation: 
    
    
    gcloud sql operations list \
    --instance INSTANCE_NAME \
    --limit 10

Import and export operations have `IMPORT` or `EXPORT` in the `TYPE` field. The status of these operations is in the `STATUS` field.

You can also list details of a specific operation or wait for a specific operation to complete. For more information on this command, see the [ `gcloud sql operations`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations) command reference page. 

Note: If your export fails, you can get information about the failure in the instance operations log. [Learn more.](https://docs.cloud.google.com/sql/docs/postgres/instance-info#logs)

If you exported into a Cloud Storage bucket, you can also check the log file created by Cloud SQL in the bucket for information about export status.

## What's next

  * Learn more about [importing and exporting data](https://docs.cloud.google.com/sql/docs/postgres/import-export).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
