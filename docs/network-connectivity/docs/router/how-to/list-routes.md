---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/list-routes/
title: List BGP routes \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:15.802828+00:00
---

# List BGP routes  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/list-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# List BGP routes

This page describes how to list advertised routes and learned routes on individual _Border Gateway Protocol (BGP)_ sessions, which can help you troubleshoot your Cloud Router routes. You can list routes either before or after [BGP route policies](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview) are applied to a route. To troubleshoot advertised and learned routes, we recommend completing the following sections in order.

## Before you begin

###  gcloud 

If you want to use the command-line examples in this guide, do the following:

  1. Install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
  2. Set a [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



###  API 

If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/compute/docs/api/prereqs).

## List BGP routes before policies are applied

###  Console 

Do the following:

  1. In the Google Cloud console, go to the **Cloud Router** page.

[Go to Cloud Router](https://console.cloud.google.com/hybrid/routers/list)

  2. On the **Cloud Router** page, click the **BGP sessions** tab.

  3. Select the BGP session peer that you want to list. The BGP session details page is displayed. Advertised routes are listed in the **Advertised routes** section.




###  gcloud 

Use the [`gcloud compute routers list-bgp-routes` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/list-bgp-routes):
    
    
    gcloud compute routers list-bgp-routes ROUTER_NAME \
        --address-family=ADDRESS_FAMILY \
        --no-policy-applied \
        --peer=PEER_NAME \
        --region=REGION \
        --route-direction=ROUTE_DIRECTION
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router

  * `ADDRESS_FAMILY`: the IP address family to display routes for:

    * `IPV4`: for IPv4-based BGP addresses
    * `IPV6`: for IPv6-based BGP addresses
  * `PEER_NAME`: the name of the BGP peer

  * `REGION`: the region in which your Cloud Router is located

  * `ROUTE_DIRECTION`: the direction to display routes for:

    * `INBOUND`: routes learned from the BGP peer
    * `OUTBOUND`: routes advertised to the BGP peer



The output is similar to the following:
    
    
    ---
    asPaths:
    - asns:
      - 64515
      type: AS_PATH_TYPE_SEQUENCE
    destination:
      prefix: 192.168.1.0/24
    med: 100
    origin: BGP_ORIGIN_INCOMPLETE
    ---
    asPaths:
    - asns:
      - 64515
      type: AS_PATH_TYPE_SEQUENCE
    destination:
      prefix: 192.168.2.0/24
    med: 333
    origin: BGP_ORIGIN_INCOMPLETE
    

###  API 

Use the [`routers.listBgpRoutes` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/listBgpRoutes):
    
    
    GET https://compute.googleapis.com/compute/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME/listBgpRoutes
    {
      "addressFamily": "ADDRESS_FAMILY",
      "peer": "PEER_NAME",
      "policyApplied": FALSE,
      "routeType": "ROUTE_TYPE"
    }
    

Replace the following:

  * `PROJECT_ID`: the project that contains your Cloud Router

  * `REGION`: the region in which your Cloud Router is located

  * `ROUTER_NAME`: the name of your Cloud Router

  * `ADDRESS_FAMILY`: the IP address family to display routes for:

    * `IPV4`: for IPv4-based BGP addresses
    * `IPV6`: for IPv6-based BGP addresses
  * `PEER_NAME`: the name of the BGP peer

  * `ROUTE_TYPE`: the type of route to display:

    * `LEARNED`: route learned from the BGP peer
    * `ADVERTISED`: route advertised to the BGP peer



The output is similar to the following:
    
    
    {
      "kind": "compute#routersListBgpRoutes",
      "result": [
        {
          "destination": {
            "prefix": "10.0.1.0/24"
          },
          "med": 100
        },
        {
          "destination": {
            "prefix": "10.0.2.0/24"
          },
          "med": 338
        }
      ]
    }
    

## List BGP routes after policies are applied

###  Console 

  1. In the Google Cloud console, go to the **Cloud Router** page.

[Go to Cloud Router](https://console.cloud.google.com/hybrid/routers/list)

  2. On the **Cloud Router** page, click the **BGP sessions** tab.

  3. Select the BGP session peer that you want to list. The BGP session details page is displayed. Advertised routes are listed in the **Advertised routes** section.




###  gcloud 

Use the [`gcloud compute routers list-bgp-routes` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/list-bgp-routes):
    
    
    gcloud compute routers list-bgp-routes ROUTER_NAME \
        --address-family=ADDRESS_FAMILY \
        --policy-applied \
        --peer=PEER_NAME \
        --region=REGION \
        --route-direction=ROUTE_DIRECTION
    

Replace the following:

  * `ADDRESS_FAMILY`: the IP address family to display routes for:

    * `IPV4`: for IPv4-based BGP addresses
    * `IPV6`: for IPv6-based BGP addresses
  * `PEER_NAME`: the name of the BGP peer

  * `ROUTE_DIRECTION`: the direction to display routes for:

    * `INBOUND`: routes learned from the BGP peer
    * `OUTBOUND`: routes advertised to the BGP peer



The output is similar to the following:
    
    
    ---
    asPaths:
    - asns:
    - 64515
    type: AS_PATH_TYPE_SEQUENCE
    communities:
    - 65535:65281
    destination:
    prefix: 192.168.1.0/24
    med: 100
    origin: BGP_ORIGIN_INCOMPLETE
    ---
    asPaths:
    - asns:
    - 64515
    type: AS_PATH_TYPE_SEQUENCE
    communities:
    - 65535:65281
    destination:
    prefix: 192.168.2.0/24
    med: 333
    origin: BGP_ORIGIN_INCOMPLETE
    

###  API 

Use the [`routers.listBgpRoutes` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/listBgpRoutes):
    
    
    GET https://compute.googleapis.com/compute/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME/listBgpRoutes
    {
    "addressFamily": "ADDRESS_FAMILY",
    "peer": "PEER_NAME",
    "policyApplied": TRUE,
    "routeType": "ROUTE_TYPE"
    }
    

Replace the following:

  * `PROJECT_ID`: the project that contains your Cloud Router

  * `REGION`: the region in which your Cloud Router is located

  * `ROUTER_NAME`: the name of your Cloud Router

  * `ADDRESS_FAMILY`: the IP address family to display routes for:

    * `IPV4`: for IPv4-based BGP addresses
    * `IPV6`: for IPv6-based BGP addresses
  * `PEER_NAME`: the name of the BGP peer

  * `ROUTE_TYPE`: the type of route to display:

    * `LEARNED`: route learned from the BGP peer
    * `ADVERTISED`: route advertised to the BGP peer



The output is similar to the following:
    
    
    {
      "kind": "compute#routersListBgpRoutes",
      "result": [
        {
          "destination": {
            "prefix": "10.0.1.0/24"
          },
          "asPaths": [
            {
              "type": "AS_PATH_TYPE_SEQUENCE",
              "asns": [
                64514
              ]
            }
          ],
          "origin": "BGP_ORIGIN_INCOMPLETE",
          "med": 100
        },
        {
          "destination": {
            "prefix": "10.0.2.0/24"
          },
          "asPaths": [
            {
              "type": "AS_PATH_TYPE_SEQUENCE",
              "asns": [
                64514
              ]
            }
          ],
          "origin": "BGP_ORIGIN_INCOMPLETE",
          "med": 338
        }
      ]
    }
    

## Check the best dynamic routes

Check the best dynamic routes per Cloud Router and per region per VPC:

###  gcloud 

Use the [`gcloud compute routers get-status` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-status):
    
    
    gcloud compute routers get-status ROUTER_NAME \
        --region=REGION
    

The output includes the following information:

  * **`bestRoutesForRouter`** : represents the best routes for a specific Cloud Router
  * **`bestRoutes`** : represents the best routes per region of a Cloud Router of that VPC.



The output is similar to the following for `bestRoutesForRouter`:
    
    
      bestRoutesForRouter:
      - asPaths:
        - asLists:
          - 65002
          pathSegmentType: AS_SEQUENCE
        creationTimestamp: '2024-09-26T18:28:54.346-07:00'
        destRange: 192.168.1.0/24
        kind: compute#route
        network: https://www.googleapis.com/compute/projects/PROJECT_ID/global/networks/NETWORK_NAME
        nextHopIp: 169.254.0.2
        nextHopOrigin: INCOMPLETE
        nextHopVpnTunnel: https://www.googleapis.com/compute/projects/PROJECT_ID/regions/REGION/vpnTunnels/vpc-demo-tunnel0
        priority: 100
        routeStatus: ACTIVE
        routeType: BGP
      - asPaths:
        - asLists:
          - 65002
          pathSegmentType: AS_SEQUENCE
        creationTimestamp: '2024-09-27T12:44:56.575-07:00'
        destRange: 192.168.1.0/24
        kind: compute#route
        network: https://www.googleapis.com/compute/projects/PROJECT_ID/global/networks/NETWORK_NAME
        nextHopIp: 169.254.1.2
        nextHopOrigin: INCOMPLETE
        nextHopVpnTunnel: https://www.googleapis.com/compute/projects/PROJECT_ID/regions/REGION/vpnTunnels/vpc-demo-tunnel1
        priority: 100
        routeStatus: ACTIVE
        routeType: BGP
    
    

The output is similar to the following for `bestRoutes`:
    
    
      bestRoutes:
      - asPaths:
        - asLists:
          - 65002
          pathSegmentType: AS_SEQUENCE
        creationTimestamp: '2024-09-26T18:33:50.505-07:00'
        destRange: 192.168.1.0/24
        kind: compute#route
        network: https://www.googleapis.com/compute/projects/PROJECT_ID/global/networks/NETWORK_NAME
        nextHopIp: 169.254.0.2
        nextHopOrigin: INCOMPLETE
        nextHopVpnTunnel: https://www.googleapis.com/compute/projects/PROJECT_ID/regions/REGION/vpnTunnels/vpc-demo-tunnel0
        priority: 100
        routeType: BGP
      - asPaths:
        - asLists:
          - 65002
          pathSegmentType: AS_SEQUENCE
        creationTimestamp: '2024-09-27T12:46:49.028-07:00'
        destRange: 192.168.1.0/24
        kind: compute#route
        network: https://www.googleapis.com/compute/projects/PROJECT_ID/global/networks/NETWORK_NAME
        nextHopIp: 169.254.1.2
        nextHopOrigin: INCOMPLETE
        nextHopVpnTunnel: https://www.googleapis.com/compute/projects/PROJECT_ID/regions/REGION/vpnTunnels/vpc-demo-tunnel1
        priority: 100
        routeType: BGP
    

The output includes the following values:

  * `PROJECT_ID`: the project that contains your Cloud Router

  * `NETWORK_NAME`: the name of the VPC network

  * `REGION`: the name of the region




###  API 

Use the [`routers.getRouterStatus` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/getRouterStatus):
    
    
    GET https://compute.googleapis.com/compute/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME/getRouterStatus
    

Replace the following:

  * `PROJECT_ID`: the project that contains your Cloud Router

  * `REGION`: the region in which your Cloud Router is located

  * `ROUTER_NAME`: the name of your Cloud Router




The output includes the following information:

  * **`bestRoutes`** : represents the best routes per region of a Cloud Router of that VPC.
  * **`bestRoutesForRouter`** : represents the best routes for a specific Cloud Router



The output is similar to the following for `bestRoutes`:
    
    
        "bestRoutes": [
          {
            "kind": "compute#route",
            "creationTimestamp": "2025-03-05T11:20:40.323-08:00",
            "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME",
            "destRange": "200.0.0.0/24",
            "priority": 100,
            "nextHopIp": "169.254.0.1",
            "nextHopVpnTunnel": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels/TUNNEL_NAME",
            "routeType": "BGP",
            "asPaths": [
              {
                "pathSegmentType": "AS_SEQUENCE",
                "asLists": [
                  65001
                ]
              }
            ],
            "nextHopOrigin": "INCOMPLETE"
          },
    

The output is similar to the following for `bestRoutesForRouter`:
    
    
        "bestRoutesForRouter": [
          {
            "kind": "compute#route",
            "creationTimestamp": "2025-03-05T11:20:50.240-08:00",
            "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME",
            "destRange": "10.2.1.0/24",
            "priority": 100,
            "nextHopIp": "169.254.0.1",
            "nextHopVpnTunnel": "https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/regions/REGION/vpnTunnels/TUNNEL_NAME",
            "routeType": "BGP",
            "asPaths": [
              {
                "pathSegmentType": "AS_SEQUENCE",
                "asLists": [
                  65001
                ]
              }
            ],
            "routeStatus": "ACTIVE",
            "nextHopOrigin": "INCOMPLETE"
          },
          {
            "kind": "compute#route",
            "creationTimestamp": "2025-03-05T01:50:01.725-08:00",
            "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/on-prem",
            "destRange": "200.0.0.0/24",
            "priority": 100,
            "nextHopIp": "169.254.0.1",
            "nextHopVpnTunnel": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels/TUNNEL_NAME",
            "routeType": "BGP",
            "asPaths": [
              {
                "pathSegmentType": "AS_SEQUENCE",
                "asLists": [
                  65001
                ]
              }
            ],
            "routeStatus": "ACTIVE",
            "nextHopOrigin": "INCOMPLETE"
          },
          {
            "kind": "compute#route",
            "creationTimestamp": "2025-03-06T05:30:06.277-08:00",
            "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/on-prem",
            "destRange": "10.2.1.0/24",
            "priority": 100,
            "nextHopIp": "169.254.1.1",
            "nextHopVpnTunnel": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels/TUNNEL_NAME",
            "routeType": "BGP",
            "asPaths": [
              {
                "pathSegmentType": "AS_SEQUENCE",
                "asLists": [
                  65001
                ]
              }
            ],
            "routeStatus": "ACTIVE",
            "nextHopOrigin": "INCOMPLETE"
          }
        ],
    

The output includes the following values:

  * `PROJECT_ID`: the project that contains your Cloud Router

  * `REGION`: the region in which your Cloud Router is located

  * `ROUTER_NAME`: the name of your Cloud Router

  * `TUNNEL_NAME`: if applicable, the name of your VPN tunnel




## View the VPC forwarding plane route table

Do the following:

  1. In the Google Cloud console, go to the **Routes** page.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. On the **Effective routes** tab, select the network you want to list routes for.

  3. In the **Region** list, select the region that you want to list routes in, and then click **View**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
