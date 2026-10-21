---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/schedule-best-practices-at-a-glance/
title: Best scheduling practices at a glance for appliance-managed backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:56:32.841408+00:00
---

# Best scheduling practices at a glance for appliance-managed backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/schedule-best-practices-at-a-glance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Best scheduling practices at a glance for appliance-managed backups Stay organized with collections  Save and categorize content based on your preferences. 

The previous topics provided definitions, detailed descriptions, and best practices of how to set a schedule in a policy. The following table summarizes the best practices and most often used policy schedules.

The production to snapshot policy defines when and how often production data is captured and how many snapshots are retained.

  * **Windowed Schedule, One Snapshot per Window.** Window to open as needed, and might span day boundary. Default is 19:00 to 07:00. Frequency: Once per window. Retain for 2 days.
  * **Windowed Schedule, Multiple Snapshots in a Window.** Window to open as needed, and might span day boundary. Default is 19:00 to 07:00. Frequency: As needed, not to overlap with time to take a snapshot. Default is every 8 hours. Retain for 2 days.
  * **Continuous Schedule, Run Daily at Regular Intervals.** Continuous schedule spans a single 24 hour boundary. Frequency: As needed, not to overlap with time to take a snapshot. Default is every 8 hours. Retain for 2 days.

Snapshot to OnVault Policy | StreamSnap Replication Policy  
---|---  
Send snapshot data to object storage defined by an OnVault Pool |   
**Windowed Schedule -- One Snapshot per Window**  
Window to open as needed, and might span day boundary.  
Default is 19:00 to 07:00.  
Frequency: Once per window.  
Retain as needed | Replicate snapshot data to a remote backup/recovery appliance, over a high quality network, to provide RPOs as low as one hour.  
A StreamSnap policy is always tied to a specific Snapshot policy, and uses the schedule and frequency settings of that Snapshot policy.  
**Continuous Schedule -- Run Daily at Regular Intervals**  
Continuous schedule spans a single 24 hour boundary.  
Frequency: As needed, not to overlap with time to take a snapshot.  
Default is every 8 hours.  
Retain for 2 days. | Can retain multiple point-in-time backups at the remote site.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
