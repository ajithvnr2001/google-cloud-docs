---
url: https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance/
title: About maintenance \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:45.256126+00:00
---

# About maintenance  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  About maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how Memorystore for Valkey performs maintenance on instances. It also provides information and configuration recommendations that your client applications must be aware of to take advantage of Memorystore for Valkey's zero-downtime maintenance design. These recommendations apply to both [highly available](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas) instances and instances without replicas. However, for all production use cases, we strongly recommend that you use the high-availability configuration.

Memorystore for Valkey updates instances routinely to ensure that the service is reliable, performant, secure, and up-to-date. These updates are called _maintenance_. Maintenance is managed fully by the service and is designed to have a zero-downtime impact.

Maintenance typically falls into the following categories:

  * **Memorystore features.** To launch some features, Memorystore requires a maintenance update.
  * **Operating system patches.** We monitor newly identified security vulnerabilities in the operating system continuously. Upon discovery, we patch the operating system to protect you from new risks.
  * **Database patches.** Maintenance can include a Valkey update to improve an instance's security, performance, and reliability. This is beyond what OSS Valkey provides.



## Configure your client application

To configure your client application for the best performance and availability during maintenance, follow these steps:

  1. Use and configure your third-party client according to the guidance at [Valkey client best practices](https://docs.cloud.google.com/memorystore/docs/valkey/general-best-practices#valkey_client_best_practices) to make sure that any scheduled maintenance doesn't impact the client application. Our recommended client configurations can avoid connection resets through periodic inline topology refreshes and background connection rotations.
  2. Test your client application with a series of update operations (such as scale in or out, or replica count changes) while running a representative workload on primary and replica nodes, and monitoring for client impact. These updates test the inline topology refresh logic on clients, full sync impact, new node discovery, and existing node removal capability. Testing helps make sure that the third-party client is configured correctly to avoid any negative impact to your application.



### Cluster Mode Disabled instances

During maintenance, Cluster Mode Disabled instances undergo a failover, which resets their connections. This failover typically lasts for 15 seconds. To reconnect your client applications to the instance after the failover, we recommend that you create a retry mechanism with exponential backoff. After you receive an email that notifies you of upcoming maintenance, you can run simulated maintenance on a non-production instance to test the impact that maintenance has on the instance. For more information, see [Run maintenance simulation on an instance](https://docs.cloud.google.com/memorystore/docs/valkey/simulate-maintenance#run-maintenance-simulation-on-instance).

We also recommend that you keep the `/instance/memory/maximum_utilization` metric at 50% or lower when the scheduled maintenance begins. Guidance for this metric refers to an 80% threshold for memory management. However, we recommend that you target a ratio of 50% or lower during maintenance. For more information about the metric, see [Cloud Monitoring metrics](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#cloud-monitoring-metrics).

You can ensure this ratio in one of the following ways:

  * Schedule maintenance when traffic for the instance is low.
  * Scale up the size of your instance temporarily during the maintenance window.



## Scheduled maintenance

Memorystore for Valkey leverages a gradual deployment and create-before-destroy lifecycle strategy to avoid any downtime impact of Memorystore scheduled maintenance on your Valkey instances. Memorystore for Valkey achieves zero-downtime maintenance by using the request redirection capabilities of the OSS Valkey instance protocol with the following Memorystore mechanisms:

  1. A coordinated failover without any loss of data.
  2. A graceful node removal to enable clients to catch up to the node topology updates without any availability impact.
  3. The instance's Private Service Connect endpoints, which aren't affected by maintenance. For more information about these endpoints, see [Instance endpoints](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#instance_endpoints).



The service behavior described in the following sections apply to scheduled maintenance only. For more information about the impact of unplanned events such as hardware failures, see [Client behavior during an unplanned failover](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas#client_behavior_during_an_unplanned_failover).

### Default maintenance windows

By default, Memorystore updates your instance in the following windows according to your instance's time zone:

  * Weekday window (Monday to Friday): 10 PM to 6 AM
  * Weekend window: Friday, 10 PM to Monday, 6 AM



### Gradual deployment strategy

Memorystore for Valkey performs deployments with a progressively increasing scope, and at a rate that allows for failure detection early enough to mitigate any impact and establish stability confidence. Bake times (the time during which the update is applied and monitored before considering it a success and moving forward) are integrated across the Memorystore fleet of instances at the service scale. Additionally, bake times are integrated within instances across zones in a region (multiple fault-domains) to reduce the scope of impact, if any.

For your instance configured for [high availability](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas), at most, Memorystore for Valkey updates one fault-domain or zone at any time to make sure that an instance shard, including both primary and replicas, has high availability throughout the update. Furthermore, Memorystore for Valkey updates only a few nodes at any time. Updates use a create-before-destroy lifecycle mechanism to maximize an instance's stability. This strategy provides the most benefits when updating an instance with many shards. Only applying the updates to a small part of the overall user keyspace at any time maximizes data availability.

### Create-before-destroy lifecycle strategy

A Valkey instance has multiple shards. Each shard has one primary node and zero-or-more replica nodes. Memorystore uses the following process to update any existing primary or replica Valkey node in a shard:

  1. Memorystore for Valkey adds a new replica with the latest software update to the shard. Memorystore creates a new node, instead of updating an existing node, to ensure your provisioned capacity is retained if an unexpected bootstrap failure occurs.
  2. If a node within the shard to be updated is a primary node, then the primary node is first converted to a replica before removing the node by using a [coordinated failover](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance#step_2_run_a_coordinated_primary_failover).
  3. Memorystore [removes the replica](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance#step_3_remove_the_replica) that uses the earlier software.
  4. For each node in the instance, Memorystore repeats this process.



The create-before-destroy strategy helps retain the provisioned capacity of the instance, as compared to a typical rolling deployment which updates in-place, but results in an availability outage (and sometimes data loss) for the client application. For shards without replicas, Memorystore for Valkey still provisions a new replica first, coordinates the failover, and lastly replaces the existing primary node of the shard.

#### Step 1: Add a replica

The first step of the create-before-destroy mechanism is to add a replica node with the latest software using the full sync OSS Valkey mechanism to copy the data from the primary to the replica node. This is done by forking a child process and leveraging diskless replication to bootstrap the replica. Memorystore for Valkey supports diskless replication. Unless you enable [persistence](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview), Memorystore for Valkey doesn't use disks during replication.

You can best take advantage of the horizontal scale architecture of the instance by provisioning a higher number of shards to reduce the keyspace size within a node. Having a smaller dataset per node helps to reduce the fork latency impact of a full sync operation. It also speeds up copying of data across the nodes.

#### Step 2: Run a coordinated primary failover

If the Valkey node that needs to be updated is a primary node, Memorystore runs a coordinated failover to the newly added replica node. Then, Memorystore [removes the node](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance#step_3_remove_the_replica). During the coordinated failover, the client and the Valkey nodes work together and use the following strategies to avoid downtime for the application:

**Important** : You don't need to perform this step for Cluster Mode Disabled instances. Because these instances have only one shard per instance, the instances don't have an in-memory topology.

  1. Incoming client requests are temporarily blocked on the primary node, providing a window to ensure the existing replica is synced 100% with the primary node.
  2. The replica completes the election process to take over the primary role.
  3. The previous primary node, now a replica node, unblocks the existing requests and redirects the requests to the new primary node by using the OSS Valkey instance protocol. Any new requests sent to the previous replica node continue to be redirected to the new primary node.
  4. Your Valkey-friendly client refreshes its in-memory topology. It learns the address of the new primary endpoint, and no longer requires redirections.



Coordinated failovers typically take tens of milliseconds. However, in-flight data pending to be flushed to replicas and your total instance size can increase failover latency. Instance size can affect the convergence across primary nodes, which affects decision making on electing the new primary node.

#### Step 3: Remove the replica

The last step of the create-before-destroy mechanism is to remove the replica node on the earlier software. The node removal impacts client applications because Memorystore for Valkey drops your clients. Because topology refresh isn't applicable for Cluster Mode Disabled instances, we recommend that you use a retry mechanism with exponential backoff to reconnect your application to the new replica endpoints after they become available.

For Cluster Mode Enabled instances, Memorystore for Valkey designed the removal of a Valkey replica to be graceful to let client applications refresh their topology before experiencing a hard node shutdown. The topology is customized to enable clients to learn about the new replica but also forget the one to be removed ahead of time.

Memorystore for Valkey keeps the replica node running the earlier software around for a certain drain period, typically on the order of minutes, during which it starts redirecting the incoming read requests to the primary node of its shard. This process lets the third-party client refresh the node topology and learn about the new replica endpoints. If the client tries to reach a removed node after the drain period, then the attempt fails. This failure triggers a node topology refresh on the connecting client so that it learns about the replica change. New refreshes of the node topology don't see the replica node to be removed.

## Maintenance settings

Memorystore for Valkey lets you customize maintenance schedules to align with your application's needs and to minimize disruptions. To customize a maintenance schedule, configure a maintenance window for your instance.

You set maintenance windows for each Memorystore for Valkey instance and you have the following configuration options:

  * **Day of the week** : the day when maintenance occurs
  * **Start hour** : the hour that maintenance begins



The maintenance window lasts for one hour. In some cases, maintenance might extend beyond the window you select.

After you configure a maintenance window for an instance, Memorystore for Valkey schedules automatic maintenance in the future according to the preferences that you set for maintenance windows.

### Default maintenance windows

If you don't set a maintenance window, then Memorystore for Valkey updates your instance in one of the following windows, according to your instance's time zone:

  * **Weekday window (Monday to Friday)** : 10:00 PM to 6:00 AM
  * **Weekend window** : Friday, 10:00 PM to Monday, 6:00 AM



## Maintenance example

As a developer managing a shopping cart service at a retailer, you oversee a production environment that includes a Memorystore for Valkey instance. To ensure optimal performance during maintenance, you schedule it when the instance experiences minimal traffic. This typically occurs around midnight on Sundays.

In this case, set your production instance's maintenance window to the following day and time:

  * **Day of the week** : Sunday
  * **Start hour** : 1 AM



## Upcoming maintenance notifications

To ensure that you stay informed about maintenance events on your instance, set up email notifications about upcoming maintenance at least one week before maintenance is scheduled. These notifications have the subject line of `"Upcoming maintenance for your Cloud Memorystore instance [your-instance-name]"`.

Memorystore for Valkey also sends a notification when maintenance starts for your instance. The subject line of the email is `"Maintenance is undergoing for your Cloud Memorystore instance [your-instance-name]"`.

After Memorystore for Valkey completes maintenance, it sends a completed notification. The subject line of the email is `"Completed Maintenance for your Cloud Memorystore instance [your-instance-name]"`.

If Memorystore for Valkey reschedules maintenance, then you receive an email that notifies you of the canceled maintenance. The subject line of this email is `"Canceled maintenance for your Cloud Memorystore instance [your-instance-name]"`.

To receive maintenance notifications you must opt in for them. To sign up for maintenance notifications, do the following:

  1. [Set a maintenance window](https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows#set-preferred-window-maintenance).
  2. [Opt in to receive maintenance notifications](https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows#turn-on-maintenance-notifications).



To receive maintenance notifications from Memorystore for Valkey, complete these steps at least one week before the scheduled maintenance update for your instance. Otherwise, Memorystore for Valkey doesn't have sufficient time to notify you of the upcoming maintenance.

Memorystore for Valkey sends notifications to the email address that's associated with your Google Account. You can't configure a custom email alias (for example, a team email alias). Also, we don't support sending notifications to a different email address.

By subscribing to maintenance notifications, you receive alerts for all Memorystore for Valkey instances that have maintenance scheduled within a Google Cloud project. For each instance, you receive a separate notification.

For more information about finding a scheduled maintenance, see [Find scheduled maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows#find-scheduled-maintenance).

## Reschedule maintenance

This section provides guidelines on how to reschedule maintenance. For example, if a new service is scheduled to launch during your current maintenance window, then you might want to postpone the maintenance window until a few days after the launch.

You can reschedule maintenance within 14 days of the originally scheduled time. As part of [rescheduling maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows#reschedule-maintenance), choose one of the following options:

  * **Update now** : instead of waiting for the scheduled maintenance window, you can apply the updates to your instance immediately.
  * **Custom day and time** : choose any time within _14 days_ of the originally scheduled maintenance time.



When you reschedule maintenance, the following restrictions apply:

  * If there's less than one hour remaining before the current scheduled maintenance time, then you can't reschedule the maintenance.
  * After you reschedule the maintenance successfully, Memorystore for Valkey sends you an email notification, confirming the cancellation of the previous maintenance. In addition, you receive a new maintenance notification with the updated schedule.



For more information about rescheduling maintenance see [Reschedule maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows#reschedule-maintenance).

**Caution:** Although Memorystore for Valkey doesn't provide you with the option to reschedule maintenance for multiple instances at once, you can reschedule maintenance in bulk programmatically.   
  
If you reschedule in bulk, then batch your operations into appropriate-sized requests. We recommend that you limit the batch size to 100 instances and wait for ample time between requests. Otherwise, you might have failed rescheduling events.

## FAQ

This section contains frequently asked questions (FAQs) about maintenance for Memorystore for Valkey.

#### How do you know when maintenance is scheduled for your instance?

To learn when maintenance is scheduled for your instance, we recommend that you subscribe to notifications and configure a maintenance window. You can also [check your instance manually](https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows#find-scheduled-maintenance) to see if the `maintenanceSchedule` parameter appears in the response.

#### When does Memorystore for Valkey notify you about upcoming maintenance?

If you subscribe to maintenance notifications and set a maintenance window, then Memorystore for Valkey notifies you by email at least one week before a maintenance event.

#### How long can you defer maintenance?

After you schedule maintenance for your instance, you can either start the update for your instance immediately or defer the update for up to two weeks from the originally scheduled maintenance date and time.

For example, if you schedule maintenance for October 11 at 11:15 PM, then you can defer maintenance until October 25 at 11:15 PM. If you don't take any action, then maintenance runs at the scheduled date and time.

For more information, see [Reschedule maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows#reschedule-maintenance).

#### Which best practices result in a smooth maintenance update experience?

To ensure a smooth maintenance update experience, we recommend that you do the following:

  1. Follow the instructions to [configure your client application](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance#configure_your_client_application).
  2. [Set your maintenance window](https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows#set-preferred-window-maintenance) to a day and time when your instance experiences minimal traffic (for example, Sundays at midnight).
  3. [Turn on maintenance notifications](https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows#turn-on-maintenance-notifications). As a result, Memorystore for Valkey notifies you by email at least seven days before a maintenance update is scheduled for your instance.
  4. If you don't have a low-impact or no-impact hour for your application usage, then use the service default of the gradual rollouts. This default contains best practices for maintenance updates. For more information, see Scheduled maintenance.



#### When do we recommend that you apply a maintenance update immediately?

You can apply a maintenance update immediately on a test instance to see how the update impacts your application. You can observe the impact that this update has. If there are issues with the update, then you can defer maintenance on your production instances until you resolve the issues.

If the current day and time works for your instance and you expect a high load on your instance in the future, then you can run the maintenance update immediately.

#### Do maintenance updates always complete inside of the maintenance window?

Memorystore for Valkey starts a maintenance update inside of the maintenance window that you specify. Memorystore for Valkey usually completes the update within the window, but this doesn't always happen.

#### Can you opt out of maintenance or schedule maintenance on certain instances first?

You can't opt out of maintenance or control the order of maintenance for your instances. However, after you receive the initial maintenance notification, you can [reschedule maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows#reschedule-maintenance) to defer it for up to two weeks.

## What's next

  * View the [permissions](https://docs.cloud.google.com/memorystore/docs/valkey/access-control#permissions_and_their_roles) that you need to manage maintenance windows for your instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
