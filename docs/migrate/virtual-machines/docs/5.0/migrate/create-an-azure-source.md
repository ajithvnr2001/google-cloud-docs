---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-an-azure-source/
title: Create an Azure source \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:08.143712+00:00
---

# Create an Azure source  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-an-azure-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Create an Azure source Stay organized with collections  Save and categorize content based on your preferences. 

[Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines) lets you migrate your Azure virtual machines (VMs) from your Azure account to Compute Engine instances.

## Prerequisites

  * [Enable the **VM Migration API**](https://console.cloud.google.com/apis/library/vmmigration.googleapis.com) on your host project.
  * Review the [supported operating systems](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions) that support migrating VMs from an Azure source.
  * Review [Migrating VMs with Migrate to Virtual Machines: Getting started](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/migrating-vms-migrate-for-compute-engine-getting-started) documentation. This document provides insight into the overall structure of Migrate to Virtual Machines, including important concepts and reference information that helps you migrate your workload efficiently and effectively.



## Migration limitations from Azure

Migrate to Virtual Machines does not support migration of VMs with the following attributes:

  * Ephemeral OS disks
  * Non-managed disks



Attempting a migration of a VM with such disks will fail with an appropriate error message.

Also note that due to their nature - temporary disks data is not guaranteed to be migrated with the VM and won't persist following the creation of a clone VM or a cutover VM.

## Migrate your workload from an Azure source

Before initiating your migration with Azure as a source, set up your Azure environment by completing the following tasks:

  1. Register your app in the Azure portal.
  2. Create a custom role to be accessed by the Migrate to Virtual Machines service.
  3. Assign the custom role to an app.
  4. Create an Azure source using Google Cloud.



### Register your app

To register your app, follow these steps:

  1. In the Azure portal, go to the **App Registration** page, and click **New registration**.
  2. To add new client credentials, click **Add a certificate or secret**.
  3. To add a new client secret, click **\+ New client secret** and enter a description and expiry date for the client secret.
  4. Click **Add**.



Your client secret is now ready. Make sure to copy your client secret value. You will need it later when you set up the source.

### Create a custom role

To migrate your Azure workload, [create a custom role](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles) and assign it to the app you registered in the Register your app step.

To create a custom role, use the following steps:

  1. In the Azure portal, go to the [Subscriptions](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBlade) page and select your Azure subscription.
  2. Copy the **Subscription ID** by clicking on it.
  3. Save following JSON template and replace `SUBSCRIPTION_ID` with the **Subscription ID** you copied in Step 2:
         
         {
           "properties": {
                 "roleName": "Minimum M2VM permissions role",
                 "description": "This role contains the bare minimum of Azure IAM permissions to support M2VM flow",
                 "assignableScopes": [
                       "/subscriptions/SUBSCRIPTION_ID"
                 ],
           "permissions": [
                       {
                       "actions": [
                             "Microsoft.Resources/subscriptions/resourceGroups/write",
                             "Microsoft.Resources/subscriptions/resourceGroups/read",
                             "Microsoft.Resources/subscriptions/resourceGroups/delete",
                             "Microsoft.Compute/virtualMachines/read",
                             "Microsoft.Compute/virtualMachines/write",
                             "Microsoft.Compute/virtualMachines/deallocate/action",
                             "Microsoft.Compute/disks/read",
                             "Microsoft.Compute/snapshots/delete",
                             "Microsoft.Compute/snapshots/write",
                             "Microsoft.Compute/snapshots/beginGetAccess/action",
                             "Microsoft.Compute/snapshots/read",
                             "Microsoft.Compute/snapshots/endGetAccess/action"
                       ],
                       "notActions": [],
                       "dataActions": [],
                       "notDataActions": []
                       }
                 ]
           }
           }
           

For more information about the permission details, see [permission details](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/roles-reference#permissions_to_configure_azure_as_a_source).

  4. In the Azure portal, go to the **Access control (IAM)** page.

  5. To add a custom role, click **\+ Add**.

  6. Click **Start from JSON** and then click **Select file** to upload the JSON file you created in Step 3.

  7. To review your inputs click **Review + Create** , and then to create the custom role click **Create**.




### Assign the custom role to an app

To assign a custom role to an app, follow these steps:

  1. In the Azure portal, go to the **Access control (IAM)** page.
  2. Click **\+ Add** and then click **Add role assignment**.
  3. Search for the custom role you created in Create a custom role by typing `m2vm`, and select it.
  4. Click **Next**.
  5. Click **\+ Select members** and search for the app name you registered in Register your app and click **Select**.
  6. To review and assign the custom role to your app, click **Review + Assign**.



### Create an Azure source

After you have registered your app, added your secret, and set its permissions, create an Azure source in the Migrate to Virtual Machines service.

To create an Azure source, follow these steps:

  1. In the Google Cloud console, go to the [Migrate to Virtual Machines](https://console.cloud.google.com/compute/mfce/dashboard) page.
  2. Select the **Sources** tab.
  3. From the **Add source** list, select **\+ Add Azure source**.
  4. Enter your source details on the **Create Azure source** panel.

**Caution:** You cannot edit the **GCP region** or **Azure location** fields after creating your source. If you need to edit these fields, we recommend that you wait 24 hours before revoking the credentials you replaced in order to not interrupt an ongoing replication cycle.

The following table describes the parameters for Azure source details.

**Parameter** |  **Description**  
---|---  
**Name (mandatory)** |  A string that identifies the source. The string must conform to [Compute Engine naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). You cannot update this field after creating your source.  
**Google Cloud region (mandatory)** |  The region in Google Cloud that you want to migrate your instances to. You cannot update this field after creating your source.  
  
For more information, see [locations](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/locations) documentation.  
**Azure location (mandatory)** |  The region in Azure (for example, **centralus**) from which you want to migrate VMs. The inventory displayed in the Migrate to Virtual Machines console only includes VMs from this Azure location. You cannot update this field after creating your source.  
  
Note: It is recommended that you choose the _region_ from the drop-down list options, or copy the _region_ from your Azure console **JSON View** and paste it into the source detail field to avoid typos. If there is a typo in the _region_ , the source doesn't become active, and you have to create a new source. You can see the status of the source in the console.  
**Subscription ID (mandatory)** |  Part of the user credentials. You cannot update this field after creating your source.  
**Client ID (mandatory)** |  Part of the user credentials.  
**Tenant ID (mandatory)** |  Part of the user credentials. You cannot update this field after creating your source.  
**Client Secret (mandatory)** |  This is the value which you saved when you created the client secret.  
  
**Note:** You cannot retrieve this value from the Azure portal or the Google Cloud console once it is set. You can update this value with a new secret in case you update the credentials.  
**Customer managed encryption key** | The key you want to use to protect your data in Google Cloud. By default, Google Cloud automatically [ encrypts data when it is at rest](https://docs.cloud.google.com/security/encryption-at-rest/default-encryption) using encryption keys managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use [ customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) to encrypt and decrypt your data at rest. These encryption keys are created, managed, and owned by you.   
  
**Note:** The encryption key that you set will be used for all the resources created under this source.   
**Optional: User tags for migration resource** |  The Migrate to Virtual Machines service creates snapshots of your VM disks to migrate them to Google Cloud.   
If you would like to have a custom tag associated with these resources, specify them here. This can help you identify all resources created by Migrate to Virtual Machines in your Azure environment. Snapshots also already have tags as detailed in [Snapshots](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#snapshots_created_when_migrating_a_workload).   
  
All snapshots are automatically created under one resource group when the source is created. The resource group name can be seen on the **Source Details** page.   
  5. Click **Create**. A notice detailing your new source appears.

  6. Wait (up to 15 minutes but usually less) until the **Source status** is indicated as **Active**.




Check your inventory to verify that there are instances that correspond to the tags (and/or security groups) that you specified when you created your source.

As part of source creation, your project is automatically added as a target project.

#### Cloud sources limitations

You can host a maximum of 15 cloud sources (AWS sources, Azure sources, or both the sources combined) on a host project at a time. For example, you can host 10 AWS sources and 5 Azure sources on a host project at a time. Conversely, you can host 7 AWS sources and 8 Azure sources on a host project at a time. If you want to add a new cloud source to a project that already hosts 15 cloud sources, you must delete an existing source, and then add the new source. You can also try using a different project to host the new cloud source if you don't want to delete any existing sources.

### Next steps: Start your migration

After you've created an Azure source, you are ready to start your migration. The rest of the process for migrating your workload from an Azure source matches the process for other sources for Migrate to Virtual Machines.

For details on how to start your migration process, see [Migrating individual VMs](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms).

## Differences from using VMware as a source

There are several unique aspects about using Azure as a source for your migrations:

  * You can create and edit an Azure source from the UI.
  * There is no utilization report for an Azure source.



## Differences from using AWS as a source

The usage is almost identical to the usage of AWS as a source.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
