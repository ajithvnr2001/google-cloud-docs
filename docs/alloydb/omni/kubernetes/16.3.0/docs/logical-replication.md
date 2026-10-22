---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/logical-replication/
title: Configure subscriber cluster for logical replication \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:50:22.087235+00:00
---

# Configure subscriber cluster for logical replication  |  AlloyDB Omni for Kubernetes: 16.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/logical-replication/

This page documents AlloyDB Omni version **16.3.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/overview)



Send feedback 

#  Configure subscriber cluster for logical replication Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/logical-replication)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/logical-replication)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/logical-replication)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/logical-replication)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/logical-replication)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/logical-replication)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/logical-replication)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/logical-replication)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/logical-replication)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/logical-replication)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/logical-replication)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/logical-replication)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/logical-replication)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/logical-replication)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/logical-replication)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/logical-replication)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/logical-replication)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/logical-replication)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/logical-replication)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/logical-replication)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/logical-replication)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/logical-replication)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/logical-replication)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/logical-replication)

This document provides examples that show you how to manually create and configure a _subscriber cluster_. A subscriber cluster is a database cluster that receives data replicated from a publisher cluster. 

The code snippets on this page are examples that you can use as models, replacing the values with values for your AlloyDB Omni resources.

## Before you begin

  * [Install Omni Operator on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/deploy-kubernetes).
  * Ensure that you create a replication slot, publisher cluster, and publication. For more information, see [Create replication slots and publication](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/create-replication-slots).



## Create and configure the subscriber cluster

  1. Create a subscriber cluster.
         
         $ cat << EOF | kubectl apply -f -
         apiVersion: v1
         kind: Secret
         metadata:
           name: db-pw-DB_CLUSTER_NAME
         type: Opaque
         data:
           DB_CLUSTER_NAME: "ENCODED_PASSWORD" # Password is odspassword
         ---
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: subscriber
         spec:
           databaseVersion: "16.3.0"
           primarySpec:
             adminUser:
               passwordRef:
                 name: db-pw-DB_CLUSTER_NAME
             resources:
               memory: MEMORY_SIZE
               cpu: CPU_COUNT
               disks:
               - name: DataDisk
                 size: DISK_SIZE
         EOF
         

Replace the following:

     * `DB_CLUSTER_NAME`: the name of this database cluster—for example, `subscriber-cluster`.
     * `ENCODED_PASSWORD`: the database login password for the default `postgres` user role, encoded as a base64 string—for example, `Q2hhbmdlTWUxMjM=` for `ChangeMe123`.

     * `CPU_COUNT`: the number of CPUs available to each database instance in this database cluster.

     * `MEMORY_SIZE`: the amount of memory per database instance of this database cluster. We recommend setting this to 8 gigabytes per CPU. For example, if you set `cpu` to `2` earlier in this manifest, then we recommend setting `memory` to `16Gi`.

     * `DISK_SIZE`: the disk size per database instance—for example, `10Gi`.

  2. Find the pod that you need.
         
         $ kubectl get pod -l "alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME, alloydbomni.internal.dbadmin.goog/task-type=database, dbs.internal.dbadmin.goog/ha-role=Primary"
         

  3. Log into the subscriber cluster database pod.
         
         $ kubectl get pod
         NAME                                          READY   STATUS    RESTARTS   AGE
         al-2bce-publisher-0                           3/3     Running   0          20h
         
         $ kubectl exec -ti SUBSCRIBER_POD_NAME  -- /bin/bash
         Defaulted container "database" out of: database, logrotate-agent, memoryagent, dbinit (init)
         postgres@al-3513-subscriber-0:/$
         

Replace `SUBSCRIBER_POD_NAME` with the name of the subscriber pod.

  4. Find the IP address of the load balancer on publisher DBcluster, like `10.116.14.190`
         
         $ kubectl get service
         NAME                     TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)          AGE
         al-publisher-rw-ilb      ClusterIP      10.116.14.190   <none>         5432/TCP         21h
         

  5. Take a schema backup from the publisher as an initial copy of the published data in the publisher database. Logical replication does not support DDL replication. A schema or table that you plan to replicate must exist in the destination (subscriber cluster) before logical replication starts.
         
         postgres@al-3513-subscriber-0:/$ pg_dump -h PUBLISHER_IP_ADDRESS -U postgres --create --schema-only customer > /tmp/customer.schema-only.sql
         

