---
url: https://docs.cloud.google.com/sql/docs/postgres/maintenance/
title: Maintenance updates on Cloud SQL instances \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:54.257457+00:00
---

# Maintenance updates on Cloud SQL instances  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Maintenance updates on Cloud SQL instances Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/maintenance "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance "View this page for the SQL Server database engine")

This page explains how maintenance updates occur on Cloud SQL instances, and how you can control the timing of these updates. To get started, see [View and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

**Note:** This page contains features related to Cloud SQL editions. For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/postgres/editions-intro). 

## Overview

As a managed service, Cloud SQL automatically updates instances to ensure that the underlying hardware, operating system, and database engine are reliable, performant, secure, and up-to-date. Most of these updates are performed while your Cloud SQL instance is up and running. However, certain system updates require a brief service interruption to be performed. These updates are called _maintenance_.

Maintenance updates the database engine, and in some cases, the operating system. Because these updates require the instance to be restarted, they incur some downtime. Maintenance updates deliver the following benefits:

  * **Cloud SQL features.** To launch new features, the database engine is updated and new plugins to the database are installed.

  * **Database version upgrades.** The database software provider that develops PostgreSQL releases new minor versions several times a year. With each new version come bug fixes, security patches, performance enhancements, and new database features. You can find the latest minor version that Cloud SQL for PostgreSQL supports by reviewing [release notes](https://docs.cloud.google.com/sql/docs/postgres/release-notes) or [Database versions and version policies](https://docs.cloud.google.com/sql/docs/postgres/db-versions). Cloud SQL instances are upgraded to the latest database version shortly after release, so that you benefit from running the latest database software. 

  * **Operating system patches**. We continuously monitor for newly identified security vulnerabilities in the operating system. Upon discovery, we patch the operating system to protect you from new risks.




## Maintenance impact

For [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/postgres/editions-intro), Cloud SQL offers [near-zero downtime planned maintenance](https://docs.cloud.google.com/sql/docs/postgres/maintenance#nearzero).

Cloud SQL schedules a maintenance update event typically once every few months. The maintenance update can take approximately 5 to 10 minutes for each instance. If the instance has read replicas, then the overall duration of the maintenance update can take longer. However, during the maintenance update event, each Cloud SQL Enterprise edition instance loses connectivity for less than 30 seconds on average. Downtime might be higher for an instance that is undergoing high amounts of activity during the maintenance update event or has a very large dataset.

You can take steps to ensure that maintenance has as little impact as possible on your operations by using our maintenance settings and by making your systems resilient to transient errors.

**Caution:** Maintenance is canceled if an instance operation, such as an [export](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-sql#export), is ongoing at the time when a maintenance event is scheduled to begin. Ensure that no other instance operations are planned when maintenance is scheduled. 

In addition, if disk usage on the instance is higher than 97%, then Cloud SQL skips the maintenance update for the instance.

## Near-zero downtime planned maintenance

**Note:** This feature is available with Cloud SQL Enterprise Plus edition only. For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/postgres/editions-intro). 

With near-zero downtime planned maintenance, Cloud SQL Enterprise Plus edition instances typically lose connectivity for less than 1 second during planned maintenance.

The downtime might be higher for instances that have high activity during the maintenance.

### Prerequisites and constraints

  * Read replicas aren't supported.


  * If you are using [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy) or [Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/postgres/language-connectors), ensure that they are updated to their latest version.

  * Any unlogged tables will be empty after planned maintenance.



  * During maintenance, the database logs will have messages from two different VMs.
  * If a DDL is issued during the planned maintenance, the changes might have a creation or modification timestamp that is after the maintenance timestamp.
  * Client-side connection strings and query settings, such as connection type, query timeouts, and connection pooling, can all impact observed downtime. Be sure to test your application's setup configuration to find the settings that best fits your needs.



### Simulate near-zero downtime planned maintenance

To test the planned maintenance downtime of your Cloud SQL Enterprise Plus edition primary instance without updating your database instance, you can simulate near-zero downtime planned maintenance.

To do this, invoke the simulation of a maintenance event on a Cloud SQL Enterprise Plus edition instance that is eligible for near-zero downtime planned maintenance. The simulation request results in an instance update operation to the same maintenance version before the operation.

You can perform the simulation even if you have a maintenance update pending on the instance. The instance version remains the same throughout the simulation.

To simulate a near-zero downtime planned maintenance event, use the following [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) command:
    
    
    gcloud sql instances patch INSTANCE_NAME --simulate-maintenance-event

Replace INSTANCE_NAME with the name of the instance where you want to run the simulated maintenance event.

## Maintenance settings

Cloud SQL offers you the ability to configure maintenance updates through a set of maintenance settings.

You can configure maintenance to be scheduled at times when brief downtime causes the lowest impact to your applications. For each Cloud SQL instance, you can configure the following:

  * **Maintenance timing** (previously **Order of update**). The week of the rollout period to update your Cloud SQL instance. You have the following options:

    * `Any`: the maintenance update can happen at any time, but typically happens within Week 1.
    * `Week 1`: the maintenance happens 7 to 14 days after the maintenance notification is sent out.
    * `Week 2`: the maintenance update happens 15 to 21 days after the notification is sent out.
    * `Week 5`: the maintenance update happens 35 to 42 days after the notification is sent out.

You set the schedule of the maintenance update when you [ configure a maintenance window](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window#set-maintenance).

  * **Maintenance window**. The day of the week and the hour in which Cloud SQL schedules maintenance. Maintenance windows last for one hour. Learn [ how to configure a maintenance window](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window#set-maintenance).

  * **Deny maintenance period**. A block of days in which Cloud SQL does not schedule maintenance. You can set a deny maintenance period for up to 90 days long. Learn [ how to configure a deny maintenance period](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window#configure-deny-maintenance).




### Default maintenance windows

If you don't set a maintenance window, then Cloud SQL updates your instance in the following default windows according to your instance's time zone:

  * Weekday window (Monday to Friday): 10 PM to 6 AM
  * Weekend window: Friday, 10 PM to Monday, 6 AM



### Maintenance example

Assume you are a developer at a retailer managing a shopping cart service. You have one Cloud SQL instance for a production environment and a second for a staging environment. You want maintenance to occur at the time when your instance handles the lowest amount of traffic, which is around midnight on Sundays. You also want to skip maintenance during your busy end-of-year holiday shopping season.

In this case, you set your production instance's maintenance settings to:

  * Maintenance window: Sundays between 12:00AM and 1:00AM ET
  * Maintenance timing: `Week 2`
  * Deny maintenance period: November 1 through January 15.



The maintenance settings for your staging environment would be identical, except the maintenance timing is set to `Week 2`. This ensures you can run operational acceptance tests for a maintenance release in staging at least seven days before maintenance rolls out to production. If something goes wrong in the staging environment, you have time to diagnose and fix the issue or set up a deny maintenance period that your production environment is unaffected.

## Upcoming maintenance notifications

You can have a notification about upcoming maintenance sent to your email at least one week before maintenance is scheduled. If you want to set an email filter for notifications, the email title is **Upcoming maintenance for your Cloud SQL instance _instancename_**.

Notifications for maintenance aren't sent out by default. You need to [opt in to maintenance notifications](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window#opt-in). Before you can receive notifications, you must also select a maintenance window.

Notifications are sent to the email address associated with your Google Account. It's not possible to configure a custom email alias (for instance, a team email alias).

You opt into maintenance notifications for all Cloud SQL instances that have maintenance windows in a given project. You receive one notification per instance. Upcoming maintenance notifications are not sent out for read replicas.

**Note:** The time given in the maintenance notification is approximate. Maintenance does not start before this time, but it might occur several minutes after the scheduled time.

You can also view upcoming maintenance information in the Google Cloud console.

  * In the **Instances** list, in the **Maintenance** column. If maintenance is scheduled, you see the date and time for when it is scheduled to start. You can filter the instances list using the term **Maintenance** to find all the instances scheduled for maintenance. The **Maintenance** column only displays when maintenance is scheduled on one or more instances in the project. If no maintenance is scheduled, the column is hidden.
  * On the **Instance details** page in the **Maintenance** pane. If maintenance is scheduled, under **Upcoming** , you see a date and time for when it is scheduled to start.
  * On the **[Logs explorer](https://console.cloud.google.com/logs)** page in the Google Cloud console. Use the **All logs name** drop-down to search for `maintenance-events`, then click **Apply**. If maintenance is scheduled for an instance, then the log shows the name of the instance and its scheduled maintenance start time.

**Note:** If the `Activity information is not found on the Logs Explorer page` status message appears in the **ACTIVITY** page, make sure you have the `[resourcemanager.projects.get](https://docs.cloud.google.com/resource-manager/docs/access-control-proj)` permission assigned to you. For more information about assigning permissions, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/postgres/roles-and-permissions).



### Other maintenance notifications

When you opt in to receive maintenance notifications, you will be notified of certain events:

  * Upcoming scheduled maintenance
  * Started maintenance
  * Completed maintenance
  * Canceled maintenance



## Reschedule maintenance

If you have a maintenance window for your instance, then you can reschedule the maintenance update up to 24 hours before the maintenance update is scheduled to occur. For example, if you are launching a new service during your scheduled maintenance window, then you might want to postpone the maintenance update to a few days after your launch.

There are some limits to rescheduling maintenance updates. After Cloud SQL sends out the notification email, Cloud SQL performs the maintenance update within a seven-week time period to avoid any overlap with the next Cloud SQL maintenance update. For example, if you select a maintenance timing of Week 1 or Week 2, then you can reschedule the maintenance update up to a maximum of 4 weeks (28 days) after the originally scheduled date. If you set your instance to a maintenance timing of Week 5, then you can only reschedule the maintenance event up to a maximum of one week (7 days) after the original date. You can reschedule maintenance multiple times as long as the rescheduled maintenance event is within the rescheduling duration defined by the maintenance timing that you configured for your instance.

For all other limitations, see Reschedule limitations.

You have a few scheduling options for the new maintenance window:

  * **Apply updates immediately.** You can apply the update to your instance immediately instead of waiting for the scheduled maintenance window. In this case, maintenance generally starts within five minutes.
  * **Reschedule to another time.** You can postpone a scheduled maintenance event in two ways:

    * **Next available window.** This option defers maintenance to the next available maintenance window following the current scheduled maintenance time, which is typically one week later.
    * **Specific time.** This option lets you choose a specific time the rescheduling duration defined by the maintenance timing that you configured for your instance. 
      * 28 days if you select Week 1 or Week 2 maintenance timing
      * 7 days if you select Week 5 maintenance timing



For instructions on how to reschedule maintenance, see [Reschedule planned maintenance](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window#reschedule).

## How maintenance works

To keep maintenance brief, Cloud SQL uses a maintenance failover workflow that largely resembles our [ automatic failover workflow](https://docs.cloud.google.com/sql/docs/postgres/high-availability#failover-overview) for highly available instances.

In short, these are the steps:

  1. Set up an updated VM with the new software.
  2. Stop the database on the original VM.
  3. Switch over the disk and static IP to the updated VM.
  4. Start the database on the updated VM.



Step through the following tabs to see details of the workflow, including pre- and post-maintenance.

### Pre-maintenance

Before maintenance, the client communicates with the original VM through a static IP address. The data is stored on a persistent disk that is attached to the original VM. In this example, the Cloud SQL instance has high availability configured, which means that another VM is on standby to take over in the event of an unplanned outage. The Cloud SQL instance is serving traffic to the application. 

![Diagram showing the pre-maintenance state](https://docs.cloud.google.com/static/sql/images/maintenance1.svg)

### Step 1

**Set up the new VM.**

a new Virtual Machine (VM) is set up with the latest database software and VM operating system (OS). The updated VM OS is started. At this point, the database engine is not yet started. For highly available instances, a new standby VM is also set up. 

The total downtime is substantially shortened by installing the software update on another VM while the original Cloud SQL instance is still serving traffic. 

![Diagram showing setting up the VM](https://docs.cloud.google.com/static/sql/images/maintenance2.svg)

### Step 2

**Stop the database on the original VM.**

The database engine is shut down so that the disk can be detached from the original VM and attached to the updated VM. Before shutting down, the database engine waits for a few seconds for ongoing transactions to be committed and requests from existing connections to drain. After that, any open or long-running transactions are rolled back. The database stops accepting new connections, and existing connections are dropped. The instance becomes unavailable and maintenance downtime begins. 

![Diagram of instance after failover](https://docs.cloud.google.com/static/sql/images/maintenance3.svg)

### Step 3

**Switch over to the updated VM.**

The disk is detached from the original VM and attached to the updated VM. The static IP address is reconfigured to point to the updated VM. This ensures that the application uses the same IP address after maintenance as before. The database cache is cycled out with the original VM, meaning that the database cache is effectively cleared during maintenance. 

![Diagram of switching over to updated VM](https://docs.cloud.google.com/static/sql/images/maintenance4.svg)

### Step 4

**Start the database on the updated VM.**

The updated database engine is started on the data disk. Using a common data disk ensures that all transactions written to the original instance prior to maintenance are still present on the updated database after maintenance. If any incomplete transactions didn't finish rolling back during database shutdown, the database automatically goes through crash recovery to ensure that the database is restored to a usable state. 

![Diagram of starting up the updated VM](https://docs.cloud.google.com/static/sql/images/maintenance5.svg)

### Post-maintenance

After Step 4, the Cloud SQL instance is available to accept connections and it returns to serving traffic to the application. 

To the application, apart from the updated software, the Cloud SQL instance looks the same. The application still connects to the Cloud SQL instance using the same static IP address, and the updated VM runs in the same zone as the original VM. All data written to the original database is preserved. 

![Diagram of post-maintenance](https://docs.cloud.google.com/static/sql/images/maintenance6.svg)

## Minimize the impact of maintenance

In general, Google Cloud recommends that users running applications in the cloud make their systems resilient to transient errors, which are momentary inter-service communication issues caused by temporary unavailability. Occasional transient errors are unavoidable in the cloud.

Some of the transient errors that occur during maintenance are dropped connections and failed in-flight transactions. If you design your systems and tune your applications to be resilient to transient errors, you're also positioned to minimize impacts due to database maintenance.

To minimize the impact of dropped connections, you can use [connection pools](https://docs.cloud.google.com/sql/docs/postgres/manage-connections#pools). While connections between the pooler and the database are dropped during maintenance, the connections between the application and the pooler are preserved. That way, the work of reestablishing the connections is transparent to the application and offloaded to the connection pooler instead.

To reduce the transaction failures, you can limit the number of long-running transactions. Rewriting queries to be smaller and more efficient not only reduces maintenance downtime, but also improves database performance and reliability.

You can use [Query Insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights) to identify slow queries. 

To recover efficiently from connection drops and transaction failures, you can efficiently [manage your database connections](https://docs.cloud.google.com/sql/docs/postgres/manage-connections). You can build connection and query retry logic with [exponential back-off](https://docs.cloud.google.com/sql/docs/postgres/manage-connections#backoff) into your applications and connection poolers. In the event that a query fails or a connection is dropped, the system institutes a wait period before retrying, which increases for each subsequent retry. For example, the system might wait just a few seconds for the first retry, but up to a minute for the fourth retry. Following this pattern ensures that these failures are corrected, without overloading the service.

Other creative solutions can minimize maintenance impacts as well, from using scripts to warm the database cache after maintenance to streamlining the number of tables in databases. We recommend following database management [best practices](https://docs.cloud.google.com/sql/docs/postgres/best-practices) and [operational guidelines](https://docs.cloud.google.com/sql/docs/postgres/operational-guidelines) to ensure that maintenance goes smoothly.

## Time-sensitive maintenance

In very rare cases, Cloud SQL might need to schedule maintenance outside of your maintenance settings to patch severe stability issues or vulnerabilities that are time-sensitive. These updates are delivered rapidly, and Cloud SQL counts them as downtime against the SLA.

## Self-service maintenance

Cloud SQL regularly releases software improvements and patches to security vulnerabilities through new maintenance versions that you can install on your instances. Cloud SQL maintains a [Cloud SQL maintenance changelog](https://docs.cloud.google.com/sql/maintenance-changelog) for each database engine major version. To learn more, see [Cloud SQL maintenance changelogs](https://docs.cloud.google.com/sql/maintenance-changelog).

While Cloud SQL schedules maintenance updates once every few months to ensure you have the latest software, you can use [self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance) to keep your instance up-to-date if:

  * You need an update sooner than your next scheduled maintenance event.
  * You want to catch up to the latest software after skipping your most recent maintenance update.



If you use read replicas, then you can use self-service maintenance to [update the primary instance and all of its read replicas](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance#update-all-read-replica-instances). You specify the primary instance, and the maintenance request updates all of the read replicas of the primary instance to the specified maintenance version. Then the primary instance is updated to the maintenance version.

## Maintenance limitations

This section describes the limitations of Cloud SQL maintenance.

### Reschedule limitations

There are a few things you need to know about rescheduling:

  * You must reschedule maintenance at least 24 hours before the originally scheduled maintenance event happens.

  * You can reschedule maintenance on one or multiple instances in your project. However, you can only reschedule one instance at a time (bulk rescheduling is not available).

  * You can reschedule maintenance to a time that falls within a deny maintenance period, or even outside the maintenance window, as long as the rescheduling duration is within the time period defined by the maintenance timing that you configured for your instance.

  * If a maintenance operation is in progress, rescheduling is delayed until the operation is complete.




### Deny maintenance period limitations

There are a few things you need to know about deny maintenance periods:

  * Starting on August 15, 2025, you can't set a deny maintenance period for an instance if its maintenance version is older than 12 months. Any instance that uses a maintenance version older than 12 months must receive an update. To find the date of the maintenance version installed on your instance, use the `gcloud sql instances describe` command, or view the **Maintenance** section of the **Instance overview** page in the Google Cloud console. For more information about finding the maintenance version of your instance, see [View instance information](https://docs.cloud.google.com/sql/docs/postgres/instance-info). To determine its release date, check the name of the maintenance version. For example, if the name of the maintenance version is `POSTGRES_16_9.R20250302.00_31`, then its corresponding release date is March 2, 2025.

To update the instance, [perform self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance) or wait for the automatic update during the [next maintenance window](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window#find-maintenance-api). After you update the instance, you can set a deny maintenance period.

  * You can have a deny maintenance period even if you don't have maintenance windows configured for your instance. Deny maintenance periods can span from 1 to 90 days.

  * The deny maintenance period takes precedence over any scheduled maintenance window. If there is a conflict between the timing of a maintenance window and the deny maintenance period, the deny maintenance period overrides the maintenance window.

  * Deny maintenance periods and maintenance timing are independent features. If you create a deny maintenance period for an instance that has `Week 1` maintenance timing, it has no impact in determining the scheduled update for an instance with `Week 2` maintenance timing. If a scheduled maintenance update falls within a deny maintenance period, then Cloud SQL doesn't send out a notification for the instances that you have configured with maintenance timing.

  * When a deny period is set on a primary instance, maintenance for all replicas associated with the primary instance is also denied. As an example, a primary instance located in region A has three read replicas: two in region A and one in region B. When a deny period is set on the primary instance, maintenance to each of the replicas, including the replica in region B, does not receive maintenance until the deny period on the primary instance expires.

  * If a deny maintenance period is set after maintenance is scheduled such that the deny maintenance period overlaps with the scheduled maintenance time, the update is skipped.

  * You can set the deny maintenance period to recur every year by not including the year in the start and end date parameters. If the year is specified, the deny maintenance period is set for only that year.

  * You can set multiple deny maintenance periods in a year. However, you can't set a deny maintenance period for an instance that's running a maintenance version older than 12 months. Avoid chaining deny periods together to skip consecutive scheduled maintenance events. Staying current on Cloud SQL maintenance is important to ensure that your instance operates reliably. Typically, Cloud SQL maintenance is scheduled once every few months.

  * In order to help ensure service reliability, Cloud SQL notifies users with instances running maintenance releases that are more than 12 months old that the next maintenance rollout is required.

  * When a deny maintenance period ends, regular maintenance behavior resumes.

  * Deny maintenance periods don't affect user-triggered operations, such as self-service maintenance.

  * Deny maintenance periods continue to apply after you stop, start, or restart an instance. When an instance is within an active deny maintenance period, if you stop and then start, or restart the instance, then any scheduled maintenance updates are skipped when the instance starts up again because the deny maintenance period is still active.




## Maintenance FAQ

  * Does maintenance downtime count toward the SLA?
  * How does maintenance affect read replicas?
  * Can I cancel scheduled maintenance?
  * What happens if the maintenance event is canceled?
  * Is Cloud SQL maintenance cumulative?
  * What happens if the instance is stopped during its scheduled maintenance update?
  * How long does self-service maintenance take for all the read replicas of a primary instance?
  * If I have multiple read replicas of my primary instance, can I do self-service maintenance on a single read replica?



### Does maintenance downtime count toward the SLA?

Downtime from normal maintenance does not count towards the SLA. However, Cloud SQL counts time-sensitive maintenance downtime against the SLA.

### How does maintenance affect read replicas?

  * Cloud SQL always maintains read replicas before the primary instance. If the primary instance has a maintenance window, read replicas observe the same maintenance window.
  * If your primary instance has multiple read replicas, Cloud SQL might update some of the replicas simultaneously.
  * Read replicas observe the deny maintenance period set for the primary instance.



### Can I cancel scheduled maintenance?

You can't cancel a scheduled maintenance window, but you can reschedule it. You can also configure a deny maintenance period that overlaps with the scheduled maintenance time to effectively skip maintenance.

### What happens if the maintenance event is canceled?

If Cloud SQL cancels a maintenance event, you receive a notification that maintenance is canceled in advance, when possible.

You receive a new notification of upcoming maintenance when the maintenance event is rescheduled.

### Is Cloud SQL maintenance cumulative?

Maintenance updates are cumulative. There's no need to apply each maintenance update that you might have missed. The latest maintenance version is applied in the next scheduled maintenance update. Or, you can apply the latest maintenance update using [self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance).

### What happens if the instance is stopped during its scheduled maintenance update?

If an instance is stopped during its scheduled maintenance update, then Cloud SQL skips the maintenance update. However, the next time that you restart the instance, Cloud SQL updates the instance with the latest maintenance update automatically.

### How long does self-service maintenance take for all the read replicas of a primary instance?

The amount of time that a self-service maintenance update takes depends on the total number of read replicas of your primary instance. To reduce the amount of time that the self-service maintenance update might take, you can update a few read replicas individually and then perform the update on the primary instance to update the rest of the read replicas.

The second update skips any replicas that already have the target maintenance version.

### If I have multiple read replicas of my primary instance, can I do self-service maintenance on a single read replica?

Yes, you can perform self-service maintenance on an [ individual read replica instance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance#update-single-instance). However, we recommend that you update the rest of the read replicas and primary instance to the same maintenance version soon afterwards. We recommend that you operate all the read replicas and primary instance with an identical maintenance version.

## What's next

  * See how to [opt in to maintenance notifications](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window#opt-in).
  * See how to [set a maintenance window](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window#set-maintenance).
  * See how to [view maintenance notifications](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window#find-maintenance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
