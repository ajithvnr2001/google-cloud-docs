---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/audit-report/
title: Audit reports on a backup/recovery appliance \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:27.684266+00:00
---

# Audit reports on a backup/recovery appliance  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/audit-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Audit reports on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This section describes an audit trail for the configuration and event details that occurred on a backup/recovery appliance.

For more information, see:

  * Audit trail report by appliance

  * Event details report




## Audit trail report by appliance

This report shows the audit trail of the configuration and other commands that are executed on each selected appliance with the details of the user and system details (source IP address) that initiated the command, as well as the status (success or failure) of the command.

### Column descriptions

  * **Date** : Date when command is executed.

  * **Source** : Component where command is delegated from.

  * **User Name** : Name of the user.

  * **User Full Name** : User's first name and last name are concatenated with a period (firstname.lastname).

  * **Source IP Address** : IP address of the system from which the command is initiated.

  * **Destination IP Address** : IP address of the system on which the command is executed.

  * **Privileged** : True for privileged users and blank for rest of the users.

  * **Details** : Command used and the status are delimited with a colon (:).




## Event details report

This **Event Details** report shows the event details on a particular appliance over a selected period.

### Column descriptions

  * **Severity** : Severity of the event (error warning or info)

  * **Event Time** : Timestamp when the event happened.

  * **Event Id** : Event type identifier.

  * **Error Message** : Reason or description for the failure.

  * **Error Code** : Unique error identifier.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
