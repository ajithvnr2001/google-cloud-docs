---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes/
title: Specify and manage custom learned routes \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:17.965160+00:00
---

# Specify and manage custom learned routes  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Specify and manage custom learned routes

Cloud Router learns routes for egress traffic dynamically from its Border Gateway Protocol (BGP) peers. However, you can also manually create such routes and apply them to a BGP session. These manually created routes are called _custom learned routes_.

You can create custom learned routes at the same time that you create a BGP session. Alternatively, you can update an existing BGP session to add custom learned routes.

For an overview of custom learned routes, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).

For information about how Cloud Router handles learned routes in general, including routes that are learned dynamically, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#egress).

## Before you begin

Before you get started, review the following sections.

### Select a project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. If you are using the Google Cloud CLI, set your project ID by running the following command. The `gcloud` instructions on this page assume that you have set your project ID. 
         
         gcloud config set project PROJECT_ID
             

  13. Confirm that the ID was set by running the following command: 
         
         gcloud config list --format='text(core.project)'
             




### Requirements for IPv6 (optional)

If you want your custom learned routes to include IPv6 prefixes, your connectivity resource must meet the underlying conditions for IPv6. For example, if you're establishing custom learned routes for a VPN tunnel, make sure that you meet the conditions described in [IPv6 support](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ipv6_support) in the Cloud VPN overview.

## Define custom learned routes while creating a session

For some Network Connectivity products, you can configure a BGP peer to include custom learned routes while you're creating the resource. For other resources, you create the BGP session first and then add the custom learned routes later.

