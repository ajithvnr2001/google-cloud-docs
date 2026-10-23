---
url: https://docs.cloud.google.com/managed-lustre/docs/maintenance/
title: Maintenance overview \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:05.297984+00:00
---

# Maintenance overview  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Maintenance overview Stay organized with collections  Save and categorize content based on your preferences. 

To keep your Google Cloud Managed Lustre instances up-to-date, Google Cloud periodically performs maintenance on them. Maintenance events include updates to the underlying software or infrastructure.

Maintenance is performed automatically on all Managed Lustre instances, and by default can occur at any time.

Managed Lustre provides two ways to manage the timing of maintenance on your instances:

  * **Maintenance policies** : Configure recurring weekly windows and exclusion periods to control when automated maintenance can occur.
  * **Self-service maintenance** : Perform maintenance on demand.



## Maintenance policies

To control when automated maintenance can occur on your instance, you can configure a _maintenance policy_. A maintenance policy consists of one or both of the following:

  * **Weekly maintenance window** : A recurring one-hour window during the week when Google Cloud is permitted to start maintenance.
  * **Maintenance exclusion window** : A period of up to two weeks, optionally recurring annually, where maintenance is blocked.



You can subscribe to receive email notifications of upcoming scheduled maintenance events. Notifications are sent from 7 to 14 days before an event. You can also reschedule a maintenance event to start immediately, during the next weekly window, or at a specific date and time up to 28 days later.

For instructions on configuring policies and rescheduling, see [Configure maintenance policies](https://docs.cloud.google.com/managed-lustre/docs/maintenance-policies).

## Self-service maintenance

Self-service maintenance lets you upgrade your instance to a newer software version on demand, as soon as a new version is available. New versions are available for self-service maintenance up to several weeks before automated maintenance reaches your instance.

For step-by-step instructions, see [Perform self-service maintenance](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance).

## Impact of maintenance

Maintenance is performed in-place. Your system data, customer-managed encryption keys, and client mount points are preserved throughout the maintenance process.

During maintenance, an instance's status transitions from `ACTIVE` to `UPGRADING` while the upgrade is applied. I/O operations to the instance temporarily pause. Affected I/O operations resume automatically once maintenance is complete and the instance returns to `ACTIVE`. Downtime is typically between 15 to 20 minutes.

## Maintenance notifications and logs

To receive email notifications for automated maintenance events, or to view maintenance records in Cloud Logging, see [Maintenance notifications and logs](https://docs.cloud.google.com/managed-lustre/docs/maintenance-notifications).

## What's next

  * [Configure maintenance policies](https://docs.cloud.google.com/managed-lustre/docs/maintenance-policies)
  * [Perform self-service maintenance](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance)
  * [Maintenance notifications and logs](https://docs.cloud.google.com/managed-lustre/docs/maintenance-notifications)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
