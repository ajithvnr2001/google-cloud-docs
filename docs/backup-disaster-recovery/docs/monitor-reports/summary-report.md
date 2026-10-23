---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/
title: Summary reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:43.809372+00:00
---

# Summary reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Summary reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The summary reports provide the daily overall status of an appliance. It is a combination of several sub-reports.

Summary reports include:

  * Appliance health Dashboard

  * Resource consumption by appliance

  * Resource consumption by application

  * Resource consumption by policy template




## Appliance health dashboard

This report shows the key attributes and resource constraints for each appliance, with colors to indicate resources (disk pools, vDisks, elapsed time since last data sync) that are approaching or exceeding their limits. A yellow color indicates a warning threshold and a red color indicates a critical level. The percentage used column (% Used) for snapshot pools is the ratio of usage and capacity of all the snapshot pools on the appliance.

### Column descriptions

  * **Appliance.** Name of the appliance.

  * **Last Sync Elapsed (hr:min).** Number of hours since the last successful data sync.

  * **Software Version.** Version of the appliance.

  * **Protected Data (TB).** **Protected Data Licenses** consumed by the appliance in tebibytes, along with a trend line.

**Snapshot Pools, VDisks.** These include the following:

    * **Used/Capacity.** Current usage and capacity. Pools are measured in terabytes.

    * **% Used.** Percentage of VDisk and pool volume that are consumed.

    * **30 Day Trend.** History of consumption and capacity over the past 30 days.




## Resource consumption by appliance

This report shows the resource consumption by Appliance, and includes the local and remote consumption of resources by an appliance.

### Column descriptions

  * **Target Appliance.** Appliance where the application's backup is replicated to.

  * **Source Appliance.** Appliance where application is protected.

  * **Application Count.** Number of applications assigned to the Appliance. Includes snapshot **Pool Consumed (TB): Local Snapshot **pool consumption by the **Appliance**.

  * **Snapshot Pool Consumed (TB).** Snapshot pool consumed by the application.

  * **VDisks Consumed.** Local VDisks consumed by the application.

  * **OnVault Consumed (TB).** OnVault consumed by the appliance.




## Resource consumption by application

This report displays the resource consumption by each application.

### Column descriptions

  * **Appliance.** Name of the appliance.

  * **Remote Appliance.** Name of the remote appliance.

  * **Application.** Name of the application.

  * **Application Type.** Type of the application.

  * **Policy Template.** Policy template name.

  * **Application Size (GB).** Data managed data by the application.

  * **Local Snapshot Pool Consumed (GB).** Local snapshot pool consumption by the application.

  * **Remote Snapshot Pool Consumed (GB).** Remote snapshot pool consumption by the application.

  * **Total Snapshot Pool Consumed (GB).** Total snapshot pool consumption by the application.

  * **Local VDisks Consumed.** Local VDisks consumed by the application.

  * **Remote VDisks Consumed.** Remote VDisks consumed by the application.

  * **Total VDisks Consumed.** Total VDisks consumed by the application.

  * **OnVault Consumed (GB).** OnVault consumed by the application.




## Resource consumption by policy templates

This report displays resource consumption by policy template, which includes the local and remote consumption of resources.

### Column descriptions

  * **Policy Template.** Unique policy template across the enterprise.

  * **Appliance Count.** Number of appliances the policy template exists on.

  * **Application Count.** Number of applications present in the policy template.

  * **Managed Data (TB).** Managed data by the policy template.

  * **Snapshot Pool Consumed (TB).** Snapshot pool consumption by the policy template.

  * **VDisks Consumed.** VDisks consumed by the policy template.

  * **OnVault Consumed (TB).** OnVault consumed by the policy template.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
