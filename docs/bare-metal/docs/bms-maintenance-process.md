---
url: https://docs.cloud.google.com/bare-metal/docs/bms-maintenance-process/
title: Bare Metal Solution maintenance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:43.451913+00:00
---

# Bare Metal Solution maintenance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-maintenance-process/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bare Metal Solution maintenance

This page provides an overview of the process for Bare Metal Solution maintenance events that require server downtime.

To ensure that your Bare Metal Solution environment remains reliable, secure, and up-to-date, Google Cloud occasionally performs scheduled maintenance on the underlying Bare Metal Solution hardware and infrastructure. We perform many updates while your servers are running. However, some updates require downtime. In either case, we notify you about the scheduled maintenance and alert you if you need to take any actions to prepare for the maintenance.

We recommend that you allow the maintenance to be performed in the scheduled window for the following reasons:

  * If you receive a maintenance notification for your server, it means that your server is running in a degraded state and must be attended as soon as possible to keep it running well and reduce the risk of unexpected failure and downtime.
  * Regular maintenance helps keep your server functional over a long period of time. 



Bare Metal Solution performs the following two types of maintenance:

  * **Infrastructure maintenance** —Includes the maintenance of the networking devices and storage components at the data center.

We notify you when an infrastructure maintenance takes place. Infrastructure maintenance notifications are only informational and do not need you to respond.

  * **Server maintenance** —Includes server maintenance activities, such as hardware replacement, patches, upgrades, and configuration changes.

For maintenance activities that do not impact your server (such as replacement of a hot-swappable and redundant power supply), we send you informational notifications to which you do not need to respond. 

However, to perform maintenance that affects your server and requires downtime (such as DIMM replacement), we need your permission.

To collaborate with you on such a maintenance activity, we create a _maintenance event_. A maintenance event lets you view the details of a maintenance activity and take an appropriate action, such as approving or rescheduling the maintenance.




## How maintenance works

Maintenance takes a lot of planning and coordination. It's a two-sided operation and requires you and us to work together to keep your servers functioning well.

To complete maintenance efficiently with minimal delay, we recommend that you read about and understand this process.

The following flowchart shows the steps involved in the Bare Metal Solution maintenance process:

![Steps involved in the Bare Metal Solution maintenance process.](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-maintenance-process.svg)

The following sections describe each of the steps in detail.

### Google creates a maintenance event

Ideally, we create a maintenance event two to three weeks before your server is due for maintenance. We use this event to coordinate and confirm with you to prevent or minimize disruption to your Bare Metal Solution environment. The event contains all the details about the maintenance activity and steps you need to take to prepare for the maintenance.

**Note:** If we need to perform an urgent maintenance activity on your server, you might receive less than three weeks notice from us.

You can [view your maintenance events](https://docs.cloud.google.com/bare-metal/docs/manage-maintenance-events#view-maintenance-event) in the Google Cloud console.

We send you reminders about your upcoming maintenance events seven days, three days, and one day before the maintenance event with preparatory steps for the event to be successful.

### User reviews the maintenance event

We recommend that you read the details and impact of the event carefully. After you've reviewed the maintenance event, you can take the following actions:

  * If you're okay with the proposed window, [approve the maintenance event](https://docs.cloud.google.com/bare-metal/docs/manage-maintenance-events#approve-maintenance-event).
  * If you're not okay with the proposed window, [reschedule the maintenance event](https://docs.cloud.google.com/bare-metal/docs/manage-maintenance-events#reschedule-maintenance-event) to propose a new window.

**Warning:** If you do not respond by five days before the scheduled start date, we might need to cancel or reschedule the maintenance event.

After we receive your response, we schedule your maintenance event. 

We do not recommend canceling a maintenance event. But, if you still need to cancel a maintenance event due to business-critical reasons, see [Cancel a maintenance event](https://docs.cloud.google.com/bare-metal/docs/manage-maintenance-events#cancel-maintenance-event). 

### User prepares for the maintenance event

You must complete the preparation as explained in [Prepare for a maintenance event](https://docs.cloud.google.com/bare-metal/docs/prepare-for-maintenance) before the maintenance event starts.

You must also complete any additional steps explained in your maintenance event.

**Warning:** Failure to complete the preparatory steps before the maintenance event starts can result in the cancellation of the maintenance event. If we cancel your maintenance event, then your server keeps running in a degraded state until its maintenance is done. Therefore, we recommend that you complete the preparatory steps.

### Maintenance event takes place

We notify you when the maintenance event starts and when the maintenance event ends. These notifications are informational and do not require you to respond.

If the maintenance does not complete as planned, we reach out to you about the issues and next steps, including options to continue the maintenance event or revert the server to its previous state.

If you are unreachable or unavailable to respond in time, we roll back the changes and return the server to its previous state.

## What's next

  * [Prepare for a maintenance event](https://docs.cloud.google.com/bare-metal/docs/prepare-for-maintenance).
  * [Manage your maintenance events](https://docs.cloud.google.com/bare-metal/docs/manage-maintenance-events#cancel-maintenance-event).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
