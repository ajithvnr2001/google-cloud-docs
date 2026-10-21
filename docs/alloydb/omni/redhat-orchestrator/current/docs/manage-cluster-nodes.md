---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/manage-cluster-nodes/
title: Manage cluster nodes in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: Current (18.3.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:54:01.156554+00:00
---

# Manage cluster nodes in AlloyDB Omni  |  AlloyDB Omni using the RPM orchestrator: Current (18.3.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/manage-cluster-nodes/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview)



Send feedback 

#  Manage cluster nodes in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/manage-cluster-nodes)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/manage-cluster-nodes)

This page describes how to add or remove database nodes in an existing AlloyDB Omni cluster using the RPM orchestrator. 

You can add standby nodes to an existing cluster to scale your read workloads or increase high availability. You can also remove specific database nodes for targeted maintenance or permanent decommissioning to reduce cluster capacity.

## Before you begin

  * Make sure [your cluster is in a healthy state](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18-next/docs/cluster-status) and that `status.phase` is `Ready`.
  * If you add a new node, verify that it meets the [System requirements](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview#requirements) and has the required AlloyDB Omni components installed.



## Add a database node

To add a new standby database node to your cluster, you must update both your deployment specification, also known as the inventory, and your database cluster resource specification.

  1. To update the deployment specification, open your `deployment_spec.yaml` file and add the new node's IP address or hostname under the `primary_instance_nodes` group.
         
         alloydbomni:
           children:
             primary_instance_nodes:
               hosts:
                 db-node-1:
                 db-node-2:
                 NEW_NODE:
         

Replace `NEW_NODE` with the IP address or hostname of the new standby node that you are adding.

  2. To update the resource specification, open your `DBCluster` resource specification file and increment the `numberOfStandbys` value by the number of nodes you are adding:
         
         DBCluster:
           metadata:
             name: DB_CLUSTER_NAME
           spec:
             # Other configurations omitted for brevity.
             # Modify the availability block in your existing DBCluster resource spec:
             availability:
               numberOfStandbys: NEW_STANDBY_COUNT
             # Remaining configurations omitted.
         

Replace the following variables:

     * `DB_CLUSTER_NAME`: the name of your database cluster.
     * `NEW_STANDBY_COUNT`: the new, incremented total number of standby nodes in your cluster.
  3. Apply the updated resource specifications using either of the following methods. The RPM orchestrator automatically provisions the new node:

###  `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "DBCLUSTER_SPECIFICATION"

###  Ansible 

To apply the changes using Ansible, complete the following steps:

     1. Create an `add.yml` playbook with the following content:
            
            ---
            # Add AlloyDB Omni database nodes
            - name: Add AlloyDB Omni database nodes
              hosts: all
              become: true
              vars:
                ansible_user: ANSIBLE_USER
                ansible_ssh_private_key_file: PRIVATE_SSH_KEY_PATH
            
              roles:
                - role: google.alloydbomni_orchestrator.add
            

Replace the following variables:

        * `ANSIBLE_USER`: the user with passwordless access to all nodes and `sudo` permissions.
        * `PRIVATE_SSH_KEY_PATH`: the path to the private SSH key for passwordless authentication.
     2. Run the created playbook:
            
            ansible-playbook -i "DEPLOYMENT_SPEC_PATH" add.yml \
              -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following variables:

     * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
     * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` manifest that you modified.



## Remove a specific database node

To remove a specific standby node from your cluster, you must remove it from the deployment specification and decrement the standby count.

**Note:** The following restrictions apply when removing a database node:

  * Standby nodes: You can only remove standby nodes. You cannot directly remove the primary database node. To identify the primary node, fetch [your cluster status](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18-next/docs/cluster-status) and check the IP address or hostname returned in the `.status.primary.endpoint` field. If you need to remove a primary node, you must [perform a manual switchover](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18-next/docs/manage-high-availability#switchover) first, and then remove the old primary node.
  * High availability (HA) clusters: You cannot remove a node from a standalone cluster. To remove a standalone node, you must delete the entire database cluster instead.



  1. To update the deployment specification, open your `deployment_spec.yaml` file and remove the target node's IP address or hostname from the `primary_instance_nodes` group.

  2. To update the resource specification, open your `DBCluster` resource specification file and decrement the `numberOfStandbys` value:
         
         DBCluster:
           metadata:
             name: DB_CLUSTER_NAME
           spec:
             # Other configurations omitted for brevity.
             # Modify the availability block in your existing DBCluster resource spec:
             availability:
               numberOfStandbys: NEW_STANDBY_COUNT
             # Remaining configurations omitted.
         

Replace the following variables:

     * `DB_CLUSTER_NAME`: the name of your database cluster.
     * `NEW_STANDBY_COUNT`: the new, decremented total number of standby nodes in your cluster.
  3. Apply the updated manifests using either of the following methods:

###  `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "DBCLUSTER_SPECIFICATION"

###  Ansible 

To apply the changes using Ansible, complete the following steps:

     1. Create a `remove.yml` playbook with the following content:
            
            ---
            # Scale-in database nodes from AlloyDB Omni cluster
            - name: Scale-In AlloyDB Omni Cluster (Logical Discovery & De-registration)
              hosts: all
              become: true
              vars:
                ansible_user: ANSIBLE_USER
                ansible_ssh_private_key_file: PRIVATE_SSH_KEY_PATH
              roles:
                - role: google.alloydbomni_orchestrator.remove
            

Replace the following variables:

        * `ANSIBLE_USER`: the user with passwordless access to all nodes and `sudo` permissions.
        * `PRIVATE_SSH_KEY_PATH`: the path to the private SSH key for passwordless authentication.
     2. Run the playbook:
            
            ansible-playbook -i "DEPLOYMENT_SPEC_PATH" remove.yml \
              -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following variables:

     * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
     * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` manifest that you modified.
  4. Optional: Clean up the components on the removed node.

###  `alloydbctl`

Manually uninstall the AlloyDB Omni components to clean up the removed node.

###  Ansible 

The Ansible orchestrator automatically cleans up the following components on the VM, if they are present:

     * AlloyDB Omni
     * AlloyDB Omni Monitor
     * Node Manager
     * `pgBackRest`
     * `PgBouncer`
     * `Keepalived`




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
