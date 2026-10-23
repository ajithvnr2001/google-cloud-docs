---
url: https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication/
title: About cross-region replication \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:46.315906+00:00
---

# About cross-region replication  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  About cross-region replication Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of cross-region replication for Memorystore for Valkey.

For instructions on managing cross-region replication, see [Work with cross-region replication](https://docs.cloud.google.com/memorystore/docs/valkey/create-manage-cross-region-replication).

Cross-region replication lets you create secondary instances from a primary instance to make your instance available for reads in different regions. Secondary instances also provide redundancy for disaster recovery scenarios in case of regional outages.

Key concepts in this page include the following:

  * **Primary instance** : A read-write instance in a single region.
  * **Secondary instance** : A read-only instance that replicates from the primary instance asynchronously. For information about promoting and detaching secondary instances, see the _detach_ and _switchover_ tasks that appear in How to manage cross-region replication.
  * **Replicator node** : A node in the primary instance's shard that replicates to a follower node in the secondary instance. Any primary or replica node in the shard can serve the role of a replicator.
  * **Follower nodes** : Nodes in the secondary instance that replicate from a replicator node in the primary instance. Only primary nodes in the secondary instance can have the role of a follower.
  * **Shard count and slot assignment** : Primary and secondary instances have the same number of shards and slot assignments.



## Benefits

Benefits of cross-region replication on Memorystore for Valkey include the following:

  * **Disaster recovery** : If the primary instance's region becomes unavailable, then you can detach or switch over to a secondary instance in another region to serve read and write requests. Secondary instances serve read requests without issuing a switchover or detach command.
  * **Geographically distributed data** : Distributing data geographically brings the data closer to you and decreases read latency.
  * **Geographic load balancing for read traffic** : If slow or overloaded connections occur in one region, then you can route traffic to another region.



## Feature behavior

This section explains important behavior for the cross-region replication feature.

  * **Scale the instance capacity** : When you [scale the capacity](https://docs.cloud.google.com/memorystore/docs/valkey/about-scaling-instance-capacity) of the primary instance, Memorystore for Valkey scales secondary instances automatically to match the primary instance.
  * **Scale the replica count** : You can [scale the replica count](https://docs.cloud.google.com/memorystore/docs/valkey/scale-replica-count) for primary and secondary instances independently based on your workload needs. Updates to the replica count are local only and don't propagate to other instances within the cross-region replication collection of instances.
  * **Switch over during a potential outage** : You can perform a switchover to promote a secondary instance, even if the primary instance isn't available because of an outage. When the outage is resolved, the unavailable primary instance becomes a secondary instance.
  * **Create online secondary instances** : When adding a secondary instance to a primary instance, the primary instance stays online. While Memorystore for Valkey creates the secondary instance, the primary instance handles requests and replicates data.
  * **Create secondary instances** : You can have up to two secondary instances. They can be located either in the same region or in different regions from each other. You can't make an existing instance into a secondary instance. You can add only new instances as secondary instances.
  * **Synchronize settings** : Memorystore for Valkey synchronizes most instance settings automatically between primary and secondary instances. For more information about these settings, see Instance settings.
  * **Pricing** : Memorystore for Valkey charges customers that use cross-region replication for any secondary instances that Memorystore for Valkey provisions for cross-region replication. For each node and replica that Memorystore for Valkey deploys on the secondary instance, you're charged as per any other primary instance. Additionally, you incur [networking charges](https://cloud.google.com/memorystore/docs/valkey/pricing#network-pricing) for transferring data between instances in different regions.
  * **Perform maintenance updates** : To ensure compatibility with cross-region replication, while creating your secondary instance, your primary instance might undergo a maintenance update. If the primary instance isn't running the required software version, then this update happens. The update process might introduce some additional latency when creating your secondary instance. For more information, see [About maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance).
  * **Use ACL policies** : If you use cross-region replication to create secondary instances from a primary instance, then you must manage [access control list (ACL) policies](https://docs.cloud.google.com/memorystore/docs/valkey/use-acl-policies) for primary and secondary instances independently. Memorystore for Valkey doesn't propagate ACL policies from primary instances to secondary instances.



## How to manage cross-region replication

Cross-region replication involves the following tasks:

  * [**Create a secondary instance**](https://docs.cloud.google.com/memorystore/docs/valkey/create-manage-cross-region-replication#create-secondary-instance): create a secondary instance that replicates data from your primary instance continuously.
  * [**View the secondary instance**](https://docs.cloud.google.com/memorystore/docs/valkey/create-manage-cross-region-replication#view-secondary-instance): view information about the secondary instance, including the name of the primary instance and the other secondary instance in the replication group.
  * [**Detach secondary instances**](https://docs.cloud.google.com/memorystore/docs/valkey/create-manage-cross-region-replication#detach-secondary-instances): detaching secondary instances is an operation in which you decouple secondary instances from their primary instance. This makes them fully functional, independent instances that allow both reads and writes. After a detach operation, the secondary instances no longer replicate data from the primary instance with which they were associated formerly. Both the original primary instance and the newly detached instances (former secondaries) function as independent instances with no relationship to one another.

You detach secondary instances for the following reasons:

    * **Regional migration** : perform a planned migration of Memorystore for Valkey resources from their primary region to another region.
    * **Disaster recovery** : activate Memorystore for Valkey resources in a secondary region rapidly if the resources in the primary region become unavailable. If the secondary instances aren't caught up to the primary instance fully, then some data loss might occur.
  * [**Switch over your instances**](https://docs.cloud.google.com/memorystore/docs/valkey/create-manage-cross-region-replication#switchover-instances): perform a switchover to reverse the roles of your primary and secondary instances. You can perform a switchover for the following reasons:

    * Test your disaster recovery setup
    * Switch over during an actual disaster recovery scenario
    * Perform a migration of your workload

After you complete the switchover, Memorystore for Valkey reverses the direction of replication. The former secondary instance can now accept both reads and writes, while the former primary instance switches to read-only.




## Architecture example for cross-region replication

This diagram shows a primary instance in the `us-east1` region and secondary instances in the `us-west1` and `asia-east1` regions. The direction of replication is always from the primary instance to the secondary instances (for this example, from the `us-east1` region to the other regions).

Even though this diagram shows the same number of replicas in all regions, cross-region replication lets you have varying numbers of replicas according to your requirements.

![](https://docs.cloud.google.com/static/memorystore/img/valkey-crr.png)

## Instance settings

This section explains the settings that are required, copied, and overridden for primary and secondary instances that use cross-region replication. It also explains the settings that you configure on the primary instance, and the settings that you configure locally.

### Required parameters to create a secondary instance

To [create a secondary instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-manage-cross-region-replication#create-secondary-instance), you must set values for the following parameters:

  * **Google Cloud project** : the project where your primary instance is located and where you create the secondary instance.
  * **Region** : the region where you want the secondary instance to be located.
  * **Private Service Connect configuration** : the [network setup](https://docs.cloud.google.com/memorystore/docs/valkey/networking) for the secondary instance.
  * **Primary instance** : when you create the secondary instance, you must indicate a primary instance. You can use any instance other than a secondary instance as a primary instance. If you don't have a primary instance, then [create it](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances).



### Settings that a secondary instance copies from the primary instance

When you create a secondary instance, this instance copies the following settings from the primary instance:

  * [Shard count](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview#shards)
  * [IAM authentication mode](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth)
  * [In-transit encryption mode](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption)
  * [Instance configurations](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations)
  * [Valkey version](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview#valkey_version)
  * [Node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#node_type_specification)
  * [Persistence mode](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview)
  * [Cluster Mode Enabled and Cluster Mode Disabled modes](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled)



### Override default settings

When you create a secondary instance, you can use the following settings to override the default settings:

  * [Zone distribution configuration](https://docs.cloud.google.com/memorystore/docs/valkey/single-zone-instances)
  * [Replica count](https://docs.cloud.google.com/memorystore/docs/valkey/scale-replica-count)
  * [Maintenance windows](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance)
  * [Deletion protection](https://docs.cloud.google.com/memorystore/docs/valkey/deletion-protection)
  * [Automated backups](https://docs.cloud.google.com/memorystore/docs/valkey/backups#automated-and-on-demand-backups)



### Update instance settings

When you update the settings for your Memorystore for Valkey instance, you can change some settings only on the primary instance. Memorystore for Valkey syncs these changes to the secondary instances automatically.

You can change other settings on the primary and secondary instances independently. Memorystore for Valkey applies these changes only locally, and doesn't sync them with the other instances.

#### Configure settings on the primary instance

You must change the following settings on the primary instance. Memorystore for Valkey syncs these changes with the secondary instances automatically.

  * [Shard count](https://docs.cloud.google.com/memorystore/docs/valkey/scale-instance-capacity#scale_the_shard_count)
  * [Instance configurations](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations)
  * [Persistence mode](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview)
  * [Valkey version](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview#valkey_version)
  * [Node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#node_type_specification)



#### Configure local settings

You configure the following settings locally:

  * [Deletion protection](https://docs.cloud.google.com/memorystore/docs/valkey/deletion-protection)
  * [Replica count](https://docs.cloud.google.com/memorystore/docs/valkey/scale-replica-count)
  * [Maintenance windows](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance)
  * [Instance endpoints](https://docs.cloud.google.com/memorystore/docs/valkey/multiple-vpcs-user-registered-psc-connection#register_psc_connections_with_your_memorystore_instance_for_network_1)
  * [Automated backups](https://docs.cloud.google.com/memorystore/docs/valkey/backups#automated-and-on-demand-backups)



## Best practices for switching primary and secondary instances

When you [perform a switchover](https://docs.cloud.google.com/memorystore/docs/valkey/create-manage-cross-region-replication#switchover-instances), we recommend that you follow the instructions in this section. This way, your application can keep track of writes and send any writes to the appropriate instance.

  1. Stop your application from writing to the primary instance.
  2. If there are multiple secondary instances to promote, then determine the secondary instance that you want to promote to the primary instance. The following factors can help you determine which secondary instance to promote:

     * How close your application is to the instance. This can affect write latency.
     * The secondary instance that's most caught up, in terms of data.
     * The secondary instance that's closest to the primary instance, in terms of settings.
  3. [Perform a switchover on the secondary instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-manage-cross-region-replication#switchover-instances).

  4. Wait for the switchover operation to complete.

  5. Update your application to send any writes to the newly promoted instance that you selected in step 2.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
