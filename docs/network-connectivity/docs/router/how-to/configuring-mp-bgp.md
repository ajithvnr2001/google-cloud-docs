---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp/
title: Configure multiprotocol BGP for IPv4 or IPv6 BGP sessions \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:13.881677+00:00
---

# Configure multiprotocol BGP for IPv4 or IPv6 BGP sessions  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure multiprotocol BGP for IPv4 or IPv6 BGP sessions 

Cloud Router lets you enable and disable IPv4 or IPv6 route exchange in individual Border Gateway Protocol (BGP) sessions that use multiprotocol BGP (MP-BGP). With MP-BGP, you can exchange IPv6 routes over an IPv4 BGP session or IPv4 routes over an IPv6 BGP session.

To exchange both IPv4 and IPv6 traffic in a single BGP session, you must select the IPv4 and IPv6 (dual stack) stack type in your Network Connectivity product, such as HA VPN or Dedicated Interconnect.

You can enable or disable IPv4 or IPv6 route exchange in a specific BGP session by modifying the configuration of the BGP peer. Disabling IPv4 or IPv6 route exchange is useful if you need to troubleshoot IPv4- or IPv6-specific network issues. Another reason might be that you want to disable traffic temporarily in a dual-stack HA VPN tunnel without deleting the tunnel and gateway.

If you disable IPv4 or IPv6 route exchange in a BGP session and then later re-enable it, IPv4 or IPv6 next hop addresses that were previously assigned are not relinquished. You can reuse those IPv4 or IPv6 next hop addresses if IPv4 or IPv6 is enabled in the BGP session again.

## Before you begin

###  gcloud 

If you want to use the command-line examples in this guide, do the following:

  1. Install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
  2. Set a [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



###  API 

If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/compute/docs/api/prereqs).

## Configure an IPv4 BGP session

This section describes how to modify the configuration of an IPv4 BGP session.

You cannot disable IPv4 route exchange in an IPv4 BGP session.

### Enable IPv6 route exchange over an IPv4 session

This procedure assumes that you are modifying IPv4 BGP sessions that have already been created for HA VPN tunnels or VLAN attachments for Cloud Interconnect.

It also assumes that you have configured the associated HA VPN gateway or VLAN attachment to use the IPv4 and IPv6 (dual stack) stack type as described in the following procedures:

  * [Create an HA VPN to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn)
  * [Create HA VPN gateways to connect VPC networks](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2)
  * [Create VLAN attachments Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)



To enable IPv6 route exchange in an existing IPv4 BGP session, perform the following steps.

###  Console 

**For HA VPN**

  1. To configure a BGP session for HA VPN, in the Google Cloud console, go to the **Cloud VPN tunnels** page.

[Go to Cloud VPN tunnels](https://console.cloud.google.com/hybrid/vpn/list)

  2. Select the Cloud VPN tunnel that contains the BGP session to update.

  3. On the **VPN tunnel details** page, click **Edit BGP session**.

  4. In the **Multiprotocol BGP** section, click the **Enable IPv6 traffic** toggle to the on position.

  5. Optional: You can allocate the IPv6 BGP addresses for HA VPN tunnels manually or automatically.

     * To allocate the addresses automatically, select **Automatically**.
     * To allocate the addresses manually: 
       1. Enter the IPv6 address for the **Cloud Router BGP IPv6 next hop** field. This address is an IPv6 address used by Cloud Router for this Cloud VPN tunnel. This IPv6 address is advertised as the next hop for the IPv6 routes that Cloud Router advertises to its BGP peer. The address must be in the range `2600:2d00:0:2::/63`.
       2. Enter the IPv6 address for the **Peer BGP IPv6 next hop** field. This address is the IPv6 address of the on-premises router or peer VPN device. This IPv6 address is the next hop for the IPv6 routes learned from the BGP peer of Cloud Router. The address must be in the range `2600:2d00:0:2::/63`.
  6. Click **Save and continue**.




**For Dedicated Interconnect**

  1. To configure a BGP session for Dedicated Interconnect, go to the **VLAN attachments** page.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list)

  2. Select the VLAN attachment that contains the BGP session to update.

  3. On the **VLAN attachment details** page, click **Edit BGP session**.

  4. In the **Multiprotocol BGP** section, click the **Enable IPv6 traffic** toggle to the on position.

  5. Click **Save and continue**.


