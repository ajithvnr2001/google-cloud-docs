---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers/
title: Configure on-premises routers \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:20.646878+00:00
---

# Configure on-premises routers  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Configure on-premises routers Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure on-premises routers for Dedicated Interconnect. If you are creating a Partner Interconnect connection, see [Configuring on-premises routers for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/configuring-onprem-routers).

After you [create a VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments), you need to configure your on-premises router to establish a Border Gateway Protocol (BGP) session with your Cloud Router. To configure your on-premises router, use the VLAN ID, interface addresses, and peering addresses provided by the VLAN attachment.

If you create a dual-stack VLAN attachment, you can configure an IPv4 BGP session, an IPv6 BGP session, or both. If you configure both an IPv4 BGP session and an IPv6 BGP session, the BGP sessions run in parallel over the same VLAN attachment. For more information about parallel BGP sessions, see [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp) in the Cloud Router documentation.

You can also optionally configure your BGP sessions to use [MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication). If you added MD5 authentication to the BGP session on Cloud Router, you must use the same authentication key when you configure BGP on your on-premises router.

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To help you solve common issues that you might encounter when using Dedicated Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).

## Use sample topologies

This document provides the following sample topologies and configurations that you can use as a guide when configuring your on-premises router:

  * **Layer 3 only topology (recommended)** : A Dedicated Interconnect connection or connections terminating on an on-premises router. The router performs BGP peering with Cloud Router.
  * **Layer2/Layer3 topology** : A Dedicated Interconnect connection or connections terminating on an on-premises switch connected to an on-premises router. The router performs BGP peering with Cloud Router.



