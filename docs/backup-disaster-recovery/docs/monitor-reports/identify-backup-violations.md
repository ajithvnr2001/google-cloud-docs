---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/identify-backup-violations/
title: Identify backup plan violations in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:56.147616+00:00
---

# Identify backup plan violations in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/identify-backup-violations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Identify backup plan violations in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Policy templates and resource profiles are defined in the backup plans section of the appliance management console. They are applied to applications and VMs in **App Manager**. A backup plan violation occurs when a job (or action) does not meet the requirements defined by a policy in a policy template.

This section details the potential causes of a backup plan violation, how the appliance management console identifies when a backup plan violation has occurred, and methods you can use to monitor backup plan violations as they occur. It includes:

  * Potential causes of backup plan policy violations
  * How a backup/recovery appliance monitors backup plan violations
  * Monitoring backup plan violations



## Potential causes of backup plan policy violations

The appliance management console applies backup plans to applications and data sets, where the management of your application copy data in the **App Manager** service is based according to the rules that you define in a backup template and its associated policies. A backup template includes one or more policies that define the source of the data (snapshot or replication) and the schedule (frequency, retention, start time, end time) for each data source. A backup plan violation occurs when the job (or action) that a backup plan policy defines does not begin according to the policy's schedule.

Each backup/recovery appliance automatically runs a backup plan analysis every hour to help identify backup plan violations as they occur throughout the day for scheduled jobs. This background operation alerts you to possible backup plan violations as close to the end of a backup plan policy window as possible, see How a backup/recovery appliance monitors backup plan violations.

The appliance management console allows its administrators to create a library of policy templates. One of the principal characteristics of each backup plan policy is the schedule that determines when this policy will be run.

Backup plan violations are often viewed as originating from issues with job slot count settings; where slot counts determine how many jobs can be run simultaneously. However, increasing job slot counts does not guarantee that backup plan violations will stop. In actuality, a backup plan violation can be related to any one of the conditions outlined in the following sections.

### Failed jobs

Failing jobs is a common cause of backup plan violations. For example, if an Oracle host is not accessible then the backup/recovery appliance cannot capture the data from Oracle RMAN, which results in a failed snapshot job. When a job fails, check your environment to confirm that all applications and hosts are accessible.

### Multiple applications per host

If a host has multiple applications, and each application is managed by a separate policy template (rather than grouped together as a consistency group), then only one application can have a snapshot job running at a time even if free slots are available.

If a VM is managed as a VM and also has applications managed through the Backup and DR agent, then only one of the applications can have a data capture job running at a time.

If a host has a D:\, E:\, and F:\ drive, and the individual drives are managed by separate backup templates, then each drive will be managed in series. For example, if the allowed run window for the policy is from 01:00 (UTC) to 03:00 (UTC), and the first drive takes three hours to complete its snapshot job, the other two drives won't get a snapshot job during that day.

One possible solution is to extend the backup plan policy window as a means to extend the total run time. Another solution is to include multiple applications in a consistency group.

### Backup plan violations can be a false positive

In some cases a backup plan violation is actually a false positive (a result which incorrectly indicates that a particular condition is present). Keep in mind that not every backup plan violation is really a violation, and it is possible to receive false positives as outlined in these two examples:

  * You are managing a VM's copy data that has a clustered volume. If the backup plan policy is running but the VM does not have control of the volume, this failure is considered a backup plan violation.
  * If a job (e.g., VM, application, etc.) has its backup plan-driven scheduler turned off, this can result in a backup plan violation occurring every time the backup plan policy should be applied.



### Constrained resources in the backup/recovery appliance

Constrained resources in a backup/recovery appliance can be related to issues such as network port throughput, maximum number of iSCSI initiators, throughput capability of the backend storage or the frontend storage. Increasing slot counts won't help in this case.

### Size of policy window or length of job run time

