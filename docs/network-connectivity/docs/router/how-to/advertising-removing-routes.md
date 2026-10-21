---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-removing-routes/
title: Remove custom advertised routes \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:16.263381+00:00
---

# Remove custom advertised routes  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-removing-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Remove custom advertised routes

This page describes how to stop advertising existing IP address ranges and prevent clients in your on-premises network from discovering subnets or custom IP address ranges in your Virtual Private Cloud (VPC) network. You can only remove existing custom advertised routes. You can't add IP address ranges to a denylist.

**Note:** To secure your VPC network, use firewall rules to block traffic from reaching unadvertised subnets. Don't rely on hidden routes. Users can still reach unadvertised virtual machine (VM) instances through static routes.

Before you begin, make sure that you have a list of existing IP address ranges or advertisement groups that you want to remove.

## Before you begin

###  gcloud 

If you want to use the command-line examples in this guide, do the following:

  1. Install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
  2. Set a [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



###  API 

If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/compute/docs/api/prereqs).

## Remove custom advertised routes on a Cloud Router

To remove existing custom advertised routes on a Cloud Router, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router to update.

  3. On the **Router details** page, click edit**Edit**.

  4. Find the custom advertised routes to delete, and then next to each route, click delete**Delete**.

  5. After you finish deleting the routes, click **Save**.




###  gcloud 

**Remove Google-defined advertisement groups**

To remove Google-defined advertisement groups, use the `gcloud compute routers update` command with the `--remove-advertisement-groups` flag. Advertisement groups are Google-defined IP address ranges that the Cloud Router dynamically advertises. For a list of all advertisement groups, see the [`set-advertisement-groups` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create) in the Google SDK documentation.
    
    
     gcloud compute routers update ROUTER_NAME \
          --remove-advertisement-groups=ADVERTISED_GROUPS
    

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `ADVERTISED_GROUPS`: Google-defined IP address ranges that the Cloud Router dynamically advertises

The only valid value is `all_subnets`, which advertises subnets based on the VPC network's dynamic routing mode (similar to default advertisement mode).




The following example updates the `my-router` Cloud Router and removes the `all_subnets` advertisement group:
    
    
     gcloud compute routers update my-router \
         --remove-advertisement-groups all_subnets
    

**Remove existing IP address ranges**

To remove existing IP address ranges that are being advertised, such as static external IP addresses or subnet IP address ranges, use the `gcloud compute routers update` command with the `--remove-advertisement-ranges` flag:
    
    
     gcloud compute routers update ROUTER_NAME \
         --remove-advertisement-ranges=ADVERTISED_IP_RANGES
    

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `ADVERTISED_IP_RANGES`: the contents of the new array of IP address ranges

You can specify both IPv4 and IPv6 custom IP address ranges. However, IPv6 custom ranges are advertised only in BGP sessions where IPv6 is enabled.




The following example removes the existing `10.0.10.0/24` subnet IP address range from the `my-router` Cloud Router:
    
    
     gcloud compute routers update my-router \
         --remove-advertisement-ranges 10.0.10.0/24
    

###  API 

To update the `bgp.advertisedGroups[]` and `bgp.advertisedIpRanges[]` fields, use the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch).

The `bgp.advertisedGroups[]` and `bgp.advertisedIpRanges[]` fields accept arrays of advertised groups and advertised IP address ranges. When you `PATCH` these fields, you overwrite the existing arrays with the new ones in your request.

  1. Send a `GET` request to get the current arrays of advertised groups and advertised IP address ranges on the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with new arrays of advertised groups and advertised IP address ranges. Use the arrays from the `GET` request in the previous step and remove any groups or IP address ranges that you do not want on the router.

You can send an empty array to remove all advertised groups or advertised IP address ranges:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "bgp": {
             "advertisedGroups": [
               "ADVERTISED_GROUPS"
            ],
             "advertisedIpRanges": [
             ADVERTISED_IP_RANGES
            ]
          }
         }
         

Replace the following:

     * `PROJECT_ID`: the project that contains the Cloud Router
     * `REGION`: the region where the Cloud Router is located
     * `ROUTER_NAME`: the name of the Cloud Router
     * `ADVERTISED_GROUPS`: a Google-defined group that the Cloud Router dynamically advertises

