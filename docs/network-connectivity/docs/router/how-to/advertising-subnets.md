---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-subnets/
title: Advertise specific VPC subnets \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:14.021147+00:00
---

# Advertise specific VPC subnets  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-subnets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Advertise specific VPC subnets

You can create custom advertised routes to limit the subnets in your Virtual Private Cloud (VPC) network that the Cloud Router advertises. The subnets that you advertise are the only ones visible to on-premises clients. Cloud Router doesn't dynamically advertise new subnets unless you configure Cloud Router to advertise all subnets. If you choose to advertise only specific subnets and want to advertise new subnets, you must add them as custom advertised routes.

For IPv6-enabled BGP sessions, you can configure custom advertised routes for specific internal (ULA) and external (GUA) IPv6 subnet ranges. For information about IPv6 subnet types, see [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

To specify custom advertised routes when you create a Cloud Router or configure a BGP session, see [Create Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/creating-routers) or [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp).

## Before you begin

###  gcloud 

If you want to use the command-line examples in this guide, do the following:

  1. Install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
  2. Set a [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



###  API 

If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/compute/docs/api/prereqs).

## Specify custom advertised routes on a Cloud Router

To specify custom advertised routes on an existing Cloud Router, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router to update.

  3. On the **Router details** page, click edit**Edit**.

  4. In the **Advertised routes** section, for **Routes** , select **Create custom routes**.

  5. If the **Advertise all subnets visible to the Cloud Router** checkbox is selected, clear it.

  6. Select **Add custom route** to add a custom advertised route.

  7. Configure the custom advertised route:

     * **Source** : Select a predefined list of subnets. Cloud Router lists all subnets available to it, which depends on the VPC network's dynamic routing mode.
     * **IP address range** : You can modify the advertised subnet IP range. For example, you can specify a more narrow range so that the Cloud Router advertises part of the subnet. You can specify both IPv4 and IPv6 custom IP ranges. However, IPv6 custom ranges are advertised only in BGP sessions where IPv6 is enabled.

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

     * **Description** : Add a description to help you identify the purpose of this custom advertised route, and then click **Done**.

  8. After you finish adding custom advertised routes, click **Save**.




###  gcloud 

Before you begin, record the IP ranges of the subnets to advertise.

Run the `update` command. To specify the subnet IP ranges to advertise, use the `--set-advertisement-ranges` flag. To append IP ranges to existing advertisements, use the `--add-advertisement-ranges` flag.

  1. Use the `--set-advertisement-ranges` flag; any existing custom advertised routes are replaced:
         
         gcloud compute routers update ROUTER_NAME \
            --advertisement-mode custom \
            --set-advertisement-ranges=ADVERTISED_IP_RANGES
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router

     * `ADVERTISED_IP_RANGES`: the contents of the new array of IP address ranges. You can specify both IPv4 and IPv6 custom IP ranges. However, IPv6 custom ranges are advertised only in BGP sessions where IPv6 is enabled.

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

The following example updates the `my-router` Cloud Router to advertise the `192.0.2.0/24` and `198.51.100.0/24` subnets; existing custom advertised routes are replaced:
    
    gcloud compute routers update my-router \
       --advertisement-mode=custom \
       --set-advertisement-ranges='192.0.2.0/24,198.51.100.0/24'
    

The following example updates the `my-router` Cloud Router to advertise the `192.0.2.0/24` and `198.51.100.0/24` IPv4 subnets, plus the `2001:db8:abcd:12::/64` IPv6 subnet:
    
    gcloud compute routers update my-router \
       --advertisement-mode=custom \
       --set-advertisement-ranges='192.0.2.0/24,198.51.100.0/24,2001:db8:abcd:12::/64'
    

Cloud Router advertises IPv6 ranges only in BGP sessions that are enabled for IPv6.

  2. The following example uses the `--add-advertisement-ranges` flag to append IP ranges to an existing advertisement:
         
         gcloud compute routers update my-router \
            --add-advertisement-ranges='203.0.113.0/24'
         

The following example adds the `2001:db8:abcd:12::/64` custom IPv6 range to the Cloud Router's advertisements:
         
         gcloud compute routers update my-router \
            --add-advertisement-ranges='2001:db8:abcd:12::/64'
         

Cloud Router advertises IPv6 ranges only in BGP sessions that are enabled for IPv6.




If the advertisement group of your Cloud Router includes all subnets, remove it to prevent the Cloud Router from advertising additional subnets. Advertisement groups are Google-defined IP ranges that the Cloud Router dynamically advertises. For a list of all advertisement groups, see the [`set-advertisement-groups`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create) flag in the Google SDK documentation.

  1. The following example uses the `describe` command to check the Cloud Router's advertised routes:
         
         gcloud compute routers describe my-router
         

  2. If the output contains the `advertisedGroups` field with the value `all_subnets`, remove it. The following example uses the `update` command with the `--remove-advertisement-groups` flag:
         
         gcloud compute routers update my-router \
            --remove-advertisement-groups all_subnets
         




###  API 

Use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgp.advertisedIpRanges[]` field. You might also need to update the `bgp.advertisedGroups[]` field if it currently has a value of `ALL_SUBNETS`.

The `bgp.advertisedGroups[]` and `bgp.advertisedIpRanges[]` fields accept arrays of advertised groups and advertised IP address ranges. When you `PATCH` these fields, you overwrite the existing arrays with the new ones in your request.

  1. Send a `GET` request to get the current arrays of advertised groups and advertised IP ranges on the router. For details, see [Viewing Cloud Router status and routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#viewing-router-status).

  2. Send a `PATCH` request with new arrays of advertised groups and advertised IP address ranges:

     * Add any subnet IP address ranges that you want on the router to the `bgp.advertisedIpRanges[]` field.
     * If the `advertisedGroups[]` field currently specifies the value `ALL_SUBNETS`, remove it by sending an empty array as shown in the following example. This prevents Cloud Router from advertising additional subnets.
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
    {
      "bgp": {
        "advertisedGroups": [],
        "advertisedIpRanges": [
        ADVERTISED_IP_RANGES
       ]
     }
    }
    

Replace the following:

     * `PROJECT_ID`: the project that contains the Cloud Router
     * `REGION`: the region where the Cloud Router is located
     * `ROUTER_NAME`: the name of the Cloud Router
     * `ADVERTISED_IP_RANGES`: the contents of the new array of IP address ranges. You can specify IPv6 custom IP address ranges in addition to IPv4 address ranges. However, IPv6 ranges are advertised only if you enable IPv6 exchange for this BGP session.

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

The following example contains two subnet IPv4 address ranges and one IPv6 address range:
    
    {
          "range": "192.0.2.0/24",
          "description": "First example range"
        },
        {
          "range": "198.51.100.0/24",
          "description": "Second example range"
        },
        {
          "range": "2001:db8:abcd:12::/64",
          "description: "Third example range"
        }
    




## Specify custom advertised routes for a BGP session

To specify custom advertised routes for an existing BGP session, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router that contains the BGP session to update.

  3. On the **Router details** page, select the BGP session to update.

  4. On the **BGP session details** page, click edit**Edit**.

  5. For **Routes** , select **Create custom routes**.

  6. If the **Advertise all subnets visible to the Cloud Router** checkbox is selected, clear it.

  7. Select **Add custom route** to add an advertised route.

  8. Configure the custom advertised route:

     * **Source** : Select a predefined list of subnets. Cloud Router lists all subnets available to it, which depends on the VPC network's dynamic routing mode.

     * **IP address range** : You can modify the advertised subnet IP range. For example, you can specify a more narrow range so that the Cloud Router advertises part of the subnet. You can specify IPv6 custom IP address ranges in addition to IPv4 address ranges. However, IPv6 ranges are advertised only if you enable IPv6 exchange for this BGP session.

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

     * **Description** : Add a description to help you identify the purpose of this custom advertised route, and then click **Done**.

  9. After you finish adding custom routes, click **Save**.




###  gcloud 

Before you begin, record the IP ranges of the subnets to advertise.

Run the `update-bgp-peer` command. To specify the subnet IP ranges to advertise, use the `--set-advertisement-ranges` flag. To append IP ranges to existing advertisements, use the `--add-advertisement-ranges` flag.

  1. Use the `--set-advertisement-ranges` flag; any existing custom advertisements are replaced:
         
         gcloud compute routers update-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME \
            --advertisement-mode=custom \
            --set-advertisement-ranges=ADVERTISED_IP_RANGES
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router
     * `PEER_NAME`: the name of your BGP peer
     * Optionally, add the `--enable-ipv6` flag if you are adding custom IPv6 ranges.
     * `ADVERTISED_IP_RANGES`: the contents of the new array of IP address ranges. You can specify both IPv4 and IPv6 custom IP ranges. However, IPv6 custom ranges are advertised only in BGP sessions where IPv6 is enabled.

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

The following example updates the `my-bgp-session` BGP session on the `my-router` Cloud Router to advertise the `192.0.2.0/24`, `198.51.100.0/24` and `2001:db8:abcd:12::/64` subnets; existing custom advertised routes are replaced:
    
    gcloud compute routers update-bgp-peer my-router \
       --peer-name my-bgp-session \
       --enable-ipv6 \
       --advertisement-mode=custom \
       --set-advertisement-ranges='192.0.2.0/24,198.51.100.0/24,2001:db8:abcd:12::/64'
    

  2. The following example uses the `--add-advertisement-ranges` flag to append IP ranges to an existing advertisement:
         
         gcloud compute routers update-bgp-peer my-router \
            --peer-name my-bgp-session \
            --add-advertisement-ranges='203.0.113.0/24'
         

The following example adds the `2001:db8:abcd:12::/64` custom IPv6 address to the Cloud Router's advertised routes:
         
         gcloud compute routers update-bgp-peer my-router \
             --peer-name my-bgp-session \
             --enable-ipv6 \
             --add-advertisement-ranges='2001:db8:abcd:12::/64'
         




If the advertisement group of your BGP session includes all subnets, remove it to prevent the Cloud Router from advertising additional subnets. Advertisement groups are Google-defined IP ranges that the Cloud Router dynamically advertises. For a list of all advertisement groups, see the [`set-advertisement-groups`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create) flag in the Google SDK documentation.

  1. The following example uses the `describe` command to check the Cloud Router's advertised routes:
         
         gcloud compute routers describe my-router
         

  2. If the related BGP session contains the `advertisedGroups` field with the value `all_subnets`, remove it. The following example uses the `update` command with the `--remove-advertisement-groups` flag:
         
         gcloud compute routers update-bgp-peer my-router \
            --peer-name my-bgp-session \
            --remove-advertisement-groups=all_subnets
         




###  API 

Use the [routers.patch](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. For each BGP peer for which you want to add custom advertised routes, do the following:

     * Add any subnet IP address range advertisements that you want to the `bgpPeers[].advertisedIpRanges[]` field.

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

     * If the `bgpPeers[].advertisedGroups[]` field currently specifies the value `ALL_SUBNETS`, remove it to prevent the BGP session from advertising additional subnets.
    
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

The following example contains two BGP peers with custom advertised routes:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "enableIpv6": true,
          "advertisedRoutePriority": 100,
          "advertiseMode": "CUSTOM",
          **"advertisedGroups": [],
          "advertisedIpRanges": [
            {
              "range": "192.0.2.0/24",
              "description": "First example subnet"
            },
            {
              "range": "198.51.100.0/24",
              "description": "Second example subnet"
            },
            {
              "range": "2001:db8:abcd:12::/64",
              "description: "Third example subnet"
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
          "advertiseMode": "CUSTOM",
          **"advertisedGroups": [],
          "advertisedIpRanges": [
            {
              "range": "203.0.113.0/24",
              "description": "Fourth example subnet"
            }
          ]**
        }
    




## What's next

  * To view the configuration of a Cloud Router, its BGP sessions, and the routes that Cloud Router is advertising, see [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).

  * To troubleshoot issues with custom advertised routes, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