**Note:** You cannot change IPv6 next-hop configuration in Cloud Interconnect. Google Cloud automatically assigns IPv6 next hop addresses to VLAN attachments.

###  gcloud 

Run the `update-bgp-peer` command. Use the `--enable-ipv6` flag to allow the BGP session to exchange IPv6 routes, as shown in the following example:
    
    
    gcloud compute routers update-bgp-peer ROUTER_NAME \
        --peer-name=PEER_NAME \
        --enable-ipv6
    

Optionally, when you enable IPv6 traffic for a BGP session used in an HA VPN tunnel, you can specify IPv6 next hop addresses:
    
    
    gcloud compute routers update-bgp-peer ROUTER_NAME \
        --peer-name=PEER_NAME \
        --enable-ipv6 \
        --ipv6-nexthop-address=IPV6_NEXTHOP_ADDRESS \
        --peer-ipv6-nexthop-address=PEER_IPV6_NEXTHOP_ADDRESS
    

Replace the following:

  * `IPV6_NEXTHOP_ADDRESS`: the IPv6 address used by Cloud Router for this Cloud VPN tunnel. This IPv6 address is advertised as the next hop for the IPv6 routes that Cloud Router advertises to its BGP peer.

The address must be in the IPv6 range `2600:2d00:0:2::/63`.

  * `PEER_IPV6_NEXTHOP_ADDRESS`: the IPv6 address of the on-premises router. This IPv6 address is the next hop for the IPv6 routes learned from the BGP peer of the Cloud Router. The address must be in the range `2600:2d00:0:2::/63`.




If you don't specify the next hop addresses, Google Cloud automatically assigns unused addresses from the `2600:2d00:0:2::/63` IPv6 range for you.

###  API 

Use the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. For each BGP peer for which you want to enable IPv6 in the BGP session, set `bgpPeers[].enableIpv6` to `TRUE`.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "bgpPeers": [
             BGP_PEERS
           ]
         }
         

Replace the following:

     * `PROJECT_ID`: the project that contains the Cloud Router
     * `REGION`: the region where the Cloud Router is located
     * `ROUTER_NAME`: the name of the Cloud Router
     * `BGP_PEERS`: the contents of the new array of BGP peers

The following example enables IPv6 in the session for the first BGP peer:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          **"enableIpv6" : true**
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          "enableIpv6": false
          "
        }
     

Additionally, if you are enabling IPv6 traffic for a BGP session used in an HA VPN tunnel, you can specify IPv6 next hop addresses:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          **"enableIpv6" : true**,
          **"ipv6NexthopAddress" : "2600:2d00:0:2:0:0:1:5"**,
          **"peerIpv6NexthopAddress" : "2600:2d00:0:2:0:0:1:6"**
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          "enableIpv6": false
        }

Use the values of `ipv6NexthopAddress` and `peerIpv6NexthopAddress` to configure your on-premises router or peer VPN device.

To view example configurations for HA VPN and your peer VPN device, see [Set up third-party VPNs for IPv4 and IPv6 traffic](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides-ipv6).

