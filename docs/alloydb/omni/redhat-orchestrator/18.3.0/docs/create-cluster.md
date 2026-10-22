---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/create-cluster/
title: Create a cluster \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:39:56.616542+00:00
---

# Create a cluster  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/create-cluster/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Create a cluster Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

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

  * [Install the AlloyDB Omni orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-orchestrator)

  * [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components)

  * [Configure TLS certificates](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/tls/configure-tls-certificates)

  * Mount an external volume (`DataDisk`) to PG_DATA_DIR on all database nodes provisioned within the orchestrator.

  * If you plan to use `alloydbctl` instead of Ansible, ensure that the required `policycoreutils-python-utils` package is installed on all of your VMs. To install this package, run the following command:
        
        sudo dnf install policycoreutils-python-utils

  * If you're using the Google Cloud environment, then set `ENVIRONMENT_TYPE` to `gcp`. Then you must authenticate your gcloud CLI account by running `gcloud auth login` as the `root` user. Additionally, the authenticated account must have the following permissions:

    * `compute.instances.get`
    * `compute.instances.list`
    * `compute.instances.updateNetworkInterface`



## Prepare cluster specifications

To create your cluster, AlloyDB Omni must know how to configure it. To create the necessary specifications, create a YAML file using the [`DBCluster`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/reference/dbcluster-spec) format:
    
    
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
        databaseVersion: 18.3.0
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

  * (Optional) `ENVIRONMENT_TYPE`: determines the environment where cluster is set up—`onprem` or `gcp`.

  * (Optional) `VIRTUAL_IP`: virtual IP address used by the load balancer. If you define `dbLoadBalancerOptions`, this is required. For more information, see [Manage high availability](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/manage-high-availability).

  * (Optional) `VIRTUAL_IP_INTERFACE`: network interface where `VIRTUAL_IP` is configured. The default value is `eth0`.




## Create your cluster

To create your cluster, select the tab that matches your environment and follow the instructions.

###  Ansible 

To create your cluster, complete the following instructions:

  1. Create a playbook for your database cluster specifications.
         
         - name: Create DBCluster
           hosts: localhost
           become: true
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

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).

     * `DBCLUSTER_SPECIFICATIONS`: path to your cluster specifications.




###  `alloydbctl`

To create your cluster, run the following command:
    
    
    alloydbctl apply -d "DEPLOYMENT_SPEC" -r "DBCLUSTER_SPECIFICATIONS"

Replace the following variables:

  * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).

  * `DBCLUSTER_SPECIFICATIONS`: path to your cluster specifications.




## Delete your cluster

To delete your cluster, select the tab that matches your environment and follow the instructions.

###  Ansible 

To delete your cluster using Ansible, complete the following:

  1. Create a playbook named `teardown.yaml`:
         
         - name: Tear down AlloyDB Omni cluster
           hosts: localhost
           become: true
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

  * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).

  * `DBCLUSTER_NAME`: name of your database cluster. For example, `my-dbcluster`.




## Appendix: SELinux policy specifications

The following tables list the SELinux policy rules and access permissions configured for each component running on the respective nodes. These policies define the mandatory boundaries for process isolation, network socket bindings, and storage access required when running hosts in SELinux Enforcing mode.

### AlloyDB Omni

