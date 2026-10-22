---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-revert-default/
title: Revert to default advertisement mode \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:12.268152+00:00
---

# Revert to default advertisement mode  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-revert-default/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Revert to default advertisement mode

If you no longer need to advertise certain subnets or custom IP ranges, you can revert back to [default advertisement mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#route-advertisement-default).

**Note:** When you revert to default advertisement mode, Cloud Router deletes the existing custom advertisement mode configuration. You must reconfigure custom advertised routes if you want use them again. If you clear custom advertisement mode on the Cloud Router, all of its BGP sessions still retain their custom advertised route configuration. To clear custom advertisement mode on the Cloud Router BGP sessions, you must individually revert each BGP session.

By default, the Cloud Router advertises all [available subnets](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#dynamic-routing-mode), including new ones. For BGP sessions, the default behavior is to inherit the Cloud Router's behavior.

## Before you begin

###  gcloud 

If you want to use the command-line examples in this guide, do the following:

  1. Install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
  2. Set a [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



###  API 

If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/compute/docs/api/prereqs).

## Revert to default advertisement mode on a Cloud Router

To revert to default advertisement mode on a Cloud Router, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router to update.

  3. On the **Router details** page, click edit**Edit**.

  4. In the **Advertised routes** section, for **Routes** , select **Advertise all subnets visible to the Cloud Router (Default)**.

  5. Click **Save** to revert to default advertisement mode.




###  gcloud 

Run the `update` command. Use the `--advertisement-mode` flag to change the advertisement mode to `default`, as shown in the following example:
    
    
    gcloud compute routers update my-router \
        --advertisement-mode default
    

**Note:** BGP sessions with custom advertised routes retain their custom configurations. You must individually revert each BGP session.

###  API 

Use the [routers.patch](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to set `bgp.advertiseMode` to `DEFAULT` and clear the custom advertisement mode configuration:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
    {
      "bgp": {
        "advertiseMode": "DEFAULT",
        "advertisedGroups": [],
        "advertisedIpRanges": []
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the project that contains the Cloud Router
  * `REGION`: the region where the Cloud Router is located
  * `ROUTER_NAME`: the name of the Cloud Router



## Revert to default advertisement mode on a BGP session

To revert to default advertisement mode on a BGP session, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router that contains the BGP session to update.

  3. On the **Router details** page, select the BGP session to update.

  4. On the **BGP session details** page, click edit**Edit**.

  5. For **Routes** , select **Advertise all subnets visible to the Cloud Router (Default)**.

  6. Click **Save** to revert to default advertisement mode.




###  gcloud 

Run the `update-bgp-peer` command. Use the `--advertisement-mode` flag to change the advertisement mode to `default`, as shown in the following example:
    
    
    gcloud compute routers update-bgp-peer my-router \
        --peer-name my-bgp-session \
        --advertisement-mode default
    

###  API 

For one or more BGP sessions, use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. For each BGP peer that you want to revert to default advertisement mode, do the following:

     * Set `advertisedMode` to `DEFAULT`
     * Set `advertisedGroup[]` and `advertisedIpRanges[]` to `[]`
    
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

The following example reverts two BGP sessions to default advertisement mode:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          **"advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": []**
        },
        {
          "name": "peer-2",
          "interfaceName": "if-peer-2",
          "ipAddress": "169.254.20.1",
          "peerIpAddress": "169.254.20.2",
          "peerAsn": 64513,
          "advertisedRoutePriority": 100,
          **"advertiseMode": "DEFAULT",
          "advertisedGroups": [],
          "advertisedIpRanges": []**
        }
    




## What's next

  * To view the configuration of a Cloud Router, its BGP sessions, and the routes that Cloud Router is advertising, see [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).

  * To troubleshoot issues with custom advertised routes, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
