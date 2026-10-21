---
url: https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/gcve/attach-iscsi-volumes-to-gcve/
title: Attach iSCSI volumes to Google Cloud VMware Engine as VMFS datastores \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:38.575858+00:00
---

# Attach iSCSI volumes to Google Cloud VMware Engine as VMFS datastores  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/gcve/attach-iscsi-volumes-to-gcve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Attach iSCSI volumes to Google Cloud VMware Engine as VMFS datastores Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to attach iSCSI volumes from the NetApp Volumes Flex Unified storage pool to VMware Engine as virtual machine file system (VMFS) datastores.

To configure a NetApp Volumes iSCSI volume as a VMFS datastore on VMware Engine private cloud ESXi hosts, set up the iSCSI software adapter directly on each ESXi host.

## Configure a service subnet for iSCSI

Use the following instructions to configure a service subnet for iSCSI:

  1. Go to the **VMware Engine** page in the Google Cloud console.

[Go to VMware Engine](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Subnets**.

  3. Locate the free service subnet, and then click the **Edit** icon (edit) in the **Actions** column.

  4. In the **Edit subnet** panel, enter an IPv4 CIDR in the **IP address range** field.

  5. Click **Save**.

  6. Copy the following information from the service subnet:

     * **IP address range**

     * **Gateway IP**

     * **VLAN ID**




## Configure a distributed port group for iSCSI

This section describes how to configure a distributed port group for iSCSI.

### Before you begin

To create and manage a distributed port group for your private cloud, you must connect to your private cloud.

  1. Go to the **Private clouds** page in the Google Cloud console.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where the vCenter client is located.

  3. Click the private cloud you want to access.

  4. In the **Management appliances** section, click the URL for the vCenter server.

  5. To open the vSphere client, click **Launch** for the vSphere client type.

  6. When prompted, enter your solution user sign-in credentials. For more information about how to obtain solution user credentials, see [Elevate VMware Engine privileges](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege).




### Create a distributed port group

Use the following instructions to create a distributed port group:

  1. Connect to the VMware vCenter interface for the private cloud.

  2. Go to the **Network configuration** section of the vCenter interface.

  3. Right-click the **Datacenter-dvs** , and select **Distributed port group** > **New distributed port group**.

  4. In the **New distributed port group** window, complete the following steps:

     1. In the **Name and location** section, enter the name for distributed port group as **iscsi-pg** in the **Name** field, and then click **Next**.

     2. In the **Configure settings** section, complete the following steps:

        1. Enter the number of ports as **128** in the **Number of ports** field.

        2. Select **VLAN** in the **VLAN type** drop-down list.

        3. Enter the VLAN ID that you previously copied from the corresponding service subnet in the **VLAN ID** field.

        4. Select the **Customize default policies configuration** checkbox, and then click **Next**.

     3. Keep the **Security** settings at their default values, and then click **Next**.

     4. Keep the **Traffic shaping** settings at their default values, and then click **Next**.

     5. In the **Teaming and failover** section, complete the following steps:

        1. In the **Failover order** section, keep only one uplink and move any other uplinks listed in the **Active uplinks** section to the **Unused uplinks** section.

        2. Click **Next**.

     6. Keep the **Monitoring** settings at their default values, and then click **Next**.

     7. Keep the **Miscellaneous** settings at their default values, and then click **Next**.

     8. Click **Finish**.




## Configure a VMkernel adapter for iSCSI

Use the following instructions to configure a VMkernel adapter for iSCSI:

  1. Right-click the **iscsi-pg** port group.

  2. Click **Add VMkernel adapters**.

  3. In the **Add VMkernel adapters** window, complete the following steps:

     1. In the **Select hosts** section, click **Select all** to select all ESXi hosts in the private cloud, and then click **Next**.

     2. In the **Configure VMkernel adapter** section, complete the following steps:

        1. Set the **MTU** to **Custom** and enter **1500**.

        2. Keep other options at their default settings, and then click **Next**.

     3. In the **IPv4 Settings** section, select **Use Static IPv4 settings** option and complete the following steps:

        1. In the **Network Settings** section, enter the **IP address** and **subnet mask** for each ESXi host in the private cloud using the values from the previously defined service subnet.

        2. In the **Gateway** section, select **Configure on VMkernel adapters** as the **Configuration type**.

        3. Enter the gateway IP address for the service subnet in the **Gateway** field.

        4. Click **Next**.

     4. Review the details and click **Finish**.




## Configure the ESXi iSCSI software adapter

Complete the following steps to configure the iSCSI software adapter on each ESXi host in the private cloud using vCenter:

  1. Select the ESXi host in the private cloud.

  2. Go to **Configure** > **Storage** > **Storage Adapters**.

  3. If an iSCSI software adapter isn't present, complete the following steps:

     1. Click **Add software adapter**.

     2. Select **Add iSCSI adapter**.

  4. Select the iSCSI adapter typically named **vmhba64**.

  5. Click the **Network port binding** tab.

  6. Click **Add**.

  7. Select the **VMkernel adapter** corresponding to the **iscsi-pg** port group, and then click **OK**.

  8. Repeat the previous steps for each ESXi host in the private cloud.




## Create a host group

A [host group](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/host-groups/overview) is a regional collection of iSCSI initiator IQNs that you can authorize to access specific volumes.

### Before you begin

Before you create a host group, you need to obtain the iSCSI qualified name (IQN) for each client that you intend to include in the host group.

To obtain the IQN, complete the following steps:

  1. In vCenter, select the ESXi host.

  2. Go to **Configure** > **Storage** > **Storage Adapters**.

  3. Select the **iSCSI software adapter**.

  4. Copy the **iSCSI name**.




### Create a host group

[Create a host group](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/host-groups/create-host-group) and select ESXi for VMware Engine datastores as the OS type.

## Create an iSCSI volume

Create an iSCSI volume to use as a VMFS datastore. For instructions, see [Create a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume#create_a_volume). When you create the iSCSI volume, enable the **Block volume from deletion when clients are connected** restriction to prevent accidental deletion of the volume. You can enable this setting in the Google Cloud console.

NetApp Volumes lets you use two target portal paths per iSCSI volume. To improve resilience, use ESXi multipath on all VMware Engine ESXi hosts.

Copy the two IP addresses for the iSCSI volume.

## Discover iSCSI LUN on the VMware Engine private cloud ESXi hosts

Complete the following steps on each ESXi host in the private cloud using vCenter:

  1. Select the ESXi host in the private cloud.

  2. Go to **Configure** > **Storage** > **Storage Adapters**.

  3. Select the **iSCSI software adapter**.

  4. Click **Dynamic discovery**.

  5. Click **Add**.

  6. In the **Add send target server** dialog, enter the IP address of the iSCSI NetApp Volume in the **iSCSI server** field, and then click **OK**.

  7. Repeat the previous two steps for the second IP address of the iSCSI NetApp Volume.

  8. Click **Rescan adapter** to rescan the storage.

  9. Verify that the iSCSI volume is visible in the **Devices** section for the iSCSI adapter.




## Create an iSCSI VMFS datastore

Complete the following steps to create an iSCSI VMFS datastore:

  1. Connect to the VMware vCenter interface for the private cloud.

  2. Go to the **Host and clusters** section of the vCenter interface.

  3. Right-click the private cloud cluster name and select **Storage** > **New datastore**.

  4. In the **New datastore** window, complete the following steps:

     1. In the **Type** section, select the datastore type as **VMFS** , and then click **Next**.

     2. In the **Name and device selection** section, complete the following steps:

        1. Enter the name of the datastore in the **Name** field.

        2. Select an ESXi host in the **Select a host** drop-down list.

        3. Select the **NetApp iSCSI disk** detected, and then click **Next**.

     3. In the **VMFS version** section, select the VMFS version as **VMFS 6** or **VMFS 5** as required, and then click **Next**.

     4. Keep the **Partition configuration** settings at their default values, and then click **Next**.

     5. Click **Finish**.




After VMware Engine mounts the datastore, use vCenter to provision VMs on the external datastore.

## What's next

  * [Attach NFS volumes to Google Cloud VMware Engine as NFS datastores](https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/gcve/attach-nfs-volumes-to-gcve).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