For more information about how to add custom learned routes while creating a session, see the following:

  * [Create an HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#create_bgp_sessions)
  * [Create VLAN attachments (Dedicated Interconnect)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#creating_vlan_attachments)



If you're creating a Partner Interconnect VLAN attachment, [create the attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#creating_vlan_attachments) first, and then update the BGP peer to add custom learned routes.

If you're installing a third-party network virtual appliance by using Network Connectivity Center and you want to use custom learned routes, first install the appliance. Then, for each custom learned route that you want to use, sign in to the appliance and configure your Router appliance instance to use the custom learned routes. After that, you can update the BGP session to use custom learned routes. For more information, see [Use custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances#use-custom-learned-routes) in the Network Connectivity Center documentation.

When you update a Cloud Router session, the Cloud Router checks for any overlaps between custom learned routes and VPC subnets. If there is an overlap, the VPC subnet takes precedence. This means that traffic is routed through the VPC subnet instead of the custom learned route. Cloud Router ignores BGP and custom learned routes that are more specific than or equal to the VPC subnet. For more information about routing in Google Cloud, see [Routes](https://docs.cloud.google.com/vpc/docs/routes).

If a BGP route and a custom learned route both match the same destination IP address, Google Cloud gives greater preference to routes that have smaller MED value. Lower MED values indicate higher priority.

For information about how to add custom learned routes while updating a BGP session, see the following section.

## Update an existing session to use custom learned routes

If you have an existing BGP session that has no custom learned routes defined, you can optionally update it to use custom learned routes.

You can also use this procedure if you have already configured custom learned routes for a session, but you want to add to the IP prefix that you previously specified.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. In the **Name** field, click the name of the appropriate Cloud Router.

  3. On the **Router details** page, click the name of the BGP session that you want to modify.

  4. On the **BGP session details** page, click edit**Edit**.

  5. Expand the **Advertised routes, custom learned routes, bidirectional forwarding detection (BFD)** section.

  6. In the **Custom learned routes** section, do the following:

     1. In the **Priority of all custom learned routes** section, to configure the route priority, enter a MED value between `0` and `65535` (inclusive) for all the custom learned routes configured for this session.

Google Cloud gives greater preference to routes that have smaller MED values. If the same IP address range is configured in multiple custom learned routes, the best path selection is based on the route's MED value.

     2. Click **Add new IP address range**.

     3. In the **IP address range** field, enter an IPv4 or IPv6 address. If you provide an IP address without a subnet mask, it is interpreted as a `/32` subnet mask (for IPv4) and a `/128` subnet mask (for IPv6).

  7. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers update-bgp-peer` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer):
    
    
      gcloud compute routers update-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME \
          --region=REGION \
          --add-custom-learned-route-ranges=IP_PREFIXES \
          --custom-learned-route-priority=ROUTE_PRIORITY

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `PEER_NAME`: the name of the BGP peer
  * `REGION`: the region where the Cloud Router is located
  * `IP_PREFIXES`: a list of comma-separated IPv4 or IPv6 address prefixes—for example, `192.0.2.0/24,198.51.100.0/24,2001:db8:abcd:12::/64`

If you provide an IP address prefix without a subnet mask, it is interpreted as a `/32` subnet mask for IPv4 and a `/128` subnet mask for IPv6. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

  * `ROUTE_PRIORITY`: a MED value between `0` and `65535` (inclusive) for all the custom learned routes configured for this session

Google Cloud gives greater preference to routes that have smaller MED values. That is, a route with a MED value of `100` is given greater preference than one with a MED value of `200`. If you don't provide a MED value, internally Google Cloud applies a MED value of `100`.




###  API 

Use the [`compute.routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) and update the `bgpPeers` array.

When you patch the `bgpPeers` array, you must provide values for every field on every item (unless you want to remove some BGP peers or some values).

For example, suppose the Cloud Router has two BGP peers. To leave the first BGP peer unchanged but add two custom learned routes to the second BGP peer, use a request like the following:
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
      {
        "bgpPeers": [
          {
            "name": "PEER_NAME_1",
            "interfaceName": "INTERFACE_NAME_1",
            "ipAddress": "IP_ADDRESS_1",
            "peerIpAddress": "PEER_IP_ADDRESS_1",
            "peerAsn": "PEER_ASN_1"
          },
          {
            "name": "PEER_NAME_2",
            "interfaceName": "INTERFACE_NAME_2",
            "ipAddress": "IP_ADDRESS_2",
            "peerIpAddress": "PEER_IP_ADDRESS_2",
            "peerAsn": "PEER_ASN_2",
            "customLearnedRoutePriority": "ROUTE_PRIORITY",
            "customLearnedIpRanges": [
             {
              "range": "IP_PREFIX_1"
             },
             {
              "range": "IP_PREFIX_2"
             }
           ]
          }
        ]
      }

Replace the placeholder values as follows.

Provide values about the Cloud Router:

  * `PROJECT_ID`: the project that contains the Cloud Router
  * `REGION`: the region where the Cloud Router is located
  * `ROUTER_NAME`: the name of the Cloud Router



Provide values about the BGP peering session that you are _not_ changing:

  * `PEER_NAME_1`: the name of the BGP session
  * `INTERFACE_NAME_1`: the name of the interface that the session uses
  * `IP_ADDRESS_1`: the Cloud Router IP address that the BGP session uses
  * `PEER_IP_ADDRESS_1`: the IP address of the BGP peer
  * `PEER_ASN_1`: the autonomous system number (ASN) for the session



Provide values about the BGP peering session to which you want to add custom learned routes:

  * `PEER_NAME_2`: the name of the BGP session
  * `INTERFACE_NAME_2`: the name of the interface that the session uses
  * `IP_ADDRESS_2`: the Cloud Router IP address that the BGP session uses
  * `PEER_IP_ADDRESS_2`: the IP address of the BGP peer
  * `PEER_ASN_2`: the autonomous system number (ASN) for the session
  * `ROUTE_PRIORITY`: a MED value between `0` and `65535` (inclusive) for all the custom learned routes configured for this session

Google Cloud gives greater preference to routes that have smaller MED values. That is, a route with a MED value of `100` is given greater preference than one with a MED value of `200`. If you don't provide a MED value, internally Google Cloud applies a MED value of `100`.

  * `IP_PREFIX_1` and `IP_PREFIX_2`: for each of these fields, enter an IPv4 or IPv6 prefix

If you provide an IP prefix without a subnet mask, it is interpreted as, for IPv4, a `/32` subnet mask and, for IPv6, `/128`. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).




## Overwrite existing custom learned routes

If you want to replace the custom learned routes that are defined for a BGP session, use the following guidance. When you use this procedure, existing custom learned routes are discarded in favor of the new routes that you define.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. In the **Name** field, click the name of the appropriate Cloud Router.

  3. On the **Router details** page, click the name of the BGP session that you want to modify.

  4. On the **BGP session details** page, click edit**Edit**.

  5. Expand the **Advertised routes, custom learned routes, bidirectional forwarding detection (BFD)** section.

  6. In the **IP address range** field, edit the IPv4 or IPv6 prefix. If you provide an IP prefix without a subnet mask, it is interpreted as a `/32` subnet mask (for IPv4) and a `/128` subnet mask (for IPv6).

  7. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers update-bgp-peer` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer). You can use the `set-custom-learned-route-ranges` flag to specify new IP prefixes or to clear previously defined prefixes:
    
    
      gcloud compute routers update-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME \
          --region=REGION \
          --set-custom-learned-route-ranges=IP_PREFIXES

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `PEER_NAME`: the name of the BGP peer
  * `REGION`: the region where the Cloud Router is located
  * `IP_PREFIXES`: a list of comma-separated IPv4 or IPv6 prefixes—for example, `1.2.3.4,6.7.0.0,2001:db8:abcd:12::/64`

If you provide an IP prefix without a subnet mask, it is interpreted as, for IPv4, a `/32` subnet mask and, for IPv6, `/128`. To clear all prefixes, use the flag with no value after it. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).




###  API 

Use the [`compute.routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) and update the `bgpPeers` array.

