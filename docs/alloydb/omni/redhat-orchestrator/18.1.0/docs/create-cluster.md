---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster/
title: Create a cluster \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:39:10.906269+00:00
---

# Create a cluster  |  AlloyDB Omni using the RPM orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster/

This page documents AlloyDB Omni version **18.1.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview)



Send feedback 

#  Create a cluster Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/create-cluster)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/create-cluster)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/create-cluster)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster)

Create a database cluster to start using AlloyDB Omni. 

## Limitations

The following limitations apply:

  * AlloyDB Omni runs on port `5432`. Configuring a custom port is not supported.

  * Ensure that all database parameter configurations are correct before creating your cluster. Once your cluster is created, you cannot modify any database parameters.




## Before you begin

Before you create your cluster, complete the following:

  * [Install the AlloyDB Omni orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-orchestrator)

  * [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components)

  * [Configure TLS certificates](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/tls/configure-tls-certificates)

  * Mount an external volume (`DataDisk`) to PG_DATA_DIR on all database nodes provisioned within the orchestrator.

  * If you plan to use `alloydbctl` instead of Ansible, ensure that the required `policycoreutils-python-utils` package is installed on all of your VMs. To install this package, run the following command:
        
        sudo dnf install policycoreutils-python-utils

  * If you're using the Google Cloud environment, then set `ENVIRONMENT_TYPE` to `gcp`. Then you must authenticate your gcloud CLI account by running `gcloud auth login` as the `root` user. Additionally, the authenticated account must have the following permissions:

    * `compute.instances.get`
    * `compute.instances.list`
    * `compute.instances.updateNetworkInterface`



## Prepare cluster specifications

To create your cluster, AlloyDB Omni must know how to configure it. To create the necessary specifications, create a YAML file using the [`DBCluster`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/reference/dbcluster-spec) format:
    
    
    Secret:
      metadata:
        name: db-pw-DBCLUSTER_NAME
      spec:
        type: Opaque
        data:
          DBCLUSTER_NAME: BASE64_PASSWORD
    ---
    DBCluster:
      metadata:
        name: DBCLUSTER_NAME
      spec:
        databaseVersion: 18.1.0
        mode: ""
        availability:
          numberOfStandbys: NUM_STANDBY_NODES
          enableAutoFailover: true
          enableAutoHeal: true
          autoFailoverTriggerThreshold: AUTOFAILOVER_TRIGGER_THRESHOLD
          autoHealTriggerThreshold: AUTOHEAL_TRIGGER_THRESHOLD
          healthcheckPeriodSeconds: HEALTHCHECK_PERIOD
          replayReplicationSlotsOnStandbys: false
        primarySpec:
          adminUser:
            passwordRef:
              name: db-pw-DBCLUSTER_NAME
          resources:
            cpu: CPU_LIMIT
            memory: MEMORY_LIMIT
            disks:
            - name: DataDisk
              path: PG_DATA_DIR
          parameters:
            max_connections: "MAX_CONNECTIONS"
            max_wal_size: "MAX_WAL_SIZE"
            max_worker_processes: "MAX_WORKER_PROCESSES"
            log_connections: "LOG_CONNECTIONS"
            log_disconnections: "LOG_DISCONNECTS"
            log_hostname: "LOG_HOSTNAME"
            log_statement: "LOG_STATEMENT"
            huge_pages: "HUGE_PAGES"
            tcp_keepalives_idle: "TCP_KEEPALIVES_IDLE"
            tcp_keepalives_interval: "TCP_KEEPALIVES_INTERVAL"
            tcp_keepalives_count: "TCP_KEEPALIVES_COUNT"
          dbLoadBalancerOptions:
            DB_LOAD_BALANCER_TYPE:
              loadBalancerIP: "VIRTUAL_IP"
              loadBalancerType: "internal"
              loadBalancerInterface: "VIRTUAL_IP_INTERFACE"
    

