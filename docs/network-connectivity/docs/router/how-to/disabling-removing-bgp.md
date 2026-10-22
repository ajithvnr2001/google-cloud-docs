---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp/
title: Disable or remove BGP sessions \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:52.158041+00:00
---

# Disable or remove BGP sessions  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Disable or remove BGP sessions

You can disable a BGP session temporarily or remove it entirely. Some common reasons for disabling a session are changing router configuration when migrating to a different BGP peer or performing maintenance on a BGP peer.

## Before you begin

###  gcloud 

If you want to use the command-line examples in this guide, do the following:

  1. Install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
  2. Set a [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



###  API 

If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/compute/docs/api/prereqs).

## Disable a BGP session

You can disable a BGP session by using the Google Cloud console, the `update-bgp-peer` command, or the API. BGP sessions are enabled by default.

If disabled, any active session with the BGP peer is shut down, and all associated routing information is removed.

To disable a BGP session, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the router that hosts the BGP session that you want to disable.
  3. On the **Router details** page, select the BGP session that you to want to disable.
  4. On the **BGP session details** page, click edit**Edit**.
  5. For **BGP peer** , select **Disabled**.
  6. Click **Save**.



###  gcloud 

Run the `update-bgp-peer` command:
    
    
      gcloud compute routers update-bgp-peer ROUTER_NAME \
          --project=PROJECT_ID \
          --peer-name=PEER_NAME \
          --region=REGION \
          --no-enabled
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `PROJECT_ID`: the project that contains the Cloud Router
  * `PEER_NAME`: the name of your BGP peer
  * `REGION`: the region where the Cloud Router is located



###  API 

Use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. For each BGP peer for which you want to disable the BGP session, set `bgpPeers[].enable` to `FALSE`.
         
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

The following example disables the session for the first BGP peer:
    
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
          **"enable": "FALSE"**
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
          "advertisedIpRanges": []
        }
    




## Enable a BGP session

You can enable a BGP session by using the Google Cloud console, the `update-bgp-peer` command, or the API. BGP sessions are enabled by default.

If enabled, the peer connection can be established with routing information.

To enable a BGP session, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the router that hosts the BGP session that you want to enable.
  3. On the **Router details** page, select the BGP session that you want to enable.
  4. On the **BGP session details** page, click edit**Edit**.
  5. For **BGP peer** , select **Enabled**.
  6. Click **Save**.



###  gcloud 

Run the `update-bgp-peer` command:
    
    
      gcloud compute routers update-bgp-peer ROUTER_NAME \
          --project=PROJECT_ID \
          --peer-name=PEER_NAME \
          --region=REGION \
          --enabled
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `PROJECT_ID`: the project that contains the Cloud Router
  * `PEER_NAME`: the name of your BGP peer
  * `REGION`: the region where the Cloud Router is located



###  API 

Use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you make a `PATCH` request with this field specified, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#api).

  2. Send a `PATCH` request with a new array of BGP peers. For each BGP peer for which you want to enable the BGP session, set `bgpPeers[].enable` to `TRUE`.
         
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

The following example enables the session for the first BGP peer:
    
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
          **"enable": "TRUE"**
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
          "advertisedIpRanges": []
        }
    




## Remove a BGP session

If you delete the Cloud VPN tunnel or VLAN attachment associated with a BGP session, the session is automatically shut down.

You can remove BGP sessions manually by using the Google Cloud console, the `remove-bgp-peer` command, or the API. If you remove the BGP session, the VPN tunnel or VLAN attachment remains, but the Cloud Router doesn't advertise routes over them.

To remove a BGP session, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the router that you want to remove a BGP session from.
  3. For **BGP sessions** , select the BGP session that you want to remove.
  4. At the top of the page, click delete**Delete** , and then confirm the deletion.



###  gcloud 

Run the `remove-bgp-peer` command:
    
    
    gcloud compute routers remove-bgp-peer ROUTER_NAME \
        --project=PROJECT_ID \
        --peer-name=PEER_NAME \
        --region=REGION \
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `PROJECT_ID`: the project that contains the Cloud Router
  * `PEER_NAME`: the name of your BGP peer
  * `REGION`: the region where the Cloud Router is located



###  API 

To remove BGP peers from a Cloud Router, use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#api).

  2. Send a `PATCH` request with a new array of BGP peers. Use the array from the `GET` request in the previous step, and remove any BGP peers that you do not want on the router.

You can send an empty array to remove all BGP peers.
         
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

The following example contains two BGP peers:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT"
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT"
        }
    




## What's next

  * To view the configuration of a Cloud Router, its BGP sessions, and the routes that Cloud Router is advertising, see [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).
  * For information about BGP session states, see [BGP session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states).
  * To troubleshoot issues with Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
