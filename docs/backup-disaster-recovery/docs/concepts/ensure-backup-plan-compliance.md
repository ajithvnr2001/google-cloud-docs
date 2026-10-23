---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/ensure-backup-plan-compliance/
title: Ensure backup plan compliance in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:11.783280+00:00
---

# Ensure backup plan compliance in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/ensure-backup-plan-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Ensure backup plan compliance in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The backup/recovery appliance automatically calculates and sets default backup plan compliance settings. Default settings are based on whether the policy is set to windowed or continuous, the policy type, and recommended best practices. The default settings calculated meets the needs of most users. Backup plan compliance settings can be set manually to meet specific requirements. In addition, a threshold can be set to alert you if your data is approaching a point where it is out of compliance.

To view or modify backup plan compliance settings, click backup plan policy compliance settings at the bottom of a policy's page. The default link name is **Default** , however, the link name is dynamic and changes according to the backup plan compliance settings used.

If data exceeds the backup plan compliance settings, a violation is raised and it remains in effect until you have successfully captured data with a consistency time that falls within the specified threshold. Because compliance is time based, a job can fail and restart multiple times but the data remains in compliance as long as the job eventually captures data with a consistency time that falls within the boundary of a specified threshold.

## Backup plan compliance settings

Policies set to **Windowed** or **Continuous** provide a link to backup plan compliance settings that have settings for the following:

  * Turning off backup plan compliance analysis
  * Using the default backup plan compliance settings
  * Defining a custom compliance setting. When defining a custom setting for a windowed policy, consider the time at which the data is snapped (consistency time), how long the window is open, and the amount of time required to capture the data.
  * Setting a warning that sends you a notification if a job is still running after a specified period of time. Set this to less than the wait time for raising a violation so you can address issues before a job is in violation.



To determine whether the data captured is in compliance, a backup/recovery appliance uses the start of the window, the consistency time of the backup, and the violation threshold specified in the backup plan settings dialog. If successfully captured data has a consistency time that falls within the window's defined threshold, the data is in compliance.

## What's next

  * Get an overview of [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan)
  * Create a [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)
  * Create a [backup policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview)
  * Create a [resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles)
  * Configure [advanced policy settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) of an application backed up by the policy
  * [Apply a backup plan to an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
