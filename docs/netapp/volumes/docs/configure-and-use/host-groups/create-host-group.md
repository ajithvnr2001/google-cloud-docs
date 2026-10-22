---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/host-groups/create-host-group/
title: Create a host group \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:23.565980+00:00
---

# Create a host group  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/host-groups/create-host-group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a host group Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** NetApp Volumes offers block storage feature with iSCSI protocol for the Flex Unified service level.

This page describes how to create a [host group](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/host-groups/overview#about_host_groups).

## Before you begin

Before you create a host group, you need to obtain the iSCSI qualified name (IQN) for each client you intend to include in the host group.

To obtain the IQN from a Linux iSCSI client, do the following:

  1. Access your Linux machine using SSH.

  2. Find the IQN.
         
         sudo cat /etc/iscsi/initiatorname.iscsi
         

  3. Note the value displayed after **InitiatorName=**. For example, **iqn.1994-05.com.redhat:client1**.




To obtain the IQN from a Windows iSCSI client:

  1. Open **iSCSI Initiator** from the **Start** menu.

  2. Navigate to the **Configuration** tab.

  3. Note the value in the **Initiator Name** field. For example, **iqn.1991-05.com.microsoft:client1**.




## Create a host group

Use the following instructions to create a host group using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Host groups** from the **External connections** menu.

  3. Click **Create**.

  4. In the **Host group details** section, complete the following steps:

     1. Enter a name for the host group in the **Host group name** field. The name must be unique for each location.

     2. Optional: enter a description for the host group in the **Description** field.

  5. In the **Location** section, select the **Region** from the drop-down list.

  6. In the **Configuration** section, select the **Operating system** type that corresponds to your iSCSI client.

  7. Optional: in the **Labels** section, click **Add label** to enter relevant labels for reporting and querying purposes.

  8. Click **Continue**.

  9. In the **Host details** section, enter the iSCSI qualified name (IQN) of the host accessing the volume in the **Initiator 1** field.

  10. Click **Add initiator** to specify additional IQNs.

  11. Click **Create**.




### gcloud

To create a host group:
    
    
    gcloud netapp host-groups create HOST_GROUP_NAME \
      --location=LOCATION \
      --type=ISCSI_INITIATOR \
      --hosts=HOSTS \
      --os-type=OS_TYPE \
      --description=DESCRIPTION

Replace the following information:

  * `HOST_GROUP_NAME`: the name for the host group.

  * `LOCATION`: the Google Cloud location (region) for the host group creation.

  * `HOSTS`: a comma-separated list of host identifiers (IQNs) to include in the host group.

  * `OS_TYPE`: the operating system of the hosts. The supported values include `LINUX`, `WINDOWS`, and `ESXI`.

  * `DESCRIPTION`: Optional: a description for the host group.




## What's next

[Manage host groups](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/host-groups/manage-host-group).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
