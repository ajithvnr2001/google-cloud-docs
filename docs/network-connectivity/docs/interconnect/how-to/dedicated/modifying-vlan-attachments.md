---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-vlan-attachments/
title: Modify VLAN attachments \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:19.685152+00:00
---

# Modify VLAN attachments  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-vlan-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Modify VLAN attachments Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to modify Dedicated Interconnect VLAN attachments and their Border Gateway Protocol (BGP) sessions.

For more information about the terms used on this page and their definitions, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

The following table lists VLAN attachment and BGP session properties. It also provides information about how to modify them.

Property | How to modify  
---|---  
Description Capacity MTU | For details, see the next section Modify description, capacity, and MTU. Modifications are immediate and in rare cases, can cause traffic disruption. If traffic is disrupted, the disruption lasts less than a minute.  
Stack type |  You can change the stack type of an existing VLAN attachment to IPv4 only (single stack) or IPv4 and IPv6 (dual stack).  If you change the stack type of your VLAN attachment, your existing traffic might be rerouted or dropped. For more details, see Modify stack type.   
Whether a VLAN attachment is enabled or disabled | To disable or re-enable a VLAN attachment, see [Disable VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/disabling-vlans).  
VLAN ID BGP IP addresses (Cloud Router IP address, on-premises router IP address) | You can't modify these properties for existing attachments. Instead, you must recreate the VLAN attachment. To create VLAN attachments for Dedicated Interconnect, see [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments).  
Custom learned routes | Follow the steps in [Update an existing session to use custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes#add-routes-to-existing-session).   
MD5 authentication | Follow the steps in [Add authentication to an existing session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication#add-authentication).   
  
The peer ASN is not a property of the VLAN attachment—it is part of the BGP configuration of the Cloud Router. To modify the peer ASN, update the Cloud Router's BGP session for the VLAN attachment.

For more information, see the following resources:

  * [Viewing BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration)
  * [`gcloud compute routers update-bgp-peer` command reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer)
  * [`routers.update` API method reference](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/update)



## Modify description, capacity, and MTU

The section provides instructions for updating the description, capacity, and maximum transmission unit (MTU) of a VLAN attachment. Changing the attributes of a VLAN attachment, in rare cases, can cause traffic disruption. If traffic is disrupted, the disruption lasts less than a minute.

To make use of a 1460-, 1500-, or 8896-byte MTU, [the VPC network that uses the attachment must have the same MTU value](https://docs.cloud.google.com/vpc/docs/mtu). In addition, the on-premises virtual machine (VM) instances and routers must also have the same MTU value. If your network has the default MTU of `1460`, then select an MTU of `1460` for your VLAN attachment.

You cannot modify the MTU (`1440`) of an encrypted VLAN attachment that is used in an HA VPN over Cloud Interconnect deployment.

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the VLAN attachment to modify.

  3. On the attachment's detail page, click **Edit**.

  4. Modify your VLAN attachment:

     * **Description** : Information about the VLAN attachment.
     * **Capacity** : The maximum bandwidth of the attachment. If you modify the capacity of an encrypted VLAN attachment, you might need to add HA VPN tunnels to accommodate increased traffic. For more information, see [Configure HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect#tunnel-table).
     * **Maximum transmission unit (MTU)** : The MTU of the attachment.
  5. Click **Save**.




###  gcloud 

Modify an `interconnectAttachment` by specifying the name of the existing VLAN attachment and the attributes to modify:
    
    
    gcloud compute interconnects attachments dedicated update NAME \
        --region=REGION \
        --description=DESCRIPTION \
        --bandwidth=BANDWIDTH \
        --mtu=MTU
    

Replace the following:

  * `NAME`: the name of the existing VLAN attachment
  * `REGION`: the region of the attachment
  * `DESCRIPTION`: a description of the attachment
  * `BANDWIDTH`: the provisioned capacity of the attachment. If you modify the capacity of an encrypted VLAN attachment, you might need to add HA VPN tunnels to accommodate the increased traffic. For more information, see [Configure HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect#tunnel-table).
  * `MTU`: the MTU of the attachment



For more information, see the [`gcloud compute interconnects attachments dedicated update` reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update).

## Modify stack type

You can change the stack type of an existing VLAN attachment to IPv4 only (single stack) or IPv4 and IPv6 (dual stack). However, a VLAN attachment with both an IPv4 and an IPv6 BGP session can't be converted to the IPv4-only stack type without deleting its IPv6 BGP session.

To support IPv6 traffic over a Dedicated Interconnect connection, you must use a dual-stack VLAN attachment. With a dual-stack VLAN attachment, you can configure an IPv6 BGP session, or you can enable IPv6 route exchange in an IPv4 BGP session.

You can't modify the stack type of VLAN attachments that you create for HA VPN over Cloud Interconnect. Encrypted VLAN attachments only support the IPv4 only (single stack) stack type.

With a dual-stack VLAN attachment, you can also configure an IPv4 BGP session and an IPv6 BGP session that run in parallel. For more information, see [Parallel IPv4 and IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp#parallel-ipv4-ipv6).

### Modification impact on IPv4 and IPv6 traffic

The following table describes how the stack type configuration of the VLAN attachment combined with the BGP session configuration affects IPv4 and IPv6 traffic.

Original stack type of VLAN attachment | Modified stack type of VLAN attachment | BGP session | MP-BGP configuration | Impact on traffic  
---|---|---|---|---  
IPv4 and IPv6 (dual stack) | IPv4 only | IPv4 BGP | IPv6 disabled  | No IPv6 traffic supported; only IPv4 traffic. This is the default state for Dedicated Interconnect and Cloud Router.   
IPv4 and IPv6 (dual stack) | IPv4 only | IPv4 BGP | IPv6 enabled |  No IPv6 traffic supported. Because the VLAN attachment is configured as IPv4 only, Cloud Router automatically disables IPv6 route exchange for the BGP session.  However, if the VLAN attachment previously had IPv6 route exchange enabled for the IPv4 BGP session, then Google Cloud might retain IPv6 BGP addresses for the VLAN attachment. Google Cloud can reuse these addresses if IPv6 route exchange is later re-enabled for the VLAN attachment.   
IPv4 only | IPv4 and IPv6 (dual stack) | IPv4 BGP | IPv6 enabled | Both IPv4 and IPv6 traffic are supported. This is the supported configuration for an IPv4 BGP session that uses MP-BGP and exchanges IPv6 routes in Dedicated Interconnect.  
IPv4 and IPv6 (dual stack) | IPv4 only | IPv6 BGP | IPv4 enabled or disabled |  Dual-stack VLAN attachments with an IPv6 BGP session can't be changed to an IPv4 only stack type. To change the stack type to IPv4 only, first delete the IPv6 BGP session.  **Note:** Changing the stack type to IPv4 only in the Google Cloud console automatically deletes the IPv6 BGP session in addition to changing the stack type.   
IPv4 and IPv6 (dual stack) | IPv4 only | Both IPv4 BGP and IPv6 BGP | Not applicable |  Dual-stack VLAN attachments with an IPv6 BGP session can't be changed to an IPv4 only stack type. To change the stack type to IPv4 only, first delete the IPv6 BGP session.  **Note:** Changing the stack type to IPv4 only in the Google Cloud console automatically deletes the IPv6 BGP session in addition to changing the stack type.   
  
### Disable IPv6 traffic

You can temporarily disable IPv6 traffic in your Dedicated Interconnect VLAN attachment for troubleshooting.

Disabling your IPv6 BGP session or disabling IPv6 route exchange in the IPv4 BGP session is less disruptive to your Cloud Interconnect configuration than changing the stack type of your VLAN attachment.

If you are using an IPv6 BGP session, you can disable your entire BGP session instead of switching the stack type of the VLAN attachment. For information about how to disable a BGP session, see [Disable or remove BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp).

To disable IPv6 traffic temporarily in an IPv4 BGP session, you can disable IPv6 route exchange in the IPv4 BGP session. For information about how to disable IPv6 route exchange in an IPv4 BGP session, see [Configure multiprotocol BGP for IPv4 or IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp).

### Change VLAN attachment stack type

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the VLAN attachment to modify.

  3. On the attachment's detail page, click **Edit**.

  4. Modify the stack type of the VLAN attachment by selecting **IPv4 (single stack)** or **IPv4 and IPv6 (dual stack)**.

If you are modifying an IPv4-only VLAN attachment to use IPv4 and IPv6 (dual stack), you can complete the configuration by choosing one of the following configurations:

     * Enable IPv6 route exchange in your IPv4 BGP session. For more information, see [Configure multiprotocol BGP for IPv4 or IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp).

     * Configure an IPv6 BGP session. See the instructions in [Create a VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#create_unencrypted_vlan_attachments).

  5. (Optional): You can specify custom IP address ranges when you change your attachment's stack type.

For more information about prerequisites, limitations and why you might use custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).

In the **Allocate BGP IPv6 addresses** section, enter the following information:

     * In the **Cloud Router IPv6** field, enter the IPv6 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `2001:db8::1/125`.
     * In the **Peer IP** field, enter the IPv6 CIDR address that you want to assign to the customer router end of your VLAN attachment.
**Important:** A VLAN attachment with both an IPv4 and an IPv6 BGP session can't be converted to the IPv4-only stack type without deleting its IPv6 BGP session.
  6. Click **Save and continue**.




###  gcloud 

**Change VLAN attachment stack type from IPv4 (single stack) to IPv4 and IPv6 (dual stack)**

  1. Modify a VLAN attachment by specifying the name of the existing attachment and the attributes to modify:
         
         gcloud compute interconnects attachments dedicated update ATTACHMENT_NAME \
             --stack-type=IPV4_IPV6
         

Replace `ATTACHMENT_NAME` with the name of your VLAN attachment.

  2. Complete the configuration by choosing one of the following configurations:

     * Enable IPv6 route exchange in your IPv4 BGP session. For more information, see [Configure multiprotocol BGP for IPv4 or IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp).

     * Configure an IPv6 BGP session. See the instructions in [Create a VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#create_unencrypted_vlan_attachments).

  3. Optional: When you update your stack type from IPv4 only to dual stack, you can provide custom IPv6 address ranges by using the `--candidate-cloud-router-ipv6-address` and `--candidate-customer-router-ipv6-address` flags.
         
         gcloud compute interconnects attachments dedicated update ATTACHMENT_NAME \
             --project=PROJECT_ID \
             --region=REGION \
             --router=ROUTER_NAME \
             --stack-type=IPV4_IPV6 \
             --candidate-cloud-router-ipv6-address=CANDIDATE_CLOUD_ROUTER_IP_ADDRESS \
             --candidate-customer-router-ipv6-address=CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS
         




Replace the following:

  * `CANDIDATE_CLOUD_ROUTER_IP_ADDRESS`: the IPv6 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment; for example, `2001:db8::1/125`
  * `CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS`: the IPv6 CIDR address that you want to assign to the customer router end of your VLAN attachment



**Change VLAN attachment stack type to IPv4 (single stack)**

If the VLAN attachment has an IPv6 BGP session, do the following:

  1. Delete the IPv6 BGP peer from Cloud Router:
         
         gcloud compute routers remove-bgp-peer ROUTER_NAME \
             --peer-name=BGP_PEER_NAME \
             --region=REGION
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router
     * `BGP_PEER_NAME`: the name of the IPv6 BGP peer
     * `REGION`: the region in which your Cloud Router is located
  2. Delete the IPv6 interface from Cloud Router:
         
         gcloud compute routers remove-interface ROUTER_NAME \
             --interface-name=INTERFACE_NAME \
             --region=REGION
         

Replace `INTERFACE_NAME` with the name of the IPv6 Cloud Router interface.

  3. Update the Cloud Interconnect VLAN attachment:
         
         gcloud compute interconnects attachments dedicated update ATTACHMENT_NAME \
             --stack-type=IPV4_ONLY \
             --region=REGION
         

Replace `ATTACHMENT_NAME` with the name of your Cloud Interconnect VLAN attachment.




## What's next

  * To configure your on-premises router for IPv4 and IPv6 (dual stack) traffic, see [Configure on-premises routers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers#set-up-third-party-routers-for-ipv4-and-ipv6-traffic).

  * To create a Dedicated Interconnect connection, see the [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
