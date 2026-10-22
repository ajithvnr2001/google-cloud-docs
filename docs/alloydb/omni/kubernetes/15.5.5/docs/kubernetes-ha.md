---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/kubernetes-ha/
title: Manage high availability in Kubernetes \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:28:23.179955+00:00
---

# Manage high availability in Kubernetes  |  AlloyDB Omni for Kubernetes: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/kubernetes-ha/

This page documents AlloyDB Omni version **15.5.5** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)



Send feedback 

#  Manage high availability in Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/kubernetes-ha)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/kubernetes-ha)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/kubernetes-ha)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/kubernetes-ha)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/kubernetes-ha)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/kubernetes-ha)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/kubernetes-ha)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/kubernetes-ha)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/kubernetes-ha)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/kubernetes-ha)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/kubernetes-ha)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/kubernetes-ha)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/kubernetes-ha)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/kubernetes-ha)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/kubernetes-ha)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/kubernetes-ha)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/kubernetes-ha)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-ha)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/kubernetes-ha)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/kubernetes-ha)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/kubernetes-ha)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/kubernetes-ha)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/kubernetes-ha)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/kubernetes-ha)

This page shows you how to enable and test high availability (HA) on your Kubernetes-based AlloyDB Omni database cluster. Performing the tasks documented here requires basic knowledge about applying Kubernetes manifest files and using the `kubectl` command-line tool. 

## Overview

You can enable HA in your database cluster by directing the AlloyDB Omni Kubernetes Operator to create standby replicas of your primary database instance. The AlloyDB Omni Operator configures your database cluster to continuously update the data on this replica, matching all changes to data on your primary instance.

## Enable HA

Before you enable HA on your database cluster, ensure that your Kubernetes cluster has the following:

  * Storage for two complete copies of your data
  * Compute resources for two database instances running in parallel



To enable HA, follow these steps:

  1. Modify the database cluster's manifest to include an `availability` section under its `spec` section. This section defines the number of standbys that you want to add by setting the `numberOfStandbys` parameter.
         
         spec:
           availability:
             numberOfStandbys: NUMBER_OF_STANDBYS
         

Replace `NUMBER_OF_STANDBYS` with the number of standbys you want to add. The maximum value is `5`. If you're setting up HA and are unsure about the number of standbys you need, then start by setting the value to either `1` or `2`.

  2. Re-apply the manifest.




## Disable HA

To disable HA, follow these steps:

  1. Set `numberOfStandbys` to `0` in the cluster's manifest:
         
         spec:
           availability:
             numberOfStandbys: 0
         

  2. Re-apply the manifest.




## Verify HA on a database cluster

To view the current HA status of a database cluster, check the `HAReady` condition of that cluster's status. If this value has a `status` set to `True`, then HA is set up and working on the database cluster.

