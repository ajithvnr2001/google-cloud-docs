---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/vmware-backup-recovery/
title: Protect and recover VMware VMs \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:56.088163+00:00
---

# Protect and recover VMware VMs  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/vmware-backup-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Protect and recover VMware VMs Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a guide to protecting and recovering VMware virtual machines (VMs) running in VMware Engine using Backup and DR. It outlines how to configure backups, perform restores, and monitor your VMware environment.

## Overview

Google Cloud VMware Engine is a fully managed service that lets you run the VMware platform in Google Cloud. Google manages the infrastructure, networking, and management services. For more information about VMware Engine, see [the VMware Engine overview page](https://docs.cloud.google.com/vmware-engine/docs/overview).

## Before you begin

Before you can back up VMware Engine instances, you must complete the following Backup and DR procedures:

  1. [Plan a Backup and DR deployment](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan).

  2. [Prepare to deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-prep).

  3. [Deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-guide).

  4. To start backing up a VMware Engine instance, complete the following procedures in the listed order:

     1. [Enable the VMware Engine API and set quotas](https://docs.cloud.google.com/vmware-engine/docs/quickstart-prerequisites).

     2. [Meet networking requirements for using VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements).

     3. [Grant Identity and Access Management roles and permissions for VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/iam).

     4. [Create a VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud).

     5. [Add a private connection between your VMware Engine private cloud and the Virtual Private Cloud where your backup/recovery appliance is deployed](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access#complete-private-connection-creation-in-the-vmware-engine-portal).




### Configure DNS for Google Cloud VMware Engine

To allow your project to resolve hostnames in your VMware Engine environment, you must configure DNS binding between your project's VPC and the VMware Engine network. This allows the Backup and DR to communicate with vCenter and other resources in your private cloud.

  1. Identify the VMware Engine network associated with your private cloud. You will need its ID for the subsequent steps.

  2. Grant DNS binding permissions: The user or service account performing the DNS binding needs the `dns.peerings.create` permission on the project and the `vmwareengine.networks.bind` permission on the VMware Engine network.

  3. Use the `gcloud dns managed-zones create` command to create a DNS peering from your VPC to the VMware Engine network. This makes the DNS zones in the VMware Engine network resolvable from your VPC.
         
         gcloud dns managed-zones create PEERING_ZONE_NAME \
              --dns-name=PRIVATE_CLOUD_DOMAIN.gve.goog. \
              --visibility=private \
              --networks=VPC_NETWORK_NAME \
              --target-project=PROJECT_ID \
              --target-network=projects/PROJECT_ID/locations/global/vmwareEngineNetworks/VEN_ID \
              --description="Peering to GCVE"
         

Replace the following:
         
         `PEERING_ZONE_NAME`: A name for your DNS peering zone.
         `PRIVATE_CLOUD_DOMAIN`: The DNS zone of your private cloud.
         `VPC_NETWORK_NAME`: The name of your VPC network.
         `PROJECT_ID`: Your Google Cloud project ID.
         `VEN_ID`: The ID of your VMware Engine network.
         




For more detailed instructions, see the [Configure DNS bindings](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-dns-bindings) documentation.

## Configure backup job

During VMware VM backup jobs, the backup/recovery appliance needs to resolve the fully qualified names of the VMware ESX servers running in your VMware Engine private cloud. The easiest way to achieve this is to add a Domain Name System (DNS) from your private cloud to the backup/recovery appliance. If you don't want to do this, you need to manually add a host entry for each ESX host in the **Host resolution** tab on the **System management** page in the Google Cloud console.

  1. In the Google Cloud console, click the menu navigation menu.

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. In the **Compute** section, click **VMware Engine** to open Backup and DR.

  3. Select **Resources** , then select your private cloud.

  4. Under **Private cloud DNS servers** copy either one or both Internet Protocols (IPs).

  5. Go to Backup and DR in the Google Cloud console.

[Go to Backup and DR](https://console.cloud.google.com/backupdr)

     1. Click **Manage**.

     2. Click **Appliances**.

     3. Right-click the appliance and choose **Configure appliance networking**.

The **System management** page opens in a new window.

     4. Under the **DNS, NTP** page, add the DNS as either primary or secondary and remove any unneeded DNS suffix searches.

     5. Under **Troubleshooting** , complete the following steps:

        1. Click the **Utility** drop-down and select **Test DNS**.

        2. Click the **Resolve** drop-down and select **IP**.

        3. Enter the IP address in the **IP to resolve** field. It should resolve to a name. If it doesn't, validate the connectivity between VMware Engine private cloud and the Backup and DR VPC.




## Set NFS ingress firewall rules for the backup/recovery appliance

Use the following instructions to set the ingress firewall rules for the backup appliance to make sure NFS mounts don't encounter unexpected errors. When performing VMware Engine VM mounts using NFS, the backup/recovery appliance provides access to the virtual machine disk using an NFS datastore.

  1. In the Google Cloud console, go to the **Firewall policies** page in **Network Security**.

[Go to the Firewall policies page](https://console.cloud.google.com/networking/firewalls/list)

  2. Find the Virtual Private Cloud firewall rule for your backup/recovery appliance which contains the following information:

     * **Target** : the service account for your backup appliance. For example, `my-service-account@my-project.iam.gserviceaccount.com`

     * `tcp`: 26, 443, 3260,5107

  3. Edit the firewall rules and add the following information:

     * In the **Source IPv4 range** , add the system management subnet of your VMware Engine private cloud. Find the system management subnet in VMware Engine portal using the following steps:

       1. Go to **Resources**.

       2. Click **Select your private cloud**.

       3. Click **Subnets**.

          * `tcp`: 26, 111, 443, 756, 902, 2049, 3260, 4001, 4045, 5107

          * `udp`: 111, 756, 2049, 4001, 4045

  4. Click **Save**.


**Note:** To authenticate to the VMware Engine vCenter, you need to retrieve or reset the solution user password using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or API commands. For instructions about how to retrieve or reset the solution user password, see [Get a solution user password](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege#get_a_solution_user_password).

### Add a new vCenter host to the Backup and DR appliance management console

Backup and DR uses VMware vSphere Storage APIs data protection, formerly known as vStorage APIs for data protection or VADP, to create backup images of VMware VMs, placing these backup images either in the snapshot pool of the backup/recovery appliance or in OnVault Pools.

To issue API calls, the backup/recovery appliance needs to connect to the vCenter host with a username and password that have authority to perform the required actions. In this section, we add the vCenter as a host and supply those user credentials (which are stored securely by the service).

Use the following instructions to add a new vCenter host to the appliance management console:

  1. In the appliance management console, go to **Manage**.

  2. Click **Hosts**.

  3. Select **\+ Add host**.

  4. In the **Add host** form, enter the name and an optional friendly name. The name of a host should start with a letter, and can contain letters and digits (0-9). Underscore (`_`) characters aren't valid in host names.

  5. Enter the IP address of the vCenter server appliance in the **IP address** field.

  6. In the **Appliances** section, select the appliance management console managed appliances that you want to serve this host. If the list is long, you can use the search box to find a specific appliance or group of appliances.

  7. From the **Host type** drop-down, select **vCenter** and add the following information:

     * Validate the data transport mode, either NFS or SAN. NFS is the default setting and we recommend you don't change it.

     * Enter the username and password of the solution user you configured earlier to connect to the vCenter server appliance and then use the **Test** button to validate the added credentials.

  8. Click **Add**.




## Create a backup plan template

VMware Engine VMs are captured in their entirety using VMware Engine API calls. You manage a VM by assigning a template and a resource profile to it to define the backup plan to capture the entire VM.

When a backup/recovery appliance associates a backup template with an entire VM it isn't aware of VM content so no application-specific actions are performed.

When an entire virtual server is captured, a fully functional virtual server (operating system, applications, and their data) is captured. This enables the data to be accessed quickly and without issues. Since the image presented is a fully functional virtual server, it can be migrated to a new, permanent location if needed. Capturing whole virtual servers allows groups of virtual servers and their applications to be managed with a single backup template.

Templates are composed of backup policies. In policies, you can defines when to run a backup, how frequently to run a backup, how long to retain the backup image for (**Days** , **Weeks** , **Months** , or **Years**), and also additional configuration when the policy is applied to a VM. Refer to [Create a backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) to create a template and assign a [backup policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview).

A resource profile specifies the storage media for VMware VM data backup images. Resource profiles define which snapshot pool is used (if a snapshot policy is in the template) and which OnVault pools are used (if OnVault or direct to OnVault policies are in the template). For more information, see [Create a resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles).

## Apply a backup plan template

Use the onboarding wizard to discover VMware virtual machines (VMs) managed by a vCenter. Once you have discovered one or more applications, you can protect them all at once by applying a [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) and [profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles#create-profile) or you can add them to the applications list as unmanaged or ignored VMs.

Use the following instructions to discover and protect VMware VMs:

  1. From the Backup and DR appliance management console, click **App Manager**.

  2. Select **Applications** from the drop-down.

The **Applications** page opens.

  3. Click **Add Application**.

  4. Select **VMware Engine**.

  5. From the server list, select a vCenter where you want to perform VM discovery and click **Next**.

  6. On the **Manage** page, a list of VMs appears. Select a VM to discover and click **Next**.

  7. Apply the policy template and profile to the VMware Engine instance:

     * Select a VM that you want to protect.

     * Select **Manage backup configuration**.

     * From the **Choose action** drop-down list, select **Manage backup configuration**.

The **Choose** template drop-down list opens.

     * From the **Choose template** drop-down list, select a template.

The **Choose profile** drop-down list opens.

     * Click **Apply backup plan**.

  8. Click **Application Settings** for each VM in the list to make changes to the default configuration.

The **Application Details and Settings** page opens. See [Configure application settings for VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-vmware-vm).

  9. In case there are multiple VMs and you want to make the same changes to all the VMs, click define settings for all applications and make the necessary changes.

  10. Click **Next**.

  11. Review the summary screen. If everything is correct, select **Finish** to complete the onboarding process. The selected VMs are backed up based on the **Policy template** you select.

  12. After onboarding is complete, a dialog appears. Click **Finish** again. Once the policy template is attached to the selected VMs, the status changes to a green check mark. The green check indicates that your VMs is all set to run a backup job within the schedule by the policy. If you want to run the job immediately, see Run an on-demand backup.




## Run an on-demand backup

On-demand backup is a type of backup that you can manually trigger at any time. On-demand backups are useful for situations where you need to backup your data before a specific event. For example, you might want to backup your VM before applying updates or patches to be sure that you can restore it to its previous state if any issues arise during the update process.

Use the following instructions to run an on-demand backup of a managed application:

  1. From the Backup and DR appliance management console, click **App Manager**.

  2. Select **Applications** from the drop-down.

The **Applications** page opens.

  3. Select a VMware Engine instance and then click **Manage Backup Configuration**.

  4. From **Policies** , select **Snapshot**.

  5. Enter a **Label** and click **Run Now**. An on-demand backup will be triggered for the selected policy.




## Recover a Google Cloud VMware Engine VM

To recover a VMware Engine VM, you must have performed the mount for a VMware Engine VM. A VMware Engine VM mount operation can be performed using the following methods:

  * [Mount a VMware Engine VM to an existing host](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image#existing)

  * [Mount a VMware Engine VM as a new VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image#new)




Once the mount process is completed, you can [recover a mounted VMware VM to production storage](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image#recover_a_mounted_vmware_vm_to_production_storage).

## Restore a VMware Engine VM

Restore is the process of restoring data from a backup image. To restore a VM, see [Restore a VMware Engine VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm).

To clone a VM, see [Clone an image of a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-vm).

## Monitor VMware Engine

You can monitor the VMware Engine jobs using the appliance management console. To learn more about how to monitor VMware Engine jobs or events, see the Backup and DR documentation about how to [monitor jobs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs) or [events](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-events).

## What's next

To back up VMware Engine VM and database resource types, refer to the following quickstarts.

  * [Protect and recover a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-recovery).

  * [Protect and recover Microsoft SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/ms-sql-server-backup-recovery).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
