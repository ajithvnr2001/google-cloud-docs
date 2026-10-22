---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/configure-log-redirection/
title: Configure log redirection \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:13:43.598359+00:00
---

# Configure log redirection  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/configure-log-redirection/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Configure log redirection Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/configure-log-redirection)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/configure-log-redirection)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/configure-log-redirection)



# Configure log redirection

You can redirect control plane and data plane service logs, internal logs, audit logs, and backup logs (`pgBackRest`) in AlloyDB Omni to a centralized folder or observation disk. By aggregating logs distributed across local node paths—such as `/var/log` or `/run/log`—you enable production monitoring tools to identify system errors, improve system observability, and streamline troubleshooting.

### Centralized observability

The AlloyDB Omni stack contains multiple components separated into a control plane—for example, cluster manager, node manager, `etcd`—and a data plane. Log redirection pushes logs from these components to a centralized path or observation disk (`ObsDisk`). You can then pipe these logs into your observability tools to detect system issues without needing to access individual node paths.

`etcd` is a standalone distributed configuration store required by the cluster manager to coordinate and manage state. It can run on its own dedicated nodes or be colocated with cluster manager nodes. In contrast, node managers act as local agents installed on data plane nodes—database and load balancer nodes—to process control plane commands.

Log redirection covers the following components:

  * Control plane components service logs 
    * cluster manager on cluster manager nodes
    * node manager on all nodes
    * `etcd` on the `etcd` nodes
  * Data plane components service logs 
    * `alloydbomni` on primary instance and readpool instance nodes
    * `alloydbomni` monitor on primary instance and readpool instance nodes
    * `pgBackRest` on primary instance nodes
    * `pgbouncer` on primary instance nodes or load balancer nodes
    * `keepalived` on primary instance nodes or load balancer nodes
    * `HAProxy` on load balancer nodes
  * AlloyDB Omni internal and audit logs



## Limitations

  * `rsyslog` and `journal` have limitations regarding global limits and rate-based limits.
  * `etcd` log redirection is only supported when you use the Ansible interface.
  * Logs truncation: `rsyslog` doesn't have built-in support for log truncation.
  * Rsyslog observability: direct monitoring of `rsyslog` daemon status might require additional setup.



## Before you begin

  * Verify that paths specified for log redirection exist on the relevant nodes and that they're directories.



## Configure log redirection

To configure log redirection in AlloyDB Omni, you must specify destination directories for both control plane and data plane components.

### Redirect control plane logs

Follow these steps to configure log redirection for the control plane components `cluster manager`, `node manager`, and `etcd`.

  1. Open your `deployment_spec.yaml` file.

  2. Add parameters to the `cluster_manager` and `etcd` stanzas to specify the destination directory.

The following `deployment_spec.yaml` provides an example:
         
         alloydbomni:
           vars:
             cluster_manager:
               name: CM_CLUSTER
               logging:
                 disk:
                   path: "/obs"
             etcd:
               logging:
                 disk:
                   path: "/obs"
         

You can provision the `etcd` service separately. To capture all control plane logs, you must define the `logging` path under both the `cluster_manager` and `etcd` stanzas in your `deployment_spec.yaml` file.

The following table describes the parameters for configuring control plane log redirection, which you can use to specify the destination path for logs in your deployment specification:

Parameter | Required | Description  
---|---|---  
`logging.disk` | No | Subsection for control plane log redirection to disk.  
`logging.disk.path` | Conditional | Required if `logging.disk` is set. Disk path where `rsyslog` redirects service logs. Must exist on nodes and must be a directory.  
  3. Apply the configuration changes.

### Ansible

The Ansible orchestrator automatically invokes configuration utilities during installation or update. To apply configuration updates using the Ansible orchestrator, follow these steps:

     1. Open your Ansible control node, which is the administrative machine or workstation where you installed Ansible.
     2. Create a file named `update.yml` and add the following contents:
            
            ---
            - hosts: all
              become: true
              vars:
                update_action: "update_logging"
                ansible_user: SSH_USER
                ansible_ssh_private_key_file: ~/path/to/private-key
              roles:
                - role: google.alloydbomni_orchestrator.update
            

Replace `SSH_USER` with the SSH username that you used to connect to your deployment nodes.

     3. Run the playbook to apply the configuration changes.
            
            ansible-playbook -i DEPLOYMENT_SPECIFICATION update.yml

Replace `DEPLOYMENT_SPECIFICATION` with the path to the deployment specification file that you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components#install-components)—for example, `deployment_spec.yaml`.

### alloydbctl

     1. On cluster manager nodes, run the following command:
            
            /usr/local/bin/alloydbomni_cm_config apply -d deployment_spec.yaml
            

     2. On node manager nodes, which include all of the database and load balancer nodes, run the following command:
            
            /usr/local/bin/alloydbomni_nm_config apply -d deployment_spec.yaml
            

     3. On `etcd` nodes, create or update the `etcd` systemd override file `/etc/systemd/system/etcd.service.d/logging.conf` with the following:
            
            [Service]
            SyslogIdentifier=etcd
            

     4. Create or update the `etcd` rsyslog file `/etc/rsyslog.d/etcd.conf`:
            
            template(name="DailyLogProg_etcd" type="string" string="ETCD_LOG_REDIRECT_DIR/%$year%-%$month%-%$day%-journal.log")
              if $programname == 'etcd' then {
                action(type="omfile" dynaFile="DailyLogProg_etcd" FileCreateMode="0644")
                stop
              }
            

