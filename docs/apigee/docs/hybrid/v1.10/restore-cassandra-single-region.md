---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/restore-cassandra-single-region/
title: Restoring in a single region \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:09:47.164354+00:00
---

# Restoring in a single region  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/restore-cassandra-single-region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Restoring in a single region Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/restore-cassandra-single-region.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/restore-cassandra-single-region.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/restore-cassandra-single-region.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/restore-cassandra-single-region.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/restore-cassandra-single-region.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/restore-cassandra-single-region.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/restore-cassandra-single-region.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/restore-cassandra-single-region.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/restore-cassandra-single-region.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/restore-cassandra-single-region.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/restore-cassandra-single-region.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/restore-cassandra-single-region.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/restore-cassandra-single-region.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/restore-cassandra-single-region.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/restore-cassandra-single-region.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/restore-cassandra-single-region.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/restore-cassandra-single-region.html)



This page describes how to restore Cassandra in a single region.

In a single region deployment, Apigee hybrid is deployed in a single data center or a region. If you have multiple Apigee organizations in your deployment, the restore process restores data for all the organizations. In a multi-organization setup, you cannot restore a specific organization.

**Note** : Before you begin restoring a single region, consider whether the following prerequisite steps are applicable: 

  * If you want to preserve an existing setup for troubleshooting and root cause analysis (RCA), you should delete all the `org` and `env` components from the Kubernetes cluster _except_ the Apigee controller, and then retain the cluster. The cluster will contain the existing Apigee datastore (Cassandra) which you can use for troubleshooting. Create a new Kubernetes cluster and then restore Cassandra in the new cluster.
  * If your hybrid installation was set up with multiple organizations, get the overrides files for each organization before proceeding with restore in a single region. You can add the restore configuration as described in Step 3 to any **one** of the overrides files. Do not add the restore configuration to any other overrides file.



## Restoring a region from a backup

In your configuration, the Cassandra backup can reside either on Cloud Storage or on a remote server. In either case, perform the following steps to restore: 

  1. Verify the hybrid version. 
         
         apigeectl version

Ensure the version is the same version that created the backup files in storage. **Tip:** Run every `apigeectl` command with the `--dry-run=true` flag first to check for any apigeectl errors. 
  2. Confirm that the Kubernetes cluster you are restoring to does not have a prior Apigee hybrid installation. If you are restoring to the existing cluster, use the following commands to delete the existing Apigee hybrid installation: 
         
         apigeectl delete -f overrides.yaml
         kubectl -n apigee get apigeedatastore,apigeeredis,apigeetelemetry,org,env,arc # The output should be empty.
         apigeectl delete --all -f overrides.yaml

  3. Open your `overrides.yaml` file and set the `restore` properties to the desired values: 

### Cloud Storage

### Parameters
         
         namespace: YOUR_RESTORE_NAMESPACE # Use the namespace as in your original cluster.
         cassandra:
           hostNetwork: false
           ...
           restore:
             enabled: true
             serviceAccountPath: "SA_JSON_FILE_PATH"
             dbStorageBucket: "CLOUD_STORAGE_BUCKET_PATH"
             cloudProvider: "GCP"  # required verbatim "GCP" (all caps)
             snapshotTimestamp: "TIMESTAMP"
           ...
           backup:
             enabled: true
             serviceAccountPath: "SA_JSON_FILE_PATH"
             dbStorageBucket: "CLOUD_STORAGE_BUCKET_PATH"
             cloudProvider: "GCP"  # required verbatim "GCP" (all caps)
             schedule: "SCHEDULE"

### Example
         
         namespace: apigee
         cassandra:
           hostNetwork: false
           ...
           restore:
             enabled: true
             serviceAccountPath: "/Users/myhome/.ssh/my_cassandra_backup.json"
             dbStorageBucket: "gs://myname-cassandra-backup"
             cloudProvider: "GCP"
             snapshotTimestamp: "20201001183903"
         
           ...
           backup:
             enabled: true
             serviceAccountPath: "/Users/myhome/.ssh/my_cassandra_backup.json"
             dbStorageBucket: "gs://myname-cassandra-backup"
             cloudProvider: "GCP"
             schedule: "0 2 * * *"
           ...

