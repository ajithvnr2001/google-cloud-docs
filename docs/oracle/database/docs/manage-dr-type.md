---
url: https://docs.cloud.google.com/oracle/database/docs/manage-dr-type/
title: Manage disaster recovery type for local peers \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:44.888636+00:00
---

# Manage disaster recovery type for local peers  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/manage-dr-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Manage disaster recovery type for local peers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage disaster recovery type for your local peer databases in Oracle Database@Google Cloud.

When you create an Autonomous AI Database, a local peer is automatically created. By default, its disaster recovery type is backup-based. You can change the disaster recovery type to [Autonomous Data Guard](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-data-guard-about.html#GUID-C483A35B-75F7-4368-BD36-B14E15FD36A7).

You can choose the disaster recovery type that meets your Recovery Time Objective (RTO) and Recovery Point Objective (RPO) requirements. The RTO is the maximum amount of time required to restore connectivity to a database after a manual or automatic failover is initiated. The RPO is the maximum duration of potential data loss on the primary database.

  * Backup-based disaster recovery: doesn't incur additional costs beyond automatic backups, but has a higher RTO than Autonomous Data Guard. We recommend that you use backup-based disaster recovery only for non-production workloads.

Backup-based disaster recovery objectives are as follows:

    * RTO: 1 hour + 1 hour per 5 TB
    * RPO: 10 seconds
  * Autonomous Data Guard: creates a standby database that is continuously updated with the changes from the primary database. We recommend that you use Autonomous Data Guard for production workloads.

Autonomous Data Guard disaster recovery objectives are as follows: 

    * RTO: 2 minutes
    * RPO: 10 seconds



## Application Continuity when using Autonomous Data Guard

Autonomous Data Guard combined with [Application Continuity](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/application-continuity1.html) can mask outages from end users and applications. Oracle applications should use Application Continuity whenever possible to minimize the impact of failover and switchover events.

You can [enable Application Continuity](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/application-continuity-configure.html) for the [predefined services](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/predefined-database-services-names.html). You can configure client connectivity with the `CONNECT_TIMEOUT`, `RETRY_DELAY`, `RETRY_COUNT`, and `TRANSPORT_CONNECT_TIMEOUT` parameters in the connection string.

An example connection string is as follows:
    
    
    localdr1 =
      (description =
        (retry_count=50)
        (connect_timeout=90)
        (retry_delay=3)
        (transport_connect_timeout=3)
        (address =
          (protocol=tcps)
          (port=1521)
          (host=localdr1.adb.uk-london-1.oraclecloud.com)
        )
        (connect_data=
          (service_name=g24da7e94756f60_localdr1_tp.adb.oraclecloud.com)
        )
        (security=
          (ssl_server_dn_match=no)
        )
      )
    

## Change disaster recovery type to Autonomous Data Guard

To change the disaster recovery type of a local peer database from backup-based to Autonomous Data Guard, enable Autonomous Data Guard and set an _automatic failover data loss limit_. 

Autonomous Data Guard monitors the status of the primary database and the local standby assumes the role of primary database in cases where the primary database becomes unavailable, according to the RTO and RPO.

Autonomous Data Guard automatically performs a failover operation according to the data loss limit. The default data loss limit is 0, which means that Autonomous Data Guard only performs an automatic failover where there is no data loss. You can also specify an automatic failover data loss limit between 0 and 3600 seconds (1 hour).

Automatic failover doesn't occur if the primary database becomes unavailable and Autonomous Data Guard determines that the possible data loss is greater than the data loss limit. In such a situation, you can still [perform a manual failover](https://docs.cloud.google.com/oracle/database/docs/perform-failover) with data loss.

To enable Autonomous Data Guard and set an automatic failover data loss limit, do the following:

### Console

  1. Go to the **Autonomous AI Database Service** page in the Google Cloud console.

[Go to Autonomous AI Database Service](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of your database.

  3. On the **Autonomous AI Database details** page, select the **Disaster recovery** tab.

  4. For the peer database on which you want to enable Autonomous Data Guard, click more_vert **View actions** , and then click **Update disaster recovery**.

  5. On the **Update disaster recovery** page, select the disaster recovery type as **Autonomous Data Guard**.

  6. Specify **Automatic failover with data loss limit in seconds**. It should be between 0-3600 seconds. The default value is 0 seconds.

  7. Click **Save**.




On the **Disaster recovery** tab, in the **Peer database** section, the **Status** field shows the progress of the update operation. After the update is complete, the peer database becomes the standby, and its **DR type** field shows "Autonomous Data Guard".

### gcloud

To enable Autonomous Data Guard and set automatic failover data loss limit, run the `gcloud oracle-database autonomous-databases update` command:
    
    
     gcloud oracle-database autonomous-databases update DATABASE_ID \
     --project=PROJECT_ID \
     --location=REGION \
     --properties-local-data-guard-enabled \
     --properties-local-adg-auto-failover-max-data-loss-limit-duration=MAX_DATA_LOSS_LIMIT
    

Replace the following:

  * DATABASE_ID: the ID of your primary database
  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your primary database is located
  * MAX_DATA_LOSS_LIMIT: automatic failover data loss limit between 0 and 3600 seconds (1 hour)



###  API 

To enable Autonomous Data Guard and set automatic failover data loss limit, run the following `curl` command:
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/DATABASE_ID"
    -d \
    '{
      "properties": {
        "localDataGuardEnabled": true,
        "localAdgAutoFailoverMaxDataLossLimitDuration": MAX_DATA_LOSS_LIMIT,
        "encryptionKey": {
             "provider": "ORACLE_MANAGED"
          }
       }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your primary database is located
  * DATABASE_ID: the ID of your primary database
  * MAX_DATA_LOSS_LIMIT: automatic failover data loss limit between 0 and 3600 seconds (1 hour)



## Change disaster recovery type to backup-based

To change the disaster recovery type of a local peer database from Autonomous Data Guard to backup-based, disable the Autonomous Data Guard.

### Console

  1. Go to the **Autonomous AI Database Service** page in the Google Cloud console.

[Go to Autonomous AI Database Service](https://console.cloud.google.com/oracle/autonomous-databases/)

  2. Click the name of your database.

  3. On the **Autonomous AI Database details** page, select the **Disaster recovery** tab.

  4. For the peer database on which you want to disable Autonomous Data Guard, click more_vert **View actions** , and then click **Remove Autonomous Data Guard**.

  5. To confirm, enter the database ID and click **Confirm**.




On the **Disaster recovery** tab, in the **Peer database** section, the **Status** field shows the progress of the update operation. After the update is complete, the peer database becomes the backup copy, and its **DR type** field shows "Backup-based".

### gcloud

To disable Autonomous Data Guard, run the `gcloud oracle-database autonomous-databases update` command:
    
    
     gcloud oracle-database autonomous-databases update DATABASE_ID \
     --project=PROJECT_ID \
     --location=REGION \
     --localDataGuardEnabled=false
    

Replace the following:

  * DATABASE_ID: the ID of your primary database
  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your primary database is located



###  API 

To disable Autonomous Data Guard, run the following `curl` command:
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/autonomousDatabases/DATABASE_ID"
    -d \
    '{
      "properties": {
        "localDataGuardEnabled": false
       }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * REGION: the region where your primary database is located
  * DATABASE_ID: the ID of your primary database



## What's next

  * [View peer database details](https://docs.cloud.google.com/oracle/database/docs/view-peer-databases).
  * Learn how to [switchover](https://docs.cloud.google.com/oracle/database/docs/perform-switchover) to a a peer database.
  * [Delete a peer database](https://docs.cloud.google.com/oracle/database/docs/delete-peer-database).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
