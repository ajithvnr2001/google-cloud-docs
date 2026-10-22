---
url: https://docs.cloud.google.com/oracle/database/docs/start-stop-databases/
title: Start, stop, and restart a database \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:42.444423+00:00
---

# Start, stop, and restart a database  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/start-stop-databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Start, stop, and restart a database Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to start, stop, and restart an Autonomous AI Database.

## Before you begin

Ensure that you have the following Identity and Access Management (IAM) role required to perform the start, stop, and restart operations:

  * `roles/autonomousDatabaseAdmin`



To learn how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).

## Start an Autonomous AI Database

Starting an Autonomous AI Database lets you open connections and run operations on it. An Autonomous AI Database continues to run until you stop it manually.

**Note:** When you create an Autonomous AI Database, it is automatically started. You don't need to start it manually.

To start an Autonomous AI Database, follow these steps:

### Console

  1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of the Autonomous AI Database that you want to start.

  3. On the **Autonomous AI Database details** page, click **Start**.

  4. In the **Start database instance** dialog, click **Start**.

In the **Details** section, the **Status** field shows you the progress of the start operation. The Autonomous AI Database is ready to use when the **Status** field shows "Available".




## Stop an Autonomous AI Database

Stopping an Autonomous AI Database shuts down the instance, closes all the open files and the active connections, and stops the running operations. It also stops the billing for the database.

To stop an Autonomous AI Database, follow these steps:

### Console

  1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of the Autonomous AI Database that you want to stop.

  3. On the **Autonomous AI Database details** page, click **Stop**.

  4. In the **Stop database instance** dialog, click **Stop**.

In the **Details** section, the **Status** field shows you the progress of the stop operation. When the Autonomous AI Database is stopped, the **Status** field shows "Stopped".




## Restart an Autonomous AI Database

To restart an Autonomous AI Database, follow these steps:

### Console

  1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of the Autonomous AI Database that you want to restart.

  3. On the **Autonomous AI Database details** page, click **Restart**.

  4. In the **Restart database instance** dialog, click **Restart**.

In the **Details** section, the **Status** field shows you the progress of the restart operation. When the restart operation is complete, the **Status** field shows "Available".




## What's next

  * Learn how to [manage](https://docs.cloud.google.com/oracle/database/docs/manage-databases) or [delete](https://docs.cloud.google.com/oracle/database/docs/delete-databases) an Autonomous AI Database.
  * Configure [Identity and Access Management roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles) for an instance.
  * [Use monitoring metrics](https://docs.cloud.google.com/oracle/database/docs/monitoring-metrics) to monitor your instances.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
