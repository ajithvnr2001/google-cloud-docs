---
url: https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance/
title: About maintenance \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:31.601684+00:00
---

# About maintenance  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  About maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of maintenance for Memorystore for Redis.

For instructions on scheduling maintenance windows, see [Finding and setting maintenance windows](https://docs.cloud.google.com/memorystore/docs/redis/finding-and-setting-maintenance-windows).

## Overview

Memorystore for Redis routinely updates instances to ensure that the service is reliable, performant, secure, and up-to-date. Most of these updates are performed while your Redis instance is up and running. However, certain system updates require a brief service interruption to be performed. These updates are called _maintenance_. Maintenance typically falls into the following categories:

  * **Memorystore features.** To launch some features, Memorystore requires a maintenance update.

  * **Operating system patches.** We continuously monitor for newly identified security vulnerabilities in the operating system. Upon discovery, we patch the operating system to protect you from new risks.

  * **Database version upgrades.** Maintenance can include an OSS Redis patch minor version update which does not include breaking or incompatible changes.




In addition to maintenance windows, you can also update your instance using [Self-service maintenance](https://docs.cloud.google.com/memorystore/docs/redis/self-service-maintenance) once an [update is available](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance#upcoming_maintenance_notifications) for your instance. The [Maintenance changelog](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-changelog) lists the maintenance version number and details for self-service maintenance updates.

## Impact of maintenance

Both Basic Tier and Standard Tier instances undergo a connection reset during maintenance. To let your application reconnect to an instance after maintenance is complete, build a retry mechanism with exponential backoff. For more information, see [Exponential backoff](https://docs.cloud.google.com/memorystore/docs/redis/exponential-backoff).

You should also take measures so that the [System Memory Usage Ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#system_memory_usage_ratio) metric is at 50% or lower at the time of the scheduled maintenance. The System Memory Usage Ratio guidance refers to an 80% threshold for memory management, but we recommend targeting a ratio of 50% or lower during maintenance.

You can ensure the desired ratio by scheduling for a time when instance traffic is low, or by temporarily scaling up your instance size during the maintenance window so that the System Memory Usage Ratio metric is at 50% or lower.

**Caution:** When Memorystore for Redis applies maintenance to an instance that has read replicas, Memorystore for Redis first applies the new maintenance version to the read replicas. Then, Memorystore for Redis applies the maintenance version to the primary instance. When this occurs, you might experience a spike in CPU usage for each replica and the primary instance. In addition, the client application can't connect to the read replicas until Memorystore for Redis completes maintenance on the primary instance.

#### Standard Tier impact

During maintenance, Standard Tier instances undergo a failover. This failover typically lasts for 15 seconds.

After the failover, client applications need to reconnect. Once you receive an email notifying you of upcoming maintenance, you can run a [manual failover](https://docs.cloud.google.com/memorystore/docs/redis/initiating-manual-failover) on a non-production instance to test the impact maintenance has on your instance.

#### Basic Tier impact

During maintenance, Basic Tier instances are unavailable. This period of unavailability typically lasts for 5 minutes.

## Maintenance settings

Memorystore offers you the ability to configure maintenance to occur at the most opportune time for your application. You can do this by configuring a maintenance window.

Maintenance windows are set per Memorystore instance and allow the following configuration options:

  * **Day of the week.** Designates the day when maintenance occurs.
  * **Start hour.** The hour that maintenance begins.



The duration of the maintenance window is 1 hour.

If a maintenance window is configured for an instance, future automatic maintenance is scheduled to respect these preferences. If a maintenance window is not specified for your instance, maintenance can begin at any time without advanced notification.

## Maintenance example

Assume you are a developer at a retailer managing a shopping cart service. You have one Memorystore for Redis instance for a production environment. You want maintenance to occur at the time when your instance handles the lowest amount of traffic, which is around midnight on Sundays.

In this case, you set your production instance's maintenance window to:

  * **Day of the week.** Sunday.
  * **Start hour.** 1 AM.



## Upcoming maintenance notifications

You can have a notification about upcoming maintenance sent to your email at least one week before maintenance is scheduled. If you want to set an email filter for notifications, the email title is `"Upcoming maintenance for your Cloud Memorystore instance [your-instance-name]"`.

Maintenance notifications are not sent out by default. If you want to get a notification for an upcoming maintenance you must do all of the following:

  1. [Set a maintenance window](https://docs.cloud.google.com/memorystore/docs/redis/finding-and-setting-maintenance-windows#set_a_preferred_window_for_maintenance_on_an_instance).
  2. [Opt in to maintenance notifications](https://docs.cloud.google.com/memorystore/docs/redis/finding-and-setting-maintenance-windows#opt_in_to_maintenance_notifications).
  3. Do both of these at least 7 days before Memorystore schedules a maintenance update for your instance. Otherwise, you have not signed up for notifications in enough time for the system to send you a notification of upcoming maintenance.



Notifications are sent to the email address associated with your Google account. It is not possible to configure a custom email alias (for instance, a team email alias), nor is it possible to subscribe another email address other than your own.

When subscribing you opt-in to maintenance notifications for all Memorystore instances that have maintenance windows in a given project. You receive one notification per instance.

For instructions on finding scheduled maintenance, see [Find scheduled maintenance](https://docs.cloud.google.com/memorystore/docs/redis/finding-and-setting-maintenance-windows#find_scheduled_maintenance).

## Rescheduling maintenance

If you have a maintenance window for your instance, you can reschedule maintenance at any time before maintenance is scheduled. For example, if you have a new service launching during your scheduled maintenance time, you might want to reschedule the maintenance window to a few days after your launch.

You can reschedule maintenance as long as it's not more than one week after the originally scheduled time. You can reschedule maintenance up to two times. As a result, you can extend the maintenance schedule for up to two weeks from the originally scheduled time.

You have a few scheduling options for the new maintenance window:

  * **Update now.** You can apply the update to your instance immediately instead of waiting for the scheduled maintenance window.
  * **Defer to next scheduled window.** This defers maintenance by one week.
  * **Custom day and time.** This lets you choose any specific time _within one week_ after the originally scheduled maintenance time.



Rescheduling maintenance has the following additional behavior:

  * You cannot reschedule maintenance if less than an hour remains before currently scheduled maintenance.
  * You cannot reschedule for multiple Redis instances with a single operation. They must be rescheduled individually.



For instructions on rescheduling maintenance see [Reschedule planned maintenance](https://docs.cloud.google.com/memorystore/docs/redis/finding-and-setting-maintenance-windows#reschedule_planned_maintenance).

**Caution:** Although Memorystore does not provide the option to reschedule maintenance for multiple instances at once, some Memorystore users with large instance counts opt to programmatically reschedule in bulk.   
  
If you are rescheduling in bulk, it is important to batch your operations into appropriate sized requests. We recommend limiting the batch size to 100 instances and waiting ample time between requests. Exceeding this limit can result in failed rescheduling events.

## FAQ

The following are some frequently asked questions about the maintenance policy for Memorystore for Redis:

#### What is the impact of maintenance on Standard Tier instances?

During maintenance, Standard Tier instances undergo a failover. A failover typically lasts for 15 seconds. After the failover, client applications need to reconnect. For more details on impact, see [Impact of maintenance](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy#impact_of_maintenance).

#### What is the impact of maintenance on Basic Tier instances?

Basic Tier instances are unavailable during maintenance which typically lasts about 5 minutes. For more details on impact, see [Impact of maintenance](https://docs.cloud.google.com/memorystore/docs/redis/maintenance-policy#impact_of_maintenance).

#### How do I know when maintenance is scheduled for my instance?

We recommend subscribing for notifications to learn when maintenance is scheduled for your instance. You can also check manually in the Cloud console. If the Cloud console is blank and you have already set a maintenance window, you do not have upcoming maintenance scheduled yet.

#### When am I notified of upcoming maintenance?

If you are subscribed for maintenance notifications and have set a maintenance window, you are alerted by email at least seven days before a maintenance event.

#### How long can I defer maintenance?

Once maintenance has been scheduled for your instance, you may start the update for your instance immediately or defer the update for up to seven days from the originally scheduled maintenance time. For example, if maintenance is scheduled for Oct. 11 at 11:15 PM, you can defer until Oct. 18 at 11:15 PM. Maintenance will be applied at the scheduled time if no action is taken.

For more details, see [Rescheduling maintenance](https://docs.cloud.google.com/memorystore/docs/redis/finding-and-setting-maintenance-windows#reschedule_planned_maintenance).

#### Will the IP address of my instance change during maintenance?

When you connect to a Memorystore for Redis instance, you specify the service IP address. This IP address will not be modified during maintenance or by any other action you take. By using the service IP address, the service will handle events like instance failover for you automatically.

#### What best practices should I follow for a smooth maintenance update experience?

We recommend you to take the following actions to ensure a smooth maintenance update experience:

  1. You should [set your maintenance window](https://docs.cloud.google.com/memorystore/docs/redis/finding-and-setting-maintenance-windows#set_a_preferred_window_for_maintenance_on_an_instance) to a time ensuring maintenance is not applied in your peak hours of Redis use.
  2. You should [opt-in to maintenance notifications](https://docs.cloud.google.com/memorystore/docs/redis/finding-and-setting-maintenance-windows#opt_in_to_maintenance_notifications) to be alerted by email at least seven days before a maintenance update is scheduled for your instance.
  3. Ensure that the [System Memory Usage Ratio](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#memory_management_concepts) metric is below 50% when maintenance starts. You can do this by scheduling for a time when instance traffic is low, or by temporarily scaling up your instance size during the maintenance window.



#### When should I apply maintenance immediately?

One circumstance when you should apply maintenance immediately is on a test instance to see how it will affect a production instance. You can [reschedule maintenance](https://docs.cloud.google.com/memorystore/docs/redis/finding-and-setting-maintenance-windows#reschedule_planned_maintenance) to have it apply immediately on a test instance. This allows you to observe the impact it has, and defer maintenance on production instances as needed/allowed.

#### Do maintenance updates always complete inside the maintenance window?

An update starts inside of the maintenance window you specify. The update usually completes within the window, but this is not guaranteed.

#### Can I opt out of maintenance or schedule maintenance on certain instances first?

No, you can neither opt out of maintenance nor control the initial scheduling of maintenance. However, you can [reschedule maintenance](https://docs.cloud.google.com/memorystore/docs/redis/finding-and-setting-maintenance-windows#reschedule_planned_maintenance) to defer it for up to seven days.

## What's next

  * View the [permissions](https://docs.cloud.google.com/memorystore/docs/redis/access-control#maintenance_policy_permissions) required to manage maintenance windows for your Redis instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
