---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-backups/
title: Plan a set of backups \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:24.456212+00:00
---

# Plan a set of backups  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Plan a set of backups Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create and manage backup plans for cluster workloads in Google Distributed Cloud (GDC) air-gapped.

_Backup plans_ provide the configuration, location, and management functions for a sequence of backups. A backup plan contains a backup configuration, including the source cluster and the selection of workloads to back up. Google recommends providing every cluster with at least one backup plan.

You can create one or more backup plans for each cluster. You might want to partition the backups of your cluster for one of the following reasons:

  * Instead of having one very large backup taken at a single time of the day, you want multiple smaller backups distributed throughout the day.
  * You want to back up some portions of your cluster more often than others, such as daily backups for some namespaces and hourly backups for others.



A single cluster or virtual machine (VM) can belong to one or more backup plans. A backup plan can't span more than one cluster; however, a single backup plan can capture multiple VMs if they exist in the same cluster. All backup and restore resources must be associated with a project name.

This document is for developers in platform administrator or application operator groups that manage cluster backup operations. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

When you back up a user cluster, ensure that the project you used to create the backup plan is attached to that cluster.

### Request IAM roles

To create a backup plan, ask your IAM Org Admin to grant you the **User Cluster Backup Admin** (`user-cluster-backup-admin`) role. This role creates, gets, lists, watches, updates, patches, and deletes backup resources such as backup plans and restore plans in user clusters.

If you are an Application Operator, ask an administrator with User Cluster Backup Admin privileges to create a backup plan for you.

## Create a backup plan

