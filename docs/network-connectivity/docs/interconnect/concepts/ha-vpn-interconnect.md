---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect/
title: HA VPN over Cloud Interconnect overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:57.395187+00:00
---

# HA VPN over Cloud Interconnect overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  HA VPN over Cloud Interconnect overview Stay organized with collections  Save and categorize content based on your preferences. 

HA VPN over Cloud Interconnect lets you encrypt the traffic that traverses your Dedicated Interconnect or Partner Interconnect connections. To use HA VPN over Cloud Interconnect, you deploy [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn) tunnels over your VLAN attachments.

With HA VPN over Cloud Interconnect, you can improve the overall security of your business and maintain compliance with existing and upcoming industry regulations. For example, you might be required to encrypt the outgoing traffic from your applications or ensure that data is encrypted in transit over third parties.

You have many choices in meeting these requirements. Encryption can be performed at several layers in the OSI stack and at some layers might not be universally supported. For example, Transport Layer Security (TLS) is not supported for all TCP-based protocols, and enabling Datagram TLS (DTLS) might not be supported for all UDP-based protocols. One solution is to implement encryption at the network layer with the IPsec protocol.

As a solution, HA VPN over Cloud Interconnect has the advantage of providing deployment tools by using the Google Cloud console, the Google Cloud CLI, and the Compute Engine API. You can also use internal IP addresses for your HA VPN gateways. The VLAN attachments that you create for HA VPN over Cloud Interconnect support [connections to Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises). Finally, HA VPN over Cloud Interconnect has an SLA that is derived from its underlying components, Cloud VPN and Cloud Interconnect. For more information, see SLA.

Another option is to create a self-managed (non-Google Cloud) VPN gateway in your Virtual Private Cloud (VPC) network and assign an internal IP address to each gateway. For example, you can run a strongSwan VPN on a Compute Engine instance. You then terminate IPsec tunnels to those VPN gateways by using Cloud Interconnect from an on-premises environment. For more information about HA VPN options, see [HA VPN topologies](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies).

You cannot deploy Classic VPN gateways and tunnels over Cloud Interconnect.

## Deployment architecture

When you deploy HA VPN over Cloud Interconnect, you create two operational tiers:

  * The Cloud Interconnect tier, which includes the VLAN attachments and the Cloud Router for Cloud Interconnect.
  * The HA VPN tier, which includes the HA VPN gateways and tunnels and the Cloud Router for HA VPN.



Each tier requires its own Cloud Router: 

  * The Cloud Router for Cloud Interconnect is used exclusively to exchange VPN gateway prefixes between the VLAN attachments. This Cloud Router is used only by the VLAN attachments of the Cloud Interconnect tier. It cannot be used in the HA VPN tier.
  * The Cloud Router for HA VPN exchanges prefixes between your VPC network and your on-premises network. You configure the Cloud Router for HA VPN and its BGP sessions in the same way you would for a regular HA VPN deployment.



You build the HA VPN tier on top of the Cloud Interconnect tier. Therefore, the HA VPN tier requires that the Cloud Interconnect tier, based on either Dedicated Interconnect or Partner Interconnect, is properly configured and operational.

The following diagram depicts an HA VPN over Cloud Interconnect deployment.

