---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/restore-cassandra-single-region/
title: Restoring in a single region \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:31.780086+00:00
---

# Restoring in a single region  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/restore-cassandra-single-region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Restoring in a single region Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

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

  1. Update the Cassandra restore details in the `overrides.yaml` file:
         
         namespace: YOUR_RESTORE_NAMESPACE # Use the same namespace as in your original cluster.
         cassandra:
           hostNetwork: false
           ...
           restore:
             enabled: true
             serviceAccountPath: "SA_JSON_FILE_PATH"
             dbStorageBucket: "CLOUD_STORAGE_BUCKET_NAME"
             cloudProvider: "GCP"  # required verbatim "GCP" (all caps)
             snapshotTimestamp: "TIMESTAMP"
           ...
           backup:
             enabled: false
           ...

Where: 

Property | Description  
---|---  
`namespace` | YOUR_RESTORE_NAMESPACE Namespace for restore. Use the same namespace as in your original cluster.  
`cassandra:hostNetwork` |  `hostNetwork` is required and should always be set to `false`.   
`restore:enabled` | Restore is disabled by default. You must set this property to `true`.  
`restore:serviceAccountPath` |  SA_JSON_FILE_PATH The path on your filesystem to the service account you created for the backup.  
`restore:dbStorageBucket` |  CLOUD_STORAGE_BUCKET_NAME The name of a Google Cloud Storage bucket that stores backup archives to be used for data restoration. **Note:** Starting in Hybrid version 1.13, the bucket name doesn't need to be prefixed with `gs://`. Support for this prefix has been deprecated and will be removed in future releases.   
`restore:cloudProvider` | **`GCP`** The `cloudProvider: "GCP"` property is required.  
`restore:snapshotTimestamp` |  TIMESTAMP The timestamp of the backup snapshot to restore. To check what timestamps can be used, go to the `dbStorageBucket` and look at the files that are present in the bucket. Each file name contains a timestamp value. For example, `backup_20210203213003_apigee-cassandra-default-0.tgz` Where 20210203213003 is the `snapshotTimestamp` value you would use if you wanted to restore the backups created at that point in time.   
`backup:enabled` | You should set this property to `false` in case it had been previously set to `true`. **Note:** Backup must not be enabled when restoring.  
**Note:** In case you are using **CSI backup** , please follow the **example restore config** in the [CSI backup and restore](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-csi-backup-restore#example-restore-config) documentation.
  2. In case you do not have a clean cluster to start out with, follow the [Decommission a hybrid region for helm](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/decommission-region#helm) documentation to bring your existing Hybrid installation into a clean state (you can leave the **Cert Manager** installed). This would bring you to an equal state as if you would have followed the [Apigee hybrid runtime setup manual](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-cluster) until the beginning of Step 12.

  3. Verify there are no pods remaining in the Apigee namespace:
         
         kubectl get pods -n APIGEE_NAMESPACE

  4. If you are using CSI backup, make sure that you can see the volumesnapshots you want to use for the restoration process by running:
         
         kubectl get volumesnapshot -n APIGEE_NAMESPACE
                   

  5. Install all Hybrid components one by one as described in [Step 11: Install Apigee hybrid using Helm ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-helm-charts). Note that the `apigee-cassandra-restore` pod will get created once you run the command to install the `datastore`, but it will only go into `running` state after you install the `apigee-org` component. 




See [Cassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-backup-overview) for more details on Cassandra backup and restore.

Verify the restoration job progress and confirm that `apigeeds` and all the other pods are up:

  1. Check `apigeeds`: 
         
         kubectl get apigeeds -n APIGEE_NAMESPACE

  2. Check all other pods: 
         
         kubectl get pods -n APIGEE_NAMESPACE




Upon successful completion of the restore and confirmation that the runtime components are healthy, we recommend configuring a backup on the cluster: 

  1. Remove the `restore` configuration from the `overrides-restore.yaml` file.
  2. Add the `backup` configuration to the `overrides-restore.yaml` file.
  3. Apply the `backup` configuration with the following command: 
         
         helm upgrade datastore apigee-datastore/ \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides-restore.yaml
         


**Warning:** See [known issue 391861216](https://docs.cloud.google.com/apigee/docs/release/known-issues#391861216) affecting Apigee Hybrid and Cassandra after restore using a remote server or Cloud Storage. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
