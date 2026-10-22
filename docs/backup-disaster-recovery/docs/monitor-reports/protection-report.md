---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protection-report/
title: Protection reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:25.282750+00:00
---

# Protection reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protection-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Protection reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Protection reports allow you to verify the application protection and discovery status within an appliance and also at an enterprise level in the appliance management console.

Protection reports include:

  * Ignored applications

  * Multiply protected applications

  * Policy summary

  * Protected applications

  * Unprotected applications




## Ignored applications

This report lists all the ignored applications across the appliances. These are applications that are either ignored on all appliances or are not protected on any appliance.

### Column descriptions

  * **Host** : Name of the host.

  * **Application** : Name of the application.

  * **Application Type** : Type of the application.

  * **Instance Name** : Name of the database instance for the instance members.

  * **Ignored on Appliances** : List of the appliances on which the application is marked as ignored.

  * **Discovered on Appliances** : List of the appliances on which the application is discovered.




## Multiply protected applications

This report shows the details of the applications that are protected on multiple appliances that are configured to the **Report Manager**.

### Column descriptions

  * **Host** : Name of the host where the application resides.

  * **Application** : Name of the application suffixed with the hostname.

  * **Application Type** : Type of the application.

  * **UUID** : Unique identifiers for application.

  * **Appliance** : Appliance name where the application is protected.

  * **Policy Template** : Template used in the appliance to protect the application.

  * **Instance Name** : Name of the SQL instance (applicable only for SQL server database)

  * **Consistency Group** : If the application is protected as part of a consistency group, its name is displayed here.

  * **Managed Data (TB)** : Managed data consumed by the application in the appliance.

  * **Most Recent Job** : Date and time to the minute of the start of the most recent snapshot job.

  * **Application ID** : The unique identifier for the application in an appliance.




## Policy summary

The report provides the policy summary for all policy templates on each appliance.

### Column descriptions

  * **Appliance** : Appliance name.

  * **Policy Template** : The assigned backup template in the backup plan.

  * **Policy** : Policy name.

  * **Operation** : Snapshot, StreamSnap, and OnVault.

  * **Retention** : A string value such as "two weeks". Note that StreamSnap retention knows when to use the snapshot retention, a custom retention, or to just keep the last image.

  * **Retention Days** : Number of days, using two digits, for example `01`.

  * **Schedule Type** : A text string with values such as **Daily** , **Continuous** , **Weekly on Saturday** , or **Monthly** on day one. This also needs to show any exceptions.

  * **Start Time** : When the window starts in the format: hh24:mm. Use the 24-hour clock notation to identify the hour, as in 20:00 for 8 PM. Leave this blank for continuous policies.

  * **Stop Time** : When the window closes. Format: hh24:mm as for **Start Time**. Leave blank for continuous policies.

  * **Frequency** : RPO (recovery point objective) text string as in "24 hours".

  * **Application Consistent** : String value of the policy option. Values are **yes** , **no** , or **last**. This field is blank if no policy option is set, which is the default.

  * **Log Backup Frequency (min)** : Minutes between database log backup jobs, or blank. This field is blank if the database log backup is not enabled.

  * **Applications Protected** : Number of applications protected by this policy template.

  * **Applications with Schedule Disabled** : Number of applications protected by this policy template that have their schedule disabled.




## Protected applications

This report provides the following details about protected applications.

  * SQL Server instance name and an indication of whether a database is protected through the SQL Server instance, a consistency group, or directly.

  * The remote node from the profile if the application is replicated.

  * All the backup plan restrictions, such as scheduler disabled and snapshots disabled.

  * Inclusions and exclusions, such as volumes included or excluded for VMs, databases included or excluded for SQL Server instances, and include or exclude patterns, and start or prune paths for file servers.




### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Host** : Name of the host.

  * **Application** : Name of the application.

  * **Application Type** : Type of application.

  * **Policy Template** : Policy template associated with the protected application.

  * **Protected On** : Date when the application protection started.

  * **Source Appliance** : Source appliance of a replicated remote application.

  * **Remote Appliance** : Remote appliance or remote node where the application is being replicated.

  * **Consistency Group** : If the application is protected as part of a consistency group, its name is displayed here.

  * **Instance Name** : This information is only available for SQL server databases.

  * **Backup Plan Restrictions** : A comma-separated list with the following options:

    * **Scheduler Disabled**
    * **Expiration Disabled**
    * **Snapshots Disabled**
    * **StreamSnap Disabled**
    * **OnVault Disabled**
    * **Process Latest Snapshot**
  * **Inclusions and Exclusions** : Volume restrictions.

  * **Policy Overrides** : Overrides include any policy options set at the application or backup plan level.




## Unprotected applications

This report displays the list of unprotected applications across the list of appliances added to **Report Manager** , with the list of appliances the application is discovered on. This report excludes applications that are marked as ignored.

### Column descriptions

  * **Host** : Name of the host where the application resides.

  * **Application** : Name of the application suffixed with the hostname.

  * **Application Type** : Type of application.

  * **Instance Name** : Name of the SQL instance.

  * **Discovered On** : List of the appliances the application is discovered on.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
