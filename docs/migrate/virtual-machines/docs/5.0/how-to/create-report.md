---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-report/
title: Create a VMware VM utilization report \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:08:56.189715+00:00
---

# Create a VMware VM utilization report  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Create a VMware VM utilization report Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is only supported for VMware virtual machine (VM) instances.

Before you can perform a test-clone or cut-over on a migrating VM, you must set the Compute Engine target details that define the landing zone for the VM on Google Cloud. These details include the Google Cloud project and network settings, but also includes:

  * Number of CPUs
  * Amount of memory
  * more



For more information, see [Configure the target for a migrated VM](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#configure-target).

To help you determine the optimal settings for the Compute Engine target, Migrate to Virtual Machines lets you create a _source VM utilization report_. This report displays information about resource allocation and utilization for the source VMs deployed on your migration source.

**Note:** For a newly created source VM, there might be a delay of several hours before utilization data is available from the migration source.

When you create a report, you set a time duration (week, month, year) for the utilization data.

For the specified source VM, the report then displays the following information calculated over that duration:

  * Number of vCPUs allocated for the source VM, average CPU usage, and maximum CPU usage
  * Allocated memory (GB), average memory usage, and maximum memory usage
  * Average and maximum network throughput (Kbps)
  * Average and maximum disk IO rate (Kbps)



You can then use this information to set the Compute Engine target details.

The following is an example report:

[ ![Utilization report.](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/utilization-report.png)](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/utilization-report.png)

## Creating a utilization report

To create a report:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Sources** tab.

  3. From the drop-down list, select your migration source.

A table appears showing the source VMs in the migration source.

  4. Select one or more VMs.

**Note:** You cannot select more than 100 VMs for a single report.
  5. Select **Create report** and enter the **Name** , **Description** (optional), and **Time period** for the report.

The **Name** must consist of lowercase letters (a-z), numbers, and hyphens.

  6. Select **Create**.

The report takes a minute or so to create.

  7. Select **View reports**.

A list of available reports appears, arranged by report name.

  8. Select the report name to view the results.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
