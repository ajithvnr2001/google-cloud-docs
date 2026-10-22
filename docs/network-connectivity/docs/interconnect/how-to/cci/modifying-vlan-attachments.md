---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/modifying-vlan-attachments/
title: Modify VLAN attachments \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:25.346374+00:00
---

# Modify VLAN attachments  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/modifying-vlan-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Modify VLAN attachments Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to modify VLAN attachments and Border Gateway Protocol (BGP) sessions for Cross-Cloud Interconnect.

**Note:** For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

The following table describes properties of VLAN attachments and their BGP sessions, along with information about how to modify them.

Property | How to modify  
---|---  
Description Capacity MTU | For details, see the next section Modifying description, capacity, and MTU. Modifications are immediate and in rare cases, can cause traffic disruption. If traffic is disrupted, the disruption lasts less than a minute.  
Whether a VLAN attachment is enabled or disabled | To disable or re-enable a VLAN attachment, see [Disable VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/disabling-vlans).  
VLAN ID BGP IP addresses (Cloud Router IP address, remote cloud router IP address) | You can't modify these properties for existing attachments. Instead, you must re-create the VLAN attachment.  
MD5 authentication | Update the BGP session by following the steps in [Add authentication to an existing session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication#add-authentication).   
Peer ASN | Update the BGP session by using the following resources:

  * [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration)
  * The [`glcoud compute routers update-bgp-peer` command reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer)
  * The [`routers.update` API method reference](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/update)

  
  
## Modify description, capacity, and MTU

The section provides instructions for updating the description, capacity, and maximum transmission unit (MTU) of a VLAN attachment. Changing the attributes of a VLAN attachment, in rare cases, can cause traffic disruption. If traffic is disrupted, the disruption typically lasts less than a minute.

To make use of the 1500-byte MTU, the VPC network that uses the attachment must have an [MTU](https://docs.cloud.google.com/vpc/docs/mtu) set to `1500`. In addition, the remote cloud resources must have an MTU set to`1500`. If your network has the default MTU of `1460`, leave the field at `1440`.

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the VLAN attachment to modify.

  3. On the attachment's detail page, click **Edit**.

  4. Modify your VLAN attachment:

     * **Description** : Information about the VLAN attachment.
     * **Capacity** : The maximum bandwidth of the attachment.
     * **Maximum transmission unit (MTU)** : The MTU of the attachment.
  5. Click **Save**.




###  gcloud 

Use the [`gcloud compute interconnects attachments dedicated update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update):
    
    
    gcloud compute interconnects attachments dedicated update NAME \
        --region=REGION \
        --description=DESCRIPTION \
        --bandwidth=BANDWIDTH \
        --mtu MTU
    

Replace the following:

  * `NAME`: the name of the VLAN attachment
  * `REGION`: the region of the attachment
  * `DESCRIPTION`: a description of the attachment
  * `BANDWIDTH`: the provisioned capacity of the attachment
  * `MTU`: the MTU of the attachment



## What's next

  * To learn more about Cross-Cloud Interconnect, see the [Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#cci).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
