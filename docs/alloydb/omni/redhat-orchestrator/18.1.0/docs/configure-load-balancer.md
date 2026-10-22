---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-load-balancer/
title: Configure the load balancer \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:08.739851+00:00
---

# Configure the load balancer  |  AlloyDB Omni using the RPM orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-load-balancer/

This page documents AlloyDB Omni version **18.1.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview)



Send feedback 

#  Configure the load balancer Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/configure-load-balancer)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/configure-load-balancer)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/configure-load-balancer)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/configure-load-balancer)

You can configure a load balancer for AlloyDB Omni using the RPM orchestrator. 

## Limitations

The following limitations apply:

  * The endpoint is limited to the ReadWrite endpoint. Readonly endpoints will be supported in future.



## Before you begin

Before you configure the load balancer, make sure that you meet the following requirements:

  * To define load balancer nodes, in your deployment specification file, include a `load_balancer_nodes` group that contains the hostnames or IP addresses of your dedicated load balancer VMs:
        
        alloydbomni:
          vars:
            ...
          children:
            **load_balancer_nodes :
              hosts:
                lb-node-1:
                lb-node-2:**
        

  * To configure the firewall, allow the following incoming traffic:

    * On dedicated load balancer VMs:

      * Port `5432` (TCP): for HAProxy database traffic.

      * Port `6432` (TCP): for PgBouncer connection pooling traffic, if applicable.

      * VRRP protocol: for `keepalived` leader election and health checks.

    * On database nodes:

      * Port `8086` (HTTP): for load balancer health checks.
  * If you're using the Google Cloud environment, then set `ENVIRONMENT_TYPE` to `gcp`. Then you must authenticate your gcloud CLI account by running `gcloud auth login` as the `root` user. Additionally, the authenticated account must have the following permissions:

    * `compute.instances.get`
    * `compute.instances.list`
    * `compute.instances.updateNetworkInterface`



## Configure the load balancer

The RPM orchestrator uses HAProxy to distribute traffic and Keepalived to provide high availability with a virtual IP (VIP).

### Update the resource specification

In your `DBCluster` specification file, add `dbLoadBalancerOptions`, which makes sure that the cluster manager and orchestrator know how to manage the load balancer endpoints.
    
    
    DBCluster:
      metadata:
        name: DBCLUSTER_NAME
      spec:
        primarySpec:
          # ... other primary settings ...
          **dbLoadBalancerOptions :
            ENVIRONMENT_TYPE::
              loadBalancerIP: "VIRTUAL_IP"
              loadBalancerType: "internal"
              loadBalancerInterface: "VIRTUAL_IP_INTERFACE"**
    

Replace the following:

  * `ENVIRONMENT_TYPE`: determines the environment where cluster is set up—`onprem` or `gcp`.

  * `DBCLUSTER_NAME`: the name of your AlloyDB Omni database cluster—for example, `my-db-cluster`.

  * `VIRTUAL_IP`: static IP address used for the floating, virtual IP. Database client applications use the IP address defined here. To make sure that Keepalived can broadcast Gratuitous Address Resolution Protocols (GARPs) successfully, this IP address must meet the following conditions: it must be available; it can't loopback; and in the case of on-premises, it belongs to the same subnet as your primary node interfaces.

  * `VIRTUAL_IP_INTERFACE`: network interface where `VIRTUAL_IP` is configured. The default value is `eth0`.




## Apply the configuration

Apply the configuration changes using your preferred orchestrator interface.

###  Ansible 

Run the bootstrap playbook using your inventory and resource specification files:
    
    
    ansible-playbook DBCLUSTER_PLAYBOOK -i "DEPLOYMENT_SPECIFICATION" \
          -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following variables:

  * `DBCLUSTER_PLAYBOOK`: path to the playbook that you created for your database cluster in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster).

  * `DEPLOYMENT_SPECIFICATION`: path to the deployment specification that you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

  * `DBCLUSTER_SPECIFICATION`: path to your cluster specifications.




###  `alloydbctl`

Apply the resource and deployment specifications:
    
    
    alloydbctl apply -d "DEPLOYMENT_SPECIFICATION" -r "DBCLUSTER_SPECIFICATION"

Replace the following variables:

  * `DEPLOYMENT_SPECIFICATION`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

  * `DBCLUSTER_SPECIFICATION`: path to your cluster specifications.




## Verify the load balancer

After the RPM orchestrator completes the setup, verify that you can connect to the database cluster using the VIP:
    
    
    psql -h VIRTUAL_IP -U postgres

Replace `VIRTUAL_IP` with the IP address you configured in the `loadBalancerIP` field.

The load balancer automatically routes your connection to the current primary node.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
