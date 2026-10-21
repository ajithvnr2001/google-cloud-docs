---
url: https://docs.cloud.google.com/netapp/volumes/docs/monitor/maintenance-events/
title: Monitor and plan for a maintenance event \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:36.918258+00:00
---

# Monitor and plan for a maintenance event  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/monitor/maintenance-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Monitor and plan for a maintenance event Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to monitor and receive updates about planned maintenance events and unplanned service outages for Google Cloud NetApp Volumes.

## View planned maintenance events

The planned maintenance notifications are published to the [NetApp Volumes maintenance Google group](https://groups.google.com/g/gc-netapp-volumes-maintenance/about).

To receive email notifications about upcoming planned maintenance events from the NetApp Volumes maintenance Google group, complete the following steps:

  1. Go to the [NetApp Volumes maintenance Google group](https://groups.google.com/g/gc-netapp-volumes-maintenance/about).

  2. Click **Join group** or **Ask to join** , depending on your organization policy.

  3. Optional: update your notification preferences to receive announcements by email.

  4. Review the group messages to view upcoming maintenance schedules and details.




## View unplanned service incidents

To view unplanned service events, including active and past availability incidents, use the [Google Cloud Personalized Service Health Dashboard](https://console.cloud.google.com/servicehealth/incidents) in the Google Cloud console.

To view unplanned service incidents, complete the following steps:

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).

  2. Click **View all products**.

  3. In the **Tools** section, click **Service Health**.

  4. Filter by the product and the location to find NetApp Volumes events.

  5. Review the incident details to understand scope, impact, and timestamps.




## Understand the impact of service events

Planned maintenance and unplanned infrastructure failures affect your storage pools:

  * Pools enter a `DEGRADED` state.

  * Operations such as pool updates, replication, and CMEK workflows are unavailable.

  * Write latency increases and throughput decreases.

  * Recovery is automatic but takes seconds to hours.




For more information about how these service events affect storage pool states, see [Storage pool states](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/overview#storage_pool_states).

## What's next

[Monitor NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/monitor/cloud-monitoring-metrics).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
