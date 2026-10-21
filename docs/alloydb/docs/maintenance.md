---
url: https://docs.cloud.google.com/alloydb/docs/maintenance/
title: Maintenance overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:40.259008+00:00
---

# Maintenance overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Maintenance overview Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB for PostgreSQL clusters and instances rely upon many internal, low-level Google Cloud resources. These include the virtual machine (VM) instances that serve as AlloyDB nodes and load balancers, and the storage volumes that hold your data. Because AlloyDB is a managed service, Google keeps these internal resources up to date. This helps ensure that your AlloyDB clusters and instances stay reliable, performant, and secure.

Most of these updates require no downtime, but certain system updates require a brief service interruption. We refer to these updates as _maintenance updates_. Because these updates require the affected node to restart, they can incur downtime. Non-disruptive maintenance operations in AlloyDB limit the downtime to less than one second for primary instances, and zero seconds for read pools. To achieve near-zero and zero downtime, AlloyDB prepares a replacement server with the updates and then switches the database server.

For more information, see [View and set maintenance times](https://docs.cloud.google.com/alloydb/docs/maintenance-windows) and [Manage AlloyDB maintenance updates using a staging cluster](https://docs.cloud.google.com/alloydb/docs/manage-maintenance-updates-staging-cluster).

## Reasons for maintenance

Periodic maintenance updates can happen for the following reasons:

  * **New AlloyDB features and bug fixes:** to launch new features, Google must update the AlloyDB software that runs on the nodes within your cluster. This might also involve updates to the PostgreSQL extensions included with AlloyDB, or installation of new extensions. Updates might also include bug and security fixes, or performance improvements.

  * **Database compatibility upgrades:** the PostgreSQL community regularly releases minor-version updates to supported major versions of PostgreSQL. Google incorporates these updates into AlloyDB, and applies them to your clusters. For more information, see [Database version policies](https://docs.cloud.google.com/alloydb/docs/db-version-policies).




## Maintenance timing and maintenance preferences

**Note:** To access new AlloyDB features, you must have the latest AlloyDB system software version. If you have a maintenance window set for your AlloyDB cluster, you might not have the latest software version.

You can set maintenance windows for both primary and secondary AlloyDB clusters. By default, no maintenance window is set on an AlloyDB cluster. Non-emergency maintenance for an AlloyDB cluster with no configured maintenance windows can occur any time except for the hours between 6 AM and 10 PM on weekdays, in the local time of the region where the cluster is located.

You can also [specify a _maintenance window_](https://docs.cloud.google.com/alloydb/docs/maintenance-windows#set-window). A maintenance window defines your preferred maintenance time, in terms of hour-of-day and day-of-week, for your cluster to begin its maintenance events. For example, you can set a cluster to have a maintenance window that begins at 11AM on Sundays (UTC).

If you set a maintenance window, then AlloyDB schedules future non-emergency maintenance events to begin no later than one hour after the specified time. In addition, if you [opt in to receive email notifications](https://docs.cloud.google.com/alloydb/docs/maintenance-windows#opt-in) about scheduled AlloyDB maintenance events, then you receive an automated notification about the event as soon as it's scheduled. Maintenance events are scheduled at least one week ahead of time.

You can't set when a maintenance window ends. This is because the total time that a single maintenance event requires can vary. The maintenance window duration depends upon the complexity of the cluster—that is, the number of read pool instances that require updates—and the nature of the update. AlloyDB first updates the read pools simultaneously, and then it updates the primary instance.

While the downtime that an individual instance requires can be brief, the entire maintenance process usually completes within an hour. You can only set a one-hour maintenance window. However, for clusters with multiple read pools, the downtime might continue past the one-hour window because the maintenance can start at any time in that window—for example, at the last minute—and then take up to an hour. This means that the downtime can occur after the maintenance window.

Emergency maintenance events, such as urgent security patches, might occur outside default maintenance times or configured maintenance windows. This includes deny maintenance periods.

## Latest available version

For clusters without a maintenance window set, maintenance is applied to clusters by region. This means that clusters in some regions receive and can access the latest version sooner than clusters in other regions.

AlloyDB [release notes](https://docs.cloud.google.com/alloydb/docs/release-notes) and [maintenance changelogs](https://docs.cloud.google.com/alloydb/docs/maintenance-changelog/overview) are published soon after maintenance is complete for all regions. Clusters with maintenance windows typically receive updates after the changelog and release notes are updated.

## Self-service maintenance

If you need to apply maintenance and update your clusters to the latest version ahead of your scheduled maintenance window, you can perform self-service maintenance. Updating to the latest version can unlock features, apply patches, and let you set a deny period on your cluster. For more information, see [Perform self-service maintenance](https://docs.cloud.google.com/alloydb/docs/self-service-maintenance).

## What's next

  * [View and set maintenance times](https://docs.cloud.google.com/alloydb/docs/maintenance-windows).
  * [Manage AlloyDB maintenance updates using a staging cluster](https://docs.cloud.google.com/alloydb/docs/manage-maintenance-updates-staging-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
