---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/manage-high-availability/
title: Manage high availability \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:54:04.891155+00:00
---

# Manage high availability  |  AlloyDB Omni using the RPM orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/manage-high-availability/

This page documents AlloyDB Omni version **18.1.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview)



Send feedback 

#  Manage high availability Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/manage-high-availability)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/manage-high-availability)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/manage-high-availability)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/manage-high-availability)

Manage high availability for your AlloyDB Omni clusters to add resilience to outages and failures through automated failovers and recovery mechanisms. 

## Configure high availability specification

To configure high availability, fill out the following information in your `DBCluster` specification:
    
    
    DBCluster:
      metadata:
        ...
      spec:
        ...
        readOnlyPort: READ_ONLY_PORT
        availability:
          numberOfStandbys: NUMBER_OF_STANDBYS
          enableStandbyAsReadReplica: true
          enableAutoFailover: true
          enableAutoHeal: true
          replayReplicationSlotsOnStandbys: true
          healthcheckPeriodSeconds: HEALTHCHECK_PERIOD
          autoFailoverTriggerThreshold: AUTOFAILOVER_TRIGGER_THRESHOLD
          autoHealTriggerThreshold: AUTOHEAL_TRIGGER_THRESHOLD
    

Replace the following variables:

  * `NUMBER_OF_STANDBYS`: number of standby nodes to set up. Setting this value to `0` disables high availability. The maximum value is `5`. If you're not sure how many standby nodes you need, start with `2` for high resiliency.

  * (Optional) `READ_ONLY_PORT`: the port on the load balancer or virtual IP address used for the standby read-only endpoint. The default value is `5433` (primary port plus 1).

  * (Optional) `HEALTHCHECK_PERIOD`: number of seconds to wait between each health check. The default value is `30`. The minimum value is `1`. The maximum value is `86400` (one day).

  * (Optional) `AUTOFAILOVER_TRIGGER_THRESHOLD`: number of times the health check can fail before a failover occurs. The default value is `3`. The minimum value is `0`, but if the value is set to `0`, AlloyDB Omni uses the default value.

An automatic failover occurs if the health check fails `AUTOFAILOVER_TRIGGER_THRESHOLD` times or for `HEALTHCHECK_PERIOD * AUTOFAILOVER_TRIGGER_THRESHOLD` seconds (90 seconds by default).

  * (Optional) `AUTOHEAL_TRIGGER_THRESHOLD`: number of times the health check can fail before auto-heal begins. The default value is `5`. The minimum value is `0`, but if the value is set to `0`, AlloyDB Omni uses the default value.

An automatic recovery occurs if the health check fails `AUTOHEAL_TRIGGER_THRESHOLD` times or for `HEALTHCHECK_PERIOD * AUTOHEAL_TRIGGER_THRESHOLD` seconds.




### Verify read-only standby endpoints

When you set `enableStandbyAsReadReplica: true`, the load balancer (HAProxy and Keepalived virtual IP address) automatically exposes a dedicated read-only endpoint in addition to the primary read-write endpoint.

HAProxy routes traffic across active standbys as follows:

  * Runs health checks on all standby nodes using `GET /isstandby`.
  * Distributes read queries across active standbys using `leastconn` load balancing.
  * Automatically updates routing upon failover without dropping client connections to the new standby topology.



To verify your cluster endpoints, run one of the following commands:

### `alloydbctl`
    
    
    alloydbctl get -d "DEPLOYMENT_SPEC" -t DBCluster -n DBCLUSTER_NAME

Replace the following variables:

  * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

  * `DBCLUSTER_NAME`: name of your database cluster that you defined in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster).




### Ansible

  1. Create an Ansible playbook for the `google.alloydbomni_orchestrator.status` role. For example, `status.yaml`:
         
         - name: STATUS_PLAYBOOK_NAME
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
           - role: google.alloydbomni_orchestrator.status
         

Replace the following variables:

     * `STATUS_PLAYBOOK_NAME`: name of your Ansible playbook. For example, `My cluster status`.

     * `ANSIBLE_USER`: OS user that Ansible uses to log into your AlloyDB Omni nodes.

     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

  2. Run the playbook:
         
         ansible-playbook status.yaml -i "DEPLOYMENT_SPEC" -e resource_type=DBCluster \
           -e resource_name=DBCLUSTER_NAME

Replace the following variables:

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

     * `DBCLUSTER_NAME`: name of your database cluster that you defined in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster).




The endpoints are reported under `status.primary.endpoints`:
    
    
        - Read-Write: VIRTUAL_IP:5432
        - Read-Only: VIRTUAL_IP:5433
    

## Apply your `DBCluster` specification

To apply your configured `DBCluster` specification, run one of the following command:

### `alloydbctl`
    
    
    alloydbctl apply -d "DEPLOYMENT_SPEC" -r "DBCLUSTER_SPECIFICATION"

Replace the following variables:

  * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

  * `DBCLUSTER_SPECIFICATION`: path to the `DBCluster` specification you created in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster).




### Ansible
    
    
    ansible-playbook DBCLUSTER_PLAYBOOK -i "DEPLOYMENT_SPEC" \
          -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following variables:

  * `RESTORE_PLAYBOOK`: path to the playbook that you created for your `DBCluster` CRD.

  * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

  * `DBCLUSTER_SPECIFICATION`: path to the `DBCluster` specification you created in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster).




## Switchover to a standby instance

