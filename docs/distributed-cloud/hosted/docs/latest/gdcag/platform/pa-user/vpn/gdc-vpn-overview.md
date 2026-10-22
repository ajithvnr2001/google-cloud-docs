---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/gdc-vpn-overview/
title: Overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:38.397825+00:00
---

# Overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/gdc-vpn-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the Google Distributed Cloud (GDC) air-gapped VPN feature and describes the supported specifications and tunneling protocols.

GDC VPN securely extends a peer network to a user's virtual machine (VM) in an organization of a GDC zone through an Internet Protocol Security (IPsec) VPN connection.

Configure the GDC VPN using the `VPNGateway`, `PeerGateway`, `VPNBGPPeer`, and `VPNTunnel` resources from the [Networking API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/v1/networking-v1).

## Specifications

The GDC VPN has the following specifications:

  * GDC VPN only supports site-to-site IPsec VPN connectivity. IPsec is a suite of protocols designed to secure communication over IP networks. Other VPN technologies, such as SSL and VPN are not supported.
  * The peer VPN gateway must have a static external IPv4 address. You need this IP address to configure VPN.
  * If your peer VPN gateway is behind a firewall rule, you must configure the firewall rule to pass both Encapsulating Security Payload (ESP) IPsec protocol and Internet Key Exchange (IKE) UDP 500 and UDP 4500 traffic to it.
  * GDC VPN only supports one-to-one NAT by using UDP encapsulation for NAT-Traversal (NAT-T). The peer VPN gateway must be configured to identify itself using its static external IPv4 address, not its internal private IP.
  * IPv6 traffic is not supported.



### IPsec and IKE support

GDC VPN supports IKEv2 by using an IKE pre-shared key (shared secret) and IKE ciphers. GDC VPN only supports a pre-shared key for authentication. When you create the GDC VPN tunnel, specify a pre-shared key. When you create the tunnel at the peer VPN gateway, specify this same pre-shared key. For more information, see [Create the secret with a PSK](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/create-secret).

**Note:** Each tunnel achieves a throughput of up to 600 Mbps.

GDC VPN supports ESP in tunnel mode with authentication, but does not support AH or ESP in transport mode.

## What's next

  * [Create a VPN gateway and peer gateway](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-the-gateways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