Where: 

Property | Description  
---|---  
`namespace` | YOUR_RESTORE_NAMESPACE Namespace for restore. Use the namespace as in your original cluster.  
`cassandra:hostNetwork` |  `hostNetwork` is required and should always be set to `false`.   
`restore:enabled` | Restore is disabled by default. You must set this property to `true`.  
`restore:serviceAccountPath` |  SA_JSON_FILE_PATH The path on your filesystem to the service account you created for the backup.  
`restore:dbStorageBucket` |  CLOUD_STORAGE_BUCKET_PATH The Cloud Storage bucket path where your backup data is stored in the following format: `gs://BUCKET_NAME`. The `gs://` is required.  
`restore:cloudProvider` | **`GCP`** The `cloudProvider: "GCP"` property is required.  
`restore:snapshotTimestamp` |  TIMESTAMP The timestamp of the backup snapshot to restore. To check what timestamps can be used, go to the `dbStorageBucket` and look at the files that are present in the bucket. Each file name contains a timestamp value. For example, `backup_20210203213003_apigee-cassandra-default-0.tgz` Where 20210203213003 is the `snapshotTimestamp` value you would use if you wanted to restore the backups created at that point in time.   
`backup:enabled` | Backup is disabled by default. You must set this property to `true`.  
`backup:serviceAccountPath` |  SA_JSON_FILE_PATH The path on your filesystem to the service account JSON file that was downloaded when you ran `./tools/create-service-account`  
`backup:dbStorageBucket` |  CLOUD_STORAGE_BUCKET_PATH The Cloud Storage bucket path in this format: `gs://BUCKET_NAME`. The `gs://` is required.  
`backup:cloudProvider` | **`GCP`** The `cloudProvider: "GCP"` property is required.  
`backup:schedule` | SCHEDULE The time when the backup starts, specified in [standard crontab syntax](https://en.wikipedia.org/wiki/Cron). Default: `0 2 * * *` **Note:** Avoid scheduling a backup that starts a short time after you apply the backup configuration to your cluster. When you apply the backup configuration, Kubernetes recreates the Cassandra nodes. If the backup starts before the nodes restart (possibly several minutes) the backup will fail.   
  
### Non-Cloud Storage

### Parameters
         
         namespace: YOUR_RESTORE_NAMESPACE # Use the namespace as in your original cluster.
           cassandra:
             hostNetwork: false
             ...
             restore:
               enabled: true
               keyFile: "PATH_TO_PRIVATE_KEY_FILE"
               server: "BACKUP_SERVER_IP"
               storageDirectory: "/home/apigee/BACKUP_DIRECTORY"
               cloudProvider: "HYBRID"  # required verbatim "HYBRID" (all caps)
               snapshotTimestamp: "TIMESTAMP"
             ...
             backup:
               enabled: true
               keyFile: "PATH_TO_PRIVATE_KEY_FILE"
               server: "BACKUP_SERVER_IP"
               storageDirectory: "/home/apigee/BACKUP_DIRECTORY"
               cloudProvider: "HYBRID" # required verbatim "HYBRID" (all caps)
               schedule: "SCHEDULE"
           

### Example
         
         namespace: apigee
           cassandra:
             hostNetwork: false
             ...
             **restore:
               enabled: true
               keyFile: "/Users/exampleuser/apigee-hybrid/hybrid-files/service-accounts/private.key"
               server: "34.56.78.90"
               storageDirectory: "/home/apigee/cassbackup"
               cloudProvider: "HYBRID"
               snapshotTimestamp: "20201001183903"**
             ...
             backup:
               enabled: true
               keyFile: "/Users/exampleuser/apigee-hybrid/hybrid-files/service-accounts/private.key"
               server: "34.56.78.90"
               storageDirectory: "/home/apigee/cassbackup"
               cloudProvider: "HYBRID"
               schedule: "0 2 * * *"
             ...

Where: 

Property | Description  
---|---  
`namespace` | YOUR_RESTORE_NAMESPACE Namespace for restore. Use the namespace as in your original cluster.  
`cassandra:hostNetwork` |  `hostNetwork` is required and should always be set to `false`.   
`restore:enabled` | Restore is disabled by default. You must set this property to `true`.  
`restore:keyFile` | PATH_TO_PRIVATE_KEY_FILE The path on your local file system to the SSH private key file (named `ssh_key` in the step where you created the SSH key pair).  
`restore:server` | BACKUP_SERVER_IP The IP address of your backup server.  
`restore:storageDirectory` | BACKUP_DIRECTORY The name of the backup directory on your backup server. This must be a directory within `home/apigee` (the backup directory is named `cassandra_backup` in the step where you created the backup directory).  
`restore:cloudProvider` | **`HYBRID`** The `cloudProvider: "HYBRID"` property is required.  
`restore:snapshotTimestamp` |  TIMESTAMP The timestamp of the backup snapshot to restore. To check what timestamps can be used, go to the `dbStorageBucket` and look at the files that are present in the bucket. Each file name contains a timestamp value. For example, `backup_20210203213003_apigee-cassandra-default-0.tgz` Where 20210203213003 is the `snapshotTimestamp` value you would use if you wanted to restore the backups created at that point in time.   
`backup:enabled` | Backup is disabled by default. You must set this property to `true`.  
`backup:keyFile` | PATH_TO_PRIVATE_KEY_FILE The path on your local file system to the SSH private key file (named `ssh_key` in the step where you created the SSH key pair).  
`backup:server` | BACKUP_SERVER_IP The IP address of your backup server.  
`backup:storageDirectory` | BACKUP_DIRECTORY The name of the backup directory on your backup server. This must be a directory within `home/apigee` (the backup directory is named `cassandra_backup` in the step where you created the backup directory).  
`backup:cloudProvider` | **`HYBRID`** The `cloudProvider: "HYBRID"` property is required.  
`backup:schedule` | SCHEDULE The time when the backup starts, specified in [standard crontab syntax](https://en.wikipedia.org/wiki/Cron). Default: `0 2 * * *` **Note:** Avoid scheduling a backup that starts a short time after you apply the backup configuration to your cluster. When you apply the backup configuration, Kubernetes recreates the Cassandra nodes. If the backup starts before the nodes restart (possibly several minutes) the backup will fail.   
  
**Note:** Apigee restores Cassandra from a Cloud Storage backup or a remote server backup based on the `backup` configuration in the `overrides.yaml` file.
  4. Create a new hybrid runtime deployment. This will create a new Cassandra cluster and begin restoring the backup data into the cluster: 
         
         ${APIGEECTL_HOME}/apigeectl init  -f overrides/overrides.yaml
         
         ${APIGEECTL_HOME}/apigeectl check-ready -f overrides/overrides.yaml
         
         ${APIGEECTL_HOME}/apigeectl apply -f overrides/overrides.yaml --restore
         
         ${APIGEECTL_HOME}/apigeectl check-ready -f overrides/overrides.yaml

  5. Verify the restoration job progress and confirm that `apigeeds` and all the other pods are up: 
     * To check `apigeeds`: 
           
           kubectl get apigeeds -n apigee

     * To check all other pods: 
           
           kubectl get pods -n apigee




Upon successful completion of the restore and confirmation that the runtime components are healthy, we recommend configuring a backup on the cluster: 

  1. Remove the `restore` configuration from the `overrides-restore.yaml` file.
  2. Add the `backup` configuration to the `overrides-restore.yaml` file.
  3. Apply the `backup` configuration with the following command: 
         
         ./apigeectl apply -f ../overrides-restore.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
