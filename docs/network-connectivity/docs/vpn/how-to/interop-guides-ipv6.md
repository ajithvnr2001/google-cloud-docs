---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides-ipv6/
title: Set up third-party VPNs for IPv4 and IPv6 traffic \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:50.330733+00:00
---

# Set up third-party VPNs for IPv4 and IPv6 traffic  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides-ipv6/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Set up third-party VPNs for IPv4 and IPv6 traffic Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for configuring third-party VPN devices to support dual-stack (IPv4 and IPv6) or IPv6-only traffic with Cloud VPN.

To enable dual-stack traffic in your HA VPN tunnels, you must configure your peer VPN gateway with IPv6 next-hop addresses. In HA VPN tunnels with dual-stack traffic enabled, IPv4 and IPv6 routes are exchanged over BGP sessions by using multiprotocol BGP (MP-BGP) with link-local IPv4 addresses. Both the Cloud Router and your peer VPN gateway need IPv6 next hop configuration to route IPv6 traffic to and from the Virtual Private Cloud (VPC) and your peer networks.

Only HA VPN gateways support dual-stack or IPv6-only traffic. Classic VPN does not support IPv6 traffic. Make sure that your peer VPN gateway is configured to use IKEv2 for its HA VPN tunnels.

## Third-party VPN support for dual-stack traffic

The following table summarizes third-party VPN device support for dual-stack traffic over IPsec tunnels.

**Note:** Vendors are continuously adding support for dual-stack traffic. For the latest updates, refer to your vendor's platform documentation.Vendor platform | Version tested for  
dual-stack configuration | IPv6 traffic over IPv4 IPsec tunnel | IPv6 only traffic | Dual-stack address family | Interoperable configuration for dual-stack traffic  
---|---|---|---|---|---  
**Cisco IOS** | Not supported | Not supported | Supported | Not supported | Use Generic Routing Encapsulation (GRE) tunnels and a virtual router to carry IPsec traffic over GRE.   
**Check Point** | Not supported | Not supported | Not supported | Not supported | Use Generic Routing Encapsulation (GRE) tunnels and a virtual router to carry IPsec traffic over GRE.  
**Juniper JunOS** | 20.2R3-S2.5 | Supported | Not supported | Supported | Supports HA VPN tunnels that can carry both IPv4 and IPv6 traffic.  
**Palo Alto Networks PAN-OS** | 9.1 | Supported | Not supported | Not supported | Requires separate HA VPN tunnels configured for either IPv4 or IPv6 traffic, but not both.  
  
## Juniper JunOS

The following procedure describes how to set up your Juniper JunOS VPN device to support IPv4 and IPv6 traffic in your HA VPN tunnels.

**Note:** These instructions provide only configuration examples for IPv4 BGP sessions that use multiprotocol BGP (MP-BGP) to exchange both IPv4 and IPv6 routes. These instructions don't provide IPv6 BGP configuration examples.

Although you configure IPv6 addresses on the tunnel interfaces of the device, the IPv6 addresses are solely used for IPv6 next hop configuration. IPv6 routes are advertised through IPv6 Network Layer Reachability Information (NLRI) over IPv4 BGP peering.

### Before you begin

In Google Cloud, set up [one dual-stack HA VPN gateway and two HA VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn). Both HA VPN tunnels carry IPv4 and IPv6 traffic.

Record the two external IPv4 addresses that Google Cloud assigns to the two HA VPN gateway interfaces.

Record the following configuration values for each tunnel:

  * The link-local IPv4 address of the BGP peer, which is your Juniper JunOS device
  * The link-local IPv4 address of the Cloud Router used for BGP peering
  * The IPv6 next hop address assigned to the peer or `peerIpv6NexthopAddress`
  * The ASN you assigned to the Cloud Router for your BGP sessions
  * The ASN you assigned to the BGP peer, which is your Juniper JunOS device
  * The pre-shared key



To find the details for your BGP session configuration, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