When you patch the `bgpPeers` array, you must provide values for every field on every item (unless you want to remove some BGP peers or some values).

For example, suppose the Cloud Router has two peers. Suppose that one does not use custom learned routes but the other does. To leave the first peer unchanged but overwrite the routes that are defined for the second peer, use a request like the following:
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
      {
        "bgpPeers": [
          {
            "name": "PEER_NAME_1",
            "interfaceName": "INTERFACE_NAME_1",
            "ipAddress": "IP_ADDRESS_1",
            "peerIpAddress": "PEER_IP_ADDRESS_1",
            "peerAsn": "PEER_ASN_1"
          },
          {
            "name": "PEER_NAME_2",
            "interfaceName": "INTERFACE_NAME_2",
            "ipAddress": "IP_ADDRESS_2",
            "peerIpAddress": "PEER_IP_ADDRESS_2",
            "peerAsn": "PEER_ASN_2",
            "customLearnedRoutePriority": "ROUTE_PRIORITY",
            "customLearnedIpRanges": [
              {
               "range": "IP_PREFIX_1"
              },
              {
               "range": "IP_PREFIX_2"
              }
             ]
           }
         ]
       }

Replace the placeholder values as follows.

Provide values about the Cloud Router:

  * `PROJECT_ID`: the project that contains the Cloud Router
  * `REGION`: the region where the Cloud Router is located
  * `ROUTER_NAME`: the name of the Cloud Router



Provide values about the BGP peering session that you are _not_ changing:

  * `PEER_NAME_1`: the name of the BGP session
  * `INTERFACE_NAME_1`: the name of the interface that the session uses
  * `IP_ADDRESS_1`: the Cloud Router IP address that the session uses
  * `PEER_IP_ADDRESS_1`: the IP address of the BGP peer
  * `PEER_ASN_1`: the autonomous system number (ASN) for the session



Provide values about the BGP peering session to which you want to overwrite the custom learned routes:

  * `PEER_NAME_2`: the name of the BGP session
  * `INTERFACE_NAME_2`: the name of the interface that the session uses
  * `IP_ADDRESS_2`: the Cloud Router IP address that the session uses
  * `PEER_IP_ADDRESS_2`: the IP address of the BGP peer
  * `PEER_ASN_2`: the autonomous system number (ASN) for the session
  * `ROUTE_PRIORITY`: a MED value between `0` and `65535` (inclusive) for all the custom learned routes configured for this session

Google Cloud gives greater preference to routes that have smaller MED values. That is, a route with a MED value of `100` is given greater preference than one with a MED value of `200`. If you don't provide a MED value, internally Google Cloud applies a MED value of `100`.

  * `IP_PREFIX_1` and `IP_PREFIX_2`: for each of these fields, enter an IPv4 or IPv6 prefix

If you provide an IP address without a subnet mask, it is interpreted as, for IPv4, a `/32` subnet mask and, for IPv6, `/128`. For information about the maximum number of custom learned routes that you can have, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).




## Remove custom learned routes from a BGP session

