---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-bfd/
title: Update or disable BFD \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:20.127409+00:00
---

# Update or disable BFD  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-bfd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update or disable BFD

You can update settings for Bidirectional Forwarding Detection (BFD) on an active BGP session or when disabling a session.

For more information about BFD for Cloud Router, see the following resources:

  * View [descriptions of the BFD settings](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#bfd-settings) used on this page.
  * Learn more about BFD in the [BFD for Cloud Router overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd).
  * Check BFD status by [viewing Cloud Router status](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#viewing-router-status).



**Important:** BFD can only be enabled on provisioned VLAN attachments that use Dataplane version 2. You can view the `dataplaneVersion` for a VLAN attachment by viewing the attachment details in one of the following ways:

  * **API** : Use the [interconnectAttachments.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/get) method. You can use this method on VLAN attachments for either Dedicated Interconnect or Partner Interconnect. 
  * **Google Cloud CLI** : Use the `gcloud compute interconnects attachments describe ATTACHMENT-NAME` command where ATTACHMENT-NAME is the name of the VLAN attachment for either Dedicated Interconnect or Partner Interconnect. 



In the output of the API or gcloud CLI command, look for the `dataplaneVersion` field with a value of `2`. If the field is absent from the output, the VLAN attachment is using version 1 and cannot be used with BFD. For more information, contact your customer account team.

The Cloud Interconnect Dataplane v2 is unrelated to [ Google Kubernetes Engine (GKE) Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2)

**Note:** Cloud Router supports only BFD single-hop mode. BFD multi-hop and BFD auth are not supported. If the on-premises router inherits the BFD mode from the eBGP multi-hop configuration, then configure BFD single-hop mode explicitly. Alternatively, consider removing eBGP multi-hop configuration because it is not needed on VLAN attachments that use Dataplane version 2, which is required for BFD. 

The Cisco command for setting a single-hop link is `neighbor x.y.y.z fall-over bfd single-hop`.

## Before you begin

###  gcloud 

If you want to use the command-line examples in this guide, do the following:

  1. Install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
  2. Set a [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



###  API 

If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/compute/docs/api/prereqs).

## Update BFD settings on an active BGP session

To update BFD settings on an existing BGP session, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router to update.

  3. On the **Router details** page, in the **BGP sessions** section, select the BGP session to update.

  4. On the **BGP session details** page, click edit**Edit**.

  5. Configure BFD options as documented in [BFD settings and timers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#bfd-settings).




###  gcloud 

Run the `update-bgp-peer` command:
    
    
      gcloud compute routers update-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME \
          --project=PROJECT_ID \
          --interface=INTERFACE \
          --ip-address=IP_ADDRESS \
          --peer-asn=PEER_ASN \
          --peer-ip-address=PEER_IP_ADDRESS \
          --region=REGION \
          --bfd-session-initialization-mode=BFD_SESSION_INITIALIZATION_MODE  \
          --bfd-min-receive-interval=BFD_MIN_RECEIVE_INTERVAL \
          --bfd-min-transmit-interval=BFD_MIN_TRANSMIT_INTERVAL \
          --bfd-multiplier=BFD_MULTIPLIER
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `PEER_NAME`: the name of your BGP peer
  * `PROJECT_ID`: the name of the project containing the Cloud Router
  * `INTERFACE`: the name of the interface for this BGP peer
  * `IP_ADDRESS`: the link-local IP address of the Cloud Router interface for this BGP peer in the range `169.254.0.0/16`; belongs to the same subnet as the interface IP address of the peer router
  * `PEER_ASN`: the BGP autonomous system number (ASN) for this BGP peer
  * `PEER_IP_ADDRESS`: the link-local address of the peer router that belongs to the range`169.254.0.0/16`
  * `REGION`: the region where the Cloud Router is located
  * Configure BFD options as documented in [BFD settings and timers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#bfd-settings).



### API

Use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgpPeers[].bfd` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. In the array element that contains the BGP session whose BFD settings you want to update, modify the `bgpPeers[].bfd` field:
         
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

The following example includes two BGP peers and sets the values in the `bgpPeers[].bfd` field. For more information about these options, see [BFD settings and timers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#bfd-settings).
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT"
          **"bfd": {
            "sessionInitializationMode": DISABLED,
            "minTransmitInterval": 1000,
            "minReceiveInterval": 1000,
            "multiplier": 5
          }**
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,
          "advertisedRoutePriority": 99,
          "advertiseMode": "DEFAULT"
          **"bfd": {
            "sessionInitializationMode": ACTIVE,
            "minTransmitInterval": 1000,
            "minReceiveInterval": 1000,
            "multiplier": 5
          }**
        }
    




## Disable BFD

When disabling BFD, you can optionally configure BFD settings that become active when you re-enable the session. The options remain configured for the disabled session, but are not in effect. This behavior is similar to disabling a firewall rule without deleting it.

To disable BFD on a BGP session, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router to update.

  3. On the **Router details** page, in the **BGP sessions** section, select the BGP session to update.

  4. On the **BGP session details** page, click edit**Edit**.

  5. Set **BFD session initialization mode** to `Disabled`.

  6. Optionally configure other BFD options as documented in [BFD settings and timers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#bfd-settings).




###  gcloud 

Run the `update-bgp-peer` command:
    
    
      gcloud compute routers update-bgp-peer ROUTER_NAME \
          --project=PROJECT_ID \
          --peer-name=PEER_NAME \
          --interface=INTERFACE \
          --ip-address=IP_ADDRESS \
          --peer-asn=PEER_ASN \
          --peer-ip-address=PEER_IP_ADDRESS \
          --region=REGION \
          --bfd-session-initialization-mode=BFD_SESSION_INITIALIZATION_MODE  \
          --bfd-min-receive-interval=BFD_MIN_RECEIVE_INTERVAL \
          --bfd-min-transmit-interval=BFD_MIN_TRANSMIT_INTERVAL \
          --bfd-multiplier=BFD_MULTIPLIER
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `PROJECT_ID`: the name of the project containing the Cloud Router
  * `PEER_NAME`: the name of your BGP peer
  * `INTERFACE`: the name of the interface for this BGP peer
  * `IP_ADDRESS`: the link-local IP address of the Cloud Router interface for this BGP peer in the range `169.254.0.0/16`; belongs to the same subnet as the interface IP address of the peer router
  * `PEER_ASN`: the BGP autonomous system number (ASN) for this BGP peer
  * `PEER_IP_ADDRESS`: the link-local address of the peer router that belongs to the range `169.254.0.0/16`
  * `REGION`: the region where the Cloud Router is located
  * `BFD_SESSION_INITIALIZATION_MODE`: set to `disabled`
  * Optional: configure other BFD options as documented in [BFD settings](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#bfd-settings)



###  API 

Use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgpPeers[].bfd.sessionInitializationMode` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. In the array element that contains the BGP session for which you want to disable BFD, set the `bgpPeers[].bfd.sessionInitializationMode` to `DISABLED`:
         
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

The following example includes two BGP peers and disables BFD for both of them. For more information about these options, see [BFD settings and timers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#bfd-settings).
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "DEFAULT"
          **"bfd": {
            "sessionInitializationMode": DISABLED,**
            "minTransmitInterval": 1000,
            "minReceiveInterval": 1000,
            "multiplier": 5
          }
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,https://cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd
          "advertisedRoutePriority": 99,
          "advertiseMode": "DEFAULT"
          **"bfd": {
            "sessionInitializationMode": DISABLED,**
            "minTransmitInterval": 1000,
            "minReceiveInterval": 1000,
            "multiplier": 5
          }
        }
    




## What's next

  * To configure BFD on a BGP session or peer router, see [Configure BFD for Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd).

  * To find examples of third-party router configurations that support BFD for Cloud Router, see [Use third-party router configurations for BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bfd-interop).

  * For help with BFD diagnostic messages, session states, and status messages, see [BFD diagnostic messages and session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd-states).

  * To configure BGP sessions, see [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp).

  * To list, update, or delete a Cloud Router, see [List and delete Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-routers).

  * To troubleshoot issues with Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
