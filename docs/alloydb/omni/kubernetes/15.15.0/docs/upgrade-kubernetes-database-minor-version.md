---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/upgrade-kubernetes-database-minor-version/
title: Perform a minor database version upgrade for AlloyDB Omni on Kubernetes \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 15.15.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:32:46.044216+00:00
---

# Perform a minor database version upgrade for AlloyDB Omni on Kubernetes  |  AlloyDB Omni using the container orchestrator: 15.15.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/upgrade-kubernetes-database-minor-version/

This page documents AlloyDB Omni version **15.15.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/overview)



Send feedback 

#  Perform a minor database version upgrade for AlloyDB Omni on Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.15.0keyboard_arrow_down

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

  * Low downtime upgrade: This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For [high availability (HA)](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/high-availability/overview) environments running AlloyDB Omni version 15.7.1 or later, AlloyDB Omni upgrades your standby instances first. Then, the AlloyDB Omni operator performs a switchover, promoting one of the upgraded standby instances to be your new primary instance. After the switchover succeeds, your old primary instance is updated.

This process ensures minimal downtime during the upgrade.

  * Simultaneous upgrade: The simultaneous upgrade method is [generally available](https://cloud.google.com/products#product-launch-stages) (GA). For all other circumstances, the AlloyDB Omni operator upgrades all instances simultaneously. This means you will experience downtime during the upgrade.




## Limitations

For low downtime upgrades, one standby instance is unavailable at any given time. To ensure that your database cluster doesn't reach zero Recovery Point Objective (RPO) and doesn't risk losing data, your database cluster must have one primary instance and at least two standby instances.

## Before your begin

  * If your cluster is HA and the AlloyDB Omni version is older than 15.7.1, follow the steps listed in [Update the database clusters](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/upgrade-kubernetes-operator-version#update-clusters) before following this minor version upgrade process.
  * Identify a low traffic period where you can perform the minor version upgrade.
  * To avoid any data loss, [back up your data](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/backup-kubernetes).



## Enable the low downtime minor database version upgrade process

To enable the low downtime minor database version upgrade process, add the following annotation to your database cluster.
    
    
    kubectl annotate dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME
    dbcluster.dbadmin.goog/enableLDTM=true
    

Replace the following variable:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/deploy-kubernetes#create).



## Upgrade your AlloyDB Omni version

To upgrade your 15.15.0 version, update the `databaseVersion` and the `controlPlaneAgentsVersion` fields in the cluster's manifest file, and then re-apply the file.

The following is the beginning of a manifest file that specifies version 15.15.0 for `databaseVersion` and version 1.7.0 for `controlPlaneAgentsVersion`:
    
    
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

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/deploy-kubernetes#create).
  * `DB_VERSION`: the version of the database you are upgrading to.
  * `CONTROL_PLANE_AGENTS_VERSION`: the version of the control plane agents.
  * `OS_TYPE`: Optional. The base operating system for the database image. Valid values are `Debian` and `UBI9`. If you don't specify this, the operator automatically sets it to `Debian` if `databaseVersion` is less than `16.9.0`, and to `UBI9` if `databaseVersion` is `16.9.0` or later.



### Monitor the upgrade process

After you update your manifest file, the AlloyDB Omni operator starts the upgrade process. To monitor the upgrade process, check the `DBCUpgradeInProgress` condition.
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -o yaml | yq '.status.conditions[] | select(.type == "DBCUpgradeInProgress")'
    

Replace the following variable:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/deploy-kubernetes#create).



While the process is in progress, the status is `true`. When the process is complete, the condition's status changes to `false`.

## Troubleshooting

If you receive any failure messages during the upgrade process, see the following sections:

  * Pre-upgrade failures
  * Upgrade failures



### Pre-upgrade failures

If you receive a pre-upgrade failure on your database cluster, then check the message and address the problem accordingly.

If you would like to bypass the pre-upgrade failure message, then you can enable the `force-upgrade` annotation.
    
    
    kubectl annotate dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME upgrade.alloydbomni.dbadmin.google/force-upgrade=true
    

Replace the following variable:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/deploy-kubernetes#create).



After the upgrade process completes, set the `force-upgrade` annotation to `false`.

### Upgrade failures

During the automatic upgrade process, there are several points where it might fail in HA environments. For more information about each failure scenario and which subsequent actions the AlloyDB Omni operator takes, see the following table.

Failure message | Description | Required user actions |  `standby instance upgrade succeeded but the replication lag of the standby(s) is too high to be promoted to synchronous standby(s)` |  The upgrade process succeeded, but the standby instance didn't catch up to the primary instance to establish synchronous replication.  A high amount of traffic goes to the primary instance. As the traffic decreases, the standby instance catches up gradually. After this happens, the `HAReady` condition becomes `true`.  |  Choose an option in  Fix primary and standby instances with different minor versions .   
---|---|---  
`all standbys upgrade succeeded but the switchover instance failed to promote an upgraded standby.` |  Your standby instances upgraded successfully, but the switchover process failed.  | 

  1. Check the status of the switchover custom resource to determine what caused the failure. 
  2. Choose an option in  Fix primary and standby instances with different minor versions . 

  
`standby instance upgrade failed but rollback succeeded.` |  Your standby instance didn't upgrade successfully, but the AlloyDB Omni operator restored it to its previous version successfully.  | 

  1. Check the upgrade failure messages. 
  2. Choose an option in  Fix primary and standby instances with different minor versions . 

  
`standby instance upgrade failed and rollback failed.` |  Your standby instance didn't upgrade successfully and the AlloyDB Omni operator can't restore the instance to its previous version.  |  [ Contact Google support ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/resources/request-support) to troubleshoot.   
  
#### Fix primary and standby instances with different minor versions

To resolve this problem, choose one of the following options:

  * If the issue that caused the upgrade failure is fixed, retry the upgrade.

To retry the upgrade, remove the upgrade's `start-time` annotation from your instance. After you remove the annotation, the AlloyDB Omni operator generates a new start time and re-initiates the upgrade process.
        
        kubectl annotate dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME upgrade.alloydbomni.dbadmin.google/start-time-
        

Replace the following variable:

    * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you provided when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/deploy-kubernetes#create).
  * If the issue that caused the upgrade failure persists, then downgrade your instance to the previous AlloyDB Omni operator version.

To downgrade your instance, follow the upgrade process and change the `databaseVersion`, `controlPlaneAgentsVersion`, and `databaseImageOSType` fields in the manifest file to the version you used before. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