### Configure JunOS

To configure JunOS devices, complete the following steps:

  1. For each VPN tunnel interface, configure the BGP peer IPv6 next hop addresses that you retrieved from the Cloud Router. These interfaces are the same interfaces that are assigned link-local addresses for IPv4 peering.
         
         set interfaces st0 unit 1 family inet mtu 1460
         set interfaces st0 unit 1 family inet address PEER_BGP_IP_1
         set interfaces st0 unit 1 family inet6 address PEER_IPV6_NEXT_HOP_ADDRESS_1
         set interfaces st0 unit 2 family inet mtu 1460
         set interfaces st0 unit 2 family inet address PEER_BGP_IP_2
         set interfaces st0 unit 2 family inet6 address PEER_IPV6_NEXT_HOP_ADDRESS_2
         

Replace the following values:

     * `PEER_BGP_IP_1`: the BGP IPv4 address of the peer for the first tunnel interface with its subnet mask
     * `PEER_IPV6_NEXT_HOP_ADDRESS_1`: the IPv6 next hop address of the peer for the first tunnel interface with its subnet mask
     * `PEER_BGP_IP_2`: the BGP IPv4 address of the peer for the second tunnel interface with its subnet mask
     * `PEER_IPV6_NEXT_HOP_ADDRESS_2`: the IPv6 next hop address of the peer for the second tunnel interface with its subnet mask

For example:
    
    set interfaces st0 unit 1 family inet mtu 1460
    set interfaces st0 unit 1 family inet address 169.254.0.2/30
    set interfaces st0 unit 1 family inet6 address 2600:2d00:0:2::2/125
    set interfaces st0 unit 2 family inet mtu 1460
    set interfaces st0 unit 2 family inet address 169.254.1.2/30
    set interfaces st0 unit 2 family inet6 address 2600:2d00:0:2::1:2/125
    

  2. Configure the IKE proposal, IKE policy, and IKE gateway objects.

**Note:** IPv6 support in HA VPN requires IKEv2.
         
         # IKE proposal
         set security ike proposal ike_prop authentication-method pre-shared-keys
         set security ike proposal ike_prop dh-group group2
         set security ike proposal ike_prop authentication-algorithm sha-256
         set security ike proposal ike_prop encryption-algorithm aes-256-cbc
         set security ike proposal ike_prop lifetime-seconds 36000
         
         # IKE policy
         set security ike policy ike_pol mode main
         set security ike policy ike_pol proposals ike_prop
         set security ike policy ike_pol pre-shared-key ascii-text SHARED_SECRET
         
         # IKE gateway objects
         set security ike gateway gw1 ike-policy ike_pol
         set security ike gateway gw1 address HA_VPN_INTERFACE_ADDRESS_0
         set security ike gateway gw1 local-identity inet 142.215.100.60
         set security ike gateway gw1 external-interface ge-0/0/0
         set security ike gateway gw1 version v2-only
         set security ike gateway gw2 ike-policy ike_pol
         set security ike gateway gw2 address HA_VPN_INTERFACE_ADDRESS_1
         set security ike gateway gw2 local-identity inet 142.215.100.60
         set security ike gateway gw2 external-interface ge-0/0/0
         set security ike gateway gw2 version v2-only
         

