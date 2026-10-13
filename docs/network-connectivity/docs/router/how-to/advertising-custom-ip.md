---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip/
title: Advertise custom address ranges \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:53.093671+00:00
---

# Advertise custom address ranges  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Advertise custom address ranges

Use custom advertisement mode in a Cloud Router or a Border Gateway Protocol (BGP) session on a Cloud Router to advertise IP address ranges other than your Virtual Private Cloud (VPC) network's subnet IP address ranges. For example, you can advertise external IP address ranges, arbitrary internal IP address ranges, or internal IP addresses from IP address ranges from other VPC networks that are connected to your VPC network. Your VPC network might be connected through VPC Network Peering or VPC spokes in Network Connectivity Center.

When a Cloud Router is configured to use default advertisement mode, it only advertises routes for subnets that are part of the same VPC network as the Cloud Router. In this mode, Cloud Router excludes any static routes and routes that are learned dynamically from other VPC networks, such as routes learned by VPC Network Peering or by VPC spokes in NCC.

**Caution:** You can specify custom advertised routes on a Cloud Router and on a BGP session. Custom advertised routes on the Cloud Router apply to all of its BGP sessions. However, if you specify any custom advertised route on a BGP session, all of the Cloud Router's advertised routes are ignored and overridden by the BGP session's custom advertised route.

To specify custom advertised routes when you create a Cloud Router or configure a BGP session, see [Create Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/docs/how-to/creating-routers) or [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/docs/how-to/configuring-bgp).

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

  5. Select the **Advertise all subnets visible to the Cloud Router** checkbox to continue advertising the subnets available to the Cloud Router. Enabling this option mimics the behavior of Cloud Router in default advertisement mode.

  6. Select **Add custom route** to add an advertised route.

  7. Configure the custom advertised routes:

     * **Source** : Select **Custom IP range**.

     * **IP address range** : Use CIDR notation to specify the custom IP range.

You can specify both IPv4 and IPv6 custom IP ranges. However, IPv6 custom ranges are advertised only in BGP sessions where IPv6 is enabled.

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

     * **Description** : Add a description to help you identify the purpose of this custom advertised route, and then click **Done**.

  8. After you finish adding custom advertised routes, click **Save**.




###  gcloud 

Run the `update` command. To specify the custom IP ranges, use the `--set-advertisement-ranges` flag or the `--add-advertisement-ranges` flag.

  1. Use the `--set-advertisement-ranges` flag; any existing custom advertisements are replaced:
         
         gcloud compute routers update ROUTER_NAME \
            --project=PROJECT_ID \
            --advertisement-mode custom \
            --set-advertisement-groups=ADVERTISED_GROUPS \
            --set-advertisement-ranges=ADVERTISED_IP_RANGES
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router
     * `PROJECT_ID`: the project that contains the Cloud Router
     * `ADVERTISED_GROUPS`: a Google-defined group that Cloud Router dynamically advertises

The only valid value is `all_subnets`, which advertises subnets based on the VPC network's dynamic routing mode (similar to default advertisement mode).

     * `ADVERTISED_IP_RANGES`: the contents of the new array of IP address ranges

You can specify both IPv4 and IPv6 custom IP ranges. However, IPv6 custom ranges are advertised only in BGP sessions where IPv6 is enabled.

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

The following example updates the `my-router` Cloud Router to advertise all subnets and the custom IP ranges `192.0.2.0/24` and `198.51.100.0/24`:
    
    gcloud compute routers update my-router \
       --advertisement-mode custom \
       --set-advertisement-groups=all_subnets \
       --set-advertisement-ranges='192.0.2.0/24,198.51.100.0/24'
    

The following example updates the `my-router` Cloud Router to advertise all subnets and the default IPv6 range:
    
    gcloud compute routers update my-router \
       --advertisement-mode custom \
       --set-advertisement-groups=all_subnets \
       --set-advertisement-ranges='2001:db8:abcd:12::/64'
    