To check this value on the command line, run the following command:
    
    
    kubectl get dbcluster.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -o jsonpath={.status.conditions[?(@.type == \'HAReady\')]} -n NAMESPACE

Replace the following:

  * `DB_CLUSTER_NAME`: the name of the database cluster.

  * `NAMESPACE`: the namespace of the database cluster.




## Fail over to a standby instance

If your primary instance becomes unavailable for a configurable period of time, then the AlloyDB Omni Operator automatically fails over from the primary database instance to the standby instance. The default time to trigger automatic failover is 90 seconds.

Failovers are a good option when you want to quickly recover from an unexpected failure and minimize downtime, even if it means potentially losing a small amount of data, if the primary database becomes unavailable before the backup is fully updated.

The AlloyDB Omni Operator supports both automatic and manual failover. Automatic failover is enabled by default.

Failover results in the following sequence of events:

  1. The AlloyDB Omni Operator takes the primary database instance offline.

  2. The AlloyDB Omni Operator promotes the standby replica to be the new primary database instance.

  3. The AlloyDB Omni Operator deletes the previous primary database instance.

  4. The AlloyDB Omni Operator creates a new standby replica.




### Disable automatic failover

Automatic failovers are enabled by default on database clusters.

To disable a failover, follow these steps:

  1. Set `enableAutoFailover` to `false` in the cluster's manifest:
         
         spec:
           availability:
             enableAutoFailover: false
         




### Adjust automatic failover trigger settings

You can use settings to adjust automatic failovers for each database cluster.

The AlloyDB Omni Operator issues regular health checks every 30 seconds. If an instance has reached the automatic failover trigger threshold, the AlloyDB Omni Operator triggers an automatic failover.

The default value for the automatic failover trigger threshold is `3`. The threshold value is the number of consecutive failures for the health check before a failover is triggered. To change the threshold value, set `autoFailoverTriggerThreshold` to an integer value in the cluster's manifest:
    
    
    ```yaml
    spec:
      availability:
        autoFailoverTriggerThreshold: TRIGGER_THRESHOLD
    ```
    

Replace the following:

  * `TRIGGER_THRESHOLD`: a integer value for the number of consecutive failures for the health check before a failover is triggered. The default value is `3`.



### Trigger a manual failover

To trigger a manual failover, create and apply a manifest for a new failover resource:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Failover
    metadata:
      name: FAILOVER_NAME
      namespace: NAMESPACE
    spec:
      dbclusterRef: DB_CLUSTER_NAME
    

Replace the following:

  * `FAILOVER_NAME`: a name for this resource—for example, `failover-1`.

  * `NAMESPACE`: the namespace for this failover resource, which must match the namespace of the database cluster that it applies to.

  * `DB_CLUSTER_NAME`: the name of the database cluster to fail over.




To monitor the failover, run the following command:
    
    
    kubectl get failover FAILOVER_NAME -o jsonpath={.status.state} -n NAMESPACE

Replace the following:

  * `FAILOVER_NAME`: the name that you assigned the failover resource when you created it.

  * `NAMESPACE`: the namespace of the database cluster.




The command returns `Success` after the new primary database instance is ready for use. To monitor the status of the new standby instance, see the next section.

## Switchover to a standby instance

Switchover is performed when you want to test your disaster recovery setup or any other planned activities that require switching the roles of the primary database and the standby replica.

After the switchover completes, the roles of the primary database instance and the standby replica are reversed along with the direction of replication. You must opt for switchovers if you want better control over the process of testing your disaster recovery setup with zero data loss.

The AlloyDB Omni Operator supports manual switchover.

Switchover results in the following sequence of events:

  1. The AlloyDB Omni Operator takes the primary database instance offline.

  2. The AlloyDB Omni Operator promotes the standby replica to be the new primary database instance.

  3. The AlloyDB Omni Operator switches the previous primary database instance to a standby replica.


**Note:** You can configure a standby replica to be used as a read-only instance. For more information, see Use a standby as a read-only instance

### Perform a switchover

Before you perform a switchover, ensure the following:

  * Verify that both your primary database instance and the standby replica are in healthy state. For more information, see [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/manage).
  * Verify that the current HA status is in `HAReady` condition. For more information, see Verify HA on a database cluster.



To perform a switchover, create and apply a manifest for a new switchover resource:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Switchover
    metadata:
        name: SWITCHOVER_NAME
    spec:
         dbclusterRef: DB_CLUSTER_NAME
         newPrimary: STANDBY_REPLICA_NAME
    

Replace the following:

  * `SWITCHOVER_NAME`: a name for this switchover resource—for example, `switchover-1`.

  * `DB_CLUSTER_NAME`: the name of the primary database instance that switchover operation applies to.

  * `STANDBY_REPLICA_NAME`: the name of the database instance that you want to promote as new primary.

To identify the standby replica name, run the following command: `posix-terminal kubectl get instances.alloydbomni.internal.dbadmin.goog`


**Important:** Local backups taken before the switchover was performed cannot be automatically restored using the `Restore` custom resource. If you want to manually clone the backup, see [Clone a database cluster in Kubernetes using a local backup](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/kubernetes-dr-backup-k8-local).

## Use standby replica as a read-only instance

To use a standby replica as a read-only instance, complete the following steps:

  1. Modify the database cluster's manifest to set the `enableStandbyAsReadReplica` parameter to `true`.
         
         spec:
           availability:
             enableStandbyAsReadReplica: true
         

  2. Re-apply the manifest.

  3. Verify that the read-only endpoint is reported in the `status` field of the `DBCluster` object:
         
         kubectl describe dbcluster -n NAMESPACE DB_CLUSTER_NAME

The following example response shows the endpoint of the read-only instance:
         
         Status:
           [...]
           Primary:
             [...]
             Endpoints:
               Name: Read-Write
               Value: 10.128.0.81:5432
               Name: Read-Only
               Value: 10.128.0.82:5432
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