To view example configurations for Dedicated Interconnect and your on-premises router, see [Set up on-premises routers for IPv4 and IPv6 traffic](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers#set-up-on-premises-routers-for-ipv4-and-ipv6-traffic).




### Disable IPv6 route exchange over an IPv4 BGP session

This procedure assumes that you are modifying an existing IPv4 BGP session that previously enabled IPv6.

###  Console 

**For HA VPN**

  1. In the Google Cloud console, go to the **Cloud VPN tunnels** page.

[Go to Cloud VPN tunnels](https://console.cloud.google.com/hybrid/vpn/list)

  2. Select the Cloud VPN tunnel that contains the BGP session to update.

  3. On the **VPN tunnel details** page, click **Edit BGP session**.

  4. To disable IPv6 route exchange, click the **Enable IPv6 traffic** toggle to the off position.

  5. Click **Save and continue**.




**For Dedicated Interconnect**

  1. In the Google Cloud console, go to the **VLAN attachments** page.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list)

  2. Select the VLAN attachment that contains the BGP session to update.

  3. On the **VLAN attachment details** page, click **Edit BGP session**.

  4. To disable IPv6 route exchange, click the **Enable IPv6 traffic** toggle to the off position.

  5. Click **Save and continue**.




###  gcloud 

Run the update-bgp-peer command. Use the --no-enable-ipv6 flag to prevent the BGP session from exchanging IPv6 routes, as shown in the following example:
    
    
    gcloud compute routers update-bgp-peer ROUTER_NAME \
    --peer-name=PEER_NAME \
    --no-enable-ipv6
    

###  API 

Use the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. For each BGP peer for which you want to disable IPv6 in the BGP session, set `bgpPeers[].enableIpv6` to `FALSE`.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "bgpPeers": [
             BGP_PEERS
           ]
         }
         

Replace the following:

     * `PROJECT_ID`: the project that contains the Cloud Router
     * `REGION`: the region where the Cloud Router is located
     * `ROUTER_NAME`: the name of the Cloud Router
     * `BGP_PEERS`: the contents of the new array of BGP peers

The following example disables IPv6 in the session for the first BGP peer:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          **"enableIpv6" : false**
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          "enableIpv6": false
        }




## Configure an IPv6 BGP session

This section describes how to modify the configuration of an IPv6 BGP session.

You cannot disable IPv6 route exchange in an IPv6 BGP session.

### Enable IPv4 route exchange over an IPv6 BGP session

This procedure assumes that you are modifying IPv6 BGP sessions that have already been created for HA VPN tunnels or VLAN attachments.

It also assumes that you have already configured an IPv4 and IPv6 (dual stack) HA VPN gateway or VLAN attachment as described in the following procedures:

  * [Create an HA VPN to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn)
  * [Create HA VPN gateways to connect VPC networks](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2)
  * [Create VLAN attachments (Dedicated Interconnect)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)



To enable IPv4 route exchange in an existing IPv6 BGP session, perform the following steps.

###  Console 

**For HA VPN**

  1. To configure a BGP session for HA VPN, in the Google Cloud console, go to the **Cloud VPN tunnels** page.

[Go to Cloud VPN tunnels](https://console.cloud.google.com/hybrid/vpn/list)

  2. Select the Cloud VPN tunnel that contains the BGP session to update.

  3. On the **VPN tunnel details** page, click **Edit BGP sessions**.

  4. In the **Multiprotocol BGP** section, click the **Enable IPv4 traffic** toggle to the on position.

  5. Optional: You can allocate the IPv6 BGP addresses for HA VPN tunnels manually or automatically.

     * To allocate the addresses automatically, select **Automatically**.
     * To allocate the addresses manually: 
       1. Select **Manually**.
       2. Enter the IPv6 address for the **Cloud Router BGP IPv6 address** field. This address is an IPv6 address used by Cloud Router for this Cloud VPN tunnel. This IPv6 address is advertised as the next hop for the IPv6 routes that Cloud Router advertises to its BGP peer. The address must be in the range `2600:2d00:0:2::/63`.
       3. Enter the IPv6 address for the **BGP peer IPv6 address** field. This address is the IPv6 address of the on-premises router or peer VPN device. This IPv6 address is the next hop for the IPv6 routes learned from the BGP peer of Cloud Router. The address must be in the range `2600:2d00:0:2::/63`.
  6. Optional: You can allocate the Cloud Router BGP IPv4 next hop addresses for HA VPN tunnels manually or automatically.

     * To allocate the addresses automatically, select **Automatically**.
     * To allocate the addresses manually: 
       1. Select **Manually**.
       2. Enter the IPv4 address for the **Cloud Router BGP IPv4 next hop** field. This address is an IPv4 address used by Cloud Router for this Cloud VPN tunnel. This IPv4 address is advertised as the next hop for the IPv4 routes that Cloud Router advertises to its BGP peer. The address must be a link-local address within the same `/30` subnet as the BGP peer IPv4 address.
       3. Enter the IPv4 address for the **Peer BGP IPv4 next hop** field. This address is the IPv4 address of the on-premises router or peer VPN device. This IPv4 address is the next hop for the IPv6 routes learned from the BGP peer of Cloud Router. The address must be a link-local address within the same `/30` subnet as the Cloud Router BGP IPv4 address.
  7. Click **Save and continue**.




**For Dedicated Interconnect**

  1. To configure a BGP session for Dedicated Interconnect, go to the **VLAN attachments** page.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list)

  2. Select the VLAN attachment that contains the BGP session to update.

  3. On the **VLAN attachment details** page, click **Edit BGP session**.

  4. In the **Multiprotocol BGP** section, click the **Enable IPv4 traffic** toggle to the on position.

  5. Click **Save and continue**.


