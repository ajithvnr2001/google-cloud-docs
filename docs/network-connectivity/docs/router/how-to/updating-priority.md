---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-priority/
title: Update the base route priority \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:29.482485+00:00
---

# Update the base route priority  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-priority/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update the base route priority

When you configure a Border Gateway Protocol (BGP) session on a Cloud Router, you can specify a base advertised priority. Before you begin, ensure that you are familiar with the Cloud Router [Advertised routes overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes). For more information about how Cloud Router uses the base advertised priority, see [Advertised priority](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority).

Base priorities are whole numbers from `0` to `65535`. The highest possible base priority is `0`. The default base priority is `100`. If you don't specify a base priority, the default priority is used.

Base priorities let you specify which Cloud VPN tunnels or Cloud Interconnect VLAN attachments on-premises systems to use to send packets to your VPC network. You can create active-active, active-passive, or a custom combination of these topologies by using the base priority to influence how packets are sent to your VPC network. For an example using HA VPN tunnels, see [Active-active and active-passive routing options for HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#active) in the Cloud VPN documentation.

When choosing base priorities, keep the following in mind:

  * Region-to-region costs are between `201` and `9999`, inclusive. The value depends on the distance, latency, and other factors between two regions. Google generates the region-to-region cost values, and you can't modify them.

  * Base priorities among Cloud Routers in a region are recommended to be between `0` and `200`, inclusive. Because region-to-region costs are at least `201`, if you use base priorities of `201` or more, you might accidentally assign a Cloud VPN tunnel or VLAN attachment a lower priority than you intend. Another BGP session in a different region might advertise the same prefix with an overall higher priority (MED, which equals base priority plus region-to-region cost). Without carefully setting base priorities in other regions, you might cause on-premises traffic to be delivered to your VPC network by way of an unexpected Cloud VPN tunnel or VLAN attachment.

  * Base priorities of `10200` or more help ensure that a prefix's overall advertised priority (MED, base priority plus region-to-region cost) is always lower than any other advertised prefix with a base priority of `200` or less.




To update the base advertised route priority for an existing BGP session, follow these steps.

###  Console 

For Cloud VPN tunnels that use dynamic routing, including HA VPN tunnels, complete the following steps:

  1. In the Google Cloud console, go to the **Cloud VPN** tunnels page.

[Go to Cloud VPN tunnels](https://console.cloud.google.com/hybrid/vpn/list?&tab=tunnels)

  2. From the list of tunnels in the **Name** column, select the tunnel that you want to modify.

  3. On the **Cloud VPN tunnel details** page, select **Modify BGP session**.

  4. Modify the **Advertised route priority** value.

  5. Click **Save and continue**.




For Dedicated Interconnect or Partner Interconnect, complete the following steps:

  1. In the Google Cloud console, go to the **VLAN attachments** tab on the **Cloud Interconnect** page.

[Go to Cloud Interconnect](https://console.cloud.google.com/hybrid/interconnects/list?&tab=attachments)

  2. From the list of attachments in the **Name** column, select the attachment that you want to modify.

  3. On the **VLAN attachment details** page, select the name of the **BGP session**.

  4. Modify the **Advertised route priority** value.

  5. Click **Save and continue**.




###  gcloud 

Run the `update-bgp-peer` command using the `--advertised-route-priority` flag. Specify the name of the Cloud Router and BGP session that correspond to the appropriate Cloud VPN tunnel or VLAN attachment.
    
    
    gcloud compute routers update-bgp-peer ROUTER_NAME \
        --peer-name=NAME_OF_BGP_SESSION \
        --advertised-route-priority=BASE_PRIORITY_VALUE
    

###  API 

Use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. In the array element that contains the BGP session that you want to update, modify the value of `advertisedRoutePriority`.
         
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

The following example includes one BGP peer with the default `advertisedRoutePriority` of `100` and another with an updated value of `99`:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          **"advertisedRoutePriority": 100** ,
          "advertiseMode": "DEFAULT"
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,
          **"advertisedRoutePriority": 99** ,
          "advertiseMode": "DEFAULT"
        }
    




## What's next?

  * To view the base advertised route priority, see [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).

  * To troubleshoot issues when using Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
