---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/compliance-report/
title: Compliance reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:59.205596+00:00
---

# Compliance reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/compliance-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Compliance reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This section explains how to work with backup plan compliance reports. These reports show how well the backup/recovery appliance is complying with the service level agreements that you have assigned to your applications.

Backup plan compliance reports include:

  * Daily protection summary

  * Daily protection table

  * Database backup status

  * Restorable images

  * Backup plan violation summary

  * Backup plan violation details




## Daily protection summary

This report shows whether any snapshot, OnVault, or direct OnVault jobs succeeded with consistency dates corresponding to the 24-hour period starting with the beginning of the snapshot window for the last eight days. It represents the success rate for snapshot, StreamSnap, OnVault and direct OnVault. Direct OnVault jobs are treated as OnVault. The report only looks at policies with a daily schedule. Any policies that are weekly or monthly are ignored. You can click any data point or table cell to drill down to the **Daily Protection Table** for details.

### Column descriptions

  * **Day** : Date of analysis.

  * **Expected** : Expected count of applications that are scheduled to be run on the analysis date.

  * **Success** : Success count of applications that ran on the analysis date.

  * **Failed** : Failed count of applications that ran on the analysis date.

  * **Not Run** : Not run count of applications that ran on the analysis date.

  * **Unknown** : Unknown count of applications that ran on the analysis date.

  * **Success%** : Success percentage of applications that ran on the analysis date.




## Daily protection table

This report shows whether any snapshot, StreamSnap, OnVault, or Direct to OnVault jobs succeeded with consistency dates corresponding to the 24-hour period starting with the beginning of the snapshot window for the last seven days. This report does not show any colored values, it shows the same information as **Daily Protection Status** plus some additional details, in a tabular format suitable for export to a spreadsheet.

### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Host** : Name of the host.

  * **Application** : Name of the application.

  * **Application Type** : Type of the application.

  * **Policy Template** : Policy template used for application protection.

  * **Date** : Date of analysis.

  * **Window Start Time** : Policy window start time for the data capture job type.

  * **Job Type** : Type classification of the job.

  * **Status** : Compliance status of the policy.

  * **Comment** : Description of the policy compliance.




## Database backup status

This report provides the database and log backup status for database applications such as Oracle, SQL Server, SAP HANA, or consistency groups with Oracle, SQL Server, and SAP HANA applications as consistency group members. It also provides the most recent job status, along with the recent successful database and log jobs.

This report has four sections:

  * Latest DB job

  * Latest successful DB job

  * Latest LOG job

  * Latest successful LOG job




### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Host** : Name of the host on which the application resides.

  * **Application** : Name of the application suffixed with the hostname.

  * **Application Type** : Type of the application.

  * **Policy Template** : Name of the policy template used for application protection.

  * **Job Name** : Name of the job.

  * **Started** : Timestamp of the start of the job.

  * **Ended** : Timestamp of the end of the job.

  * **Status** : Completion status of the job (**Succeeded** , **Failed** , **Canceled** , **Running** , or **Queued**).

  * **Image Age (Hours)** : Time from the backup time to the last successful data sync time for the appliance.

  * **Message** : Reason or cause for the job failure. Blank for successful, canceled, and running jobs.




## Restorable images

This report lists all the images that can be restored in an appliance. The images can be snapshots, log captures, or OnVault. Note that this is not the same as job type. For example, a StreamSnap image is a type snapshot with the destination of a remote appliance.

### Column descriptions

  * **Image Location** : Target appliance or OnVault.

  * **Source Appliance** : Source appliance where the application is protected.

  * **Host** : Name of the host where the application resides.

  * **Application** : Name of the application suffixed with the hostname.

  * **Application** : Type of the application.

  * **Policy Template** : Policy Template used for application protection.

  * **Policy** : Policy used for application protection.

  * **Job Type** : Type classification of backup job.

  * **Image Type** : Type of backup image.

  * **Image Name** : Name of backup image.

  * **Mounted Host** : Name of the host where image is mounted.

  * **Label** : Tag or description of the image.

  * **Consistency Point** : Consistency time of the backup image.

  * **Roll forward To** : Log image recovered up to.

  * **Immutability Date** : Date when the image expires.

  * **Created** : Date when the backup was triggered.

  * **Scheduled Expiration** : Date when the backup is scheduled to expire.

  * **Retention (Days)** : Number of days the backup is supposed to retain.

  * **Image Age (Days)** : Difference between the source appliance last contact time and consistency time.




## Backup plan violation details

This report shows all backup plan violations reported by the backup/recovery appliances. All appliances that have the parameter **backup plan.enable** set to the default value of **true** will analyze their data protection policies at the end of every policy window and report on violations. Details on these violations are shown in the report.

### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Host** : Name of the host.

  * **Application** : Name of the application.

  * **Application Type** : Type of the application.

  * **Policy Template** : Name of the policy template used for application protection.

  * **Policy Name** : Name of the policy used to protect the application.

  * **Job Type** : Type of job for which the violation occurred.

  * **Violation Time** : Timestamp when the backup plan violation occurred.

  * **Violation Type** : Type of violation.

  * **Reason** : Reason why the policy violation occurred.




## Backup plan violation summary

This report provides a backup plan violation summary for the configured appliances. The backup plan violation types **Failed** , **Scheduler Off** , and **Not Run** are summarized for job types snapshot, OnVault, and StreamSnap individually for each appliance.

  * The **Summary** row displays the enterprise violation count for each column.

    * Click **Appliance Name** to see the selected appliance's summary.

    * Click **Violation Count** to see the violation details with the corresponding filters selected.

  * **Top 5 Appliances with High Violation Count Graph** : This graph is a dual-level pie graph. The inner layer holds the top five appliances with the highest number of violations that occurred. The total violation count includes job types snapshot, OnVault, and StreamSnap. The outer layer consists of job types snapshot, OnVault, and StreamSnap for each of the top five appliances with highest violation count.

  * **Violations Count by Job Type and Violation Type Graph** : This graph is a dual-level pie graph. The inner layer contains the total violation count for job types snapshot, OnVault, and StreamSnap. The outer layer consists of violation types **Failed** , **Scheduler Off** , and **Not Run** aggregated for all the configured appliances.




Click the pie sector to view the details report with the selected filters.

  * **The Total Violations Graph** : This graph displays the total violation history for violation types **Failed** , **Scheduler Off** , and **Not Run** aggregated for all the configured appliances for each date of the selected interval.

  * **The Snapshot Violation Graphs** : This graph displays the violation history for violation types **Failed** , **Scheduler Off** , and **Not Run** aggregated for all the configured appliances.




Click any data point in the graph to view the details report with selected filters.

### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Application Count** : Number of applications that have contributed to the violations for the selected time period.

  * **Violation Count** : Number of violations that occurred in the selected interval.




For snapshot, OnVault, and StreamSnap sections, there are the following descriptions:

  * **Failed** : Number of **Failed** violations that have occurred for the selected interval.

  * **Scheduler Off** : Number of **Scheduler Off** violations that occurred in the selected interval.

  * **Not Run** : Number of **Not Run** violations that occurred in the selected interval.

  * **Other** : Number of other violations that occurred in the selected interval.

  * **Total** : Number of **Failed** , **Scheduler Off** , and **Not Run** that violations occurred in the selected interval. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
