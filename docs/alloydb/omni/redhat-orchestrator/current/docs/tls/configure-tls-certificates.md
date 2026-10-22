---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/tls/configure-tls-certificates/
title: Configure TLS certificates \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:45.270076+00:00
---

# Configure TLS certificates  |  AlloyDB Omni using the RPM orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/tls/configure-tls-certificates/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview)



Send feedback 

#  Configure TLS certificates Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/tls/configure-tls-certificates)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/tls/configure-tls-certificates)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/tls/configure-tls-certificates)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/tls/configure-tls-certificates)

To create your AlloyDB Omni cluster, you must first configure Transport Layer Security (TLS) communications. 

You only need to configure TLS certificate and key files if you want to use your own files, or if you aren't using Ansible. Ansible can generate self-signed certificates during the installation phase.

For more information about how AlloyDB Omni uses TLS, see the [TLS overview](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/tls/overview).

## Before you begin

Before you configure your TLS certificates, complete the following requirements:

  * To provide your own private, root key; root certificate; and signed server certificate for TLS communications, generate them now. If you don't want to provide these, Ansible can generate self-signed certificates for you during installation.

  * Choose the name for your AlloyDB Omni database cluster (DBCLUSTER_NAME)—for example, `my-db-cluster`.




## Configure SSL certificates for the control path

Configuring SSL certificates for AlloyDB Omni's control path establishes a Zero Trust Architecture (ZTA) between its components.

