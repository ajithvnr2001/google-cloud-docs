---
url: https://docs.cloud.google.com/compute/vm-manager/docs/patch/
title: About Patch \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:34.933286+00:00
---

# About Patch  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  About Patch Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page describes the Patch feature in VM Manager and how it works. To create patch jobs, see [Creating patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job).

Use Patch to apply operating system patches across a set of Compute Engine VM instances (VMs). Long running VMs require periodic system updates to protect against defects and vulnerabilities.

The Patch feature has two main components:

  * Patch compliance reporting, which provides insights on the patch status of your VM instances across Windows and Linux distributions. Along with the insights, you can also view recommendations for your VM instances.
  * Patch deployment, which automates the operating system and software patch update process. A _patch deployment_ schedules _patch jobs_. A _patch job_ runs across VM instances and applies patches.



## Benefits

The Patch service gives you the flexibility to complete the following processes:

  * Create patch approvals. You can select what patches to apply to your system from the full set of updates available for the specific operating system.
  * Set up flexible scheduling. You can choose when to run patch updates (one-time and recurring schedules).
  * Apply advanced patch configuration settings. You can customize your patches by adding configurations such as pre and post patching scripts.
  * Manage these patch jobs or updates from a centralized location. You can use the the Patch dashboard for monitoring and reporting of patch jobs and compliance status.



## Supported operating systems

For the full list of operating systems and versions that support Patch, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#vm-manager).

## Pricing

