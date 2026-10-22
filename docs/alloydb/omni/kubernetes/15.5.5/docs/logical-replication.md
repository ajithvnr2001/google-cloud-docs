---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/logical-replication/
title: Configure logical replication in Kubernetes \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:01.736196+00:00
---

# Configure logical replication in Kubernetes  |  AlloyDB Omni for Kubernetes: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/logical-replication/

This page documents AlloyDB Omni version **15.5.5** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)



Send feedback 

#  Configure logical replication in Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

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

In PostgreSQL, _logical replication_ is a method for copying data changes from a publisher database to one or more subscribers, which can be databases or other applications. You can enable and configure logical replication on clusters that you create using the AlloyDB Omni Kubernetes Operator. 

This document provides examples that show you how to create and configure a publisher cluster and a subscriber cluster. Before you read this document, you should be familiar with the [AlloyDB Omni overview](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview). You should also be aware of the [limitations of PostgreSQL logical replication](https://www.postgresql.org/docs/current/logical-replication-restrictions.html).

The code snippets on this page are examples that you can use as models, replacing the values with values for your AlloyDB Omni resources.

## Create the clusters

  1. [Install Omni Operator on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/deploy-kubernetes).

  2. Create a publisher cluster.
         
         $ cat << EOF | kubectl apply -f -
         apiVersion: v1
         kind: Secret
         metadata:
           name: db-pw-publisher
         type: Opaque
         data:
           publisher: "b2RzcGFzc3dvcmQ=" # Password is odspassword
         ---
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: publisher
         spec:
           primarySpec:
             adminUser:
               passwordRef:
                 name: db-pw-publisher
             databaseVersion: "15.5.5"
             resources:
               memory: 10Gi
               cpu: 1
               disks:
               - name: DataDisk
                 size: 40Gi
         EOF
         

  3. Create a subscriber cluster.
         
         $ cat << EOF | kubectl apply -f -
         apiVersion: v1
         kind: Secret
         metadata:
           name: db-pw-subscriber
         type: Opaque
         data:
           subscriber: "b2RzcGFzc3dvcmQ=" # Password is odspassword
         ---
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: subscriber
         spec:
           primarySpec:
             adminUser:
               passwordRef:
                 name: db-pw-subscriber
             databaseVersion: "15.5.5"
             resources:
               memory: 10Gi
               cpu: 1
               disks:
               - name: DataDisk
                 size: 40Gi
         EOF
         




## Configure the publisher cluster

Configure the publisher cluster and create a table. Optionally, you can publish data as a test to make sure it is replicated to the subscriber.

  1. Update parameter `wal_level` to `logical`.
         
         $ kubectl patch dbclusters.al publisher  -p '{"spec":{"primarySpec":{"parameters":{"wal_level":"logical"}}}}' --type=merge
         

  2. Find the pod that you need.
         
         $ kubectl get pod -l "alloydbomni.internal.dbadmin.goog/dbcluster=publisher, alloydbomni.internal.dbadmin.goog/task-type=database, dbs.internal.dbadmin.goog/ha-role=Primary"
         

  3. Sign in to the database pod for the publisher cluster.
         
         NAME                                          READY   STATUS    RESTARTS   AGE
         al-2bce-publisher-0                           3/3     Running   0          36m
         $ kubectl exec -ti al-2bce-publisher-0  -- /bin/bash
         

  4. Create a database called `customer`.
         
         CREATE DATABASE customer;
         

  5. Optional: For test purposes, add a table to the database and insert some data. You can use this data to observe data replication from the publisher to the subscriber.
         
         $ psql -h localhost -U postgres customer
         customer=# CREATE TABLE COMPANY(
         customer(#    ID INT PRIMARY KEY     NOT NULL,
         customer(#    NAME           TEXT    NOT NULL,
         customer(#    AGE            INT     NOT NULL,
         customer(#    SALARY         REAL
         customer(# );
         CREATE TABLE
         customer=# INSERT INTO COMPANY (ID,NAME,AGE,SALARY) VALUES
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
         
         customer=# select * from company;
         id | name  | age | salary
         ----+-------+-----+--------
           1 | Quinn  |  25 |  65000
           2 | Kim  |  22 |  72250
           3 | Bola   |  31 |  53000
           4 | Sasha |  33 | 105000
           5 | Yuri |  27 |  85000
         (5 rows)
         

  6. Create a user `logicalreplica` for replication and to grant permissions to.
         
         CREATE USER logicalreplica WITH REPLICATION LOGIN PASSWORD '123';
         

  7. Grant permissions. This example uses a public schema.
         
         GRANT SELECT ON ALL TABLES IN SCHEMA public TO logicalreplica;
         GRANT USAGE ON SCHEMA public TO logicalreplica;
         ALTER DEFAULT PRIVILEGES IN SCHEMA public
             GRANT SELECT ON TABLES TO logicalreplica;
         

  8. Create a publication in the `customer` database.
         
         CREATE PUBLICATION pub_customer;
         ALTER PUBLICATION pub_customer ADD TABLE company;
         




## Configure the subscriber cluster

Enable the subscriber cluster to receive data updates from the publisher cluster.

  1. Set parameter `wal_level` to `logical` in the subscriber database.
         
         $ kubectl patch dbclusters.al subscriber  -p '{"spec":{"primarySpec":{"parameters":{"wal_level":"logical"}}}}' --type=merge
         

  2. Find the pod that you need.
         
         $ kubectl get pod -l "alloydbomni.internal.dbadmin.goog/dbcluster=subscriber, alloydbomni.internal.dbadmin.goog/task-type=database, dbs.internal.dbadmin.goog/ha-role=Primary"
         

  3. Log into the subscriber cluster database pod.
         
         $ kubectl get pod
         NAME                                          READY   STATUS    RESTARTS   AGE
         al-2bce-publisher-0                           3/3     Running   0          20h
         
         $ kubectl exec -ti al-3513-subscriber-0  -- /bin/bash
         Defaulted container "database" out of: database, logrotate-agent, memoryagent, dbinit (init)
         postgres@al-3513-subscriber-0:/$
         

  4. Find the IP address of the publisher pod, like `10.116.14.190`
         
         $ kubectl get service
         NAME                     TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)          AGE
         al-publisher-rw-ilb      ClusterIP      10.116.14.190   <none>         5432/TCP         21h
         

  5. Take a schema backup from the publisher as an initial copy of the published data in the publisher database. Logical replication does not support DDL replication. A schema or table that you plan to replicate must exist in the destination (subscriber cluster) before logical replication starts.
         
         postgres@al-3513-subscriber-0:/$ pg_dump -h 10.116.14.190 -U postgres --create --schema-only customer > /tmp/customer.schema-only.sql
         

  6. Apply the backup in the subscriber database.
         
         postgres@al-3513-subscriber-0:/$ psql -h localhost -U postgres < /tmp/customer.schema-only.sql
         

  7. Optional: Verify that no data is in the table.
         
         # There is no data in table company
         customer=# select * from company;
         id | name | age | salary
         ----+------+-----+--------
         (0 rows)
         

  8. Create a subscription for the database `customer`.
         
         postgres@al-3513-subscriber-0:/$ psql -h localhost -U postgres customer
         customer=# CREATE SUBSCRIPTION sub_customer CONNECTION 'host=10.116.14.190 port=5432 user=logicalreplica dbname=customer password=123' PUBLICATION pub_customer;
         

  9. Optional: Verify replication on the subscriber cluster.
         
         postgres@al-3513-subscriber-0:/$ psql -h localhost -U postgres customer
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
         postgres@al-2bce-publisher-0:/$ psql -h localhost -U postgres customer
         customer=# insert into company(id, name, age, salary) values (6, 'Alex', 39, 100000);
         

  11. On the subscriber cluster, verify that the row added to the table in the publisher cluster has been replicated to table in the subscriber cluster.
         
         # On the subscriber database, data is synced.
         postgres@al-3513-subscriber-0:/$ psql -h localhost -U postgres customer
         customer=# select * from company;
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

  * [Manage high availability (HA) in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/kubernetes-ha).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
