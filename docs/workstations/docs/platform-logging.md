---
url: https://docs.cloud.google.com/workstations/docs/platform-logging/
title: Cloud Workstations platform logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:45.942024+00:00
---

# Cloud Workstations platform logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/platform-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Cloud Workstations platform logging Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Google Cloud platform logs created by Cloud Workstations.

## Overview

Cloud Logging receives, indexes, and stores platform log entries from Google Cloud services, such as Cloud Workstations. Platform logs are system-defined, service-specific logs that can help you debug and troubleshoot issues, as well as better understand the Google Cloud services you're using.

User-defined [audit logging](https://docs.cloud.google.com/workstations/docs/audit-logging) is chargeable and logs activity when a user updates resources. [Platform logging](https://docs.cloud.google.com/logging/docs/api/platform-logs), however, is non-chargeable and logs activity when Cloud Workstations assigns resources to a workstation.

Cloud Workstations creates the following types of platform logs:

  * **Disk assignments:** Logs when Cloud Workstations assigns a persistent disk to a workstation. The `logName` field of this platform log ends with `disk_assignments` and can be selected by updating the Logs Explorer with the query `logName=projects/$PROJECT/logs/workstations.googleapis.com%2Fdisk_assignments`.

  * **Instance assignments:** Logs when Cloud Workstations assigns a VM instance to a workstation. These logs contain the VM name, VM ID, internal IP address, and external IP address (if present). The `logName` field of this platform log ends with `vm_assignments` and can be selected by updating the Logs Explorer with the query `logName=projects/$PROJECT/logs/workstations.googleapis.com%2Fvm_assignments`.

  * **Workstation shutdowns:** Logs when Cloud Workstations shuts down a workstation and unassigns the VM instance. These logs contain the VM name, VM ID, internal IP address, and external IP address (if present). The `logName` field of this platform log ends with `workstation_shutdowns` and can be selected by updating the Logs Explorer with the query `logName=projects/$PROJECT/logs/workstations.googleapis.com%2Fworkstation_shutdowns`.




For information about how to view Cloud Workstations logs in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), see [View logs](https://docs.cloud.google.com/workstations/docs/audit-logging#viewing_logs).

## What's next

  * Learn more about [Cloud Workstations logging API](https://docs.cloud.google.com/logging/docs/api/platform-logs#workstations).

  * Understand and manage [Google Cloud platform logs](https://docs.cloud.google.com/logging/docs/api/platform-logs#managing-logs).

  * Learn more about [Cloud Workstations audit logging](https://docs.cloud.google.com/workstations/docs/audit-logging).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
