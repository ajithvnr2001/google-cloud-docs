---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/configure-onprem-routers/
title: Configure on-premises routers \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:12:45.170503+00:00
---

# Configure on-premises routers  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/configure-onprem-routers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Configure on-premises routers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure on-premises routers for Cross-Site Interconnect.

After you create a cross-site network with one or more wire groups, you need to configure your on-premises routers at sites A and B to establish connectivity with each other.

This page provides a sample topology and configuration that you can use as a guide when configuring your on-premises routers.

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology) and the [Cross-Site Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview).

## Sample topology

This page provides sample configurations for a topology in which:

  * Each Cross-Site Interconnect connection terminates on an on-premises router.
  * A cross-site network with a redundant wire group has been created over the connections.
  * Each on-premises router establishes connectivity with the corresponding router at the opposite site over the wire between the connections. The routers exchange routes using IGP.



The following diagrams show both the physical and logical topology.

[ ![Sample physical topology for Cross-Site Interconnect.](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/cross-site-topology-physical.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/cross-site-topology-physical.svg) Sample physical topology (click to enlarge).

  
  
[ ![Sample logical topology for Cross-Site Interconnect.](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/cross-site-topology-logical.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/cross-site-topology-logical.svg) Sample logical topology (click to enlarge).

## Configure on-premises routers

This section provides sample on-premises router configurations. Consider the following when using the samples on this page:

  * The samples assume 10 Gbps Cross-Site Interconnect connections.
  * Some configurations are marked as optional. Use the corresponding samples as needed depending on your use case.
  * The samples apply to router A1 from the sample topology. You must also configure routers A2, B1, and B2.



For additional information about configuration settings and values, see the documentation for your device.

### Configure the interface

This sample configures the interface of the on-premises router as follows:

  * Sets the description to the name and interface of the neighbor router with which you are establishing connectivity, in the format `ROUTER_NAME`:`INTERFACE_NAME`. For router A1, the neighbor router is router B1.
  * Sets the IP addresses of the interface for router A1 using the values from the sample topology.
  * Sets MTU to the recommended value of `9000`.
  * Sets MTU values for MPLS in both samples, and enables MPLS in the Cisco sample. These settings are optional as indicated by the brackets (`[]`). You can omit these settings if you don't plan to configure MPLS RSVP.




###  Router A1 (Juniper) 

See the following sample configuration:
    
    
    set interfaces xe-1/1/0 unit 0 description routerB1:xe-1/1/0
    set interfaces xe-1/1/0 unit 0 family inet mtu 9000
    set interfaces xe-1/1/0 unit 0 family inet address 10.0.0.0
    set interfaces xe-1/1/0 unit 0 family iso mtu 9000
    set interfaces xe-1/1/0 unit 0 family inet6 mtu 9000
    set interfaces xe-1/1/0 unit 0 family inet6 address 2001::
    [set interfaces xe-1/1/0 unit 0 family mpls mtu 9000]
    

###  Router A1 (Cisco) 

See the following sample configuration:
    
    
    interface TenGigE/1/0
     description routerB1:xe-1/1/0:TenGigE/1/0
     mtu 9000
     ip address 10.0.0.0
     ipv6 mtu 9000
     ipv6 address 2001::
     [mpls mtu 9000]
     [mpls ip]
    

### Configure traffic shaper

To help avoid packet loss, shape traffic below the Cross-Site Interconnect connection capacity to account for additional encapsulation overhead. If you don't configure traffic shaper, you might experience packet loss when traffic is at or near the full capacity of the connection, depending on the frame size.

This sample configures traffic shaper with a value of `9500000000` bits per second (bps) for a 10 Gbps Cross-Site Interconnect connection. If you have a 100 Gbps connection, the recommended value is `96000000000`.

This sample also sets the description to the name of the neighbor router. For router A1, the neighbor is router B1.

###  Router A1 (Juniper) 

See the following sample configuration:
    
    
    set interfaces xe-1/1/0 unit 0 description routerB1:xe-1/1/0
    set class-of-service interfaces xe-1/1/0 scheduler-map qos-scheduler
    set class-of-service interfaces xe-1/1/0 shaping-rate 9500000000
    

###  Router A1 (Cisco) 

See the following sample configuration:
    
    
    interface TenGigE/1/0
     description routerB1
     service-policy output qos-scheduler
     shape average 9500000000
    !
    

### Enable IGP and BFD

Enable IGP and BFD to exchange routes and detect failures so that you can implement failover.

To save bandwidth, the following sample disables CSNP by setting `csnp-interval` to the maximum value. This setting is optional as indicated by the brackets (`[]`). You can remove or adjust this setting if your network requires CSNP.

**Note:** We recommend that you configure BFD with the following timers and associate it with an IGP as follows. You can alternatively use another method, such as configuring BFD on the interfaces or with static routes.

###  Router A1 (Juniper) 

See the following sample configuration:
    
    
    set protocols isis interface xe-1/1/0.0 level 2 metric 3000
    set protocols isis interface xe-1/1/0.0 level 2 hello-interval 1
    set protocols isis interface xe-1/1/0.0 level 2 hold-time 5
    set protocols isis interface xe-1/1/0.0 level 1 disable
    set protocols isis interface xe-1/1/0.0 hello-padding adaptive
    [set protocols isis interface xe-1/1/0.0 csnp-interval 65535]
    set protocols isis interface xe-1/1/0.0 point-to-point
    set protocols isis interface xe-1/1/0.0 family inet bfd-liveness-detection version 1
    set protocols isis interface xe-1/1/0.0 family inet bfd-liveness-detection minimum-interval 250
    set protocols isis interface xe-1/1/0.0 family inet bfd-liveness-detection multiplier 3
    set protocols isis interface xe-1/1/0.0 family inet bfd-liveness-detection detection-time threshold 900
    set protocols isis interface xe-1/1/0.0 family inet bfd-liveness-detection authentication key-chain IS-IS-BFD-KEY
    set protocols isis interface xe-1/1/0.0 family inet bfd-liveness-detection authentication algorithm keyed-sha-1
    

Replace `IS-IS-BFD-KEY` with the name of your IS-IS BFD keychain.

### Enable LLDP

If you have port mode wire groups, enable LLDP to help verify connectivity between your routers. LLDP protocol data units (PDUs) are automatically forwarded across the port mode wire between your routers. When your routers successfully exchange LLDP information, it confirms that the wire is functioning correctly.

You can also enable LLDP before completing the interface configuration to help verify newly provisioned Cross-Site Interconnect connections.

###  Router A1 (Juniper) 

See the following sample configuration:
    
    
    set protocols lldp interface xe-1/1/0.0
    

###  Router A1 (Cisco) 

See the following sample configuration:
    
    
    interface TenGigE/1/0
     lldp
      receive disable
      transmit disable
     !
    

### Enable MACsec

Enable MACsec (port mode, optional) if you have port mode wire groups and want to use MACsec.

This sample configuration does the following:

  * Enables a must-secure policy
  * Configures a replay window with the maximum value to prevent replay protection from generating false positives when MACsec attempts to order packets
  * Sets the `eapol` destination MAC address to `broadcast-address`




###  Router A1 (Cisco) 
    
    
    interface TenGigE/1/0
     Description facing google PF
     macsec replay-protection window-size 4294967295
     macsec network-link
     no cdp enable
     eapol destination-address broadcast-address
     mka policy MKA_POLICY_NAME
     mka pre-shared-key key-chain MKA_KEY_CHAIN
     service-policy output egress-scheduler
    End
    

Replace the following:

  * `MKA_POLICY_NAME`: the name of your MKA policy
  * `MKA_KEY_CHAIN`: the name of your MKA keychain



### Enable QinQ

QinQ is optional and is used to transport VLANs across a service provider network.

Adjust the sample as needed depending on whether you are using STP, LACP, or both protocols between your endpoints.

###  Router A1 (Cisco) 

See the following sample configuration:
    
    
    interface TenGigE/1/0
     switchport access vlan VLAN_ID
     switchport mode dot1q-tunnel
     l2protocol-tunnel stp
     l2protocol-tunnel point-to-point lacp
    

Replace `VLAN_ID` with your VLAN ID.

### Configure MPLS RSVP

MPLS RSVP is optional and is used to handle failover.

###  Router A1 (Juniper) 

See the following sample configuration:
    
    
    set protocols mpls interface xe-1/1/0.0 admin-group encrypted
    set protocols mpls interface xe-1/1/0.0 admin-group unencrypted
    
    set protocols rsvp interface xe-1/1/0.0 subscription 80
    set protocols rsvp interface xe-1/1/0.0 update-threshold 5
    set protocols rsvp interface xe-1/1/0.0 link-protection optimize-timer 3000
    set protocols rsvp interface xe-1/1/0.0 link-protection exclude-srlg
    set protocols rsvp interface xe-1/1/0.0 link-protection admin-group include-all encrypted
    set protocols rsvp interface xe-1/1/0.0 link-protection admin-group include-all unencrypted
    set protocols rsvp interface xe-1/1/0.0 link-protection admin-group exclude red
    

[ Previous arrow_back  Create a cross-site network  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/create-network)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
