---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/cross-data-center-replication/work-with-cross-data-center-replication/
title: Work with cross-data-center replication \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:07:05.376509+00:00
---

# Work with cross-data-center replication  |  AlloyDB Omni for containers: 15.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/cross-data-center-replication/work-with-cross-data-center-replication/

This page documents AlloyDB Omni version **15.7.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/overview)



Send feedback 

#  Work with cross-data-center replication Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.0keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/cross-data-center-replication/work-with-cross-data-center-replication)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/cross-data-center-replication/work-with-cross-data-center-replication)

This page describes how to use cross-data-center replication by creating and working with secondary database clusters in Kubernetes. 

For a conceptual overview of cross-data-center replication, see [About cross-data-center replication](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/cross-data-center-replication/about-cross-data-center-replication).

## Before you begin

  * [Install](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/deploy-kubernetes) AlloyDB Omni operator version 1.1.0 or higher to deploy AlloyDB Omni on a Kubernetes cluster in the primary data center and a Kubernetes cluster in the secondary data center.
  * [Create an AlloyDB Omni database cluster](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/deploy-kubernetes#create) on the Kubernetes cluster in the primary data center.



## Create a secondary database cluster

To create an AlloyDB Omni secondary database cluster and enable replication from your primary database cluster, follow these steps:

###  Kubernetes 

  1. Ensure external connectivity is enabled on your AlloyDB Omni primary database cluster. If external connectivity is not enabled, add the following to the spec section of the database cluster manifest:
         
         kind: DBCluster
           spec:
            allowExternalIncomingTraffic: true
         

  2. To use cross-data-center replication with a primary database cluster that has HA enabled, make sure that both the primary and standby database servers in your primary database cluster have adequate Write-Ahead Logging (WAL) space that can accomodate the WAL files required for replication to the secondary cluster. Set the WAL size for your AlloyDB Omni primary database cluster by setting the spec section of the database cluster manifest:
         
         kind: DBCluster
           spec:
             primarySpec:
               parameters:
                 wal_keep_size: WAL_KEEP_SIZE
                 max_wal_size: MAX_WAL_SIZE
         

Replace the following:

     * `WAL_KEEP_SIZE`: The minimum size of past WAL files stored in the WAL directory in case a secondary server needs to fetch them for streaming replication. If a secondary server connected to the primary server falls behind by more than `wal_keep_size` megabytes, the primary server might remove a WAL segment that the secondary server needs. In this case, the replication connection is terminated. Downstream connections will also eventually fail as a result. Set `WAL_KEEP_SIZE` to a value that supports your workload requirements, based on WAL generation rate, replication network characteristics and replication lag between the data centers where your primary and secondary database clusters are deployed. The default is 100MB.
     * `MAX_WAL_SIZE`: Maximum size to let the WAL grow during automatic database checkpoints. The default is 1504MB. This value must be set higher than the `wal_keep_size` value.
  3. To enable replication on your primary database cluster, apply a manifest similar to the following to your Kubernetes cluster on the primary data center:
         
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
          upstream:
            password:
              name: ha-rep-pw-DB_CLUSTER_NAME
         

Replace the following:

     * `DB_CLUSTER_NAME`: The name of the database cluster—for example, `dbc-1`.
     * `ENCODED_PASSWORD`: The password for the database user to be used for replication from secondary databases, encoded as a base64 string—for example, `Q2hhbmdlTWUxMjM= for ChangeMe123`. The default value is `alloydbreplica`.
     * `REPLICATION_NAME`: the name of the replication—for example, `replication-1`.

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

  6. [Create an AlloyDB Omni cluster](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/deploy-kubernetes#create) on your Kubernetes cluster in the secondary data center with configuration identical to your primary database cluster. 

  7. Ensure external connectivity is enabled on your AlloyDB Omni secondary database cluster.

  8. If external connectivity is not enabled, add the following to the spec section of its manifest:
         
         allowExternalIncomingTraffic: true
         

  9. To enable replication on your secondary database cluster, apply a manifest similar to the following to your Kubernetes cluster on the secondary data center:
         
         apiVersion: v1
           kind: Secret
           metadata:
             name: ha-rep-pw-SECONDARY_DB_CLUSTER_NAME
           type: Opaque
           data:
             rep-user-pw: "ENCODED_PASSWORD"
           ---
           apiVersion: alloydbomni.dbadmin.goog/v1
           kind: Replication
           metadata:
             name: SECONDARY_REPLICATION_NAME
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

     * `SECONDARY_DB_CLUSTER_NAME`: The name of the secondary database cluster—for example, `dbc-2`.
     * `ENCODED_PASSWORD`: The password for the database user to be used for replication the primary database cluster, encoded as a base64 string—for example, `Q2hhbmdlTWUxMjM= for ChangeMe123`. The default value is `alloydbreplica`.
     * `SECONDARY_REPLICATION_NAME`: the name of the replication—for example, `replication-2`.
     * `PRIMARY_HOST`: the connection endpoint of the primary database cluster from the output in step 3 that the secondary database can access for replication.
     * `PRIMARY_PORT`: the connection port of the primary database cluster from the output in step 3 that the secondary database can access for replication.
     * `PRIMARY_REPLICATION_SLOT`: the name of the replication slot on the primary database cluster from the output in step 3 that the secondary database can use for replication.



## View replication on the secondary database cluster

To view detailed information about an AlloyDB Omni secondary database cluster and its replication status, run the following commands:

###  Kubernetes 
    
    
    kubectl get dbcluster SECONDARY_DB_CLUSTER_NAME
    kubectl get replication SECONDARY_REPLICATION_NAME

When the secondary database cluster is successfully set up and has streaming replication from the primary database cluster, the replication status is both ready and healthy.

## Promote a secondary database cluster

Before you promote a secondary database cluster, perform the following steps to verify that the secondary database cluster has applied all transactions received from the primary database cluster:

###  Kubernetes 

  * Check the replication status of the secondary database cluster, to ensure that it's both ready and healthy.
        
        kubectl get replication SECONDARY_REPLICATION_NAME

  * Stop all writes to the primary database cluster. Run the following query on your primary database cluster to check the replication lag of the secondary database. Confirm that the result shows a minimal lag.

A lag value of 0 is ideal. If the lag is greater than 0, you can still promote the secondary database cluster, at the risk of losing some recent transactions already committed on the primary database cluster.
        
        psql -h PRIMARY_HOST -U postgres -d postgres -c 'SELECT application_name, pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) AS replay_lag FROM pg_stat_replication;'




To promote a secondary database cluster to a primary database cluster, update the **control** field of your secondary database cluster's replication manifest to `promote`, and apply that on your Kubernetes cluster on the secondary data center.

###  Kubernetes 
    
    
        apiVersion: v1
        kind: Secret
        metadata:
          name: ha-rep-pw-SECONDARY_DB_CLUSTER_NAME
        type: Opaque
        data:
          rep-user-pw: "ENCODED_PASSWORD"
        ---
        apiVersion: alloydbomni.dbadmin.goog/v1
        kind: Replication
        metadata:
          name: SECONDARY_REPLICATION_NAME
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

To ensure data consistency of your primary and secondary database clusters during switchover, perform the following steps to verify that the secondary database cluster has applied all transactions received from the primary database cluster:

###  Kubernetes 

  * Check the replication status of the secondary database cluster, to ensure that it's both ready and healthy.
        
        kubectl get replication SECONDARY_REPLICATION_NAME

  * Stop all writes to the primary database cluster. Run the following query on your primary database cluster to check the replication lag of the secondary database. Confirm that the result shows a lag value of `0`.
        
        psql -h PRIMARY_HOST -U postgres -d postgres -c 'SELECT application_name, pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) AS replay_lag FROM pg_stat_replication;'




To perform a switchover, complete the following steps:

###  Kubernetes 

  1. To convert your AlloyDB Omni secondary database cluster into a primary database cluster, update its replication manifest on your Kubernetes cluster in the secondary data center as follows:
         
         apiVersion: v1
            kind: Secret
            metadata:
             name: ha-rep-pw-SECONDARY_DB_CLUSTER_NAME
            type: Opaque
            data:
              rep-user-pw: "ENCODED_PASSWORD"
            ---
            apiVersion: alloydbomni.dbadmin.goog/v1
            kind: Replication
            metadata:
             name: SECONDARY_REPLICATION_NAME
            spec:
             dbcluster:
                name: SECONDARY_DB_CLUSTER_NAME
              upstream:
                password:
                  name: ha-rep-pw-SECONDARY_DB_CLUSTER_NAME
         

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

  4. To verify the replication status use:
         
         kubectl get replication REPLICATION_NAME




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
