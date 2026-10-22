---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install-web-ui/
title: Install the web UI \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:37.272386+00:00
---

# Install the web UI  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install-web-ui/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)



Send feedback 

#  Install the web UI Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/install-web-ui)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/install-web-ui)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install-web-ui)



This page shows how to install the AlloyDB Omni web user interface so that you can monitor the health and configuration of your self-managed database clusters. The web UI provides the following features:

Feature | Description | Containers (standalone) | Kubernetes | RPM (Linux) | RPM orchestrator  
---|---|---|---|---|---  
Cluster selection | A connectivity screen that lets you establish, register, and save connection credentials for access to target clusters. | Supported | Supported | Supported | Supported  
Cluster overview | Observation dashboard displaying all active cluster instances and telemetry graphs. | Supported | Supported | Supported | Supported  
Databases | Overview page displaying catalog tables and database sizes on the cluster. | Supported | Supported | Supported | Supported  
[Columnar engine](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/columnar-engine/overview) | Configuration settings and scan execution statistics for analytical queries. | Supported | Supported | Supported | Supported  
Database flags | Observation board displaying active flags and configurations that deviate from default settings. | Supported | Supported | Supported | Supported  
Query insights | Telemetry and query performance dashboards displaying structural histograms and slow query lists. | Supported | Supported | Supported | Supported  
System insights | Telemetry charts displaying CPU consumption, memory footprints, and disk I/O. | Not supported (standalone container only) | Supported | Supported | Supported  
  
## Before you begin

Before you install the web UI, make sure that you do the following:

  1. Obtain the images for your deployment and download and install AlloyDB Omni so that you can use the web UI: [Install AlloyDB Omni using RPM](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/deploy-vm). 

  2. Configure the database user.

The web UI relies on a limited user account, which has the `pg_monitor` role for accessing the database. Configure this user on each cluster by running the following commands in a `psql` session:
         
         CREATE ROLE alloydbui WITH LOGIN PASSWORD 'PASSWORD';
         GRANT pg_monitor TO alloydbui WITH INHERIT TRUE;
         

**Note:** The `alloydbui` user requires specific permissions to populate certain sections in the user interface. For example, the `alloydbui` user needs at least one permission on tables to view data in the Columnar Store section, `SELECT` permission on tables for the Vector Columns section, and `SELECT` permission on `pg_stat_ann_indexes` for vector indexes. Consider your security requirements when you grant these permissions. 
  3. Configure the AlloyDB Omni monitoring agent.

