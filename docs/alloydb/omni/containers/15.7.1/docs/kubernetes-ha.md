---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/kubernetes-ha/
title: Manage high availability in Kubernetes \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:07:10.004808+00:00
---

# Manage high availability in Kubernetes  |  AlloyDB Omni for containers: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/kubernetes-ha/

This page documents AlloyDB Omni version **15.7.1** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)



Send feedback 

#  Manage high availability in Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.1keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/kubernetes-ha)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/kubernetes-ha)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/kubernetes-ha)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/kubernetes-ha)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/kubernetes-ha)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/kubernetes-ha)

This page describes how to enable and test [high availability (HA)](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/high-availability/overview) on your Kubernetes-based AlloyDB Omni database cluster. This document assumes basic knowledge about applying Kubernetes manifest files and using the `kubectl` command-line tool. 

## Overview

You enable HA in your database cluster by configuring the AlloyDB Omni Kubernetes operator to create standby replicas of your primary database instance. The AlloyDB Omni operator configures your database cluster to continuously update the data on this replica, and it matches all data changes on your primary instance.

## Enable HA

Before you enable HA on your database cluster, ensure that your Kubernetes cluster has the following:

  * Storage for two complete copies of your data

  * Compute resources for two database instances running in parallel




To enable HA, follow these steps:

  1. Modify the database cluster's manifest to include an `availability` section under its `spec` section. This section uses the `numberOfStandbys` parameter to specify the number of standbys to add.
         
         spec:
           availability:
             numberOfStandbys: NUMBER_OF_STANDBYS
         

Replace `NUMBER_OF_STANDBYS` with the number of standbys that you want to add. The maximum value is `5`. If you're unsure about the number of standbys you need, then start by setting the value to `1` or `2`.

  2. Re-apply the manifest.




## Disable HA

To disable HA, follow these steps:

  1. Set `numberOfStandbys` to `0` in the cluster's manifest:
         
         spec:
           availability:
             numberOfStandbys: 0
         

  2. Re-apply the manifest.




## Verify HA on a database cluster

To check the status of HA on a database cluster, check its `HAReady` status. If the status of `HAReady` is `True`, then HA is enabled and working on the cluster. If it's `False`, then it's enabled but not ready because it's in the process of being set up.

