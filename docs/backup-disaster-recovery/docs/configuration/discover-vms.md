---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-vms/
title: Discover and protect VMs in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:55.020307+00:00
---

# Discover and protect VMs in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Discover and protect VMs in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Use the onboarding wizard to discover VMware virtual machines (VMs) managed by a vCenter or by an individual ESXi server. Once you discover one or more applications, you can protect them all at once by applying a [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) and [profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles#create-profile) or you can add them to the applications list as unmanaged or ignored VMs.

To discover and protect VMware VMs:

  1. In the appliance management console, click the **App Manager** drop-down menu and select **Applications**.

  2. Click **Add Application**.

  3. Select **VMware Engine**.

  4. Click **Add New Server** to add vCenters or an ESXi server.

  5. Select a vCenter or an ESXi server where you want to perform VM discovery and click **Next** from the server list.

  6. On the **Manage** page, a list of VMs appears. Select a VM to discover and click **Next**.

  7. Apply the policy template and profile to the Compute Engine instance:

     1. Select one or more VMs that you want to protect.

     2. Select **Apply Backup Plan**.

     3. Select **Apply Backup Plan** from the **Choose action** drop-down list.

The **Choose template** drop-down list opens.

     4. Select a template from the **Choose template** drop-down list.

The **Choose profile** drop-down list opens.

     5. Click **OK**.

  8. Click **Application Settings** for each VM in the list to make changes to the default configuration.

The **Application Details and Settings** page opens. See [Configure application settings for VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-vmware-vm)

  9. If there are multiple VMs and you want to make the same changes to all the VMs, click **define settings for all applications** and make the necessary changes.

  10. Click **Next**.

  11. Review the summary screen. If everything is correct, click **Finish** to complete the onboarding process. The selected VMs are backed up based on the policy template that you select.

  12. After onboarding is complete, a dialog appears. Click **Finish** again.

Once the policy template is attached to the selected VMs, the status changes to a check mark.

The check mark indicates that your VMs are ready to run a backup job within the schedule by the policy. If you want to run the job immediately, see [Run on-demand job](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run).




## Add a server

In case the vCenter or ESXi server of interest isn't in the server list, add the VCenter or ESXi as new server using the following instructions.

  1. Click **Add New Server**.

  2. For **Type** , keep vCenter, the default, or select ESXi.

  3. Add the hostname and a friendly path for the host in **Hostname**. The name of the host must start with a letter, and contain letters, digits (0-9), and an underscore (___).

  4. Enter the IP address of the host in the **IP Address** field.

  5. Optionally, you can enter the port number—if you aren't using the default port number—in the **Port** field.

**Note:** The default management port is 443.
  6. Enter the login credentials for authentication in the **Username** and **Password** fields.

  7. Select one or more backup/recovery appliances where you want to add the server from the **Appliance(s)** checklist.

  8. Click **Add** to add the new server. If the information provided is incorrect, you see an error message and the new server isn't added.




## What's next

  * To define application settings, see [Configure application settings for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-application-settings-for-vmware-vm).



## The VMware administrator's guide

This page is one in a series of pages specific to protecting and recovering VMware VMs with Backup and DR. You can find additional information at:

  * [Backup and DR for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/vmware-intro)
  * [Configure Google Cloud VMware Engine for Backup and DR protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware)

  * [Add vCenter and ESX server hosts to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host)

  * [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)

  * [Apply a backup template to protect a VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-template-to-manage-a-VM)

  * [Configure Application settings for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-application-settings-for-vmware-vm)

  * [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm)

  * [Mount a VMware backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image)

  * [Clone a backup of a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-image-of-a-vm)

  * [Create LiveClone workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-liveclone-workflows)

  * [Move VM management between two backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-vmware)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