Replace the following values:

     * `HA_VPN_INTERFACE_ADDRESS_0`: the external IPv4 address of the first tunnel interface on the HA VPN gateway
     * `HA_VPN_INTERFACE_ADDRESS_1`: the external IPv4 address of the second tunnel interface on the HA VPN gateway
     * `SHARED_SECRET`: the pre-shared key you configured for the HA VPN tunnel
  3. Configure IPsec proposal and IPsec policy. For example:
         
         set security ipsec proposal ipsec_prop protocol esp
         set security ipsec proposal ipsec_prop authentication-algorithm hmac-sha1-96
         set security ipsec proposal ipsec_prop encryption-algorithm aes-256-cbc
         set security ipsec proposal ipsec_prop lifetime-seconds 10800
         

  4. Configure the IPsec VPN gateway configurations and bind them to the tunnel interfaces. For example:
         
         set security ipsec vpn vpn1 bind-interface st0.1
         set security ipsec vpn vpn1 ike gateway gw1
         set security ipsec vpn vpn1 ike ipsec-policy ipsec_pol
         set security ipsec vpn vpn1 establish-tunnels immediately
         set security ipsec vpn vpn2 bind-interface st0.2
         set security ipsec vpn vpn2 ike gateway gw2
         set security ipsec vpn vpn2 ike ipsec-policy ipsec_pol
         set security ipsec vpn vpn2 establish-tunnels immediately
         

  5. Create the policy statements that change the next hop for IPv6 peers to the IPv6 next hop addresses.
         
         set policy-options policy-statement set-v6-next-hop-1 term 1 from family inet6
         set policy-options policy-statement set-v6-next-hop-1 term 1 then next-hop PEER_IPV6_NEXT_HOP_ADDRESS_1
         set policy-options policy-statement set-v6-next-hop-1 term 1 then accept
         set policy-options policy-statement set-v6-next-hop-2 term 1 from family inet6
         set policy-options policy-statement set-v6-next-hop-2 term 1 then next-hop PEER_IPV6_NEXT_HOP_ADDRESS_2
         set policy-options policy-statement set-v6-next-hop-2 term 1 then accept
         

Replace the following values:

     * `PEER_IPV6_NEXT_HOP_ADDRESS_1`: the IPv6 next hop address of the BGP peer for the first tunnel
     * `PEER_IPV6_NEXT_HOP_ADDRESS_2`: the IPv6 next hop address of the BGP peer for the second tunnel

For example: 
    
    set policy-options policy-statement set-v6-next-hop-1 term 1 from family inet6
    set policy-options policy-statement set-v6-next-hop-1 term 1 then next-hop 2600:2d00:0:2::2
    set policy-options policy-statement set-v6-next-hop-1 term 1 then accept
    set policy-options policy-statement set-v6-next-hop-2 term 1 from family inet6
    set policy-options policy-statement set-v6-next-hop-2 term 1 then next-hop 2600:2d00:0:2::1:2
    set policy-options policy-statement set-v6-next-hop-2 term 1 then accept
    

  6. Configure BGP for IPv6 route exchange.

When configuring BGP, you must specify `include-mp-next-hop` statements to send the next hop attribute to the peer.

Then you export the policy statement that you defined in the previous step to change the next hop to the IPv6 address.
         
         set protocols bgp group vpn family inet unicast
         set protocols bgp group vpn family inet6 unicast
         set protocols bgp group vpn peer-as ROUTER_ASN
         set protocols bgp group vpn neighbor ROUTER_BGP_IP_1 export set-v6-next-hop-1
         set protocols bgp group vpn neighbor ROUTER_BGP_IP_1 local-as PEER_ASN
         set protocols bgp group vpn neighbor ROUTER_BGP_IP_1 graceful-restart restart-time 120
         set protocols bgp group vpn neighbor ROUTER_BGP_IP_1 include-mp-next-hop
         set protocols bgp group vpn2 type external
         set protocols bgp group vpn2 local-address ROUTER_IP_2
         set protocols bgp group vpn2 family inet unicast
         set protocols bgp group vpn2 family inet6 unicast
         set protocols bgp group vpn2 peer-as ROUTER_ASN
         set protocols bgp group vpn2 neighbor ROUTER_BGP_IP_2 export set-v6-next-hop-2
         set protocols bgp group vpn2 neighbor ROUTER_BGP_IP_2 local-as PEER_ASN
         set protocols bgp group vpn2 neighbor ROUTER_BGP_IP_2 graceful-restart restart-time 120
         set protocols bgp group vpn2 neighbor ROUTER_BGP_IP_2 include-mp-next-hop
         

