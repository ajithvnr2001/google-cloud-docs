---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/set-up-read-replica/
title: Create a read-only replica \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:52:06.758982+00:00
---

# Create a read-only replica  |  AlloyDB Omni for Kubernetes: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/set-up-read-replica/

This page documents AlloyDB Omni version **15.5.5** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)



Send feedback 

#  Create a read-only replica Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/set-up-read-replica)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/set-up-read-replica)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/set-up-read-replica)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/set-up-read-replica)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/set-up-read-replica)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/set-up-read-replica)

To increase read throughput and availability, you can create an AlloyDB Omni replica server for an existing AlloyDB Omni server. A replica server provides a read-only clone of your primary database server. It continuously updates its own data to reflect changes to your primary server's data. 

The following sections provide steps to configure your AlloyDB Omni primary server for replication, configure the replica server, and verify replication status on the primary server.

The information on this page applies only to AlloyDB Omni for containers. It does not apply to AlloyDB Omni for Kubernetes.

For details, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/deploy-kubernetes).

## Configure your primary server for replication

  1. Update the network or firewall settings of your primary server's host so that it allows ingress traffic from the replica server's host through the primary server's [Postgres port](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/install).

  2. Create a replication user:

###  Docker 
         
         docker exec CONTAINER_NAME psql -h localhost -U postgres -c "create user REPLICA_USER with replication password 'PASSWORD'"

Replace the following:

     * `REPLICA_USER`: the name of the replica user.
     * `PASSWORD`: the password for the replica user.
     * `CONTAINER_NAME`: the name that you assigned to the AlloyDB Omni container when you installed it.

###  Podman 
    
    podman exec CONTAINER_NAME psql -h localhost -U postgres -c "create user REPLICA_USER with replication password 'PASSWORD'"

Replace the following:

     * `REPLICA_USER`: the name of the replica user.
     * `PASSWORD`: the password for the replica user.
     * `CONTAINER_NAME`: the name that you assigned to the AlloyDB Omni container when you installed it.

  3. Add the following lines in the `/DATA_DIR/pg_hba.conf` file **before** `host all all all scram-sha-256` that exists in the file:
         
         host alloydbmetadata    alloydbmetadata   IP_RANGE trust
         host replication        REPLICA_USER    IP_RANGE scram-sha-256
         

Replace the following:

     * `IP_RANGE`: the IP range, in CIDR notation, of the subnet where your replica machine is located. For example, `203.0.113.0/24`.
     * `DATA_DIR`: the file system path you want this replica to use for its data directory.
  4. Restart your primary server:

###  Docker 
         
         docker restart CONTAINER_NAME

###  Podman 
         
         podman restart CONTAINER_NAME




## Create and configure the replica server

To create and configure an AlloyDB Omni replica server, complete the following steps:

  1. Ensure the replica has network connectivity to the primary server:
         
         ping SOURCE_IP

Replace `SOURCE_IP` with the IP address of the primary AlloyDB Omni instance to replicate from.

  2. Ensure the replica can connect to the primary server:

###  Docker 
         
         docker run -it --rm google/alloydbomni psql "host=SOURCE_IP user=REPLICA_USER replication=1" -c "IDENTIFY_SYSTEM;"

###  Podman 
         
         podman run -it --rm google/alloydbomni psql "host=SOURCE_IP user=REPLICA_USER replication=1" -c "IDENTIFY_SYSTEM;"

The output should look similar to the following:
         
         systemid       | timeline |  xlogpos  | dbname
          ---------------------+----------+-----------+--------
           7376500460465963036 |        1 | 0/454B670 |
           (1 row)
         

  3. The replica must have a persistent storage location on disk:

###  Docker 
         
         mkdir alloydb && docker run --rm -it \
            -e PGDATA=/var/lib/postgresql/data/pgdata \
            -v "$PWD/alloydb":/var/lib/postgresql/data \
            -p 5432:5432 \
            --user $(id -u):$(id -g) \
            google/alloydbomni \
            /usr/lib/postgresql/15/bin/pg_basebackup \
              --pgdata=/var/lib/postgresql/data/pgdata \
              --checkpoint=fast \
              --host="SOURCE_IP" \
              --port="SOURCE_PORT" \
              --username=REPLICA_USER \
              --create-slot \
              --write-recovery-conf \
              --slot="SLOT_NAME"

Replace the following:

     * `SOURCE_PORT`: the TCP port of the primary AlloyDB Omni instance to replicate from. If you don't provide this value, then AlloyDB Omni applies a default value of `5432`.
     * `SLOT_NAME`: the label for the name of the replication slot.

###  Podman 
    
    mkdir alloydb && podman run --rm -it \
       -e PGDATA=/var/lib/postgresql/data/pgdata \
       -v "$PWD/alloydb":/var/lib/postgresql/data \
       -p 5432:5432 \
       --user $(id -u):$(id -g) \
       google/alloydbomni \
       /usr/lib/postgresql/15/bin/pg_basebackup \
         --pgdata=/var/lib/postgresql/data/pgdata \
         --checkpoint=fast \
         --host="SOURCE_IP" \
         --port="SOURCE_PORT" \
         --username=REPLICA_USER \
         --create-slot \
         --write-recovery-conf \
         --slot="SLOT_NAME"

Replace the following:

     * `SOURCE_PORT`: the TCP port of the primary AlloyDB Omni instance to replicate from. If you don't provide this value, then AlloyDB Omni applies a default value of `5432`.
     * `SLOT_NAME`: the label for the name of the replication slot.

  4. Start your replica instance:

###  Docker 
         
         docker run --detach \
           --name pg-service \
           -e POSTGRES_PASSWORD=a \
           -e PGDATA=/var/lib/postgresql/data/pgdata \
           -v "$PWD/alloydb":/var/lib/postgresql/data \
           -v /dev/shm:/dev/shm \
           -p 5432:5432 \
           --user $(id -u):$(id -g) \
           google/alloydbomni

###  Podman 
         
         podman run --detach \
           --name pg-service \
           -e POSTGRES_PASSWORD=a \
           -e PGDATA=/var/lib/postgresql/data/pgdata \
           -v "$PWD/alloydb":/var/lib/postgresql/data \
           -v /dev/shm:/dev/shm \
           -p 5432:5432 \
           --user $(id -u):$(id -g) \
           google/alloydbomni




## Verify replication status on the primary server

To verify replication is configured properly, run the following command on the primary server's host:

###  Docker 
    
    
      docker exec -it CONTAINER_NAME psql -h localhost -U postgres -c "select * from pg_stat_replication"

###  Podman 
    
    
      podman exec -it CONTAINER_NAME psql -h localhost -U postgres -c "select * from pg_stat_replication"

The output table contains one row for every replica connected to your primary database server.

After you set up replication, all inserts, updates, and deletions to rows in your primary database server become readable on your replica within seconds.

## What's next

  * [Logical replication](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/about-pglogical)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