For values for third-party platforms that you might use for your on-premises router, see [vendor-specific notes](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides#vendor-specific-notes). For definite values, see your on-premises router documentation.

The sample topologies in this document use the following Google Cloud resources:

  * The project `Sample Interconnect Project`
  * The network `my-network`
  * The region `us-east1`



There are two Dedicated Interconnect connections, `my-interconnect1` and `my-interconnect2`. These connections are already provisioned and have a status of `ready to use`.

### Layer 3 only topology

In this topology, the Dedicated Interconnect connections terminate on an on-premises router, which performs BGP peering with Cloud Router.

The following diagrams show both the physical and logical Layer 3 only topology.

[ ![Sample physical, Layer 3 only topology \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/topology-1-physical.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/topology-1-physical.svg) Sample physical, on-premises Layer 3 only topology (click to enlarge)

  
  
[ ![Sample logical, Layer 3 only topology \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/topology-1-logical.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/topology-1-logical.svg) Sample logical, on-premises Layer 3 only topology (click to enlarge)

### Layer 2/Layer 3 topology

In this topology, the Dedicated Interconnect connections terminate on an on-premises switch, which then connects to an on-premises router. The router performs BGP peering with Cloud Router.

The following diagrams show the physical and logical Layer 2/Layer 3 topology.

[ ![Sample physical Layer 2/Layer 3 topology \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/topology-2-physical.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/topology-2-physical.svg) Sample physical Layer 2/Layer 3 topology (click to enlarge)

  
  
[ ![Sample logical Layer 2/Layer 3 topology \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/topology-2-logical.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/topology-2-logical.svg) Sample logical Layer 2/Layer 3 topology (click to enlarge)

## Configure on-premises devices for testing

The following section describes how to configure on-premises devices for testing your Dedicated Interconnect. For a Layer 2/Layer 3 configuration, this example describes configuring the test interface on one or more Google Cloud-facing switches, but not on the routers.

  * For information about how to test, see [Testing connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/testing-connections).
  * For production configurations of on-premises devices that show all device settings, see Configuring on-premises routers for production.



Before Google starts testing your new Dedicated Interconnect connection, configure your interfaces without VLAN tagging, which is sometimes referred to as _access mode_.

### Sample configuration for testing

The following example shows how to configure a Juniper router before testing, showing the required parameters to configure for port channel `ae0`. This configuration uses the following settings:

  * A BGP IPv4 address of `169.254.0.2` configured on port channel `ae0`.
  * LACP configured on port channel `ae0`.
  * VLAN tagging _not_ configured on port channel `ae0`. You must configure your interfaces without VLAN tagging (access mode).
  * A 1460-byte maximum transmission unit (MTU). However, you can use a 1500- or 8896-byte MTU if you adjust the router interface configuration accordingly, and if the MTU of the attachment and the MTU of the connected VPC network are also set to 1500 or 8896 bytes.
        
        set interfaces xe-0/0/0 description "my-interconnect2"
        set interfaces xe-0/0/0 gigether-options 802.3ad ae0
        set interfaces ae0 description "my-interconnect2"
        set interfaces ae0 aggregated-ether-options lacp active
        set interfaces ae0 aggregated-ether-options minimum-links 1
        set interfaces ae0 unit 0 family inet mtu 1460
        set interfaces ae0 unit 0 family inet address 169.254.0.2
        




After your Dedicated Interconnect connection is working, continue to the next section to see a sample production configuration for each topology.

## Configure on-premises routers for production

This section describes how to configure the Layer 3 only topology and the Layer 2/Layer 3 topology for production use. Each sample configuration describes all device settings.

For information about how to configure on-premises devices for testing your Dedicated Interconnect connection, see Configure on-premises routers for testing.

### Production on-premises router settings for both topologies

Based on the configuration in the sample Google Cloud project, the following table summarizes the on-premises router settings to use for the example topologies.

For the sample project name, VPC network, and region used on the Google Cloud side, see the topology reference.

The hold timer and keepalive timer values allow Google to quickly transfer traffic to redundant connections in the event of an issue. Set their values as shown in the table.

Graceful restart prevents BGP sessions from packet drops and route withdrawal during Cloud Router maintenance. If your on-premises device supports BGP graceful restart, enable it and set the graceful restart and stalepath timers as shown in the table.

For more information about BGP timer settings, see the [recommended values for BGP timers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers) in the Cloud Router documentation.

Settings | `my-interconnect1` | `my-interconnect2`  
---|---|---  
VLAN number | 1010 | 1020  
VLAN interface IPv4 address | 169.254.10.2/29 | 169.254.20.2/29  
On-premises ASN | 64500 | 64500  
Cloud Router ASN | 65200 | 65200  
Cloud Router BGP IPv4 address | For cr-us-east1 interface 0:  
169.254.10.1 | For cr-us-east1 interface 1:   
169.254.20.1  
BGP timers | Keepalive: 20 sec | Keepalive: 20 sec  
Hold timer: 60 sec | Hold timer: 60 sec  
Graceful restart: Set the graceful restart timer to a value that is appropriate for your needs. For more information, see [BGP timer settings](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#timer-settings). | Graceful restart: Set the graceful restart timer to a value that is appropriate for your needs.  
Stalepath timer: 300 sec | Stalepath timer: 300 sec  
On-premises LAN subnet range | 192.168.12.0/24 | 192.168.12.0/24  
  
### Configure Layer 3 only topology for production

Use the following guidelines when configuring the Layer 3 only topology:

  * The on-premises router port (0/0 in the diagram) or ports facing Cloud Router must be part of a port channel, even if there is only one port.
  * The port channel must have LACP enabled in either active or passive mode. LACP is required because it allows you to adjust the capacity of a Dedicated Interconnect connection without disrupting traffic.
  * The maximum transmission unit of the router interface (0/0 in the diagram) should be one of 1440, 1460, 1500, or 8896 bytes, depending on the MTU of the attachment and the [MTU of the connected VPC network](https://docs.cloud.google.com/vpc/docs/mtu).
  * For EBGP multi-hop configuration, check the Dataplane version of your VLAN attachment by using the `gcloud compute interconnects attachments describe` command. The command returns a `dataplaneVersion` field if the Dataplane version is `2` or higher. If the command output does not contain a `dataplaneVersion` field, the Dataplane version is `1`. 
    * If your VLAN attachment uses Dataplane version 1, you must configure multi-hop for the EBGP neighbor. The recommended value for this setting is `4`.
    * If your VLAN attachment uses Dataplane version 2 or higher, you are not required to configure multi-hop for the EBGP neighbor. Do not configure EBGP multi-hop if you plan to use Bidirectional Forwarding Detection (BFD) in the BGP sessions of your VLAN attachment, and if BFD multi-hop is inherited from your BGP multi-hop configuration. Google Cloud supports only BFD single-hop mode. See [Configuring BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd).

**Note:** For Juniper, you might need to configure [`aggregated-devices`](https://www.juniper.net/documentation/us/en/software/junos/chassis-cluster-security-devices/topics/ref/statement/aggregated-devices-edit-chassis.html) for aggregated interfaces (`ae`) to function.

#### Device configuration

### VLAN 1010 Router (Cisco)

The following listing shows a Layer 3 only sample configuration for on-premises `Router1` (Cisco) on VLAN 1010:
    
    
            interface E0/0
              description connected_to_google_edge_device
              channel-group 2 mode active
              no shut
    
            interface Po2
              description my-interconnect1
              no shut
    
            interface Po2.1010
              description attachment_vlan1010
              encapsulation dot1Q 1010
              ip address 169.254.10.2 255.255.255.248
              ip mtu 1460
    
            ip prefix-list TO_GCP seq 5 permit 192.168.12.0/24
    
            route-map TO_GCP_OUTBOUND permit 10
              match ip address prefix-list TO_GCP
    
            router bgp 64500
              bgp graceful-restart
              bgp graceful-restart restart-time 60
               neighbor 169.254.10.1 description peering_to_cloud_router
               neighbor 169.254.10.1 remote-as 65200
               neighbor 169.254.10.1 ebgp-multihop 4
               neighbor 169.254.10.1 timers 20 60
               neighbor 169.254.10.1 update-source Po2.1010
               neighbor 169.254.10.1 route-map TO_GCP_OUTBOUND out
          

### VLAN 1020 Router (Juniper)

The following listing shows a Layer 3 only sample configuration for on-premises `Router2` (Juniper) on VLAN 1020:
    
    
            set interfaces xe-0/0/0 ether-options 802.3ad ae1
            set interfaces xe-0/0/0 description "connected_to_google_edge_device"
    
            set interfaces ae1 description my-interconnect2
            set interfaces ae1 flexible-vlan-tagging
            set interfaces ae1 aggregated-ether-options minimum-links 1
            set interfaces ae1 aggregated-ether-options lacp active
            set interfaces ae1 unit 1020 family inet mtu 1460
            set interfaces ae1 unit 1020 vlan-id 1020
            set interfaces ae1 unit 1020 family inet address 169.254.20.2/29
    
            set routing-options autonomous-system 64500
    
            set policy-options prefix-list TO_GCP 192.168.12.0/24
    
            set policy-options policy-statement TO_GCP_OUTBOUND term 1 from protocol direct
            set policy-options policy-statement TO_GCP_OUTBOUND term 1 from prefix-list TO_GCP
            set policy-options policy-statement TO_GCP_OUTBOUND term 1 then accept
            set policy-options policy-statement TO_GCP_OUTBOUND term 2 then reject
    
            set protocols bgp group config_vlan_1020 type external
            set protocols bgp group config_vlan_1020 multihop ttl 4
            set protocols bgp group config_vlan_1020 local-address 169.254.20.2
            set protocols bgp group config_vlan_1020 peer-as 65200
            set protocols bgp group config_vlan_1020 neighbor 169.254.20.1 export TO_GCP_OUTBOUND
            set protocols bgp group config_vlan_1020 neighbor 169.254.20.1 graceful-restart restart-time 60
          

### Configure Layer 2/Layer 3 topology for production

Use the following guidelines for your on-premises switch and routers when configuring the Layer 2/Layer 3 topology:

  * VLANs must be configured on the switch.
  * The switch port (1/1 as shown in the diagram) or ports facing toward Cloud Router must be part of a port channel. 
    * The port channel must have LACP enabled, in either active or passive mode. LACP is required because it allows you to adjust the capacity of a Dedicated Interconnect connection without disrupting traffic.
    * The port channel must be configured in 802.1Q trunk mode, and all VLAN IDs used by the Dedicated Interconnect connection must be allowed.
    * The port channel must have 802.1Q VLAN tagging enabled.
  * The switch port (1/2 as shown in the diagram) facing toward the on-premises router can be a trunk port or an access port. This covers the case where a router port is dedicated to a single VLAN.
  * When enabling trunk mode on the switch side, the on-premises router must support subinterfaces with necessary encapsulation (dot1q tags).
  * This configuration uses a 1460-byte MTU. However, you can use a 1500- or 8896-byte MTU if you adjust the router interface configuration accordingly, and if the MTU of the attachment and the MTU of the connected VPC network are also 1500 or 8896 bytes.
  * For EBGP multi-hop configuration, check the Dataplane version of your VLAN attachment by using the `gcloud compute interconnects attachments describe` command. The command returns a `dataplaneVersion` field if the Dataplane version is `2` or higher. If the command output does not contain a `dataplaneVersion` field, the Dataplane version is `1`. 
    * If your VLAN attachment uses Dataplane version 1, you must configure multi-hop for the EBGP neighbor. The recommended value for this setting is `4`.
    * If your VLAN attachment uses Dataplane version 2 or higher, you are not required to configure multi-hop for the EBGP neighbor. Do not configure EBGP multi-hop if you plan to use Bidirectional Forwarding Detection (BFD) in the BGP sessions of your VLAN attachment, and if BFD multi-hop is inherited from your BGP multi-hop configuration. Google Cloud supports only BFD single-hop mode. See [Configuring BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd).

**Note:** For Juniper, you might need to configure [`aggregated-devices`](https://www.juniper.net/documentation/us/en/software/junos/chassis-cluster-security-devices/topics/ref/statement/aggregated-devices-edit-chassis.html) for aggregated interfaces (`ae`) to function.

#### Device configuration

### VLAN 1010 (Cisco) switch

The following listing shows a Layer 2/Layer 3 sample configuration for on-premises `Switch1` (Cisco) on VLAN 1010:
    
    
              vlan 1010
              name cloud_vlan1010
    
              interface E1/1
                description connected_to_google_edge_device
                Channel-group 1 mode active
    
              interface port-channel1
                description connected_to_google_edge_device
                Switchport trunk encapsulation dot1q
                Switchport mode trunk
                Switchport trunk allowed vlan 1,1010
    
              interface E1/2
                description connected_to_onprem_router
                channel-group 2 mode active
    
              interface port-channel2
                description connected_to_onprem_router
                Switchport trunk encapsulation dot1q
                Switchport mode trunk
                Switchport trunk allowed vlan 1,1010
            

### VLAN 1010 (Cisco) router

The following listing shows a Layer 2/Layer 3 sample configuration for on-premises `Router1` (Cisco) on VLAN 1010:
    
    
            interface E0/0
              description connected_to_onprem_switch
              channel-group 2 mode active
              no shut
    
            interface Po2
              description my-interconnect1
              no shut
    
            interface Po2.1010
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
              neighbor 169.254.10.1 remote-as 65200
              neighbor 169.254.10.1 ebgp-multihop 4
              neighbor 169.254.10.1 timers 20 60
              neighbor 169.254.10.1 update-source Po2.1010
              neighbor 169.254.10.1 route-map TO_GCP_OUTBOUND out
          

### VLAN 1020 (Juniper) switch

The following listing shows a Layer 2/Layer 3 sample configuration for on-premises `Switch2` (Juniper) on VLAN 1020:
    
    
            set vlans cloud_vlan1020 vlan-id 1020
    
            set interfaces xe-0/1/1 description "connected_to_google_edge_device"
            set interfaces xe-0/1/1 ether-options 802.3ad ae1
    
            set interfaces ae1 aggregated-ether-options lacp active
            set interfaces ae1 unit 0 description "connected_to_google_edge_device"
            set interfaces ae1 unit 0 family ethernet-switching port-mode trunk
            set interfaces ae1 unit 0 family ethernet-switching vlan member cloud_vlan1020
    
            set interfaces xe-0/1/2 description "connected_to_onprem_router"
            set interfaces xe-0/1/2 ether-options 802.3ad ae2
    
            set interfaces ae2 unit 0 description "connected_to_onprem_router"
            set interfaces ae2 unit 0 family ethernet-switching port-mode trunk
            set interfaces ae2 unit 0 family ethernet-switching vlan member cloud_vlan1020
          

### VLAN 1020 (Juniper) router

The following listing shows a Layer 2/Layer 3 sample configuration for on-premises `Router2` (Juniper) on VLAN 1020:
    
    
    
          set interfaces xe-0/0/0 ether-options 802.3ad ae1
          set interfaces xe-0/0/0 description connected_to_onprem_switch
    
          set interfaces ae1 description my-interconnect2
          set interfaces ae1 flexible-vlan-tagging
          set interfaces ae1 aggregated-ether-options minimum-links 1
          set interfaces ae1 aggregated-ether-options lacp active
          set interfaces ae1 unit 1020 family inet mtu 1460
          set interfaces ae1 unit 1020 vlan-id 1020
          set interfaces ae1 unit 1020 family inet address 169.254.20.2/29
    
          set routing-options autonomous-system 64500
    
          set policy-options prefix-list TO_GCP 192.168.12.0/24
    
          set policy-options policy-statement TO_GCP_OUTBOUND term 1 from protocol direct
          set policy-options policy-statement TO_GCP_OUTBOUND term 1 from prefix-list TO_GCP
          set policy-options policy-statement TO_GCP_OUTBOUND term 1 then accept
          set policy-options policy-statement TO_GCP_OUTBOUND term 2 then reject
    
          set protocols bgp group config_vlan_1020 type external
          set protocols bgp group config_vlan_1020 multihop ttl 4
          set protocols bgp group config_vlan_1020 local-address 169.254.20.2
          set protocols bgp group config_vlan_1020 peer-as 65200
          set protocols bgp group config_vlan_1020 neighbor 169.254.20.1 export TO_GCP_OUTBOUND
          set protocols bgp group config_vlan_1020 neighbor 169.254.20.1 graceful-restart restart-time 1
          

## Set up on-premises routers for IPv4 and IPv6 traffic

This section provides vendor-specific configuration examples that you can use to set up your on-premises routers to exchange IPv4 and IPv6 traffic with Cloud Interconnect and Cloud Router.

You can exchange IPv4 and IPv6 routes in your Dedicated Interconnect by doing either of the following:

  * Create an IPv4 BGP session and an IPv6 BGP session for each of your dual-stack VLAN attachments.
  * Create a single IPv4 or IPv6 BGP session for each VLAN attachment and enable multiprotocol BGP (MP-BGP).



IPv6 BGP session support is in [Preview](https://cloud.google.com/products#product-launch-stages). Dual-stack VLAN attachments are not supported for Partner Interconnect or for HA VPN over Cloud Interconnect deployments.

### Before you begin

Before you configure your on-premises router for IPv4 and IPv6 traffic, you need several pieces of information from Cloud Router.

To obtain BGP session details from Cloud Router, run the `gcloud compute routers describe` command and specify the name of the Cloud Router used by your VLAN attachments.
    
    
    gcloud compute routers describe ROUTER_NAME /
       --project PROJECT_ID /
       --region REGION
    

The output is similar to the following if you created both an IPv4 BGP session and an IPv6 BGP session for each of your VLAN attachments.
    
    
     bgp:
        advertiseMode: DEFAULT
        **asn: 65200**
        keepaliveInterval: 20
      bgpPeers:
      - advertiseMode: DEFAULT
        bfd:
          minReceiveInterval: 1000
          minTransmitInterval: 1000
          multiplier: 5
          sessionInitializationMode: DISABLED
        enable: 'TRUE'
        enableIpv4: true
        enableIpv6: false
        interfaceName: if-bgp4-1
        **ipAddress: 169.254.10.1**
        name: bgp4-1
        **peerAsn: 64500**
        **peerIpAddress: 169.254.10.2**
      - advertiseMode: DEFAULT
        bfd:
          minReceiveInterval: 1000
          minTransmitInterval: 1000
          multiplier: 5
          sessionInitializationMode: DISABLED
        enable: 'TRUE'
        enableIpv4: false
        enableIpv6: true
        interfaceName: if-bgp6-1
        **ipAddress: 2600:2d00:0:1:8000:12:0:2d1**
        name: bgp6-1
        **peerAsn: 64500**
        **peerIpAddress: 2600:2d00:0:1:8000:12:0:2d2**
      - advertiseMode: DEFAULT
        bfd:
          minReceiveInterval: 1000
          minTransmitInterval: 1000
          multiplier: 5
          sessionInitializationMode: DISABLED
        enable: 'TRUE'
        enableIpv4: true
        enableIpv6: false
        interfaceName: if-bgp4-2
        **ipAddress: 169.254.20.1**
        name: bgp4-2
        **peerAsn: 64500**
        **peerIpAddress: 169.254.20.2**
      - advertiseMode: DEFAULT
        bfd:
          minReceiveInterval: 1000
          minTransmitInterval: 1000
          multiplier: 5
          sessionInitializationMode: DISABLED
        enable: 'TRUE'
        enableIpv4: false
        enableIpv6: true
        interfaceName: if-bgp6-2
        **ipAddress: 2600:2d00:0:1:8000:0:2a1**
        name: bgp6-2
        **peerAsn: 64500**
        **peerIpAddress: 2600:2d00:0:1:8000:0:2a2**
      creationTimestamp: '2022-08-26T08:07:41.827-07:00'
    

In the output, locate the following fields in the `bgp` field and each of the `bgpPeers` fields associated with your dual-stack VLAN attachments:

  * `asn`: The ASN used by the Cloud Router.
  * `peerAsn`: The ASN used by the on-premises router. Normally, each peer uses the same value.
  * `ipAddress`: the IPv4 or IPv6 BGP address assigned to each Cloud Router interface.
  * `peerIpAddress`: the IPv4 or IPv6 BGP address assigned to each on-premises router interface.



Record these values, then proceed to Device configuration for IPv4 and IPv6 BGP sessions.

The output is similar to the following if you created a single BGP session for each of your VLAN attachments and enabled MP-BGP:
    
    
     bgp:
        advertiseMode: DEFAULT
        asn: 65200
        keepaliveInterval: 20
      bgpPeers:
      - advertiseMode: DEFAULT
        bfd:
          minReceiveInterval: 1000
          minTransmitInterval: 1000
          multiplier: 5
          sessionInitializationMode: DISABLED
        enable: 'TRUE'
        enableIpv6: true
        interfaceName: if-bgp-1
        **ipAddress: 169.254.10.1**
        ipv6NexthopAddress: 2600:2d00:0:1:8000:12:0:2d0
        name: bgp-1
        peerAsn: 64500
        **peerIpAddress: 169.254.10.2**
        **peerIpv6NexthopAddress: 2600:2d00:0:1:8000:12:0:2da**
      - advertiseMode: DEFAULT
        bfd:
          minReceiveInterval: 1000
          minTransmitInterval: 1000
          multiplier: 5
          sessionInitializationMode: DISABLED
        enable: 'TRUE'
        enableIpv6: true
        interfaceName: if-bgp-2
        **ipAddress: 169.254.20.1**
        ipv6NexthopAddress: 2600:2d00:0:1:8000:12:0:2d1
        name: bgp-2
        peerAsn: 64500
        **peerIpAddress: 169.254.20.2**
        **peerIpv6NexthopAddress: 2600:2d00:0:1:8000:12:0:2d2**
      creationTimestamp: '2022-08-26T08:07:41.827-07:00'
    

In the output, locate the following fields in the `bgpPeers` entries associated with your dual-stack VLAN attachments:

  * `peerIpv6NexthopAddress`: the IPv6 next hop addresses that is allocated to the BGP peer. Google Cloud automatically allocates these addresses when you enable IPv6 prefix exchange on your BGP session. 
  * `peerIpAddress`: the BGP IPv4 link-local address assigned to the on-premises router interface
  * `ipAddress`: the BGP IPv4 link-local address assigned to the Cloud Router interface



Record these values, then proceed to Device configuration for multiprotol BGP (MP-BGP) sessions.

### Device configuration for IPv4 and IPv6 BGP sessions

Do the following to configure your on-premises routers for IPv4 and IPv6 routing using separate IPv4 BGP sessions and IPv6 BGP sessions over Dedicated Interconnect. 

### VLAN 1010 / VLAN 1020 router (Arista EOS)

The following describes how to set up your Arista EOS router with IPv4 and IPv6 BGP sessions to exchange IPv4 and IPv6 traffic on your VLAN attachments.

#### Configure Arista EOS interfaces

Configure both an IPv4 and an IPv6 address on each of the interfaces using the following configuration commands:
    
    
    interface Ethernet1
    no switchport
    interface Ethernet1.1010
    encapsulation dot1q vlan 1010
    ip address BGP_PEER_IPV4_ADDRESS_1 255.255.255.248
    ipv6 address BGP_PEER_IPV6_ADDRESS_1/125
    end
    
    interface Ethernet2
    interface Ethernet2.1020
    encapsulation dot1q vlan 1020
    ip address BGP_PEER_IPV4_ADDRESS_2 255.255.255.248
    ipv6 address BGP_PEER_IPV6_ADDRESS_2/125
    end
    

Replace the following:

  * `BGP_PEER_IPV4_ADDRESS_1`: `peerIpAddress` from the IPv4 `bgpPeers` entry associated with your first VLAN attachment
  * `BGP_PEER_IPV6_ADDRESS_1`: `peerIpAddress` from the IPv6 `bgpPeers` entry associated with your first VLAN attachment
  * `BGP_PEER_IPV4_ADDRESS_2`: `peerIpAddress` from the IPv4 `bgpPeers` entry associated with your second VLAN attachment
  * `BGP_PEER_IPV6_ADDRESS_2`: `peerIpAddress` from the IPv6 `bgpPeers` entry associated with your second VLAN attachment



The following is an example configuration:
    
    
    interface Ethernet1
    no switchport
    interface Ethernet1.1010
    encapsulation dot1q vlan 1010
    ip address 169.254.10.2 255.255.255.248
    ipv6 address 2600:2d00:0:1:8000:12:0:2d2/125
    end
    
    interface Ethernet2
    no switchport
    interface Ethernet2.1020
    encapsulation dot1q vlan 1020
    ip address 169.254.20.2 255.255.255.248
    ipv6 enable
    ipv6 address 2600:2d00:0:1:8000:12:0:2a2/125
    end
    

#### Configure Arista BGP sessions

Enter the following commands to configure BGP for the IPv4 and IPv6 address families:
    
    
    router bgp ASN
    bgp log-neighbor-changes
    neighbor BGP_IPV4_ADDRESS_1 remote-as ROUTER_ASN
    neighbor BGP_IPV4_ADDRESS_2 remote-as ROUTER_ASN
    neighbor BGP_IPV6_ADDRESS_1 remote-as ROUTER_ASN
    neighbor BGP_IPV6_ADDRESS_2 remote-as ROUTER_ASN
    !
    address-family ipv4
    neighbor BGP_IPV4_ADDRESS_1 activate
    neighbor BGP_IPV4_ADDRESS_2 activate
    !
    address-family ipv6
    neighbor BGP_IPV6_ADDRESS_1 activate
    neighbor BGP_IPV6_ADDRESS_2 activate
    !
    

Replace the following:

  * `ASN`: the `peerAsn` from each of the `bgpPeers` entries associated with your VLAN attachments
  * `CLOUD_ROUTER_ASN`: the `asn` assigned to your Cloud Router
  * `BGP_PEER_IPV4_ADDRESS_1`: `ipAddress` from the IPv4 `bgpPeers` entry associated with your first VLAN attachment
  * `BGP_PEER_IPV6_ADDRESS_1`: `ipAddress` from the IPv6 `bgpPeers` entry associated with your first VLAN attachment
  * `BGP_PEER_IPV4_ADDRESS_2`: `ipAddress` from the IPv4 `bgpPeers` entry associated with your second VLAN attachment
  * `BGP_PEER_IPV6_ADDRESS_2`: `ipAddress` from the IPv6 `bgpPeers` entry associated with your second VLAN attachment



The following is an example configuration:
    
    
    router bgp 65201
    bgp log-neighbor-changes
    neighbor 169.254.10.1 remote-as 65200
    neighbor 169.254.20.1 remote-as 65200
    neighbor 2600:2d00:0:1:8000:12:0:2d2/125 remote-as 65200
    neighbor 2600:2d00:0:1:8000:12:0:2a2/125 remote-as 65200
    !
    address-family ipv4
    neighbor 169.254.10.1 activate
    neighbor 169.254.20.1 activate
    !
    address-family ipv6
    neighbor 2600:2d00:0:1:8000:12:0:2d2/125 activate
    neighbor 2600:2d00:0:1:8000:12:0:2a2/125 activate
    !
    

#### Add your IPv4 and IPv6 networks

Enter the following commands to add your IPv4 and IPv6 networks to the BGP configuration. The networks are advertised to Cloud Router.
    
    
    address-family ipv4
    network IPV4_NETWORK mask IPV4_NET_MASK
    !
    address-family ipv6
    network IPV6_NETWORK/IPV6_NET_PREFIX_LEN
    !
    

Replace the following:

  * `IPV4_NETWORK`: the address of your on-premises IPv4 network
  * `IPV4_NET_MASK`: the address mask of your on-premises IPv4 network
  * `IPV6_NETWORK`: the address of your on-premises IPv6 network
  * `IPV6_NET_PREFIX_LEN`: the prefix length of your on-premises IPv6 network



The following is an example configuration:
    
    
    address-family ipv4
    network 10.10.0.0 mask 255.255.0.0
    !
    address-family ipv6
    network 2001:db8::/32
    !
    

#### Verify status

To verify BGP connectivity after you have configured your device, run the following command:
    
    
    show ip route
    show ipv6 route
    

### VLAN 1010 / VLAN 1020 router (Cisco)

The following describes how to set up your Cisco IOS and IOS-XE routers with IPv4 and IPv6 BGP sessions to exchange IPv4 and IPv6 traffic on your VLAN attachments.

#### Configure Cisco interfaces

Configure both an IPv4 and an IPv6 address on each of the interfaces, then enable IPv6.

To configure two interfaces, enter the following configuration commands:
    
    
    interface Po2.1010
    no shutdown
    encapsulation dot1Q 1010
    ip address BGP_PEER_IPV4_ADDRESS_1 255.255.255.248
    ipv6 address BGP_PEER_IPV6_ADDRESS_1/125
    ipv6 enable
    !
    interface Po3.1020
    no shutdown
    encapsulation dot1Q 1020
    ip address BGP_PEER_IPV4_ADDRESS_2 255.255.255.248
    ipv6 address BGP_PEER_IPV6_ADDRESS_2/125
    ipv6 enable
    !
    

Replace the following:

  * `BGP_PEER_IPV4_ADDRESS_1`: `peerIpAddress` from the IPv4 `bgpPeers` entry associated with your first VLAN attachment
  * `BGP_PEER_IPV6_ADDRESS_1`: `peerIpAddress` from the IPv6 `bgpPeers` entry associated with your first VLAN attachment
  * `BGP_PEER_IPV4_ADDRESS_2`: `peerIpAddress` from the IPv4 `bgpPeers` entry associated with your second VLAN attachment
  * `BGP_PEER_IPV6_ADDRESS_2`: `peerIpAddress` from the IPv6 `bgpPeers` entry associated with your second VLAN attachment



The following is an example configuration:
    
    
    interface Po2.1010
    no shutdown
    encapsulation dot1Q 1010
    ip address 169.254.10.2 255.255.255.248
    ipv6 address 2600:2d00:0:1:8000:12:0:2d2/125
    ipv6 enable
    !
    interface Po3.1020
    no shutdown
    encapsulation dot1Q 1020
    ip address 169.254.20.2 255.255.255.248
    ipv6 address 2600:2d00:0:1:8000:12:0:2a2/125
    ipv6 enable
    !
    

#### Configure Cisco BGP sessions

Next, configure BGP for the IPv4 and IPv6 address families by entering the following commands: 
    
    
    router bgp ASN
    bgp log-neighbor-changes
    neighbor BGP_IPV4_ADDRESS_1 remote-as CLOUD_ROUTER_ASN
    neighbor BGP_IPV4_ADDRESS_2 remote-as CLOUD_ROUTER_ASN
    neighbor BGP_IPV6_ADDRESS_1 remote-as CLOUD_ROUTER_ASN
    neighbor BGP_IPV6_ADDRESS_2 remote-as CLOUD_ROUTER_ASN
    !
    address-family ipv4
    neighbor BGP_IPV4_ADDRESS_1 activate
    neighbor BGP_IPV4_ADDRESS_2 activate
    exit-address-family
    !
    address-family ipv6
    neighbor BGP_IPV6_ADDRESS_1 activate
    neighbor BGP_IPV6_ADDRESS_2 activate
    exit-address-family
    !
    

Replace the following:

  * `ASN`: the `peerAsn` from each of the `bgpPeers` entries associated with your VLAN attachments
  * `CLOUD_ROUTER_ASN`: the `asn` assigned to your Cloud Router
  * `BGP_PEER_IPV4_ADDRESS_1`: `ipAddress` from the IPv4 `bgpPeers` entry associated with your first VLAN attachment
  * `BGP_PEER_IPV6_ADDRESS_1`: `ipAddress` from the IPv6 `bgpPeers` entry associated with your first VLAN attachment
  * `BGP_PEER_IPV4_ADDRESS_2`: `ipAddress` from the IPv4 `bgpPeers` entry associated with your second VLAN attachment
  * `BGP_PEER_IPV6_ADDRESS_2`: `ipAddress` from the IPv6 `bgpPeers` entry associated with your second VLAN attachment



The following is an example configuration:
    
    
    router bgp 64500
    bgp log-neighbor-changes
    neighbor 169.254.10.1 remote-as 65200
    neighbor 169.254.20.1 remote-as 65200
    neighbor 2600:2d00:0:1:8000:12:0:2d1 remote-as 65200
    neighbor 2600:2d00:0:1:8000:12:0:2a1 remote-as 65200
    !
    address-family ipv4
    neighbor 169.254.10.1 activate
    neighbor 169.254.20.1 activate
    exit-address-family
    !
    address-family ipv6
    neighbor 2600:2d00:0:1:8000:12:0:2d1 activate
    neighbor 2600:2d00:0:1:8000:12:0:2a1 activate
    exit-address-family
    !
    

#### Add your IPv4 and IPv6 networks

Enter the following commands to add your IPv4 and IPv6 networks to the BGP configuration. The networks are advertised to Cloud Router.
    
    
    router bgp ASN
    !
    address-family ipv4
    network IPV4_NETWORK mask IPV4_NET_MASK
    exit-address-family
    !
    address-family ipv6
    network IPV6_NETWORK/IPV6_NET_PREFIX_LEN
    exit-address-family
    !
    

Replace the following:

  * `ASN`: the `peerAsn` from each of the `bgpPeers` entries associated with your VLAN attachments
  * `IPV4_NETWORK`: the address of your on-premises IPv4 network
  * `IPV4_NET_MASK`: the address mask of your on-premises IPv4 network
  * `IPV6_NETWORK`: the address of your on-premises IPv6 network
  * `IPV6_NET_PREFIX_LEN`: the prefix length of your on-premises IPv6 network



The following is an example configuration:
    
    
    router bgp 64500
    !
    address-family ipv4
    network 10.10.0.0 mask 255.255.0.0
    exit-address-family
    !
    address-family ipv6
    network 2001:db8::/32
    exit-address-family
    !
    

#### Verify status

To verify BGP connectivity after you have configured your device, run the following command:
    
    
    show ip route
    show ipv6 route
    

In the output, verify that your IPv4 and IPv6 networks are advertised over BGP.

### VLAN 1010 / VLAN 1020 router (Juniper)

The following describes how to configure IPv4 and IPv6 BGP sessions on your Juniper JunOS router to exchange IPv4 and IPv6 traffic using your Dedicated Interconnect.

#### Configure Juniper JunOS interfaces

Configure both an IPv4 and an IPv6 address on each of the interfaces, then enable IPv6.

To configure two interfaces, run the following configuration commands:
    
    
    set interfaces xe-0/0/0 vlan-tagging
    set interfaces xe-0/0/0 unit 0 vlan-id 1010
    set interfaces xe-0/0/0 unit 0 family inet address BGP_PEER_IPV4_ADDRESS_1/29
    set interfaces xe-0/0/0 unit 0 family inet6 address BGP_PEER_IPV6_ADDRESS_1/125
    
    set interfaces xe-0/0/1 vlan-tagging
    set interfaces xe-0/0/1 unit 0 vlan-id 1020
    set interfaces xe-0/0/1 unit 0 family inet address BGP_PEER_IPV4_ADDRESS_2/29
    set interfaces xe-0/0/1 unit 0 family inet6 address BGP_PEER_IPV6_ADDRESS_2/125
    

Replace the following:

  * `BGP_PEER_IPV4_ADDRESS_1`: `peerIpAddress` from the IPv4 `bgpPeers` entry associated with your first VLAN attachment
  * `BGP_PEER_IPV6_ADDRESS_1`: `peerIpAddress` from the IPv6 `bgpPeers` entry associated with your first VLAN attachment
  * `BGP_PEER_IPV4_ADDRESS_2`: `peerIpAddress` from the IPv4 `bgpPeers` entry associated with your second VLAN attachment
  * `BGP_PEER_IPV6_ADDRESS_2`: `peerIpAddress` from the IPv6 `bgpPeers` entry associated with your second VLAN attachment



The following is an example configuration:
    
    
    set interfaces xe-0/0/0 vlan-tagging
    set interfaces xe-0/0/0 unit 0 vlan-id 1010
    set interfaces xe-0/0/0 unit 0 family inet address 169.254.10.2/29
    set interfaces xe-0/0/0 unit 0 family inet6 address 2600:2d00:0:1:8000:12:0:2d2/125
    
    set interfaces xe-0/0/1 vlan-tagging
    set interfaces xe-0/0/1 unit 0 vlan-id 1020
    set interfaces xe-0/0/1 unit 0 family inet address 169.254.20.2/29
    set interfaces xe-0/0/1 unit 0 family inet6 address 2600:2d00:0:1:8000:12:0:2a2/125
    

The following is an example configuration block:
    
    
    interfaces {
        xe-0/0/0 {
            vlan-tagging;
            unit 0 {
                vlan-id 1010;
                family inet {
                    address 169.254.10.2/29;
                }
                family inet6 {
                    address 2600:2d00:0:1:8000:12:0:2d2/125;
                }
            }
        }
        xe-0/0/1 {
            vlan-tagging;
            unit 0 {
                vlan-id 1020;
                family inet {
                    address 169.254.20.2/29;
                }
                family inet6 {
                    address 2600:2d00:0:1:8000:12:0:2a2/125;
                }
            }
        }
    }
    

#### Configure Juniper JunOS BGP sessions

Configure BGP for the IPv4 and IPv6 address families:
    
    
    set protocols bgp group ebgp-peers type external
    set protocols bgp group ebgp-peers neighbor BGP_IPV4_ADDRESS_1 local-as ASN
    set protocols bgp group ebgp-peers neighbor BGP_IPV4_ADDRESS_2 local-as ASN
    set protocols bgp group ebgp-peers neighbor BGP_IPV4_ADDRESS_1 peer-as CLOUD_ROUTER_ASN
    set protocols bgp group ebgp-peers neighbor BGP_IPV4_ADDRESS_2 peer-as CLOUD_ROUTER_ASN
    set protocols bgp group ebgp-peers family inet6
    set protocols bgp group ebgp-peers neighbor BGP_IPV6_ADDRESS_1 local-as ASN
    set protocols bgp group ebgp-peers neighbor BGP_IPV6_ADDRESS_2 local-as ASN
    set protocols bgp group ebgp-peers neighbor BGP_IPV6_ADDRESS_1 peer-as CLOUD_ROUTER_ASN
    set protocols bgp group ebgp-peers neighbor BGP_IPV6_ADDRESS_2 peer-as CLOUD_ROUTER_ASN
    

Replace the following:

  * `ASN`: the `peerAsn` from each of the `bgpPeers` entries associated with your VLAN attachments
  * `CLOUD_ROUTER_ASN`: the `asn` assigned to your Cloud Router
  * `BGP_PEER_IPV4_ADDRESS_1`: `ipAddress` from the IPv4 `bgpPeers` entry associated with your first VLAN attachment
  * `BGP_PEER_IPV6_ADDRESS_1`: `ipAddress` from the IPv6 `bgpPeers` entry associated with your first VLAN attachment
  * `BGP_PEER_IPV4_ADDRESS_2`: `ipAddress` from the IPv4 `bgpPeers` entry associated with your second VLAN attachment
  * `BGP_PEER_IPV6_ADDRESS_2`: `ipAddress` from the IPv6 `bgpPeers` entry associated with your second VLAN attachment



The following is an example configuration block:
    
    
    protocols {
        bgp {
            group ebgp-peers {
                type external;
                neighbor 169.254.10.1 {
                    local-as 64500;
                    peer-as 65200;
                }
                neighbor 169.254.20.1 {
                    local-as 64500;
                    peer-as 65200;
                }
                family inet6;
                neighbor 2600:2d00:0:1:8000:12:0:2d1 {
                    local-as 64500;
                    peer-as 65200;
                }
                neighbor 2600:2d00:0:1:8000:12:0:2a1 {
                    local-as 64500;
                    peer-as 65200;
                }
            }
        }
    }
    

#### Verify BGP connectivity

To verify BGP connectivity after you have configured your Juniper JunOS device, run the following command.
    
    
    show route protocol bgp
    

In the output, verify that your IPv4 and IPv6 networks are advertised over BGP.

### Device configuration for multiprotocol BGP (MP-BGP) sessions

Use the following to configure your on-premises routers for IPv4 and IPv6 routing using multiprotocol BGP (MP-BGP) over Dedicated Interconnect.

Cloud Router allows you to use MP-BGP in IPv4 or IPv6 BGP sessions. However, the following instructions provide configuration examples only for IPv4 BGP sessions with MP-BGP. These instructions do not provide configuration examples for IPv6 BGP sessions with MP-BGP.

If you use this configuration, IPv6 route exchange depends on the IPv4 BGP sessions. This setup requires that you use routing policy configure IPv6 next hop addresses on your on-premises router.

### VLAN 1010 / VLAN 1020 router (Arista EOS)

The following procedure describes how to set up your Arista EOS router to support IPv4 and IPv6 traffic on your VLAN attachments using MP-BGP.

#### Configure Arista EOS interfaces

Enable and configure the IPv6 addresses on each BGP peer interface that is also configured with link-local addresses for IPv4 BGP peering. To configure two interfaces, you run the following configuration commands:
    
    
    interface Ethernet1.1010
    encapsulation dot1q vlan 1010
    ip address BGP_PEER_IPV4_ADDRESS_1/29
    **ipv6 enable**
    **ipv6 address BGP_PEER_IPV6_NEXT_HOP_ADDRESS_1/125**
    !
    !
    interface Ethernet2.1020
    encapsulation dot1q vlan 1020
    ip address BGP_PEER_IPV4_ADDRESS_2/29
    **ipv6 enable**
    **ipv6 address BGP_PEER_IPV6_NEXT_HOP_ADDRESS_2/125**
    

Replace the following:

  * `BGP_PEER_IPV4_ADDRESS_1`: the link-local IPv4 address of the first BGP peer, which is configured as the first interface on your Arista EOS device
  * `BGP_PEER_IPV4_ADDRESS_2`: the link-local IPv4 address of the second BGP peer, which is configured as the second interface on your Arista EOS device
  * `BGP_PEER_IPV6_NEXT_HOP_ADDRESS_1`: the IPv6 next hop address, or `peerIpv6NexthopAddress`, assigned to the first BGP peer in Cloud Router
  * `BGP_PEER_IPV6_NEXT_HOP_ADDRESS_2`: the IPv6 next hop address, or `peerIpv6NexthopAddress`, assigned to the second BGP peer in Cloud Router



For example, your configuration might look like the following:
    
    
    interface Ethernet1.1010
    encapsulation dot1q vlan 1010
    ip address 169.254.10.2/29
    ipv6 enable
    ipv6 address 2600:2d00:0:1:8000:12:0:2d2/125
    !
    !
    interface Ethernet2.1020
    encapsulation dot1q vlan 1020
    ip address 169.254.20.2/29
    ipv6 enable
    ipv6 address 2600:2d00:0:1:8000:12:0:2da/125
    

#### Create route-maps

Next, create route-maps that change the next-hop for the IPv6 peer to the addresses created in the previous step.
    
    
    route-map IPv6-NextHop-1 permit 10
    set ipv6 next-hop BGP_PEER_IPV6_NEXT_HOP_ADDRESS_1
    !
    route-map IPv6-NextHop-2 permit 10
    set ipv6 next-hop BGP_PEER_IPV6_NEXT_HOP_ADDRESS_2
    

Replace the following:

  * `BGP_PEER_IPV6_NEXT_HOP_ADDRESS_1`: the IPv6 next hop address, or `peerIpv6NexthopAddress`, assigned to the first BGP peer in Cloud Router
  * `BGP_PEER_IPV6_NEXT_HOP_ADDRESS_2`: the IPv6 next hop address, or `peerIpv6NexthopAddress`, assigned to the second BGP peer in Cloud Router



For example, your configuration might look like the following:
    
    
    route-map IPv6-NextHop-1 permit 10
    set ipv6 next-hop 2600:2d00:0:1:8000:12:0:2d2
    !
    route-map IPv6-NextHop-2 permit 10
    set ipv6 next-hop 2600:2d00:0:1:8000:12:0:2da
    

####  Create BGP for the IPv6 address family

Next, configure BGP for IPv6 address family, and specify the IPv6 networks that you want to advertise.

When you configure the neighbors for the IPv4 peers, you configure the route-map to change the next-hop to the interfaces specified in the previous step.
    
    
    router bgp ASN
    maximum-paths 8
    neighbor BGP_IPV4_ADDRESS_1 remote-as ROUTER_ASN
    neighbor BGP_IPV4_ADDRESS_2 remote-as ROUTER_ASN
    !
    address-family ipv4
    neighbor BGP_IPV4_ADDRESS_1 activate
    neighbor BGP_IPV4_ADDRESS_2 activate
    !
    address-family ipv6
    neighbor BGP_IPV4_ADDRESS_1 activate
    neighbor BGP_IPV4_ADDRESS_1 route-map IPv6-NextHop-1 out
    neighbor BGP_IPV4_ADDRESS_2 activate
    neighbor BGP_IPV4_ADDRESS_2 route-map IPv6-NextHop-2 out
    network YOUR_IPV6_NETWORK
    

Replace the following:

  * `ASN`: the ASN for the Arista side of the BGP session
  * `CLOUD_ROUTER_ASN`: the ASN for the Cloud Router side of the BGP session
  * `BGP_IPV4_ADDRESS_1`: the IPv4 link local address, or `ipAddress`, of the Cloud Router interface of the first BGP peer 
  * `BGP_IPV4_ADDRESS_2`: the IPv4 link local address, or `ipAddress`, of the Cloud Router interface of the second BGP peer 
  * `YOUR_IPV6_NETWORK`: The on-premises IPv6 network that you want to advertise 



For example, your configuration might look like the following:
    
    
    router bgp 65201
    maximum-paths 8
    neighbor 169.254.10.1 remote-as 65200
    neighbor 169.254.20.1 remote-as 65200
    !
    address-family ipv4
    neighbor 169.254.10.1 activate
    neighbor 169.254.20.1 activate
    !
    address-family ipv6
    neighbor 169.254.10.1 activate
    neighbor 169.254.10.1 route-map IPv6-NextHop-1 out
    neighbor 169.254.20.1 activate
    neighbor 169.254.20.1 route-map IPv6-NextHop-2 out
    network 2001:db8::/32
    

#### Enable IP routing and IPv6 routing

Make sure that IP routing and IPv6 routing is enabled:
    
    
    ip routing
    !
    ipv6 unicast-routing
    

#### Verify status

After you have configured both IP and IPv6 routing, you can verify BGP status on your with Arista EOS device with the following command:
    
    
    show ipv6 route
    

### VLAN 1010 / VLAN 1020 router (Cisco)

The following procedure describes how to set up your Cisco IOS and IOS-XE routers to support IPv4 and IPv6 traffic on your VLAN attachments using MP-BGP.

#### Configure Cisco interfaces

Configure the IPv6 addresses on each BGP peer interface that is also configured with link-local addresses for IPv4 BGP peering. Then enable IPv6.

To configure two interfaces, you supply the following configuration commands:
    
    
    interface Po2.1010
    no shutdown
    encapsulation dot1Q 1010
    ip address BGP_PEER_IPV4_ADDRESS_1 255.255.255.248
    **ipv6 address BGP_PEER_IPV6_NEXT_HOP_ADDRESS_1/125**
    **ipv6 enable**
    !
    interface Po3.1020
    no shutdown
    encapsulation dot1Q 1020
    ip address BGP_PEER_IPV4_ADDRESS_2 255.255.255.248
    **ipv6 address BGP_PEER_IPV6_NEXT_HOP_ADDRESS_2/125**
    **ipv6 enable**
    

Replace the following:

  * `BGP_PEER_IPV4_ADDRESS_1`: the link-local IPv4 address of the first BGP peer, or `peerIpAddress`, which is configured as the first interface on your Cisco device
  * `BGP_PEER_IPV4_ADDRESS_2`: the link-local IPv4 address of the second BGP peer, or `peerIpAddress`, which is configured as the second interface on your Cisco device
  * `BGP_PEER_IPV6_NEXT_HOP_ADDRESS_1`: the IPv6 next hop address, or `peerIpv6NexthopAddress`, assigned to the first BGP peer in Cloud Router
  * `BGP_PEER_IPV6_NEXT_HOP_ADDRESS_2`: the IPv6 next hop address, or `peerIpv6NexthopAddress`, assigned to the second BGP peer in Cloud Router



For example, your configuration might look like the following:
    
    
    interface Po2.1010
    no shutdown
    encapsulation dot1Q 1010
    ip address 169.254.10.2 255.255.255.248
    ipv6 address 2600:2d00:0:1:8000:12:0:2d2/125
    ipv6 enable
    !
    interface Po3.1020
    no shutdown
    encapsulation dot1Q 1020
    ip address 169.254.20.2 255.255.255.248
    ipv6 address 2600:2d00:0:1:8000:12:0:2da/125
    ipv6 enable
    

#### Create route-maps

Next, create route-maps that change the next-hop for the IPv6 peer to the addresses created in the previous step.
    
    
    route-map IPv6-NextHop-1 permit 10
    set ipv6 next-hop BGP_PEER_IPV6_NEXT_HOP_ADDRESS_1
    !
    route-map IPv6-NextHop-2 permit 10
    set ipv6 next-hop BGP_PEER_IPV6_NEXT_HOP_ADDRESS_2
    

Replace the following:

  * `BGP_PEER_IPV6_NEXT_HOP_ADDRESS_1`: the IPv6 next hop address, or `peerIpv6NexthopAddress`, assigned to the first BGP peer in Cloud Router
  * `BGP_PEER_IPV6_NEXT_HOP_ADDRESS_2`: the IPv6 next hop address, or `peerIpv6NexthopAddress`, assigned to the second BGP peer in Cloud Router



For example, your configuration might look like the following:
    
    
    route-map IPv6-NextHop-1 permit 10
    set ipv6 next-hop 2600:2d00:0:1:8000:12:0:2d2
    !
    route-map IPv6-NextHop-2 permit 10
    set ipv6 next-hop 2600:2d00:0:1:8000:12:0:2dA
    

#### Create BGP for the IPv6 address family

Next, configure BGP for IPv6 address family, and specify the networks you want to advertise.

The neighbor configuration for the IPv4 peers have the route-map configured to change the next-hop to the interfaces specified in the previous step.
    
    
    router bgp ASN
    bgp log-neighbor-changes
    neighbor BGP_IPV4_ADDRESS_1 remote-as CLOUD_ROUTER_ASN
    neighbor BGP_IPV4_ADDRESS_2 remote-as CLOUD_ROUTER_ASN
    !
    ...
    !
    address-family ipv6
    maximum-paths eibgp 8
    network YOUR_IPV6_NETWORK
    neighbor BGP_IPV4_ADDRESS_1 activate
    neighbor BGP_IPV4_ADDRESS_1 route-map IPv6-NextHop-1 out
    neighbor BGP_IPV4_ADDRESS_2 activate
    neighbor BGP_IPV4_ADDRESS_2 route-map IPv6-NextHop-2 out
    exit-address-family
    

Replace the following:

  * `ASN`: the ASN for the Cisco side of the BGP session
  * `CLOUD_ROUTER_ASN`: the ASN for the Cloud Router side of the BGP session
retrieved from `peerIpv6NexthopAddress` for the first BGP peer 
  * `BGP_IPV4_ADDRESS_1`: the IPv4 link local address, or `ipAddress`, of the Cloud Router interface of the first BGP peer 
  * `BGP_IPV4_ADDRESS_2`: the IPv4 link local address, or `ipAddress`, of the Cloud Router interface of the second BGP peer 
  * YOUR_IPV6_NETWORK: The on-premises IPv6 network that you want to advertise 



For example, your configuration might look like the following:
    
    
    router bgp 64500
    bgp log-neighbor-changes
    neighbor 169.254.10.1 remote-as 65200
    neighbor 169.254.20.1 remote-as 65200
    !
    ...
    !
    address-family ipv6
    maximum-paths eibgp 8
    network 2001:db8::/32
    neighbor 169.254.10.1 activate
    neighbor 169.254.10.1 route-map IPv6-NextHop-1 out
    neighbor 169.254.20.1 activate
    neighbor 169.254.20.1 route-map IPv6-NextHop-2 out
    exit-address-family
    

#### Verify status

After you have completed the configuration, you can verify BGP status with the following commands:
    
    
    show ipv6 route
    show ip route
    

### VLAN 1010 / VLAN 1020 router (Juniper)

The following sections describe how to configure IPv4 and IPv6 (dual-stack) traffic on your Juniper JunOS router for your Dedicated Interconnect connection using MP-BGP.

#### Configure Juniper JunOS interfaces

Configure the IPv6 addresses on each BGP peer interface that is also configured with link-local addresses for IPv4 BGP peering.
    
    
    set interfaces xe-0/0/0 vlan-tagging
    set interfaces xe-0/0/0 unit 0 vlan-id 1010
    set interfaces xe-0/0/0 unit 0 family inet address BGP_PEER_IPV4_ADDRESS_1/29
    **set interfaces xe-0/0/0 unit 0 family inet6 address BGP_PEER_IPV6_NEXT_HOP_ADDRESS_1/125**
    
    set interfaces xe-0/0/1 vlan-tagging
    set interfaces xe-0/0/1 unit 0 vlan-id 1020
    set interfaces xe-0/0/1 unit 0 family inet address BGP_PEER_IPV4_ADDRESS_2/29
    **set interfaces xe-0/0/1 unit 0 family inet6 address BGP_PEER_IPV6_NEXT_HOP_ADDRESS_2/125**
    

Replace the following:

  * `BGP_PEER_IPV4_ADDRESS_1`: the link-local IPv4 address of the first BGP peer, or `peerIpAddress`, which is configured as the first interface on your Juniper device
  * `BGP_PEER_IPV4_ADDRESS_2`: the link-local IPv4 address of the second BGP peer, or `peerIpAddress`, which is configured as the second interface on your Cisco device
  * `BGP_PEER_IPV6_NEXT_HOP_ADDRESS_1`: the IPv6 next hop address, or `peerIpv6NexthopAddress`, assigned to the first BGP peer in Cloud Router
  * `BGP_PEER_IPV6_NEXT_HOP_ADDRESS_2`: the IPv6 next hop address, or `peerIpv6NexthopAddress`, assigned to the second BGP peer in Cloud Router



For example, your configuration might look like the following:
    
    
    set interfaces xe-0/0/0 vlan-tagging
    set interfaces xe-0/0/0 unit 0 vlan-id 1010
    set interfaces xe-0/0/0 unit 0 family inet address 169.254.10.2/29
    set interfaces xe-0/0/0 unit 0 family inet6 address 2600:2d00:0:1:8000:12:0:2d2/125
    
    set interfaces xe-0/0/1 vlan-tagging
    set interfaces xe-0/0/1 unit 0 vlan-id 1020
    set interfaces xe-0/0/1 unit 0 family inet address 169.254.20.2/29
    set interfaces xe-0/0/1 unit 0 family inet6 address 2600:2d00:0:1:8000:12:0:2da/125
    

**Configuration block example:**
    
    
    interfaces {
        xe-0/0/0 {
                vlan-tagging;
                unit 0 {
                        vlan-id 1010;
                        family inet {
                                    address 169.254.10.2/29;
                        }
                        family inet6 {
                                    address 2600:2d00:0:1:8000:12:0:2d2/125;
                        }
                }
        }
        xe-0/0/1 {
                vlan-tagging;
                unit 0 {
                        vlan-id 1020;
                        family inet {
                                    address 169.254.20.2/29;
                        }
                        family inet6 {
                                    address 2600:2d00:0:1:8000:12:0:2da/125;
                        }
                }
        }
    }
    

#### Create policy statements

Next, create policy statements that change the next-hop for the IPv6 peer to the addresses created above:
    
    
    set policy-options policy-statement set-v6-next-hop-1 term 1 from family inet6
    set policy-options policy-statement set-v6-next-hop-1 term 1 from prefix-list ipv6
    **set policy-options policy-statement set-v6-next-hop-1 term 1 then next-hop BGP_PEER_IPV6_NEXT_HOP_ADDRESS_1**
    **set policy-options policy-statement set-v6-next-hop-1 term 1 then accept**
    set policy-options policy-statement set-v6-next-hop-2 term 1 from family inet6
    set policy-options policy-statement set-v6-next-hop-2 term 1 from prefix-list ipv6
    **set policy-options policy-statement set-v6-next-hop-2 term 1 then next-hop BGP_PEER_IPV6_NEXT_HOP_ADDRESS_2**
    **set policy-options policy-statement set-v6-next-hop-2 term 1 then accept**
    

Replace the following:

  * `BGP_PEER_IPV6_NEXT_HOP_ADDRESS_1`: the IPv6 next hop address, or `peerIpv6NexthopAddress`, assigned to the first BGP peer in Cloud Router
  * `BGP_PEER_IPV6_NEXT_HOP_ADDRESS_2`: the IPv6 next hop address, or `peerIpv6NexthopAddress`, assigned to the second BGP peer in Cloud Router



For example, your configuration might look like the following:
    
    
    set policy-options policy-statement set-v6-next-hop-1 term 1 from family inet6
    set policy-options policy-statement set-v6-next-hop-1 term 1 from prefix-list ipv6
    set policy-options policy-statement set-v6-next-hop-1 term 1 then next-hop 2600:2d00:0:1:8000:12:0:2d2
    set policy-options policy-statement set-v6-next-hop-1 term 1 then accept
    set policy-options policy-statement set-v6-next-hop-2 term 1 from family inet6
    set policy-options policy-statement set-v6-next-hop-2 term 1 from prefix-list ipv6
    set policy-options policy-statement set-v6-next-hop-2 term 1 then next-hop 2600:2d00:0:1:8000:12:0:2da
    set policy-options policy-statement set-v6-next-hop-2 term 1 then accept
    

**Configuration block example:**
    
    
     policy-statement set-v6-next-hop-1 {
            term 1 {
                    from {
                            family inet6;
                         }
                    then {
                            next-hop 2600:2d00:0:1:8000:12:0:2d2;
                            accept;
                         }
            }
    }
    policy-statement set-v6-next-hop-2 {
            term 1 {
                    from {
                            family inet6;
                          }
                    then {
                            next-hop 2600:2d00:0:1:8000:12:0:2da;
                            accept;
                         }
            }
    }
    

#### Configure BGP for IPv6 route exchange

Next, configure BGP for IPv6 and set the "include-mp-next-hop" statement to send the next-hop attribute to the peer.

Configure the export statement to the policy statement created above to change the next-hop to the IPv6 address specified.
    
    
    set protocols bgp group ebgp-peers type external
    set protocols bgp group ebgp-peers family inet unicast
    set protocols bgp group ebgp-peers family inet6 unicast
    
    **set protocols bgp group ebgp-peers neighbor BGP_IPV4_ADDRESS_1 export set-v6-next-hop-1**
    set protocols bgp group ebgp-peers neighbor BGP_IPV4_ADDRESS_1 peer-as CLOUD_ROUTER_ASN
    **set protocols bgp group ebgp-peers neighbor BGP_IPV4_ADDRESS_1 include-mp-next-hop**
    **set protocols bgp group ebgp-peers neighbor BGP_IPV4_ADDRESS_2 export set-v6-next-hop-2**
    set protocols bgp group ebgp-peers neighbor BGP_IPV4_ADDRESS_2 peer-as CLOUD_ROUTER_ASN
    **set protocols bgp group ebgp-peers neighbor BGP_IPV4_ADDRESS_2 include-mp-next-hop**
    

Replace the following:

  * `CLOUD_ROUTER_ASN`: the ASN for the Cloud Router side of the BGP session
retrieved from `peerIpv6NexthopAddress` for the first BGP peer 
  * `BGP_IPV4_ADDRESS_1`: the IPv4 link local address, or `ipAddress`, of the Cloud Router interface of the first BGP peer 
  * `BGP_IPV4_ADDRESS_2`: the IPv4 link local address, or `ipAddress`, of the Cloud Router interface of the second BGP peer 


    
    
    
    set protocols bgp group ebgp-peers type external
    set protocols bgp group ebgp-peers family inet unicast
    set protocols bgp group ebgp-peers family inet6 unicast
    
    set protocols bgp group ebgp-peers neighbor 169.254.10.1 export set-v6-next-hop-1
    set protocols bgp group ebgp-peers neighbor 169.254.10.1 peer-as 65200
    set protocols bgp group ebgp-peers neighbor 169.254.10.1 include-mp-next-hop
    set protocols bgp group ebgp-peers neighbor 169.254.20.1 export set-v6-next-hop-2
    set protocols bgp group ebgp-peers neighbor 169.254.20.1 peer-as 65200
    set protocols bgp group ebgp-peers neighbor 169.254.20.1  include-mp-next-hop
    

**Configuration block example:**
    
    
    protocols {
            bgp {
                group ebgp-peers {
                        type external;
                        family inet {
                                    unicast;
                        }
                        family inet6 {
                                    unicast;
                        }
                        neighbor 169.254.10.1 {
                                    export set-v6-next-hop-1;
                                    peer-as 65200;
                                    include-mp-next-hop;
                        }
                        neighbor 169.254.20.1 {
                                    export set-v6-next-hop-2;
                                    peer-as 65200;
                                    include-mp-next-hop;
                        }
                }
         }
    }
    routing-options {
            autonomous-system 64500;
    }
    

#### Verify BGP connectivity

To verify BGP connectivity after you have configured your Juniper JunOS device, run the following command.
    
    
    show route protocol bgp
    

In the output, verify that your IPv6 networks are being advertised over BGP.

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

[ Previous arrow_back  Create VLAN attachments  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