Replace the following values:

     * `ROUTER_BGP_IP_1`: the IPv4 address assigned to the Cloud Router for the first tunnel
     * `ROUTER_BGP_IP_2`: the IPv4 address assigned to the Cloud Router for the second tunnel
     * `ROUTER_ASN`: the ASN assigned to the Cloud Router for your BGP sessions.
     * `PEER_ASN`: The ASN you assigned to the BGP peer, which is your Juniper JunOS device.

The following example shows the `include-mp-next-hop` and `export` statements in bold text: 
    
    set protocols bgp group vpn family inet unicast
    **set protocols bgp group vpn family inet6 unicast**
    set protocols bgp group vpn peer-as 16550
    **set protocols bgp group vpn neighbor 169.254.0.1 export set-v6-next-hop-1**
    set protocols bgp group vpn neighbor 169.254.0.1 local-as 65010
    set protocols bgp group vpn neighbor 169.254.0.1 graceful-restart restart-time 120
    **set protocols bgp group vpn neighbor 169.254.0.1 include-mp-next-hop**
    set protocols bgp group vpn2 type external
    set protocols bgp group vpn2 local-address 169.254.1.2
    set protocols bgp group vpn2 family inet unicast
    set protocols bgp group vpn2 family inet6 unicast
    set protocols bgp group vpn2 peer-as 16550
    **set protocols bgp group vpn2 neighbor 169.254.1.1 export set-v6-next-hop-2**
    set protocols bgp group vpn2 neighbor 169.254.1.1 local-as 65010
    set protocols bgp group vpn2 neighbor 169.254.1.1 graceful-restart restart-time 120
    **set protocols bgp group vpn2 neighbor 169.254.1.1 include-mp-next-hop**
    

  7. Verify BGP connectivity.
         
         show route protocol bgp
         




## Palo Alto Networks PAN-OS

This section describes how to set up your Palo Alto Networks PAN-OS device to support IPv4 and IPv6 traffic in your HA VPN tunnels.

PAN-OS supports the transport of IPv6 traffic over IPv4. However, PAN-OS does not support dual-stack address families. As a result, you must set up separate VPN tunnels that carry either IPv4 traffic or IPv6 traffic.

**Note:** The following instructions reflect PAN-OS 9.1.

For more information about configuring PAN-OS devices for use with VPN, see [ Palo Alto PAN OS VPN documentation](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/vpns).

### Before you begin

In Google Cloud, set up two HA VPN gateways and four HA VPN tunnels. Two tunnels are for IPv6 traffic and two tunnels are for IPv4 traffic.

  1. Create the [HA VPN gateway and tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn) for IPv4 traffic. Create the following:

     * One HA VPN gateway that uses the IPv4-only stack type
     * Two VPN tunnels that can carry IPv4 traffic
  2. Create the [HA VPN gateway and tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn) for IPv6 traffic. Create the following:

     * One HA VPN gateway that uses the dual-stack stack type
     * Two VPN tunnels that can carry IPv6 traffic
     * Enable IPv6 in the BGP sessions for the IPv6 tunnels
  3. Record the external IPv4 addresses that Google Cloud assigns to each HA VPN gateway interface.

  4. Record the following configuration values for each tunnel:

     * The link-local IPv4 address of the BGP peer, which is the PAN-OS side of the BGP session
     * The link-local IPv4 address of the Cloud Router used for BGP peering
     * The ASN you assigned to the BGP peer, which is your PAN-OS device
     * The ASN you assigned to the Cloud Router for your BGP sessions
     * The pre-shared key
  5. For each IPv6 tunnel, also record the `peerIpv6NexthopAddress`, which is the IPv6 next hop address assigned to the BGP peer. Google Cloud might have automatically assigned this address for you, or you might have manually specified the addresses when you created the VPN tunnel.




To find the details for your BGP session configuration, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

### Configure PAN-OS

