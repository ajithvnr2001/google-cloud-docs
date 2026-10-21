---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/configure-disaster-recovery/
title: Configure disaster recovery for a cluster \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:22:16.704893+00:00
---

# Configure disaster recovery for a cluster  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/configure-disaster-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure disaster recovery for a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to configure disaster recovery for cluster workloads in Google Distributed Cloud (GDC) air-gapped.

As a Platform Administrator (PA), you must create a bucket, backup repository, and a backup plan for a specified cluster.

Once these resources are created, you must inform an Infrastructure Operator (IO) to complete the restore.

## Before you begin

To configure disaster recovery for a cluster, you must have the following:

  * Access to the Kubernetes cluster you want to create the restore for. For more information, see [Kubernetes cluster overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters).
  * The necessary identity and access roles: 
    * DR Backup Admin: performs disaster recovery backups. Ask your Organization IAM Admin to grant you the DR Backup Admin (`dr-backup-admin`) cluster role.
    * DR System Admin: manage objects in dr-system namespace for setting up management cluster backups. Ask your Organization IAM Admin to grant you the DR System Admin (`dr-system-admin`) role.



### Create bucket on the backup site

Create a bucket on the backup site:

  1. Use the gdcloud CLI to create a bucket in the backup site:
         
         gdcloud dr buckets create --cluster=CLUSTER_NAME \
         --source-site=SOURCE_SITE
         

Replace the following:

     * `SOURCE_SITE`: the identifier of the source site as chosen by the customer. For example, `us-west`.
     * `CLUSTER_NAME`: the cluster name for the cluster such as `root-admin`.
     * `BUCKET_CONFIG_FILE`: the path of saved bucket configuration file.
  2. Store the bucket configuration locally in JSON format:
         
         gdcloud dr buckets describe --cluster=CLUSTER_NAME \
         --source-site=SOURCE_SITE \
         --output-path=BUCKET_CONFIG_FILE
         

  3. Modify the endpoint field in the configuration for the remote backup use case. Append port `:8082` to the URL: For example, `https://objectstorage.zone1.google.gdch.test` becomes `https://objectstorage.zone1.google.gdch.test:8082`.




### Create backup repository on the source site

Create a backup repository by loading the bucket config file in the source site:
    
    
        gdcloud dr backup-repositories create
        --cluster=CLUSTER_NAME
        --bucket-config-file=BUCKET_CONFIG_FILE
    

### Create backup plans for infrastructure and Management API servers

Create a `BackupPlan` resource on both the infrastructure and Management control planes using `kubectl`:
    
    
        apiVersion: backup.gdc.goog/v1
        kind: BackupPlan
        metadata:
        name: MANAGEMENT_BACKUP_PLAN_NAME
        namespace: dr-system
        spec:
        clusterName: infra-mp
        backupSchedule:
            cronSchedule: "0 0 * * *"
            paused: false
        backupConfig:
            backupScope:
            selectedNamespaces:
                namespaces:
                - NAMESPACE_MP
            backupRepository: dr-backup-repo
            includeVolumeData: true
            volumeStrategy: ProvisionerSpecific
        retentionPolicy:
            backupDeleteLockDays: 40
            backupRetainDays: 40
        ---
        apiVersion: backup.gdc.goog/v1
        kind: BackupPlan
        metadata:
        name: INFRASTRUCTURE_BACKUP_PLAN_NAME
        namespace: dr-system
        spec:
        clusterName: infra-cp
        backupSchedule:
            cronSchedule: "0 0 * * *"
            paused: false
        backupConfig:
            backupScope:
            selectedNamespaces:
                namespaces:
                - NAMESPACE_CP
            backupRepository: dr-backup-repo
            includeVolumeData: true
            volumeStrategy: ProvisionerSpecific
        retentionPolicy:
            backupDeleteLockDays: 40
            backupRetainDays: 40
    

Replace the following:

  * `MANAGEMENT_BACKUP_PLAN_NAME`: your chosen name for the backup plan. resource on the infrastructure cluster management plane.
  * `INFRASTRUCTURE_BACKUP_PLAN_NAME`: your chosen name for the backup plan resource on the infrastructure cluster control plane.
  * `NAMESPACE_MP`: the chosen namespace to backup in the Management API server.
  * `NAMESPACE_CP`: the chosen namespace to backup in the infrastructure API server.



These backup plans follow these rules:

  * Backs up the selected namespace every 24 hours. This frequency can be adjusted by modifying the `cronSchedule` field.
  * The backup includes volume data and uses a provisioner specific strategy.
  * A retention policy is set to keep backups for 40 days. You can adjust `backupRetainDays` and `backupDeleteLockDays` to meet your data retention policies.



## Perform the restoration

You must escalate and instruct an Infrastructure Operator (IO) to perform the restore on your behalf. Provide the necessary information such as the name of the `BackupRepository` and `BackupPlan` resource. For more information on audience groups in GDC, see [Documentation audiences](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
