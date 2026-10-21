---
url: https://docs.cloud.google.com/oracle/database/docs/delete-peer-database/
title: Delete a peer database \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:26:16.259759+00:00
---

# Delete a peer database  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/delete-peer-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Delete a peer database Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete a peer database in Google Cloud.

You can't delete a peer database during a switchover operation.

## Before you begin

Ensure that you have the following roles and permissions required to delete a peer database:

  * `roles/autonomousDatabaseAdmin`



## Delete a peer database

To delete a peer database, do the following:

### Console

  1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of the Autonomous AI Database for which you want to delete a peer database.

  3. On the **Autonomous AI Database details** page, click the **Disaster Recovery** tab.

  4. In the **Peer database** section, for the peer database that you want to delete, click more_vert **View actions** , and then click **Delete**.

  5. In the **Delete database instance** dialog, enter the peer database ID and click **Confirm**.

The deletion of the peer database might take a few hours. On the **Disaster recovery** tab, in the **Peer database** section, the **Status** field shows you the progress of the delete operation. When the peer database is deleted, it's removed from the peer database list.




### gcloud

You can use the `gcloud oracle-database autonomous-databases delete` command to delete a peer database.
    
    
    gcloud oracle-database autonomous-databases delete DATABASE_ID
    --location=REGION_ID
    

Replace the following:

  * DATABASE_ID: the identifier for the peer database.
  * REGION_ID: the region of the peer database.



## What's next

  * Learn how to [switchover](https://docs.cloud.google.com/oracle/database/docs/perform-switchover) to a a peer database.
  * [View peer database details](https://docs.cloud.google.com/oracle/database/docs/view-peer-databases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
