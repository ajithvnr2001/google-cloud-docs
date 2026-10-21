---
url: https://docs.cloud.google.com/oracle/database/docs/perform-switchover/
title: Perform a switchover \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:26:16.213312+00:00
---

# Perform a switchover  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/perform-switchover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Perform a switchover Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to perform a switchover to a peer Autonomous AI Database in Google Cloud. You can perform a switchover through both Google Cloud and OCI.

If the Primary Autonomous AI Database is down, you can perform a switchover from the peer (Standby) database.

## Before you begin

Ensure that you have the following roles and permissions required to perform a switchover:

  * `roles/autonomousDatabaseAdmin`



## Perform a Switchover

To switchover to a peer database, do the following:

### Console

  1. Go to the **Autonomous AI Database** page.

[Go to Autonomous AI Database](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of the primary Autonomous AI Database on which you want to perform a switchover operation.

  3. On the **Autonomous AI Database details** page, click the **Disaster Recovery** tab.

  4. In the **Peer database** section, for the peer database that you want to switchover to, click more_vert **View actions** , and then click **Switchover**.

  5. In the **Confirm switchover to peer** dialog, do the following:

     1. If your primary database is not automatically detected, select the region of your primary database.
     2. Enter the ID of your peer database.
     3. Click **Confirm**.



On the **Disaster recovery** tab, in the **Peer database** section, the **Status** field shows you the progress of the switchover operation. After the switchover is complete, the peer database becomes the "Primary" and its **Status** field shows "Available". Whereas, the former Primary Autonomous AI Database becomes the "Standby".

If you initiated the switchover in the OCI console, you can still see the progress of the switchover in the Google Cloud console.

### gcloud

To perform a switchover to a cross-region peer, run the `gcloud oracle-database autonomous-databases switchover` command.
    
    
    gcloud oracle-database autonomous-databases switchover DATABASE_ID
    --project=PROJECT_ID
    --location=REGION
    --peer-autonomous-database=projects/PROJECT_ID/locations/REGION/autonomousDatabases/PEER_DATABASE_ID
    

Replace the following:

  * DATABASE_ID: the ID of your database
  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your database is located
  * PEER_DATABASE_ID: the ID of your peer database



To perform a controlled switchover to a local standby peer database, run the following command:
    
    
    gcloud oracle-database autonomous-databases switchover DATABASE_ID
    --project=PROJECT_ID
    --location=REGION
    

Replace the following:

  * DATABASE_ID: the ID of your database
  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your database is located



###  API 

To perform a switchover to a cross-region peer, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/DATABASE_ID:switchover" \
    -d \
    '{
      "peerAutonomousDatabase": "projects/PROJECT_ID/locations/REGION/autonomousDatabases/PEER_DATABASE_ID"
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your database is located
  * DATABASE_ID: the ID of your database
  * PEER_DATABASE_ID: the ID of your peer database



To perform a controlled switchover to a local standby peer database, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/DATABASE_ID:switchover"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your database is located
  * DATABASE_ID: the ID of your database



## What's next

  * [View peer database details](https://docs.cloud.google.com/oracle/database/docs/view-peer-databases).
  * [Create a peer database](https://docs.cloud.google.com/oracle/database/docs/create-peer-database).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