You must define a cron schedule for the backup plan, so that backups automatically generate according to the cron schedule. You can also manually back up your workloads. For more information, see [Create a manual backup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/back-up-workloads#create-manual-backup).

Create backup plans using the GDC console or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click **Create Backup Plan**.
  4. In the **Plan details** section, complete the following steps and click **Continue** : 
     1. In the **Cluster** list, select the cluster to back up.
     2. In the **Project** list, select the project.
     3. In the **Backup plan name** field, enter your chosen backup plan name.
     4. (Optional) In **Backup plan description** enter a description for the backup plan.
     5. In the **Backup repo** field, select a backup repository. Backup repositories are a set of object storage implementations.
     6. Click **Next**.
  5. In the **Scope and encryption** section, complete the following steps and click **Continue** :

     1. Select one of the following scopes for the backup plan:

        1. Click **Entire cluster** to back up all namespace resources in the backup.
        2. Click **Selected namespaces within the cluster** to choose the namespaces in the cluster to back up. 
           1. Click **Edit Cluster Namespace** and then **Add Cluster Namespace** to enter a **Namespace**.
        3. Click **Selected protected applications within this cluster** to add resources by specifying the namespace and the application name. 
           1. Click **Edit Protected Applications** and then **Add Protected Application** to enter a **Namespace** and **Protected Application**.
     2. Click **Include Secrets** to include Kubernetes `Secret` resources.

     3. Click **Include persistent volume data** if you want the volume data in your backup. Clear this checkbox if you want to create empty volumes during the backup.

  6. In the **Schedule and retention** section, complete the following steps and click **Continue** :

     1. To define a schedule, enter an expression using standard cron syntax in the **CRON string** field. For example, the expression `10 3 * * *` creates a backup at 0310 every day. All times are interpreted as UTC. The minimum interval between scheduled backups is 10 minutes.
     2. In the **Delete backups after** field, set the number of days for which to retain the backup. Once the number of days is reached, the backup is automatically deleted.
     3. Set the number of days during which backups cannot be deleted.
     4. To lock the retention policy, click the lock icon to turn the lock from **Off** to **On**.
  7. Review the backup plan details and click **Create Plan**.




### API

Create a `ClusterBackupPlan` custom resource in the cluster to schedule backups. A backup plan periodically schedules backups based on the `backupSchedule`. `ClusterBackupPlan` resources are namespace resources. Here's an example of a `ClusterBackupPlan`:
    
    
    apiVersion: backup.gdc.goog/v1
    kind: ClusterBackupPlan
    metadata:
      name: CLUSTER_BACKUP_PLAN
      namespace: PROJECT_NAME
    spec:
      targetCluster:
        targetClusterType: UserCluster
        targetClusterName:
          kind: "Cluster"
          name: CLUSTER_NAME
      backupSchedule:
        cronSchedule: CRON_SCHEDULE
        paused: BACKUP_SCHEDULE_STATUS
        maxConcurrency: MAX_CONCURRENCY
      clusterBackupConfig:
        backupScope:
          selectedNamespaces:
            namespaces: [NAME_SPACE]
        clusterBackupRepositoryName: CLUSTER_BACKUP_REPOSITORY
      retentionPolicy:
        backupDeleteLockDays: BACKUP_DELETE_LOCK_DAYS
        backupRetainDays: BACKUP_RETAIN_DAYS
      description: BACKUP_PLAN_DESCRIPTION
    

Replace the following:

  * `CLUSTER_BACKUP_PLAN`: your cluster backup plan name.
  * `PROJECT_NAME`: the name of your GDC project.
  * `CLUSTER_NAME`: the name of the cluster to back up. The enclosing `targetCluster` field has the following components: 
    * `targetClusterType`: The type of cluster to back up, such as `UserCluster` or `ManagementAPI`. This example uses `UserCluster`.
    * `targetClusterName`: Contains `name`, which is set by `CLUSTER_NAME`.
  * `CRON_SCHEDULE`: a crontab schedule indicating when to schedule backups, such as `"*/30 * * * *"`. The minimum interval between scheduled backups is 10 minutes.
  * `BACKUP_SCHEDULE_STATUS`: if `true`, periodic backups are not scheduled.
  * `MAX_CONCURRENCY`: specifies the maximum number of active scheduled backups that can exist under a backup plan at the same time. If specified, no more than this number of scheduled backups from this backup plan can be in the active state at any given time. If not specified, it defaults to 2. The value must be between 1 and 7.
  * `NAME_SPACE`: a list of namespaces to include in the backup. The enclosing `clusterBackupConfig` field includes configuration details for backups: 
    * `backupScope`: Indicates which resources are backed up. This example uses `selectedNamespaces`. Possible values include: 
      * `allNamespaces`: captures all resources in all namespaces.
      * `selectedNamespaces`: captures resources in the list of specified namespaces.
      * `selectedApplication`: captures resources defined by `protectedApplications`.
    * `namespaces`: Applicable if `backupScope` is `selectedNamespaces`.
  * `CLUSTER_BACKUP_REPOSITORY`: value for `clusterBackupRepositoryName` in `clusterBackupConfig`. This is the target repository that stores the backups and must be imported as `ReadWrite`.
  * `BACKUP_DELETE_LOCK_DAYS`: prevents deletion of the backup for the number of days specified after backup creation, for example, `10 days`.
  * `BACKUP_RETAIN_DAYS`: defines the total number of days to retain the backup. After this period, the backup is automatically deleted. Setting this value to a higher number might lead to storage exhaustion, while setting it to a lower value can increase the risk of data loss. This value is set to 35 by default if not specified. Retention policies don't override the retention policies of the storage location, nor can they exceed 90 days.
  * `BACKUP_PLAN_DESCRIPTION`: a description of the backup plan.



After you create your backup plan, backups automatically generate with the specified backup configuration based on the backup schedule.

## View a backup plan

View a backup plan using the GDC console:

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click **Select project** and select an organization to see all backup plans in an organization or select a project to see all backup plans in a project.
  4. Click the **Backup Plans** tab.
  5. Click a backup plan in the list to view its details. Users with User Cluster Backup Admin privileges can view all backup plans in the organization. Users with the Backup Creator role can view all backup plans in the selected project.



## Edit a backup plan

Edit a backup plan using the GDC console:

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click **Select project** , and select an organization to see all backup plans in an organization, or select a project to see all of the backup plans in a project.
  4. Click the **Backup Plans** tab.
  5. Click the name of the backup plan that you want to edit.
  6. Click the **Plan Configuration** tab to view the fields that can be modified.
  7. Click the _edit_ Edit icon for **Schedule and retention** to edit that resource:

     1. To update a schedule, enter an expression using standard cron syntax in the **CRON string** field. For example, the expression `10 3 * * *` creates a backup at 0310 every day. All times are interpreted as UTC. The minimum interval between scheduled backups is 10 minutes.
     2. In the **Delete backups after** field, set the number of days for which to retain the backup. Once the number of days is reached, the backup is automatically deleted.
     3. In the **Prevent deletion for** field, set the number of days during which backups cannot be deleted.

**Note:** If both fields are enabled, the value of the **Prevent deletion for** field must be less than the value of the **Delete backups after** field.
     4. To lock the retention policy, click the lock icon from **Off** to **On**.

**Note:** Once the retention policy is locked, you can't edit the retention policy of this backup plan again. You can only update the schedule.
     5. Click the **Save** button to confirm your changes.




## Deactivate a backup plan

**Warning:** This operation can't be undone. Deactivating the backup plan doesn't delete the backups contained within it, but you can't create any new backups automatically or manually.

Deactivate a backup plan using the GDC console:

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click **Select project** , and select an organization to see all backup plans in an organization or select a project to see all backup plans in a project.
  4. Click the **Backup Plans** tab.
  5. Click the name of the backup plan you want to deactivate.
  6. Click the **Deactivate Plan** button.
  7. Enter the name of the backup plan you are deactivating into the field.
  8. Click the **Deactivate** button to complete the deactivation of this backup plan.



## What's next

  * [Back up your workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/back-up-workloads)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
