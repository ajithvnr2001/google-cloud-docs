---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/upgrade-kubernetes-database-minor-version/
title: Perform a minor database version upgrade for AlloyDB Omni on Kubernetes \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:42:02.823983+00:00
---

# Perform a minor database version upgrade for AlloyDB Omni on Kubernetes  |  AlloyDB Omni using the container orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/upgrade-kubernetes-database-minor-version/

This page documents AlloyDB Omni version **18.3.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/overview)



Send feedback 

#  Perform a minor database version upgrade for AlloyDB Omni on Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/upgrade-kubernetes-database-minor-version)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/upgrade-kubernetes-database-minor-version)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/upgrade-kubernetes-database-minor-version)



This page describes how to perform a minor database version upgrade for AlloyDB Omni on Kubernetes.

To perform a minor database version upgrade, there are two options:

  * Low downtime upgrade (LDTM): in [highly available (HA) environments](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/high-availability/overview), the AlloyDB Omni operator upgrades your standby instances first. Once all standbys are successfully upgraded, the operator performs a switchover, promoting one of the upgraded standby instances to be your new primary instance. After the switchover succeeds, the old primary instance is upgraded. This sequential rolling process ensures minimal downtime and keeps the primary active on the previous version until the upgrade of the standby environment is fully validated.
  * Simultaneous upgrade: in non-HA environments or if LDTM is explicitly disabled, the AlloyDB Omni operator upgrades all database instances simultaneously. This method causes database downtime during the upgrade process.



## Limitations

During the low downtime upgrade process, each standby instance is upgraded sequentially and is temporarily unavailable while upgrading.

To ensure that your database cluster maintains a zero Recovery Point Objective (RPO) and doesn't risk data loss during the standby upgrade, it is recommended to have at least two standby instances. This setup acts as a three-node HA configuration.

