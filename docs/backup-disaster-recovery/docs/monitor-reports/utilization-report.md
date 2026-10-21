---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/utilization-report/
title: Utilization reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:09.732130+00:00
---

# Utilization reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/utilization-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Utilization reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Utilization reports show the usage of resources by protected applications and VMs. The required resources fall into two categories: bandwidth used to replicate data from a primary to a DR appliance, and the pools used for storage.

Utilization reports include:

  * Application growth

  * Cloud resource consumption by day

  * Protected application sizes

  * OnVault pool consumption

  * Storage resource trending

  * Storage resource usage summary




## Application growth

This report gives the growth trends for the resources that are being used by the applications. It spreads the interval into 10 equal intervals and report the usage on corresponding date.

### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Remote Node** : Name of the remote appliance.

  * **Host** : Name of the host.

  * **Application** : Name of the application.

  * **Application Type** : Name of the application type.

  * **Resources** : Type of storage resource.

Each column represents the metric of the resource used for the corresponding date.

  * **Growth** : The difference between the initial non-zero value and final usage of the resource.

  * **Growth %** : Percentage of the difference between the initial non-zero value and final usage of the resource.

  * **Chart** : Growth trend of the metric for the application.




## Cloud resource consumption by day

This report shows the day by day resource utilization of Cloud Volumes, Cloud Snapshots, and Cloud Instances.

### Column descriptions

  * **Date** : Date for which resources utilization is mentioned.

  * **Pool** : Name of the Cloud pool.

  * **Appliance** : Name of the appliance.

Cloud Volumes, Cloud Snapshots, and Cloud Instances account for create and delete operations will have the following details:

    * **Count** : Count of jobs run.

    * **Virtual Size (GB)** : Size of data modified.




## Protected application sizes

This report gives the list of applications that are consuming the Protected Data license for each appliance. This provides the number of backups of each job class has with their latest expiration and backup creation dates.

### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Host** : Name of the host where the application resides.

  * **Application** : Name of the application suffixed with the hostname.

  * **Application Type** : Type of the application.

  * **Policy Template** : Policy template used for application protection.

  * **Protected Data (TB)** : Data protected by the application.

  * Snapshot, Remote, Remote Snapshot (StreamSnap), and OnVault sections:

    * **Image Count** : Count of backups the application has for the corresponding job class.

    * **Latest Expiration Date** : Date when the longest-retained backup will expire.

    * **Latest Image Date** : Date when the most recent backup image was created.




## OnVault pool consumption

This report shows the OnVault pool consumption for each pool, followed by the details of consumption in each pool. The details section shows the trend of appliance and pool followed by recent date's consumption for the selected interval.

### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Host** : Name of the host where the application resides.

  * **Application** : Name of the application suffixed with the hostname.

  * **Application Type** : Type of the application.

  * **Consumption (TB)** : OnVault storage used by the application.




## Storage resource trending

This report shows the resource consumption for snapshot pools and VDisks. It also forecasts the future consumption of the resources.

### Column descriptions

  * **Capacity (Blue Line)** : Storage capacity of the pool.

  * **Consumed (Green Line)** : Consumption of the storage pool.

  * **Trend (Red Line)** : Linear regression trend line for future pool consumption.




## Storage resource usage summary

This report provides the concise detailed summary of resource consumption for a selected date.

### Column descriptions

  * **Appliance** : Name of the Appliance.

  * **Date** Date consumption was calculated.

  * **Resource Type** One of the resource types (snapshot pool, VDisks, OnVault pools, primary pools, and total storage).

  * **Name** Date consumption was calculated.

  * **Capacity** Capacity of the resource types, blank for OnVault pools.

  * **Used** Consumption of the resource types.

  * **% Used** Percentage of VDisk and pool volume that are consumed. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
