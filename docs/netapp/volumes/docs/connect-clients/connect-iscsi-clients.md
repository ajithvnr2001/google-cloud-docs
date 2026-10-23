---
url: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-iscsi-clients/
title: Connect iSCSI clients \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:26.539288+00:00
---

# Connect iSCSI clients  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-iscsi-clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Connect iSCSI clients Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** NetApp Volumes provides block storage with iSCSI and NVMe/TCP protocols for the Flex Unified service level.

This page provides instructions about how to connect iSCSI clients.

Use the following instructions to attach NetApp Volumes to iSCSI clients using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click more_vert **Show more** icon on the volume.

  4. Click **Mount instructions**.

  5. Follow the mount instructions shown in the Google Cloud console.

  6. Click **Finish**.




### gcloud

Connect iSCSI clients:
    
    
    gcloud netapp volumes describe VOLUME_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --format="value(mountOptions.instructions)"

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.




For more information about additional optional flags, see [Google Cloud SDK documentation on volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/describe).

## Firewall rules for iSCSI volumes access

For iSCSI access, NetApp Volumes uses specific network ports to enable communication between initiators (clients) and targets (storage volumes). For communication between Google Compute Engine and NetApp Volumes, these ports aren't blocked by default. If you use a firewall, you must enable access to the following ports for the full [NetApp Volume PSA CIDR](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking#configure_private_services_access) or the individual volume IP addresses:

  * `3260 TCP iSCSI` target port



The IP addresses for NetApp Volumes are automatically assigned from the CIDR range you assigned to the service during network peering. For more information, see [Choose a CIDR](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking#configure_private_services_access).

## What's next

  * [Protect your data](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/protect-your-data).

  * [Connect NVMe/TCP clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nvme-tcp-clients).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
