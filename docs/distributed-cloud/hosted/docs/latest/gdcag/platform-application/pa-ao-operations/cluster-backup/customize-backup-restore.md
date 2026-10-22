---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/customize-backup-restore/
title: Customize backup and restore for an application \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:56.919167+00:00
---

# Customize backup and restore for an application  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/customize-backup-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Customize backup and restore for an application Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use `ProtectedApplication` resources to customize the behavior of backup and restores in Google Distributed Cloud (GDC) air-gapped.

These steps are optional and aren't required to successfully configure backup and restoration for your workloads. `ProtectedApplication` resources are optional Kubernetes resources in namespaces that customize the backup and restore of individual stateful applications. Without `ProtectedApplication` resources, the following restrictions apply:

  * You restrict the backup and restore scope granularity to the namespace level.
  * No flush and quiesce operations occur on workloads during backup execution.This might result in virtual machines with multiple disks not being crash-consistent after restoration.



`ProtectedApplication` resources are optional Kubernetes namespace resources used to customize the backup and restore of individual stateful applications. The `ProtectedApplication` resource defines which Kubernetes resources belong to an application instance. You can manually set up a specialized orchestration using the `kubectl` command to create a backup and restore of those applications in the following scenarios:

  * To identify a set of resources in a namespace that might be backed up or restored independently of the other resources in that namespace. A `ProtectedApplication` is the most fine-grained namespace entity that you can identify for a backup or restore scope.
  * To provide specialized backup orchestration whenever the `ProtectedApplication` falls within the scope of a backup. In particular, if the `ProtectedApplication` contains `PersistentVolumeClaim` (PVC) resources either directly or through a template from a `StatefulSet`, you can run _hooks_ before and after backing up the volumes. Hooks are commands that run in application containers. These hooks are often used for flush, quiesce, or unquiesce operations, and provide an application-consistent backup.



## Before you begin

Define the `ProtectedApplication` resource before creating a backup plan. For more information, see [Plan a set of backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-backups).

### Request IAM roles

To use `ProtectedApplication` resources, ask your IAM Org Admin or IAM Project Admin to grant you one of the following roles:

  * **User Cluster Backup Admin** (`user-cluster-backup-admin`): creates, gets, lists, watches, updates, patches, and deletes backup resources such as backup and restore plans in user clusters. Contact your IAM Org Admin to request this role.

  * **Backup Creator** (`backup-creator`): creates, gets, lists, watches, updates, patches, and deletes manual backup requests and manual restore requests. Contact your IAM Project Admin to request this role.




## Deploy protected application resources

The following yaml snippet is an example of a `Deployment` specification with a `ProtectedApplication` resource that backs up all of the resources associated with the application during backup, and restores all resources during the restore:
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: "applications"
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: protected-application-deployment
      namespace: applications
      labels:
        app: protected
    spec:
      selector:
        matchLabels:
          app: nginx
      replicas: 2
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: nginx:1.14.2
            ports:
            - containerPort: 80
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: unprotected-application-deployment
      namespace: applications
      labels:
        app: unprotected
    spec:
      selector:
        matchLabels:
          app: nginx
      replicas: 2
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: nginx:1.14.2
            ports:
            - containerPort: 80
    ---
    
    apiVersion: gkebackup.gke.io/v1
    kind: ProtectedApplication
    metadata:
      name: protected-application-test
      namespace: applications
    spec:
      applicationName: protectedApplication
      resourceSelection:
        type: Selector
        selector:
          matchLabels:
            app: protected
      components:
        - name: protect-application-deployment
          resourceKind: Deployment
          resourceNames:
            - protected-application-deployment
          strategy:
            type: BackupAllRestoreAll
            backupAllRestoreAll: {}
    

Specify the `ProtectedApplication` in the list of `selectedApplications` in the `backupScope`. For example:
    
    
    apiVersion: backup.gdc.goog/v1
    kind: BackupPlan
    metadata:
      name: protected-application-backupplan-test
      namespace: applications
    spec:
      clusterName: "cluster-sample"
      backupSchedule:
        cronSchedule: "*/30 * * * *"
        paused: true
      backupConfig:
        backupScope:
          selectedApplications:
            namespacedNames:
            - name: protected-application-test
              namespace: applications
        backupRepository: "backup-repository"
      retentionPolicy:
        backupDeleteLockDays: 10
        backupRetainDays: 10
    

This example includes the following values:

Value | Description  
---|---  
`resourceSelection` | Defines how to identify resources that belong to the protected application: 

  * `type:` Specify one of:
    * `ApplicationName`: Backs up a sig-apps application within the same namespace.
    * `Selector`: Backs up resources that match a given selector within the same namespace.
  * `applicationName`: If `type` is `ApplicationName`, specifies the name of the sig-apps Application within the same namespace.
  * `selector`: If `type` is `Selector`, specifies the label selector to select resources within the same namespace.

  
`components` | The list of components for the protected application, such as deployments or stateful sets: 

  * `name`: The unique name of the component.


  * `resourceKind`: Choose between `Deployment` or `StatefulSet`.


  * `resourceNames`: The list of names identifying the `resourceKind` in the namespace.


  * `strategy`: Additional details on how to back up or restore this component. For more information, see [Protected application strategies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/protected-application-strategies). 

  
  
## What's next

  * To select a protected application strategy, see [Protected application strategies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/protected-application-strategies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
