---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/database/
title: Manage databases \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:42:30.444633+00:00
---

# Manage databases  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Manage databases Stay organized with collections  Save and categorize content based on your preferences. 

GDC Sandbox provides the Database Service to test and manage database clusters.

## Create Database

To create and manage a database cluster, see [Create and Manage database cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/application/ao-user/db-create-cluster#create).

### Available Database Engines

GDC Sandbox supports PostgreSQL and AlloyDB Omni database engines.

List available database engines and their supported versions:
    
    
    gdcloud database engine list
    

For more information, see [`gdcloud database engine list`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/resources/gdcloud-reference/gdcloud-database-engine-list).

Use either the GDC console or the Distributed Cloud CLI to create database clusters:

###  Console 

  1. From the main menu, choose **Database Service**.
  2. Click **Create Database Cluster**.
  3. In the **Choose a database engine** dialog, choose a database engine.

  4. In the **Configure your cluster** dialog, specify the cluster ID, password, and database version. You can enable backups and configure the backup retention period.

  5. In the **Configure your primary instance** dialog, specify the CPU, memory, and storage capacity of the primary instance of the database cluster. We recommend you choose enough memory to hold your largest table.

  6. Click **Create**. Creating the database cluster can take a few minutes. Check the status of the cluster from the **Cluster overview** page. The status changes from _Creating_ to _Ready_ when the cluster is ready.




###  gdcloud 

  1. Before using Distributed Cloud CLI, [install and initialize](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/resources/gdcloud-install) it. Then, [authenticate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/resources/gdcloud-auth) with your organization.

  2. Run the following command to create a database cluster:
         
         gdcloud database clusters create CLUSTER_NAME \
             --database-version DB_VERSION \
             --admin-password ADMIN_PASSWORD
         

Replace the following variables:

     * `CLUSTER_NAME` with the name for the new cluster.
     * `DB_VERSION` with the version string for the new cluster (for example, `POSTGRESQL_15` or `ALLOYDBOMNI_15`). To see all available versions, run `gdcloud database engine list`.
     * `ADMIN_PASSWORD` with the administrator password for the new cluster.
  3. For more information on configuring the CPU, memory, and storage resources for the database cluster, configuring backup, enabling high availability, and for other available options, run:
         
         gdcloud database clusters create --help
         




###  API 

  1. Create a file `db-cluster-create.yaml` with contents
         
         apiVersion: v1
         kind: Secret
         metadata:
           name: db-pw-DBCLUSTER_NAME
           namespace: USER_PROJECT
         type: Opaque
         data:
           DBCLUSTER_NAME: "BASE64_PASSWORD"
         ---
         apiVersion: DBENGINE_NAME.dbadmin.gdc.goog/v1
         kind: DBCluster
         metadata:
           name: DBCLUSTER_NAME
           namespace: USER_PROJECT
         spec:
           primarySpec:
             adminUser:
               passwordRef:
                 name: db-pw-DBCLUSTER_NAME
             version: "DB_VERSION"
             resources:
               memory: DB_MEMORY
               cpu: DB_CPU
               disks:
               - name: DataDisk
                 size: DB_DATA_DISK
         

Replace the following variables:

     * `DBCLUSTER_NAME`, the name of the database cluster.
     * `USER_PROJECT`, the name of the user project where the database cluster will be created.
     * `BASE64_PASSWORD`, the base64 encoding of the database's administrator password.
     * `DBENGINE_NAME`, the name of the database engine. This is one of `alloydbomni`, or `postgresql`.
     * `DB_VERSION`, the version of the database engine. To view available versions, run `gdcloud database engine list`.
     * `DB_MEMORY`, the amount of memory allocated to the DB Cluster, for example `5Gi`.
     * `DB_CPU`, the amount of CPUs allocated to the DB Cluster, for example `2`.
     * `DB_DATA_DISK`, amount of space allocated to the DB Cluster, for example `10 Gi`.
  2. kubectl --kubeconfig MANAGEMENT_API apply -f db-cluster-create.yaml
         




## Connect to the Database

By default, a database cluster only allows connection from within the user cluster and the same project.

To enable connections to all database clusters in your project from another project, see [Enable cross-project connections](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/application/ao-user/db-cross-project-connect).

To connect to the database from IP addresses outside your GDC Sandbox organization, follow the instructions at [Connect to a database cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/application/ao-user/db-connect-cluster) to enable the external connections.

You can use `sshuttle` to connect to your database with a local database client like `psql`:

  1. Navigate to the **Connectivity** section of the **Database Service** page for the database cluster. This page includes:

     * The password of the administrator account (the username is `dbsadmin`)
     * Hostname and port number of the database cluster's primary endpoint
     * A `psql` command for connecting to the cluster (for PostgreSQL and AlloyDB Omni database clusters)
     * A link to download the certificate authority (CA) certificate of the database cluster
  2. Download the CA certificate from the GDC console in the **Connectivity** section of the **Database Service** page for your database cluster.

  3. Configure your client to use the CA certificate to verify the database. For `psql` clients, set the `PGSSLROOTCERT` env variable to the path of the certificate file and the `PGSSLMODE` env variable to your preference:
         
         export PGSSLROOTCERT=path/to/accounts_cert.pem
             export PGSSLMODE="verify-full"
         

  4. Initiate a secure tunnel. If you have a running instance of `sshuttle` as described in [Connect to your instance](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/connect), terminate that process.
         
         sshuttle -r zone1-org-1-data@GDC_SANDBOX_INSTANCE_NAME --no-latency-control \
             --ssh-cmd 'gcloud compute ssh --project PROJECT_NAME --zone ZONE --tunnel-through-iap' \
             10.200.0.0/16 --dns
         

Replace the following with the values provided to you by the GDC Sandbox team:

     * `GDC_SANDBOX_INSTANCE_NAME`: the name of your GDC Sandbox instance.
     * `PROJECT_NAME`: the project containing your GDC Sandbox environment.
     * `ZONE`: the zone containing your GDC Sandbox environment.
  5. While the tunnel is active, run the command using `psql` in a different terminal
         
         PGPASSWORD=DB_PASSWORD psql -h DB_HOSTNAME -p PORT -U USERNAME -d postgres
         

Replace the following variables:

     * `DB_PASSWORD`: the password from the console UI.
     * `DB_HOSTNAME`: the database hostname from the console.
     * `DB_PORT`: the database port number from the console.
     * `DB_USERNAME`: the database username from the console.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
