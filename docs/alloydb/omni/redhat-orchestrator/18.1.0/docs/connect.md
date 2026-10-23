---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/connect/
title: Connect to AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:53:54.763191+00:00
---

# Connect to AlloyDB Omni  |  AlloyDB Omni using the RPM orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/connect/

This page documents AlloyDB Omni version **18.1.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview)



Send feedback 

#  Connect to AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/connect)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/connect)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/connect)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/connect)

This page describes how to connect to AlloyDB Omni after you deploy it using the RPM orchestrator. 

Any client application that works with PostgreSQL can also work with AlloyDB Omni, with no modification needed.

To connect to your database cluster, use any PostgreSQL-compatible client, such as `psql`, that's installed on a client machine.

## Before you begin

  * [Install AlloyDB Omni using the RPM orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).
  * [Create an AlloyDB Omni cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster).
  * Make sure that you have the following connection information:

    * Host: the IP address of the database node. You can find the IP addresses of your nodes by [getting the cluster status](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/cluster-status). If the HA is enabled for your cluster, follow the steps in [Verify read-only endpoints](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/manage-high-availability#verify-read-only-standby-endpoints) to find the IP addresses of your endpoints.
    * Port: `5432`
    * Username: `postgres` or the administrative user you configured.
    * Password: the password for the administrative user that you configured when creating the cluster.



## Connect to a database node using psql

To connect to your database node, run the `psql` command from a client machine that has network access to the database node.

  1. Run the following command:
         
         psql -h NODE_IP_ADDRESS -p 5432 -U postgres

Replace `NODE_IP_ADDRESS` with the IP address of the database node.

  2. When you're prompted, enter the password for the `postgres` user.




## Connect through a connection pooler

If you configured PgBouncer, you can connect to the cluster through the connection pooler. For more information, see [Verify the connection pooler](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/use-pgbouncer-connection-pooler#verify-connection-pooler).

## Connect using your own applications

Any client application that works with PostgreSQL can also work with AlloyDB Omni, with no modification needed.

Use any PostgreSQL-compatible client or code library to connect to AlloyDB Omni.

After you connect to the database server, you can define, query, and modify your databases by sending DML and SQL queries through standard PostgreSQL communication protocols.

Because AlloyDB Omni runs in your own environment, you can control how you connect to AlloyDB Omni. You can allow or restrict network access to AlloyDB Omni according to the needs of your application, just as you would with an ordinary PostgreSQL server.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