To configure your Palo Alto Networks device, perform the following steps in the PAN-OS Web Interface.

  1. Enable IPv6 firewalling.

  2. Select **Device** > **Setup** > **Session Settings**.

     1. Select **Enable IPv6 firewalling**.
  3. Create a loopback interface for IPv4 and IPv6.

     1. Select **Network** > **Interfaces** > **Loopback interface** and create a new loopback interface.
     2. Create a loopback interface. For example, `loopback.10`.
     3. On the **Config** tab, set **Virtual Router** to `external` and set **Security Zone** to `ZONE_EXTERNAL`.
     4. On the **IPv4** tab, assign the loopback interface with IPv4 address ranges that are appropriate for your on-premises network.
     5. On the **IPv6** tab, select **Enable IPv6 on the interface** , and add an IPv6 address range appropriate for your on-premises network.
     6. On the **Advanced** tab, specify a **Management Profile** for the loopback interface. Make sure that the profile that you specify allows ping so you can verify connectivity.
  4. Create four IKE gateway tunnels, two tunnels for IPv6 traffic and two tunnels for IPv4 traffic. Each tunnel connects to an interface on a HA VPN gateway.

     * Create two tunnels for IPv6 traffic. 
       1. Select **Network** > **Interfaces** > **Tunnel** and create a new tunnel.
       2. Specify a name for the first tunnel. For example, `tunnel.1`.
       3. On the **Config** tab, set **Virtual Router** to `external` and set **Security Zone** to `ZONE_EXTERNAL`.
       4. On the **IPv4** tab, specify the link-local address of the BGP peer that you set up when creating the VPN tunnels for the HA VPN. For example, `169.254.0.2/30`.
       5. On the **IPv6** tab, select **Enable IPv6 on the interface** , and specify the IPv6 next hop address configured for the BGP peer. For example, `2600:2D00:0:2::2/125`.
       6. On the **Advanced** tab, set **MTU** to `1460`.
       7. Repeat this procedure for the second tunnel. For example, `tunnel.2`. On the **IPv4** and **IPv6** tabs, specify appropriate values for the BGP peer and IPv6 next hop fields. Use the values that match the second tunnel of the dual-stack HA VPN. For example, `169.254.1.2/30` and `2600:2D00:0:3::3/125`.
     * Create two tunnels for IPv4 traffic. 
       1. Select **Network** > **Interfaces** > **Tunnel** and create a new tunnel.
       2. Specify a name for the third tunnel. For example, `tunnel.3`.
       3. On the **Config** tab, set **Virtual Router** to `external` and set **Security Zone** to `ZONE_EXTERNAL`.
       4. On the **IPv4** tab, specify the link-local address of the BGP peer that you set up when creating the VPN tunnels for the HA VPN. For example, `169.254.2.2/30`.
       5. Skip the **IPv6** tab configuration.
       6. On the **Advanced** tab, set **MTU** to `1460`.
       7. Repeat this procedure for the fourth tunnel. For example, `tunnel.4`. On the **IPv4** tab, specify appropriate values for the BGP peer that match the second tunnel of the IPv4-only HA VPN. For example, `169.254.3.2/30`.
  5. Create an IPsec crypto profile.

     1. Select **Network** > **IPSec Crypto** and create a new profile.
     2. Enter values for the following fields: 
        * **Name** : Enter a profile name. For example, `ha-vpn`.
        * **IPSec Protocol** : Select **ESP**.
        * **Encryption** : Add a [supported IKE cipher](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers).
        * **Authentication** : Specify a hash function. For example, `sha512`.
        * **DH group** : Select a DH group. For example, **group14**.
        * **Lifetime** : Select **Hours** and enter `3`.
     3. Click **OK**.
  6. Create an IKE crypto profile.

     1. Select **Network** > **IKE Crypto**.
     2. Enter values for the following fields: 
        * **Name** : Enter a profile name. For example, `ha-vpn`.
        * **DH group** : Verify that the DH group that you selected for the IPsec Crypto profile appears in the list.
        * **Authentication** : Specify a hash function. For example, `sha512`.
        * **Encryption** : Add a [supported IKE cipher](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers).
     3. In the **Timers** pane, select **Hours** for **Key Lifetime** and enter `10`.
     4. Click **OK**.
  7. After you create four IKE tunnels, create four IKE gateways, one for each tunnel.

     1. Select **Network** > **IKE Gateways** , and create a new gateway.
     2. On the **General** tab, enter values for the following fields: 
        * **Name** : Name of the IKE gateway for the first tunnel. For example, `havpn-v6-tunnel1`.
        * **Version** : Select `IKEv2 only mode`.
        * **Address type** : Select `IPv4`.
        * **Interface** : Specify the loopback interface that you created at the beginning of this procedure. For example, `loopback.10`.
        * **Local IP Address** : Specify an IPv4 address range appropriate for your on-premises network.
        * **Peer IP Address Type** : Select `IP`.
        * **Peer Address** : Specify the external IPv4 address of the first HA VPN interface for the tunnel.
        * **Authentication** : Select `Pre-Shared Key`.
        * **Pre-shared Key** , **Confirm Pre-Shared Key** : Enter the shared secret you configured in Google Cloud for the tunnel.
        * **Local Identification** : Select **IP address** , and specify an IPv4 address appropriate for your on-premises network.
        * **Peer Identification** : Select **IP address** , and the external IPv4 address of the HA VPN interface for the tunnel.
     3. Select the **Advanced Options** tab.
     4. For the **IKE Crypto Profile** , select the profile that you created previously. For example, `ha-vpn`.
     5. Enable **Liveness Check** and enter `5` for the **Interval (sec)**.
     6. Click **OK**.
     7. Repeat this procedure for the other three tunnels, but substitute appropriate values for the following fields: 
        * **Name** : Name of the IKE gateway for the tunnel. For example, `havpn-v6-tunnel2`, `havpn-v4-tunnel1`, or `havpn-v4-tunnel2`.
        * **Local IP Address** / **Local Identification** : Specify an unused IPv4 address appropriate for your on-premises network.
        * **Peer Address** / **Peer Identification** : Specify the external IPv4 address for the matching HA VPN interface of the tunnel.
        * **Pre-shared Key** : Specify the shared secret configured for the tunnel.
  8. Create four IPsec tunnels.

     1. Select **Network** > **IPSec Tunnels** and create a new tunnel.
     2. Enter values for the following fields: 
        * **Name** : Unique name for the tunnel. For example, `hapvpn-tunnel-1`.
        * **Tunnel Interface** : Select a tunnel interface for the IKE gateway tunnel that you created earlier. For example, `tunnel.1`.
        * **Type** : Select **Auto Key**.
        * **Address Type** : Select **IPv4**.
        * **IKE Gateway** : Select one of the IKE Gateways that you created earlier. For example, `havpn-v6-tunnel`.
        * **IPSec Crypto Profile** : Select the profile that you created earlier. For example, `ha-vpn`.
     3. Don't configure **Proxy IDs**.
     4. Click **OK**.
     5. Repeat this procedure for the other three tunnels, but substitute appropriate values for the following fields: 
        * **Name** : Unique name for the IPsec tunnel. For example, `havpn-tunnel2`, `havpn-tunnel3`, or `havpn-tunnel4`.
        * **Tunnel Interface** : Select an unused tunnel interface for the IKE gateway tunnel that you created earlier. For example, `tunnel.2`, `tunnel.3` or `tunnel.4`.
        * **IKE Gateway** : Select one of the IKE Gateways that you created earlier. For example, `havpn-v6-tunnel2`, `havpn-v4-tunnel1`, or `havpn-v4-tunnel2`.
  9. Optional: Configure ECMP.

     1. Select **Network** > **Virtual Routers** > **ROUTER_NAME** > **Router Settings** > **ECMP**.
     2. On the **ECMP** tab, select **Enable**.
     3. Click **OK**.
  10. Configure BGP.

     1. Select **Network** > **Virtual Routers** > **ROUTER_NAME** > **Router Settings** > **BGP**.
     2. On the **General** tab, select **Enable**.
     3. On the **Router ID** field, enter the link-local IPv4 address assigned to the BGP peer, which is the PAN-OS side of the BGP session. peer.
     4. In the **AS Number** field, enter the ASN for the PAN-OS side of the BGP session.
     5. For **Options** , make sure **Install Route** is selected.
     6. Click **OK**.
  11. Create a BGP peer group with one BGP peer for each IPv6 tunnel. You create a separate BGP peer group for each IPv6 tunnel so you can configure a different IPv6 next hop address per tunnel.

     1. Select **Network** > **Virtual Routers** > **ROUTER_NAME** > **Router Settings** > **BGP** > **Peer Group**.
     2. On the **Peer Group** tab, create a new peer group for the first IPv6 tunnel.
     3. In the **Name** field, enter a name for the peer group. For example, `havpn-bgp-v6-tunnel1`.
     4. Select **Enable**.
     5. Select **Aggregated Confed AS Path**.
     6. In the **Type** list, select **EBGP**.
     7. For **Import Next Hop** , select **Original**.
     8. For **Export Next Hop** , select **Resolve**.
     9. Select **Remove Private AS**.
     10. In the **Peer** pane, click ![](https://docs.cloud.google.com/static/style/images/icon-add.png)**Add** to add a peer to the BGP peer group.
     11. In the **Peer** dialog, enter the following values: 
        * **Name** : Name for the peer. For example, `havpn-v6-tunnel1`.
        * Select **Enable**.
        * **Peer AS** : The ASN assigned to the Cloud Router for the BGP session.
        * On the **Addressing** tab, configure the following options: 
          * Select **Enable MP-BGP Extensions**.
          * For **Address Family Type** , select **IPv6**.
          * In **Local Address** , for **Interface** select the first tunnel that you defined when creating the IKE gateway tunnels. For example, `tunnel.1`.
          * For **IP** , select the link-local IPv4 address of the BGP peer. For example, `169.254.0.2./30`.
          * In **Peer Address** , for **Type** select **IP**.
          * For **Address** , select the link-local IPv4 address of the Cloud Router for this BGP session. For example, `169.254.0.1`.
        * Click **OK**.
     12. After you finish adding the peer, click **OK**.
     13. Repeat this procedure for the other IPv6 tunnel, but substitute appropriate values for the following fields: 
        * **Name** : Unique name for the BGP peer group. For example, `havpn-bgp-v6-tunnel2`.
        * In the **Peer** dialog, enter appropriate values for the tunnel in the following fields: 
          * **Name** : Name for the peer. For example, `havpn-v6-tunnel1`.
          * In **Local Address** , for **Interface** select the second tunnel that you defined when creating the IKE gateway tunnels. For example, `tunnel.2`.
          * For **IP** , select the link-local IPv4 address of the BGP peer for the second tunnel. For example, `169.254.1.2./30`.
          * In **Peer Address** , for **Address** , select the link-local IPv4 address of the Cloud Router for this BGP session. For example, `169.254.1.1`.
  12. Create a BGP peer group for the IPv4 tunnels.

     1. Select **Network** > **Virtual Routers** > **ROUTER_NAME** > **Router Settings** > **BGP** > **Peer Group**.
     2. On the **Peer Group** tab, create a new peer group for the IPv4 tunnel.
     3. In the **Name** field, enter a name for the peer group. For example, `havpn-bgp-v4`.
     4. Select **Enable**.
     5. Select **Aggregated Confed AS Path**.
     6. In the **Type** list, select **EBGP**.
     7. For **Import Next Hop** , select **Original**.
     8. For **Export Next Hop** , select **Resolve**.
     9. Select **Remove Private AS**.
     10. In the **Peer** pane, click ![](https://docs.cloud.google.com/static/style/images/icon-add.png)**Add** to add a peer to the BGP peer group.
     11. In the **Peer** dialog, enter the following values: 
        * **Name** : Enter a name for the peer. For example, `havpn-v4-tunnel1`.
        * Select **Enable**.
        * **Peer AS** : The ASN assigned to the Cloud Router for the BGP session.
        * On the **Addressing** tab, configure the following options: 
          * Don't select **Enable MP-BGP Extensions**.
          * For **Address Family Type** , select `IPv4`.
          * In **Local Address** , for **Interface** select the third tunnel that you defined when creating the IKE gateway tunnels. For example, `tunnel.3`.
          * For **IP** , select the link-local IPv4 address of the BGP peer. For example, `169.254.2.2./30`.
          * In **Peer Address** , select `IP` for **Type**.
          * For **Address** , select the link-local IPv4 address of the Cloud Router for this BGP session. For example, `169.254.2.1`.
        * Click **OK**.
     12. In the **Peer** pane, click ![](https://docs.cloud.google.com/static/style/images/icon-add.png)**Add** to add the second peer to the BGP peer group.
     13. In the **Peer** dialog, enter the following values: 
        * **Name** : Enter a name for the peer. For example, `havpn-v4-tunnel2`.
        * Select **Enable**.
        * **Peer AS** : The ASN assigned to the Cloud Router for the BGP session.
        * On the **Addressing** tab, configure the following options: 
          * Don't select **Enable MP-BGP Extensions**.
          * For **Address Family Type** , select **IPv4**.
          * In **Local Address** , for **Interface** select the fourth tunnel that you defined when creating the IKE gateway tunnels. For example, `tunnel.4`.
          * For **IP** , select the link-local IPv4 address of the BGP peer. For example, `169.254.3.2./30`.
          * In **Peer Address** , for **Type** select **IP**.
          * For **Address** , select the link-local IPv4 address of the Cloud Router for this BGP session. For example, `169.254.3.1`.
     14. Click **OK**.
     15. After you finish adding both peers, click **OK**.
  13. Export BGP configuration rules to the BGP peer groups for the IPv6 tunnels. This step lets you assign different IPv6 next hop addresses to the tunnels.

     1. Select **Network** > **Virtual Routers** > **ROUTER_NAME** > **Router Settings** > **BGP** > **Export**.
     2. In the **Export Rule** dialog, enter a name in the **Rules** field. For example, `havpn-tunnel1-v6`.
     3. Select **Enable**.
     4. In the **Used By** pane, click ![](https://docs.cloud.google.com/static/style/images/icon-add.png)**Add** to add the BGP peer group you created for the first IPv6 tunnel. For example, `havpn-bgp-v6-tunnel1`.
     5. On the **Match** tab, select **Unicast** in the **Route Table** list.
     6. In **Address Prefix** , add the address prefix for the IPv6 addresses used in your on-premises network.
     7. On the **Action** tab, configure the following options: 
        * In the **Action** list, select **Allow**.
        * In the **Next Hop** , enter the IPv6 next hop address assigned to the BGP peer when you created the tunnel. For example, `2600:2D00:0:2::2`.
     8. Click **OK**.
     9. Repeat this procedure for the BGP peer group used by the second IPv6 tunnel, but substitute appropriate values for the following fields: 
        * In the **Export Rule** dialog, enter a unique name in the **Rules** field. For example, `havpn-tunnel2-v6`.
        * In the **Used By** pane, click ![](https://docs.cloud.google.com/static/style/images/icon-add.png)**Add** to add the BGP peer group you created for the second IPv6 tunnel. For example, `havpn-bgp-v6-tunnel1`.
     10. On the **Action** tab, configure the **Next Hop** field, enter the IPv6 next hop address assigned to the BGP peer for this tunnel. For example, `2600:2D00:0:3::3`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
