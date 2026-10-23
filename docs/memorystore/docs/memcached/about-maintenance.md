---
url: https://docs.cloud.google.com/memorystore/docs/memcached/about-maintenance/
title: About maintenance on Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:54.820901+00:00
---

# About maintenance on Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/about-maintenance/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  About maintenance on Memorystore for Memcached Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of maintenance for Memorystore for Memcached.

For instructions on scheduling maintenance windows, see [Finding and setting maintenance windows](https://docs.cloud.google.com/memorystore/docs/memcached/finding-and-setting-maintenance-windows).

## Overview

Memorystore for Memcached routinely updates instances to ensure that the service is reliable, performant, secure, and up-to-date. Most of these updates are performed while your Memcached instance is up and running. However, certain system updates require a brief service interruption to be performed. These updates are called _maintenance_. Maintenance typically falls into the following categories:

  * **Memorystore features.** To launch some features, Memorystore requires a maintenance update.

  * **Operating system patches.** We continuously monitor for newly identified security vulnerabilities in the operating system. Upon discovery, we patch the operating system to protect you from new risks.

  * **Database version upgrades.** Maintenance can include an OSS Memcached patch minor version update which does not include breaking or incompatible changes.




Users have two ways to perform maintenance: automatically or manually. The [maintenance windows](https://docs.cloud.google.com/memorystore/docs/memcached/finding-and-setting-maintenance-windows) feature allows users to specify a recurring time frame when maintenance can be automatically scheduled and performed. For users who want finer control over their instance's maintenance, [manual maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/maintenance-policy#manual_maintenance) provides a gcloud interface for updating an instance based on your desired schedule and logic.

## Impact of maintenance

During maintenance, a Memorystore for Memcached cluster experiences dropped connections and a full cache flush.

The nodes in your cluster are updated sequentially and evenly across the entire duration of your maintenance window. When a node is updated the cache is flushed and data is not restored post maintenance. The downtime is usually on the order of 5 minutes per node.

When a node undergoes maintenance, the connection is dropped and reset for that node. You should create a retry mechanism with [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) to reconnect your application to the nodes after maintenance occurs.

For users who have opted for [manual maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/maintenance-policy#manual_maintenance), you control the update timing for the individual nodes of your cluster.

## Maintenance settings

Memorystore offers you the ability to configure maintenance to occur at the most opportune time for your application. You can do this by configuring a maintenance window.

Maintenance windows are set per Memorystore instance and allow the following configuration options:

  * **Day of the week.** Designates the day when maintenance occurs.
  * **Start hour.** The hour that maintenance begins.
  * **Duration.** The length of the maintenance window, ranging from 3 hours to 8 hours.



If a maintenance window is configured for an instance, future automatic maintenance is scheduled to respect these preferences. If a maintenance window is not specified for your instance, maintenance can begin at any time without advanced notification.

## Maintenance example

Assume you are a developer at a retailer managing a shopping cart service. You have one Memorystore for Memcached instance for a production environment. You want maintenance to occur at the time when your instance handles the lowest amount of traffic, which is around midnight on Sundays.

In this case, you set your production instance's maintenance window to:

  * **Day of the week.** Sunday.
  * **Start hour.** 1 AM.
  * **Duration.** 3 hours.



In this case, we've opted for the shortest allowed duration, which ensures that maintenance takes place during this period of low traffic. For an application that has steady 24/7 traffic, specifying a longer duration may be preferred, as this more evenly spreads the impact of cache flushes. For applications which are particularly sensitive to any service impact, we recommend performing [maintenance manually](https://docs.cloud.google.com/memorystore/docs/memcached/maintenance-policy#manual_maintenance).

## Upcoming maintenance notifications

You can have a notification about upcoming maintenance sent to your email at least one week before maintenance is scheduled. If you want to set an email filter for notifications, the email title is `"Upcoming maintenance for your Cloud Memorystore instance [your-instance-name]"`.

Maintenance notifications are not sent out by default. If you want to get a notification for an upcoming maintenance you must do both of the following:

  1. [Set a maintenance window](https://docs.cloud.google.com/memorystore/docs/memcached/finding-and-setting-maintenance-windows#set_maintenance).
  2. [Opt in to maintenance notifications](https://docs.cloud.google.com/memorystore/docs/memcached/finding-and-setting-maintenance-windows#opt_in).



Notifications are sent to the email address associated with your Google account. It is not possible to configure a custom email alias (for instance, a team email alias), nor is it possible to subscribe another email address other than your own.

When subscribing you opt into maintenance notifications for all Memorystore instances that have maintenance windows in a given project. You receive one notification per instance.

For instructions on finding scheduled maintenance, see [Find scheduled maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/finding-and-setting-maintenance-windows#find_scheduled_maintenance).

## Rescheduling maintenance

If you have a maintenance window for your instance, you can reschedule maintenance at any time before maintenance is currently scheduled. For example, if you have a new service launching during your currently scheduled maintenance time, you might want to reschedule the maintenance window to a few days after your launch.

You may reschedule maintenance multiple times so long as it's not more than one week after the originally scheduled time. You have a few scheduling options for the new maintenance window:

  * **Update now.** You can apply the update to your instance immediately instead of waiting for the scheduled maintenance window.

  * **Defer to next scheduled window.** This defers maintenance by one week.

  * **Custom day and time.** This lets you choose any specific time _within one week_ after the originally scheduled maintenance time.




Rescheduling maintenance has the following additional behavior:

  * You cannot reschedule maintenance if less than an hour remains before currently scheduled maintenance.

  * You cannot reschedule for multiple Memcached instances with a single operation. They must be rescheduled individually.




For instructions on rescheduling maintenance see [Reschedule planned maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/find-and-set-maintenance-windows#reschedule_planned_maintenance).

**Caution:** Although Memorystore does not provide the option to reschedule maintenance for multiple instances at once, some Memorystore users with large instance counts opt to programmatically reschedule in bulk.   
  
If you are rescheduling in bulk, it is important to batch your operations into appropriate sized requests. We recommend limiting the batch size to 100 instances and waiting ample time between requests. Exceeding this limit can result in failed rescheduling events.

## Best practices

  * Set a maintenance window and subscribe to notifications for all production instances.
  * Choose an appropriate duration. Nodes are updated sequentially over the course of your entire specified duration. Choosing a longer duration spreads node cache flushes over a longer period of time which yields less impact to your application. However, a shorter duration allows the update to complete more quickly which may be desirable for applications that have well known low traffic periods or applications that are sensitive to any level of cache disruption.
  * Take measures so that the [System Memory Utilization](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-metrics) metric is at 50% or lower at the time of the scheduled maintenance. You can do this by scheduling for a time when instance traffic is low, or by temporarily scaling up your instance size during the maintenance window so that the System Memory Utilization metric is at 50% or lower.
  * Implement a retry mechanism with [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) to reconnect your application to the instance after maintenance.
  * Leverage the reschedule features to test the update on a non-production instance once the update becomes available



## Manual maintenance

While we expect that automatic maintenance via maintenance windows meets the requirements for the majority of Memorystore users, manual maintenance provides a gcloud interface for updating an instance. By using this interface, you can individually update your cluster nodes at a rate and time that makes the most sense for your application. As each node is updated by calling the gcloud interface, the individual node cache is flushed and connections are dropped similar to [automatic maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/maintenance-policy#impact_of_maintenance).

To perform manual maintenance you must first set a maintenance window for your instance and subscribe for maintenance notifications. Once an update is available you receive an email notification with the scheduled maintenance time for your instance. At this point, you can begin to [manually apply updates to your instance](https://docs.cloud.google.com/memorystore/docs/memcached/finding-and-setting-maintenance-windows#manually_applying_maintenance_updates). If the Memorystore for Memcached cluster is not fully updated by the scheduled maintenance time, any remaining cluster nodes are updated automatically during the maintenance window. If you have fully updated your instance prior to the scheduled maintenance time, there is no impact to the instance during the defined maintenance window.

## FAQ

The following are some frequently asked questions about the maintenance policy for Memorystore for Memcached:

#### What is the impact of maintenance on Memcached instances?

During maintenance the nodes in your cluster are updated sequentially over the duration of your maintenance window. Each node undergoes a cache flush with a downtime of approximately 5 minutes per node. For more details on impact, see [Impact of maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/maintenance-policy#impact_of_maintenance).

#### What is the duration of a maintenance update?

The window duration is user configurable from 3 to 8 hours. Node updates are spaced evenly across the designated duration.

#### How do I know when maintenance is scheduled for my instance?

We recommend subscribing for notifications to learn when maintenance is scheduled for your instance. You can also check manually in the Cloud console. If the Cloud console is blank and you have already set a maintenance window, you do not have upcoming maintenance scheduled yet.

#### When am I notified of upcoming maintenance?

If you are subscribed for maintenance notifications and have set a maintenance window, you are alerted by email at least seven days before a maintenance event.

#### How long can I defer maintenance?

Once maintenance has been scheduled for your instance, you may start the update for your instance immediately or defer the update for up to seven days from the originally scheduled maintenance time. For example, if maintenance is scheduled for Oct. 11 at 11:15 PM, you can defer until Oct. 18 at 11:15 PM. Maintenance is applied at the scheduled time if no action is taken.

For more details, see [Reschedule planned maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/about-maintenance#rescheduling_maintenance).

#### Is the IP address of my instance change during maintenance?

No. The IP address of your Memcached instance does not change.

#### Does setting or adjusting a maintenance window impact my instance?

No. Setting or adjusting the maintenance window does not cause any downtime for your instance. Also, it does not change the IP address of the instance, or cause any other changes to your instance.

#### What best practices should I follow for a smooth maintenance update experience?

We recommend that you follow the guidance in the [best practices section](https://docs.cloud.google.com/memorystore/docs/memcached/maintenance-policy#best_practices_for_maintenance_updates) for maintenance updates.

#### When should I apply maintenance immediately?

One circumstance when you should apply maintenance immediately is on a test instance to see how it affects a production instance. You can [reschedule planned maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/about-maintenance#rescheduling_maintenance) to have it apply immediately on a test instance. This allows you to observe the impact it has, and defer maintenance on production instances as needed/allowed.

#### Do maintenance updates always complete inside the maintenance window?

Updates start inside of the maintenance window you specify. The update almost always completes within the window.

#### Can I opt out of maintenance or schedule maintenance on certain instances first?

No, you can neither opt out of maintenance nor control the initial scheduling of maintenance. However, you can [reschedule maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/about-maintenance#rescheduling_maintenance) to defer it for up to seven days.

#### Can an update ever be applied outside a maintenance window?

In very rare circumstances, in order to protect against vulnerabilities that are time sensitive, maintenance can be applied to a Memcached instance outside of your designated maintenance window.

#### What happens if Memorystore cancels maintenance?

If Memorystore cancels a maintenance event you receive a notification that maintenance is cancelled. In rare cases, it might not be possible for Memorystore to send a cancellation notification in advance. In this case, you are notified that maintenance was not applied after the scheduled maintenance window has passed.

The maintenance is then rescheduled for a future maintenance window based on your selected preferences. You receive a new notification of upcoming maintenance when the maintenance event is rescheduled.

#### What time format is used for maintenance windows?

When using the Google Cloud console, maintenance windows are displayed and set in your local time zone but stored in UTC time; the Google Cloud console also displays the maintenance window time relative to UTC time. When setting windows with the Google Cloud CLI, you set the time using UTC time.

You should schedule windows based off UTC time because the Google Cloud console shows the window in the viewer's local time zone. This can cause confusion if users are setting the window in different time zones.

Maintenance windows do not undergo daylight savings time changes.

## What's next

  * View the [permissions](https://docs.cloud.google.com/memorystore/docs/memcached/access-control#maintenance_policy_permissions) required to manage maintenance windows for your Memcached instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