Cloud Router advertises IPv6 ranges only in BGP sessions that are enabled for IPv6.

The `--set-advertisement-groups` flag accepts Google-defined groups that the Cloud Router dynamically advertises. You can remove the `--set-advertisement-groups` flag to exclude subnet advertisements. For a list of all advertisement groups, see the [`set-advertisement-groups`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create) flag in the Google SDK documentation.

  2. Use the `--add-advertisement-ranges` flag, which requires the Cloud Router's advertisement mode to already be set to `custom`:
         
         gcloud compute routers update ROUTER_NAME \
            --add-advertisement-ranges=ADVERTISED_IP_RANGES
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router
     * `ADVERTISED_IP_RANGES`: the contents of the new array of IP address ranges

The following example adds the `203.0.113.1` custom IP address to the Cloud Router's advertisements:
    
    gcloud compute routers update my-router \
       --add-advertisement-ranges='203.0.113.1'
    

The following example adds the `2001:db8:abcd:12::/64` custom IPv6 range to the Cloud Router's advertisements:
    
    gcloud compute routers update my-router \
       --add-advertisement-ranges='2001:db8:abcd:12::/64'
    

Cloud Router advertises IPv6 ranges only in BGP sessions that are enabled for IPv6.




###  API 

Use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgp.advertisedGroups[]` and `bgp.advertisedIpRanges[]` fields.

The `bgp.advertisedGroups[]` and `bgp.advertisedIpRanges[]` fields store arrays of advertised groups and advertised IP address ranges. When you `PATCH` these fields, you overwrite the existing arrays with the new ones in your request.

  1. Send a `GET` request to get the current arrays of advertised groups and advertised IP address ranges on the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with new arrays of advertised groups and advertised IP address ranges. Use the arrays from the `GET` request in the previous step, and add any groups or IP address ranges that you want on the router.
         
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
     * `ADVERTISED_GROUPS`: a Google-defined group that Cloud Router dynamically advertises

The only valid value is `ALL_SUBNETS`, which advertises subnets based on the VPC network's dynamic routing mode (similar to the default advertisements).

     * `ADVERTISED_IP_RANGES`: the contents of the new array of IP address ranges

You can specify both IPv4 and IPv6 custom IP ranges. However, IPv6 custom ranges are advertised only in BGP sessions where IPv6 is enabled.

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

The following example contains two IPv4 address ranges and one IPv6 address range:
    
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

  6. Select the **Advertise all subnets visible to the Cloud Router** checkbox to continue advertising the subnets available to the Cloud Router. Enabling this option mimics the Cloud Router's default behavior.

  7. Select **Add custom route** to add an advertised route.

  8. Configure the route advertisement:

     * **Source** : Select **Custom IP range**.

     * **IP address range** : Use CIDR notation to specify the custom IP range. You can specify both IPv4 and IPv6 custom IP ranges. However, IPv6 custom ranges are advertised only in BGP sessions where IPv6 is enabled.

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

     * **Description** : Add a description to help you identify the purpose of this route advertisement, and then click **Done**.

  9. After you finish adding custom routes, click **Save**.




###  gcloud 

Run the `update-bgp-peer` command. To specify the custom IP ranges, use the `--set-advertisement-ranges` flag or the `--add-advertisement-ranges` flag.

  1. Use the `--set-advertisement-ranges` flag; any existing custom advertisements are replaced:
         
         gcloud compute routers update-bgp-peer ROUTER_NAME \
             --peer-name=PEER_NAME \
             --advertisement-mode custom \
             --set-advertisement-groups=ADVERTISED_GROUPS \
             --set-advertisement-ranges=ADVERTISED_IP_RANGES
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router
     * `PEER_NAME`: the name of your BGP peer
     * Optionally, add the `--enable-ipv6` flag if you are adding custom IPv6 ranges.
     * `ADVERTISED_GROUPS`: a Google-defined group that Cloud Router dynamically advertises

The only valid value is `all_subnets`, which advertises subnets based on the VPC network's dynamic routing mode (similar to the default advertisements).

     * `ADVERTISED_IP_RANGES`: the contents of the new array of IP address ranges

You can specify both IPv4 and IPv6 custom IP ranges. However, IPv6 custom ranges are advertised only in BGP sessions where IPv6 is enabled.

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

The following example updates the `my-bgp-session` BGP session on the `my-router` Cloud Router to advertise all subnets and the custom IP ranges `192.0.2.1`, `198.51.100.0/24`, and `2001:db8:abcd:12::/64`.
    
    gcloud compute routers update-bgp-peer my-router \
        --peer-name my-bgp-session \
        --enable-ipv6 \
        --advertisement-mode custom \
        --set-advertisement-groups=all_subnets \
        --set-advertisement-ranges='192.0.2.1,198.51.100.0/24,2001:db8:abcd:12::/64'
    

The `--set-advertisement-groups` flag accepts Google-defined groups that the BGP session dynamically advertises. You can remove the `--add-advertisement-groups` flag to exclude subnet advertisements. For a list of all advertisement groups, see the [`set-advertisement-groups`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create) flag in the Google SDK documentation.

  2. Use the `--add-advertisement-ranges` flag, which requires the Cloud Router's advertisement mode to already be set to `custom`:
         
         gcloud compute routers update-bgp-peer ROUTER_NAME \
             --peer-name=PEER_NAME \
             --add-advertisement-ranges=ADVERTISED_IP_RANGES
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router
     * `PEER_NAME`: the name of your BGP peer
     * `ADVERTISED_IP_RANGES`: the contents of the new array of IP address ranges

You can specify both IPv4 and IPv6 custom IP ranges. However, IPv6 custom ranges are advertised only in BGP sessions where IPv6 is enabled.

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

The following example adds the `198.51.100.1` custom IP address to the Cloud Router's advertisements:
    
    gcloud compute routers update-bgp-peer my-router \
        --peer-name my-bgp-session \
        --add-advertisement-ranges='198.51.100.1'
    

The following example adds the `2001:db8:abcd:12::/64` custom IPv6 address to the Cloud Router's advertisements:
    
    gcloud compute routers update-bgp-peer my-router \
        --peer-name my-bgp-session \
        --enable-ipv6 \
        --add-advertisement-ranges='2001:db8:abcd:12::/64'
    




###  API 

Use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgpPeers[]` field.