The only valid value is `ALL_SUBNETS`, which advertises subnets based on the VPC network's dynamic routing mode (similar to default advertisement mode). To stop advertising subnets, you can send an empty array.

     * `ADVERTISED_IP_RANGES`: the contents of the new array of IP address ranges

The following example contains two IP address ranges:
    
    {
          "range": "1.2.3.4",
          "description": "First example range"
        },
        {
          "range": "6.7.0.0/16",
          "description": "Second example range"
        }
    




## Remove custom advertised routes from a BGP session

To remove existing advertised routes from a BGP session, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router that contains the BGP session to update.

  3. On the **Router details** page, select the BGP session to update.

  4. On the **BGP session details** page, click edit**Edit**.

  5. Find the advertised routes to delete, and then next to each route, click delete**Delete**.

  6. After you finish deleting the routes, click **Save**.




###  gcloud 

**Remove Google-defined advertisement groups**

To remove advertisement groups, use the `gcloud compute routers update-bgp-peer` command with the `--remove-advertisement-groups` flag. You can remove any existing advertisement groups.
    
    
     gcloud compute routers update-bgp-peer ROUTER_NAME \
         --peer-name=PEER_NAME \
         --remove-advertisement-groups=ADVERTISED_GROUPS
    

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `PEER_NAME`: the name of your BGP peer

  * `ADVERTISED_GROUPS`: a Google-defined group that Cloud Router dynamically advertises

The only valid value is `all_subnets`, which advertises subnets based on the VPC network's dynamic routing mode (similar to default advertisement mode).




For a list of all advertisement groups, see the [`set-advertisement-groups` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create) in the Google SDK documentation.

The following example updates the `my-bgp-session` BGP session on the `my-router` Cloud Router to remove the `all_subnets` advertisement group:
    
    
     gcloud compute routers update-bgp-peer my-router \
         --peer-name my-bgp-session \
         --remove-advertisement-groups all_subnets
    

**Remove existing IP ranges**

To remove existing IP address ranges that are being advertised, such as static external IP addresses or subnet IP address ranges, use the `gcloud compute routers update-bgp-peer` command with the `--remove-advertisement-ranges` flag:
    
    
     gcloud compute routers update-bgp-peer ROUTER_NAME \
         --peer-name=PEER_NAME \
         --remove-advertisement-ranges=ADVERTISED_IP_RANGES
    

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `PEER_NAME`: the name of your BGP peer

  * `ADVERTISED_IP_RANGES`: the contents of the new array of IP address ranges

You can specify both IPv4 and IPv6 custom IP address ranges. However, IPv6 custom ranges are advertised only in BGP sessions where IPv6 is enabled.




The following example updates the `my-bgp-session` BGP session on the `my-router` Cloud Router to remove the existing `10.0.10.0/24` subnet IP range:
    
    
     gcloud compute routers update-bgp-peer my-router \
         --peer-name my-bgp-session \
         --remove-advertisement-ranges 10.0.10.0/24
    

###  API 

To update the `bgpPeers[]` field, use the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch).

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. For each BGP peer that you want to remove custom advertised routes for, do the following:

     * Remove any IP address range advertisements that you do not want from the `bgpPeers[].advertisedIpRanges[]` field.
     * Remove any group advertisements that you do not want from the `bgpPeers[].advertisedGroups[]` field.
    
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

In the following example, the first BGP peer includes values for the `advertisedGroups[]` and `advertisedIpRanges[]` fields. For the second BGP peer, custom advertised routes have been removed and the `advertiseMode` has been reverted to `DEFAULT`.
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "advertisedRoutePriority": 100,
          "advertiseMode": "CUSTOM",
          **"advertisedGroups": ["ALL_SUBNETS"],
          "advertisedIpRanges": [
            {
              "range": "1.2.3.4",
              "description": "First example range"
            },
            {
              "range": "6.7.0.0/16",
              "description": "Second example range"
            }
          ]**
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

  * To view the configuration of a Cloud Router, its BGP sessions, and the routes that the Cloud Router is advertising, see [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).

  * To troubleshoot issues with custom advertised routes, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