**Note:** You cannot the change IPv6 next-hop configuration in Cloud Interconnect. Google Cloud automatically assigns IPv6 next hop addresses to VLAN attachments.

###  gcloud 

Run the `update-bgp-peer` command. Use the `--enable-ipv4` flag to allow the BGP session to exchange IPv4 routes, as shown in the following example:
    
    
    gcloud compute routers update-bgp-peer ROUTER_NAME \
        --peer-name=PEER_NAME \
        --enable-ipv4
    

Optionally, when you enable IPv4 traffic for an IPv6 BGP session used in an HA VPN tunnel, you can specify the IPv4 next hop addresses:
    
    
    gcloud compute routers update-bgp-peer ROUTER_NAME \
        --peer-name=PEER_NAME \
        --enable-ipv4 \
        --ipv4-nexthop-address=IPV4_NEXTHOP_ADDRESS \
        --peer-ipv4-nexthop-address=PEER_IPV4_NEXTHOP_ADDRESS
    

Replace the following:

  * `IPV4_NEXTHOP_ADDRESS`: the IPv4 address used by Cloud Router for this HA VPN tunnel. This IPv4 address is advertised as the next hop for the IPv4 routes that Cloud Router advertises to its BGP peer. The address must be in the IPv4 link-local range `169.254.0.0/16`.
  * `PEER_IPV4_NEXTHOP_ADDRESS`: the IPv4 address of the on-premises router. This IPv4 address is the next hop for the IPv4 routes learned from the BGP peer of Cloud Router. The address must be in the IPv4 link-local range `169.254.0.0/16`.

If you don't specify the next-hop addresses, Google Cloud automatically assigns unused addresses from the IPv4 link-local `169.254.0.0/16` range for you.




###  API 

Use the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. For each BGP peer for which you want to enable IPv4 in the BGP session, set `bgpPeers[].enableIpv4` to `TRUE`.
         
         PATCH https://compute.googleapis.com/compute/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "bgpPeers": [
             BGP_PEERS
           ]
         }
         

Replace the following:

     * `PROJECT_ID`: the project that contains the Cloud Router
     * `REGION`: the region where the Cloud Router is located
     * `ROUTER_NAME`: the name of the Cloud Router
     * `BGP_PEERS`: the contents of the new array of BGP peers

The following example enables IPv4 in the session for the first BGP peer:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "fdff:1::1",
          "peerIpAddress": "fdff:1::2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          **"enableIpv4" : true**
    
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "fdff:1::3",
          "peerIpAddress": "fdff:1::4",
          "peerAsn": 64513,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          "enableIpv4": false
        }
     

Additionally, if you are enabling IPv4 traffic for a BGP session used in an HA VPN tunnel, you can specify IPv4 next hop addresses:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "fdff:1::1",
          "peerIpAddress": "fdff:1::2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          **"enableIpv4" : true**,
          **"ipv4NexthopAddress" : "169.254.0.1"**,
          **"peerIpv4NexthopAddress" : "169.254.0.2"**
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "fdff:1::3",
          "peerIpAddress": "fdff:1::4",
          "peerAsn": 64513,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          "enableIpv4": false
        }




