---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/about-connector/
title: About the Backup and DR agent for appliance-managed backups \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:19.085458+00:00
---

# About the Backup and DR agent for appliance-managed backups  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/about-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  About the Backup and DR agent for appliance-managed backups Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page describes the Backup and DR agent, including How to obtain the right Backup and DR agent for your host. The Backup and DR agent is a small-footprint process that you install on your hosts.

## Backup and DR agent capabilities

The Backup and DR agents:

  * Discover and backup individual and groups of applications, including Microsoft SQL Server clusters.

  * Quiesce applications for application consistency during backup.

  * Enable change block tracking on Windows hosts and low-splash on non-Windows hosts for incremental-forever backup.

  * Backup and manage transaction logs, including truncating database transaction logs and rolling database transaction logs forward for point-in-time recovery.

  * Rescan storage buses, bring new devices online, assign drive letters, import volume groups, and mount file systems based on the operating system of the application host.

  * Prepare application volumes for restore operations.

  * Enable agent-based backups of applications on pRDMs and vRDMs on VMware VMs to avoid potential virtual server stun issues caused by VMware snapshots. Also, Backup and DR agents enable backups of Microsoft SQL Server clusters running on VMware VMs.

  * When the Backup and DR agent manages data movement, the backup/recovery appliance presents a staging disk to store a copy of changed application data during each snapshot job.




## Obtain the right Backup and DR agent for your host

The appliance management console has four different Backup and DR agent installer files. Each is of a file type appropriate to its intended host type.

For OS | Running on | Use this agent  
---|---|---  
Red Hat, CentOS, SLES | i686 32-bit Intel architecture | connector-Linux_x86-version.rpm  
Red Hat, CentOS, SLES | x64 64-bit Intel architecture | connector-Linux-version.rpm  
Debian, Ubuntu | x64 64-bit Intel architecture | connector-Linux_Ubuntu_amd64-version.deb  
Windows Server | Both 32-bit and 64-bit Intel architecture | connector-win32-version.exe  
  
## Download a Backup and DR agent installer file

You can download a Backup and DR agent installer file with a web browser from the appliance management console using the following steps:

  1. In the appliance management console, go to the **Manage** drop-down menu and click **Appliances**.

  2. Right-click an appliance and select **Configure Appliance**.

  3. Select **Agent Management**. The four installer files appear at the top of the window. Download the agent installer file that you need.

  4. Depending on your host operating system, install the Backup and DR agent:

     * To install the Backup and DR agent on the Linux host, refer to [Install the Backup and DR agent on a Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent).

     * To install the Backup and DR agent on the Windows host, refer to [Install the Backup and DR agent on a Windows host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/windows-agent).

**Note:** Port 5106 must be open for `UDSAgent` to ensure that the backup/recovery appliance can communicate with the Backup and DR agent on the host. This requires an ingress firewall rule where the backup/recovery appliance is the source, the host running the agent is the target, and the target port is 5106. Also, you don't need to add port 5106 to the default ingress rule created for the appliance, as this specifies the appliance as the target.
  5. When the installation is complete, a secret key displays. Save the secret key in a notepad or in a text editor, you need to add this in the Backup and DR agent section in [Linux](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-linux-hosts) or [Windows](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-windows) hosts. This secret key is valid for two hours.




## Network traffic

Traffic between the backup/recovery appliances and the Backup and DR agent on your hosts is encrypted and communicates by SSL. The Backup and DR agent uses port 5106 by default for communication from the appliance. Make sure your firewall permits communication through this port. If you have existing services using this port, contact Support for assistance.

## Antivirus software

These are some high-level recommendations for antivirus software. Specific antivirus or security products may call things by different names, not support some features as process exclusion is commonly not supported, and are configured by different means.

  * **Exclude the`udsagent` process from Antivirus Monitoring**: This is typically called process exclusion or process threat level. Excluding anything that `UDSAgent.exe` for Windows or `udsagent` for Linux does from scanning provides the best performance for the backup and the least chance that the antivirus software blocks anything.

  * **Exclude scanning of mounted staging disks** : Prevent the antivirus software from scanning the files that Backup and DR writes to the staging disk. This is typically slower than reading files on the protected volume already.

### Windows
        
        C:\Windows\act\*.*
        C:\Windows\act\
        C:\Program Files\Google Cloud Backup and DR\UDSAgent.exe
        C:\Program Files\Google Cloud Backup and DR\driver\aamservice.exe
        C:\Program Files\Google Cloud Backup and DR\log\*.*
        C:\Program Files\Google Cloud Backup and DR\tmpdata\*.*
        C:\Program Files\Google Cloud Backup and DR\act_scripts
        

### Linux
        
        /opt/act/bin/udsagent
        /act/mnt
        

**Note:** You might still have failures if the antivirus software blocks the Backup and DR agent from opening or reading a file on the protected volume.
  * **Disable antivirus heuristics** : This is not required, but may help in some cases. Antivirus heuristics typically block operations that look suspicious. When the Backup and DR agent is running a backup of a system volume, it looks suspicious since it is reading the contents of the Windows directory and recreating it on the staging disk.

In some cases, disabling the antivirus software fails to prevent backup failures, but disabling the antivirus software heuristics allows backups to succeed.




## What's next

  * To install Backup and DR agent on a Linux host, see [Install the Backup and DR agent on a Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent)

  * To install Backup and DR agent on a Windows host, see [Backup and DR agent on Windows hosts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/windows-agent)

  * To upgrade Backup and DR agent, see [Maintain Backup and DR agents on hosts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-agent)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
