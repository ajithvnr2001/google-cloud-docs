---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/update-redhat-orchestrator/
title: Update your RPM orchestrator cluster components \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:17:22.138768+00:00
---

# Update your RPM orchestrator cluster components  |  AlloyDB Omni using the RPM orchestrator: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/update-redhat-orchestrator/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/overview)



Send feedback 

#  Update your RPM orchestrator cluster components Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/update-redhat-orchestrator)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/update-redhat-orchestrator)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/update-redhat-orchestrator)

This page describes how to update your AlloyDB Omni database cluster software packages, resource configurations, and the RPM orchestrator in Red Hat Enterprise Linux (RHEL) environments. 

## Before you begin

Make sure that you have the deployment specification file, `deployment_spec.yaml`, which contains all your node and cluster components details.

## Upgrade the orchestrator

The orchestrator manages your database clusters. You must upgrade the orchestrator on your control node before upgrading the other cluster components.

###  Ansible 

If you manage your infrastructure by using Ansible playbooks, complete the following steps:

  1. Check the installed version of the `google.alloydbomni_orchestrator` collection on your control node by running the following command:
         
         ansible-galaxy collection list | grep alloydbomni_orchestrator

  2. To overwrite your existing version, download the latest stable release of the collection tar file and perform a forced installation:
         
         ansible-galaxy collection install --force google-alloydbomni_orchestrator-NEW_VERSION.tar.gz

Replace `NEW_VERSION` with the version of the new collection.




###  alloydbctl 

If you use the `alloydbctl` command-line tool, complete the following steps:

  1. To check the installed package version of the RPM orchestrator `alloydbomni_orchestrator` on your control node, run the following command:
         
         rpm -q alloydbomni_orchestrator

  2. Upgrade the software package on your control node by using the package manager:
         
         sudo dnf upgrade alloydbomni_orchestrator




## Update cluster components using Ansible

Google recommends that you update by using the provided Ansible role.

  1. Create a playbook named `update.yaml` that references the `update` role from the orchestrator collection. You must set the `update_action` parameter value to `update_rpm`.

By default, the `update` role updates both control plane and data plane. To update only control or data plane components, set the parameter for the other plane to `false`.
         
         ---
         - hosts: all
           become: true
           vars:
             update_action: "update_rpm"
             ansible_user: SSH_USER
             ansible_ssh_private_key_file: PRIVATE_KEY_PATH
             update_control_plane: true # Optional argument if you want to only update data plane components
             update_data_plane: true # Optional argument if you want to only update control plane components
           roles:
             - role: google.alloydbomni_orchestrator.update
         

Replace the following:

     * `SSH_USER`: the SSH username that has access to your cluster nodes.
     * `PRIVATE_KEY_PATH`: the path to your private SSH key file.
     * `update_action`: the scope of the update. Set this value to `update_rpm`.
     * `update_control_plane`: optional. Set to `false` to update only data plane components. The default is `true`.
     * `update_data_plane`: optional. Set to `false` to update only control plane components. The default is `true`.
  2. To perform an update across all specified nodes, run the playbook with your inventory file:
         
         ansible-playbook -i DEPLOYMENT_SPEC update.yaml

Replace `DEPLOYMENT_SPEC` with the path to your deployment specification file.

Make sure that your deployment specification file defines the installed version for each component in your cluster. The update role updates components based on how you configure their versions in the inventory file:

     * If a component's version matches the installed version, the update role makes no changes to that component.
     * If you change a component's version to a specific target version, it updates the component to that version.
     * If you leave a component's version field empty, it updates the component to the latest available version in the configured repository.

**Note:** If a package update fails during an Ansible-triggered orchestration process, the AlloyDB Omni orchestrator Ansible role uses built-in transactional integrity to recover. Before the Ansible role executes the update, it automatically captures the existing package versions. If the update fails, the Ansible role block and rescue structures automatically downgrade to the previously installed package version. In high availability (HA) topologies, this recovery process carefully bypasses primary nodes if standbys fail, or executes HA switchovers if primary nodes fail. This helps maintain cluster stability and avoid downtime.

## Update cluster components manually

If you are not using the Ansible orchestrator or if you want granular control over the update process, you can update RPM components manually for each node in your cluster. It is recommended to perform software updates during the scheduled maintenance window.

