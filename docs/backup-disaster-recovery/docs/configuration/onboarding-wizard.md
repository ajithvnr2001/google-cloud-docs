---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/onboarding-wizard/
title: Discover applications on your hosts from the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:02.649103+00:00
---

# Discover applications on your hosts from the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/onboarding-wizard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Discover applications on your hosts from the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

To manage your application, the appliance management console must discover the applications, VMs, and Cloud instances managed through its appliances.

Use the **Application Back up wizard** to discover applications within a host or in a VM. Once you discover one or more applications, VMs, or cloud instances, you can protect them all at once by applying a backup template and profile or you can add them to the appliance management console as unmanaged or ignored.

You can access the wizard from:

  * Back up & recover menu.

  * Add applications in **App Manager** menu.




## Back up & recover menu

The **Back up & Recover** menu provides two wizards to help you back up and recover your databases and applications.

  * Click the Back up option to open the application back up wizard. From here you can discover and manage applications and VMs.

  * Click the Recover option to open the **Data Recovery** wizard. From here, you can mount, restore, and perform other data access operations.




### Application back up wizard

The **Application Back up** wizard helps you discover and manage applications and VMs.

Use the following instructions to open the **Application Back up** wizard:

  1. Click **Back up & Recover** and select **Back up** from the drop-down menu.

The **Application Back up** wizard opens.

  2. From this wizard, you can you discover and protect applications and VMs.




### Data recovery wizard

The **Data Recovery** wizard helps you access backed up data. Application data can be backed up in a physical or a virtual machine.

Use the following instructions to open the recovery wizard:

  1. Click **Back up & Recover** and select **Recovery** from the drop-down menu.

  2. Select the applications or databases that you want to recover and click **Next**.

The **Application Recovery** page opens with the timeline ramp view. From the [timeline ramp view](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time), you can perform various access actions like performing a mount, clone, and restore as detailed in [Access captured and backed up data](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-captured-and-backed-up-data).




## Add applications

The **Add Application** wizard helps you discover and manage applications and VMs.

Use these instructions to open the **Add Application** wizard:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Application Management** page opens.

  2. Click **+Add Application** in top right corner to launch the **Add Application** wizard.

  3. From this wizard, you can you discover and protect applications and VMs, including:

     * [Discover and Protect Consistency Groups](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-consistency-groups)
     * [Discover and Protect Generic Applications](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-generic-apps)
     * [Discover and Protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-vms)
     * [Discover and Protect Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-compute-engine)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
