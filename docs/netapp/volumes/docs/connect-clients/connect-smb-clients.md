---
url: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-smb-clients/
title: Connect SMB clients \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:08.387462+00:00
---

# Connect SMB clients  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-smb-clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Connect SMB clients Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to connect SMB clients.

## Before you begin

Before you begin, make sure your client is logged in as a valid domain user.

## Connect SMB clients

Use the following instructions to connect SMB clients using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click more_vert **Show more**.

  4. Click **Mount instructions**.

  5. Follow the mount instructions shown in the Google Cloud console.

  6. Click **Finish**.




### gcloud

Run the following command:
    
    
    gcloud netapp volumes describe VOLUME_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --format="value(mountOptions.instructions)"

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.




For more information about additional optional flags, see [Google Cloud SDK documentation on volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes).

### ONTAP-mode

Use the following steps to identify your volume's hostname or IP address, and share name:

  1. Look up the [computer account name](https://docs.netapp.com/us-en/ontap-cli//vserver-active-directory-show.html#description) you used when you created the SMB server. When joining the domain, ONTAP registers this name with Active Directory DNS using secure DDNS updates. For large capacity volumes, ONTAP registers all IP addresses for that hostname.

  2. Find the IP addresses of the share by looking up [all network interfaces](https://docs.netapp.com/us-en/ontap-cli//network-interface-show.html#description) for the `data_cifs` service.

  3. Look up the [share name](https://docs.netapp.com/us-en/ontap-cli//vserver-cifs-share-show.html#description) assigned to your volume.

  4. Connect your client to `\\<var>HOSTNAME</var>\<var>SHARENAME</var>`.

  5. If you use IP addresses instead of the hostname, make sure your Active Directory has the appropriate Kerberos service principal names (SPN) created for those IP addresses.




After you identify the required commands, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

## Firewall rules for SMB volumes access

SMB uses various ports to communicate between the client and a server. For communication between Google Compute Engine and NetApp Volumes, these ports aren't blocked by default. If you use a firewall, you must enable access to the following ports for the full [NetApp Volume PSA CIDR](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking#configure_private_services_access) or the following individual volume IP addresses:

  * `445 TCP SMB2/3`

  * `135 TCP msrpc` and `40001 TCP SMB CA`: Used only for SMB 3.x continuously available shares. These ports aren't required for non-continuously available shares.




The service exposes, but doesn't use, port `139/TCP`.

The IP addresses for NetApp Volumes are automatically assigned from the CIDR range you assigned to the service during network peering. For more information, see [Choose a CIDR](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking#configure_private_services_access).

Your SMB clients don't need to expose ingress ports for SMB to work.

## What's next

Connect [NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