When you run AlloyDB Omni using RPM, the `alloydbomni_monitor` monitoring agent is available as a separate RPM package in the same repository. For more information, see [Install and start the AlloyDB Omni monitor](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/manage#install-monitor), [Configure the AlloyDB Omni monitor](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/manage#configure-monitor), and [Verify the AlloyDB Omni monitor](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/manage#verify-monitor).

If your installation uses a custom data directory (`PG_DATA_DIR`), configure `/etc/systemd/system/alloydbomni_monitor.service.d/override.conf` and restart the monitor service:
         
         sudo mkdir -p /etc/systemd/system/alloydbomni_monitor.service.d
         sudo tee /etc/systemd/system/alloydbomni_monitor.service.d/override.conf <<'EOF'
         [Service]
         Environment="PG_DATA_DIR=PG_DATA_DIR"
         EOF
         sudo systemctl daemon-reload
         sudo systemctl restart alloydbomni_monitor
         

Replace `PG_DATA_DIR` with the path to your database data directory—for example, `/var/lib/postgresql/18/data` or `/data`.

To verify that the monitoring agent is active and exporting metrics, run `sudo systemctl status alloydbomni_monitor` and `curl http://localhost:9187/metrics`.

**Note:** To make sure that the web UI displays maximum CPU and memory statistics (`alloydb_omni_memory_limit_byte`, `alloydb_omni_memory_available_byte`, and `alloydb_omni_node_cpu_mcpu`), configure `CPUQuota` and `MemoryMax` in a systemd override file for your AlloyDB Omni service. You can set the quota value to `100%` (no restriction) so that the monitoring agent exports maximum resource metrics. For more information, see [Monitor limitations](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/manage#monitor-limitations). To configure these limits, run the following commands:
         
         sudo mkdir -p /etc/systemd/system/alloydbomni18.service.d
         sudo tee /etc/systemd/system/alloydbomni18.service.d/override.conf <<'EOF'
         [Service]
         CPUQuota=100%
         MemoryMax=100%
         IOAccounting=yes
         EOF
         sudo systemctl daemon-reload
         sudo systemctl restart alloydbomni18
         

  4. Configure Prometheus.

To view chart data on the **Overview** and **System Insights** pages, including CPU usage, install and configure Prometheus. Follow the installation and configuration instructions in [Choose and install monitoring tools](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/choose-install-monitoring-tools#prometheus). 




### Optional steps

To enable additional web UI features:

  * Query insights setup

To use the query insights feature, enable the `pg_stat_statements` extension. In a `psql` session, run the following commands to configure the libraries:
        
        ALTER SYSTEM SET shared_preload_libraries=google_columnar_engine,google_job_scheduler,google_storage,google_db_advisor,pg_stat_statements;
        ALTER SYSTEM SET pg_stat_statements.max = 10000;
        ALTER SYSTEM SET pg_stat_statements.track_utility = on;
        ALTER SYSTEM SET track_io_timing = on;
        

Then, execute the following command in each database individually to create the extension:
        
        CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
        

Restart the database for these changes to take effect. If you plan to enable the columnar engine, wait to restart until that setup is complete.

  * Columnar engine setup

To access columnar engine data in the web UI, configure the engine as described in [Columnar engine overview](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/columnar-engine/overview).

**Note:** To view data in the **Columnar Queries** page in the web UI, you must install and configure the `pg_stat_statements` extension as described in the **Query insights setup** section.
  * AlloyDB AI setup

To use AlloyDB AI features in the web UI, grant the following permissions:

    * To populate vector indexes, grant the `alloydbui` user the `SELECT` permission on `pg_stat_ann_indexes`.
    * To display vector columns, grant the `alloydbui` user the `SELECT` permission on a table.

For more information, see [Build generative AI applications using AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview-ai). 

## Install the web UI

You can install and run the web UI on any node; the web UI doesn't require a dedicated node. The full installation requires approximately 250 MB of disk space. After you obtain the images for your deployment and download AlloyDB Omni, you can install and run the web UI.

### Install using RPM

Google signs the AlloyDB Omni RPM packages with the Linux package signing key. To configure the YUM repository with GPG signature verification and install the web UI RPM package, complete the following steps:

  1. Configure the YUM repository in your local directory:
         
         sudo tee -a /etc/yum.repos.d/alloydbomni_ui.repo << EOF
         [alloydbomni_ui]
         name=alloydbomni_ui
         baseurl=ALLOYDB_OMNI_COMMON_REPOSITORY_URL
         enabled=1
         repo_gpgcheck=1
         gpgcheck=1
         gpgkey=https://dl.google.com/linux/linux_signing_key.pub
         EOF
         
         
         sudo yum makecache
         

Replace `ALLOYDB_OMNI_COMMON_REPOSITORY_URL` with the URL of the AlloyDB Omni common repository.

**Note:** If you already configured the AlloyDB Omni common repository on this host (for example, to install the `alloydbomni_monitor` package), this step is optional.
  2. Install the web UI RPM package:
         
         sudo dnf install alloydbomni_ui
         




## Start the web UI

The web UI uses a Java Keystore to protect the 256-bit AES key that is used to encrypt connection data. When you start the web UI, specify an environment variable containing the password.

**Note:** The web UI serves HTTP traffic on port `9080` by default and doesn't provide built-in TLS (HTTPS) termination. To secure traffic to the web UI using TLS (HTTPS), host the web UI behind a reverse proxy configured with your TLS certificates.

### Start the web UI on Linux
    
    
    export ALLOYDB_OMNI_UI_KEYSTORE="PASSWORD"
    /opt/alloydbomni/app/alloydb-ui/app/bin/alloydb
    

## Open the web UI

To view the web UI, open a browser at `http://HOST:9080`.

Replace `HOST` with the hostname or IP address of the node where the web UI is installed.

  * If you configured a custom base path using the optional `ALLOYDB_OMNI_BASE_PATH` environment variable (for example, when hosting behind an existing reverse proxy), then you must append the path to the URL: `http://HOST:9080/BASE_PATH`.
  * You can configure the base path without a leading slash—for example, `ALLOYDB_OMNI_BASE_PATH=PATH`. All of the following are valid alternatives:

    * `/test/`
    * `test/`
    * `test`
    * `/test`



## Limitations

The web UI has the following limitations:

  * Overview charts and system insights aren't available when connecting to AlloyDB Omni standalone container deployments because a containerized monitoring agent isn't available for standalone container deployments. All other non-chart features and metrics remain fully functional.

  * To view columnar engine data for a given table, the `alloydbui` user needs at least one permission on that table, for example, `SELECT`.

  * To view vector index data, the `alloydbui` user needs the `SELECT` permission on `pg_stat_ann_indexes`.

  * To view vector column data for a given table, the `alloydbui` user needs the `SELECT` permission on that table.




## Best practices and caveats

Follow these best practices and caveats when you install and configure the web UI:

  * **Keystore password protection** : The web UI generates a Java Keystore to protect the 256-bit AES database encryption key. Use a strong passphrase for `ALLOYDB_OMNI_UI_KEYSTORE`. Decryption errors occur if you transfer your configuration files and connect with a mismatching keystore password.
  * **Prometheus metrics scraping** : Configure the scrapers to poll target instances at standard ranges (15s to 30s) to query statistics without overloading database nodes. 

**Note:** In RPM VM installations, connection files are saved to the active system user's home directory (`~/.config/`). Configure file permissions on this directory to prevent other system accounts from reading credentials. 

## What's next

  * [Connect to the web UI](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/connect-web-ui).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