You can perform switchovers when you need to test your high availability setup or any other planned maintenance activities that require switching the primary and standby replica. Once the switchover occurs, the direction of replication and roles of the primary and standby are reversed.

Switchovers perform the following actions:

  1. AlloyDB Omni orchestrator takes the primary offline.

  2. AlloyDB Omni orchestrator promotes the standby to be the new primary.

  3. AlloyDB Omni orchestrator converts the primary into a standby.

  4. AlloyDB Omni starts the newly-converted standby.




### Perform a switchover

To perform a switchover, complete the following steps:

  1. Verify that your primary and standby instances are healthy.

  2. Verify that the high availability `status.phase` is `Ready`.

### `alloydbctl`
         
         alloydbctl get -d "DEPLOYMENT_SPEC" -t DBCluster -n DBCLUSTER_SPECIFICATION -o yaml

Replace the following variables:

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

     * `DBCLUSTER_SPECIFICATION`: name of your `DBCluster` specification that you defined in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster).

### Ansible
    
    ansible-playbook status.yaml -i DEPLOYMENT_SPEC -e resource_type=DBCluster \
      -e resource_name=DBCLUSTER_SPECIFICATION

Replace the following variables:

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

     * `DBCLUSTER_SPECIFICATION`: name of your `DBCluster` specification that you defined in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster).

  3. Create a `Switchover` specification using the following format:
         
         Switchover:
           metadata:
             name: SWITCHOVER_NAME
           spec:
             dbClusterRef: DBCLUSTER_NAME
             newPrimary: NEW_PRIMARY_NAME
         

Replace the following variables:

     * `SWITCHOVER_NAME`: name for this `Switchover` specification. For example, `my-switchover-1`. This name must be unique every time a switchover is performed.

     * `DBCLUSTER_NAME`: name of your database cluster that you defined in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster).

     * (Optional) `NEW_PRIMARY_NAME`: is the standby instance that becomes the new primary. To map the instance name to a host, see the `instanceList` field in the status of the referenced `DBCluster`.

  4. If you're using Ansible, create a playbook for your `Switchover` specification.
         
         - name: SWITCHOVER_PLAYBOOK_NAME
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
           - role: google.alloydbomni_orchestrator.switchover
         

Replace the following variables:

     * `SWITCHOVER_PLAYBOOK_NAME`: name of your Ansible playbook. For example, `My Switchover`.

     * `ANSIBLE_USER`: OS user that Ansible uses to log into your AlloyDB Omni nodes.

     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

  5. Apply your `Switchover` specification.

### `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPEC" -r "SWITCHOVER_SPECIFICATION"

Replace the following variables:

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

     * `SWITCHOVER_SPECIFICATION`: path to the `Switchover` specification you created in step three.

### Ansible
    
    ansible-playbook SWITCHOVER_PLAYBOOK -i "DEPLOYMENT_SPEC" \
      -e resource_spec="SWITCHOVER_SPECIFICATION"

Replace the following variables:

     * `SWITCHOVER_PLAYBOOK`: path to the playbook that you created for your `Switchover` CRD in step four.

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

     * `SWITCHOVER_SPECIFICATION`: path to the `Switchover` specification you created in step three.




## Load balancer for high availability

The load balancer (HAProxy) achieves high availability by pairing its nodes with Keepalived and a virtual IP. Keepalived utilizes the Virtual Router Redundancy Protocol (VRRP) to control a floating, virtual IP. Database client applications connect to this virtual IP instead of the database node's IP address.

In configurations where a dedicated load balancer isn't used, Keepalived is installed directly on the database nodes. In this scenario, high availability is achieved by dynamically assigning the virtual IP to the current primary node, ensuring seamless failover if the primary becomes unavailable.

To establish a stable election, Keepalived assigns VRRP priorities to the database cluster nodes. The first load balancer node assumes the primary role with a higher Keepalived priority— for example, `110`. Subsequent nodes act as secondaries with a lower priority— for example, `100`.

To ensure that the virtual IP points to a healthy node, Keepalived runs continuous health checks every two seconds. This verifies the state of the `systemd` HAProxy process. If the HAProxy service on the primary fails, Keepalived migrates the virtual IP to a healthy secondary node.

If the database node's membership changes, HAProxy and Keepalived automatically point to the new active database nodes. The underlying routing configuration updates without dropping live client connections.

### Configure the load balancer

**Note:** If you are using a Google Cloud environment, replace `onprem` with `gcp` under `dbLoadBalancerOptions`. You must choose either `gcp` or `onprem`. If you specify both `gcp` and `onprem`, you get an error when you apply the configuration.

To configure the virtual IP for the load balancer nodes, add the following `dbLoadBalancerOptions` field to the `primarySpec` field in your `DBCluster` specification:
    
    
    DBCluster:
      spec:
        primarySpec:
          ...
          dbLoadBalancerOptions:
            onprem:
              loadBalancerIP: "VIRTUAL_IP"
              loadBalancerType: "internal"
              loadBalancerInterface: "VIRTUAL_IP_INTERFACE"
    

Replace the following variables:

  * `VIRTUAL_IP`: static IP address used for the floating, virtual IP. Database client applications use the IP address defined here. To ensure that Keepalived can broadcast gratuitous ARPs successfully, this IP address must be available; can't loopback; and in the case of on-premises, belongs to the same subnet as your primary node interfaces.

  * `VIRTUAL_IP_INTERFACE`: network interface where `VIRTUAL_IP` is configured. The default value is `eth0`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
