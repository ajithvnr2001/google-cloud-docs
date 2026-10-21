---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/read-pool-orchestrator/
title: Create an asynchronous replicated read pool instance using the RPM orchestrator \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:12.671266+00:00
---

# Create an asynchronous replicated read pool instance using the RPM orchestrator  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/read-pool-orchestrator/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Create an asynchronous replicated read pool instance using the RPM orchestrator Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/read-pool-orchestrator)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/read-pool-orchestrator)
  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/read-pool-orchestrator)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/read-pool-orchestrator)

To increase the read throughput and availability of your database cluster, you can create an asynchronous read pool instance. A read pool instance provides a read-only clone of your database instance, ensuring data access even if your database instance becomes unavailable. 

You can define the read pool instance configuration in the database instance's manifest file. Each read pool instance requires creating a unique manifest file. You can deploy multiple read pool instances, with up to 20 read pool nodes total per database cluster.

Each read pool instance occupies the same amount of storage as the instance it replicates.

## Create an asynchronous replicated read pool instance

To create an AlloyDB Omni asynchronous replicated read pool instance, complete the following steps:

  1. Create the database instance manifest to define the read pool instance type:
         
         DBInstance:
           metadata:
             name: READ_POOL_INSTANCE_NAME
           spec:
             instanceType: ReadPool
             nodeCount: READ_POOL_NODE_COUNT
             readPoolPort: READ_POOL_PORT
             dbcParent:
               name: DB_CLUSTER_NAME
         

Replace the following:

     * `READ_POOL_INSTANCE_NAME`: a name for this resource—for example, `read-pool-instance-1`.

     * `DB_CLUSTER_NAME`: the name of the database cluster to which the instance belongs.

     * `READ_POOL_NODE_COUNT`: (Optional) the number of nodes in a read pool instance. This determines the instance's overall computing capacity. You can have a maximum of 20 read pool nodes total per database cluster.

     * `READ_POOL_PORT`: (Optional) the port on the load balancer (VIP) to route read traffic to this read pool instance. Defaults to `5434`.

**Caution:** Creating too many read pool instances in your database cluster might reduce the primary instance's performance.
  2. Apply the `DBInstance` specification.

### `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPECIFICATION_PATH" -r "DBINSTANCE_SPECIFICATION"

Replace the following variables:

     * `DEPLOYMENT_SPECIFICATION_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).

     * `DBINSTANCE_SPECIFICATION`: path to the `DBInstance` manifest file you created in the previous step.

### Ansible
    
    ansible-playbook DBINSTANCE_PLAYBOOK -i "DEPLOYMENT_SPECIFICATION_PATH" \
          -e resource_spec="DBINSTANCE_SPECIFICATION"

Replace the following variables:

     * `DBINSTANCE_PLAYBOOK`: path to the playbook that you created for your `DBInstance` specification.

     * `DEPLOYMENT_SPECIFICATION_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).

     * `DBINSTANCE_SPECIFICATION`: path to the `DBInstance` manifest file you created in the previous step.




## Verify instance status

To verify the availability of the read pool instance, get the status of the `DBInstance` resource:

### `alloydbctl`
    
    
    alloydbctl get -d "DEPLOYMENT_SPECIFICATION_PATH" -t DBInstance -n "READ_POOL_INSTANCE_NAME" -o yaml

Replace the following variables:

  * `DEPLOYMENT_SPECIFICATION_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).

  * `READ_POOL_INSTANCE_NAME`: the name of the read pool instance you specified in the manifest.




### Ansible

Run the `google.alloydbomni_orchestrator.status` playbook. For more information, see [Get cluster status](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/cluster-status#ansible).
    
    
    ansible-playbook STATUS_PLAYBOOK_PATH -i "DEPLOYMENT_SPECIFICATION_PATH" \
          -e resource_type="DBInstance" -e resource_name="READ_POOL_INSTANCE_NAME"

Replace the following variables:

  * `STATUS_PLAYBOOK_PATH`: path to the playbook that you created to get your cluster's status.

  * `DEPLOYMENT_SPECIFICATION_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).

  * `READ_POOL_INSTANCE_NAME`: the name of the read pool instance you specified in the manifest.




Check the `.status.conditions` section of the response for the following:

  * If the `Available` condition's status is `true`, it indicates that the read pool instance can serve queries, but might not be replicating data from your database instance.
  * If the `Streaming` condition's status is `true`, it indicates that the read pool instance is connected to your database instance and actively streaming changes.



When your database instance is unreachable, the read pool instance continues to serve queries. In this case, the availability status will be `true` while the streaming status will be `false`.

After you set up the read pool instance, all inserts, updates, and deletions to rows in your primary database instance become readable on your read pool instance.

## Connect to the read pool instance

After the read pool instance becomes `Available`, the load balancer automatically configures a dedicated read-only frontend that routes traffic to the read pool nodes.

To view the connection endpoint, check `status.endpoints` in the `DBInstance` status output. The read-only endpoint, for example, `VIP_IP:5434`, distributes incoming read-only queries across all healthy nodes in the read pool.

To connect to the read pool instance, use the `psql` client tool with the IP address and port from the endpoint:
    
    
    psql -h VIP_IP -p READ_POOL_PORT -U postgres

Replace the following:

  * `VIP_IP`: the IP address of the read-only endpoint.
  * `READ_POOL_PORT`: the port of the read-only endpoint.



If you attempt to perform write operations against this endpoint, the operations fail immediately with an error indicating that you cannot execute inserts in a read-only transaction.

## Manage the read pool instance

The RPM orchestrator supports dynamic scaling and deletion of read pool instances with zero cluster downtime.

### Scale a read pool instance

To add or remove nodes from an existing read pool, update the `nodeCount` field in your `DBInstance` manifest file.

  1. Open your `DBInstance` manifest file and modify the `nodeCount` value to reflect the selected number of nodes.

  2. Apply the updated manifest using your preferred deployment method, the `alloydbctl apply` command or your Ansible playbook.




The RPM orchestrator automatically provisions or removes the read replica nodes, and the load balancer dynamically updates to route traffic to the available nodes in the pool.

### Delete a read pool instance

To delete a read pool instance, use the `alloydbctl delete` command:
    
    
    alloydbctl delete -t DBInstance -n READ_POOL_INSTANCE_NAME

Replace `READ_POOL_INSTANCE_NAME` with the name of the read pool instance you want to delete.

When you delete a read pool instance, the orchestrator stops the read replica service and cleans up the nodes. The load balancer automatically removes the routing without causing any promotion deadlocks or impacting traffic to your primary or standby instances.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