Replace `ETCD_LOG_REDIRECT_DIR` with the path to the directory where you want `etcd` logs redirected—for example, `/obs`.

     5. Restart the `rsyslog` service:
            
            sudo systemctl restart rsyslog
            




### Redirect data plane logs

To configure log redirection for data plane components, follow these steps:

  1. Open your `DBCluster` resource specification.

  2. Add an observation disk (`ObsDisk`) to the list of disks. The following example shows how to define a storage extension, add an observation disk, and specify that the disk must be mounted or accessed at the path `/obs`.
         
         DBCluster:
            metadata:
              name: "DBCLUSTER_NAME"
            spec:
              primarySpec:
                resources:
                  disks:
                  - name: ObsDisk
                    path: /obs
          ```
         

  3. Apply or bootstrap the `DBCluster` resource.

### Ansible

     1. Create a file named `update.yml` and add the following contents:
            
            ---
            - hosts: all
              vars:
                update_action: "update_resource_spec"
                ansible_user: SSH_USER
                ansible_ssh_private_key_file: PRIVATE_KEY_PATH
              roles:
                - role: google.alloydbomni_orchestrator.update
            

Replace the following:

        * `SSH_USER`: the SSH username used to connect to your deployment nodes.
        * `PRIVATE_KEY_PATH`: the path to the SSH private key file on your Ansible control node—for example,`~/path/to/private-key`.
     2. Run the playbook to apply the configuration changes.
            
            ansible-playbook -i DEPLOYMENT_SPECIFICATION update.yml -e "resource_spec=DBCLUSTER_SPECIFICATION"

Replace the following:

        * `DEPLOYMENT_SPECIFICATION`: path to the deployment specification that you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).
        * `DBCLUSTER_SPECIFICATION`: path to your cluster specification.

### alloydbctl

Run the following command:
    
    alloydbctl apply -d DEPLOYMENT_SPECIFICATION -r DBCLUSTER_SPECIFICATION

Replace the following:

     * `DEPLOYMENT_SPECIFICATION`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).
     * `DBCLUSTER_SPECIFICATION`: path to your cluster specification.




## Verify log redirection

After you apply your configurations, verify that the logs are streaming to the specified directories by reviewing the control plane and data plane redirected paths.

### Control plane redirected paths

Component | Redirected log path  
---|---  
`alloydbomni_cluster_manager` | `LOGGING_DISK_PATH/CM_CLUSTER_NAME/alloydbomni_cluster_manager/YYYY-MM-DD-journal.log`  
`alloydbomni_node_manager` | `LOGGING_DISK_PATH/CM_CLUSTER_NAME/alloydbomni_node_manager/YYYY-MM-DD-journal.log`  
`etcd` | `LOGGING_DISK_PATH/CM_CLUSTER_NAME/etcd/YYYY-MM-DD-journal.log`  
  
  * `LOGGING_DISK_PATH`: the base directory path on your node where the control plane service logs are redirected—for example, `/obs`.
  * `CM_CLUSTER_NAME`: the name of your control plane cluster as defined in the `deployment_spec.yaml` file.



### Data plane redirected paths

Component | Redirected log path  
---|---  
`alloydbomni` | `OBS_DISK_PATH/DB_CLUSTER_NAME/alloydbomniVERSION@SYSTEMD_INSTANCE_NAME/YYYY-MM-DD-journal.log`  
`alloydbomni_monitor` | `OBS_DISK_PATH/DB_CLUSTER_NAME/alloydbomni_monitor@SYSTEMD_INSTANCE_NAME/YYYY-MM-DD-journal.log`  
`pgbouncer` | `OBS_DISK_PATH/DB_CLUSTER_NAME/PgBouncer@SYSTEMD_INSTANCE_NAME/YYYY-MM-DD-journal.log`  
`keepalived` | `OBS_DISK_PATH/DB_CLUSTER_NAME/keepalived@SYSTEMD_INSTANCE_NAME/YYYY-MM-DD-journal.log`  
`haproxy` | `OBS_DISK_PATH/DB_CLUSTER_NAME/haproxy@SYSTEMD_INSTANCE_NAME/YYYY-MM-DD-journal.log`  
`pgbackrest` | `OBS_DISK_PATH/DB_CLUSTER_NAME/pgbackrest/YYYY-MM-DD-*.log`  
  
  * `OBS_DISK_PATH`: the path specified in `ObsDisk`—for example, `/obs`.
  * `DB_CLUSTER_NAME`: the name of your database cluster.



### Logging configuration parameters

AlloyDB Omni automatically sets the standard PostgreSQL parameters to manage log generation based on your configuration. However, you can override parameters like `log_rotation_age` and `log_filename` in your user-defined parameter to customize your log rotation policy.

GUC | Description | Without OBS disk | With OBS disk  
---|---|---|---  
`logging_collector` | Enables the logging collector background process. | On | On  
`log_directory` | Directory for internal and audit logs. | `DATA_DISK_PATH/VERSION/log` | `OBS_DISK_PATH/DB_CLUSTER_NAME/alloydbomni/VERSION`  
`log_filename` | Filename pattern (`strftime`). | `postgresql-%H.log` (truncated every 24 hours) | `postgresql-%Y-%m-%d_%H%M%S.log`  
`log_file_mode` | File permissions. | `0600` | `0600`  
`log_rotation_age` | Maximum time to use a file before rotating. | 60 minutes | 60 minutes  
`log_rotation_size` | Maximum file size before rotating. | 0 | 0  
`log_truncate_on_rotation` | Truncate rather than append on rotation. | On | Off  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
