---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/create-replication-slots/
title: Create a replication slot and publication \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 15.17.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:20.582852+00:00
---

# Create a replication slot and publication  |  AlloyDB Omni using the container orchestrator: 15.17.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/create-replication-slots/

This page documents AlloyDB Omni version **15.17.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/overview)



Send feedback 

#  Create a replication slot and publication Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.17.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/create-replication-slots)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/create-replication-slots)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/create-replication-slots)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/create-replication-slots)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/create-replication-slots)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/create-replication-slots)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/create-replication-slots)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/create-replication-slots)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/create-replication-slots)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/create-replication-slots)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/create-replication-slots)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/create-replication-slots)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/create-replication-slots)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/create-replication-slots)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/create-replication-slots)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/create-replication-slots)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/create-replication-slots)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/create-replication-slots)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/create-replication-slots)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/create-replication-slots)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/create-replication-slots)



This document describes how to create logical replication slots in AlloyDB Omni. In PostgreSQL, _logical replication_ is a method for copying data changes from a publisher database to one or more subscribers, which can be databases or other applications. You can enable and configure logical replication on clusters that you create using the AlloyDB Omni Kubernetes Operator.

**Note:** You can only create logical replication slots on AlloyDB Omni Kubernetes operator and control plane agents version 1.3.0 and later.

The streamed changes can be individual row updates, insertions, or deletions. Subscribers connect to the publisher through a unique replication slot that ensures a persistent connection. A persistent connection maintains the data streaming state, so if a disruption occurs, streaming resumes from where it left off.

