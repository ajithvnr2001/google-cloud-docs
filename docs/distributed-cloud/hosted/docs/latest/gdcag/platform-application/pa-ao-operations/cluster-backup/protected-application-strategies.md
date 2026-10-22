---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/protected-application-strategies/
title: Protected application strategies \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:36.368515+00:00
---

# Protected application strategies  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/protected-application-strategies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Protected application strategies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the different protected application strategies available in Google Distributed Cloud (GDC) air-gapped.

Protected application strategies lets you run specific pre-execution and post-execution hooks and define custom behavior for quiescing, backing up, or restoring a stateful workload.

There are three backup and restore strategies that you can use when defining a `ProtectedApplication` resource:

  * Back up all and restore all
  * Back up one and restore all
  * Dump and load



Strategy definitions can include the following values:

Type | Attribute | Description  
---|---|---  
`BackupAllRestoreAll` |  | Back up and restore everything in the component.  
| `backupPreHooks` | List of hooks to execute before backup.  
| `backupPostHooks` | List of hooks to execute after backup.  
| `volumeSelector` | Label selector specifying what persistent volumes to backup. If empty, all PVs are selected.  
`backupOneRestoreAll` |  | Back up one copy of a selected pod and use it to restore all pods.  
| `backupTargetName` | The name of the preferred `Deployment` or ` StatefulSet` to use for the backup.  
| `backupPreHooks` | List of hooks to execute before backup.  
| `backupPostHooks` | List of hooks to execute after backup.  
| `volumeSelector` | Label selector specifying what persistent volumes to back up. If empty, all PVs are selected.  
`dumpAndLoad` |  | Uses a dedicated volume for backup and restore.  
| `dumpTarget` | Specifies the name of the preferred `Deployment` or `StatefulSet` that is used to dump the component data. The target pod is selected based on how this component is composed:  


  * Deployment: pick the only pod created by the target `Deployment`.


  * Single-StatefulSet: pick the second pod created by the target `StatefulSet` if the replica number is greater than two. Otherwise, pick the only pod.


  * Multi-StatefulSet: pick the first pod created by the target `StatefulSet`

  
| ` loadTarget ` | Specifies the name of the preferred `Deployment` or `StatefulSet` that is used to load the component data. The target pod is selected based on how this component is composed:  


  * Deployment: pick the only pod created by the target `Deployment`.


  * StatefulSet: always pick the first pod created by the target `StatefulSet`.

  
| `dumpHooks` | List of hooks that are used to dump the data.  
| `backupPostHooks` | List of hooks to execute after backup.  
| `loadHooks` | List of hooks that are used to load the data of this component from dedicated volume. It might also include cleanup steps after the load is completed. The execution target pod is one of the pods selected from the `LoadTarget`.  
| `volumeSelector` | Label selector specifying what persistent volumes to backup. If empty, all PVs are selected.  
  
## Back up all and restore all

This strategy backs up all of the application resources during the backup, and restores all of those resources during the restore. This strategy works best for standalone applications, where applications have no replication between pods.

For a backup all and restore all strategy, include the following information in the resource definition:

  * **Hooks** : define commands that are executed before and after taking volume backups, such as application quiesce and unquiesce steps. These commands are executed on all pods within a component.

  * **Volume selection** : provides finer granularity on which volumes are backed up and restored within the component. Any volumes not selected are not backed up. During a restore, any volumes skipped during backup are restored as empty volumes.




This example creates a `ProtectedApplication` resource that quiesces the file system before backing up the logs volume and unquiesces after the backup:
    
    
    kind: ProtectedApplication
    apiVersion: gkebackup.gke.io/v1
    metadata:
      name: nginx
      namespace: sales
    spec:
      resourceSelection:
        type: Selector
        selector:
          matchLabels:
            app: nginx
      components:
      - name: nginx-app
        resourceKind: Deployment
        resourceNames: ["nginx"]
        strategy:
          type: BackupAllRestoreAll
          backupAllRestoreAll:
            backupPreHooks:
            - name: fsfreeze
              container: nginx
              Commands: [ /sbin/fsfreeze, -f, /var/log/nginx ]
            backupPostHooks:
            - name: fsunfreeze
              container: nginx
              commands: [ /sbin/fsfreeze, -u, /var/log/nginx ]
    

## Back up one and restore all

This strategy backs up one copy of a selected pod. This single copy is the source for restoring all pods during a restore. This method can help reduce storage cost and backup time. This strategy works in a high availability configuration when a component is deployed with one primary `PersistentVolumeClaim` and multiple secondary `PersistentVolumeClaims`.