Jobs that run for many hours hold job slots that could be used by other applications. If each application completes its job in one minute on average, and you have five slots, then 300 jobs per hour is possible, If each application takes one hour on average, and you have five slots, then five jobs per hour is possible. However, if the total window for the policy is three hours, then the number of applications trying to use this backup plan policy will have a huge impact on the total application copy data management possible in a 24-hour time period.

For example, if there are 100 applications, then in the first example (300 jobs per hour) the appliance will finish all the applications in approximately 20 minutes. However, if we have 100 applications in the second example (five jobs per hour) then the appliance will only manage 15 applications per day. This will result in 85 backup plan violations.

Although you cannot control job run time, you can look at the length of time the running applications are scheduled. Long job times can also occur during the first snapshot job for a new application. On-ramp settings can be used to prevent ingest jobs from locking up slots and locking out already ingested applications.

## How a backup/recovery appliance monitors backup plan violations

Each backup/recovery appliance automatically runs a backup plan analysis every hour to help identify backup plan violations as they occur throughout the day for scheduled jobs. This background operation alerts you to possible backup plan violations as close to the end of a backup plan policy window as possible.

During the analysis, the appliance checks for all backup plan policies whose working hours have ended within the past hour. Each policy is examined for backup plan violations, and if a backup plan policy has a backup plan violation within 60 minutes of the end of the policy window, an entry is made in the event database for those violations. If a policy does not have a backup plan violation, no alert or event will be generated.

**Note:** The backup plan analysis process does not take into account on-demand protection jobs that are run from the **App Manager**.

When a backup plan violation occurs within the 60-minute backup plan policy completion window, an alert is initiated and an event notification generated. You can receive backup plan violation alerts in the form of System Monitor events (see [Monitor](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor)) or email event notifications. Each alert includes details about each backup plan policy in violation for a specific application, including information such as the event message, policy name and type, violation time and type, and job information (jobs expected, tolerance, succeeded, failed). Backup plan violation alerts contain the same level of detail that can be seen in backup plan violation reports included as part of the backup plan compliance reports in the **Report Manager**.

A platform server log (the udppm log file) is also created to outline when the analysis was run, which policies have been analyzed, and what was the outcome of the analysis.

The backup plan analysis takes into account discrepancies that might be the result of in-flight jobs. In certain circumstances a job begins within the allotted policy start time but might run longer than anticipated and fail to complete within the specified policy time window (for example, a job starts at 10:00 PM but ends at 11:30 PM). Initially, the job is seen as a success and does not result in a backup plan violation alert. However, upon completion of the job, it is reevaluated as part of the next backup plan analysis cycle and possibly flagged as a backup plan violation. The success or failure of a backup plan policy depends on when a job actually completes.

If, during the analysis, the appliance determines that a backup plan policy failed to have one or more jobs run, a backup plan violation occurs and the generated alert or event contains the following additional information regarding the failed job:

  * The expected job run time
  * The reason the job failed to run



The appliance also examines the timeline to determine if no jobs were run because there were no available slots for that job type. If this was the reason, the alert or event includes this information.

If the application has multiple backup plan policies that have overlapping policy windows, and there is a missed job for both policies during this overlapping time, the appliance will only generate a single alert. It won't initiate duplicate alerts for overlapping policies to eliminate duplication. Missed job alerts are aggregated by application, policy type, and time window.

## Monitor backup plan violations

You can monitor and view backup plan violations from the **Monitor** tab or from a managed appliance through email notifications or by using the **Report Manager**.

### Monitor

You can view the details of a backup plan violation as an event from the **Monitor** tab (**Monitor > Events**). For details on using the **Monitor** tab, see [Monitor](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor).

### Report Manager

There is a complete library of backup plan violation reports available in the **Report Manager** for your appliance management console. These reports can help simplify how you confirm the current success rate, as well as make it easier for you to differentiate between multiple applications with the same name.

## What's next

  * Get an overview of [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan)
  * Create a [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)
  * Create a [backup policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview)
  * Create a [resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles)
  * Configure [advanced policy settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) of an application backed up by the policy
  * [Apply a backup plan to an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
