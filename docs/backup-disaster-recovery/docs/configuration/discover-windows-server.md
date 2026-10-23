---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-windows-server/
title: Add Windows server hosts to the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:29.902451+00:00
---

# Add Windows server hosts to the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-windows-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Add Windows server hosts to the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR supports Windows server application types that include Microsoft SQL Server, SMB, and local file systems. Before you can discover and back up data from these hosts, you must do the following:

  * [Install the Backup and DR agent on Windows host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/windows-agent)

  * Add the Windows host




## Add Windows host

If you have added the Windows server to Backup and DR as a Compute Engine instance or as a VMware VM, then a host for this VM already exists and you don't need to add it again using the following procedure. Instead, find and edit that host and proceed from step 7.

Use the following instructions to add a new Windows Server host to appliance management console: 

  1. Click **Manage** > **Hosts**.

  2. Select **\+ Add Host**.

  3. In the **Add Host** form, enter the name and an optional friendly name. The name of a host should start with a letter, and can contain letters and digits (0-9). Underscore ('_') characters are not valid in host names.

  4. Enter the IP address of the host in **IP Address**. Click the **plus sign (+)** to add it.

  5. In the **Appliances** section, select the appliance management console managed appliances that serve this host. If the list is long, you can use the search field to find a specific appliance or group of appliances.

  6. Leave **Host Type** as **Generic**.

  7. Enter **Application Discovery Credentials** to discover and protect the database applications on the host. This field is applicable only for MaxDB, PostgreSQL, SAP ASE, and SAP IQ databases.

  8. In the Backup and DR agent settings, complete the following:

     * The Backup and DR agent port is normally port 5106. If it is anything else, enter the port number here.

     * If there are CIFS shares that need to be discovered you must supply a username and password that can access those CIFS shares.

     * You must supply the secret key generated on the Windows host using the instructions [Install the Backup and DR agent on a Windows host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/windows-agent) or [Regenerate the secret key](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/windows-agent#regenerate) section. You can add the secret key now or later using the Add a secret key instructions but before running the application discovery.

  9. Click **Add**.




### Add a secret key

If you want to update the secret key or if you did not add the secret key for the first time, you can add it in the Windows host using the following instructions.

  1. Click **Manage** and then select **Hosts**.

  2. Right-click the Windows host and choose **Edit**.

  3. Scroll to **Backup and DR Agent Settings** section and find the **Secret** field.

  4. Paste the secret key that you saved earlier in the **Secret** field and click **Save**. Ensure the certificate status changes to **Valid**.




## Find logs and scripts on Windows server hosts

On a Microsoft Windows server host, UDSAgent.logs are stored in `C:\Program Files\Google Cloud Backup and DR\log`

You can create scripts to perform pre- and post- actions on applications on your Windows hosts. Create a new folder in which to store all scripts: `C:\Program Files\Google Cloud Backup and DR\scripts`.

**Note:** The Backup and DR agent can be firewalled out if the host joins a domain after the Backup and DR agent has been installed. If this happens, uninstall and then re-install the Backup and DR agent.

## Discover local file system

Use these instructions to add local file systems, you must do the following:

  1. Discover the local file system in either of these ways:

     * Go to **Back up & Recover** and select **Back up**.

     * Go to **App Manager** , click **Applications** , and then select **Add application**.

  2. Select the **All Apps** tile. If you select the **All Apps** tile you also discover Microsoft SQL Server apps. After the local file systems are discovered, you can find them using the file system filter in the **Applications** page.




## Service access point IP address for cluster support

If a file system is a cluster resource and if you want it to be backed up irrespective of which cluster node is hosting the file system, specify the Cluster resource IP address as a Service Access Point IP. This allows the backup/recovery appliance to connect to the Backup and DR agent using the cluster resource IP and to back up the file system from the active cluster node. For backup to work correctly across all cluster nodes, the Backup and DR agent must be installed on all cluster nodes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
