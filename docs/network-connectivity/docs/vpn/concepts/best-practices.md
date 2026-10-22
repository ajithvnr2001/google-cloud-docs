---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/best-practices/
title: Best practices for Cloud VPN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:34.399712+00:00
---

# Best practices for Cloud VPN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Best practices for Cloud VPN Stay organized with collections  Save and categorize content based on your preferences. 

The following best practices can be helpful when planning for and configuring Cloud VPN.

## Use separate Google Cloud projects for networking resources

To make configuration of Identity and Access Management (IAM) roles and permissions easier, wherever possible, keep your Cloud VPN and Cloud Router resources in a project separate from your other Google Cloud resources.

## Routing and failover

### Choose dynamic routing

Choose a Cloud VPN gateway that uses [dynamic routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#dynamic-routing) and the Border Gateway Protocol (BGP). Google recommends using HA VPN and deploying on-premises devices that support BGP.

### Maximize Cloud VPN availability

For high availability and better SLA, use HA VPN with BGP. If your setup requires static routes, then use Classic VPN.

For more information, see [types of VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#vpn-types) in the Cloud VPN overview.

### Configuring peer Cloud VPN gateway

We recommend using the default values from the configuration templates provided by Google Cloud. These templates often specify shorter IKE lifetimes than the Google Cloud defaults to ensure maximum compatibility across third-party VPN vendors.

To avoid connectivity drops or tunnel instability, don't change the generated lifetime values unless your third-party vendor explicitly recommends a different configuration.

Best practice | Recommended action | Description  
---|---|---  
**SA lifetime alignment** | If you are configuring tunnels manually using the API, Google Cloud CLI, or Terraform, set **Phase 1** to `36000` seconds and **Phase 2** to `10800` seconds. For more information, see the [Supported IKE Ciphers table](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers#ikev2-aead-ciphers). | Mismatched SA lifetimes cause intermittent connection drops and packet loss during key rotation.  
**Template usage** | If you are using a [ downloadable peer template](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/download-config) from the console, use the exact lifetime values defined in that template. | Downloaded templates are optimized for vendor-specific compatibility, but both endpoints must match.  
  
### Choose the appropriate tunnel configuration

Choose the appropriate tunnel configuration based on the number of HA VPN tunnels:

  * If you have two HA VPN tunnels, use an active/passive tunnel configuration.

  * If you have more than two HA VPN tunnels, use an active/active tunnel configuration.




For more information, see the following sections in the Cloud VPN overview:

  * [Active/active and active/passive routing options for HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#active-passive_routing_in_full_mesh_topologies)
  * [Recommended routing option](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#recommended-routing-option)



## Reliability

The following best practices can help improve the reliability of your Cloud VPN setup.

### Use predefined dashboards for proactive monitoring of Cloud VPN tunnels

We recommend that you use the predefined dashboards in the Cloud VPN console for monitoring Cloud VPN tunnels and overall project health in a single view.

This way is the fastest way to detect project-wide performance issues.

  * Project-wide visibility: on the **Observability** tab, check the overall health of all your tunnels.

  * Tunnel-specific visibility: on the **Monitoring** tab, view integrated Cloud VPN tunnel logs and Cloud VPN gateway logs for quick, tunnel-specific diagnosis.




For more information, see [View Monitoring dashboards](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics#viewing-monitoring-dashboards)

### Configure your peer VPN gateway with only one cipher for each cipher role

Cloud VPN can act as an initiator or a responder to IKE requests depending on the origin of traffic when a new security association is needed.

When Cloud VPN initiates a VPN connection, Cloud VPN proposes the [cipher algorithms](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#configure-ciphers) configured in the Cloud VPN tunnel. If you have not configured the cipher algorithms, then the Cloud VPN tunnel proposes the cipher algorithms in the order shown in the [supported cipher tables](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers#tables) for each cipher role. The peer side receiving the proposal selects an algorithm.

If the peer side initiates the connection, then Cloud VPN selects a cipher from the proposal by using the same order as configured or shown in the table for each cipher role.

Depending on which side is the initiator or the responder, the selected cipher can be different. For example, the selected cipher might even change over time as new security associations (SAs) are created during key rotation. Because a change in cipher selection can impact important tunnel characteristics such as performance or MTU, use a stable cipher selection. For more information about MTU, see [MTU considerations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations).

To prevent frequent changes in cipher selection, configure your peer VPN gateway and the Cloud VPN tunnel to propose and accept only one cipher for each cipher role. This cipher must be supported by both Cloud VPN and your peer VPN gateway. Do not provide a list of ciphers for each cipher role. This best practice ensures that both sides of your Cloud VPN tunnel always select the same IKE cipher during IKE negotiation.

Cloud Location Finder helps you identify the closest Google Cloud regions and zones to your physical locations worldwide. By using Cloud Location Finder, you can make informed decisions about which Google Cloud region to deploy your Cloud VPN gateways in, potentially optimizing for latency, geographic location, and carbon energy usage. For more information, see the [Cloud Location Finder](https://docs.cloud.google.com/location-finder/docs/overview) documentation.

For HA VPN tunnel pairs, configure both HA VPN tunnels on your peer VPN gateway to use the same cipher and IKE Phase 2 lifetime values.

**Note:** You can configure cipher algorithms for HA VPN topologies that connect VPC networks. If you don't configure cipher algorithms, then the HA VPN gateways auto-negotiate the cipher consistently no matter which side initiates the connection.

## Security

### Set up firewall rules for your VPN gateways

Create secure firewall rules for traffic that travels over Cloud VPN. For more information, see the [VPC firewall rules overview](https://docs.cloud.google.com/vpc/docs/firewalls).

### Use strong pre-shared keys

Google recommends [generating a strong pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key) for your Cloud VPN tunnels.

### Restrict IP addresses for your peer VPN gateways

By restricting which IP addresses can be specified for a peer VPN gateway, you can prevent unauthorized VPN tunnels from being created.

For more information, see [Restrict IP addresses for peer VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/restrict-peer-ip-addresses).

### Configure the strongest cipher on your peer VPN gateway

When configuring your peer VPN gateway, choose the strongest cipher for each cipher role that is supported by both your peer VPN gateway and Cloud VPN.

The listed proposal order for Cloud VPN is not ordered by strength.

For a list of supported IKE ciphers, see [Supported IKE ciphers](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers).

## What's next

  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