Source domain | Target resource / type | Security class | Granted permissions | Security rationale & constraint  
---|---|---|---|---  
`init_t` (systemd) | `postgresql_exec_t` | `file` | `getattr`, `open`, `read`, `execute` | Allows systemd service manager to execute the PostgreSQL binary.  
`init_t` | `postgresql_t` | `process` | `transition` | Enforces mandatory domain transition from systemd into the confined `postgresql_t` domain.  
`postgresql_t` | `postgresql_exec_t` | `file` | `entrypoint`, `execute`, `read`, `map` | Restricts domain entry strictly to the official PostgreSQL executable.  
`postgresql_t` | `lib_t` | `file` / `dir` | `read`, `open`, `getattr`, `map` | Authorizes dynamic linker access to shared database libraries.  
`postgresql_t` | `postgresql_db_t` | `dir` | `open`, `read`, `write`, `create`, `rmdir`, `search`, `getattr`, `setattr`, `add_name`, `remove_name` | Manages the complete storage directory lifecycle for the data directory and tablespaces.  
`postgresql_t` | `postgresql_db_t` | `file` | `open`, `read`, `write`, `create`, `unlink`, `lock`, `append`, `getattr`, `setattr`, `map` | Authorizes read/write operations for heap tables, WAL segments, catalogs, and indexes.  
`postgresql_t` | `postgresql_var_run_t` | `dir` / `sock_file` | `open`, `read`, `write`, `create`, `unlink`, `search`, `getattr` | Manages runtime PID file and Unix domain socket in `/var/run/postgresql`.  
`postgresql_t` | `postgresql_port_t` | `tcp_socket` | `name_bind` | Restricts TCP network binding strictly to assigned PostgreSQL ports (default TCP 5432).  
`alloydbomni_nm_t` | `postgresql_exec_t` | `file` | `execute`, `execute_no_trans`, `getattr`, `open`, `read`, `map` | Authorizes Node Manager to run health probes and control tools, for example `pg_isready` or `pg_ctl`.  
`alloydbomni_nm_t` | `postgresql_db_t` | `dir` / `file` | `open`, `read`, `write`, `create`, `unlink`, `relabelto`, `relabelfrom` | Grants Node Manager the authority to initialize directories and apply SELinux labels.  
  
### AlloyDB Omni monitor

Source domain | Target resource / type | Security class | Granted permissions | Security rationale & constraint  
---|---|---|---|---  
`postgresql_t` | `unreserved_port_t` | `tcp_socket` | `name_bind` | Authorizes binding to a high unreserved port to export Prometheus metrics and health status.  
`postgresql_t` | `net_conf_t` | `file` | `open`, `read`, `getattr` | Read-only access to `/etc/resolv.conf` for DNS and hostname resolution.  
`postgresql_t` | `sysfs_t` | `file` / `dir` | `open`, `read`, `getattr`, `search` | Host metrics inspection without granting root or administrative privileges.  
  
### Keepalived

Source domain | Target resource / type | Security class | Granted permissions | Security rationale & constraint  
---|---|---|---|---  
`keepalived_t` | `keepalived_script_exec_t` | `file` | `execute`, `execute_no_trans`, `getattr`, `open`, `read`, `map`, `setattr`, `ioctl` | Confines execution of VIP tracking scripts to a dedicated, restricted script context.  
`keepalived_t` | `hostname_exec_t` | `file` | `execute`, `execute_no_trans`, `getattr`, `open`, `read`, `map` | Invokes standard system `hostname` to verify node identity during failover.  
`keepalived_t` | `ifconfig_exec_t` | `file` | `execute`, `execute_no_trans`, `getattr`, `open`, `read`, `map` | Assigns and releases the Virtual IP on the physical network interface.  
`keepalived_t` | `systemd_systemctl_exec_t` | `file` | `execute`, `execute_no_trans`, `getattr`, `open`, `read`, `map` | Queries service dependency states using systemctl without modifying service configuration.  
`keepalived_t` | `system_dbusd_t` | `unix_stream_socket` | `connectto` | Connects to system DBus daemon for inter-process notifications.  
`keepalived_t` | `system_dbusd_t` / `init_t` | `dbus` | `send_msg` | Broadcasts DBus state transition events to the `init_t` systemd domain.  
`keepalived_t` | `haproxy_unit_file_t` / `systemd_unit_file_t` | `service` | `status` | Checks operational state of HAProxy and related services.  
`keepalived_t` | `haproxy_var_lib_t` | `dir` / `file` / `sock_file` | `open`, `read`, `write`, `search`, `getattr` | Inspects colocated HAProxy stats socket in `/var/lib/haproxy` when deployed.  
`keepalived_t` | `keepalived_var_run_t` | `dir` / `file` | `open`, `read`, `write`, `create`, `unlink`, `search`, `getattr` | Maintains runtime state and PID tracking files in `/var/run/keepalived`.  
`alloydbomni_nm_t` | `keepalived_t` | `process` | `signal`, `signull` | Enables Node Manager to manage daemon lifecycle using POSIX signals.  
  
