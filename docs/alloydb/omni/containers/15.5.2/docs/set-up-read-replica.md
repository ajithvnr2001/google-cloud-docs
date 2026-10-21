---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/set-up-read-replica/
title: Create a read-only replica \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:49:08.783561+00:00
---

# Create a read-only replica  |  AlloyDB Omni for containers: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/set-up-read-replica/

This page documents AlloyDB Omni version **15.5.2** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



Send feedback 

#  Create a read-only replica Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/set-up-read-replica)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/set-up-read-replica)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/set-up-read-replica)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/set-up-read-replica)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/set-up-read-replica)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/set-up-read-replica)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/set-up-read-replica)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/set-up-read-replica)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/set-up-read-replica)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/set-up-read-replica)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/set-up-read-replica)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/set-up-read-replica)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/set-up-read-replica)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/set-up-read-replica)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/set-up-read-replica)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/set-up-read-replica)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/set-up-read-replica)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/set-up-read-replica)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/set-up-read-replica)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/set-up-read-replica)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/set-up-read-replica)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/set-up-read-replica)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/set-up-read-replica)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/set-up-read-replica)

To increase read throughput and availability, you can create an AlloyDB Omni replica server for an existing AlloyDB Omni server. A replica server provides a read-only clone of your primary database server. It continuously updates its own data to reflect changes to your primary server's data. 

The following sections provide steps to configure your AlloyDB Omni primary server for replication, configure the replica server, and verify replication status on the primary server.

The information on this page applies only to AlloyDB Omni for containers. It does not apply to AlloyDB Omni for Kubernetes.

## Configure your primary server for replication

  1. Update the network or firewall settings of your primary server's host so that it allows ingress traffic from the replica server's host through TCP port `5432`.

  2. Add the following lines in the `/var/alloydb/config/pg_hba.conf` file:
         
         host all                alloydbreplica     IP_RANGE trust
         host replication        alloydbreplica     IP_RANGE trust
         host alloydbmetadata    alloydbmetadata    IP_RANGE trust
         

Replace IP_RANGE with the IP range, in CIDR notation, of the subnet where your replica machine is located. For example, `203.0.113.0/24`.

  3. Restart your primary server:
         
         sudo alloydb database-server stop
         sudo alloydb database-server start




## Create and configure the replica server

To create and configure an AlloyDB Omni replica server, complete the following steps:

  1. [Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install) onto the system you want to host the replica.

When you run the `alloydb database-server install` command, include the flags that are specific to creating a replica:
         
         sudo alloydb database-server install \
           --data-dir=DATA_DIR \
           --pg-port=PORT \
           --replica-source-ip=SOURCE_IP \
           --replica-source-port=SOURCE_PORT

Replace the following:

     * `DATA_DIR`: the file system path you want this replica to use for its data directory.

     * `PORT`: the TCP port that you want AlloyDB Omni to accept connections on. If you don't provide this value, then AlloyDB Omni applies a default value of `5432`.

     * `SOURCE_IP`: the IP address of the primary AlloyDB Omni instance to replicate from.

     * `SOURCE_PORT`: the TCP port of the primary AlloyDB Omni instance to replicate from. If you don't provide this value, then AlloyDB Omni applies a default value of `5432`.

  2. Ensure the replica has network connectivity to the primary server:
         
         ping SOURCE_IP

  3. Start your replica:
         
         sudo alloydb database-server start




## Verify replication status on the primary server

To verify replication is configured properly, run the following command on the primary server's host:
    
    
      docker exec -it pg-service psql -h localhost -U alloydbadmin -c "select * from pg_stat_replication"

The output table contains one row for every replica connected to your primary database server.

After you set up replication, all inserts, updates, and deletions to rows in your primary database server become readable on your replica within seconds.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