For information about pricing, see [VM Manager pricing](https://docs.cloud.google.com/compute/vm-manager/docs#pricing).

## How Patch works

To use the Patch feature, you must set up the OS Config API and install the OS Config agent. For detailed instructions, see [Set up VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/setup). The OS Config service enables patch management in your environment while the OS Config agent uses the update mechanism for each operating system to apply patches. Updates are pulled from the package repositories (otherwise called the _distribution source package_) or a local repository for the operating system.

**Note:** You cannot host a local repository if you're running Pay-As-You-Go (PAYG) RHEL, RHEL for SAP, SLES, and SLES for SAP images.

The following update tools are used to apply patches:

  * Red Hat Enterprise Linux (RHEL), Rocky Linux and CentOS - `yum upgrade`
  * Debian and Ubuntu - `apt upgrade`
  * SUSE Linux Enterprise Server (SLES) - `zypper update`
  * Windows - Windows Update Agent



### Patch and package sources

To use the Patch feature in VM Manager, the VM must have access to the package updates or patches. The Patch service does not host or maintain package updates or patches. In some scenarios your VM might not have access to the updates. For example, if your VM doesn't use public IPs or you are using a private VPC network. In these scenarios, you must complete additional steps to allow access to the updates or patches. Consider the following options:

  * Google recommends hosting your own local repository or a Windows Server Update Service for full control over the patch baseline.
  * Alternatively, you can make external update sources available to your VMs by using [Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation) or other proxy services.



Patch management consist of two services: patch deployment and patch compliance. Each service is explained in the following sections.

### Patch deployment overview

A patch deployment is initiated by making a call to the VM Manager API (also known as the OS Config API). This can be done by using either the Google Cloud console, Google Cloud CLI, or a direct API call. Then the VM Manager API notifies the OS Config agent that is running on the target VMs to start patching.

The OS Config agent runs the patching on each VM by using the patch management tool that is available for each distribution. For example, Ubuntu VMs use the `apt` utility tool. The utility tool retrieves updates (patches) from the distribution source for the operating system. As patching proceeds, the OS Config agent reports the progress to the VM Manager API.

### Patch compliance overview

After you [set up the VM Manager](https://docs.cloud.google.com/compute/docs/manage-os) on a VM, the following takes place on the VM:

  * The OS Config agent periodically (about every 10 minutes) reports [OS inventory data ](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management#data-collected).
  * The patch compliance backend periodically reads this data, cross references it with the package metadata obtained from the OS distribution and saves it.
  * The Google Cloud console then gets the patch compliance data and displays this information in the console.



#### How patch compliance data is generated

The patch compliance backend periodically completes the following tasks:

  1. Reads the reports that are collected from [OS inventory data ](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management#data-collected) on a VM.
  2. Scans for classification data from the vulnerability source for each operating system, and orders this data based on severity (from highest to lowest).

The following table summarizes vulnerability source that is used for each operating system. 

**Operating system** | **Vulnerability source package**  
---|---  
RHEL and CentOS | <https://access.redhat.com/security/data> Vulnerability scanning results for RHEL are based on the latest minor version for each major version released. There might be inaccuracies in scanning results for older minor versions of RHEL.  
Debian | <https://security-tracker.debian.org/tracker>  
Ubuntu | <https://launchpad.net/ubuntu-cve-tracker>  
SLES | [https://www.suse.com/support/update/](https://www.suse.com/support/update)  
Rocky Linux | [https://errata.rockylinux.org/](https://errata.rockylinux.org)  
Windows | The patch compliance backend gets the classification data from the Windows Update Agent API.   
  3. Maps these classifications (provided by the vulnerability source) to Google's [patch compliance status](https://docs.cloud.google.com/compute/vm-manager/docs/patch#patch_compliance_status).

The following table summarizes the mapping system used to generate Google's patch compliance status. 

**Distribution source categories** | **Google's patch compliance status**  
---|---  
     * Critical
     * Urgent
     * WINDOWS_CRITICAL_UPDATE
| Critical (RED)  
     * Important
     * High
     * WINDOWS_SECURITY_UPDATE
| Important/Security (ORANGE)  
     * Everything else
| Other (YELLOW)  
     * No updates available
| Up-to-date (GREEN)  
  4. Selects the highest severity data for each available update and shows it on the Google Cloud console dashboard page. You can also see a full report of all available updates for the VM on the [VM details page](https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs#list-instance-details).




For example, if the [OS inventory data ](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management#data-collected) for a RHEL 7 VM has the following package data:

  * Package name: package1
  * Installed Version: 1.4
  * Update Version: 2.0



The patch compliance backend scans for classification data (from the source distribution) and retrieves the following information:

  * Version 1.5 => Critical, fixes CVE-001
  * Version 1.8 => Low, fixes CVE-002
  * Version 1.9 => Low, fixes CVE-003



Then on the Google Cloud console dashboard, this RHEL 7 VM is then added to list of VMs that have a `Critical` update available. If you review the details for this VM, you see 1 `Critical` update available (version 2.0) with 3 CVE's, CVE-001, CVE-002 and CVE-003.

### Simultaneous patching

When you initiate a patch job, the service uses the [instance filter](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job#instance-filters) you provided to determine the specific instances to be patched. Instance filters allow you to simultaneously patch many instances at the same time. This filtering is done when the patch job starts to account for changes in your environment after the job is scheduled.

### Scheduled patching

Patches can be executed on demand, scheduled in advance, or configured with a recurring schedule. You can also cancel an in-progress patch job if you need to stop it immediately.

**Note:** In the event of a cancellation or timeout, the OS Config agent attempts to complete the task it is on before stopping.

You can set up patch maintenance windows by creating patch deployments with a specified frequency and duration. Scheduling patch jobs with a specified duration ensures that patching tasks do not start outside of your designated maintenance window.

You can also enforce patch installation deadlines by creating patch deployments to be completed at a specific time. If targeted VMs are not patched by this date, then the scheduled deployment starts installing patches on this date. If VMs are already patched no action is taken on those VMs, unless a pre or post patch script is specified or a reboot is required.

## What is included in a patch job?

When a patch job runs on a VM, depending on the operating system, a combination of updates are applied. You can choose to target specific updates, packages, or, for Windows operating systems, specify the KB IDs that you want to update.

You can also use a patch job to update any Google agents that are installed as a standard package for that specific distribution. Use the update tool for that distribution to query the packages that are available. For example, to see the available Google agents for an Ubuntu operating system, run `apt list --installed | grep -P 'google'`.

###  Windows 

For Windows operating system, you can apply all or select from the following updates:

  * Definition updates
  * Driver updates
  * Feature pack updates
  * Security updates
  * Tool updates

**Note:** By default, VM Manager does not apply updates for the Microsoft applications running on your Windows VMs. See how to [enable patching Microsoft software on Windows VMs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job#patch-ms-software).

###  RHEL/Rocky/CentOS 

For Red Hat Enterprise Linux, Rocky Linux and CentOS operating systems, you can apply all or select from the following updates:

  * System updates
  * Security updates



###  Debian/Ubuntu 

For Debian and Ubuntu systems, you can apply all or select from the following updates:

  * Distribution updates
  * Package manager updates



###  SUSE 

For SUSE Enterprise Linux Server (SLES) and openSUSE operating systems, you can apply all or select from the following updates:

  * System package updates
  * Zypper patches (specific bug fixes and security fixes)



## Access patch summary for your VMs

To view the patch summary for your VMs, you have the following options:

  * To view the patch summary information for all VMs in an organization or folder, use the Patch dashboard on the Google Cloud console. See [View patch summary for VMs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/view-patch-summary).

  * To view the status of the patch jobs, use the **Patch jobs** page on the Google Cloud console. You can also use the Google Cloud CLI or the OS Config API. For more information, see [Manage patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs).




To view other information such as OS package updates and vulnerability reports, see [view operating system details](https://docs.cloud.google.com/compute/docs/instances/view-os-details).

## The Patch dashboard

In the Google Cloud console, a dashboard is available that you can use to monitor the patch compliance for your VM instances.

[Go to the Patch page](https://console.cloud.google.com/compute/patch)

[ ![Patch dashboard.](https://docs.cloud.google.com/static/compute/images/manage-os/os-patchdashboard.png)](https://docs.cloud.google.com/static/compute/images/manage-os/os-patchdashboard.png)

### Understanding the Patch dashboard

#### Operating system overview

This section reflects the total number of VMs, organized by operating system. For a VM to show up in this list, it must have the OS Config agent [installed](https://docs.cloud.google.com/compute/docs/manage-os#check-install) and OS inventory management [enabled](https://docs.cloud.google.com/compute/docs/manage-os#enable-metadata).

[ ![Number of VMs card.](https://docs.cloud.google.com/static/compute/images/manage-os/number-of-vms.png)](https://docs.cloud.google.com/static/compute/images/manage-os/number-of-vms.png)

If a VM is listed with its operating system as `No data`, one or more of the following scenarios might be true:

  * The VM is unresponsive.
  * OS Config agent is not installed.
  * OS inventory management is not enabled.
  * The operating system is not supported. For a list of supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#vm-manager).



#### Patch compliance status

[ ![OS specific card.](https://docs.cloud.google.com/static/compute/images/manage-os/os-specific.png)](https://docs.cloud.google.com/static/compute/images/manage-os/os-specific.png)

This section describes the compliance status of each VM, organized by operating system.

Compliance status is categorized into four main categories:

  * **Critical:** This means that a VM has critical updates available.
  * **Important or security:** This means that a VM has important or security updates available.
  * **Other:** This means that a VM has updates available, but none of these updates are categorized as a critical or security update.
  * **Up-to-date:** This means that a VM has no updates available.



## Limitations

The Patch feature in VM Manager has the following limitations:

  * You can deploy and run patch jobs only for VMs in a single Google Cloud project. You cannot run patch jobs across Google Cloud projects, even if the VMs are in a Shared VPC. However, you can [view the patch compliance data across projects](https://docs.cloud.google.com/compute/vm-manager/docs/patch#accessing_os_patch_management_data).
  * By default, VM Manager does not patch any VMs that are part of a managed instance group (MIG). You can override this default behavior when you create the patch job. The following limitations apply when you patch VMs that are part of a MIG: 
    * When a [MIG repairs a VM](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair), it recreates the VM based on the instance template. This might revert the VM to an unpatched state.
    * Patching VMs can cause unexpected results in a MIG that has autoscaling enabled. Autoscaler deletes patched VMs when the load goes down and creates new, unpatched VMs using MIG's instance template when the load increases. For example, if the average CPU utilization is less than the target utilization you specified for autoscaling, MIG can remove some of the patched VMs while scaling in.



## What's next?

  * [Create a patch job](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job).
  * [Manage patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs).
  * [Schedule patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/schedule-patch-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
