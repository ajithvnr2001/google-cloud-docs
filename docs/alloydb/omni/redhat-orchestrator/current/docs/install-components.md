---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components/
title: Install AlloyDB Omni using the RPM orchestrator \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:03:23.516690+00:00
---

# Install AlloyDB Omni using the RPM orchestrator  |  AlloyDB Omni using the RPM orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview)



Send feedback 

#  Install AlloyDB Omni using the RPM orchestrator Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-components)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components)

This page describes how to install the AlloyDB Omni software stack and its management components using the AlloyDB Omni orchestrator. 

## Before you begin

Before you install the components, make sure you have completed the following prerequisites:

  * [Install the orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-orchestrator): make sure the AlloyDB Omni orchestrator Ansible collection or CLI is installed on your control node.
  * Provision machines: you must have RHEL9 virtual machines provisioned according to your chosen architecture, such as standalone or high availability.
  * [Configure network and firewall](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-orchestrator#configure-network-firewalls): make sure all required ports are open between your nodes. This includes `5432` for database traffic, `2379`/`2380` for `etcd`, and the management ports `6703`, `6702`, and `6700` used by the Cluster Manager and Node Manager.
  * [Check software package dependencies](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/package-dependencies): If you manage software packages through a private Yum repository, then follow the instructions from your repository management to include dependent RPM files into the repository.



## Prepare the deployment specification inventory

**Note:** For optional version parameters in the inventory file, the orchestrator installs the latest available version of the software by default if a specific version is not specified.

The orchestrator uses a deployment specification file in Ansible inventory format to understand your cluster topology. Create a file named `deployment_spec.yaml` with your node details.
    
    
    alloydbomni:
      vars:
        cluster_manager:
          name: "MANAGEMENT_CLUSTER_NAME"
        etcd:
          setup: SETUP_ETCD
          config_forcewrite: FORCE_OVERWRITE_ETCD
          # version: ETCD_VERSION  # Optional: defaults to the latest version
          # repo_url: ETCD_REPOSITORY_URL  # Optional
          # repo_gpg_key_url: GPG_KEY  # Optional
        alloydbomni:
          major_version: "PG_VERSION" # Mandatory: for example, 18
          # version: ALLOYDB_OMNI_VERSION    # Optional: defaults to the latest version
          # repo_url: ALLOYDB_OMNI_COMMON_REPOSITORY_URL     # Optional
          # repo_gpg_key_url: GPG_KEY  # Optional
        alloydbomni_monitor:
          # version: ALLOYDB_OMNI_MONITOR_VERSION    # Optional: defaults to the latest version
          # repo_url: ALLOYDB_OMNI_COMMON_REPOSITORY_URL   # Optional
          # repo_gpg_key_url: GPG_KEY  # Optional
        alloydbomni_cluster_manager:
          # version: ALLOYDB_OMNI_CLUSTER_MANAGER_VERSION      # Optional: defaults to the latest version
          # repo_url: ALLOYDB_OMNI_ORCHESTRATOR_REPOSITORY_URL # Optional
          # repo_gpg_key_url: GPG_KEY  # Optional
        alloydbomni_node_manager:
          # version: ALLOYDB_OMNI_NODE_MANAGER_VERSION         # Optional: defaults to the latest version
          # repo_url: ALLOYDB_OMNI_ORCHESTRATOR_REPOSITORY_URL # Optional
          # repo_gpg_key_url: GPG_KEY  # Optional
        pgbouncer:
          # version: ALLOYDB_OMNI_PGBOUNCER_VERSION    # Optional
          # repo_url: ALLOYDB_OMNI_COMMON_REPOSITORY_URL   # Optional
          # repo_gpg_key_url: GPG_KEY  # Optional
        pgbackrest:
          # version: ALLOYDB_OMNI_PGBACKREST_VERSION   # Optional
          # repo_url: ALLOYDB_OMNI_COMMON_REPOSITORY_URL   # Optional
          # repo_gpg_key_url: GPG_KEY  # Optional
    
      children:
        primary_instance_nodes:
          hosts:
            DB_HOST_1:
            DB_HOST_2:
            DB_HOST_3:
        load_balancer_nodes:    # Optional. Host group for load balancer. If empty, no load balancer is configured.
          hosts:
            LB_HOST_1:
            LB_HOST_2:
        etcd_nodes:     # Optional: Host group where etcd is set up
          hosts:
            ETCD_HOST_1:
            ETCD_HOST_2:
            ETCD_HOST_3:
        cluster_manager_nodes:    # Optional: Host group for cluster manager
          hosts:
            CM_HOST_1:
            CM_HOST_2:
            CM_HOST_3:
    

Replace the following:

  * `MANAGEMENT_CLUSTER_NAME`: the name of your management cluster. This can be the same as your database cluster name if they are installed on the same nodes, for example, `my-management-cluster`.
  * `SETUP_ETCD`: specifies whether the orchestrator must configure and bootstrap the `etcd` cluster. When set to `true`, the orchestrator performs the initial `etcd` setup and initialization on the designated `etcd` nodes. If no `etcd` nodes are defined in your deployment_spec, it defaults to configuring `etcd` on the cluster manager nodes. This parameter corresponds to the `etcd.setup` key in the deployment specification.
  * `FORCE_OVERWRITE_ETCD`: determines whether to replace an existing `etcd` configuration file during the setup process. Set to `true` to overwrite existing configuration file on the target nodes; otherwise, set to `false`(the default) to maintain the existing configuration and prevent unintended service disruptions.
  * `ETCD_VERSION`: the version of the etcd package to install, for example, `3.4.13`.
  * `ETCD_REPOSITORY_URL`: the URL of the repository containing the `etcd` RPMs.
  * `PG_VERSION`: the major PostgreSQL version of your AlloyDB Omni installation, for example, `18`.
  * `ALLOYDB_OMNI_VERSION`: the version of the AlloyDB Omni database engine to install, for example, `18.1.0`. If omitted, the orchestrator installs the latest available version.
  * `ALLOYDB_OMNI_COMMON_REPO_URL`: the URL of the common repository containing AlloyDB Omni, monitor, PgBouncer, and pgBackRest RPMs.
  * `GPG_KEY`: the location of Google's public key for GNU Privacy Guard (GPG) verification—for example, `https://dl.google.com/linux/linux_signing_key.pub`. This can also be set as a path if the key is downloaded to a file on all VMs, for example, `/tmp/linux_signing_key.pub`.
  * `ALLOYDB_OMNI_MONITOR_VERSION`: the version of the AlloyDB Omni monitor package to install. Defaults to the latest available version.
  * `ALLOYDB_OMNI_CLUSTER_MANAGER_VERSION`: the version of the AlloyDB Omni cluster manager to install. If omitted, the orchestrator installs the latest available version.
  * `ALLOYDB_OMNI_ORCHESTRATOR_REPO_URL`: the URL of the repository containing the AlloyDB Omni cluster manager and node manager RPMs.
  * `ALLOYDB_OMNI_NODE_MANAGER_VERSION`: the version of the AlloyDB Omni node manager to install. If omitted, the orchestrator installs the latest available version.
  * `ALLOYDB_OMNI_PGBOUNCER_VERSION`: the version of the PgBouncer package to install.
  * `ALLOYDB_OMNI_PGBACKREST_VERSION`: the version of the pgBackRest package to install.
  * `DB_HOST_1`, `DB_HOST_2`, `DB_HOST_3`: the IP addresses or fully qualified domain names (FQDNs) of the virtual machines designated as database nodes.
  * `LB_HOST_1`, `LB_HOST_2`: the IP addresses or fully qualified domain names (FQDNs) of the virtual machines designated as load balancer nodes.
  * `ETCD_HOST_1`, `ETCD_HOST_2`, `ETCD_HOST_3`: the IP addresses or FQDNs of the virtual machines designated as `etcd` nodes.
  * `CM_HOST_1`, `CM_HOST_2`, `CM_HOST_3`: the IP addresses or FQDNs of the virtual machines designated as cluster manager nodes.



## Install the components

You can install the AlloyDB Omni components and their dependencies using Ansible or by manually installing the software packages on each node.

### Install AlloyDB Omni components using Ansible

The recommended method for installation is using the provided Ansible role.

  1. Create a playbook named `install.yaml` that references the install role from the orchestrator collection.
         
         - name: Install AlloyDB Omni cluster components
           hosts: all
           become: true
           vars:
             ansible_user: SSH_USER
             ansible_ssh_private_key_file: SSH_KEY_PATH
           roles:
             - role: google.alloydbomni_orchestrator.install
         

Replace the following:

     * `SSH_USER`: the username that you use to connect to the nodes in your cluster using SSH.
     * `SSH_KEY_PATH`: the path to the SSH private key file on your control node —for example, `~/.ssh/id_rsa`.
  2. To download and install the components across all specified nodes, execute the playbook using your inventory file.
         
         ansible-playbook -i deployment_spec.yaml install.yaml
         


**Note:** The `google.alloydbomni_orchestrator.install` role configures the EPEL release repository on all nodes. Make sure that the `epel-release yum` repository is accessible.

### Install AlloyDB Omni components without Ansible

If you do not have an Ansible environment and you plan to use Orchestrator CLI for cluster management, you will need to install all the components manually, as Orchestrator CLI does not provide automated installation of components.

#### Install components on all nodes

The table below lists down all the types of nodes and corresponding components (RPMs) to be installed.

Node | SW Components (RPM) | Note  
---|---|---  
`control node` | `alloydbomni_orchestrator` |   
`primary_instance_nodes` | `alloydbomni18`  
`alloydbomni_monitor`  
`alloydbomni_node_manager`  
`keepalived`  
`pgbackrest`  
`pgbouncer` | Keepalived and pgbouncer are needed only for environments where there are no load balancers.  
`etcd_nodes` | `etcd` | ETCD can be installed on cluster manager nodes when there are no dedicated nodes for ETCD.  
`cluster_manager_nodes` | `alloydbomni_cluster_manager` | Cluster Manager can be installed on the DB nodes (`primary_instance_nodes`) when there are no dedicated nodes for Cluster Manager.  
`load_balancer_nodes` | `alloydbomni_node_manager`  
`haproxy`  
`keepalived`  
`pgbouncer` | keepalived and pgbouncer are installed on load balancer nodes only for the environment where there are load balancers configured.  
  
Installation commands:

  * `REPO_GPG_KEY`: Location of Google's public key for GPG verification, for example, `https://dl.google.com/linux/linux_signing_key.pub`. Can also be set as a file path once downloaded and placed on all VMs, for example, `file:///tmp/linux_signing_key.pub`.



#### Install AlloyDB Omni components on etcd nodes

  1. On all `etcd` nodes, create a YUM repository configuration file named `/etc/yum.repos.d/alloydb-etcd.repo`:
         
         [etcd]
         name=AlloyDB Omni ETCD
         baseurl=ETCD_REPOSITORY_URL
         enabled=1
         repo_gpgcheck=0
         gpgcheck=1
         gpgkey=REPO_GPG_KEY
         

  2. Install `etcd`:
         
         sudo dnf install -y etcd
         

  3. Bootstrap `etcd` by editing the configuration file. You must bootstrap `etcd` before you install AlloyDB Omni components.

**Note:** For information about how to obtain or generate the required certificate and key files, see [Configure SSL certificates for the control path](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/tls/configure-tls-certificates#control-path-cli).

On `etcd_nodes`, edit `/etc/etcd/etcd.conf`:
         
         ETCD_NAME=ETCD_HOST
         ETCD_DATA_DIR=/var/lib/etcd/data
         ETCD_LISTEN_PEER_URLS=https://ETCD_HOST_IP:2380,https://127.0.0.1:2380
         ETCD_LISTEN_CLIENT_URLS=https://ETCD_HOST_IP:2379,https://127.0.0.1:2379
         ETCD_INITIAL_ADVERTISE_PEER_URLS=https://ETCD_HOST_IP:2380
         ETCD_ADVERTISE_CLIENT_URLS=https://ETCD_HOST_IP:2379
         
         ETCD_INITIAL_CLUSTER=ETCD_HOST_1=https://ETCD_HOST_IP_1:2380,ETCD_HOST_2=https://ETCD_HOST_IP_2:2380,ETCD_HOST_3=https://ETCD_HOST_IP_3:2380
         
         ETCD_INITIAL_CLUSTER_STATE=new
         ETCD_INITIAL_CLUSTER_TOKEN=CLUSTER_NAME
         ETCD_ENABLE_V2=true
         
         ETCD_CLIENT_CERT_AUTH=true
         ETCD_TRUSTED_CA_FILE=/var/lib/etcd/ssl/etcd-ca.crt
         ETCD_CERT_FILE=/var/lib/etcd/ssl/etcd-tls.crt
         ETCD_KEY_FILE=/var/lib/etcd/ssl/etcd-tls.key
         ETCD_PEER_CLIENT_CERT_AUTH=true
         ETCD_PEER_TRUSTED_CA_FILE=/var/lib/etcd/ssl/etcd-ca.crt
         ETCD_PEER_CERT_FILE=/var/lib/etcd/ssl/etcd-tls.crt
         ETCD_PEER_KEY_FILE=/var/lib/etcd/ssl/etcd-tls.key
         

Where:

     * `ETCD_HOST`: current `etcd` host.
     * `ETCD_HOST_IP`: current `etcd` host IP.
     * `ETCD_HOST_1`: the name of the first node in the `etcd` cluster.
     * `ETCD_HOST_IP_1`: the IP address of the first node in the `etcd` cluster.
     * `ETCD_HOST_2`: the name of the second node in the `etcd` cluster.
     * `ETCD_HOST_IP_2`: the IP address of the second node in the `etcd` cluster.
     * `ETCD_HOST_3`: the name of the third node in the `etcd` cluster.
     * `ETCD_HOST_IP_3`: the IP address of the third node in the `etcd` cluster.
     * `CLUSTER_NAME`: cluster name as per the control plane.
  4. Configure the firewall to allow TCP communication on ports `2379` and `2380`.

  5. Start etcd:
         
         sudo systemctl enable etcd
         sudo systemctl start etcd
         


**Note:** You can reuse an existing `etcd` setup for AlloyDB Omni. If your `etcd` nodes have SELinux enabled, you must install the `policycoreutils-python-utils` package.

#### Install AlloyDB Omni components on primary instance nodes

  1. On all `primary_instance_nodes`, create a YUM repository configuration file named `/etc/yum.repos.d/alloydb-omni.repo`:
         
         [alloydbomni_core]
         name=AlloyDB Omni Core
         baseurl=ALLOYDB_OMNI_REPOSITORY_URL
         enabled=1
         repo_gpgcheck=0
         gpgcheck=1
         gpgkey=REPO_GPG_KEY
         
         [alloydbomni_common]
         name=AlloyDB Omni Common
         baseurl=ALLOYDB_OMNI_COMMON_REPOSITORY_URL
         enabled=1
         repo_gpgcheck=0
         gpgcheck=1
         gpgkey=REPO_GPG_KEY
         priority=1
         
         [alloydbomni_orchestrator]
         name=AlloyDB Omni Orchestrator
         baseurl=ALLOYDB_OMNI_ORCHESTRATOR_REPOSITORY_URL
         enabled=1
         repo_gpgcheck=0
         gpgcheck=1
         gpgkey=REPO_GPG_KEY
         

  2. Install `alloydbomni18`, `alloydbomni_monitor`, `alloydbomni_node_manager`, and `pgbackrest` on all `primary_instance_nodes`:
         
         sudo dnf install -y alloydbomni18 alloydbomni_monitor alloydbomni_node_manager pgbackrest
         

  3. (Optional) If you don't have load balancer nodes (`load_balancer_nodes`), install `pgbouncer` and `keepalived`:
         
         sudo dnf install -y pgbouncer keepalived
         

  4. Once `alloydbomni_node_manager` is installed, `alloydbomni_node_manager` must be configured before starting the services. Make sure that the deployment specification file (`deployment_spec.yaml`) is copied to all the respective VMs:
         
         sudo /usr/local/bin/alloydbomni_nm_config apply -d deployment_spec.yaml
         




#### Install AlloyDB Omni components on cluster manager nodes

  1. On all cluster manager nodes, create a YUM repository configuration file named `/etc/yum.repos.d/alloydb-orchestrator.repo`:
         
         [alloydbomni_orchestrator]
         name=AlloyDB Omni Orchestrator
         baseurl=ALLOYDB_OMNI_ORCHESTRATOR_REPOSITORY_URL
         enabled=1
         repo_gpgcheck=0
         gpgcheck=1
         gpgkey=REPO_GPG_KEY
         

  2. Install the cluster manager:
         
         sudo dnf install -y alloydbomni_cluster_manager
         

  3. Once `alloydbomni_cluster_manager` is installed and `etcd` is bootstrapped, `alloydbomni_cluster_manager` must be configured before starting the services.
         
         sudo /usr/local/bin/alloydbomni_cm_config apply -d deployment_spec.yaml
         




#### Install AlloyDB Omni components on load balancer nodes

  1. On all load balancer nodes, create a YUM repository configuration file named `/etc/yum.repos.d/alloydb-omni-lb.repo`:
         
         [pgbouncer]
         name=AlloyDB Omni Common
         baseurl=ALLOYDB_OMNI_COMMON_REPOSITORY_URL
         enabled=1
         repo_gpgcheck=0
         gpgcheck=1
         gpgkey=REPO_GPG_KEY
         priority=1
         
         [alloydbomni_node_manager]
         name=AlloyDB Omni Orchestrator
         baseurl=ALLOYDB_OMNI_ORCHESTRATOR_REPOSITORY_URL
         enabled=1
         repo_gpgcheck=0
         gpgcheck=1
         gpgkey=REPO_GPG_KEY
         

  2. Install the load balancer components:
         
         sudo dnf install -y alloydbomni_node_manager keepalived pgbouncer haproxy
         

  3. Once `alloydbomni_node_manager` is installed and `etcd` is bootstrapped, `alloydbomni_node_manager` must be configured before starting the services. Make sure that the deployment specification file (`deployment_spec.yaml`) is copied to all the respective VMs:
         
         sudo /usr/local/bin/alloydbomni_nm_config apply -d deployment_spec.yaml
         




## Summary of installed AlloyDB Omni components

The installation process deploys several key RPM packages depending on the node type:

Node type | Components installed | Notes  
---|---|---  
Primary instance nodes | `alloydbomni18`, `alloydbomni_monitor`, `alloydbomni_node_manager`, `pgbouncer`, `pgbackrest` | Components for the database engine, monitoring, and management.  
Load Balancer nodes | `haproxy` | Optional. Installation skipped if load balancer nodes are not available.  
Cluster manager nodes | `alloydbomni_cluster_manager` | Can be installed on database nodes if no dedicated nodes are available. If cluster manager nodes aren't specified, the cluster manager component is installed on the `primary_instance_nodes`.  
etcd nodes | `etcd` | Can be installed on cluster manager nodes if needed. If etcd nodes aren't specified, `etcd` is installed on the `cluster_manager_nodes`  
  
## Uninstall the components

If you need to remove the AlloyDB Omni installation from your environment—for example, to decommission a cluster or to prepare for a clean reinstallation—then you can uninstall all of its software components. You uninstall AlloyDB Omni using Ansible or by manually removing the RPMs from each node.

### Uninstall AlloyDB Omni components using Ansible

To remove the AlloyDB Omni software stack components using Ansible, use your existing inventory file and a playbook that references the `google.alloydbomni_orchestrator.uninstall` role.

  1. Create a playbook named `uninstall.yaml`.
         
         - name: Uninstall AlloyDB Omni cluster
           hosts: all
           become: true
           vars:
             ansible_user: SSH_USER
             ansible_ssh_private_key_file: SSH_KEY_PATH
           roles:
             - role: google.alloydbomni_orchestrator.uninstall
         

Replace the following:

     * `SSH_USER`: the username that you use to connect to the nodes in your cluster using SSH.
     * `SSH_KEY_PATH`: the path to the SSH private key file on your control node —for example, `~/.ssh/id_rsa`.
  2. Execute the playbook. You must pass `cleanup_data=true` and `cleanup_config=true` as extra variables to remove the configuration files and data directory.
         
         ansible-playbook -i deployment_spec.yaml uninstall.yaml -e "cleanup_data=true cleanup_config=true"
         

**Note:** If the uninstall process fails due to inconsistencies in the cluster state, you can attempt a force uninstall by adding `-e force=true` to the command.



### Uninstall AlloyDB Omni components manually

If you are using the AlloyDB Omni orchestrator CLI, you must manually remove the RPMs from each node.

  1. On all database nodes, run the following command:
         
         sudo dnf remove -y alloydbomni_node_manager alloydbomni18 alloydbomni_monitor pgbackrest keepalived pgbouncer
         

  2. On all load balancer nodes, run the following command:
         
         sudo dnf remove -y alloydbomni_node_manager keepalived haproxy pgbouncer
         

  3. On all cluster manager nodes, run the following command:
         
         sudo dnf remove -y alloydbomni_cluster_manager
         

  4. Optional: On all etcd nodes, run the following command to uninstall etcd and clean etcd data:
         
         sudo dnf remove -y etcd
         sudo rm -rf /var/lib/etcd/data
         




## What's next

  * To bring your own certificate and key files for TLS, see [How AlloyDB Omni uses TLS](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/tls/overview).

  * [Create an AlloyDB Omni cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/create-cluster).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
