---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-alloydb-maintenance/
title: Troubleshoot AlloyDB maintenance \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:34.139137+00:00
---

# Troubleshoot AlloyDB maintenance  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-alloydb-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Troubleshoot AlloyDB maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to resolve issues with AlloyDB for PostgreSQL maintenance events. AlloyDB maintenance ensures that your clusters and instances remain reliable, performant, secure, and up to date. For more information, see [Maintenance overview](https://docs.cloud.google.com/alloydb/docs/maintenance).

## Your database environment is disrupted during service-driven maintenance

**Description:** During AlloyDB maintenance operations, your database environment experiences sub-second downtime.

AlloyDB minimizes the disruption during maintenance by creating a virtual machine (VM) with the updates. When the replacement VM is ready, AlloyDB swaps it with the active VM.

The impact from the VM swap on instances is as follows:

  * **Primary instances:** typically experience <1 second of downtime.
  * **Read pool instances:** experience 0 seconds of downtime.



**Recommended fix:** Configure your database environment with robust retry logic so that your database and applications automatically reconnect.

Depending on your instance and database sizes, you can expect minor post-maintenance performance degradation. To minimize performance degradation, AlloyDB pre-warms the caches of replacement machines for a pre-set amount of time. This pre-warming is sufficient for most environments. If a time-out occurs before the caches are filled, the process continues after maintenance is complete.

## Your database environment is disrupted during user-driven maintenance

**Description:** When you make updates and configuration changes to your database environment—such as instance resizing or most database flag changes— your database environment experiences sub-second downtime.

By default, user-driven database configuration changes use the same non-disruptive maintenance operations as service-driven events, and the operation causes a sub-second downtime. While downtime is brief, the overall operation length can extend beyond 15 minutes. For more information, see [Maintenance overview](https://docs.cloud.google.com/alloydb/docs/maintenance).

**Recommended fix:** When you update your database environment, you can't avoid the sub-second downtime of the primary instance, but you can plan for the momentary connection drop.

## Your database experiences minor performance degradation after user-driven maintenance

**Description:** After user-driven maintenance, your database experiences minor performance degradation.

**Recommended fix:** For user-initiated maintenance, AlloyDB aims to prevent performance slowdowns by pre-warming the caches of replacement machines for up to five minutes. While this is usually sufficient, some environments may still experience unavoidable performance degradation. The pre-warming duration is generally shorter for user-driven changes than for service-driven maintenance. If a timeout occurs before the caches are fully loaded, the cache-filling process resumes after the maintenance window is complete.

## When you use the FORCE_APPLY flag, your database experiences downtime

**Description:** You use the optional `FORCE_APPLY` flag to make changes to your database. 

Expect downtime when you use the `FORCE_APPLY` flag option. Using this flag restarts the instance, which makes the database unavailable for a few minutes.

**Note:** Use the `FORCE_APPLY` flag option with caution. `FORCE_APPLY` is primarily useful in test and development environments when downtime is acceptable. This flag has limited use in production environments.

## You experience unexpected maintenance on your production cluster

**Description:** Your production cluster experiences an unexpected maintenance update.

**Recommended fix:** To avoid unexpected maintenance on your production cluster, schedule the maintenance period so that you know when the maintenance event will occur.

To schedule a maintenance window on your clusters, see [Manage AlloyDB for PostgreSQL cluster maintenance windows](https://docs.cloud.google.com/alloydb/docs/maintenance-windows).

If you don't schedule a maintenance window, non-emergency maintenance for an AlloyDB cluster can occur any time except between 6 AM and 10 PM on weekdays in the local time of the region where the cluster is located.

You can schedule a maintenance window for any one-hour window on any day of the week.

To receive a reminder of the scheduled maintenance on your production cluster, opt in to receive email notifications before your scheduled maintenance.

You can also prevent maintenance operations during a specific time period by configuring a deny maintenance period that can span 1 to 30 days. For more information, see [Configure a deny maintenance period](https://docs.cloud.google.com/alloydb/docs/maintenance-windows#configure-deny-maintenance-period).

**Note:** Maintenance windows and deny maintenance windows don't apply to emergency rollouts, such as urgent security fixes. AlloyDB applies these fixes immediately regardless of your scheduled maintenance window.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
