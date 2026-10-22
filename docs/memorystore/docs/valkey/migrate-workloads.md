---
url: https://docs.cloud.google.com/memorystore/docs/valkey/migrate-workloads/
title: Migrate your Redis and Valkey workloads into Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:28.953978+00:00
---

# Migrate your Redis and Valkey workloads into Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/migrate-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Migrate your Redis and Valkey workloads into Memorystore for Valkey Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore supports the automated migration of your self-managed Redis and Valkey workloads into Memorystore for Valkey. Using this feature lets you seamlessly transition from the operational burden of managing your own infrastructure. By migrating to a fully managed environment in Memorystore for Valkey, you eliminate the need for manual OS patching, replication setup, and custom backup scripts, while gaining automatic failover and VPC-native security capabilities, and the ability to scale to hundreds of nodes with a near-zero downtime.

By migrating your self-managed workloads into Memorystore for Valkey, you unlock the following advantages that eliminate operational toil and modernize your database infrastructure:

  * **Eliminate your operational overhead** : offload manual and time-consuming tasks to Google Cloud, such as OS patching, infrastructure monitoring, backup scripts, and replication management. As a result, you can focus on application development instead of database maintenance.
  * **Achieve enterprise-grade high availability** : benefit from a fully managed 99.99% SLA. Memorystore for Valkey provides automatic failover, and built-in backup and restore capabilities. This protects your applications from unexpected node failures and ensures a rapid disaster recovery.
  * **Scale with a near-zero downtime** : scale your instances in or out to match unpredictable traffic spikes dynamically. You can expand to hundreds of nodes (up to 250 shards) seamlessly without taking your applications offline.
  * **Enhance your security** : replace complex, manually configured network rules with secure, built-in VPC connectivity and granular Identity and Access Management (IAM)-based access controls. This ensures that Google Cloud's strict security boundaries protect your data.
  * **Consolidate and upgrade your instances** : merge your scattered, siloed, and self-managed instances into a single, high-performance deployment in Memorystore for Valkey effortlessly. As part of this migration, you can also upgrade your outdated Redis or Valkey versions to the latest supported releases automatically.
  * **Unlock advanced real-time analytics and GenAI** : transition to an optimized environment that delivers microsecond latencies for caching and session management. To power your generative AI (GenAI) applications, you gain immediate, managed access to advanced features like Vector Search.



## Version support

The table in this section lists the following information about your source Redis and Valkey self-managed instances, and the target instances in Memorystore for Valkey:

  * The types and versions of the source instances that the migration supports
  * The versions of the target Memorystore for Valkey instances into which you can migrate your workloads

**Source instance type** | **Source instance version** | **Target instance version**  
---|---|---  
Redis | 3.2.x - 7.2.x | Valkey 7.2, 8.0, 9.0, and 9.1  
Valkey | 7.x, 8.x, and 9.x | Valkey 7.2, 8.0, 9.0, and 9.1  
**Important** : The version of the target instance _must_ either be the same or a later version than the version of the source instance. You can't downgrade the target instance to an earlier version.

## Before you begin

Before you begin to migrate your workloads, complete the prerequisites in this section.

### Use the Google Cloud console, Google Cloud CLI, and APIs

To use the Google Cloud console, gcloud CLI, and APIs, do the following:

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

