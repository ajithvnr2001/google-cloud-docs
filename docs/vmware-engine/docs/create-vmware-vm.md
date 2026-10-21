---
url: https://docs.cloud.google.com/vmware-engine/docs/create-vmware-vm/
title: Quickstart: Create a VMware VM \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:52.188347+00:00
---

# Quickstart: Create a VMware VM  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/create-vmware-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a VMware VM

This page explains how to create and manage virtual machines (VMs) and policies in your private cloud by using the vSphere client.

## Before you begin

To create and manage VMs on your private cloud using the vSphere client, you must first be able to connect to your private cloud. This quickstart assumes that you have done the following:

  1. Created a Google Cloud VMware Engine private cloud. You can create one by completing the following quickstart: [Creating your first private cloud](https://docs.cloud.google.com/vmware-engine/docs/create-private-cloud).
  2. Established a secure connection from your on-premises network to the private cloud using one of the following options:

     * [Connect an on-premises network to a VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises)
     * [Connect using a point-to-site VPN connection](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpn-gateways)
  3. Created a subnet on your private cloud. You can create one by completing the following quickstart: [Creating your first subnet](https://docs.cloud.google.com/vmware-engine/docs/quickstart-network-segment).




## Access the vCenter client from the Google Cloud console

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where the vCenter client is located.

  3. Click the private cloud you want to access.

  4. Under **Management Appliances** , click the URL for the vCenter server.

  5. To open the vSphere client, click the **Launch** button for the vSphere client type. For ISO upload, use the vSphere HTML5 client.

  6. When prompted, enter your sign-in credentials. As a reminder, you can [retrieve generated credentials](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client#sign-in) from the private cloud details page.


**Note:** Using the Flex client for ISO or vSphere template uploads can result in an error.

## Upload an ISO or vSphere template

Provide installation media for your VM by uploading an ISO file or a vSphere template:

  1. Obtain the ISO or vSphere template that you want to upload to vCenter to create a VM and have it available on your local system.
  2. In vCenter, click the **Storage** icon and select **vsanDatastore**. Click **Files > New Folder**.
  3. Create a folder called _ISOs and templates_.
  4. In your new folder, click **Upload files**.
  5. Follow the on-screen instructions to upload the ISO.



## Create a VM in the vCenter client

Create your new VM in vCenter, and attach it to a workload network segment:

  1. In vCenter, click the **Hosts and clusters** icon.
  2. Right-click **Workload** and select **New virtual machine**.
  3. Select **Create new virtual machine** and click **Next**.
  4. Name the machine, select the **Workload VM** 's location, and click **Next**.
  5. Select the **Workload** compute resource and click **Next**.
  6. Select **vsanDatastore** and click **Next**.
  7. Keep the default ESXi compatibility selection and click **Next**.
  8. Select the guest OS of the ISO for the VM that you are creating and click **Next**.
  9. Select hard disk and network options.
  10. Under **New CD/DVD Drive** , select **Datastore ISO file**.
  11. Select the workload network segment that you created in NSX. This must not be the VMware Engine management appliances subnet.
  12. A selection window opens. Select the file you previously uploaded to the **ISOs and templates** folder and click **OK**.
  13. Review the settings and click **OK** to create the VM.



The VM is added to the workload compute resources and is ready for use. The basic setup is now complete. You can power on your VM and install the operating system. You can start using your private cloud similar to how you would use your on-premises VM infrastructure.

The following sections contain optional information about setting up DNS and DHCP servers for private cloud workloads and modifying the default networking configuration.

## Configure other tools and products (optional)

You can further expand the capabilities of your private cloud environment by installing and configuring other tools and products such as [VMware Site Recovery Manager (SRM)](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-srm). By doing so, you gain access to other methods of disaster recovery, replication, or other functions to protect your VM.

Some tools and products used with your private cloud might require a user to have administrative privileges in vSphere. In those cases, use one of the [solution user accounts](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-solution-user-accounts) provided for you in your private cloud.

## What's next

  * Learn how to set up [VPN gateways](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpn-gateways) on the VMware Engine network.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