For more information about logical replication in PostgreSQL, see [Logical Replication](https://www.postgresql.org/docs/15/logical-replication.html).

The code snippets on this page are examples that you can use as models, replacing the values with values for your AlloyDB Omni resources.

## Before you begin

  * [Install Omni Operator on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/deploy-kubernetes).



## Create a publisher cluster

Before you create the replication slots, you must create the publisher cluster with logical replication enabled. You must set the `wal_level` parameter to `logical` in the `DBCluster` manifest.

To create publisher database cluster with logical replication enabled, apply the following manifest:
    
    
      apiVersion: v1
      kind: Secret
      metadata:
        name: db-pw-DB_CLUSTER_NAME
        namespace: DB_CLUSTER_NAMESPACE
      type: Opaque
      data:
        DB_CLUSTER_NAME: "ENCODED_PASSWORD"
      ---
      apiVersion: alloydbomni.dbadmin.goog/v1
      kind: DBCluster
      metadata:
        name: DB_CLUSTER_NAME
        namespace: DB_CLUSTER_NAMESPACE
      spec:
        databaseVersion: "ALLOYDB_OMNI_VERSION"
        spec:
        availability:
          numberOfStandbys: 1
        primarySpec:
          parameters:
            **wal_level: "logical"**
          adminUser:
            passwordRef:
              name: db-pw-DB_CLUSTER_NAME
          resources:
            cpu: CPU_COUNT
            memory: MEMORY_SIZE
            disks:
            - name: DataDisk
              size: DISK_SIZE

Replace the following:

  * `DB_CLUSTER_NAME`: the name of this database cluster—for example, `publisher`.

  * `DB_CLUSTER_NAMESPACE` (Optional): the namespace where you want to create the database cluster—for example, `publisher-namespace`.

  * `ENCODED_PASSWORD`: the database login password for the default `postgres` user role, encoded as a base64 string—for example, `Q2hhbmdlTWUxMjM=` for `ChangeMe123`.

  * `ALLOYDB_OMNI_VERSION`: the AlloyDB Omni version, `15.7.0` or later.

  * `CPU_COUNT`: the number of CPUs available to each database instance in this database cluster.

  * `MEMORY_SIZE`: the amount of memory per database instance of this database cluster. We recommend setting this to 8 gigabytes per CPU. For example, if you set `cpu` to `2` earlier in this manifest, then we recommend setting `memory` to `16Gi`.

  * `DISK_SIZE`: the disk size per database instance—for example, `10Gi`.




## Create a replication slot

After you create the publisher cluster, you can create a logical replication slot using the `Replication` resource in the publisher cluster. Each `Replication` resource is associated with a corresponding database cluster resource. A database cluster can have multiple logical replication resources associated with it.

To configure a replication slot in your publisher cluster, apply the following manifest:
    
    
    $ cat << EOF | kubectl apply -f -
    apiVersion: v1
    kind: Secret
    metadata:
      name: USER_PASSWORD_SECRET_NAME
      namespace: USER_PASSWORD_SECRET_NAMESPACE
    type: Opaque
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Replication
    metadata:
      name: REPLICATION_NAME
      namespace: NAMESPACE
    spec:
      dbcluster:
        name: DB_CLUSTER_NAME
      upstream:
        logicalReplication:
          pluginName: DECODER_PLUGIN
          databaseName: DATABASE_NAME
        applicationName: APPLICATION_NAME
        replicationSlotName: REPLICATION_SLOT_NAME
        synchronous: "REPLICATION_MODE"
        username: APPLICATION_USER
        password:
          name: USER_PASSWORD_SECRET_NAME
          namespace: USER_PASSWORD_SECRET_NAMESPACE
    EOF

Replace the following:

  * REPLICATION_NAME: a name for this `Replication` resource—for example, `replication-1`.
  * NAMESPACE: the Kubernetes namespace for this `Replication` resource. It must match the namespace of the database cluster.
  * DB_CLUSTER_NAME: the name of your database cluster, which you assigned when you created it.
  * DECODER_PLUGIN: set to the decoding plugin, such as `pgoutput`, that you want to use for logical replication. For more information about various decoding plugins, see [Output plugins](https://www.postgresql.org/docs/current/logicaldecoding-explanation.html#LOGICALDECODING-EXPLANATION-OUTPUT-PLUGINS).
  * DATABASE_NAME: set to the name of the database whose changes you want to stream to the replication slot. Ensure that the database is already created in the publisher cluster.
  * APPLICATION_NAME (Optional): set to the application name that will connect to the replication slot. This field is required when the streaming mode is set to synchronous.
  * REPLICATION_MODE (Optional): set to `false` for asynchronous replication. If you want to enable synchronous replication, but at the expense of speed, then set this value as `true`. The default value is `false`, if not set explicitly.
  * REPLICATION_SLOT_NAME: the name of the replication slot that will be created, and used by the subscriber—for example, `logicalrepltestslot`.
  * REPLICATION_USER (Optional): the name of the user that connects to the replication slot. If you set the replication user, then setting the secret name, namespace, and password is required.
  * USER_PASSWORD_SECRET_NAME (Optional): the application user's Kubernetes Secret name. Required, if application user is set.
  * USER_PASSWORD_SECRET_NAMESPACE (Optional): the namespace where the Kubernetes secret for the application user is located. Required, if application user is set.



## View replication slot status

To view the status of the replication slots, run the following command:
    
    
    kubectl get replication.alloydbomni.dbadmin.goog REPLICATION_NAME -n NAMESPACE -oyaml
    

The `status` field along with other details is included in the response:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Replication
    metadata:
      name: REPLICATION_NAME
      namespace: NAMESPACE
    ...
    ...
    status:
      conditions:
      - lastTransitionTime: "2025-01-25T06:49:25Z"
        **message: Ready for replication**
        reason: Ready
        status: "True"
        type: Ready
      - lastTransitionTime: "2025-01-25T06:49:25Z"
        **message: Replication slot is not being used**
        reason: Unhealthy
        status: "False"
        type: Healthy
      observedGeneration: 2
      upstream:
        **host: DATABASE_ENDPOINT**
        password:
          name: USER_PASSWORD_SECRET_NAME
          namespace: USER_PASSWORD_SECRET_NAMESPACE
        port: DATABASE_PORT
        replicationSlotName: REPLICATION_SLOT_NAME
        username: APPLICATION_USER

The `DATABASE_ENDPOINT` shows the IP address that you use to connect to the database. The status `TRUE` in the `READY` column indicates that the slot is ready to stream. When the subscriber DBCluster or application connects to the replication slot, the status in the `HEALTHY` column changes to `TRUE`.

**Note:** A replication slot's `HEALTHYREASON` status shows as `Unhealthy` when no application is streaming from it. This indicates that the slot is actually healthy and ready to accept connections.

## Configure the publisher cluster

  1. Find the pod that you need.
         
         $ kubectl get pod -l "alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME, alloydbomni.internal.dbadmin.goog/task-type=database, dbs.internal.dbadmin.goog/ha-role=Primary"
         

  2. Connect to the primary pod on publisher cluster using `psql`:
         
         psql -h IP_ADDRESS -U USERNAME -d DATABASE_NAME

Replace the following:

     * IP_ADDRESS: the IP address of the primary pod of the publisher cluster.
     * USERNAME: the postgres user of the database.
     * DATABASE_NAME: the database to which the subscriber wants to subscribe.
  3. If the `DATABASE_NAME` specified in the replication resource doesn't exist, create a database.
         
         CREATE DATABASE DATABASE_NAME;
         

  4. Optional: For test purposes, add a table to the database and insert some data. You can use this data to observe data replication from the publisher to the subscriber.
         
         $ psql -h localhost -U postgres DATABASE_NAME
         customer=# CREATE TABLE TABLE_NAME(
         customer(#    ID INT PRIMARY KEY     NOT NULL,
         customer(#    NAME           TEXT    NOT NULL,
         customer(#    AGE            INT     NOT NULL,
         customer(#    SALARY         REAL
         customer(# );
         CREATE TABLE
         customer=# INSERT INTO TABLE_NAME (ID,NAME,AGE,SALARY) VALUES
         customer-# (1, 'Quinn', 25, 65000.00),
         customer-# (2, 'Kim', 22, 72250.00),
         customer-# (3, 'Bola', 31, 53000.00),
         customer-# (4, 'Sasha', 33, 105000.00),
         customer-# (5, 'Yuri', 27, 85000.00);
         INSERT 0 5
         customer=# \dt
                   List of relations
         Schema |  Name   | Type  |  Owner
         --------+---------+-------+----------
         public | company | table | postgres
         (1 row)
         
         customer=# select * from TABLE_NAME;
         id | name  | age | salary
         ----+-------+-----+--------
           1 | Quinn  |  25 |  65000
           2 | Kim  |  22 |  72250
           3 | Bola   |  31 |  53000
           4 | Sasha |  33 | 105000
           5 | Yuri |  27 |  85000
         (5 rows)
         

Replace the TABLE_NAME with a table where you want to store the data and which the subscriber subscribes to.

  5. Grant the permissions:
         
         GRANT SELECT ON ALL TABLES IN SCHEMA public TO REPLICATION_USER;
         GRANT USAGE ON SCHEMA public TO REPLICATION_USER;
         ALTER DEFAULT PRIVILEGES IN SCHEMA public
         GRANT SELECT ON TABLES TO REPLICATION_USER;
         

  6. Create publication by running the following command:
         
         CREATE PUBLICATION PUBLICATION_NAME;
         ALTER PUBLICATION PUBLICATION_NAME ADD TABLE TABLE_NAME;
         

Replace the following:

     * PUBLICATION_NAME: the publication name that subscriber will use to subscribe.



After creating the publication, you can either [set up your subscriber cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/logical-replication) for logical replication or configure your application to start replicating.

## Limitations

  * Updates to the replication slot configuration aren't supported. To update the configuration, drop the replication slot, and re-create it with updated configuration.

To drop the replication slot, run the following command:
        
        kubectl delete replication.alloydbomni.dbadmin.goog REPLICATION_NAME -n NAMESPACE
        

  * You can only configure the logical replication slot on the publisher database. The replication API doesn't support logical replication subscriber DBCluster or applications.

  * If the database cluster referenced by the replication object is configured for high availability, then the logical replication slot is recreated on the promoted standby after a failover. After the replication slot is recreated, the position of the stream in the slot is no longer available, and any applications subscribing to the stream must reconnect and replay the stream.




## What's next

  * [Configure subscriber cluster for logical replication](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/logical-replication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