For a back up one and restore all strategy, you must include the following information in the resource definition:

  * **Backup target** : specifies which `Deployment` or `StatefulSet` to use to back up the data. The best pod to back up is automatically selected. In a high availability configuration, Google recommends to back up from a secondary `PersistentVolumeClaim`.
  * **Hooks** : defines commands that are executed before and after taking volume backups, such as application quiesce and unquiesce steps. These commands are only executed on the selected backup pod.
  * **Volume selection** : provides finer granularity on which volumes are backed up and restored within the component.



If a component is configured with multiple `Deployment` or `StatefulSet` resources, all resources must have the same `PersistentVolume` structure, and follow these rules:

  * The number of `PersistentVolumeClaim` resources used by all `Deployment` or `StatefulSet` resources must be the same.
  * The purpose of `PersistentVolumeClaim` resources in the same index must be the same. For `StatefulSet` resources, the index is defined in the `volumeClaimTemplate`. For `Deployment` resources, the index is defined in `Volume` resources and any non-persistent volumes are skipped.



Given these considerations, multiple volume sets can be selected for backup, but only one volume from each volume set is selected.

This example, assuming an architecture of one primary `StatefulSet` and a secondary `StatefulSet`, shows a backup of the volumes within a single pod in a secondary `StatefulSet`, and then a restore to all other volumes:
    
    
    kind: ProtectedApplication
    apiVersion: gkebackup.gke.io/v1
    metadata:
      name: mariadb
      namespace: mariadb
    spec:
      resourceSelection:
        type: Selector
        selector:
          matchLabels:
            app: mariadb
      components:
      - name: mariadb
        resourceKind: StatefulSet
        resourceNames: ["mariadb-primary", "mariadb-secondary"]
        strategy:
          type: BackupOneRestoreAll
          backupOneRestoreAll:
            backupTargetName: mariadb-secondary
            backupPreHooks:
            - name: quiesce
              container: mariadb
              command: [...]
            backupPostHooks:
            - name: unquiesce
              container: mariadb
              command: [...]
    

## Dump and load

This strategy uses a dedicated volume for backup and restore processes and requires a dedicated `PersistentVolumeClaim` attached to a component that stores dump data. For a dump and load strategy, include the following information in the resource definition:

  * **Dump target:** specifies which `Deployment` or `StatefulSet` should be used to dump the data. The best pod to back up is automatically selected. In a high availability configuration, it is recommended to back up from a secondary `PersistentVolumeClaim`.
  * **Load target:** specifies which `Deployment` or `StatefulSet` should be used to load the data. The best pod to back up is automatically selected. The load target does not have to be the same as the dump target.
  * **Hooks:** defines the commands that are executed before and after taking volume backups. There are specific hooks you must define for dump and load strategies: 
    * **Dump hooks:** defines the hooks that dump the data into the dedicated volume before back up. This hook is executed only on the selected dump pod.
    * **Load hooks:** defines the hooks that load the data after the application starts. This hook is executed only on the selected load pod.
    * **Optional - Post-backup hooks:** defines the hooks that are executed after the dedicated volumes are backed up, such as cleanup steps. This hook is executed only on the selected dump pod.
  * **Volume selection:** specifies all of the dedicated volumes that store the dump data. You must select only one volume for each dump and load pod.



If the application consists of `Deployments`, each `Deployment` must have exactly one replica.

This example, assuming an architecture of one primary `StatefulSet` and a secondary `StatefulSet` with dedicated `PersistentVolumeClaims` for both primary and secondary `StatefulSets`, shows a dump and load strategy:
    
    
    kind: ProtectedApplication
    apiVersion: gkebackup.gke.io/v1
    metadata:
      name: mariadb
      namespace: mariadb
    spec:
      resourceSelection:
        type: Selector
        selector:
          matchLabels:
            app: mariadb
      components:
      - name: mariadb-dump
        resourceKind: StatefulSet
        resourceNames: ["mariadb-primary", "mariadb-secondary"]
        backupStrategy:
          type: DumpAndLoad
          DumpAndLoad:
            loadTarget: mariadb-primary
            dumpTarget: mariadb-secondary
            dumpHooks:
            - name: db_dump
              container: mariadb
              commands:
              - bash
              - "-c"
              - |
                mysqldump -u root --all-databases > /backup/mysql_backup.dump
            loadHooks:
            - name: db_load
              container: mariadb
              commands:
              - bash
              - "-c"
              - |
                mysql -u root < /backup/mysql_backup.sql
        volumeSelector:
          matchLabels:
            gkebackup.gke.io/backup: dedicated-volume
    

## What's next

  * [Plan a set of backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-backups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