The `bgpPeers[]` field accepts an array of BGP peers. When you `PATCH` this field, you overwrite the existing array of BGP peers with the new array included in your request.

  1. Send a `GET` request to get the current array of BGP peers for the router. For details, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#bgp-configuration).

  2. Send a `PATCH` request with a new array of BGP peers. For each BGP peer for which you want to add advertisements, do the following:

     * Add any IP address range advertisements that you want in the `bgpPeers[].advertisedIpRanges[]` field.
     * Add any group advertisements that you want in the `bgpPeers[].advertisedGroups[]` field.

The only valid value is `ALL_SUBNETS`, which advertises subnets based on the VPC network's dynamic routing mode (similar to default advertisement mode).

For more information about these values, see [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) in the API documentation.
    
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

The following example contains two BGP peers with custom advertisements:
    
    {
          "name": "peer-1",
          "interfaceName": "if-peer-1",
          "ipAddress": "169.254.10.1",
          "peerIpAddress": "169.254.10.2",
          "peerAsn": 64512,
          "enableIpv6": true,
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
            },
            {
              "range": "2001:db8:abcd:12::/64",
              "description: "Third example range"
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
          **"advertisedIpRanges": [
            {
              "range": "192.168.10.0/24",
              "description": "Fourth example range"
            }
          ]**
        }
    




## What's next

  * To view the configuration of a Cloud Router, its BGP sessions, and the routes that Cloud Router is advertising, see [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).

  * To troubleshoot issues with custom advertised routes, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