[Go to the project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  3. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI.

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. You need at least gcloud CLI version `489.0.0` to access the Memorystore for Valkey gcloud CLI commands.

  4. Enable the Memorystore for Valkey API.   
[Memorystore for Valkey API](https://console.cloud.google.com/apis/library/memorystore.googleapis.com)
  5. Enable the Network Connectivity API.   
[Network Connectivity API](https://console.cloud.google.com/apis/library/networkconnectivity.googleapis.com)
  6. Enable the Service Consumer Management API.   
[Service Consumer Management API](https://console.cloud.google.com/apis/library/serviceconsumermanagement.googleapis.com)
  7. Enable the Compute Engine API.   
[Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com)



### Assign roles and permissions

To perform all operations for migrating the workloads of your self-managed Redis and Valkey instances into Memorystore for Valkey, ask your administrator to grant you the [Memorystore Admin ](https://docs.cloud.google.com/memorystore/docs/valkey/access-control#predefined_roles) (`roles/memorystore.admin`) IAM role on your Google Cloud project.

To create and view network attachments, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project.

## Workflow to migrate your workloads

To migrate the workloads of your self-managed Redis and Valkey instances into Memorystore for Valkey, perform the following actions:

  1. **Prepare your source instance**: configure your self-managed Redis or Valkey instance to allow secure connections and outbound replication to Memorystore for Valkey.
  2. **Prepare the target instance**: determine your required instance specifications, such as shard count and node type.
  3. **Create the target instance**: provision the Memorystore for Valkey instance that receives your migrated data.
  4. **Configure a network attachment**: set up a network attachment. This attachment lets the target instance in the producer VPC network initiate connections to the source instance that's running in the consumer VPC network. As a result, replication is established.
  5. **Start the migration**: initiate the synchronization process. The target instance connects to your source instance automatically and begins to replicate your data as a read replica continuously.
  6. **Monitor the migration**: verify that the migration is progressing without issues and that the status of the migration is **HEALTHY**.
  7. **Finish the migration**: cut over your application traffic to the target instance.



## Prepare your source instance

You must prepare your self-managed Redis or Valkey instance so that you can migrate your workloads into a target Memorystore for Valkey instance.

To allow connections from the nodes of the target instance to the nodes of the source instance, do the following:

  * If the **protected-mode** is enabled on the source nodes, then deactivate it.
  * If you configured the source nodes with an explicit `bind` directive, then update the nodes to allow incoming connections from the target nodes. The target nodes initiate connections from the IP addresses in the network attachment's subnet.
  * Update any firewall rules that might block incoming connections from the target nodes.
  * If authentication and Transport Layer Security (TLS) are enabled on the source nodes, then deactivate them.



To enable replication to be established from the nodes of the target instance to the nodes of the source instance, do the following:

  * Don't rename any Valkey or Redis commands that perform data modification or used for replication (for example, `PING`, `PSYNC`, and `HSET`).
  * If you use access control lists (ACL) for your instance, then allow the following commands for the `default` user so that the target instance can establish replication: 
    * `REPLCONF`
    * `SYNC`
    * `PSYNC`
    * `PING`
    * `INFO`
    * `CLUSTER|NODES`
  * Ensure that the source instance possesses enough memory and CPU capacity to manage the additional replication load that originates from the nodes of the target instance.



**Important** : Make a note of the IP address and port number of the source instance. You need this information to start the migration process.

Also, Memorystore for Valkey must be able to communicate with this IP address and port throughout the migration process. Memorystore for Valkey uses the IP address and port to discover the other nodes in the instance's topology automatically.

## Prepare the target instance

To ensure a smooth replication process, you must size your target Memorystore for Valkey instance appropriately to handle the incoming workload from your source instance. To do this, you must determine the exact specifications for your target instance. These specifications include the compatibility with the source instance, type of cluster mode, number of databases, shard count, version, and node type of the target instance.

To prepare the target instance, use the following guidelines:

  * **Compatibility with the source instance** : the source and target instances must reside in the same project and region.
  * **Cluster mode** : the [cluster mode](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled) of the target instance must match the cluster mode of the source instance. If the source instance is Cluster Mode Disabled, then the target instance must also be Cluster Mode Disabled. Otherwise, the target instance must be Cluster Mode Enabled.
  * **Number of databases** : if the target instance is Cluster Mode Disabled, then the number of logical databases on the instance must be the same or greater than the number of databases on the source instance.
  * **Shard count** : if the target instance is Cluster Mode Enabled, then the number of shards on the target instance must be identical to the number of shards on the source instance. However, the number of replicas on the source and target instances can be different.
  * **Instance version** : the version of the target instance must be compatible with the version of the source instance. For more information, see Version support.
  * **Maintenance version** : the maintenance version of the target instance must be `MEMORYSTORE_20260313_01_00` or later. For more information, see [About maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance).
  * **Node type** : the node type on the target instance must be large enough to handle the data that it receives from the nodes of the source instance. For more information about the node types that you can select for the target instance and the corresponding keyspace capacity for each node type, see [Node type specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#node_type_specification).

**Important** : You can't use [cross-region replication](https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication) instances as target instances. Also, verify that Memorystore for Valkey doesn't [block](https://docs.cloud.google.com/memorystore/docs/valkey/supported-commands#blocked-commands) any of the commands that you use in the source instance.

## Create the target instance

If you don't have a target instance that meets the requirements to receive data that's migrated from the source instance, then you must create the instance.

You can create this instance by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important** : Before you create the target instance, make sure that you review the guidelines in Prepare the target instance.

### Console

To create the target instance, see [Create instances](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances).

### gcloud

To create the target instance, see [Create instances](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances).

## Configure a network attachment

To migrate the workloads of a source instance into a target instance, the nodes of the target instance must establish a connection to the nodes of the source instance. As a result, the data in the source instance can be replicated into the target instance.

For this connection and replication to occur, you must use a [network attachment](https://docs.cloud.google.com/vpc/docs/about-network-attachments). Connection attempts from the target nodes originate from the subnet in the source instance's VPC network that's linked to the network attachment.

You can use a network attachment that meets the following requirements:

  * It must reside in the same project and region as the target instance.
  * Its subnet must be located within the same VPC network as the source instance.
  * The subnet in the source instance must have an adequate IP CIDR range, supporting a minimum of `N+1` usable IP addresses (where `N` is the number of nodes in the target instance). For example, if a target instance has three shards and one replica, then it has six nodes: three nodes for the primary instance and three nodes for the replica. Therefore, you need at least seven IP addresses.
  * The subnet range can't overlap with `10.0.0.0/23` because this range is reserved for Memorystore for Valkey.



If your network attachment doesn't meet these requirements or you don't have a network attachment, then you must [create](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments) one.

## Start the migration

By starting the migration, the target instance establishes replication with the source instance. Any data that's written to the source instance is replicated into the target instance automatically. The target instance becomes a read replica of the source instance.

You can start the migration by using either the Google Cloud console or [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important** : Before you start the migration, make sure that you review the guidelines in Configure a network attachment. Also, after you start the migration, don't conduct slot migration operations on the source instance until after you finish the migration.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the ID of the target instance.

  3. On the **Instance at a glance** page, click **Start migration**.

  4. In the **Migrate Self Managed Redis and Valkey Instances** window, do the following:

  5. In the **Prepare** tab, read the information about the prerequisites for the source instance and the guidelines for the network attachment. Then, click **Continue**.

  6. In the **Connect** tab, do the following:

     1. Enter the **IP Address** and **Port** of the source instance. You noted this information in Prepare your source instance.
     2. Select the network attachment that you want to use to migrate data.
     3. Click **Continue**.
  7. In the **Review** tab, review the information that's associated with the migration process. This information includes the ID of the target instance, the IP address and port of the source instance, and the name of the network attachment. After reviewing this information, click **Start migration**.

  8. On the **Instance at a glance** page, verify that a **Migrating** status appears.




If either the nodes of the target instance can't connect to the nodes of the source instance or the data in the source instance can't replicate into the target instance, then the migration fails.

When this occurs, Memorystore for Valkey rolls back the target instance to its state before you started the migration process. The status of the target instance reverts to **Ready** , and the instance has both read and write capabilities again.

After resolving the issues for the migration failing, you can start the migration again.

### gcloud

To start the migration, use the [`gcloud memorystore instances start-migration`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/start-migration) command.
    
    
    gcloud memorystore instances start-migration INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION \
    --source-ip=SOURCE_IP_ADDRESS \
    --source-port=SOURCE_PORT \
    --network-attachment=projects/NETWORK_ATTACHMENT_PROJECT_ID/locations/NETWORK_ATTACHMENT_REGION/networkAttachments/NETWORK_ATTACHMENT_ID
    

Make the following replacements:

  * INSTANCE_ID: the ID of the target instance.
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the target instance.
  * REGION: the region where the target instance is located.
  * SOURCE_IP_ADDRESS: the IP address of the source instance. You noted this IP address in Prepare your source instance.
  * SOURCE_PORT: the port number of the source instance. You noted this port in Prepare your source instance.
  * NETWORK_ATTACHMENT_PROJECT_ID: the ID or project number of the Google Cloud project, which contains the network attachment that you want to use to migrate data.
  * NETWORK_ATTACHMENT_REGION: the region where the network attachment is located.
  * NETWORK_ATTACHMENT_ID: the ID of the network attachment.



To confirm that the migration has started successfully, use the [`gcloud memorystore instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/describe) command.
    
    
    gcloud memorystore instances describe INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID
    

Verify that a `MIGRATING` status appears next to the `state` parameter.

If either the nodes of the target instance can't connect to the nodes of the source instance or the data in the source instance can't replicate into the target instance, then the migration fails.

When this occurs, Memorystore for Valkey rolls back the target instance to its state before you started the migration process. The status of the target instance reverts to `ACTIVE`, and the instance has both read and write capabilities again.

After resolving the issues for the migration failing, you can start the migration again.

## Monitor the migration

To ensure that the migration is progressing without issues, you can monitor the migration on the source and target instances.

### Monitor the source instance

On the source instance, verify that the client output buffer usage remains low on the source nodes. Sustained low usage indicates a minimal lag and a successful synchronization of the data from the source instance to the target instance.

### Monitor the target instance

You can monitor the health of the migration from the source instance to Memorystore for Valkey. To do this, check the [**Migration status** (`/instance/migration_status`)](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#cloud-monitoring-metrics) metric for the target instance to verify that the current status of the instance is **HEALTHY**. This status indicates that the replication links between the shards of the source and target instances are active and functioning correctly during the migration process.

To check the **Migration status** metric for the instance using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Metrics explorer** page.

[Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. From the **Metric** menu, select the **Migration status** metric. To do this, select **Memorystore Instance** > **Instance** > **Migration status** , and then click **Apply**.

  3. From the **Filter** field, add the following filter: `instance_id = (equals) INSTANCE_ID`.

Replace INSTANCE_ID with the ID of the target instance.

  4. In the **Results** section, check the current status of the instance. If a **HEALTHY** status appears, then the instance is functioning, and you can finish the migration.

If the **HEALTHY** status doesn't appear, then you can use the [**Migration status** (`/instance/node/migration_status`)](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#cloud-monitoring-node-metrics) metric for the primary nodes of the target instance. By monitoring these nodes, you can determine whether any nodes aren't healthy. 

To use the **Migration status** metric for the instance nodes, do the following:

     1. From the **Metric** menu, select the **Migration status** metric. To do this, select **Memorystore Instance Node** > **Instance** > **Migration status** , and then click **Apply**.

     2. From the **Filter** field, add the following filter: `role = (equals) primary`.

     3. In the **Results** section, verify that the current status of all primary nodes is **HEALTHY**. If so, then the nodes are functioning and you can finish the migration.




## Finish the migration

When you're ready to cut over your application traffic to the target instance, finish the migration. By doing so, the nodes of the target instance no longer replicate with the nodes of the source instance. The target instance allows all read and write operations.

You can finish the migration by using either the Google Cloud console or [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Important** : By default, Memorystore for Valkey ensures that the target instance is fully caught up to the source instance up to the time that you finish the migration. Any writes to the source instance _after_ you finish the migration might not be replicated.

If you want a total consistency of data between the source and target instances, and no data loss, then before you finish the migration, stop all write operations to the source instance.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the ID of the target instance.

  3. On the **Instance at a glance** page, click **Finish migration**.

  4. In the **Finish migration** dialog, do the following:

     1. If you want to ensure that all data on the source instance is replicated onto the target instance, then select **Standard**.

**Caution** : If you want to cut over your application traffic to the new target instance immediately, then select **Force (Skip-sync)**. However, if you make this selection, then Memorystore for Valkey might not be able to replicate all data on the source instance into the target instance.
     2. In the **Instance ID** text field, enter the ID of the target instance.

     3. Click **Finish migration**.

  5. On the **Instance at a glance** page, verify that a **Migrated** status appears.


**Important** : After you finish the migration, update your application's configuration files to point all traffic to the target instance.

### gcloud

To finish the migration, use the [`gcloud memorystore instances finish-migration`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/finish-migration) command.
    
    
    gcloud memorystore instances finish-migration INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION
    

Make the following replacements:

  * INSTANCE_ID: the ID of the target instance
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the target instance
  * REGION: the region where the target instance is located

**Caution** : If you want to cut over your application traffic to the new target instance immediately, then use the `--force` parameter. However, by using this parameter, Memorystore for Valkey might not be able to replicate all data on the source instance into the target instance.

To confirm that the migration has finished successfully, use the [`gcloud memorystore instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/describe) command.
    
    
    gcloud memorystore instances describe INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID
    

Verify that a `MIGRATED` status appears next to the `state` parameter.

**Important** : After you finish the migration, update your application's configuration files to point all traffic to the target instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