### Disable IPv4 route exchange over an IPv6 BGP session

This procedure assumes that you are modifying an existing IPv6 BGP session that previously exchanged IPv4 routes.

###  Console 

**For HA VPN**

  1. In the Google Cloud console, go to the **Cloud VPN tunnels** page.

[Go to Cloud VPN tunnels](https://console.cloud.google.com/hybrid/vpn/list)

  2. Select the Cloud VPN tunnel that contains the BGP session to update.

  3. On the **VPN tunnel details** page, click **Edit BGP session**.

  4. In the **Multiprotocol BGP** section, click the **Enable IPv4 traffic** toggle to the off position.

  5. Click **Save and continue**.




**For Dedicated Interconnect**

  1. In the Google Cloud console, go to the **VLAN attachments** page.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list)

  2. Select the VLAN attachment that contains the BGP session to update.

  3. On the **VLAN attachment details** page, click **Edit BGP sessions**.

  4. In the **Multiprotocol BGP** section, click the **Enable IPv4 traffic** toggle to the off position.

  5. Click **Save and continue**.




###  gcloud 

Run the `update-bgp-peer` command. Use the `--no-enable-ipv4` flag to prevent the IPv6 BGP session from exchanging IPv4 routes, as shown in the following example:
    
    
    gcloud compute routers update-bgp-peer ROUTER_NAME \
        --peer-name=PEER_NAME \
        --no-enable-ipv4
    

###  API 

Use the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. For each BGP peer for which you want to disable IPv4 in the BGP session, set `bgpPeers[].enableIpv4` to `FALSE`.
         
         PATCH https://compute.googleapis.com/compute/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "bgpPeers": [
             BGP_PEERS
           ]
         }
         

Replace the following:

     * `PROJECT_ID`: the project that contains the Cloud Router
     * `REGION`: the region where the Cloud Router is located
     * `ROUTER_NAME`: the name of the Cloud Router
     * `BGP_PEERS`: the contents of the new array of BGP peers

The following example disables IPv4 in the session for the first BGP peer:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "fdff:1::1",
          "peerIpAddress": "fdff:1::2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          **"enableIpv4" : false**
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "fdff:1::3",
          "peerIpAddress": "fdff:1::4",
          "peerAsn": 64513,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          "enableIpv4": false
        }




## Separate an existing IPv4 MP-BGP session to use IPv4 and IPv6 BGP sessions

Existing Cloud Router IPv4 MP-BGP sessions use IPv4 control packets even when exchanging routing information about IPv6 BGP prefixes. IPv6-based BGP sessions are supported in networks with dual-stack subnets or with a mix of IPv4-only and IPv6-only subnets. This section describes how to modify an existing IPv4 MP-BGP session to use separate IPv4 and IPv6 BGP sessions.

###  Console 

**For HA VPN**

  1. To configure a BGP session for HA VPN, in the Google Cloud console, go to the **Cloud VPN tunnels** page.

