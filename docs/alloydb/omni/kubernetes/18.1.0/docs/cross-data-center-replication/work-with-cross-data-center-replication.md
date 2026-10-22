---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/cross-data-center-replication/work-with-cross-data-center-replication/
title: Work with cross-data-center replication \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:25:27.368472+00:00
---

# Work with cross-data-center replication  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/cross-data-center-replication/work-with-cross-data-center-replication/

This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)



Send feedback 

#  Work with cross-data-center replication Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/cross-data-center-replication/work-with-cross-data-center-replication)



This page describes how to use cross-data-center replication by creating and working with secondary database clusters in Kubernetes.

For a conceptual overview of cross-data-center replication, see [About cross-data-center-replication](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/cross-data-center-replication/about-cross-data-center-replication).

## Before you begin

  * Confirm that you have reliable and low latency network connectivity between the primary and secondary data centers, which is crucial for cross-data-center replication to function effectively.
  * [Install](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes) the latest version of AlloyDB Omni operator to deploy AlloyDB Omni on a Kubernetes cluster in the primary data center and a Kubernetes cluster in the secondary data center. Cross-data-center replication is supported in AlloyDB Omni operator version 1.5.0 and later.
  * [Create an AlloyDB Omni database cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes#create) on the Kubernetes cluster in the primary data center.
  * Make sure the primary and standby database servers in your primary database cluster have adequate Write-Ahead Logging (WAL) space that can accommodate the WAL files required for replication to the secondary cluster. Any data which isn't replicated yet to the secondary cluster is stored in the primary cluster as WAL files. Depending on the connection speed between the primary and secondary clusters, you might need additional disk space for this purpose.
  * Keep in mind the following information about secondary database high availability standbys ([Preview](https://cloud.google.com/products#product-launch-stages)): if the AlloyDB Omni operator version and the control plane agent version are 1.7.0 or later, then the secondary database cluster can support high availability (HA) standbys. 

Unlike HA standbys on the primary database cluster, HA standbys on the secondary database cluster are asynchronous until the secondary database cluster is promoted to a primary database. HA standbys automatically become synchronous or asynchronous if the database cluster role is changed during a switchover.




## Create a secondary database cluster

To create an AlloyDB Omni secondary database cluster and enable replication from your primary database cluster, follow these steps:

  1. Verify that external connectivity is enabled on your AlloyDB Omni primary database cluster. If external connectivity is not enabled, add the following to the spec section of the database cluster manifest:
         
         ...
         spec:
           ...
           allowExternalIncomingTraffic: true
          

  2. To use cross-data-center replication with a primary database cluster that has high availability (HA) enabled, confirm that the `replayReplicationSlotsOnStandbys` field is enabled on the primary database cluster:
         
         ...
         spec:
           ...
           availability:
             ...
             replayReplicationSlotsOnStandbys: true
          

Enabling this field, along with the `logReplicationSlots` explained in the following step, synchronizes the replication slot used by the secondary database cluster to all HA standbys. This configuration helps the new HA primary retain any Write-Ahead Logging (WAL) files not yet consumed by the secondary database cluster after a failover or switchover, allowing the secondary database cluster to resume replication without disruption.

**Note:** Expect to see a 10- to 20-second downtime when modifying this field on an existing database cluster. This is because the field requires all HA standbys to restart and reconnect to the primary to take effect. 
  3. To enable replication on your primary database cluster, apply a manifest similar to the following to your Kubernetes cluster on the primary data center:
         
         apiVersion: v1
         kind: Secret
         metadata:
           name: ha-rep-pw-DB_CLUSTER_NAME
           namespace: DB_CLUSTER_NAMESPACE
         type: Opaque
         data:
           rep-user-pw: "ENCODED_PASSWORD"
         ---
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: Replication
         metadata:
           name: REPLICATION_NAME
           namespace: DB_CLUSTER_NAMESPACE
         spec:
           dbcluster:
             name: DB_CLUSTER_NAME
           upstream:
             password:
               name: ha-rep-pw-DB_CLUSTER_NAME
             logReplicationSlot: true

Replace the following:

     * `DB_CLUSTER_NAME`: The name of the database cluster—for example, `dbc-1`.
     * `ENCODED_PASSWORD`: The password for the database user to be used for replication from secondary databases, encoded as a base64 string—for example, `Q2hhbmdlTWUxMjM= for ChangeMe123`. The default value is `alloydbreplica`.
     * `REPLICATION_NAME`: The name of the replication—for example, `replication-1`.
     * `LOG_REPLICATION_SLOT`: Log replication slot data to WAL files. To enable this option, set its value to `true`. The default value is `false`.

We recommend that you enable the `logReplicationSlot` option with a primary database cluster that has high availability (HA) enabled to make sure that replication can continue working after a failover or switchover.

**Note:** Creating a replication with `logReplicationSlot` enabled causes a database restart on the primary. 

Wait for the replication status to be ready.

**Note:** If no active replication is happening on the slot, the replication status shows as ready but not healthy. The unhealthy status is expected when you haven't set up the secondary database cluster yet. 
  4. To get the upstream connection information that is used to configure replication on the secondary database cluster, run the following command:
         
         kubectl get replication REPLICATION_NAME
         kubectl get replication REPLICATION_NAME -o json | jq .status.upstream

Sample output looks similar to the following:
         
         {
             "host": "35.230.32.36",
             "password": {
               "name": "ha-rep-pw-dbc-1"
             },
             "port": 5432,
             "replicationSlotName": "dbc_1_replication_1",
             "username": "alloydbreplica"
           }
           

  5. Take a note of the output since you need it to enable replication on the secondary database cluster in the following step.
  6. [Create an AlloyDB Omni cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes#create) on your Kubernetes cluster in the secondary data center with configuration identical to your primary database cluster.
  7. Verify that external connectivity is enabled on your AlloyDB Omni secondary database cluster
  8. If external connectivity isn't enabled, add the following to the spec section of its manifest:
         
         ...
         spec:
           ...
           allowExternalIncomingTraffic: true

  9. To enable replication on your secondary database cluster, apply a manifest similar to the following to your Kubernetes cluster on the secondary data center: 
         
         apiVersion: v1
         kind: Secret
         metadata:
           name: ha-rep-pw-SECONDARY_DB_CLUSTER_NAME
           namespace: SECONDARY_DB_CLUSTER_NAMESPACE
         type: Opaque
         data:
           rep-user-pw: "ENCODED_PASSWORD"
         ---
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: Replication
         metadata:
           name: SECONDARY_REPLICATION_NAME
           namespace: SECONDARY_DB_CLUSTER_NAMESPACE
         spec:
           dbcluster:
             name: SECONDARY_DB_CLUSTER_NAME
           downstream:
             host: PRIMARY_HOST
             port: PRIMARY_PORT
             username: alloydbreplica
             password:
               name: ha-rep-pw-SECONDARY_DB_CLUSTER_NAME
             replicationSlotName: PRIMARY_REPLICATION_SLOT
             control: setup

Replace the following:

     * `SECONDARY_DB_CLUSTER_NAME`: the name of the secondary database cluster—for example, `dbc-2`.
     * `ENCODED_PASSWORD`: the password for the database user to be used for replication from the primary database cluster, encoded as a base64 string—for example, `Q2hhbmdlTWUxMjM= for ChangeMe123`. The default value is `alloydbreplica`.
     * `SECONDARY_REPLICATION_NAME`: the name of the replication—for example, `replication-2`.
     * `PRIMARY_HOST`: the connection endpoint of the primary database cluster from the output in step 4 that the secondary database can access for replication.
     * `PRIMARY_PORT`: the connection port of the primary database cluster from the output in step 4 that the secondary database can access for replication.
     * `PRIMARY_REPLICATION_SLOT`: the name of the replication slot on the primary database cluster from the output in step 4 that the secondary database can use for replication.



## View replication on the secondary database cluster

To view detailed information about an AlloyDB Omni secondary database cluster and its replication status, run the following commands:
    
    
    kubectl get dbcluster SECONDARY_DB_CLUSTER_NAME
    kubectl get replication SECONDARY_REPLICATION_NAME

When the secondary database cluster is successfully set up and has streaming replication from the primary database cluster, the replication status is both ready and healthy.

## Promote a secondary database cluster

When you promote a secondary database cluster, you must first verify that the secondary database cluster applied all transactions received from the primary database cluster.

  1. To verify that the cluster is ready and healthy, check the replication status of the secondary database cluster.  

         
         kubectl get replication SECONDARY_REPLICATION_NAME

  2. Stop all writes to the primary database cluster. Execute a checkpoint on the primary database cluster, and then run the following query on your primary database cluster to check the replication lag of the secondary database. Confirm that the result shows a minimal lag. 
     1. Execute a checkpoint to flush memory to disk.  

            
            psql -h PRIMARY_HOST -U postgres -d postgres -c 'CHECKPOINT;'

     2. Check the replication lag. A lag value of `0` is optimal. If the lag is greater than `0`, you can still promote the secondary database cluster. However, there is a risk of losing recent transactions that are already committed on the primary database cluster.  

            
            psql -h PRIMARY_HOST -U postgres -d postgres -c 'SELECT application_name, pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) AS replay_lag FROM pg_stat_replication;'

  3. Promote a secondary database cluster to a primary database cluster by updating the `control` field of your secondary database cluster's replication manifest to `promote`. Then, apply the updated replication manifest on your Kubernetes cluster on the secondary data center. 
         
         apiVersion: v1
         kind: Secret
         metadata:
           name: ha-rep-pw-SECONDARY_DB_CLUSTER_NAME
           namespace: SECONDARY_DB_CLUSTER_NAMESPACE
         type: Opaque
         data:
           rep-user-pw: "ENCODED_PASSWORD"
         ---
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: Replication
         metadata:
           name: SECONDARY_REPLICATION_NAME
           namespace: SECONDARY_DB_CLUSTER_NAMESPACE
         spec:
           dbcluster:
             name: SECONDARY_DB_CLUSTER_NAME
           downstream:
             host: PRIMARY_HOST
             port: PRIMARY_PORT
             username: alloydbreplica
             password:
               name: ha-rep-pw-SECONDARY_DB_CLUSTER_NAME
             replicationSlotName: PRIMARY_REPLICATION_SLOT
             control: promote




## Perform a switchover

Before you perform a switchover, verify that the primary and the secondary database clusters that belong to both data centers are online and that the database clusters are in a healthy state.

To enforce data consistency of your primary and secondary database clusters during switchover, perform the following steps to verify that the secondary database cluster has applied all transactions that it received from the primary database cluster:

  1. Check the replication status of the secondary database cluster, to verify that it's both ready and healthy. 
         
         kubectl get replication SECONDARY_REPLICATION_NAME

  2. Stop all writes to the primary database cluster. Execute a checkpoint on the primary database cluster, and then run the following query on your primary database cluster to check the replication lag of the secondary database.  

     1. Execute a checkpoint to flush memory to disk.  

            
            psql -h PRIMARY_HOST -U postgres -d postgres -c 'CHECKPOINT;'

     2. Confirm that the result shows a lag value of `0`.  

            
            psql -h PRIMARY_HOST -U postgres -d postgres -c 'SELECT application_name, pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) AS replay_lag FROM pg_stat_replication;'

  3. To promote the secondary cluster to become the primary cluster, follow these steps:

     1. To convert your AlloyDB Omni secondary database cluster into a primary database cluster, update its replication manifest on your Kubernetes cluster in the secondary data center as follows:
            
            apiVersion: v1
            kind: Secret
            metadata:
              name: ha-rep-pw-SECONDARY_DB_CLUSTER_NAME
              namespace: SECONDARY_DB_CLUSTER_NAMESPACE
            type: Opaque
            data:
              rep-user-pw: "ENCODED_PASSWORD"
            ---
            apiVersion: alloydbomni.dbadmin.goog/v1
            kind: Replication
            metadata:
              name: SECONDARY_REPLICATION_NAME
              namespace: SECONDARY_DB_CLUSTER_NAMESPACE
            spec:
              dbcluster:
                name: SECONDARY_DB_CLUSTER_NAME
              upstream:
                password:
                  name: ha-rep-pw-SECONDARY_DB_CLUSTER_NAME

Replace `SECONDARY_DB_CLUSTER_NAME`, which is the name of your secondary database cluster—for example, `dbc-2`.

Wait for the replication status to be ready.

     2. To get the upstream connection information for replication, run the following command:
            
            kubectl get replication SECONDARY_REPLICATION_NAME
            kubectl get replication SECONDARY_REPLICATION_NAME -o json | jq .status.upstream

Sample output looks similar to the following:
            
            {
                "host": "34.23.207.137",
                "password": {
                  "name": "ha-rep-pw-dbc-2"
                },
                "port": 5432,
                "replicationSlotName": "dbc_2_replication_2",
                "username": "alloydbreplica"
              }
            

     3. To convert your AlloyDB Omni primary database cluster into a secondary database cluster, update its replication manifest on your Kubernetes cluster on the primary data center similar to the following:
            
            apiVersion: v1
            kind: Secret
            metadata:
              name: ha-rep-pw-DB_CLUSTER_NAME
            type: Opaque
            data:
              rep-user-pw: "ENCODED_PASSWORD"
            ---
            apiVersion: alloydbomni.dbadmin.goog/v1
            kind: Replication
            metadata:
              name: REPLICATION_NAME
            spec:
              dbcluster:
                name: DB_CLUSTER_NAME
              downstream:
                host: SECONDARY_HOST
                port: SECONDARY_PORT
                username: alloydbreplica
                password:
                  name: ha-rep-pw-DB_CLUSTER_NAME
                replicationSlotName: SECONDARY_REPLICATION_SLOT
                control: rewind

Wait for the replication status to become ready and healthy.

     4. To verify the replication status, run the following command:
            
            kubectl get replication REPLICATION_NAME




## Perform unplanned disaster recovery

If you experience a DR failover, follow these steps:

  1. To convert your AlloyDB Omni secondary database cluster into a primary database cluster, update that cluster's replication manifest on your Kubernetes cluster in the secondary data center. For more information, see Step 3a. in Perform a switchover.
  2. To convert the former primary database cluster into a secondary database cluster replicating from the new primary (role reversal), wait for the original primary to become available. Use the `rewind` control in the downstream replication configuration to determine if the conversion works as expected. If you encounter issues, use the `setup` control instead.  


**Note:** The execution of the `setup` control can take a long time to complete, especially when it's applied to large databases. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