To remove some or all of the custom learned routes from a BGP session, use the following guidance.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. In the **Name** field, click the name of the appropriate Cloud Router.

  3. On the **Router details** page, click the name of the BGP session that you want to modify.

  4. On the **BGP session details** page, click edit**Edit**.

  5. Expand the **Advertised routes, custom learned routes, bidirectional forwarding detection (BFD)** section.

  6. In the **Custom learned routes** section, next to the **IP address range** that you want to remove, click delete**Delete IP range**.

  7. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers update-bgp-peer` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer):
    
    
      gcloud compute routers update-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME \
          --region=REGION \
          --remove-custom-learned-route-ranges=IP_PREFIXES

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `PEER_NAME`: the name of the BGP peer
  * `REGION`: the region where the Cloud Router is located
  * `IP_PREFIXES`: a comma-separated list of the IP prefixes that you want to remove



###  API 

Use the [`compute.routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) and update the `bgpPeers` array.

When you patch the `bgpPeers` array, you must provide values for every field on every item (unless you want to remove some BGP peers or some values).

For example, suppose the Cloud Router has two BGP peers. Suppose that one does not use custom learned routes but the other does. To leave the first peer unchanged and remove the routes that are defined for the second peer, use a request like the following:
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
      {
        "bgpPeers": [
          {
            "name": "PEER_NAME_1",
            "interfaceName": "INTERFACE_NAME_1",
            "ipAddress": "IP_ADDRESS_1",
            "peerIpAddress": "PEER_IP_ADDRESS_1",
            "peerAsn": "PEER_ASN_1"
          },
          {
            "name": "PEER_NAME_2",
            "interfaceName": "INTERFACE_NAME_2",
            "ipAddress": "IP_ADDRESS_2",
            "peerIpAddress": "PEER_IP_ADDRESS_2",
            "peerAsn": "PEER_ASN_2"
          }
        ]
      }

Replace the placeholder values as follows.

Provide values about the Cloud Router:

  * `PROJECT_ID`: the project that contains the Cloud Router
  * `REGION`: the region where the Cloud Router is located
  * `ROUTER_NAME`: the name of the Cloud Router



Provide values about the BGP peering session that you are _not_ changing:

  * `PEER_NAME_1`: the name of the BGP session
  * `INTERFACE_NAME_1`: the name of the interface that the session uses
  * `IP_ADDRESS_1`: the Cloud Router IP address that the session uses
  * `PEER_IP_ADDRESS_1`: the IP address of the BGP peer
  * `PEER_ASN_1`: the autonomous system number (ASN) for the session



Provide values about the BGP peering session from which you want to remove custom learned routes:

  * `PEER_NAME_2`: the name of the session
  * `INTERFACE_NAME_2`: the name of the interface that the session uses
  * `IP_ADDRESS_2`: the Cloud Router IP address that the session uses
  * `PEER_IP_ADDRESS_2`: the IP address of the BGP peer
  * `PEER_ASN_2`: the autonomous system number (ASN) for the session



## Change the MED values for all custom learned routes on a BGP session

If you want to update a BGP session to use a different MED values for its custom learned routes, use the following guidance. Be aware that MED values always apply to all custom routes defined for a BGP peer; you can't apply different MED values to different IP prefixes.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. In the **Name** field, click the name of the appropriate Cloud Router.

  3. On the **Router details** page, click the name of the BGP session that you want to modify.

  4. On the **BGP session details** page, click edit**Edit**.

  5. Expand the **Advertised routes, custom learned routes, bidirectional forwarding detection (BFD)** section.

  6. In the **Priority of all custom learned routes** field, to edit the route's MED value, enter a new MED value between `0` and `65535` (inclusive) for all the custom learned routes configured for this session.

Google Cloud gives greater preference to routes that have smaller MED values. If the same IP address range is configured in multiple custom learned routes, the best path selection is based on the route's MED value.

  7. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers update-bgp-peer` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer):
    
    
      gcloud compute routers update-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME \
          --region=REGION \
          --custom-learned-route-priority=NEW_ROUTE_PRIORITY

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `PEER_NAME`: the name of the BGP peer
  * `REGION`: the region where the Cloud Router is located
  * `NEW_ROUTE_PRIORITY`: a MED value between `0` and `65535` (inclusive) for all the custom learned routes configured for this session

Google Cloud gives greater preference to routes that have smaller MED values. That is, a route with a MED value of `100` is given greater preference than one with a MED value of `200`.




###  API 

Use the [`compute.routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) and update the `bgpPeers` array.

When you patch the `bgpPeers` array, you must provide values for every field on every item, unless you want to remove some BGP peers or some values.

