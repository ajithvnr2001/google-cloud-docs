---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/connect-web-ui/
title: Connect to the web UI \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:38.335135+00:00
---

# Connect to the web UI  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/connect-web-ui/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Connect to the web UI Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/connect-web-ui)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/connect-web-ui)



This page describes how to connect to the AlloyDB Omni web user interface so that you can monitor your database clusters.

Before you begin, make sure that you do the following:

  * [Install the web UI](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-web-ui).
  * Have the `alloydbui` database user password configured on your database instance. For more information, see [Configure the database user](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-web-ui#database-user-config).
  * Have your database cluster and Prometheus endpoints ready.



## Configure a database connection

The web UI provides a **Cluster Selection** view that lets you add and configure multiple AlloyDB Omni database instances.

To configure a new database connection:

  1. Open the web UI at `http://HOST:9080` (or your configured custom base path).
  2. Click **Add Cluster Connection**.
  3. Enter the connection settings according to the following parameter reference:

Setting | Description  
---|---  
Cluster name | A human-readable display label to identify your target database instance in the UI.  
Cluster hostname (or IP address) | The location where the AlloyDB Omni cluster runs. For high availability (HA) setups, specify the proxy host; otherwise, specify the primary instance host. Note: The hostname or IP must be accessible to the web UI container, not the machine from which you access the web UI.  
Cluster port | The port the database listens on for connections. Defaults to `5432`.  
`alloydbui` password | The password created for the `alloydbui` user, as described in [Configure the database user](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-web-ui#database-user-config).  
Prometheus hostname (or IP address) | The location where Prometheus runs. This must be an address accessible to the web UI, which is not necessarily the user's workstation.  
Prometheus port | The port that the Prometheus service listens on for connections. Defaults to `9090`.  
  
### Troubleshoot database authentication and permissions

If the web UI fails to connect or display cluster data, you can use the `psql` client to verify that the `alloydbui` monitoring role can authenticate and query the database.

**Note:** Running `psql` inside the database container or pod using `docker exec`, `podman exec`, or `kubectl exec` verifies the `alloydbui` credentials and permissions. To also verify network reachability to the database from the web UI, run `psql` directly from the host or container environment where the web UI is installed.

To verify `alloydbui` authentication using the `psql` client to the cluster endpoint, run the following command:
    
    
    psql -h DB_HOST -p 5432 -U alloydbui -d postgres
    

Replace `DB_HOST` with the hostname or IP address of your cluster proxy or primary instance—for example, `localhost`, an IP address, or a DNS hostname.

## Select an existing connection

After you configure a cluster connection, subsequent UI sessions let you select the saved connection details without re-entering the configuration.

## Manage connection data

This section explains how the web UI stores, deletes, and transfers connection data.

### Storage of connection data

The web UI stores connection data in the `.config/alloydb-omni-ui` directory of the user account that starts the web UI. The web UI encrypts connection data with a 256-bit AES key. The password that you specify in the `ALLOYDB_OMNI_UI_KEYSTORE` environment variable when starting the application protects the key.

### Deletion of connection data

Delete connection data by removing the `.dat` files in the `.config/alloydb-omni-ui` directory.

### Portability of connection data

You can copy connection data files from the `.config/alloydb-omni-ui` directory to another device running the web UI. You must start the application with the same value for the `ALLOYDB_OMNI_UI_KEYSTORE` environment variable.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
