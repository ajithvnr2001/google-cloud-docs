---
url: https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management/
title: OS inventory management \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:11.122407+00:00
---

# OS inventory management  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  OS inventory management Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of OS inventory management. For information on setting up and using OS inventory management, see [Viewing operating system details](https://docs.cloud.google.com/compute/docs/instances/view-os-details).

Use OS inventory management to collect and view operating system details for your virtual machine (VM) instances. These operating system details include information such as hostname, operating system, and kernel version. You can also get information about installed OS packages, available OS package updates, Windows applications and OS vulnerabilities.

## When to use OS inventory management

OS inventory management can be used to complete the following tasks:

  * Identify VMs that are running a specific version of an operating system
  * View operating system packages that are installed on a VM
  * Generate a list of operating system package updates that are available for each VM
  * Identify missing operating system packages, updates, or patches for a VM
  * View vulnerability reports for a VM



## How OS inventory management works

When OS inventory management is enabled, the OS Config agent runs an inventory scan to collect data and then sends this information to the metadata server, OS Config API, and various log streams. By default, this scan runs every 10 minutes on the VM. You can customize the scan interval by setting the `osconfig-poll-interval` metadata value. For more information, see [Configure the OS inventory scan interval](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/view-os-details#configure-scan-interval).

To enable OS inventory management, VM Manager must be set up on the VM. See [Set up VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/setup).

After you set up VM Manager, you can then query either the guest attributes or the OS Config API to retrieve information about the operating system that is running on a VM. See [View operating system details](https://docs.cloud.google.com/compute/docs/instances/view-os-details#overview).

### How the operating system data is collected

For Linux VMs, the OS Config agent runs on the VM and parses the `/etc/os-release`, or the equivalent file for the Linux distribution to gather operating system details. The OS Config agent also uses package managers such as `apt`, `yum`, or [GooGet](https://github.com/google/googet) to collect information about the installed packages and available updates for the instance.

For Windows VMs, the OS Config agent uses the Windows system APIs to collect the OS information details. The Windows Update agent is also used to find the installed and available updates.

### Where the operating system data is stored

Inventory data is stored in the OS Config API. The contents for the installed packages and package updates are compressed using gzip to save space and then base64 encoded.

### Logging

During the collection and storage of data, the OS Config agent writes activity logs to the various log streams on Compute Engine. These include:

  * [The serial port](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output)
  * System logs - Windows event log and Linux syslog
  * Standard streams - stdout
  * [Cloud Logging logs](https://docs.cloud.google.com/logging/docs) \- These logs are only available if Cloud Logging is enabled on the VM instance.



## Information provided by OS inventory management

OS inventory management can provide the following information about the operating system that is running on your VM instance:

  * Hostname
  * LongName - The detailed operating system name. For example, `Microsoft Windows Server 2016 Datacenter`.
  * ShortName - The short form of the operating system name. For example, `Windows`.
  * Kernel version
  * OS architecture
  * OS version
  * OS Config agent version
  * Last updated - A timestamp of the last time the agent successfully scanned the system and updated the guest attributes with OS Inventory data.



### Installed operating system package and application information

The following table summarizes the information that OS inventory management provides for installed operating system packages on Linux and Windows VMs. It also outlines the information that is available for applications that are running on Windows.

Operating system | Package manager | Available fields  
---|---|---  
Linux and Windows Server | Installed package information is available from the following package managers:  


  * RPM for Red Hat Enterprise Linux (RHEL)
  * DEB for Debian and Ubuntu
  * GooGet for Windows Server

| For each installed package the following information is provided:  


  * Name of the package
  * Architecture
  * Version

  
Windows Server | Windows update agent | The following fields are listed for the [Windows updates](https://docs.microsoft.com/en-us/windows/desktop/api/wuapi/nn-wuapi-iupdate):  


  * Title
  * Description
  * Categories
  * CategoryIDs1
  * KBArticleIDs
  * SupportURL
  * UpdateID1
  * RevisionNumber1
  * LastDeploymentChangeTime

  
Windows Server | Windows Quick Fix Engineering updates | The following fields are listed for the [QuickFixEngineering updates](https://docs.microsoft.com/en-us/windows/desktop/cimwin32prov/win32-quickfixengineering)  


  * Caption
  * Description 
  * HotFixID 
  * InstalledOn

  
Windows Server | Windows Installer 2 | The following fields are listed for the [Windows Installer](https://docs.microsoft.com/en-us/windows/win32/msi/uninstall-registry-key):  


  * DisplayName
  * DisplayVersion
  * Publisher
  * InstallDate
  * HelpLink

  
  
1This field is hidden in the default `gcloud compute instances os-inventory describe` command-line output. To view this field you must view the output in the JSON format. To view the output in JSON format, append the `--format=JSON` to the `gcloud` command. For more information about output formatting, review [`gcloud topic formats`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats).

2To view installer properties for your Windows applications, you need OS Config agent version `20210811` or later. To view agent version, see [View OS Config agent version](https://docs.cloud.google.com/compute/docs/manage-os/upgrade-vm-manager#view-version).

### Available operating system package update information

The following table summarises the update information that OS inventory management provides for installed operating system packages.

Operating system | Package manager | Available fields  
---|---|---  
Linux and Windows Server | Package update information is available from the following package managers:  


  * Yum for Red Hat Enterprise Linux (RHEL)
  * Apt for Debian and Ubuntu
  * GooGet for Windows Server

| For each package update that is available the following information is provided:  


  * Name of the package
  * Architecture
  * Version

  
Windows Server | Windows update agent | The following fields are listed for the [Windows updates](https://docs.microsoft.com/en-us/windows/desktop/api/wuapi/nn-wuapi-iupdate):  


  * Title
  * Description
  * Categories
  * CategoryIDs1
  * KBArticleIDs
  * SupportURL
  * UpdateID1
  * RevisionNumber1
  * LastDeploymentChangeTime

  
  
1This field is hidden in the default `gcloud compute instances os-inventory describe` command-line output. To view this field you must view the output in the JSON format. To view the output in JSON format, append the `--format=JSON` to the `gcloud` command. For more information about output formatting, review [`gcloud topic formats`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats).

### Vulnerability reports

Software vulnerabilities are weaknesses that can either cause an accidental system failure or result in malicious activity. For VMs, a vulnerability can be an issue in the code or the logic of operation for either operating system packages or software applications.

Vulnerabilities associated with the installed operating system packages are normally stored in a vulnerability source repository. For more information about these vulnerability sources, see Vulnerability sources. You can use OS inventory management to view vulnerability reports for issues with installed OS packages.

To get vulnerability data for a VM, VM Manager must be set up, and OS Config agent version dated `20201110` or later must be running on the VM. See [Setting up VM Manager](https://docs.cloud.google.com/compute/docs/manage-os).

After the OS Config agent is set up and reporting inventory, the OS Config API service continuously scans and checks the vulnerability source of the operating system against the available inventory data. When a vulnerability is detected in the operating system packages, the service generates a vulnerability report. These reports are generated as follows:

  * When a package is installed or updated in a VM's operating system, you can expect to see [Common Vulnerabilities and Exposures (CVEs)](https://wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) information for the VM in VM Manager, Security Command Center, and Cloud Asset Inventory within two hours after the change.
  * When new security advisories are published for an operating system, updated CVEs are normally available within 24 hours after the operating system vendor publishes the advisory.



To view these vulnerability reports, see [View vulnerability reports](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/vulnerability-reports).

#### How vulnerability reports are generated

VM Manager periodically completes the following tasks:

  1. Reads the reports that are collected from [OS inventory data ](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management#data-collected) on a VM.
  2. Scans for classification data from the vulnerability source for each operating system, and orders this data based on severity (from highest to lowest), at least once daily.
  3. Displays the CVE data for a VM on the Google Cloud console. You can also [view the vulnerability reports](https://docs.cloud.google.com/compute/docs/os-patch-management/manage-patch-jobs#list-instance-details) using Security Command Center or Cloud Asset Inventory.



#### Vulnerability sources

The following table summarizes vulnerability source that is used for each operating system. For a complete list of supported operating systems and their versions, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#vm-manager).

**Operating system** | **Vulnerability source package**  
---|---  
RHEL and CentOS | <https://access.redhat.com/security/data> See Limitations  
Debian | <https://security-tracker.debian.org/tracker>  
Ubuntu | <https://launchpad.net/ubuntu-cve-tracker>  
SLES | <https://ftp.suse.com/pub/projects/security/oval/>  
Rocky Linux | <https://errata.rockylinux.org/>  
Windows | Vulnerability data published by [Microsoft Security Response Center](https://msrc.microsoft.com/).  
  
## Data retention

OS inventory and vulnerability report data is stored until the VM is deleted. However, if for any reason the OS Config agent stops reporting to the OS Config API service for a few days, then VM Manager deletes the available OS inventory and vulnerability report data collected until that point. No data will be available for that VM until the OS Config agent starts running again.

## Pricing

For information about pricing, see [VM Manager pricing](https://docs.cloud.google.com/compute/vm-manager/docs/pricing).

## Limitations

The following limitation applies to OS inventory management:

  * VM Manager provides vulnerability scanning results for RHEL based on the latest minor version for each major version released. If your VM runs an older minor version of RHEL, then you might get inaccurate results in the vulnerability reports.



## What's next

  * Use the OS inventory management tool to [view operating system details](https://docs.cloud.google.com/compute/docs/instances/view-os-details).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
