---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-agent/
title: Maintain the Backup and DR agent for appliance-managed backups \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:53.474999+00:00
---

# Maintain the Backup and DR agent for appliance-managed backups  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Maintain the Backup and DR agent for appliance-managed backups Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page describes how to manage or upgrade the Backup and DR agent on a host.

The Backup and DR agent management tool lets you uninstall or upgrade the Backup and DR agent on your hosts when new versions are available.

## Upgrade Backup and DR agent

You can use the agent management tool to upgrade the Backup and DR agent on your hosts when new versions are available.

**Note:** You must have at least 1 GB of free space in the /opt directory for UDSAgent to install or upgrade on Linux hosts.

Use the following instructions to upgrade Backup and DR agent from agent management:

  1. In the appliance management console, click the **Manage** drop-down menu and select **Appliances**.

  2. Select an appliance.

  3. Click **Configure Appliance** to open the **Appliance Configuration** page.

  4. Go to **Configuration** then **Agent Management**.

In the **Latest Available Agents** section, you can view the available version in the **Discovered Hosts** section, including the version of the agent installed on that host.

  5. From the **Discovered Hosts** section, select a host that you want to upgrade the agent for and click the **plus sign (+)**. You can add multiple hosts one at a time.

  6. Click **Upgrade**.

  7. In the **Agent Upgrade** window, select **Start Upgrade** or **Force Upgrade** and then click **Submit**. A message appears that indicates the status of the upgrade. You can check the status of the Backup and DR agent from the **Current status** column.




## Manage Backup and DR agent

You can use the agent management tool to manage the Backup and DR agent on your hosts.

Use the following instructions to manage Backup and DR agent from agent management:

  1. In the appliance management console, click the **Manage** drop-down menu and select **Appliances**.

  2. Select an appliance.

  3. Click **Configure Appliance** to open the **Appliance Configuration** page.

  4. Go to **Configuration** and click **Agent Management**.

The latest available Backup and DR agents with version and discovered hosts appears.

  5. From the discovered hosts section, select a host and click the **plus sign (+)** icon.

  6. Choose one of the options per host:

     * **Abort** : Abort agent upgrade in progress

     * **Rescan** : Rescan the host to detect current agent version

     * **Remove** : Remove the agent from the list. This doesn't uninstall the agent.

     * **Uninstall** : Uninstall the agent from the host.




## What's next

  * To install Backup and DR agent on a Linux host, see [Install the Backup and DR agent on a Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent)

  * To install Backup and DR agent on a Windows host, see [Backup and DR agent on Windows hosts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/windows-agent)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