Replace the following variables:

  * `DBCLUSTER_NAME`: name of your database cluster. For example, `my-dbcluster`.

  * `BASE64_PASSWORD`: base64-encoded password used for the `postgres` administrator user.

  * `NUM_STANDBY_NODES`: number of standby nodes in your cluster. For example, `2`.

  * (Optional) `AUTOFAILOVER_TRIGGER_THRESHOLD`: number of times the health check can fail before a failover occurs. The default value is `3`. The minimum value is `0`, but if the value is set to `0`, AlloyDB Omni uses the default value.

An automatic failover occurs if the health check fails `AUTOFAILOVER_TRIGGER_THRESHOLD` times or if the cumulative duration of the health check reaches `HEALTHCHECK_PERIOD * AUTOFAILOVER_TRIGGER_THRESHOLD` seconds.

  * (Optional) `AUTOHEAL_TRIGGER_THRESHOLD`: number of times the health check can fail before auto-heal begins. The default value is `3`. The minimum value is `0`, but if the value is set to `0`, AlloyDB Omni uses the default value.

An automatic recovery occurs if the health check fails `AUTOHEAL_TRIGGER_THRESHOLD` times or if the cumulative duration of the health check reaches `HEALTHCHECK_PERIOD * AUTOHEAL_TRIGGER_THRESHOLD` seconds.

  * (Optional) `HEALTHCHECK_PERIOD`: number of seconds to wait between each health check. The default value is `30`. The minimum value is `1`. The maximum value is `86400` (one day).

  * `CPU_LIMIT`: number of CPUs to allocate to the database container. For example, `4`.

  * `MEMORY_LIMIT`: amount of memory to allocate to the database container. For example, `32Gi`, `500Mi`.

  * `PG_DATA_DIR`: host path to the directory where the database data will be stored.

  * (Optional) `MAX_CONNECTIONS`: maximum number of concurrent connections to the PostgreSQL database. The default value is `50`. Minimum supported value is also `50`. For more information, see the [PostgreSQL `max_connections` reference](https://www.postgresql.org/docs/18/runtime-config-connection.html#GUC-MAX-CONNECTIONS).

  * (Optional) `MAX_WAL_SIZE`: maximum size to let the Write-Ahead-Log (WAL) grow during automatic checkpoints. The default value is `1GB`. For more information, see the [PostgreSQL `max_wal_size` reference](https://www.postgresql.org/docs/18/runtime-config-wal.html#GUC-MAX-WAL-SIZE).

  * (Optional) `MAX_WORKER_PROCESSES`: maximum number of workers that can be started by a single `Gather` or `Gather Merge`. The default value is `64`. For more information, see the [PostgreSQL `max_worker_processes` reference](https://www.postgresql.org/docs/18/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES).

  * (Optional) `LOG_CONNECTIONS`: determines whether or not connections to your PostgreSQL server are logged. The default value is `on`. For more information, see the [PostgreSQL `log_connections` reference](https://www.postgresql.org/docs/18/runtime-config-logging.html#GUC-LOG-CONNECTIONS).

  * (Optional) `LOG_DISCONNECTS`: determines if PostgreSQL session terminations are logged. The default value is `on`. For more information, see the [PostgreSQL `log_disconnections` reference](https://www.postgresql.org/docs/18/runtime-config-logging.html#GUC-LOG-DISCONNECTIONS).

  * (Optional) `LOG_HOSTNAME`: determines whether or not the hostname is logged in addition to the IP for the connecting host. The default value is `on`. For more information, see the [PostgreSQL `log_hostname` reference](https://www.postgresql.org/docs/18/runtime-config-logging.html#GUC-LOG-HOSTNAME).

  * (Optional) `LOG_STATEMENT`: determines which SQL statements are logged. The default value is `none`. For more information, see the [PostgreSQL `log_statement` reference](https://www.postgresql.org/docs/18/runtime-config-logging.html#GUC-LOG-STATEMENT).

  * (Optional) `HUGE_PAGES`: determines if huge pages are requested for the main shared memory area. The default value is `off`. For more information, see the [PostgreSQL `huge_pages` reference](https://www.postgresql.org/docs/18/runtime-config-resource.html#GUC-HUGE-PAGES).

  * (Optional) `TCP_KEEPALIVES_IDLE`: amount of time, in seconds, with no network activity before the OS attempts to send a TCP `keepalive` message to the client. The default value is `10`. For more information, see the [PostgreSQL `tcp_keepalives_idle` reference](https://www.postgresql.org/docs/18/runtime-config-connection.html#GUC-TCP-KEEPALIVES-IDLE).

  * (Optional) `TCP_KEEPALIVES_INTERVAL`: amount of time, in seconds, before a TCP `keepalive` message that hasn't been acknowledged by the client should be retransmitted. The default value is `10`. For more information, see the [PostgreSQL `tcp_keepalives_interval` reference](https://www.postgresql.org/docs/18/runtime-config-connection.html#GUC-TCP-KEEPALIVES-INTERVAL).

  * (Optional) `TCP_KEEPALIVES_COUNT`: number of TCP `keepalive` messages that can be lost before the server's connection to the client is considered inactive. The default value is `10`. For more information, see the [PostgreSQL `tcp_keepalives_count` reference](https://www.postgresql.org/docs/18/runtime-config-connection.html#GUC-TCP-KEEPALIVES-INTERVAL).

  * (Optional) `ENVIRONMENT_TYPE`: determines the environment where cluster is set up—`onprem` or `gcp`.

  * (Optional) `VIRTUAL_IP`: virtual IP address used by the load balancer. If you define `dbLoadBalancerOptions`, this is required. For more information, see [Manage high availability](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/manage-high-availability).

  * (Optional) `VIRTUAL_IP_INTERFACE`: network interface where `VIRTUAL_IP` is configured. The default value is `eth0`.




## Create your cluster

To create your cluster, select the tab that matches your environment and follow the instructions.

###  Ansible 

To create your cluster, complete the following instructions:

  1. Create a playbook for your database cluster specifications.
         
         - name: Create DBCluster
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
           - role: google.alloydbomni_orchestrator.bootstrap
         
         

Replace the following variables:

     * `ANSIBLE_USER`: OS user that Ansible uses to log into your AlloyDB Omni nodes.

     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

  2. Run your playbook.
         
         ansible-playbook DBCLUSTER_PLAYBOOK -i "DEPLOYMENT_SPEC" \
               -e resource_spec="DBCLUSTER_SPECIFICATIONS"

Replace the following variables:

     * `DBCLUSTER_PLAYBOOK`: path to the playbook that you created for your database cluster.

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

     * `DBCLUSTER_SPECIFICATIONS`: path to your cluster specifications.




###  `alloydbctl`

To create your cluster, run the following command:
    
    
    alloydbctl apply -d "DEPLOYMENT_SPEC" -r "DBCLUSTER_SPECIFICATIONS"

Replace the following variables:

  * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

  * `DBCLUSTER_SPECIFICATIONS`: path to your cluster specifications.




## Delete your cluster

To delete your cluster, select the tab that matches your environment and follow the instructions.

###  Ansible 

To delete your cluster using Ansible, complete the following:

  1. Create a playbook named `teardown.yaml`:
         
         - name: Tear down AlloyDB Omni cluster
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
           - role: google.alloydbomni_orchestrator.delete
         

  2. Execute the playbook using `ansible-playbook`. You must specify `DBCluster` as the `resource_type` and the name of the cluster to be deleted as `resource_name`.
         
         ansible-playbook -i "DEPLOYMENT_SPEC" teardown.yaml \
           -e `resource_type`=`DBCluster` -e `resource_name`="DBCLUSTER_NAME"




If the teardown process fails due to inconsistencies in the cluster state (for example, if a node is unreachable), you can attempt to force delete your cluster by adding `-e force=true` to the command. This instructs the orchestrator to ignore errors during the teardown process and attempt to remove as many resources as possible.
    
    
      ansible-playbook -i "DEPLOYMENT_SPEC" teardown.yaml \
        -e resource_type=DBCluster -e resource_name="DBCLUSTER_NAME" -e force=true

###  `alloydbctl`

To delete your cluster using `alloydbctl`, run the following command:
    
    
    alloydbctl delete -d "DEPLOYMENT_SPEC" \
          --resource_type DBCluster --resource_name "DBCLUSTER_NAME"

Replace the following variables:

  * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

  * `DBCLUSTER_NAME`: name of your database cluster. For example, `my-dbcluster`. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
