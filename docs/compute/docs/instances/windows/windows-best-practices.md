---
url: https://docs.cloud.google.com/compute/docs/instances/windows/windows-best-practices/
title: Best practices for Windows Server VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:42:09.733007+00:00
---

# Best practices for Windows Server VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/windows-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practices for Windows Server VMs Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

You can apply several best practices to optimize Compute Engine instances that run Microsoft Windows Server. This document describes how you can utilize other products available on Google Cloud and to ensure your Windows instances are performing optimally in terms of performance, security, redundancy and availability. For further information on configuration and setup of Windows instances, see [Windows Workloads](https://docs.cloud.google.com/compute/docs/instances/windows). For Microsoft SQL instances, refer to [Best Practices for SQL Server](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices).

## General Compute Engine best practices

  * Understand which [versions of Windows Server](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server) are supported, best suited for your use case, and which versions might be coming up to the [end of Windows Server support on Google Cloud](https://docs.cloud.google.com/compute/docs/instances/windows/end-of-support). Further information can be found at [Lifecycle FAQ from Microsoft](https://learn.microsoft.com/en-us/lifecycle/faq/extended-security-updates).
  * Understand how to correctly [Add a persistent disk to your Windows VM](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-windows).
  * Enable or disable Windows Server operating system features not required for the services run by your organization, unused features will consume resources you might not be using.
  * Launch new instances with the latest image version provided by Google Cloud public images, if you are using [Pay-as-you-go (PAYG) licence](https://docs.cloud.google.com/compute/docs/licenses/about).



## Security

  * If you are running Windows, you should be running antivirus software. Malware and software viruses present a significant risk to any system connected to a network, and antivirus software is a simple mitigation step you can use to protect your data. Microsoft provides advice about on [antivirus software](https://support.microsoft.com/en-US/windows-antivirus-software-providers).
  * Understand how to [create new local users](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials#create_a_local_user_account) and [grant/revoke Administrator privileges](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials#grant_local_users_administrator_privileges) on local accounts to limit critical applications and system files.
  * If you are using Active Directory, make use of [Configuring User Access Control and Permissions](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/configure/user-access-control) to implement the principle of least privilege for user permissions within the Windows operating system. For further information see [summary of best practices for Active Directory](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn487442\(v=ws.11\)).



### Best practices for securing Windows VMs with BitLocker

Bitlocker provides enhanced protection for your Windows operating system (OS) and data drives, but the increased security comes with the added risk of inadvertently losing access to your own data. You are responsible for ensuring the backup of your recovery key. Don't rely solely on the vTPM for seamless boots in a disaster recovery scenario. You should always externally store the BitLocker recovery key.

**Warning:** If you lose access to your BitLocker recovery keys, then you won't be able to decrypt the disks and the data is unrecoverable. Google can't recover your data if you lose your BitLocker recovery keys.

To prevent losing access to your data, follow these best practices to safely store your BitLocker recovery keys.

  * Ensure that you don't start BitLocker encryption unless the recovery key is stored in [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs). For more information, see Require BitLocker escrow with a Group Policy Object (GPO).
  * Deploy your Active Directory instance across multiple regions to ensure you can access your recovery keys even during a regional outage.
  * Periodically export your recovery keys to a secure, versioned location such as a [Cloud Storage](https://docs.cloud.google.com/storage/docs/buckets) bucket in a different project or a [Secret Manager](https://docs.cloud.google.com/secret-manager/docs) instance.
  * Certain operations or modifications On Shielded VM instances, such as changing the vTPM or recreating an instance from a disk, trigger recovery mode. Once the instance is in recovery mode, you can't access the instance until you enter the recovery key. Therefore, you must always maintain an external copy of the recovery key.



#### Require BitLocker escrow with a Group Policy Object (GPO)

To prevent losing access to your BitLocker-encrypted disks, configure your instances to ensure that encryption never starts unless the recovery key is safely stored in Managed Service for Microsoft Active Directory.

  1. Open the Group Policy Management Console: on your Domain Controller or management VM, open `gpmc.msc`.
  2. Create a GPO: create a new GPO linked to the OU containing your Compute Engine Windows instances.
  3. Open the BitLocker Policies: Click **Computer Configuration** > **Policies**
  4. Click **Administrative Templates**.
  5. Click **Windows Components**
  6. Click **BitLocker Drive Encryption**.
  7. Click **Operating System Drives**.
  8. Configure backup requirements: 
     1. Open **Choose how BitLocker-protected operating system drives can be recovered**.
     2. Select **Enabled**.
     3. Select **Do not enable BitLocker until recovery information is stored in Active Directory DS for operating system drives**.
     4. Make sure **Store BitLocker recovery information in AD DS** is selected and set to store both recovery passwords and key packages.
     5. To protect secondary disks, repeat these steps for the **Fixed Data Drives** folder.



For detailed information about configuring BitLocker, see [Configure BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/configure?tabs=common#windows-edition-and-licensing-requirements).

To recover a Windows VM that requires a BitLocker recovery key, see [Recover a Windows VM that requires a BitLocker recovery key](https://docs.cloud.google.com/compute/docs/disks/recover-vm#recover-windows-vm-bitlocker).

## Backup & Recovery

  * Routinely review and verify your backup and recovery strategy.
  * Enable regular [disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots) for a quick recovery from a previous backup if there is a VM failure. 
    * Only enable [VSS](https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service) snapshots on data volumes and where the application is VSS compatible. Avoid [creating VSS snapshots](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot#create-snapshot) on the operating system disk because the VSS service marks this disk as read-only.



## Patch Management

  * Confirm your Windows operating system is updated to the latest version and all system and quality updates (also referred to as "cumulative updates" or "cumulative quality updates") are installed.
  * Make use of automatic Windows Update on your instance. Microsoft releases patches every second Tuesday of each month at minimum. You should have a strategy for applying these updates to help safeguard the system from known bugs and vulnerabilities. If automatic restarts are not an option, consider [creating patch jobs by using VM Manager](https://docs.cloud.google.com/compute/docs/os-patch-management), which can schedule updates and restart your instances at an appropriate time.



## Logging and Monitoring

  * [Enable virtual displays](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display) to better understand the current state of the operating system, and to allow you to view the console in case your instance is inaccessible.
  * If your VM instance is stopped, logs from the [serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console) will no longer be available, to retain these logs you can [stream serial port output to Cloud Logging](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#enable-stackdriver) and use the output stored to assist with troubleshooting and auditing.
  * Consider configuring the [Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent) to centralize the logs you see in Event Viewer by [streaming logs to Cloud Logging](https://docs.cloud.google.com/logging/docs/agent/ops-agent/authorization), this allows for easier retrieval of the logs and more consistent retention. This step is completely optional, but recommended.
  * Consider installing the [Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent) to monitor and retain the monitoring data of your instance performance.
  * Consider [streaming logs from third-party Applications](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party).



## Google related drivers, agents & features

  * When you use Microsoft software, you are responsible for understanding and complying with any licensing agreements that you might have with Microsoft. To understand the requirements and options for licensing, refer to the [Microsoft Licenses](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing) documentation.
  * Keep the guest environment updated in line with your Windows Update strategy. Regularly [updating the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#update-guest) of your Windows instance will ensure you are running the latest and most stable version of all necessary Google Cloud agents and drivers.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