### HAProxy

Source domain | Target resource / type | Security class | Granted permissions | Security rationale & constraint  
---|---|---|---|---  
`haproxy_t` | `postgresql_port_t` | `tcp_socket` | `name_bind`, `name_connect` | Listens on port 5432 and forwards database connections to backend database nodes.  
`haproxy_t` | `unreserved_port_t` | `tcp_socket` | `name_bind`, `name_connect` | Listens on custom load-balancer ports and connects to upstream read/write endpoints.  
`haproxy_t` | `haproxy_conf_t` | `file` / `dir` | `open`, `read`, `search`, `getattr` | Read-only configuration access for `/etc/haproxy/haproxy.cfg`.  
`haproxy_t` | `haproxy_var_lib_t` | `dir` / `file` / `sock_file` | `open`, `read`, `write`, `create`, `unlink`, `search`, `getattr` | Manages runtime sockets and stats tables in `/var/lib/haproxy`.  
`haproxy_t` | `haproxy_var_run_t` | `dir` / `file` | `open`, `read`, `write`, `create`, `unlink`, `search`, `getattr` | Manages PID and control sockets in `/var/run/haproxy`.  
`alloydbomni_nm_t` | `haproxy_unit_file_t` | `service` | `start`, `stop`, `status`, `reload`, `enable`, `disable` | Authorizes Node Manager to control HAProxy systemd service lifecycle.  
`alloydbomni_nm_t` | `haproxy_t` | `process` | `signal`, `signull` | Authorizes Node Manager to send reload signals upon configuration changes.  
  
### PgBouncer

Source domain | Target resource / type | Security class | Granted permissions | Security rationale & constraint  
---|---|---|---|---  
`init_t` | `pgbouncer_exec_t` | `file` | `getattr`, `open`, `read`, `execute` | Allows systemd to invoke the PgBouncer executable (`/usr/bin/pgbouncer`).  
`init_t` | `pgbouncer_t` | `process` | `transition` | Automates domain transition from systemd to isolated `pgbouncer_t`.  
`pgbouncer_t` | `pgbouncer_exec_t` | `file` | `entrypoint`, `execute`, `read`, `map` | Restricts executable entrypoint to `/usr/bin/pgbouncer`.  
`pgbouncer_t` | `unreserved_port_t` | `tcp_socket` | `name_bind` | Listens for incoming client database connections, for example, TCP port 6432.  
`pgbouncer_t` | `node_t` | `tcp_socket` | `node_bind` | Binds network socket to node network interfaces.  
`pgbouncer_t` | `postgresql_port_t` / `unreserved_port_t` | `tcp_socket` | `name_connect` | Initiates TCP connections to backend AlloyDB Omni database instances.  
`pgbouncer_t` | `self` | `unix_stream_socket` | `create`, `bind`, `listen`, `accept`, `read`, `write`, `connectto` | Provides local client connectivity over Unix domain sockets.  
`pgbouncer_t` | `pgbouncer_conf_t` | `file` / `dir` | `open`, `read`, `getattr`, `search` | Read-only configuration access for `/etc/pgbouncer/pgbouncer.ini` and user authentication files.  
`pgbouncer_t` | `pgbouncer_var_run_t` / `tmp_t` | `dir` / `sock_file` | `open`, `read`, `write`, `create`, `unlink`, `search`, `getattr` | Creates and manages runtime socket files in `/var/run/pgbouncer` and `/tmp`.  
`pgbouncer_t` | `self` | `netlink_route_socket` | `create`, `bind`, `read`, `write`, `nlmsg_read`, `getattr` | Discovers network route for resolving database and client endpoints.  
`pgbouncer_t` | `self` | `udp_socket` | `create`, `connect`, `read`, `write`, `getattr`, `setopt`, `getopt` | Performs DNS name resolution.  
`pgbouncer_t` | `init_t` / `kernel_t` | `unix_dgram_socket` | `sendto` | Sends `sd_notify` heartbeat and readiness signals to systemd.  
`pgbouncer_t` | `sysfs_t` | `file` / `dir` | `open`, `read`, `getattr`, `search` | Reads CPU topology for worker thread optimization.  
  
