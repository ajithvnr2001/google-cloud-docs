---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/vmware-backup-recovery-bv/
title: Protect and recover a VMware VM from a backup vault in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:56.398474+00:00
---

# Protect and recover a VMware VM from a backup vault in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/vmware-backup-recovery-bv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Protect and recover a VMware VM from a backup vault in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

This page provides you an end-to-end overview about protecting a VMware VM running in Google Cloud VMware Engine using backup vault, how to backup and restore your Google Cloud VMware Engine, and monitor backups.

## Before you begin

Before you can start backing up Google Cloud VMware Engine instances, use the following procedures and deploy Backup and DR:

  1. [Set up and plan a Backup and DR deployment](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan)
  2. [Prepare to deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-prep)
  3. [Deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-guide)



## Prerequisites to configure backups

Google Cloud VMware Engine is a fully managed service that lets you run the VMware platform in Google Cloud. Google manages the infrastructure, networking, and management services. For more detailed information, refer to [VMware engine](https://docs.cloud.google.com/vmware-engine/docs/overview) documentation. This quickstart helps you protect and recover VMware VM workloads using Backup and DR. To start backing up a Google Cloud VMware Engine instance, you must read and complete the following procedures:

  * [VMware - API access and quota](https://docs.cloud.google.com/vmware-engine/docs/quickstart-prerequisites)
  * [Networking requirements](https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements)
  * [IAM roles and permissions](https://docs.cloud.google.com/vmware-engine/docs/iam)
  * Create a [Google Cloud VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud)
  * [Add a private connection between your Google Cloud VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access#complete-private-connection-creation-in-the-vmware-engine-portal) and the VPC where your backup/recovery appliance is deployed.



### Configure backup/recovery appliance network settings

During Google Cloud VMware Engine backup jobs, the backup/recovery appliance needs to resolve the fully qualified names of the ESX servers running in your Google Cloud VMware Engine private cloud. To achieve this, add a DNS from your private cloud to the backup/recovery appliance.

**On Google Cloud VMware Engine**

In the Google Cloud VMware Engine, complete the following:

  1. Click **Resources** , then select your private cloud.

  2. Using the **Private cloud DNS servers** option, copy either one or both IPs.




If you can't add a DNS from your private cloud, you need to manually add a host entry for each ESX host in the **System management** > **Host resolution** tab.

**In the Backup and DR management console**

In the Backup and DR appliance management console, complete the following:

  1. Go to **Manage** > **Appliances**.

  2. Right-click the appliance and select **Configure appliance networking**.

The **System management** page opens in a new window.

  3. In the **DNS, NTP** page:

     1. Add the DNS as either primary or secondary. Enter the IP address of your primary DNS server and your secondary DNS server, the secondary DNS is optional.

     2. Remove any unneeded DNS suffix searches. If you set any entries in **DNS Suffix Search** , then the DNS Domain will NOT be searched.




To troubleshoot problematic network connections, try the following in the **Troubleshooting** section:

  * Click the **Utility** drop-down and select **Test DNS**.

  * Click the **Resolve** drop-down and select **IP** , then enter the source or destination IP in the **IP to resolve** field. The test DNS should resolve to a name. If it doesn't, validate the connectivity between the Google Cloud VMware Engine private cloud and the Backup and DR VPC.




### Set NFS ingress firewall rules for the backup/recovery appliance

When performing VMware VM mounts using NFS, the backup/recovery appliance provides access to the VMDKs (Virtual Disk File file format) using an NFS datastore. You need to set the ingress firewall rules for the backup appliance to ensure NFS mounts don't encounter unexpected errors.

  1. In the Google Cloud console, go to the **Firewall** page. 

[Go to Firewall](https://console.cloud.google.com/networking/firewalls/list)

  2. Find the VPC firewall rule for your backup/recovery appliance that contains the following:

     * **Target** : Service account for your backup appliance.

     * **tcp** : 26, 443, 3260,5107

  3. Edit the firewall rules and add the following:

     * In the **Source IPv4 range** , add the system management subnet of your Google Cloud VMware Engine private cloud. Find the system management subnet in Google Cloud VMware Engine portal by navigating to **Resources** , then **Select your private cloud** , then **Subnets**.

     * **tcp** : 26, 111, 443, 756, 902, 2049, 3260, 4001, 4045, 5107

     * **udp** : 111, 756, 2049, 4001, 4045

  4. Click **Save**.




To authenticate to the Google Cloud VMware Engine vCenter, you need to retrieve or reset the solution user password using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or API commands. For instructions on retrieving or resetting the solution user password, see [Get a solution user password](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege#get_a_solution_user_password).

## Add a new vCenter host to the appliance management console

Backup and DR uses VMware vSphere Storage APIs data protection to create backup images of VMware VMs, placing these backup images either in the snapshot pool of the backup/recovery appliance or in OnVault pools. [OnVault pools created with the backup vault type](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-gcve-into-backup-vault#onvault) store data in the backup vault. See [Add vCenter and ESX server hosts to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host).

To issue API calls, the backup/recovery appliance needs to connect to the vCenter host with a username and password that have authorization to perform the required backup creation actions. In this section, add the vCenter as a host and supply those user credentials that are stored securely by the service.

To add a new vCenter host to the appliance management console, complete the following:

  1. In the appliance management console, go to **Manage** then **Hosts**.

  2. Click **add Add host**.

  3. In the **Add host** field, enter the name and an optional friendly name. The name of a host should start with a letter, and can contain letters and digits (0-9). Underscore (`_`) characters aren't valid in host names.

  4. Enter the IP address of the vCenter server appliance in **IP address**.

  5. In the **Appliances** section, select the appliance management console managed appliances that you want to serve this host. If the list is long, you can use the search box to find a specific appliance or group of appliances.

  6. From the **Host type** drop-down, select **vCenter** and add the following:

     * Validate the data transport mode, either NFS or SAN. NFS is the default setting and we recommend you don't change it.

     * Enter the username and password of the solution user you configured earlier to connect to the vCenter server appliance and then use the **Test** button to validate the added credentials.

  7. Click **Add**.




## Create a backup plan

A backup plan includes a template that defines when and how to capture a backup, and a resource profile that defines where to save the backup.

Refer to [Create a backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) to create a template and assign a [backup policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview).

A resource profile specifies the storage media for VMware VM data backup images. Resource profiles define which snapshot pool is used (if a snapshot policy is in the template) and which OnVault pools are used. For more information, see [Create a resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-resource-profiles).

In this quickstart you will create a resource profile that assigns a backup vault as the storage for the VM backup.

OnVault pools can point to backup vaults or to Cloud Storage to store Google Cloud Google Cloud VMware Engine backups. Sending backups to a backup vault provides protection against modification (immutability) and deletion (indelibility). For more information about backup vault, see [Overview of backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

To create and store data in a backup vaults, see [Back up VMware Engine into a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-gcve-into-backup-vault).

After you have created a resource profile, you can apply a backup plan template and profile to the VMware VMs.

## Discover the VM and apply a backup plan template

You can use the [onboarding wizard](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/onboarding-wizard) to discover VMware virtual machines (VMs) managed by a vCenter. Once you have discovered one or more applications, you can protect them all at once by applying a [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-template-to-manage-a-vm), and [resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-resource-profiles), or you can add them to the applications list as unmanaged or ignored VMs.

Use the following instructions to discover and protect VMware VMs by applying a backup template and resource profile.

### Discover VMware VMs

  1. Click **App Manager** , and select **Applications** , then click **Add Application**.

  2. Select **Google Cloud VMware Engine**.

  3. From the server list, select a vCenter where you want to perform VM discovery and click **Next**.

  4. On the **Manage** page, a list of VMs appears. Select a VM to discover and click **Next**.




### Protect VMware VMs

The following steps help you back up Google Cloud VMware Engine:

  1. Apply the backup policy template and resource profile to the Google Cloud VMware Engine instance:

  2. Select a VM that you want to protect.

  3. Select **Manage backup configuration**.

  4. From the **Choose action** drop-down list, select **Manage backup configuration**. The **Choose template** drop-down list opens.

  5. Select a template. The **Choose profile** drop-down list opens.

  6. Click **Apply backup plan**.

  7. If there are multiple VMs and you want to make the same changes to all the VMs, click **Define settings** for all applications and make the necessary changes.

  8. Click **Application Settings** for each VM in the list to make changes to the default configuration.

  9. The **Application Details and Settings** page opens. See [Configure application settings for VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-vmware-vm).

  10. Click **Next**.

  11. Review the summary screen. If everything is accurate, select **Finish** to complete the onboarding process. The selected VMs are backed up based on the backup policy template you select.

  12. After onboarding is complete, a dialog appears. Click **Finish** again. Once the policy template is attached to the selected VMs, the status changes to a green check mark. The green check indicates that a backup job can be run for the VM within the schedule by the policy.




If you want to run the job immediately, run an on-demand backup as follows:

  1. Click the **App Manager** tab and select **Applications** from the list. The **Applications** page opens.
  2. Select an Google Cloud VMware Engine instance and then click **Manage Backup Configuration** from the drop-down list at the bottom right corner of the page.
  3. From the **Policies** drop-down, select **Snapshot**.
  4. Enter a name into the **Label** field, and click **Run Now**. An on-demand backup is triggered for the selected policy.
  5. You can view the progress of the Google Cloud VMware Engine backup job from the **Jobs** tab. See [monitor jobs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs).



## Recover a VMware VM

There are two ways to recover your VMware VM:

  * Use the restore function to restore data from a backup image. To restore a VM, see [Restore data from a backup image.](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm).

  * Cloning a VMware VM backup creates a new VMware VM that has no dependency on a backup/recovery appliance. As with a restore operation, it copies all the data before the VM is available. To clone a VM, see [Clone an image of a VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-vm).




## Monitor

You can view the progress of the Google Cloud VMware Engine backup job from the **Jobs** tab. See [monitor jobs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