For more information, see the [TLS overview](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/tls/overview#tls-architecture).

To configure SSL certificates for the control path, follow the instructions for one of the following options, depending on your environment:

  * Ansible
  * AlloyDB Omni orchestrator CLI



### Ansible

Ansible uses playbooks to automatically manage and deploy the required SSL certificate and key files.

After Ansible playbooks are configured, they run during the install phase when you [create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/bootstrap-cluster). The playbooks copy the provided certificate and key files to each AlloyDB Omni node.

If you configure an Ansible-based SSL configuration and you don't provide certificate and key files, Ansible generates its own self-signed certificates.

To configure an Ansible-based SSL configuration, create an Ansible playbook (`inventory.yaml`) using the following format:
    
    
    alloydbomni:
      vars:
        cluster_manager:
          name: DBCLUSTER_NAME
          ssl:
            enable: true
            key_file: "SERVER_CERTIFICATE_PATH"
            cert_file: "SERVER_KEY_PATH"
            ca_file: "ROOT_CERTIFICATE_PATH"
        etcd:
          setup: true
          ssl:
            enable: true
            key_file: "SERVER_CERTIFICATE_PATH"
            cert_file: "SERVER_KEY_PATH"
            ca_file: "ROOT_CERTIFICATE_PATH"
    

Replace the following variables:

  * `DBCLUSTER_NAME`: the name of your AlloyDB Omni database cluster—for example, `my-db-cluster`.
  * `SERVER_CERTIFICATE_PATH`: the path for your signed server certificate—for example, `server.crt`.
  * `SERVER_KEY_PATH`: the path for your private server key—for example, `server.key`.
  * `ROOT_CERTIFICATE_PATH`: the path for your self-signed root certificate—for example, `root.crt`.



### AlloyDB Omni orchestrator CLI

To use the AlloyDB Omni orchestrator CLI, you must manually manage and deploy the following certificate and key files to fixed locations with fixed filenames on each database cluster node:

  * Signed server certificate
  * Private server key
  * Root certificate



The signed server and root certificates must have all virtual IPs, node IPs, and the hostname defined in the Subject Alternative Name (SAN).

**Note:** If you don't provide these certificate and key files, Ansible generates self-signed certificates during installation.Cluster node | Target path | Source path  
---|---|---  
Control | `/etc/alloydbomni/orchestrator/ssl/DBCLUSTER_NAME/cluster-manager-tls.crt` | `SERVER_CERTIFICATE_PATH`  
Control | `/etc/alloydbomni/orchestrator/ssl/DBCLUSTER_NAME/cluster-manager-tls.key` | `SERVER_KEY_PATH`  
Control | `/etc/alloydbomni/orchestrator/ssl/DBCLUSTER_NAME/cluster-manager-ca.crt` | `ROOT_CERTIFICATE_PATH`  
Cluster manager | `/etc/alloydbomni/cluster_manager/ssl/server-tls.crt` | `SERVER_CERTIFICATE_PATH`  
Cluster manager | `/etc/alloydbomni/cluster_manager/ssl/server-tls.key` | `SERVER_KEY_PATH`  
Cluster manager | `/etc/alloydbomni/cluster_manager/ssl/server-ca.crt` | `ROOT_CERTIFICATE_PATH`  
Cluster manager | `/etc/alloydbomni/cluster_manager/ssl/etcd-tls.crt` | `SERVER_CERTIFICATE_PATH`  
Cluster manager | `/etc/alloydbomni/cluster_manager/ssl/etcd-tls.key` | `SERVER_KEY_PATH`  
Cluster manager | `/etc/alloydbomni/cluster_manager/ssl/etcd-ca.crt` | `ROOT_CERTIFICATE_PATH`  
Cluster manager | `/etc/alloydbomni/cluster_manager/ssl/node-manager-tls.crt` | `SERVER_CERTIFICATE_PATH`  
Cluster manager | `/etc/alloydbomni/cluster_manager/ssl/node-manager-tls.key` | `SERVER_KEY_PATH`  
Cluster manager | `/etc/alloydbomni/cluster_manager/ssl/node-manager-ca.crt` | `ROOT_CERTIFICATE_PATH`  
Node manager | `/etc/alloydbomni/node_manager/ssl/server-tls.crt` | `SERVER_CERTIFICATE_PATH`  
Node manager | `/etc/alloydbomni/node_manager/ssl/server-tls.key` | `SERVER_KEY_PATH`  
Node manager | `/etc/alloydbomni/node_manager/ssl/server-ca.crt` | `ROOT_CERTIFICATE_PATH`  
`etcd` manager | `/var/lib/etcd/ssl/etcd.crt` | `SERVER_CERTIFICATE_PATH`  
`etcd` manager | `/var/lib/etcd/ssl/etcd.key` | `SERVER_KEY_PATH`  
`etcd` manager | `/var/lib/etcd/ssl/rootca.crt` | `ROOT_CERTIFICATE_PATH`  
  
Replace the following variables:

  * `DBCLUSTER_NAME`: the name of your AlloyDB Omni database cluster—for example, `my-db-cluster`.
  * `SERVER_CERTIFICATE_PATH`: the path for your signed server certificate—for example, `server.crt`.
  * `SERVER_KEY_PATH`: the path for your private server key—for example, `server.key`.
  * `ROOT_CERTIFICATE_PATH`: the path for your self-signed root certificate—for example, `root.crt`.



## Configure SSL certificates for the data path

Configuring SSL certificates for AlloyDB Omni's data path requires the following certificate and key files:

  * Signed server certificate.
  * Private server key.
  * Root certificate, which provides mutual TLS (mTLS) support.



The signed server and root certificates must have all virtual IPs, node IPs, and the hostname defined in the Subject Alternative Name (SAN).

For the list of components on the data path, see the [TLS overview](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/tls/overview#tls-architecture).

To configure SSL certificates for the data path, follow these high-level steps:

  1. Configure SSL certificates for the database cluster.
  2. Configure SSL certificates for PgBouncer.



If you don't complete these high-level steps, then AlloyDB Omni automatically configures its own self-signed, SSL certificates before installation.

### Database cluster

To configure SSL certificates for the database cluster, follow these steps:

  1. Create a YAML secret file that contains the base64-encoded certificate and key files described in Configure SSL certificates for data path.
         
         Secret:
           metadata:
             name: DBCLUSTER_SECRET_NAME
           spec:
             type: Opaque
             data:
               tls.crt: BASE64_SERVER_CERTIFICATE
               tls.key: BASE64_SERVER_KEY
               ca.crt:  BASE64_ROOT_CERTIFICATE
         

Replace the following variables:

     * `DBCLUSTER_SECRET_NAME`: name for your database cluster secret file—for example, `my-db-cluster-secret`.
     * `BASE64_SERVER_CERTIFICATE`: base64-encoded string of your signed server certificate—for example, you can get this encoded string by running the following command:
           
           cat SERVER_CERTIFICATE_PATH | base64

     * `BASE64_SERVER_KEY`: base64-encoded string of your private server key.

     * `BASE64_ROOT_CERTIFICATE`: base64-encoded string of your self-signed root certificate.

  2. Add a reference to the newly created secret in your `DBCluster` specification.
         
         DBCluster:
           metadata:
             name: DBCLUSTER_NAME
           spec:
             databaseVersion: 18.4.0
             mode: ""
             primarySpec:
               port: PG_PORT
               adminUser:
                 passwordRef:
                   name: db-pw-DBCLUSTER_NAME
             tls:
               certSecret:
                 name: "DBCLUSTER_SECRET_NAME"
         

Replace the following variables:

     * `DBCLUSTER_NAME`: name of your AlloyDB Omni database cluster—for example, `my-db-cluster`.
     * `PG_PORT`: port number that hosts PostgreSQL—for example, `5432`.
     * `DBCLUSTER_SECRET_NAME`: name for your database cluster secret resource—for example, `my-db-cluster-secret`.



### PgBouncer

To configure SSL certificates for PgBouncer, follow these steps:

  1. Create a YAML secret file that contains the base64-encoded certificate and key files described in Configure SSL certificates for data path.
         
         Secret:
           metadata:
             name: PGBOUNCER_SECRET_NAME
           spec:
             type: Opaque
             data:
               tls.crt: BASE64_SERVER_CERTIFICATE
               tls.key: BASE64_SERVER_KEY
               ca.crt:  BASE64_ROOT_CERTIFICATE
         

Replace the following variables:

     * `PGBOUNCER_SECRET_NAME`: name for your PgBouncer secret file—for example, `db-tls-secret`.
     * `BASE64_SERVER_CERTIFICATE`: base64-encoded string of your signed server certificate—for example, you can get this encoded string by running the following command:
           
           cat SERVER_CERTIFICATE_PATH | base64

     * `BASE64_SERVER_KEY`: base64-encoded string of your server key.

     * `BASE64_ROOT_CERTIFICATE`: base64-encoded string of your self-signed root certificate. The root certificate must match the root certificate that signed the database cluster's leaf certificate. The leaf certificate must contain the Common Name (CN) `alloydbpgbouncer`.

  2. Add a reference to the secret that you created in your `PgBouncer` specification.
         
         PgBouncer:
           metadata:
             name: PGBOUNCER_NAME
           spec:
             dbClusterRef: DBCLUSTER_NAME
             serverTLS:
               certSecret:
                 name: "PGBOUNCER_SECRET_NAME"
         

Replace the following variables:

     * `PGBOUNCER_NAME`: name for this PgBouncer specification file. For example, `my-pgbouncer-spec`.
     * `DBCLUSTER_NAME`: name of your AlloyDB Omni database cluster—for example, `my-db-cluster`.
     * `PGBOUNCER_SECRET_NAME`: name for your newly-created PgBouncer secret resource—for example, `db-tls-secret`.



## What's next

  * [Create an AlloyDB Omni cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/create-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
