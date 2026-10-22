---
url: https://docs.cloud.google.com/oracle/database/docs/view-peer-databases/
title: View peer databases \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:39.888295+00:00
---

# View peer databases  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/view-peer-databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  View peer databases Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view the details of your peer databases in Google Cloud.

## Before you begin

Ensure that you have the following roles and permissions required to view the details of your peer databases:

  * `roles/autonomousDatabaseViewer`



## View peer database details

To view the details of your peer databases, do the following:

### Console

  1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of the Autonomous AI Database for which you want to view the peer databases details.

  3. On the **Autonomous AI Database details** page, click the **Disaster Recovery** tab.

In the **Peer database** section, you can view the details of your peer database.




### gcloud

Use the `gcloud oracle-database autonomous-databases describe` command to view peer database information.
    
    
    gcloud oracle-database autonomous-databases describe DATABASE_ID
    --location=REGION_ID
    

Replace the following:

  * DATABASE_ID: the identifier for the peer database.
  * REGION_ID: the region of the peer database.



## What's next

  * Learn how to [switchover](https://docs.cloud.google.com/oracle/database/docs/perform-switchover) to a a peer database.
  * [Delete a peer database](https://docs.cloud.google.com/oracle/database/docs/delete-peer-database).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
