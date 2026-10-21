---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/install-agent-windows/
title: Install the Backup and DR agent on a Windows host \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:53.155035+00:00
---

# Install the Backup and DR agent on a Windows host  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/install-agent-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Install the Backup and DR agent on a Windows host Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page describes how to install the Backup and DR agent on a Windows host and perform other operations such as check the status of your backup, restart, and uninstall the Backup and DR agent.

## How it works

The Backup and DR agent for Microsoft Windows runs as a Windows service under the Local System account. The Backup and DR agent writes logs to a log file in its installation directory. For Microsoft Windows Server, the installer comes in `connector-Win32-<version>.exe` format.

**Note:** If you intend to manage multiple clustered Windows hosts, then install a Backup and DR agent on each host.

When you install the Windows Backup and DR agent, you have the option to install the Change Tracking Driver. If you plan to protect Microsoft SQL Server applications, install the Backup and DR agent with the Change Tracking Driver to enable efficient incremental backups.

Microsoft SQL Server is supported on NTFS and ReFS volumes. The Change Tracking Driver doesn't support SMB volumes.

After you install the agent, you need to initialize trusted communications between the backup/recovery appliance and the Backup and DR agent. This only needs to be done once. The secret key needs to be added within two hours of being generated. If the secret key expires, you need to generate a new key.

## Install the Backup and DR agent on a Windows host

To install the Backup and DR agent on a Windows host, use the following instructions:

  1. Download the Windows Backup and DR agent from the [Obtain the right Backup and DR agent for your host](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/about-connector#right-connector) section.

  2. Log on to the host as a user with the **Administrator** account type.

  3. If this is a Compute Engine instance, you need to ensure the iSCSI initiator is started and also ensure it auto-starts upon reboot. To do this, launch the **iSCSI Initiator** application using the following steps.

     1. Click the **Start Menu**.

     2. Type in **iSCSI Initiator** to find the application.

     3. Launch the process.

     4. When prompted to enable iSCSI, click **Yes**.

The **iSCSI Initiator** page appears. To close it, click **OK**.

  4. Copy the installer file to your Windows server.

  5. Launch `connector-win32-version.exe.`

  6. Click **Run** and follow the setup wizard instructions.

  7. Select the designated location where you want to install the agent and click **Next**.

  8. If you intend to protect SQL Server databases, select **Backup and DR agent with Change Tracking Driver** and click **Next**.

  9. Select the **Add windows Firewall rules to enable communication on the default port (5106)** checkbox and click **Next**.

**Note:** Port 5106 must be open for UDSAgent to ensure that the backup/recovery appliance can communicate with the agent running on the host. This requires an ingress firewall rule where the backup/recovery appliance is the source, the host running the agent is the target and the target port is 5106. Additionally, you don't need to add port 5106 to the default ingress rule created for the appliance, as this specifies the appliance as the target.
  10. Click **Install**.

  11. After you install the agent, a secret key is displayed. Save the key in the Backup and DR agent section of [Add Windows host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-windows). This secret key is valid for 2 hours.

**Note:** If at completion, the agent doesn't display a secret key, you need to manually generate a key.
  12. Click **Finish**.




### Check Backup and DR agent status

After the agent is installed, you can verify its status on the Windows hosts.

#### Verify the agent is running

To verify that the Backup and DR agent is running, run the following command on the host. This opens up the Microsoft Management Console (MMC) snap-in for **Services**.

  1. Run the following command:
         
         services.msc
         

  2. Verify the following services are both in the **Running** status with **Automatic** startup type:

     * Google Cloud Backup and DR agent

     * Google Cloud Backup and DR CBT agent




### Install the Backup and DR agent from the Windows command prompt

To install the Backup and DR agent from a script or from a Windows command prompt, use the following instructions.

  1. Open a Windows Command prompt using the **Run as administrator** option.

  2. Run the following command from the directory where you copied the agent installer file.
         
         connector-Win32-version.exe /SUPPRESSMSGBOXES /NORESTART /VERYSILENT /TYPE=FULL
         




### Regenerate the secret key

The secret key that is generated in the Install the Backup and DR agent on a Windows host section is valid only for two hours. You need to add it to the management console within this timeframe or generate a new one.

To generate a new key and add it to the appliance management console, use the following instructions:

  1. Open a Windows Command prompt using the **Run as administrator** option.

  2. Change to the install directory. By default, the command would be `cd C:\Program Files\Google Cloud Backup and DR`:

     * To reset the secret key after confirmation the action, run the following command:
           
           UDSAgent secret --reset
           

     * To reset the secret immediately without confirmation, run the following command:
           
           UDSAgent secret --reset --restart
           

  3. Save the secret key in a notepad or in editor. This secret key is valid for two hours.




### Restart the Backup and DR agent on a Windows host

To restart the Backup and DR agent on a Windows host use the following instructions:

  1. Open **services.msc** on the host.

  2. Select **Google Cloud Backup and DR agent** and click **Restart**.




### Uninstall the Backup and DR agent

To uninstall the Backup and DR agent, use the following instructions:

  1. Open a Windows Command prompt using the **Run as administrator** option.

  2. Go to the c`:\Program Files\Google Cloud Backup and DR` folder created during the installation.

  3. Select and double-click the uninstaller executable: `unins000.exe`

  4. Click **Yes** to confirm and then click **OK** to finish.




### Uninstall the Backup and DR agent from command prompt

To uninstall the Backup and DR agent using a script or from a command prompt, use the following instructions.

  1. Open a Windows Command prompt using the **Run as administrator** option.

  2. Run the following command.
         
         "C:\Program Files\Google Cloud Backup and DR\unins000.exe" /VERYSILENT /NORESTART /SUPPRESSMSGBOXES
         




### Add a secret key

If you want to update the secret key or if you didn't add the secret key the first time, you can add in the Windows host using the following instructions:

  1. Go to the appliance management console, select **Manage** and then select **Hosts**.

  2. Right-click the Windows host and choose **Edit**.

  3. Go to the **Backup and DR agent Settings** section and find the **Secret** field.

  4. Paste the secret key that you saved earlier in the **Secret** field and click **Save**. Ensure the Certificate status changes to **Valid**.




## What's next

  * To install the Backup and DR agent on a Linux host, see [Install the Backup and DR agent on a Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent)

  * To install the Backup and DR agent on a Windows host, see [Backup and DR agent on Windows hosts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/windows-agent)

  * To upgrade the Backup and DR agent, see [Maintain Backup and DR agents on hosts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-agent)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
