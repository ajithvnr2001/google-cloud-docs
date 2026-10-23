---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides/
title: Use third-party VPNs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:46.302442+00:00
---

# Use third-party VPNs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Use third-party VPNs Stay organized with collections  Save and categorize content based on your preferences. 

This page provides Google-tested interoperability guides and vendor-specific notes for peer third-party VPN devices or services that you can use to connect to Cloud VPN.

Each Interop guide offers specific instructions for connecting the third-party VPN solution to Cloud VPN. If the third-party solution supports dynamic (BGP) routing, the guide includes configuration instructions for [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview).

Most peer VPN devices should be compatible with Cloud VPN. For general information about configuring peer VPN devices, see [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway).

Any third-party device or service that supports IPsec and IKE versions 1 or 2 should be compatible with Cloud VPN. For a list of IKE ciphers and other configuration parameters used by Cloud VPN, see [Supported IKE ciphers](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers).

Some third-party device configuration templates are available for download from the Google Cloud console. For more information, see [Download a peer VPN configuration template](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/download-config).

IPv6 is supported only in HA VPN configurations. IPv6 is not supported by Classic VPN.

For more information about Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

For definitions of terms used on this page, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms).

**Note:** Guides on this page may refer to the Classic VPN configuration instead of HA VPN.

## Interop guides by vendor

This section lists interoperability guides by vendor. Each guide covers how to use that vendor's VPN gateway solution with Cloud VPN.

For detailed notes covering the vendors listed in this section, see the vendor-specific notes section.

### A-L

Guide | Notes  
---|---  
[Alibaba Cloud VPN Gateway without redundancy](https://github.com/GoogleCloudPlatform/community/blob/master/archived/using-cloud-vpn-with-alibaba-site-to-site/index.md) | Supports static routes only.  
[Alibaba Cloud VPN Gateway with redundancy](https://github.com/GoogleCloudPlatform/community/blob/master/archived/using-cloud-vpn-with-alibaba-redundancy/index.md) | Supports static routes only.  
[Amazon Web Services with HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws) | Supports dynamic routing with Cloud Router only. **Known issue** : When setting up VPN tunnels to AWS, [using IKEv2 and setting up fewer IKE transform sets](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#aws-known-issue) on the AWS side is required.  
[Amazon Web Services with Classic VPN](https://cloud.google.com/files/CloudVPNGuide-UsingCloudVPNwithAmazonWebServices.pdf) | Supports static routes or dynamic routing with Cloud Router.  
[Cisco ASA 5506H with HA VPN](https://github.com/GoogleCloudPlatform/community/blob/master/archived/using-ha-vpn-with-cisco-asa/index.md) | Supports dynamic routing with Cloud Router only.  
[Cisco ASA 5505 with Classic VPN](https://cloud.google.com/files/CloudVPNGuide-UsingCloudVPNwithCiscoASA.pdf) | Supports static routes only.  
[Cisco ASR](https://github.com/GoogleCloudPlatform/community/blob/master/archived/using-cloud-vpn-with-cisco-asr/index.md) | Supports static routes or dynamic routing with Cloud Router.  
[Check Point security gateway](https://github.com/GoogleCloudPlatform/community/blob/master/archived/using-cloud-vpn-with-checkpoint/index.md) | Supports static routes or dynamic routing with Cloud Router.  
[Fortinet FortiGate with HA VPN](https://github.com/GoogleCloudPlatform/community/blob/master/archived/using-ha-vpn-with-fortigate/index.md) | Supports dynamic routing with Cloud Router only.  
[Fortinet FortiGate 300C with Classic VPN](https://cloud.google.com/files/CloudVPNGuide-UsingCloudVPNwithFortinetFortiGate300C.pdf) | Supports static routes or dynamic routing with Cloud Router.  
[Juniper SRX](https://github.com/GoogleCloudPlatform/community/blob/master/archived/using-cloud-vpn-with-juniper-srx/index.md) | Supports static routes or dynamic routing with Cloud Router.  
  
### M-Z

Guide | Notes  
---|---  
[Microsoft Azure with HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-azure) | Supports dynamic routing with Cloud Router only.  
[Palo Alto Networks PA-3020](https://cloud.google.com/files/CloudVPNGuide-UsingCloudVPNwithPaloAltoNetworksPA-3020.pdf) | Supports static routes or dynamic routing with Cloud Router.  
[strongSwan](https://github.com/GoogleCloudPlatform/community/blob/master/archived/using-cloud-vpn-with-strongswan/index.md) | Supports dynamic routing with Cloud Router and [BIRD](https://bird.network.cz/).  
  
## Vendor-specific notes

The following vendor-specific guidelines help you configure your third-party VPN devices to work with Cloud VPN.

### Check Point

Check Point VPN implements IKEv2 by creating multiple Child Security Associations (SAs) when you specify more than one CIDR per traffic selector. This implementation is incompatible with Cloud VPN, which requires all CIDRs for the local traffic selector and all CIDRs for the remote traffic selector to be located in a single Child SA. For suggestions about how to create a compatible configuration, see [Traffic selector strategies](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#route-alignment).

### Cisco

If your VPN gateway runs Cisco IOS XE, make sure that you're running version 16.6.3 (Everest) or later. Earlier versions have known problems with Phase 2 rekey events, which result in tunnels going down for a few minutes every few hours.

Cisco ASA supports route-based VPN with Virtual Tunnel Interface (VTI) in IOS version 9.7(x) and later. For more information, see the following:

  * [Release Notes for the Cisco ASA Series, 9.7(x)](https://www.cisco.com/c/en/us/td/docs/security/asa/asa97/release/notes/asarn97.html)
  * [Virtual Tunnel Interface sections in the Cisco ASA Series VPN CLI Configuration Guide, 9.7](https://www.cisco.com/c/en/us/td/docs/security/asa/asa97/configuration/vpn/asa-97-vpn-config/vpn-vti.pdf)

**Note:** IOS version 9.7 is not supported with ASA hardware version 5505, which has reached [end-of-life status](https://www.cisco.com/c/en/us/products/collateral/security/asa-5505-adaptive-security-appliance/eos-eol-notice-c51-738642.html). For more information, see the [ASA compatibility matrix](https://www.cisco.com/c/en/us/td/docs/security/asa/compatibility/asamatrx.html).



When using Cisco ASA devices with a Cloud VPN tunnel, you cannot configure more than one IP address range (CIDR block) for each of the local and remote traffic selectors. The reason is that Cisco ASA devices use a unique SA for each IP address range in a traffic selector, while Cloud VPN uses a single SA for all IP ranges in a traffic selector. For more information, see [Policy-based tunnels and traffic selectors](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#static-routing-networks).

## What's next

  * To configure your third-party VPN for dual-stack (IPv4 and IPv6) or IPv6-only traffic, see [Set up third-party VPNs for IPv4 and IPv6 traffic](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides-ipv6).
  * To configure firewall rules for your peer network, see [Configure firewall rules](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-firewall-rules).
  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