[Go to Cloud VPN tunnels](https://console.cloud.google.com/hybrid/vpn/list)

  2. Find the Cloud VPN tunnel that contains the BGP session to update.

  3. On the **VPN tunnel details** page, click **Edit BGP sessions**.

  4. Select a BGP session type. To enable route exchange for IPv4 and IPv6 select **Both**.

  5. Optional: You can allocate the BGP IPv4 addresses for HA VPN tunnels manually or automatically.

     * To allocate the addresses automatically, select **Automatically**.
     * To allocate the addresses manually: 
       1. Select **Manually**.
       2. Enter the IPv4 address for the **Cloud Router BGP IPv4 address**. This address is an IPv4 address used by Cloud Router for this Cloud VPN tunnel. This IPv4 address is advertised as the next hop for the IPv4 routes that Cloud Router advertises to its BGP peer. The address must be a link-local address within the same `/30` subnet as the BGP peer IPv4 address.
       3. Enter the IPv4 address for the **BGP peer IPv4 address**. This address is the IPv4 address of the on-premises router or peer VPN device. This IPv4 address is the next hop for the IPv6 routes learned from the BGP peer of Cloud Router. The address must be a link-local address within the same `/30` subnet as the Cloud Router BGP IPv4 address.
  6. Optional: You can allocate the BGP IPv6 addresses for HA VPN tunnels manually or automatically.

     * To allocate the addresses automatically, select **Automatically**.
     * To allocate the addresses manually: 
       1. Select **Manually**.
       2. Enter the IPv6 address for the **Cloud Router BGP IPv6 address**. This address is an IPv6 address used by Cloud Router for this Cloud VPN tunnel. This IPv6 address is advertised as the next hop for the IPv6 routes that Cloud Router advertises to its BGP peer. The address must be in the range `fdff:1::/64`.
       3. Enter the IPv6 address for the **BGP peer IPv6 address**. This address is the IPv6 address of the on-premises router or peer VPN device. This IPv6 address is the next hop for the IPv6 routes learned from the BGP peer of Cloud Router. The address must be in the range `fdff:1::/64`.
  7. Click **Save and continue**.




**For Dedicated Interconnect**

  1. To configure a BGP session for Dedicated Interconnect, go to the **VLAN attachments** page.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list)

  2. Select the VLAN attachment that contains the BGP session to update.

  3. On the **VLAN attachment details** page, click **Edit BGP session**.

  4. Select a BGP session type. To enable route exchange for IPv4 and IPv6 select **Both**.

  5. In the **IPv4 BGP session** section, enter the ASN value for the on-premises side of the BGP session in **Peer ASN**.

  6. In the **IPv6 BGP session** section, enter the ASN value for the on-premises side of the BGP session in **Peer ASN**.

  7. Click **Save and continue**.


**Note:** You cannot change the IPv6 next-hop configuration in Cloud Interconnect. Google Cloud automatically assigns IPv6 next hop addresses to VLAN attachments.

###  gcloud 

  1. To avoid a conflict with the new IPv6 BGP, disable IPv6 route exchange on your existing IPv4 BGP session.

**Important:** Disabling IPv6 route exchange on your existing IPv4 BGP session causes IPv6 traffic to route away from your VLAN attachment and to backup paths until IPv6 BGP is established.

Run the following command:
         
         gcloud compute routers update-bgp-peer ROUTER_NAME
             --peer-name=PEER_NAME \
             --no-enable-ipv6
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router
     * `PEER_NAME`: the name of the BGP peer
  2. Add the new IPv6 interface:
         
         gcloud compute routers add-interface ROUTER_NAME \
             --interface-name=INTERFACE_NAME \
             --interconnect-attachment=ATTACHMENT_NAME \
             --ip-version=IPV6
         

Replace the following:

     * `INTERFACE_NAME`: the name of the interface
     * `ATTACHMENT_NAME`: the name of the VLAN attachment
  3. Add the new IPv6 BGP peer:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
             --peer-name=PEER_NAME \
             --interface=INTERFACE_NAME \
             --peer-asn=PEER_ASN
         

Replace the following:

     * `PEER_ASN`: the BGP peer's ASN
  4. To configure the on-premises BGP session, get the VLAN attachment's IPv6 address:
         
         gcloud compute interconnects attachments describe ATTACHMENT_NAME
         

The output is similar to the following:
         
         adminEnabled: true
         edgeAvailabilityDomain: AVAILABILITY_DOMAIN_1
         bandwidth: BPS_1G
         cloudRouterIpAddress: 169.254.67.201/29
         **cloudRouterIpv6Address : 2600:2d00:0:1::1/125**
         creationTimestamp: '2017-12-01T08:31:11.580-08:00'
         customerRouterIpAddress: 169.254.67.202/29
         **customerRouterIpv6Address : 2600:2d00:0:1::2/125**
         description: Interconnect for Customer 1
         id: '7193021941765913888'
         interconnect: https://www.googleapis.com/compute/projects/partner-project/global/interconnects/lga-2
         kind: compute#interconnectAttachment
         labelFingerprint: 42WmSpB8rSM=
         name: partner-attachment
         partnerMetadata:
           interconnectName: New York (2)
           partnerName: Partner Inc
           portalUrl: https://partner-portal.com
         region: https://www.googleapis.com/compute/projects/partner-project/regions/us-central1
         selfLink: https://www.googleapis.com/compute/projects/partner-project/regions/us-central1/interconnectAttachments/customer-attachment
         stackType: IPV4_IPV6
         state: ACTIVE
         type: PARTNER
         vlanTag8021q: 1000
         