### pgBackRest

Source domain | Target resource / type | Security class | Granted permissions | Security rationale & constraint  
---|---|---|---|---  
`postgresql_t` / `alloydbomni_nm_t` | `pgbackrest_exec_t` | `file` | `execute`, `getattr`, `open`, `read`, `map` | Allows Postgres and Node Manager to execute `/usr/bin/pgbackrest` for WAL archiving and backups, respectively.  
`postgresql_t` / `alloydbomni_nm_t` | `pgbackrest_t` | `process` | `transition`, `signal`, `sigkill`, `signull` | Controlled process transition into confined `pgbackrest_t` domain.  
`pgbackrest_t` | `pgbackrest_exec_t` | `file` | `entrypoint`, `execute`, `execute_no_trans`, `read`, `map`, `getattr`, `open` | Confines pgBackRest binary entrypoint.  
`pgbackrest_t` | `postgresql_db_t` | `dir` / `file` / `lnk_file` | `open`, `read`, `write`, `create`, `unlink`, `lock`, `append`, `search`, `getattr`, `setattr`, `map` | Reads/writes database files during physical backup and Point-in-Time Recovery (PITR).  
`pgbackrest_t` | `postgresql_t` | `unix_stream_socket` | `connectto` | Connects to running PostgreSQL engine using local socket to trigger backup checkpoints.  
`pgbackrest_t` | `postgresql_var_run_t` | `dir` / `sock_file` / `file` | `open`, `read`, `write`, `search`, `getattr` | Accesses PostgreSQL connection socket in `/var/run/postgresql`.  
`pgbackrest_t` | `http_port_t` | `tcp_socket` | `name_connect` | **Strict Egress** : Outbound TCP connections restricted strictly to HTTPS (443) for cloud object storage (GCS/S3). Inbound listeners are prohibited.  
`pgbackrest_t` | `cert_t` | `dir` / `file` / `lnk_file` | `open`, `read`, `search`, `getattr`, `map` | Reads system trust store certificates (`/etc/pki/tls`) to validate TLS connections to object storage.  
`pgbackrest_t` | `pgbackrest_conf_t` | `file` / `dir` | `open`, `read`, `getattr`, `search`, `map` | Read-only configuration access for `/etc/pgbackrest/pgbackrest.conf`.  
`pgbackrest_t` | `pgbackrest_log_t` | `file` / `dir` | `open`, `read`, `write`, `create`, `unlink`, `append`, `lock`, `getattr`, `setattr` | Manages audit logs in `/var/log/pgbackrest`.  
`pgbackrest_t` | `pgbackrest_tmp_t` | `dir` / `file` / `sock_file` | `open`, `read`, `write`, `create`, `unlink`, `append`, `lock`, `getattr`, `setattr`, `relabelto`, `relabelfrom` | Dedicated isolated temporary storage and inter-thread communication sockets in `/tmp/pgbackrest`.  
`pgbackrest_t` | `shadow_t` / `sysfs_t` / `sssd_var_lib_t` | `file` / `dir` | `dontaudit` (suppressed) | Silently drops and ignores irrelevant host credential probes, preventing audit log pollution.  
  
### Node Manager