To check the `HAReady` status using the `kubectl` command-line, run the following command:
    
    
    kubectl get dbcluster.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -o jsonpath={.status.conditions[?(@.type == \'HAReady\')]} -n NAMESPACE

Replace the following:

  * `DB_CLUSTER_NAME`: the name of the database cluster.

  * `NAMESPACE`: the namespace of the database cluster.




## Fail over to a standby instance

If your primary instance becomes unavailable for a configurable period of time, then the AlloyDB Omni operator automatically fails over from the primary database instance to the standby instance. The following parameters determine when to start an automatic failover:

  * The time between health checks (default is 30 seconds)

  * The number of consecutive failed health checks (default is 3)




An automatic failover starts after the specified number of consecutive failed health checks occur, with the specified time between each failed health check. If the default values are retained, then an automatic failover occurs after 3 consecutive health check failures that are each 30 seconds apart.

Performing a manual failover is a good option when you want to quickly recover from an unexpected failure and minimize downtime.

The AlloyDB Omni operator supports both automatic and manual failover. Automatic failover is enabled by default.

Failover results in the following sequence of events:

  1. The AlloyDB Omni operator takes the primary database instance offline.

  2. The AlloyDB Omni operator promotes the standby replica to be the new primary database instance.

  3. The AlloyDB Omni operator deletes the previous primary database instance.

  4. The AlloyDB Omni operator creates a new standby replica.




### Disable automatic failover

Automatic failovers are enabled by default on database clusters.

To disable automatic failover, follow these steps:

  1. Set `enableAutoFailover` to `false` in the cluster's manifest:
         
         spec:
           availability:
             enableAutoFailover: false
         




### Adjust automatic failover trigger settings

You can use settings to adjust automatic failovers for each database cluster.

The AlloyDB Omni operator issues regular health checks to the primary database instance as well as to all standby replicas. The default frequency for health checks is `30` seconds. If an instance reaches the automatic failover trigger threshold, then the AlloyDB Omni operator triggers an automatic failover.

The threshold value is the number of consecutive failures for the health check before a failover is triggered. To change the health check period or the threshold value, set the `healthcheckPeriodSeconds` and `autoFailoverTriggerThreshold` fields to integer values in the cluster's manifest:
    
    
    spec:
      availability:
        healthcheckPeriodSeconds: HEALTHCHECK_PERIOD
        autoFailoverTriggerThreshold: AUTOFAILOVER_TRIGGER_THRESHOLD
    

Replace the following:

  * `HEALTHCHECK_PERIOD`: an integer value that indicates the number of seconds to wait between each health check. The default value is `30`. The minimum value is `1` and the maximum value is `86400` (equivalent to a day).

  * `AUTOFAILOVER_TRIGGER_THRESHOLD`: an integer value for the number of consecutive failures for the health check before a failover is triggered. The default value is `3`. The minimum value is `0`. There is no maximum value. If this field is set to `0`, then the default value of `3` is used instead.




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

After the switchover completes, the direction of replication and the roles of the primary database instance and the standby replica are reversed. Use switchovers to gain more control over testing your disaster recovery setup with no data loss.

The AlloyDB Omni operator supports manual switchover. A switchover results in the following sequence of events:

  1. The AlloyDB Omni operator takes the primary database instance offline.

  2. The AlloyDB Omni operator promotes the standby replica to be the new primary database instance.

  3. The AlloyDB Omni operator switches the previous primary database instance to be a standby replica.


**Note:** You can configure a standby replica to be used as a read-only instance. For more information, see Use a standby as a read-only instance.

### Perform a switchover

Before you begin a switchover, do the following:

  * Verify that both your primary database instance and the standby replica are in a healthy state. For more information, see [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/manage).

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

  * `SWITCHOVER_NAME`: a name for this switchover resource — for example, `switchover-1`.

  * `DB_CLUSTER_NAME`: the name of the primary database instance that switchover operation applies to.

  * `STANDBY_REPLICA_NAME`: the name of the database instance that you want to promote to be the new primary.

To identify the standby replica name, run the following command:
        
        kubectl get instances.alloydbomni.internal.dbadmin.goog


**Important:** If local backups are created before the switchover is performed, you can't restore using the `Restore` custom resource. If you want to manually clone the backup, see [Clone a database cluster in Kubernetes using a local backup](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/kubernetes-dr-backup-k8-local).

## Heal a standby instance automatically

If a standby instance becomes unavailable, then the AlloyDB Omni operator heals the instance by deleting the old standby replica and creating a new standby replica that takes its place. The default time to trigger an automatic heal is 90 seconds.

Automatically healing the database cluster helps maintain healthy, continuous replication of the primary database.

### Disable healing the instance automatically

By default, healing a standby instance automatically is enabled on database clusters.

To disable automatic heals, follow these steps:

  1. In the cluster's manifest, set `enableAutoHeal` to `false`:
         
         spec:
           availability:
             enableAutoHeal: false
         




### Adjust automatic heal trigger settings

For each database cluster, you can use settings to adjust automatic heals.

The AlloyDB Omni operator issues regular health checks that you can configure. For more information, see Adjust automatic failover trigger settings. If a standby replica reaches the automatic heal trigger threshold, then the AlloyDB Omni operator triggers an automatic heal.

The threshold value is the number of consecutive failures for the health check before a heal is triggered. To change the threshold value, set `autoHealTriggerThreshold` in the cluster's manifest:
    
    
    spec:
      availability:
        autoHealTriggerThreshold: AUTOHEAL_TRIGGER_THRESHOLD
    

Replace the following:

  * `AUTOHEAL_TRIGGER_THRESHOLD`: an integer value for the number of consecutive failures for the health check before a heal is triggered. The default value is `5`. The minimum value is `2` because of possible transient, one-time errors on standby health checks.



### Troubleshoot instance healing

If you use a large number of database clusters in a single Kubernetes cluster, or if you have database clusters that are underprovisioned, automatic healing might cause unavailability for the AlloyDB Omni operator or the database clusters. If you receive an error that starts with `HealthCheckProber: health check for instance failed` and the error references a timeout or failure to connect, try the following recommended fixes:

  * Reduce the number of database clusters you're managing in your Kubernetes cluster.

  * Increase the `healthcheckPeriodSeconds` threshold value so that health checks occur less frequently. For more information, see Adjust automatic failover trigger settings.

  * Increase the `autoHealTriggerThreshold` value so that automatic healing occurs less frequently. For more information, see Adjust automatic heal trigger settings.

  * Disable automatic healing on database clusters. For more information, see Disable healing the instance automatically.

  * Increase the CPU limit, the memory limit, or both, for the AlloyDB Omni operator. For more information, see [About automatic memory management](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/automatic-memory-management) and [Analyze AlloyDB Omni operator memory heap usage](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/analyze-memory-heap-usage).

  * Increase the resource limits for the AlloyDB Omni database clusters. For more information, see [Resize your Kubernetes-based database cluster](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/manage#resize-kubernetes).




The following are examples of errors that might be caused by overwhelming automatic healing. These examples omit environment details that help you identify the error source, such as the name of a cluster or an IP address.

  * `HealthCheckProber: health check for instance failed" err="DBSE0005: DBDaemon Client Error. secure dbdaemon connection failed: context deadline exceeded...`

  * `HealthCheckProber: health check for instance failed" err="rpc error: code = Code(10303) desc = DBSE0303: Healthcheck: Health check table query failed. dbdaemon/healthCheck: read healthcheck table: timeout...`

  * `HealthCheckProber: health check for instance failed" err="rpc error: code = Code(12415) desc = DBSE2415: Postgres: failed to connect to database. dbdaemon/healthCheck: failed to connect...`




## Use standby replica as a read-only instance

To use a standby replica as a read-only instance, complete the following steps:

  1. Set `enableStandbyAsReadReplica` to `true` in the manifest of the database cluster:
         
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
