---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/install-web-ui/
title: Install the web UI \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:52:11.112461+00:00
---

# Install the web UI  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/install-web-ui/

This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)



Send feedback 

#  Install the web UI Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/install-web-ui)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/install-web-ui)



This page shows how to install the AlloyDB Omni web user interface so that you can monitor the health and configuration of your self-managed database clusters. The web UI provides the following features:

Feature | Description | Containers (standalone) | Kubernetes | RPM (Linux) | RPM orchestrator  
---|---|---|---|---|---  
Cluster selection | A connectivity screen that lets you establish, register, and save connection credentials for access to target clusters. | Supported | Supported | Supported | Supported  
Cluster overview | Observation dashboard displaying all active cluster instances and telemetry graphs. | Supported | Supported | Supported | Supported  
Databases | Overview page displaying catalog tables and database sizes on the cluster. | Supported | Supported | Supported | Supported  
[Columnar engine](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/overview) | Configuration settings and scan execution statistics for analytical queries. | Supported | Supported | Supported | Supported  
Database flags | Observation board displaying active flags and configurations that deviate from default settings. | Supported | Supported | Supported | Supported  
Query insights | Telemetry and query performance dashboards displaying structural histograms and slow query lists. | Supported | Supported | Supported | Supported  
System insights | Telemetry charts displaying CPU consumption, memory footprints, and disk I/O. | Not supported (standalone container only) | Supported | Supported | Supported  
  
## Before you begin

Before you install the web UI, make sure that you do the following:

  1. Obtain the images for your deployment and download and install AlloyDB Omni so that you can use the web UI: [Install AlloyDB Omni using the container orchestrator](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes). 

  2. Configure the database user.

The web UI relies on a limited user account, which has the `pg_monitor` role for accessing the database. Configure this user on each cluster by running the following commands in a `psql` session:
         
         CREATE ROLE alloydbui WITH LOGIN PASSWORD 'PASSWORD';
         GRANT pg_monitor TO alloydbui WITH INHERIT TRUE;
         

**Note:** The `alloydbui` user requires specific permissions to populate certain sections in the user interface. For example, the `alloydbui` user needs at least one permission on tables to view data in the Columnar Store section, `SELECT` permission on tables for the Vector Columns section, and `SELECT` permission on `pg_stat_ann_indexes` for vector indexes. Consider your security requirements when you grant these permissions. 
  3. Configure Prometheus.

To view chart data on the **Overview** and **System Insights** pages, including CPU usage, install and configure Prometheus. The AlloyDB Omni Kubernetes operator automatically runs a monitoring agent that exports Prometheus-compatible metrics on port `9187`. However, to view time-series charts in the web UI, you must install and configure a Prometheus server to scrape those metrics. For more information about the metrics endpoint, see [View metrics using the Prometheus API](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/manage#view-api). For an example of configuring Prometheus to scrape port `9187`, see [Choose and install monitoring tools](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/choose-install-monitoring-tools#prometheus). 




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

To access columnar engine data in the web UI, configure the engine as described in [Columnar engine overview](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/overview).

**Note:** To view data in the **Columnar Queries** page in the web UI, you must install and configure the `pg_stat_statements` extension as described in the **Query insights setup** section.
  * AlloyDB AI setup

To use AlloyDB AI features in the web UI, grant the following permissions:

    * To populate vector indexes, grant the `alloydbui` user the `SELECT` permission on `pg_stat_ann_indexes`.
    * To display vector columns, grant the `alloydbui` user the `SELECT` permission on a table.

For more information, see [Build generative AI applications using AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview-ai). 

## Install the web UI

You can install and run the web UI on any node; the web UI doesn't require a dedicated node. The full installation requires approximately 250 MB of disk space. After you obtain the images for your deployment and download AlloyDB Omni, you can install and run the web UI.

### Install the web UI using a Kubernetes manifest

  1. To preserve connection details across pod restarts, create a `PersistentVolumeClaim` (PVC) manifest and apply it to your cluster:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: alloydb-omni-ui-pvc
         spec:
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               storage: 256Mi
         

  2. To deploy the web UI as a Pod, apply the following Kubernetes manifest.

**Note:** Use a strong passphrase for `ALLOYDB_OMNI_UI_KEYSTORE`. Decryption errors occur if you transfer your configuration files and connect with a mismatching keystore password.
         
         ---
         # This is a secret to protect web UI data on disk.
         # It is not used to connect to the DB.
         apiVersion: v1
         kind: Secret
         metadata:
           name: alloydb-omni-ui-secret
         type: Opaque
         data:
           ALLOYDB_OMNI_UI_KEYSTORE: BASE64-ENCODED-PASSWORD
         ---
         apiVersion: v1
         kind: Pod
         metadata:
           name: alloydb-omni-ui-pod
           labels:
             app: alloydb-omni-ui
         spec:
           containers:
           - name: alloydb-omni-ui
             image: ALLOYDB_OMNI_UI_IMAGE_TAG
         
             # --- Container Port ---
             ports:
             - containerPort: 9080
         
             # --- Environment Variables ---
             env:
             - name: ALLOYDB_OMNI_UI_KEYSTORE
               valueFrom:
                 secretKeyRef:
                   name: alloydb-omni-ui-secret
                   key: ALLOYDB_OMNI_UI_KEYSTORE
         
             # --- Resources ---
             resources:
               requests:
                 memory: "256Mi"
                 cpu: "500m"
               limits:
                 memory: "512Mi"
                 cpu: "1"
         
             # --- Optional Configurations ---
             # --- Volume Mounts ---
             volumeMounts:
             - name: ui-config-storage
               mountPath: /root/.config/alloydb-omni-ui
         
           # --- Optional Volumes Configuration ---
           volumes:
           - name: ui-config-storage
             persistentVolumeClaim:
               claimName: alloydb-omni-ui-pvc
         


**Note:** For container orchestrator deployments, you can also install the [RPM](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/install-web-ui) or [container](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install-web-ui) package outside the cluster based on your management environment.

## Start the web UI

The web UI uses a Java Keystore to protect the 256-bit AES key that is used to encrypt connection data. When you start the web UI, specify an environment variable containing the password.

**Note:** The web UI serves HTTP traffic on port `9080` by default and doesn't provide built-in TLS (HTTPS) termination. To secure traffic to the web UI using TLS (HTTPS), host the web UI behind a reverse proxy configured with your TLS certificates.

You can start the web UI by accessing the web UI deployed as a Pod, or you can connect an external web UI instance to your Kubernetes cluster using port forwarding.

### Access the web UI deployed as a Pod

If you deployed the web UI as a Kubernetes Pod using the manifest, enable port-forwarding to access the web UI locally:
    
    
    kubectl port-forward pod/alloydb-omni-ui-pod 9080:9080
    

### Forward cluster ports for an external web UI instance

If you run the web UI outside the Kubernetes cluster (for example, using [containers](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install-web-ui) or [RPM](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/install-web-ui)), enable port-forwarding to the pods where the database and Prometheus are running:
    
    
    kubectl port-forward --address 0.0.0.0 pod/DB_POD 5432:5432
    kubectl port-forward --address 0.0.0.0 pod/PROMETHEUS_POD 9090:9090
    

Make the following replacements:

  * `DB_POD`: the name of your database pod.
  * `PROMETHEUS_POD`: the name of your Prometheus pod.



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

## What's next

    * [Connect to the web UI](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/connect-web-ui).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
