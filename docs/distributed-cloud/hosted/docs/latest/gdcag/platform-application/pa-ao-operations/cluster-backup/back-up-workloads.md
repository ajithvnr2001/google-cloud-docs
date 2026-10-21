---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/back-up-workloads/
title: Back up your workloads \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:40:18.339830+00:00
---

# Back up your workloads  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/back-up-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Back up your workloads Stay organized with collections  Save and categorize content based on your preferences. 

Manual backups in Google Distributed Cloud (GDC) air-gapped let you protect container workloads and persistent volumes on your Kubernetes clusters before application upgrades. From an existing plan, you can create on-demand copies, inspect their status, and delete obsolete entries.

## Before you begin

Application Operator (AO) users can only perform manual backups from an existing backup plan.

### Request IAM roles

To create, view, and delete backups, ask your Organization IAM Admin or Project IAM Admin to grant you one of the following roles:

  * **User Cluster Backup Admin** (`user-cluster-backup-admin`): creates, gets, lists, watches, updates, patches, and deletes backup resources such as backup and restore plans in user clusters. Contact your Organization IAM Admin to request this role.

  * **Backup Creator** (`backup-creator`): creates, gets, lists, watches, updates, patches, and deletes manual backup requests and manual restore requests. Contact your Project IAM Admin to request this role.




## Create a manual backup

If your backup plan defines a schedule for the backup, the backups are automatically created according to that schedule. You can also manually create a backup outside the scope of your backup plan schedule. For example, you might want to back up your workloads before you upgrade your applications. A backup does not include cluster configuration information, such as node configurations, node pools, initial cluster size, or what features are enabled.

Two forms of data are captured in a backup:

  * **Config backup** : A set of Kubernetes resource descriptions extracted from the API server of the cluster undergoing backup.
  * **Volume backup** : A backup of `PersistentVolumeClaims`.



### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click the **Backup Plans** tab.
  4. Click the plan that you want to use for the backup.
  5. Click **Start a backup**.
  6. Enter a backup name and an optional description.
  7. Set the number of days to retain the backup. Once this number of days is reached, the backup is automatically deleted.
  8. Set the number of days during which backups cannot be deleted.
  9. Click **Start**.



### API

The manual backup must reference an existing backup plan for the backup configuration and the backup must be created by issuing a `ManualClusterBackupRequest`.

Here's an example of a `ManualClusterBackupRequest`:
    
    
    apiVersion: backup.gdc.goog/v1
    kind: ManualClusterBackupRequest
    metadata:
      name: manualbackuprequest-test
      namespace: PROJECT_NAME
    spec:
      clusterBackupName: "backup-test"
      clusterBackupPlanRef: "backupplan-test"
      deleteLockDays: 5
      retainDays: 6
    

Replace `PROJECT_NAME` with the name of your GDC project.

This example includes the following values:

Value | Description  
---|---  
`clusterBackupName` | The name of the backup to create.  
`clusterBackupPlanRef` | The name of the `ClusterBackupPlan` to use for the configuration of the backup. The backup plan must exist in the same namespace as the `ManualClusterBackupRequest`.  
  
`deleteLockDays` | Blocks any deletion of the backup for the number of days specified after backup creation. This overrides the `retentionPolicy` in the `ClusterBackupPlan`.   
`retainDays` | Deletes backups once the specified number of days is reached following backup creation. This value overrides the `retentionPolicy` in the `ClusterBackupPlan`. Retention policies don't override the retention policies of the storage location, nor can they exceed 90 days.   
  
## View a backup

Users with the User Cluster Backup Admin (`user-cluster-backup-admin`) role can see all backups in the organization. Users with the Backup Creator (`backup-creator`) role can see all of the backups in a project.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click **Select project** to select an organization or project depending on your role: 
     * User Cluster Backup Admin: Select an organization to see all backups in an organization or select a project to see all backups in a project.
     * Backup Creator: Select a project to see all backups in a project.
  4. Click the **Backups** tab.
  5. Click a backup in the list to view its details.



### kubectl

View a list of your backups:
    
    
    kubectl get clusterBackups
    

An example of the output:
    
    
    NAME            STATE
    backup-test   Succeeded
    

## Delete a backup

Backups can't be deleted by a regular interaction with the Kubernetes API server. To delete a backup, use the GDC console or issue a `DeleteClusterBackupRequest`.

### Console

Delete the backup from the **Backups** tab:

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click **Select project** to select an organization or project depending on your role: 
     * User Cluster Backup Admin: Select an organization to see all backups in an organization, or select a project to see all backups in a project.
     * Backup Creator: Select a project to see all backups in a project.
  4. Click the **Backups** tab.
  5. Click the three-dot menu icon for the backup you want to delete.
  6. Type the name of the backup into the text field.
  7. Click the **Delete Backup** button to complete the deletion of this backup.

**Note:** This operation can't be undone.



Alternatively, delete the backup by clicking on the backup name when viewing a backup plan:

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click **Select project** , and select an organization or project depending on your role: 
     * User Cluster Backup Admin: Select an organization to see all of the backup plans in an organization, or select a project to see all of the backup plans in a project.
     * Backup Creator: Select a project to see all of the backup plans in a project.
  4. Click the **Backup Plans** tab.
  5. Click the name of the backup plan containing the backup you want to delete.
  6. Click the **Backups** tab.
  7. Click the name of the backup you want to delete.
  8. Click the **Delete Backup** button.
  9. Enter the name of the backup into the text field.
  10. Click the **Delete** button to complete the deletion of this backup.

**Note:** This operation can't be undone.



### kubectl

Send a `DeleteClusterBackupRequest` request:
    
    
    apiVersion: backup.gdc.goog/v1
    kind: DeleteClusterBackupRequest
    metadata:
      name: deletebackuprequest-test
      namespace: PROJECT_NAME
    spec:
      clusterBackupRef: "backup-test"
    

Replace `PROJECT_NAME` with the name of your GDC project.

This example includes the following values:

  * `backupName`: the name of the backup being deleted. This backup must exist in the same namespace as the `DeleteClusterBackupRequest`.
  * `DeleteClusterBackupRequest`: the resource that deletes the backup custom resource from the cluster and removes all artifacts associated with that backup from the storage location of the backup, including volume data.

**Note:** Attempting to delete a `ClusterBackup` resource without applying a `DeleteClusterBackupRequest` resource doesn't clean object storage artifacts and might result in undefined behavior.

## What's next

  * [Plan a set of restores](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-restores)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