The relevant IPv6 addresses are listed under `cloudRouterIPv6Address` and `customerRouterIpv6Address`.




###  API 

Use the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. For each BGP peer for which you want to enable IPv6 in the BGP session, set `bgpPeers[].enableIpv6` to `TRUE` and `bgpPeers[].enableIpv4` to `FALSE`.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "bgpPeers": [
             BGP_PEERS
           ]
         }
         

Replace the following:

     * `PROJECT_ID`: the project that contains the Cloud Router
     * `REGION`: the region where the Cloud Router is located
     * `ROUTER_NAME`: the name of the Cloud Router
     * `BGP_PEERS`: the contents of the new array of BGP peers

The following example enables IPv6 in the session for the first BGP peer:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          **"enableIpv6" : true**,
          **"enableIpv4" : false**
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          "enableIpv6": false
        }
     

Additionally, if you are enabling IPv6 traffic for a BGP session used in an HA VPN tunnel, you can specify IPv6 next hop addresses:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          **"enableIpv6" : true**,
          **"enableIpv4" : false**,
          **"ipv6NexthopAddress" : "2600:2d00:0:2:0:0:1:5"**,
          **"peerIpv6NexthopAddress" : "2600:2d00:0:2:0:0:1:6"**
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          "enableIpv6": false
        }

Use the values of `ipv6NexthopAddress` and `peerIpv6NexthopAddress` to configure your on-premises router or peer VPN device.

To view example configurations for HA VPN and your peer VPN device, see [Set up third-party VPNs for IPv4 and IPv6 traffic](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides-ipv6).