The manual update process involves updating the following two planes:

  * Control plane (RPM orchestrator components): The control plane is the layer that controls and manages your database clusters. In an RPM deployment, the control plane includes the `cluster_manager`, `node_manager`, and `etcd`.

  * Data plane (Database cluster): The data plane contains the database cluster components, including the AlloyDB Omni database engine itself, `monitor`, as well as services such as `pgBackRest`, `PgBouncer`, `keepalived`, and `HAProxy`. Upgrading the data plane applies database version updates, security patches, and performance improvements directly to your database clusters.




Regardless of your reference architecture, the steps to update the control plane remain the same. You must update the control plane components before you update the data plane. The steps to update your data plane differ based on your database deployment architecture.

To update a service or package, perform the following steps:

  1. Stop the service:
         
         sudo systemctl stop SERVICE

  2. Upgrade the package by using one of the following commands:

     * To update to the latest available version:
           
           sudo dnf upgrade PACKAGE

     * To update to a specific version:
           
           sudo dnf upgrade PACKAGE-VERSION

  3. Start the service:
         
         sudo systemctl start SERVICE




Replace the following:

  * `SERVICE`: the name of the service to stop and start, for example `pgbouncer` or `keepalived`.
  * `PACKAGE`: the name of the package to update, for example `pgbouncer` or `alloydbomni18`.
  * `VERSION`: the target package version to install, for example `18.3.0` or `18.3.0-2.rhel9`.



### Update the control plane manually

To update the control plane, perform the following steps on the designated nodes:

  1. To stop the cluster manager on all cluster manager nodes, run the following command:

**Note:** Before updating other control plane components, stop the cluster manager on all cluster manager nodes.
         
         sudo systemctl stop alloydbomni_cluster_manager

  2. To update `etcd` on all DCS nodes, run the following commands in sequence:
         
         sudo systemctl stop etcd
         sudo dnf upgrade etcd
         sudo systemctl start etcd

  3. To update the node manager on all nodes, run the following commands in sequence:
         
         sudo systemctl stop alloydbomni_node_manager
         sudo dnf upgrade alloydbomni_node_manager
         sudo systemctl start alloydbomni_node_manager

  4. After updating the control plane components, you can update the cluster manager on all cluster manager nodes, and restart it if necessary.
         
         sudo dnf upgrade alloydbomni_cluster_manager
         sudo systemctl start alloydbomni_cluster_manager




### Update the data plane manually

To update the data plane, update the database and helper services in the order specified for your deployment architecture. For each service, you must follow a strict sequence of stopping the service, upgrading the package, and starting the service.

Follow the instructions for your deployment depending on the reference architecture.

  1. Retrieve your cluster status using the `alloydbctl get` command and set the output format to YAML:
         
         alloydbctl get -d DEPLOYMENT_SPEC -t RESOURCE_TYPE -n CLUSTER_NAME -o yaml

Replace the following:

     * `RESOURCE_TYPE`: the resource type to inspect, for example `DBCluster`.
     * `CLUSTER_NAME`: the name of your database cluster.
     * `DEPLOYMENT_SPEC`: the path to your deployment specification file.
  2. In the YAML output, note the `instanceList` under the `status` section.

Find the node that has its role set to `Primary`. All other database nodes are your standby nodes.

  3. Update all data plane components running on standby nodes first and then update those components on the primary node. Use the following steps to update the data plane components on each node.

     1. To update AlloyDB Omni, run the following commands in sequence:
            
            sudo systemctl stop alloydbomni18
            sudo dnf upgrade alloydbomni18
            sudo systemctl start alloydbomni18

**Note:** To step down the active primary node safely, perform a switchover. For more information, see [Perform a switchover](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/manage-high-availability#perform-switchover).
     2. To update the monitor, run the following commands in sequence:
            
            sudo systemctl stop alloydbomni_monitor
            sudo dnf upgrade alloydbomni_monitor
            sudo systemctl start alloydbomni_monitor

     3. To update pgBackRest, run the following commands in sequence:
            
            sudo dnf upgrade pgbackrest

     4. To update PgBouncer, run the following commands in sequence:
            
            sudo systemctl stop pgbouncer
            sudo dnf upgrade pgbouncer
            sudo systemctl start pgbouncer

     5. To update keepalived, run the following commands in sequence:
            
            sudo systemctl stop keepalived
            sudo dnf upgrade keepalived
            sudo systemctl start keepalived

**Note:** If your reference architecture includes load balancers, then `keepalived` and `pgbouncer` run on the load balancer nodes. Update these components on the standby load balancer nodes first, and then update them on the primary load balancer node.
     6. To update HAProxy, run the following commands in sequence:
            
            sudo systemctl stop haproxy
            sudo dnf upgrade haproxy
            sudo systemctl start haproxy




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
