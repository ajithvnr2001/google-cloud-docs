---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/schedule-cassandra-backup-gcs/
title: Scheduling backups in Cloud Storage \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:23:08.648385+00:00
---

# Scheduling backups in Cloud Storage  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/schedule-cassandra-backup-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Scheduling backups in Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/schedule-cassandra-backup-gcs.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/schedule-cassandra-backup-gcs.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/schedule-cassandra-backup-gcs.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/schedule-cassandra-backup-gcs.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/schedule-cassandra-backup-gcs.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/schedule-cassandra-backup-gcs.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/schedule-cassandra-backup-gcs.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/schedule-cassandra-backup-gcs.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/schedule-cassandra-backup-gcs.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/schedule-cassandra-backup-gcs.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/schedule-cassandra-backup-gcs.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/schedule-cassandra-backup-gcs.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/schedule-cassandra-backup-gcs.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/schedule-cassandra-backup-gcs.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/schedule-cassandra-backup-gcs.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/schedule-cassandra-backup-gcs.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/schedule-cassandra-backup-gcs.html)



This page describes how to schedule backups for Cassandra in Cloud Storage. In this method, backups are stored in the specified Cloud Storage bucket.

**Note:** After applying the backup configuration on the existing cluster, the Cassandra pods will restart one after another (rolling restart) from last to first. 

To schedule Cassandra backups, perform the following steps: 

  1. Run the following `create-service-account` command to create a Google Cloud service account (SA) with the standard [ `roles/storage.objectAdmin`](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) role. This SA role allows you to write backup data to Cloud Storage. Execute the following command in the `hybrid-base-directory/hybrid-files` directory: 
         
         ./tools/create-service-account --env non-prod --dir ./service-accounts

This command creates a single service account named `apigee-non-prod` for use in non-production environments and places the downloaded key file in the `./service-accounts` directory. **Note:** If you prefer to create all the individual service accounts for a production environment, use the following command: 
         
         ./tools/create-service-account **--env prod** --dir ./service-accounts

For more information about Google Cloud service accounts, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts). 
  2. The `create-service-account` command saves a JSON file containing the service account private key. The file is saved in the same directory where the command executes. You will need the path to this file in the following steps.
  3. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets). Specify a reasonable data [ retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy) for the bucket. Apigee recommends a data retention policy of 15 days.
  4. Open your `overrides.yaml` file.
  5. Add the following `cassandra.backup` properties to enable backup. Do not remove any of the properties that are already configured. 

### Parameters
         
         cassandra:
             ...
         
             backup:
               enabled: true
               serviceAccountPath: SA_JSON_FILE_PATH
               dbStorageBucket: CLOUD_STORAGE_BUCKET_PATH
               schedule: BACKUP_SCHEDULE_CODE
               cloudProvider: "GCP"  # For remote server backup set this to HYBRID (all caps)
         
             ...
             

### Example
         
         ...
         
           cassandra:
             storage:
               type: gcepd
               capacity: 50Gi
               gcepd:
                 replicationType: regional-pd
             auth:
               default:
                 password: "abc123"
               admin:
                 password: "abc234"
               ddl:
                 password: "abc345"
               dml:
                 password: "abc456"
             nodeSelector:
               key: cloud.google.com/gke-nodepool
               value: apigee-data
             **backup :
               enabled: true
               serviceAccountPath: "/Users/myhome/.ssh/my-cassandra-backup-sa.json"
               dbStorageBucket: "gs://myname-cassandra-backup"
               schedule: "45 23 * * 6"
               cloudProvider: "GCP"
               **
         
         
             ... 

Where: Property | Description  
---|---  
`backup:enabled` | Backup is disabled by default. You must set this property to `true`.  
`backup:serviceAccountPath` | SA_JSON_FILE_PATH The path on your filesystem to the service account JSON file that was downloaded when you ran the `./tools/create-service-account` command. You can also provide a relative file path. The path will be relative to the `hybrid-base-directory/hybrid-files` directory.  
`backup:dbStorageBucket` | CLOUD_STORAGE_BUCKET_PATH The Cloud Storage bucket path in this format: `gs://BUCKET_NAME`. The `gs://` is required.  
`backup:cloudProvider` | **`GCP/HYBRID`** For a Cloud Storage backup, set the property to `GCP`. For example, `cloudProvider: "GCP"`. For a remote server backup, set the property to `HYBRID`. For example, `cloudProvider: "HYBRID"`.  
`backup:schedule` | BACKUP_SCHEDULE_CODE The time when the backup starts, specified in [standard crontab syntax](https://en.wikipedia.org/wiki/Cron). Default: `0 2 * * *` **Note:** Avoid scheduling a backup that starts a short time after you apply the backup configuration to your cluster. When you apply the backup configuration, Kubernetes recreates the Cassandra nodes. If the backup starts before the nodes restart, the first backup will fail and the subsequent backups will pass.   
  6. Apply the configuration changes to the new cluster. For example: 
         
         $APIGEECTL_HOME/apigeectl apply --datastore -f YOUR_OVERRIDES_FILE

Where YOUR_OVERRIDES_FILE is the path to the overrides file you just edited. 

  7. Verify the backup job. For example: 
         
         kubectl get cronjob -n apigee
         
         NAME                      SCHEDULE     SUSPEND   ACTIVE   LAST SCHEDULE   AGE
           apigee-cassandra-backup   33 * * * *   False     0        <none>          94s




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
