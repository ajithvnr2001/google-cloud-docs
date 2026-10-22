---
url: https://docs.cloud.google.com/memorystore/docs/valkey/create-manage-cross-region-replication/
title: Work with cross-region replication \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:57.901753+00:00
---

# Work with cross-region replication  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/create-manage-cross-region-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Work with cross-region replication Stay organized with collections  Save and categorize content based on your preferences. 

Cross-region replication lets you create secondary instances from a primary instance to make the instance available in different regions. If the primary instance's region becomes unavailable, then you can detach or switch over to a secondary instance in another region to serve read and write requests. Secondary instances serve read requests without detaching or switching over to the primary instance. Distributing data geographically brings the data closer to you and decreases read latency. If slow or overloaded connections occur in one region, then you can route traffic to another region.

[Access control list (ACL) policies](https://docs.cloud.google.com/memorystore/docs/valkey/use-acl-policies) aren't replicated across regions in Memorystore for Valkey. If you assign an ACL policy to a cross-region replication instance, then you must manage the consistency for the policy in the different regions that are associated with the instance.

To maintain consistency, update and delete each policy that's assigned to the primary and secondary instances separately, and ensure that the rules for each policy are consistent. ACL policies aren't linked to one another so you can modify and delete policies in any order.

**Note** : To create a secondary instance, you must have a service network policy in the region where you want the instance to be located. For more information about service network policies, see [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking).

Also, for a conceptual overview of cross-region replication, see [About cross-region replication](https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication).

## Create a secondary instance

When you create a secondary instance, Memorystore for Valkey copies and applies some settings of the primary instance as secondary instance settings. For more information, see [Instance settings](https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication#instance-settings).

You can create a secondary instance in Memorystore for Valkey by using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click a primary instance. The primary instance is the parent of the secondary instance that you're creating.

**Note** : Don't click a secondary instance because Memorystore for Valkey doesn't support cascading replicas. Also, don't click a primary instance if it already has two secondary instances because a primary instance can have no more than two secondary instances.

If no primary instances appear, then [create an instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances). After you create it, you can click it.

  3. In the side panel, click the **Secondary instances** tab.

  4. Click **Add secondary instance**.

  5. In the **Add secondary instances** window, make the following changes:

     1. In the **Instance ID** field, enter the ID of the secondary instance that you're creating. The ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter, end with a lowercase letter or number, and be unique in its region.

     2. From the **Region** menu, select the region where you want the secondary instance to be located.

     3. In the **Zonal availability** section, select one of the following options:

        * If you want all of the shards and replicas of the instance to be distributed across three zones of the region where Memorystore for Valkey creates the instance, then select the **Multi-zone** option.

For example, if the region you select is `us-central1`, and you select the **Multi-zone** option, then Memorystore for Valkey distributes the instance's shards and replicas across the `us-central1-a`, `us-central1-b`, and   
`us-central1-c` zones. In case of a zonal failure, the nodes in the instance failover to the replicas.

        * If you want all of the shards and replicas of the instance to be located in one zone of the region where Memorystore for Valkey creates the instance, select the **Single zone** option, and then select the zone from the **Zone** menu.

By using a single zone, you reduce network costs. However, in case of a zonal failure, failover doesn't occur.

     4. From the **Replicas** menu, select the number of replicas (per shard) for the instance. You can have zero, one, or two replicas.

     5. From the **Network** menu, select a network for the instance. For more information about networking for Memorystore for Valkey, see [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking).

  6. Click **Add secondary instance**.




### gcloud

**Note** : If you installed the gcloud CLI, then make sure that you have the latest version by running [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update). To manage cross-region replication for Memorystore for Valkey, you need at least gcloud CLI version 488.0.0.

To create a secondary instance, use the [`gcloud memorystore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/create) command.
    
    
    gcloud memorystore instances create INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID \
    --cross-instance-replication-config-role=secondary \
    --psc-auto-connections=network=NETWORK,projectId=PROJECT_ID \
    --primary-instance=PRIMARY_INSTANCE_PATH
    

Make the following replacements:

  * INSTANCE_ID: the ID of the secondary instance that you're creating. The ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter, end with a lowercase letter or number, and be unique in its region.
  * PROJECT_ID: the ID of the project where you want to create the secondary instance. This is the same project where your primary instance is located.
  * REGION_ID: the ID of the region where you want the secondary instance to be located.
  * NETWORK: the network used to create the instance. It must use this format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID must match the network ID that the [service connection policy](https://docs.cloud.google.com/memorystore/docs/valkey/networking#prerequisites_required_before_creating_an_instance) uses. Otherwise, you can't create the secondary instance.
  * PRIMARY_INSTANCE_PATH: the path of the primary instance. For example: `projects/my-project/locations/us-central1/instances/my-primary-instance`. You can choose any instance in your project to be the primary instance as long as it's not a secondary instance.



For example:
    
    
    gcloud memorystore instances create my-secondary-instance \
    --project=my-project \
    --location=us-central1 \
    --cross-instance-replication-config-role=secondary \
    --psc-auto-connections=network=projects/my-project/global/networks/default,projectId=my-project \
    --primary-instance=projects/my-project/locations/us-central1/instances/my-primary-instance
    

## View a secondary instance

You can view summary information about a secondary instance by using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the expander arrow next to a primary instance. This instance is the parent of the secondary instance about which you want to view information.

  3. Click the secondary instance. Summary information about the instance appears.




### gcloud

To view information about a secondary instance, including a membership field that lists the primary and secondary instances in the replication group, use the [`gcloud memorystore instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/describe) command.
    
    
    gcloud memorystore instances describe INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID
    

Make the following replacements:

  * INSTANCE_ID: the ID of the secondary instance
  * PROJECT_ID: the ID of the project that contains the secondary instance
  * REGION_ID: the ID of the region where the secondary instance is located



## Perform a switchover

A switchover lets you reverse the roles of the primary and secondary instances by promoting a secondary instance to a primary instance for disaster recovery purposes. For more information, see [About cross-region replication](https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication#switchover).

You can perform a switchover by using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Note:** Before you perform a switchover, follow the instructions in [Best practices for switching primary and secondary instances](https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication#best-practices-switch). Using these instructions, your application can keep track of the writes that it makes, and send the writes to the appropriate instance.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the expander arrow next to a primary instance. This instance is the parent of the secondary instance that you want to switch over.

  3. Click the secondary instance.

  4. Click **Promote to Primary**.

  5. In the **Promote secondary instance to primary?** dialog, enter the ID of the secondary instance, and then click **Promote**.




After the switchover is complete, you must reconnect your applications to the new primary instance.

### gcloud

To perform a switchover, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command.
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID \
    --clear-primary-instance \
    --cross-instance-replication-config-role=primary \
    --cross-instance-replication-config-secondary-instances=[instance=SECONDARY_INSTANCE_PATH]
    

Make the following replacements:

  * INSTANCE_ID: the ID of the secondary instance that you want to promote to a primary instance by performing the switchover.
  * PROJECT_ID: the ID of the project that contains the secondary instance.
  * REGION_ID: the ID of the region where the secondary instance is located.
  * SECONDARY_INSTANCE_PATH: the path of the secondary instance. For example: `projects/my-project/locations/us-central1/instances/my-secondary-instance`.

If you have multiple secondary instances, then separate each instance by commas. For example: `[instance=projects/my-project/locations/us-central1/instances/my-first-secondary-instance,instance=projects/my-project/locations/europe-west1/instances/my-second-secondary-instance]`.




Suppose you have the following instances that are contained in the `my-project` project:

  * `instance-1`: this primary instance is located in the `us-east1` region.
  * `instance-2`: this secondary instance resides in the `asia-east1` region.
  * `instance-3`: this secondary instance resides in the `southamerica-east1` region.



You want to reverse the roles of `instance-1` and `instance-2` so that `instance-2` is the new primary instance and `instance-1` is a secondary instance.

To do this, use the following code:
    
    
    gcloud memorystore instances update instance-2 \
    --project=my-project \
    --location=asia-east1 \
    --clear-primary-instance \
    --cross-instance-replication-config-role=primary \
    --cross-instance-replication-config-secondary-instances=[instance=projects/my-project/locations/us-east1/instances/instance-1,instance=projects/my-project/locations/southamerica-east1/instances/instance-3]
    

After the switchover is complete, you must reconnect your applications to the new primary instance.

## Detach secondary instances

Detaching one or more secondary instances from their primary instance makes them fully functional independent instances that allow both reads and writes. For more information, see [How to manage cross-region-replication](https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication#how-to-manage-cross-region-replication).

You can detach secondary instances by using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Detach a secondary instance

This section explains how to detach a secondary instance from its primary instance.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click a primary instance. This is the parent of the secondary instance that you're detaching from the primary instance.

  3. In the side panel, click the **Secondary instances** tab.

  4. Select the checkbox next to the ID of the secondary instance that you're detaching from the primary instance.

  5. Click **Detach from Primary**.

  6. In the **Detach secondary instance?** dialog, enter the ID of the secondary instance, and then click **Detach**.




### gcloud

To detach a secondary instance, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command.
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --project=PROJECT_ID \
    --location=REGION_ID \
    --cross-instance-replication-config-role=none \
    --clear-primary-instance
    

Replace the following:

  * INSTANCE_ID: the ID of the secondary instance that you want to detach
  * PROJECT_ID: the ID of the project that contains the secondary instance
  * REGION_ID: the region where the secondary instance is located



### Detach multiple secondary instances

This section explains how to detach multiple secondary instances from their primary instance. You can also use the procedure in this section to detach an unavailable secondary instance from its primary instance.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click a primary instance. This is the parent of the secondary instances that you're detaching from the primary instance.

  3. In the side panel, click the **Secondary instances** tab.

  4. Select the checkboxes next to the IDs of the secondary instances that you're detaching from the primary instance.

  5. Click **Detach from Primary**.

  6. In the **Detach secondary instances?** dialog, do the following:

     1. Enter the IDs of the secondary instances. Use commas to separate the IDs.

     2. Click **Detach**.




### gcloud

To detach multiple secondary instances, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command.
    
    
    gcloud memorystore instances update PRIMARY_INSTANCE_ID \
    --project=PROJECT_ID \
    --location=PRIMARY_INSTANCE_REGION_ID \
    --remove-cross-instance-replication-config-secondary-instances=[instance=SECONDARY_INSTANCES] \
    --cross-instance-replication-config-role=none
    

Make the following replacements:

  * PRIMARY_INSTANCE_ID: the ID of the primary instance.
  * PROJECT_ID: the ID of the project that contains the secondary instances.
  * PRIMARY_INSTANCE_REGION_ID: the ID of the region where the primary instance is located.
  * SECONDARY_INSTANCES: the secondary instances that you want to detach. Use commas to separate the instance IDs. Each secondary instance must have this format: `projects/PROJECT_ID/locations/SECONDARY_INSTANCE_REGION_ID/instances/INSTANCE_ID`.



For example:
    
    
    gcloud memorystore instances update my-primary-instance \
    --project=my-project \
    --location=us-central1 \
    --remove-cross-instance-replication-config-secondary-instances=[instance=projects/my-project/locations/us-west4/instances/my-secondary-instance-1,instance=projects/my-project/locations/asia-southeast2/instances/my-secondary-instance-2] \
    --cross-instance-replication-config-role=none
    

**Note:** The `--cross-instance-replication-config-role=none` line of code is optional. If you want to detach _all_ secondary instances from the primary instance, then you must use this code. As a result, the primary instance becomes an independent instance.

You can also detach secondary instances from the primary instance by specifying a list of instances that you _don't_ want to detach. Memorystore for Valkey detaches any instances that you don't include in this list.

Suppose you have the following secondary instances:

  * `instance-1`: this instance is located in the `us-east1` region.
  * `instance-2`: this instance resides in the `asia-east1` region.



You want to detach both secondary instances from `my-primary-instance`. This primary instance is located in the `us-central1` region and is contained in the `my-project` project.

To detach the secondary instances, use the following code:
    
    
    gcloud memorystore instances update my-primary-instance \
    --project=my-project \
    --location=us-central1 \
    --cross-instance-replication-config-secondary-instances=[]
    --cross-instance-replication-config-role=none
    

For this example, because the null `[]` value is assigned to the `--cross-instance-replication-config-secondary-instances` parameter, Memorystore for Valkey detaches all secondary instances from the primary instance.

## Update instance settings

This section provides links to update instance settings. The process for updating instance settings is different, depending on whether you change settings on the primary instance or secondary instance. For more information about how to update settings, see [Instance settings](https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication#instance-settings).

### Update settings on the primary instance

You must change the following settings on the primary instance. After you do, Memorystore for Valkey synchronizes the changes to the secondary instance.

  * [Scale the instance's capacity](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity)
  * [Configure the instance](https://docs.cloud.google.com/memorystore/docs/valkey/configure-instances)
  * [Prevent the deletion of the instance](https://docs.cloud.google.com/memorystore/docs/valkey/deletion-protection)
  * [Manage persistence for the instance](https://docs.cloud.google.com/memorystore/docs/valkey/manage-persistence)



### Update settings on the secondary instance

You must change the following settings on the secondary instance:

  * [Configure whether the instance is single-zone or multi-zone](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances)
  * [Scale the instance's replica count](https://docs.cloud.google.com/memorystore/docs/valkey/scale-replica-count)
  * [Set maintenance windows for the instance](https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows)



## Delete instances that use cross-region-replication

This section explains how to delete primary and secondary instances that use cross-region replication.

### Delete a primary instance

To delete a primary instance, do the following:

  1. Detach or delete all secondary instances.
  2. To delete the primary instance, follow the instructions at [Delete instances](https://docs.cloud.google.com/memorystore/docs/valkey/delete-instances).



To protect against accidental deletion, you can't delete primary and secondary instances simultaneously.

### Delete a secondary instance

To delete a secondary instance, follow the instructions at [Delete instances](https://docs.cloud.google.com/memorystore/docs/valkey/delete-instances). For the instance ID, use the ID of the secondary instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