For example, suppose the Cloud Router has two BGP peers. To leave the first peer unchanged but update the MED value of the two custom learned routes defined for the second peer, use a request like the following:
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
      {
        "bgpPeers": [
          {
            "name": "PEER_NAME_1",
            "interfaceName": "INTERFACE_NAME_1",
            "ipAddress": "IP_ADDRESS_1",
            "peerIpAddress": "PEER_IP_ADDRESS_1",
            "peerAsn": "PEER_ASN_1"
          },
          {
            "name": "PEER_NAME_2",
            "interfaceName": "INTERFACE_NAME_2",
            "ipAddress": "IP_ADDRESS_2",
            "peerIpAddress": "PEER_IP_ADDRESS_2",
            "peerAsn": "PEER_ASN_2",
            "customLearnedRoutePriority": "NEW_ROUTE_PRIORITY",
            "customLearnedIpRanges": [
              {
               "range": "IP_PREFIX_1"
              },
              {
               "range": "IP_PREFIX_2"
              }
            ]
          }
        ]
      }

Replace the following:

  * `PROJECT_ID`: the project that contains the Cloud Router

  * `REGION`: the region where the Cloud Router is located

  * `ROUTER_NAME`: the name of the Cloud Router

  * `PEER_NAME_1`: the name of the BGP session

  * `INTERFACE_NAME_1`: the name of the interface that the session uses

  * `IP_ADDRESS_1`: the Cloud Router IP address that the session uses

  * `PEER_IP_ADDRESS_1`: the IP address of the BGP peer

  * `PEER_ASN_1`: the autonomous system number (ASN) for the session

  * `PEER_NAME_2`: the name of the BGP session

  * `INTERFACE_NAME_2`: the name of the interface that the session uses

  * `IP_ADDRESS_2`: the Cloud Router IP address that the session uses

  * `PEER_IP_ADDRESS_2`: the IP address of the BGP peer

  * `PEER_ASN_2`: the autonomous system number (ASN) for the session

  * `NEW_ROUTE_PRIORITY`: a MED value between `0` and `65535` (inclusive) for all the custom learned routes configured for this session

Google Cloud gives greater preference to routes that have smaller MED values. That is, a route with a MED value of `100` is given greater preference than one with a MED value of `200`.

  * `IP_PREFIX_1` and `IP_PREFIX_2`: the IP prefixes that are already defined for the BGP session




## Check the status of custom learned routes

To check the status of your custom learned routes, use the following guidance.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. In the **Name** field, click the name of the appropriate Cloud Router.

  3. On the **Router details** page, click the name of the BGP session that you want to modify.

  4. On the **BGP session details** page, click edit**Edit**.

  5. Expand the **Advertised routes, custom learned routes, bidirectional forwarding detection (BFD)** section.

  6. To view the route's MED value , see the **Priority of all custom learned routes** field.

Google Cloud gives greater preference to routes that have smaller MED values. That is, a route with a MED value of `100` is given greater preference than one with a MED value of `200`.

  7. To view the IP address ranges, see the **IP address range** fields.




###  gcloud 

  1. To check the configuration of your BGP sessions, use the [`gcloud compute routers describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/describe). For example:
         
         gcloud compute routers describe ROUTER_NAME \
             --region=REGION

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router
     * `REGION`: the region where the Cloud Router is located

The output of the command includes the IP prefixes and MED values that are configured for each BGP session.

  2. To see whether any of your custom learned routes are considered best routes for the router, use the [`gcloud compute routers get-status` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-status):
         
         gcloud compute routers get-status ROUTER_NAME \
             --region=REGION

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router
     * `REGION`: the Google Cloud region

The output lists the best routes for the Cloud Router and tells you the state of each BGP session.




###  API 

  1. To retrieve BGP session configuration details, use the [`routers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/get):
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         

Replace the following:

     * `PROJECT_ID`: the project that contains the Cloud Router
     * `REGION`: the region where the Cloud Router is located
     * `ROUTER_NAME`: the name of the Cloud Router

The `bgpPeers` field in the output contains the configuration for each BGP session.

  2. Use the [`routers.getRouterStatus` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/getRouterStatus):
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME/getRouterStatus
         

Replace the following:

     * `PROJECT_ID`: the project that contains the Cloud Router
     * `REGION`: the region where the Cloud Router is located
     * `ROUTER_NAME`: the name of the Cloud Router

The output lists the best routes for the Cloud Router and tells you the state of each BGP session.




## What's next

  * For help understanding the state of a BGP session, see [BGP session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states).

  * To troubleshoot issues with Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