Replace `PUBLISHER_IP_ADDRESS` with the IP address of the load balancer on publisher DBcluster.

  6. Apply the backup in the subscriber database.
         
         postgres@al-3513-subscriber-0:/$ psql -h localhost -U postgres < /tmp/customer.schema-only.sql
         

  7. Optional: Verify that no data is in the table.
         
         # There is no data in table company
         customer=# select * from company;
         id | name | age | salary
         ----+------+-----+--------
         (0 rows)
         

  8. Create a subscription for the database. Ensure that the publication is already created on the publisher DBCluster.
         
         postgres@al-3513-subscriber-0:/$ CREATE SUBSCRIPTION sub_customer CONNECTION 'host=PUBLISHER_IP_ADDRESS port=5432 user=REPLICATION_USER dbname=DATABASE_NAME password=PUBLISHER_CLUSTER_PASSWORD sslmode=require' PUBLICATION PUBLICATION_NAME WITH (slot_name='REPLICATION_SLOT_NAME');
         

Replace the following:

     * REPLICATION_USER: the name of the user that connects to the replication slot.
     * DATABASE_NAME: set to the name of the database whose changes you want to stream from the replication slot.
     * PUBLISHER_CLUSTER_PASSWORD: the database login password for the `postgres` user of publisher DBCluster.
     * PUBLICATION_NAME: the publication name that subscriber subscribes to.
     * REPLICATION_SLOT_NAME: the name of the replication slot created on publisher DBCluster.
  9. Optional: Verify replication on the subscriber cluster.
         
         postgres@al-3513-subscriber-0:/$ psql -h localhost -U postgres DATABASE_NAME
         customer=# select * from public.company;
         id | name  | age | salary
         ----+-------+-----+--------
           1 | Quinn |  25 |  65000
           2 | Kim   |  22 |  72250
           3 | Bola  |  31 |  53000
           4 | Sasha |  33 | 105000
           5 | Yuri  |  27 |  85000
         (5 rows)
         

  10. On the publisher cluster, add a row to the table.
         
         # On the publisher database
         $ kubectl exec -ti al-2bce-publisher-0  -- /bin/bash
         Defaulted container "database" out of: database, logrotate-agent, memoryagent, dbinit (init)
         postgres@al-2bce-publisher-0:/$ psql -h localhost -U postgres DATABASE_NAME
         customer=# insert into TABLE_NAME (id, name, age, salary) values (6, 'Alex', 39, 100000);
         

Replace the TABLE_NAME with the name of the table in the publisher DBCluster that the subscriber is subscribed to.

  11. On the subscriber cluster, verify that the row added to the table in the publisher cluster has been replicated to table in the subscriber cluster.
         
         # On the subscriber database, data is synced.
         postgres@al-3513-subscriber-0:/$ psql -h localhost -U postgres DATABASE_NAME
         customer=# select * from TABLE_NAME;
         id | name  | age | salary
         ----+-------+-----+--------
           1 | Quinn |  25 |  65000
           2 | Kim   |  22 |  72250
           3 | Bola  |  31 |  53000
           4 | Sasha |  33 | 105000
           5 | Yuri  |  27 |  85000
           6 | Alex  |  39 | 100000
         (6 rows)
         




## Manually create additional tables

Logical replication doesn't automatically synchronize DDL changes, unlike the `replicate_ddl_command` in `pglogical`. While the open-source tool [`pgl_ddl_deploy`](https://github.com/enova/pgl_ddl_deploy) offers a solution, you can also execute DDL commands manually on the subscriber.

  1. To illustrate this, create a new table called `finance` in the `customer` database on the publisher cluster.
         
         # On the publisher database
         $ kubectl exec -ti al-2bce-publisher-0  -- /bin/bash
         Defaulted container "database" out of: database, logrotate-agent, memoryagent, dbinit (init)
         postgres@al-2bce-publisher-0:/$ psql -h localhost -U postgres customer
         customer=# create table finance (row text);
         CREATE TABLE
         customer=# insert into finance values ('critical data');
         INSERT 0 1
         customer=# ALTER PUBLICATION pub_customer ADD TABLE finance;
         ALTER PUBLICATION
         

  2. When a new table is added to the publisher cluster, you manually apply the DDL (table creation) in the subscriber, and then verify replication by running the following on the subscriber cluster.
         
         postgres@al-3513-subscriber-0:/$ psql -h localhost -U postgres customer
         customer=# create table finance (row text);
         CREATE TABLE
         customer=# ALTER SUBSCRIPTION sub_customer REFRESH PUBLICATION;
         ALTER SUBSCRIPTION
         customer=# select * from finance;
               row
         ---------------
         critical data
         (1 row)
         




## What's next

  * [Manage high availability (HA) in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/kubernetes-ha)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
