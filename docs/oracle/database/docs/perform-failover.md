---
url: https://docs.cloud.google.com/oracle/database/docs/perform-failover/
title: Perform a failover \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:26:17.017532+00:00
---

# Perform a failover  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/perform-failover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Perform a failover Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to perform a failover operation for an Autonomous AI Database in Google Cloud.

For your Autonomous AI Database, Oracle Database@Google Cloud lets you failover to a standby peer database.

**Caution:** If your primary database is accessible, we recommend that you [perform a switchover](https://docs.cloud.google.com/oracle/database/docs/perform-switchover). Perform a failover only in the event of a disaster when your primary database becomes inaccessible, because a failover operation is irreversible, and might result in data loss and disconnection of all clients.

## Before you begin

Ensure that you have the following roles and permissions required to perform a failover:

  * `roles/autonomousDatabaseAdmin`



## Perform a failover

To failover to a standby peer database, do the following:

### Console

  * In the event of a disaster, if your primary database is inaccessible, follow these steps:

    1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database](https://console.cloud.google.com/oracle/autonomous-databases/)

    2. Click the name of the standby peer for which you want to perform the failover operation.

    3. On the **Autonomous AI Database details** page, click **Failover**.

    4. In the **Confirm failover to peer** dialog, do the following:

       1. If your primary database is not automatically detected, select the region of your primary database.
       2. Enter the ID of your primary database.
       3. Click **Confirm**.
  * If your primary database is accessible, follow these steps:

    1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database](https://console.cloud.google.com/oracle/autonomous-databases/)

    2. Click the name of the primary database for which you want to perform the failover operation.

    3. On the **Autonomous AI Database details** page, select the **Disaster recovery** tab.

    4. For the peer database to which you want to failover, click more_vert **View actions** , and then click **Failover**.

    5. In the **Confirm failover to peer** dialog, enter the ID of your primary database.

    6. Click **Confirm**.




After the failover is complete, the peer database becomes the "Primary" and its **Status** field shows "Available".

### gcloud

To perform a failover to a cross-region peer, run the `gcloud oracle-database autonomous-databases failover` command.
    
    
    gcloud oracle-database autonomous-databases failover PEER_DATABASE_ID
    --project=PROJECT_ID
    --location=PEER_REGION
    --peer-autonomous-database=projects/PROJECT_ID/locations/PRIMARY_REGION/autonomousDatabases/PRIMARY_DATABASE_ID
    

Replace the following:

  * PEER_DATABASE_ID: the ID of your peer database
  * PROJECT_ID: the ID of your Google Cloud project
  * PEER_REGION: the region where your peer database is located
  * PRIMARY_REGION: the region where your primary database is located
  * PRIMARY_DATABASE_ID: the ID of your primary database



To perform a manual failover to a local standby peer database, run the following command:
    
    
    gcloud oracle-database autonomous-databases failover DATABASE_ID
    --project=PROJECT_ID
    --location=REGION
    

Replace the following:

  * PEER_DATABASE_ID: the ID of your primary database
  * PROJECT_ID: the ID of your Google Cloud project
  * PEER_REGION: the region where your primary database is located



### API

To perform a failover operation, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/PEER_REGION/autonomousDatabases/PEER_DATABASE_ID:failover" \
    -d \
    '{
      "peer_autonomous_database": "projects/PROJECT_ID/locations/PRIMARY_REGION/autonomousDatabases/PRIMARY_DATABASE_ID"
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains your primary database
  * PEER_REGION: the region where your peer database is located
  * PEER_DATABASE_ID: the ID of your peer database
  * PRIMARY_REGION: the region where your primary database is located
  * PRIMARY_DATABASE_ID: the ID of your primary database



To perform a manual failover to a local standby peer database, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/DATABASE_ID:failover"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your primary database is located
  * DATABASE_ID: the ID of your primary database



## What's next

  * [Perform a switchover](https://docs.cloud.google.com/oracle/database/docs/perform-switchover).
  * [View peer database details](https://docs.cloud.google.com/oracle/database/docs/view-peer-databases).
  * [Create a peer database](https://docs.cloud.google.com/oracle/database/docs/create-peer-database).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
