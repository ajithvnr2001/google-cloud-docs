---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/configuring-onprem-routers/
title: Configure on-premises routers \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:05.541541+00:00
---

# Configure on-premises routers  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/configuring-onprem-routers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Configure on-premises routers Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure on-premises routers for Partner Interconnect. If you are creating a Dedicated Interconnect connection, see [Configure on-premises routers for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers).

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To help you solve common issues that you might encounter when using Partner Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#partner).

## When to configure your on-premises router

An on-premises router in this context means a [device that you configure to enable Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#connectivity-type).

  * For Layer 2 connections, configure your on-premises router after your service provider has configured your VLAN attachments.
  * For Layer 3 connections, configuring BGP on your local router is not required because the service provider configures BGP on their on-premises routers.



This document provides a sample topology and configuration for Layer 2 connections that you can use as a guide when configuring your on-premises router.

## Topology for Layer 2 connections

In this topology, the Partner Interconnect connection or connections terminate on an on-premises router, which performs BGP peering with Cloud Router.

This sample topology uses the following Google Cloud resources:

  * The project `Sample Interconnect Project`
  * The network `my-network`
  * The region `us-east1`



There are two VLAN attachments, `my-attachment1` and `my-attachment2`, which are already active and have BGP configured.

### Physical topology

The following diagram shows the physical topology for Layer 2 connections. Google and your service provider set up and manage the physical connections between Google Cloud and your service provider's network.

[ ![Sample physical Layer 2 topology \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/partner-topology-physical.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/partner-topology-physical.svg) Sample physical topology for Layer 2 connections (click to enlarge)

### Logical topology

The following diagram shows the logical topology for Layer 2 connections.

[ ![Sample logical Layer 2 topology \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/partner-topology-logical.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/partner-topology-logical.svg) Sample logical topology for Layer 2 connections (click to enlarge)

## Configure your on-premises router

This section describes how to configure Layer 2 topologies for production use. The sample configuration describes all device settings.

### On-premises router settings

Based on the configuration in the sample Google Cloud project, the following table summarizes the on-premises router settings to use for the example topology.

For the sample project name, Virtual Private Cloud (VPC) network, and region used on the Google Cloud side, see the topology reference.

The hold timer and keepalive timer values allow Google to quickly transfer traffic to redundant connections in the event of an issue. Set their values as shown in the table.

Graceful restart prevents BGP sessions from packet drops and route withdrawal during Cloud Router maintenance. If your on-premises device supports BGP graceful restart, enable it and set the graceful restart and stalepath timers as shown in the table.

For more information about BGP timer settings, see the [recommended values for BGP timers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#timer-settings) in the Cloud Router documentation.

Settings | `my-attachment1` | `my-attachment2`  
---|---|---  
VLAN number | 1010 | 1020  
VLAN interface IP address | 169.254.10.2/29 | 169.254.20.2/29  
On-premises ASN | 64500 | 64500  
Cloud Router ASN | 16550 | 16550  
Cloud Router BGP IP address | For cr1-us-east1:  
169.254.10.1 | For cr2-us-east1:   
169.254.20.1  
BGP timers | Keepalive: 20 sec | Keepalive: 20 sec  
Hold timer: 60 sec | Hold timer: 60 sec  
Graceful restart: Set the graceful restart timer to a value that is appropriate for your needs. For more information, see [BGP timer settings](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#timer-settings). | Graceful restart: Set the graceful restart timer to a value that is appropriate for your needs.  
Stalepath timer: 300 sec | Stalepath timer: 300 sec  
On-premises LAN subnet range | 192.168.12.0/24 | 192.168.12.0/24  
  
### Configuration guidelines

Use the following information on your on-premises switch or router to establish a BGP session with your Cloud Router:

  * The interface IP address and peering IP address provided by your [activated VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections).
  * The VLAN ID provided by your service provider.
  * A maximum transmission unit (MTU) of 1440, 1460, 1500, or 8896 bytes, depending on the MTU of your attachment and the VPC network.
  * You can optionally configure your BGP sessions to use [MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication). If you added MD5 authentication to the BGP session on Cloud Router, you must use the same authentication key when you configure BGP on your on-premises router.
  * For EBGP multi-hop configuration, check the Dataplane version of your VLAN attachment by using the `gcloud compute interconnects attachments describe` command. The command returns a `dataplaneVersion` field if the Dataplane version is `2` or higher. If the command output does not contain a `dataplaneVersion` field, the Dataplane version is `1`.

**Note:** The `dataplaneVersion` field appears only in the output for VLAN attachment types of `PARTNER` and `DEDICATED`. The field is not present for `PARTNER_PROVIDER`.
    * If your VLAN attachment uses Dataplane version 1, you must configure multi-hop for the EBGP neighbor. The recommended value for this setting is `4`.
    * If your VLAN attachment uses Dataplane version 2 or higher, you are not required to configure multi-hop for the EBGP neighbor. Do not configure EBGP multi-hop if you plan to use Bidirectional Forwarding Detection (BFD) in the BGP sessions of your VLAN attachment, and if BFD multi-hop is inherited from your BGP multi-hop configuration. Google Cloud supports only BFD single-hop mode. See [Configuring BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd).

**Note:** When using Partner Interconnect, your on-premises device physically connects with service provider devices rather than with a Google Edge device. For this reason, the Partner Interconnect Layer 2 configuration can be exactly the same as the example configuration or different from it. To configure your service provider-facing ports, follow the guidance that you received from your service provider.

#### Device configuration

### VLAN 1010 (Cisco) router

The following listing shows a Layer 2 sample configuration for on-premises `Router1` (Cisco) on VLAN 1010:
    
    
            interface E0/0
              description connected_to_service_provider_device
              no shut
    
            interface E0/0.1010
              description attachment_vlan1010
              encapsulation dot1Q 1010
              ip address 169.254.10.2 255.255.255.248
              ip mtu 1460
    
            ip prefix-list TO_GCP seq 5 permit 192.168.12.0/24
    
            route-map TO_GCP_OUTBOUND permit 10
              match ip address prefix-list TO_GCP
    
            router bgp 64500
              bgp graceful-restart restart-time 1
               neighbor 169.254.10.1 description peering_to_cloud_router
               neighbor 169.254.10.1 remote-as 16550
               neighbor 169.254.10.1 ebgp-multihop 4
               neighbor 169.254.10.1 timers 20 60
               neighbor 169.254.10.1 update-source E0/0.1010
               neighbor 169.254.10.1 route-map TO_GCP_OUTBOUND out
          

### VLAN 1020 (Juniper) router

The following listing shows a Layer 2 sample configuration for on-premises `Router2` (Juniper) on VLAN 1020:
    
    
              set interfaces xe-0/0/0 description "connected_to_service_provider_device"
              set interfaces xe-0/0/0 flexible-vlan-tagging
              set interfaces xe-0/0/0 unit 1020 family inet mtu 1460
              set interfaces xe-0/0/0 unit 1020 vlan-id 1020
              set interfaces xe-0/0/0 unit 1020 family inet address 169.254.20.2/29
    
              set routing-options autonomous-system 64500
    
              set policy-options prefix-list TO_GCP 192.168.12.0/24
    
              set policy-options policy-statement TO_GCP_OUTBOUND term 1 from protocol direct
              set policy-options policy-statement TO_GCP_OUTBOUND term 1 from prefix-list TO_GCP
              set policy-options policy-statement TO_GCP_OUTBOUND term 1 then accept
              set policy-options policy-statement TO_GCP_OUTBOUND term 2 then reject
    
              set protocols bgp group config_vlan_1020 type external
              set protocols bgp group config_vlan_1020 multihop ttl 4
              set protocols bgp group config_vlan_1020 local-address 169.254.20.2
              set protocols bgp group config_vlan_1020 peer-as 16550
              set protocols bgp group config_vlan_1020 neighbor 169.254.20.1 export TO_GCP_OUTBOUND
              set protocols bgp group config_vlan_1020 neighbor 169.254.20.1 graceful-restart restart-time 1
          

## Best practices

Follow these best practices to ensure effective connectivity to Google Cloud from your on-premises devices when using Cloud Interconnect 99.9% and 99.99% topologies.

### Configuring devices for active/active forwarding

  * Ensure that the same MED values are exchanged across all BGP sessions.
  * Enable [equal-cost multipath (ECMP) routing](https://wikipedia.org/wiki/Equal-cost_multi-path_routing) in your BGP configuration.
  * Enable graceful restart on your BGP sessions to minimize the impact of Cloud Router task restarts. When you connect two attachments through different edge availability domains, as described in the recommended topologies, the Cloud Router uses one task per edge availability domain. To avoid downtime, [software tasks](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#software-task-processing) are scheduled independently.
  * If you are configuring two on-premises devices, use any routing protocol to connect both devices to each other. If you are configuring your device to use redistribution, use either IBGP or IGP.



### Configuring devices for active/passive forwarding

  * To avoid asymmetric routing, make sure that higher MED values are applied on the Cloud Router side and on the on-premises device side.
  * Enable graceful restart on your BGP sessions to minimize the impact of Cloud Router task restarts. When you connect two attachments through different edge availability domains, as described in the recommended topologies, the Cloud Router uses one task per edge availability domain. To avoid downtime, [software tasks](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#software-task-processing) are scheduled independently.
  * If you are configuring two on-premises devices, make sure that both devices have Layer 3 connectivity to each other. If you are configuring your device to use redistribution, use either IBGP or IGP.



### Verifying BGP sessions

Check that your BGP sessions are working between your on-premises network and your Google Virtual Private Cloud (VPC) network. For more information, see [Viewing Cloud Router status and routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details) in the Cloud Router documentation.

[ Previous arrow_back  Activate connections  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