To view example configurations for Dedicated Interconnect and your on-premises router, see [Set up on-premises routers for IPv4 and IPv6 traffic](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers#set-up-on-premises-routers-for-ipv4-and-ipv6-traffic).




## Combine separate IPv4 and IPv6 BGP sessions onto a single IPv4 MP-BGP session

You can combine separate IPv4 and IPv6 BGP sessions into a single IPv4 MP-BGP session. In this case, IPv4 control packets are used to exchange routing information for both IPv4 and IPv6 BGP sessions. The following procedures describe how to convert separate IPv4 and IPv6 BGP sessions into a single IPv4 MP-BGP session:

###  Console 

**For HA VPN**

  1. To configure a BGP session for HA VPN, in the Google Cloud console, go to the **Cloud VPN tunnels** page.

[Go to Cloud VPN tunnels](https://console.cloud.google.com/hybrid/vpn/list)

  2. Find the Cloud VPN tunnel that contains the BGP session to update.

  3. On the **VPN tunnel details** page, click **Edit BGP sessions**.

  4. Select a BGP session type. To enable route exchange for IPv4 select **IPv4 BGP session**.

  5. To enable MP-BGP, in the **Multiprotocol BGP** section, click the **Enable IPv6 traffic** toggle to the on position.

  6. Optional: You can allocate the IPv4 BGP addresses for HA VPN tunnels manually or automatically.

     * To allocate the addresses automatically, in the **Allocate BGP IPv4 address** section, select **Automatically**.
     * To allocate the addresses manually: 
       1. Select **Manually**.
       2. Enter the IPv4 address for the **Cloud Router BGP IPv4 address**. This address is an IPv4 address used by Cloud Router for this Cloud VPN tunnel. This IPv4 address is advertised as the next hop for the IPv4 routes that Cloud Router advertises to its BGP peer. The address must be a link-local address within the same `/30` subnet as the BGP peer IPv4 address.
       3. Enter the IPv4 address for the **BGP peer IPv4 address**. This address is the IPv4 address of the on-premises router or peer VPN device. This IPv4 address is the next hop for the IPv6 routes learned from the BGP peer of Cloud Router. The address must be a link-local address within the same `/30` subnet as the Cloud Router BGP IPv4 address.
  7. Optional: You can allocate the IPv6 BGP next hop addresses for HA VPN tunnels manually or automatically.

     * To allocate the addresses automatically, in the **Allocate BGP IPv6 next hop** section, select **Automatically**.
     * To allocate the addresses manually: 
       1. Select **Manually**.
       2. Enter the IPv6 address for the **Cloud Router BGP IPv6 next hop**. This address is an IPv6 address used by Cloud Router for this Cloud VPN tunnel. This IPv6 address is advertised as the next hop for the IPv6 routes that Cloud Router advertises to its BGP peer. The address must be in the range `2600:2d00:0:2::/63`.
       3. Enter the IPv6 address for the **Peer BGP IPv6 next hop**. This address is the IPv6 address of the on-premises router or peer VPN device. This IPv6 address is the next hop for the IPv6 routes learned from the BGP peer of Cloud Router. The address must be in the range `2600:2d00:0:2::/63`.
  8. Click **Save and continue**.




**For Dedicated Interconnect**

  1. To configure a BGP session for Dedicated Interconnect, go to the **VLAN attachments** page.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list)

  2. Select the VLAN attachment that contains the BGP session to update.

  3. On the **VLAN attachment details** page, click **Edit BGP session**.

  4. Select a BGP session type. To enable route exchange for IPv4 select **IPv4 BGP session**.

  5. To enable MP-BGP, in the **Multiprotocol BGP** section, click the **Enable IPv6 traffic** toggle to the on position.

  6. Click **Save and continue**.




###  gcloud 

  1. Remove the IPv6 BGP peer:
         
         gcloud compute routers remove-bgp-peer ROUTER_NAME \
             --peer-name=PEER_NAME
         

  2. Remove the IPv6 BGP interface:
         
         gcloud compute routers remove-interface ROUTER_NAME \
             --interface-name=INTERFACE_NAME
         

  3. Enable IPv4 MP-BGP:
         
         gcloud compute routers update-bgp-peer ROUTER_NAME \
             --peer-name=PEER_NAME \
             --enable-ipv6
         




###  API 

Use the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. For each BGP peer for which you want to enable IPv6 in the BGP session, set `bgpPeers[].enableIpv6` to `TRUE` and `bgpPeers[].enableIpv4` to `FALSE`.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "bgpPeers": [
             BGP_PEERS
           ]
         }
         

Replace the following:

     * `PROJECT_ID`: the project that contains the Cloud Router
     * `REGION`: the region where the Cloud Router is located
     * `ROUTER_NAME`: the name of the Cloud Router
     * `BGP_PEERS`: the contents of the new array of BGP peers

The following example enables IPv4 and disable IPv6 in the session for the first BGP peer:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          **"enableIpv6" : false**,
          **"enableIpv4" : true**
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          "enableIpv6": false
        }
     

Additionally, if you are enabling IPv6 traffic for a BGP session used in an HA VPN tunnel, you can specify IPv6 next hop addresses:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          **"enableIpv6" : false**,
          **"enableIpv4" : true**,
          **"ipv6NexthopAddress" : "2600:2d00:0:2:0:0:1:5"**,
          **"peerIpv6NexthopAddress" : "2600:2d00:0:2:0:0:1:6"**
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": [],
          "enable": "TRUE",
          "enableIpv6": false
        }

Use the values of `ipv6NexthopAddress` and `peerIpv6NexthopAddress` to configure your on-premises router or peer VPN device.

To view example configurations for HA VPN and your peer VPN device, see [Set up third-party VPNs for IPv4 and IPv6 traffic](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides-ipv6).

To view example configurations for Dedicated Interconnect and your on-premises router, see [Set up on-premises routers for IPv4 and IPv6 traffic](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers#set-up-on-premises-routers-for-ipv4-and-ipv6-traffic).




## What's next

  * To disable or end a BGP session, see [Disable or remove BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
