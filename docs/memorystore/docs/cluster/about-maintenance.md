---
url: https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance/
title: About maintenance \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:52.316022+00:00
---

# About maintenance  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  About maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how Memorystore for Redis Cluster performs maintenance on clusters. It also provides information and configuration recommendations that your client applications should be aware of to take advantage of Memorystore for Redis Cluster's zero downtime maintenance design. These recommendations apply to both [highly available](https://docs.cloud.google.com/memorystore/docs/cluster/ha-and-replicas) clusters and clusters without replicas. However, we strongly recommend the high availability configuration for all production use cases.

Memorystore for Redis Cluster routinely updates clusters to ensure that the service is reliable, performant, secure, and up-to-date. These updates are called _maintenance_. Maintenance is fully managed by the service and is designed to have zero downtime impact.

Maintenance typically falls into the following categories:

  * **Memorystore features.** To launch some features, Memorystore requires a maintenance update.
  * **Operating system patches.** We continuously monitor newly identified security vulnerabilities in the operating system. Upon discovery, we patch the operating system to protect you from new risks.
  * **Database patches.** Maintenance can include a Redis update to improve security, performance, and reliability characteristics for clusters beyond what Redis provides.



## Configure your client application

To configure your client application for the best performance and availability possible during maintenance, follow these steps:

  1. Use and configure your OSS Redis cluster client according to the guidance at [Redis client best practices](https://docs.cloud.google.com/memorystore/docs/cluster/general-best-practices#redis_client_best_practices) to make sure that any scheduled maintenance doesn't impact your client application. Our recommended client configurations can avoid connection resets through periodic inline topology refreshes and background connection rotations.
  2. Test your client application with a series of update operations (such as scale in or out, replica count changes) while running a representative workload on primary and replica nodes, and monitoring for client impact. These updates test the inline topology refresh logic on clients, full sync impact, new node discovery, and existing node removal capability. Testing helps make sure that the client is configured correctly to avoid any negative impact to your application.



## Scheduled maintenance

Memorystore for Redis Cluster leverages a gradual deployment and create-before-destroy lifecycle strategy to avoid any downtime impact caused by maintenance. Zero-downtime maintenance is achieved by using the request redirection capabilities of the Redis protocol with the following Memorystore mechanisms:

  1. Coordinated failover without any loss of data.
  2. Graceful node removal to enable clients to catch up to the cluster topology updates without any availability impact.
  3. The cluster's Private Service Connect endpoints aren't affected by maintenance. For more information about these endpoints, see [Cluster endpoints](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#cluster_endpoints).



The service behavior described in the following sections applies to scheduled maintenance only. For information about the impact of unplanned events such as hardware failures, see [Client behavior during an unplanned failover](https://docs.cloud.google.com/memorystore/docs/cluster/ha-and-replicas#client_behavior_during_an_unplanned_failover).

### Gradual deployment strategy

Memorystore for Redis Cluster maintenance deployments are performed with progressively increasing scope, and at a rate that allows for failure detection early enough to mitigate impact and establish stability confidence. Bake times (time during which the update is applied and monitored before considering it a success and moving forward) are integrated across the Memorystore fleet of clusters at the service scale. Additionally, bake times are integrated within the cluster across zones in a region (multiple fault-domains) to reduce the scope of impact, if any.

For your cluster configured for [high availability](https://docs.cloud.google.com/memorystore/docs/cluster/ha-and-replicas), at most one fault-domain/zone is updated at any given time to make sure that a cluster shard, including both primary and replicas, has high availability throughout the update. Furthermore, only a few Redis nodes are updated at any given time. Updates use a create-before-destroy lifecycle mechanism to maximize cluster stability. This strategy provides the most benefits when updating a cluster with many shards. Only applying the updates to a small part of the overall user keyspace at any given time maximizes data availability.

### Create-before-destroy lifecycle strategy

A Redis cluster has multiple shards. Each shard has one primary node and zero-or-more replica nodes. Memorystore uses the following process to update any existing primary or replica Redis node in a shard:

  1. Memorystore for Redis Cluster first adds a completely new replica with the latest software update to the shard. Memorystore creates an entirely new node, instead of updating an existing node, to ensure your provisioned capacity is retained in the event of an unexpected bootstrap failure.
  2. If a node within the shard to be updated is a primary node, it is first converted to a replica before removal using a [coordinated failover](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance#step_2_coordinated_primary_failover).
  3. Next Memorystore [removes the replica](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance#step_3_remove_redis_replica) that uses the earlier software.
  4. The process is repeated for each node in the cluster.



The create-before-destroy strategy helps retain the provisioned capacity of the cluster, as compared to a typical rolling deployment which updates in-place, but results in an availability outage (and sometimes data loss) for the client application. For shards without replicas, Memorystore for Redis Cluster still provisions a new replica first, coordinates the failover, and lastly replaces the existing primary node of the shard.

#### Step 1: Add Redis replica

The first step of the create-before-destroy mechanism is to add a replica node with the latest software using the full sync OSS Redis mechanism to copy the data from the primary to the replica node. This is done by forking a child process and leveraging diskless replication to bootstrap the replica. Memorystore for Redis Cluster supports diskless replication. Unless you enable [persistence](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview), Memorystore for Redis Cluster doesn't use disks during replication.

You can best take advantage of the horizontal scale architecture of the cluster by provisioning a higher number of shards to reduce the keyspace size within a node. Having a smaller dataset per node helps to reduce the fork latency impact of a full sync operation. It also speeds up copying of data across the nodes.

#### Step 2: Coordinated primary failover

If the Redis node that needs to be updated is a primary node, Memorystore first executes a coordinated failover to the newly added replica node, and then proceeds with the [node removal](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance#step_3_remove_redis_replica). During the coordinated failover, the client and the Redis nodes work together and use the following strategies to avoid downtime for the application:

  1. Incoming client requests are temporarily blocked on the primary node, providing a window to ensure the existing replica is 100% synced with the primary.
  2. The replica completes the election process to take over the primary role.
  3. The previous primary node, now a replica, unblocks the existing requests and redirects them to the newly elected primary using the OSS Redis cluster protocol. Any new requests sent to the previous replica node continue to be redirected to the new primary node.
  4. Your Redis-cluster-friendly client refreshes its in-memory topology. It learns the address of the new primary endpoint, and no longer requires redirections.



Coordinated failovers should typically take tens of milliseconds. However, your total cluster size can increase failover latency. So can inflight data pending to be flushed to replicas. Cluster size can affect the convergence across primary nodes, which affects decision making on electing the new primary.

#### Step 3: Remove Redis replica

The last step of the create-before-destroy mechanism is to remove the replica node on the earlier software. An abrupt node removal would be impactful for client applications because clients cache the endpoint information and the cluster topology. Memorystore for Redis Cluster has designed the removal of a Redis replica to be graceful in order to allow client applications to refresh their topology before experiencing a hard node shutdown. The topology is customized to enable clients to learn about the new replica. The topology also forgets the replica that will be removed before it's removed.

The replica node running the earlier software is kept around for a certain drain period, typically on the order of minutes, during which it starts redirecting the incoming read requests to the primary node of its shard. It allows the cluster client to refresh the cluster topology and learn about the new replica endpoints. If the client tries to reach a removed node after the drain period, the attempt fails, which in turn triggers a cluster topology refresh on the cluster client so it learns about the replica change. New refreshes of the cluster topology don't see the replica node that will be removed.

## Maintenance settings

With Memorystore, you can customize maintenance schedules to align with your application's needs and minimize disruptions. You can do this by configuring a maintenance window for your cluster.

Maintenance windows are set per Memorystore cluster and allow the following configuration options:

  * **Day of the week.** Designates the day when maintenance occurs.
  * **Start hour.** The hour that maintenance begins.



The duration of the maintenance window is 1 hour. Note that in some cases, maintenance may spill beyond the window you have selected.

After you configure a maintenance window for a cluster, Memorystore for Redis Cluster schedules automatic maintenance in the future according to the preferences that you set for maintenance windows.

### Default maintenance windows

If you don't set a maintenance window, Memorystore will update your cluster in one of the following time windows according to your cluster's time zone:

  * **Weekday window (Monday to Friday).** 10 PM to 6 AM

  * **Weekend window.** Friday, 10 PM to Monday, 6 AM




## Maintenance example

As a developer managing a shopping cart service at a retailer, you have the responsibility to oversee a production environment that includes a cluster. To ensure optimal performance during maintenance, you aim to schedule it when the cluster experiences minimal traffic, which typically occurs around midnight on Sundays.

In this case, you can set your production cluster's maintenance window to:

  * **Day of the week.** Sunday.
  * **Start hour.** 1 AM.



## Upcoming maintenance notifications

To ensure you stay informed about maintenance events on your cluster, you can set up email notifications regarding upcoming maintenance at least one week before it's scheduled. These notifications will have the subject line, `"Upcoming maintenance for your Cloud Memorystore instance [your-cluster-name]"`.

A notification is also sent when the maintenance starts for your cluster. The subject line of the email would be `"Maintenance is undergoing for your Cloud Memorystore instance [your-cluster-name]"`.

On maintenance completion, a completed notification is sent. The email title is `"Completed Maintenance for your Cloud Memorystore instance [your-cluster-name]"`.

If Memorystore reschedules maintenance, you receive an email notifying you of the canceled maintenance. The subject line of this email would be `"Canceled maintenance for your Cloud Memorystore instance [your-cluster-name]"`.

You must opt in to receive these maintenance notifications. To sign up for maintenance notifications, follow these steps:

  1. [Set a maintenance window](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows#set-preferred-window-maintenance).
  2. [Turn on maintenance notifications](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows#turn-on-maintenance-notifications).



To receive maintenance notifications from Memorystore, ensure that you completed these steps at least one week before the scheduled maintenance update for your cluster. If you fail to do so, then Memorystore for Redis Cluster doesn't have sufficient time to notify you of the upcoming maintenance.

Memorystore for Redis Cluster sends notifications to the email address associated with your Google account. You can't configure a custom email alias (for example, a team email alias). At this time, we don't support sending notifications to a different email address.

By subscribing to maintenance notifications, you receive alerts for all Memorystore clusters with scheduled maintenance within a specified project. If subscribed, you receive a separate notification for each cluster.

For instructions on finding scheduled maintenance, see [Find scheduled maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows#find-scheduled-maintenance).

## Rescheduling maintenance

In the scenario where maintenance windows are configured for your cluster, this section provides guidelines on how to reschedule maintenance. For example, if a new service is scheduled to launch during your current maintenance window, you might want to postpone the maintenance window until a few days after the launch.

You can reschedule maintenance within 14 days of the originally scheduled time. As part of [rescheduling maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows#reschedule-maintenance), choose one of the following options:

  * **Update now** : instead of waiting for the scheduled maintenance window, you can apply the updates to your cluster immediately.
  * **Custom day and time** : choose any time within _14 days_ of the originally scheduled maintenance time.



While rescheduling maintenance, the following restrictions apply:

  * If there's less than an hour remaining before the current scheduled maintenance time, then you can't reschedule the maintenance.
  * Upon successful rescheduling, an email is sent confirming the cancellation of the previous maintenance, and a new upcoming maintenance notification is sent with the updated schedule.



For instructions on rescheduling maintenance see [Reschedule maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows#reschedule-maintenance).

**Caution:** Although Memorystore does not provide the option to reschedule maintenance for multiple clusters at once, some Memorystore users with large cluster counts opt to programmatically reschedule in bulk.   
  
If you are rescheduling in bulk, it is important to batch your operations into appropriately sized requests. We recommend limiting the batch size to 100 clusters and waiting ample time between requests. Exceeding this limit can result in failed rescheduling events.

## FAQ

This section contains frequently asked questions (FAQs) about maintenance for Memorystore for Redis Cluster.

#### How do you know when maintenance is scheduled for your cluster?

To learn when maintenance is scheduled for your cluster, we recommend that you subscribe to notifications and configure a maintenance window. You can also [check your cluster manually](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows#find-scheduled-maintenance) to see if the `maintenanceSchedule` parameter appears in the response.

#### When does Memorystore for Redis Cluster notify you about upcoming maintenance?

If you subscribe to maintenance notifications and set a maintenance window, then Memorystore for Redis Cluster notifies you by email at least one week before a maintenance event.

#### How long can you defer maintenance?

After you schedule maintenance for your cluster, you can either start the update for your cluster immediately or defer the update for up to two weeks from the originally scheduled maintenance date and time.

For example, if you schedule maintenance for October 11 at 11:15 PM, then you can defer maintenance until October 25 at 11:15 PM. If you don't take any action, then maintenance runs at the scheduled date and time.

For more information, see [Reschedule maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows#reschedule-maintenance).

#### Which best practices result in a smooth maintenance update experience?

To ensure a smooth maintenance update experience, we recommend that you do the following:

  1. Follow the instructions to [configure your client application](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance#configure_your_client_application).
  2. [Set your maintenance window](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows#set-preferred-window-maintenance) to a day and time when your cluster experiences minimal traffic (for example, Sundays at midnight).
  3. [Turn on maintenance notifications](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows#turn-on-maintenance-notifications). As a result, Memorystore for Redis Cluster notifies you by email at least seven days before a maintenance update is scheduled for your cluster.
  4. If you don't have a low-impact or no-impact hour for your application usage, then use the service default of the gradual rollouts. This default contains best practices for maintenance updates. For more information, see [Scheduled maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance#scheduled_maintenance).



#### When do we recommend that you apply a maintenance update immediately?

You can apply a maintenance update immediately on a test cluster to see how the update impacts your application. You can observe the impact that this update has. If there are issues with the update, then you can defer maintenance on your production clusters until you resolve the issues.

If the current day and time works for your cluster and you expect a high load on your cluster in the future, then you can run the maintenance update immediately.

#### Do maintenance updates always complete inside of the maintenance window?

Memorystore for Redis Cluster starts a maintenance update inside of the maintenance window that you specify. Memorystore for Redis Cluster usually completes the update within the window, but this doesn't always happen.

#### Can you opt out of maintenance or schedule maintenance on certain clusters first?

You can't opt out of maintenance or control the order of maintenance for your clusters. However, after you receive the initial maintenance notification, you can [reschedule maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/find-and-set-maintenance-windows#reschedule-maintenance) to defer it for up to two weeks.

## What's next

  * View the [permissions](https://docs.cloud.google.com/memorystore/docs/cluster/access-control#permissions_and_their_roles) that you need to manage maintenance windows for your cluster.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