## Before you begin

  * If your cluster is HA and the AlloyDB Omni version is older than 15.7.1, follow the steps listed in [Update the database clusters](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/upgrade-kubernetes-operator-version#upgrade-clusters) before following this minor version upgrade process.
  * To avoid any data loss, [back up your data](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/backup-kubernetes).
  * While the low downtime upgrade operation is ongoing, the database cluster HA redundancy is temporarily degraded while a standby instance undergoes upgrade. However, the database remains available for read and write traffic on the active primary instance.



## Enable the low downtime minor database version upgrade process

The low downtime upgrade (LDTM) process is automatically enabled by default if your database cluster has two or more standbys.

If your database cluster has only one standby, you must manually enable LDTM by adding the `dbcluster.dbadmin.goog/enableLDTM=true` annotation to your database cluster:
    
    
    kubectl annotate dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME
    dbcluster.dbadmin.goog/enableLDTM=true
    

Replace the following variable:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/deploy-kubernetes#create).



## Upgrade your AlloyDB Omni version

To upgrade your 18.3.0 version, update the `databaseVersion` and the `controlPlaneAgentsVersion` fields in the cluster's manifest file, and then re-apply the file.

The following is the beginning of a manifest file that specifies version 18.3.0 for `databaseVersion` and version 1.8.2 for `controlPlaneAgentsVersion`:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
        name: DB_CLUSTER_NAME
    spec:
        **databaseVersion : "DB_VERSION"**
        **controlPlaneAgentsVersion : "CONTROL_PLANE_AGENTS_VERSION"**
        # It is recommended to switch to UBI9 for improved security and
        # compatibility.
        # If you need to stick to Debian, set this field to "Debian".
        **databaseImageOSType : "OS_TYPE"**
    ...
    

Replace the following variable:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/deploy-kubernetes#create).
  * `DB_VERSION`: the version of the database you are upgrading to.
  * `CONTROL_PLANE_AGENTS_VERSION`: the version of the control plane agents.
  * `OS_TYPE`: Optional. The base operating system for the database image. Valid values are `Debian` and `UBI9`. If you don't specify this, the operator automatically sets it to `Debian` if `databaseVersion` is less than `16.9.0`, and to `UBI9` if `databaseVersion` is `16.9.0` or later.



### Monitor the upgrade process

After you update your manifest file, the AlloyDB Omni operator starts the upgrade process. To monitor the upgrade process, check the `DBCUpgradeInProgress` condition.
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -o yaml | yq '.status.conditions[] | select(.type == "DBCUpgradeInProgress")'
    

Replace the following variable:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/deploy-kubernetes#create).



While the process is in progress, the condition status is `true`. When the process is complete, the condition's status changes to `false` and the reason updates to `UpgradeComplete` or `UpgradeFailed`.

## Troubleshooting

If you receive any failure messages during the upgrade process, see the following sections:

  * Pre-upgrade failures
  * Upgrade failures



### Pre-upgrade failures

If you receive a pre-upgrade failure on your database cluster, then check the message and address the problem accordingly.

If you would like to bypass the pre-upgrade failure message, then you can enable the `force-upgrade` annotation.
    
    
    kubectl annotate dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME upgrade.alloydbomni.dbadmin.google/force-upgrade=true
    

Replace the following variable:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/deploy-kubernetes#create).



After the upgrade process completes, set the `force-upgrade` annotation to `false`.

### Upgrade failures

During the automatic upgrade process, there are several points where it might fail in HA environments. For more information about each failure scenario and which subsequent actions the AlloyDB Omni operator takes, see the following table.

Failure message | Description | Required user actions |  `Standby instance upgrade succeeded but its replication lag is too high to be promoted to a synchronous standby. Please monitor replication status.` |  The standby instance upgraded successfully, but couldn't catch up to the primary instance fast enough to meet the synchronous replication threshold before the timeout window. This is typically caused by heavy write traffic on the primary instance.  |  To allow the standby instance to synchronize, perform the following:

  1. Wait for the write traffic to subside so that the standby instance catches up gradually. The AlloyDB Omni operator automatically promotes it once it is synchronized.
  2. (Optional) You can increase the catch-up timeout by setting the `upgrade.alloydbomni.dbadmin.google/standby-catch-up-timeout-in-minutes` annotation on your DBCluster.

  
---|---|---  
`All standbys upgrade succeeded but the switchover instance failed to promote an upgraded standby.` |  Your standby instances upgraded successfully, but the automatic switchover process designed to promote an upgraded standby to primary failed.  |  To investigate and resolve the switchover failure, perform the following steps:

  1. Inspect the status of the switchover custom resource to determine the root cause:  
`kubectl get switchovers.alloydbomni.dbadmin.goog -n NAMESPACE`
  2. Check the switchover controller logs and events for issues like network partitions or API latency.
  3. Choose an option in Fix primary and standby instances with different minor versions.

  
`Standby instance upgrade failed but rollback to the previous versions succeeded` |  The standby instance failed to upgrade, but the AlloyDB Omni operator successfully rolled back the instance to its previous working version. Since the primary instance was never touched, your database remains healthy on the previous version.  |  To diagnose the underlying issue and apply a fix, perform the following steps:

  1. Diagnose the upgrade failure by examining the standby pod's logs and events:  
`kubectl describe pod -l alloydbomni.dbadmin.goog/instance=[standby-name] -n NAMESPACE`
  2. Once the blocker, for example, node resource exhaustion or taints is resolved, choose an option in Fix primary and standby instances with different minor versions.

  
`Standby instance upgrade failed and rollback to the previous versions failed` |  The standby instance failed to upgrade, and the AlloyDB Omni operator's automatic attempt to roll it back to the previous version also failed. The standby instance is left in an unhealthy/unusable state (reducing HA redundancy), while the primary continues to handle read/write traffic on the previous version.  |  To restore cluster health, re-provision the standby as follows:

  1. Delete the unhealthy standby instance by setting the standby count to 0 in the DBCluster spec:  
`kubectl patch dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE --type=merge -p '{"spec": {"availability": {"numberOfStandbys": 0}}}'`
  2. Wait for the broken standby instance and its pod to be fully deleted.
  3. Scale the standby count back up to provision a clean standby instance that will automatically sync with the active primary:  
`kubectl patch dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE --type=merge -p '{"spec": {"availability": {"numberOfStandbys": 1}}}'`

  
  
#### Fix primary and standby instances with different minor versions

To resolve this problem, choose one of the following options:

  * If the underlying issue that caused the upgrade failure has been resolved, you can re-initiate the upgrade. Remove the upgrade's `start-time` annotation from your DBCluster to prompt the AlloyDB Omni operator to generate a new start time and retry:
        
        kubectl annotate dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME upgrade.alloydbomni.dbadmin.google/start-time-
        

Replace `DB_CLUSTER_NAME` with the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/deploy-kubernetes#create).

  * If the issue that caused the upgrade failure persists and you prefer to keep the cluster on the previous version, you don't need to perform a downgrade procedure. Because the upgrade failed during the standby phase, your primary was never upgraded.

To clear the `UpgradeFailed` status and return to a stable, non-upgrading state, update your DBCluster manifest's `databaseVersion` and `controlPlaneAgentsVersion` fields back to the versions used prior to the upgrade attempt, then re-apply the file. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
