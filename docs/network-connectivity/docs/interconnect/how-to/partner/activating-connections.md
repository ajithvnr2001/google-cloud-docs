---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections/
title: Activate connections \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:05.204731+00:00
---

# Activate connections  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Activate connections Stay organized with collections  Save and categorize content based on your preferences. 

After your [service provider](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/service-providers) configures your VLAN attachment for a Partner Interconnect connection, you must activate it before the attachment can start passing traffic. Activating a VLAN attachment lets you check that you're connecting with an expected service provider before the attachment starts passing traffic. It also enables you to control when the attachment starts passing traffic.

If you [pre-activate](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#pre-activate) your VLAN attachment, the attachment is automatically activated after it's configured.

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To help you solve common issues that you might encounter when using Partner Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#partner).

To activate your VLAN attachment, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the VLAN attachment to view its details page.

  3. If the status of your attachment is `Waiting for service provider`, wait until your service provider has completed the VLAN configuration.

**Note** : If your encrypted VLAN attachment remains in the `PENDING_PARTNER` or `Waiting for service provider` state for an extended period of time, contact your service provider for assistance.
  4. Review the **Interconnect** information to check that the expected service provider configured the VLAN attachment.

If an unexpected third party pairs with your VLAN attachment, [delete the VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/delete-vlan-attachments) and then create a new one, which generates a new pairing key. Use the new pairing key to request another connection from your service provider.

**Note:** The **VLAN ID** for the connection is for the Google Cloud side of the connection. To configure your on-premises router for Layer 2 connections, use the VLAN ID provided by your service provider.
  5. Click **Activate**.




###  gcloud 

  1. Describe the VLAN attachment to view its details; the state of the attachment must be `PENDING_CUSTOMER` before you can activate it:
         
         gcloud compute interconnects attachments describe ATTACHMENT_NAME \
             --region=REGION
         

Replace the following:

     * `ATTACHMENT_NAME`: the name of your VLAN attachment

     * `REGION`: the region that your VLAN attachment is located in

The output is similar to the following for IPv4 VLAN attachments:
    
    adminEnabled: false
    edgeAvailabilityDomain: AVAILABILITY_DOMAIN_1
    bandwidth: BPS_1G
    cloudRouterIpAddress: 169.254.67.201/29
    creationTimestamp: '2017-12-01T08:29:09.886-08:00'
    customerRouterIpAddress: 169.254.67.202/29
    id: '7976913826166357434'
    kind: compute#interconnectAttachment
    labelFingerprint: 42WmSpB8rSM=
    name: ATTACHMENT_NAME
    pairingKey: 7e51371e-72a3-40b5-b844-2e3efefaee59/REGION/2
    partnerMetadata:
      interconnectName: New York (2)
      partnerName: My Service Provider Inc
      portalUrl: https://service-provider-portal.com
    region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION
    router: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION/routers/my-router
    selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION/interconnectAttachments/my-attachment
    stackType: IPV4_ONLY
    state: PENDING_CUSTOMER
    type: PARTNER
    vlanTag8021q: 1000
    

The output is similar to the following for IPv4 and IPv6 (dual stack) VLAN attachments:
    
    adminEnabled: false
    edgeAvailabilityDomain: AVAILABILITY_DOMAIN_1
    bandwidth: BPS_1G
    cloudRouterIpAddress: 169.254.67.201/29
    cloudRouterIpv6Address: 2600:2d00:0:1::1/125
    creationTimestamp: '2017-12-01T08:31:11.580-08:00'
    customerRouterIpAddress: 169.254.67.202/29
    customerRouterIpv6Address: 2600:2d00:0:1::2/125
    description: Interconnect for Customer 1
    id: '7193021941765913888'
    interconnect: https://www.googleapis.com/compute/alpha/projects/partner-project/global/interconnects/lga-2
    kind: compute#interconnectAttachment
    labelFingerprint: 42WmSpB8rSM=
    name: ATTACHMENT_NAME
    partnerMetadata:
      interconnectName: New York (2)
      partnerName: Partner Inc
      portalUrl: https://partner-portal.com
    region: https://www.googleapis.com/compute/alpha/projects/partner-project/regions/REGION
    selfLink: https://www.googleapis.com/compute/alpha/projects/partner-project/regions/REGION/interconnectAttachments/customer-attachment
    stackType: IPV4_IPV6
    state: PENDING_CUSTOMER
    type: PARTNER
    vlanTag8021q: 1000
    

If your service provider configured your VLAN attachment, the state of your attachment changes from `PENDING_PARTNER` to `PENDING_CUSTOMER`. If the state is still `PENDING_PARTNER`, wait until your service provider has completed the VLAN configuration.

**Note** : If your encrypted VLAN attachment remains in the `PENDING_PARTNER` or `Waiting for service provider` state for an extended period of time, contact your service provider for assistance.**Note:** The VLAN ID for the connection is for the Google Cloud side of the connection. To configure your on-premises router for Layer 2 connections, use the VLAN ID provided by your service provider.
  2. View the `partnerMetadata` field to check that it shows your expected service provider.

If an unexpected third party pairs with your VLAN attachment, [delete the VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/delete-vlan-attachments) and then create a new one, which generates a new pairing key. Use the new pairing key to request another connection from your service provider.

  3. Activate the attachment by using the `--adminEnabled` flag:
         
         gcloud compute interconnects attachments partner update ATTACHMENT_NAME \
             --region=REGION \
             --admin-enabled
         




After activation, your VLAN attachment can start passing traffic. For Layer 3 connections, you don't need to do any additional configuration. Your service provider supplies their autonomous system number (ASN) when configuring your VLAN attachment, and then Google automatically adds the ASN to the Border Gateway Protocol (BGP) session on your Cloud Router.

If you have activated encrypted VLAN attachments, you can complete the HA VPN over Cloud Interconnect deployment by [creating HA VPN gateways and tunnels](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect).

For Layer 2 connections, you must add the ASN of your on-premises router to your Cloud Router.

To configure Cloud Router, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the VLAN attachment that you activated to view its details page.

  3. Click **Configure BGP**.

  4. In the **Peer ASN** field, add the ASN of your on-premises router.

  5. Click **Save and continue**.




###  gcloud 

  1. For each of the BGP peers associated with your VLAN attachments, describe the Cloud Router associated with your VLAN attachment, and then find the name of the automatically created BGP peer that's associated with your VLAN attachment.

Run the following command:
         
         gcloud compute routers describe ROUTER_NAME \
            --region=REGION
         

Replace the following:

     * `ROUTER_NAME`: the name of your Cloud Router
     * `REGION`: the region in which your Cloud Router is located

The output is similar to the following for IPv4 VLAN attachments:
    
    bgp:
     advertiseMode: DEFAULT
     asn: 16550
    bgpPeers:
    - interfaceName: auto-ia-if-my-attachment-c2c53a710bd6c2e
     ipAddress: 169.254.67.201
     managementType: MANAGED_BY_ATTACHMENT
     name: auto-ia-bgp-my-attachment-c2c53a710bd6c2e
     peerIpAddress: 169.254.67.202
    creationTimestamp: '2018-01-25T07:14:43.068-08:00'
    description: 'test'
    id: '4370996577373014668'
    interfaces:
    - ipRange: 169.254.67.201/29
     linkedInterconnectAttachment: https://www.googleapis.com/compute/alpha/projects/customer-project/regions/REGION/interconnectAttachments/my-attachment-partner
     managementType: MANAGED_BY_ATTACHMENT
     name: auto-ia-if-my-attachment-c2c53a710bd6c2e
    kind: compute#router
    name: partner
    network: https://www.googleapis.com/compute/v1/projects/customer-project/global/networks/default
    region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION
    selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION/routers/my-router
    

The output is similar to the following for IPv4 and IPv6 (dual stack) VLAN attachments:
    
    bgp:
     advertiseMode: DEFAULT
     asn: 16550
    bgpPeers:
    - enableIpv4: true
     enableIpv6: false
     ipAddress: 169.254.67.201
     interfaceName: auto-ia-if-my-attachment-0098154607ecb20
     managementType: MANAGED_BY_ATTACHMENT
     name: auto-ia-bgp4-my-attachment-0098154607ecb20
     peerIpAddress: 169.254.67.202
    - enableIpv4: false
     enableIpv6: true
     ipAddress: 2600:2d00:0:1::1
     interfaceName: auto-ia-if6-my-attachment-0098154607ecb20
     managementType: MANAGED_BY_ATTACHMENT
     name: auto-ia-bgp6-my-attachment-0098154607ecb20
     peerIpAddress: 2600:2d00:0:1::2
    creationTimestamp: '2018-03-29T09:58:25.476-07:00'
    description: ''
    id: '466013140766729694'
    interfaces:
    - ipRange: 169.254.67.201/29
     linkedInterconnectAttachment: https://www.googleapis.com/compute/alpha/projects/customer-project/regions/REGION/interconnectAttachments/customer-attachment
     managementType: MANAGED_BY_ATTACHMENT
     name: auto-ia-if-customer-attach-0098154607ecb20
    - ipRange: 2600:2d00:0:1::1/125
     linkedInterconnectAttachment: https://www.googleapis.com/compute/alpha/projects/customer-project/regions/REGION/interconnectAttachments/customer-attachment
     managementType: MANAGED_BY_ATTACHMENT
     name: auto-ia-if6-customer-attach-0098154607ecb20
    kind: compute#router
    name: customer-router
    network: https://www.googleapis.com/compute/alpha/projects/customer-project/global/networks/default
    region: https://www.googleapis.com/compute/alpha/projects/customer-project/regions/REGION
    selfLink: https://www.googleapis.com/compute/alpha/projects/customer-project/regions/REGION/routers/customer-router
    

  2. Update each BGP peer with your on-premises router's ASN.

For the IPv4 BGP peer, run the following command:
         
         gcloud compute routers update-bgp-peer ROUTER_NAME \
            --peer-name=IPV4_PEER_NAME \
            --peer-asn=ON_PREM_ASN \
            --region=REGION
         

Replace the following:

     * `IPV4_PEER_NAME`: the `name` of the `bgpPeers` entry with `enableIpv4: true` from the output from the `gcloud compute routers describe` command
     * `ON_PREM_ASN`: your on-premises router's ASN

For the IPv6 BGP peer, run the following command:
    
    gcloud compute routers update-bgp-peer ROUTER_NAME \
       --peer-name=IPV6_PEER_NAME \
       --peer-asn=ON_PREM_ASN \
       --region=REGION
    

Replace `IPV6_PEER_NAME` with the `name` of the `bgpPeers` entry with `enableIpv6: true` from the output from the `gcloud compute routers describe` command.




[ Previous arrow_back  Request connections  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/requesting-connections)

[ Next Configure on-premises routers  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/configuring-onprem-routers)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
