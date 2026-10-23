---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/host-groups/manage-host-group/
title: Manage host groups \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:09.274766+00:00
---

# Manage host groups  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/host-groups/manage-host-group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage host groups Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** NetApp Volumes offers block storage feature with iSCSI protocol for the Flex Unified service level.

This page describes how to manage your [host groups](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/host-groups/overview#about_host_groups).

## Edit a host group

This section provides details about which host group settings are editable and instructions for how to edit a host group.

### Editable settings

After a host group is created, you can modify its settings.

**Host details** : you can add or remove host initiators to the host groups after the host group creation. However, a host group must always have at least one host initiator; the initiator list can't be empty.

### Edit a host group

Use the following instructions to edit a host group using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Host groups** from the **External connections** menu.

  3. Click more_vert **Show more** icon on the host group and click **Edit**.

  4. In the **Host details** section, you can add or remove the host initiator information.

  5. Click **Save** to record your changes.




### gcloud

Edit a host group:
    
    
    gcloud netapp host-groups update HOST_GROUP_NAME \
      --location=LOCATION \
      --hosts=IQN1, IQN2

Replace the following information:

  * `HOST_GROUP_NAME`: the name for the host group.

  * `LOCATION`: the Google Cloud location (region) where the host group was created.

  * `IQN1, IQN2`: a comma-separated list of host identifiers (IQNs) to include in the host group.




## Delete a host group

This section provides details about how to delete a host group.

Use the following instructions to delete a host group using the Google Cloud console or Google Cloud CLI.

You can't delete a host group if volumes are attached to it. Before deleting the host group, make sure that the host group attachment has been removed from the volumes.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Host groups** from the **External connections** menu.

  3. Click more_vert **Show more** icon on the host group and click **Delete**.

  4. A confirmation dialog with information is displayed. Read through the warnings.

  5. Enter the name of the host group and click **Delete**.




### gcloud

Delete a host group:
    
    
    gcloud netapp host-groups delete HOST_GROUP_NAME \
      --location=LOCATION

Replace the following information:

  * `HOST_GROUP_NAME`: the name for the host group.

  * `LOCATION`: the Google Cloud location (region) where the host group was created.




## What's next

[Manage customer-managed encryption key policies](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/cmek-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