Source domain | Target resource / type | Security class | Granted permissions | Security rationale & constraint  
---|---|---|---|---  
`init_t` | `alloydbomni_nm_exec_t` | `file` | `getattr`, `open`, `read`, `execute` | Allows systemd to launch the Node Manager daemon.  
`alloydbomni_nm_t` | `self` | `capability` | `audit_write`, `chown`, `dac_override`, `dac_read_search`, `fowner`, `fsetid`, `setgid`, `setuid`, `net_admin` | Strictly bounded Linux capabilities required for host lifecycle management and volume provisioning.  
`alloydbomni_nm_t` | `unreserved_port_t` | `tcp_socket` | `name_bind`, `name_connect` | Serves gRPC / HTTP APIs to Cluster Manager and serves health check probes to HAProxy.  
`alloydbomni_nm_t` | `http_port_t` | `tcp_socket` | `name_connect` | Outbound communication to cloud APIs or monitoring endpoints.  
`alloydbomni_nm_t` | `semanage_exec_t`, `setfiles_exec_t`, `setsebool_exec_t`, `load_policy_exec_t` | `file` | `execute`, `execute_no_trans`, `getattr`, `open`, `read`, `map` | Executes core SELinux management binaries to compile and enforce CIL policies.  
`alloydbomni_nm_t` | `security_t` | `security` | `load_policy` | Loads compiled SELinux policy modules directly into the Linux kernel.  
`alloydbomni_nm_t` | `semanage_store_t`, `selinux_config_t` | `dir` / `file` | `open`, `read`, `write`, `create`, `unlink`, `lock`, `getattr` | Maintains SELinux persistent policy configuration stores.  
`alloydbomni_nm_t` | `unlabeled_t` (disks/mounts) | `filesystem` / `dir` / `file` | `getattr`, `open`, `read`, `write`, `create`, `unlink`, `setattr`, `relabelto`, `relabelfrom` | **Dynamic Disk Relabeling** : Discovers freshly attached raw disks, for example `/data1` or `/obs` and relabels them to `postgresql_db_t`.  
`alloydbomni_nm_t` | `rpm_exec_t` | `file` | `execute`, `execute_no_trans`, `getattr`, `open`, `read`, `ioctl`, `map` | Executes RPM/DNF package manager commands for automated software installation and updates.  
`alloydbomni_nm_t` | `rpm_var_cache_t`, `rpm_var_lib_t`, `rpm_log_t` | `dir` / `file` | `open`, `read`, `write`, `create`, `unlink`, `lock`, `getattr` | Manages RPM database and cache files during package installations.  
`alloydbomni_nm_t` | `systemd_unit_file_t`, `syslogd_unit_file_t`, `haproxy_unit_file_t`, `keepalived_unit_file_t` | `service` | `start`, `stop`, `status`, `reload`, `enable`, `disable` | Orchestrates systemd service lifecycles across all managed database and auxiliary components.  
`alloydbomni_nm_t` | `system_dbusd_t`, `systemd_logind_t`, `systemd_hostnamed_t` | `dbus` / `unix_stream_socket` | `send_msg`, `connectto` | Coordinates host state, time, and system logging over system DBus.  
  
### Cluster Manager

Source domain | Target resource / type | Security class | Granted permissions | Security rationale & constraint  
---|---|---|---|---  
`init_t` | `alloydbcontrol_exec_t` | `file` | `getattr`, `open`, `read`, `execute` | Allows systemd to launch the Cluster Manager executable.  
`alloydbcontrol_t` | `alloydbcontrol_exec_t` | `file` | `entrypoint`, `execute`, `read`, `map`, `getattr`, `open` | Confines control plane execution to the authorized binary.  
`alloydbcontrol_t` | `unreserved_port_t` | `tcp_socket` | `name_bind`, `name_connect` | Binds API endpoints and connects to Distributed Consensus Store (DCS / etcd) and Node Managers.  
`alloydbcontrol_t` | `node_t` | `tcp_socket` | `node_bind` | Binds network listeners to network interfaces.  
`alloydbcontrol_t` | `alloydbcontrol_conf_t` | `file` / `dir` | `open`, `read`, `search`, `getattr` | Read-only configuration access for `/etc/alloydbomni/cluster_manager`.  
`alloydbcontrol_t` | `net_conf_t`, `passwd_file_t`, `sssd_public_t`, `sssd_var_lib_t` | `file` / `dir` | `open`, `read`, `search`, `getattr` | Host resolution and user authentication for management interfaces.  
`alloydbcontrol_t` | `cgroup_t`, `sysctl_net_t`, `sysfs_t` | `file` / `dir` | `open`, `read`, `search`, `getattr` | Read-only Go runtime performance optimization and telemetry.  
`alloydbcontrol_t` | `init_t` | `unix_stream_socket` | `dontaudit` (`ioctl`) | Suppresses non-critical systemd file descriptor ioctl warnings.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
