---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/alerts-scc/
title: Security Command Center and Google SecOps for Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:31.265959+00:00
---

# Security Command Center and Google SecOps for Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/alerts-scc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Security Command Center and Google SecOps for Backup and DR Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes the integration between Security Command Center, Google Security Operations (Google SecOps), and Backup and DR. This integration enables alerts for high risk actions that occur within Backup and DR that are surfaced in Security Command Center and Google SecOps.

With Security Command Center and Google SecOps for Backup and DR you can:

  * Receive instant alerts on high-risk actions, such as removing protection from a workload
  * Investigate threats and identify affected backup resources 
  * Aggregate backup threats in cases for quick and systematic remediation



Security Command Center ingests logs and events from across Google Cloud to identify potential security risks. Google SecOps, included as part of Security Command Center Enterprise, is a SIEM (security information and event management) and SOAR (security orchestration, automation, and response) tool that intelligently aggregates and correlates threats across multiple sources. Google SecOps also enables case management and remediation for threats.

**Before You Begin**

Activate Security Command Center Premium if it is not already enabled. This can be done using the Google Cloud console. For Security Command Center Enterprise, contact your Google Cloud account team.

**Generating a Finding**

High risk actions taken by a user in Backup and DR are monitored using Event Threat Detection (part of Security Command Center Premium and Security Command Center Enterprise). These actions are monitored in real-time, correlated with other risk events across Google Cloud, and surfaced as _findings_ (Security Command Center), _alerts_ (Google SecOps) and auto-curated _cases_ (Google SecOps).

These actions include:

  * Deleting a backup
  * Deleting a Backup Plan
  * Removing backup protection from a workload
  * Removing backup infrastructure that may impact recovery



A full list of detections are available in [Security Command Center documentation](https://docs.cloud.google.com/security-command-center/docs).

**Real-time findings in Security Command Center**

When an action is deemed a security risk by Security Command Center, a finding is generated. A security administrator can then take a closer look at the resources affected and take recommended next steps. Findings include details on the resources affected, when the security event occurred, and what actions to take to remediate a threat.

Security Command Center offers built-in investigation tooling for customers. Links to Cloud Logging, MITRE indicator, and affected resources enable rapid remediation.

  * Cloud Logging integration lets you click through to a detailed Cloud Logging query.
  * Cloud Monitoring integration enables [creation of additional alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-by-api) on similar events.
  * MITRE classifications indicate type of attack indicated by a finding as shown in this [example](https://attack.mitre.org/techniques/T1490/).



**Case management and remediation in Google SecOps**

Google SecOps features _curated detections_ which surface high-risk events as Alerts. Among these curated detections are potential threats to backups and backup resources. Curated detections require no additional configuration. Alerts are also aggregated into cases for triage and remediation. 

Threat detection for Backup and DR is available to all Security Command Center Premium and Security Command Center Enterprise customers. Google SecOps for Backup and DR is available exclusively to Security Command Center Enterprise customers.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