[ ![Deployment architecture for HA VPN over
Cloud Interconnect \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/havpn-interconnect-architecture.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/havpn-interconnect-architecture.svg) **Figure 1.** Deployment architecture for HA VPN over Cloud Interconnect (click to enlarge).

The IP address ranges learned by the Cloud Router on the Cloud Interconnect tier are used to select the internal traffic sent to the HA VPN gateways and the VLAN attachments.

## Failover

The following sections describe different types of HA VPN over Cloud Interconnect failover.

### Cloud Interconnect failover

When the BGP session on the Cloud Interconnect tier goes down, the corresponding HA VPN to Cloud Interconnect routes are retracted. This retraction leads to HA VPN tunnel interruption. As a result, routes are shifted to the other HA VPN tunnels that are hosted on the other VLAN attachment.

The following diagram depicts Cloud Interconnect failover.

[ ![Cloud Interconnect VLAN attachment failover for HA VPN over Cloud Interconnect \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/havpn-interconnect-failover.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/havpn-interconnect-failover.svg) **Figure 2.** Cloud Interconnect VLAN attachment failover for HA VPN over Cloud Interconnect (click to enlarge).

### HA VPN tunnel failover

When a BGP session on the HA VPN tier goes down, normal BGP failover occurs, and HA VPN tunnel traffic is routed to other available HA VPN tunnels. The BGP sessions of the Cloud Interconnect tier are unaffected.

The following diagram depicts HA VPN tunnel failover.

[ ![HA VPN tunnel failover for HA VPN over Cloud Interconnect \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/havpn-interconnect-tunnel-failover.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/havpn-interconnect-tunnel-failover.svg) **Figure 3.** HA VPN tunnel failover for HA VPN over Cloud Interconnect (click to enlarge).

## SLA

[HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn) is a high-availability (HA) Cloud VPN solution that lets you securely connect your on-premises network to your VPC network by using an IPsec VPN connection in a single [Google Cloud region](https://docs.cloud.google.com/docs/geography-and-regions). HA VPN, deployed on its own, has its own [SLA](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies) when properly configured.

However, because HA VPN is deployed on top of Cloud Interconnect, the overall SLA for HA VPN over Cloud Interconnect matches the SLA of the Cloud Interconnect topology that you choose to deploy.

The SLA for HA VPN over Cloud Interconnect depends on the Cloud Interconnect topology that you choose to deploy. To qualify for an SLA, your deployments must have a gateway with 2 VLAN attachments associated (failover).

  * **Deployments with a single VLAN attachment**

There is no SLA for deployments of gateways with a single VLAN attachment.

  * **Multi-region deployment for production-level applications**

If the deployment uses a multi-region Cloud Interconnect topology, the HA VPN over Cloud Interconnect deployment has an SLA of 99.99%.

    * For Dedicated Interconnect, see [Establish 99.99% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability).
    * For Partner Interconnect, see [Establish 99.99% availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability).
  * **Single region deployment for non-critical applications**

If the deployment uses a single region Cloud Interconnect topology, the HA VPN over Cloud Interconnect deployment has an SLA of 99.9%.

    * For Dedicated Interconnect, see [Establish 99.9% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-999-availability).
    * For Partner Interconnect, see [Establish 99.9% availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-999-availability). 



## Pricing summary

For HA VPN over Cloud Interconnect deployments, you are charged for the following components:

  * Your Dedicated Interconnect connection, if you use Dedicated Interconnect.
  * Each VLAN attachment.
  * Each VPN tunnel.
  * Cloud Interconnect egress traffic only. You are not charged for the Cloud VPN egress traffic carried by your HA VPN tunnels.
  * Regional external IP addresses assigned to your HA VPN gateways, if you choose to use external IP addresses. However, you are only charged for the IP addresses that are not in use by VPN tunnels.



For more information, see [Cloud VPN Pricing](https://cloud.google.com/vpn/pricing) and [Cloud Interconnect Pricing](https://cloud.google.com/network-connectivity/pricing).

## Limitations

  * Configuration:

    * The HA VPN gateway is an immutable resource. Once you create and associate a VLAN attachment, you cannot change the associations between the attachment and the interfaces of the HA VPN gateway.

For example, if you decide later that you need to configure for failover, you must create a new HA VPN gateway and then delete the original gateway and its tunnels.

    * You must select IPsec encryption when you create the VLAN attachment. You cannot add encryption to an existing attachment at a later time.

    * For each VLAN attachment, you can reserve only one internal IP address range for your HA VPN gateway interfaces.

    * Enabling [Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd) does not provide faster failure detection for HA VPN over Cloud Interconnect deployments.

    * HA VPN over Cloud Interconnect supports IPv4 and IPv6 (dual-stack) HA VPN gateways. To create dual-stack HA VPN gateways, you must use the Google Cloud CLI or Cloud Interconnect API. You cannot use the HA VPN over Cloud Interconnect deployment wizard in the Google Cloud console.

  * Payload and latency:

    * HA VPN over Cloud Interconnect differentiates between the following maximum transmission unit (MTU) values:

      * [HA VPN over Cloud Interconnect gateway MTU](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms#cloud-vpn-gateway-mtu): 1440 bytes.

      * [HA VPN over Cloud Interconnect payload MTU](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms#ha-vpn-interconnect-payload-mtu): is between 1354 to 1386 bytes, depending on the cipher used. For more information, see [Encrypted traffic MTU values](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations#encrypted-traffic-mtu-values).

    * Each HA VPN tunnel can support up to 250,000 packets per second for the sum of ingress and egress traffic. This is a limitation of HA VPN. For more information, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/vpn/quotas#limits) in the Cloud VPN documentation.

    * For a single VLAN attachment with encryption enabled, the combined inbound and outbound throughput is limited to 50 Gbps.

    * In terms of latency, adding IPsec encryption to Cloud Interconnect

traffic adds some delay. During normal operations, the added latency is under 5 milliseconds.

  * You can terminate the VLAN attachments and IPsec tunnels on two different physical on-premises devices. The BGP sessions over each VLAN attachment, advertising and negotiating the VPN gateway prefixes, should terminate on the on-premises VLAN attachment device. The BGP sessions over each VPN tunnel, advertising the cloud prefixes (as usual), should terminate on the VPN device.

  * The ASNs of the two Cloud Routers can be different. Cloud Router interfaces that peer with on-premises devices cannot be assigned RFC 1918 (private) IP addresses.




## What's next?

  * To follow the steps required to deploy HA VPN over Cloud Interconnect, see [HA VPN over Cloud Interconnect deployment process](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-deploy-process).

  * To deploy HA VPN over Cloud Interconnect

using Terraform, see [Terraform examples for HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-terraform).

  * To configure HA VPN over Cloud Interconnect, see [Configure HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
