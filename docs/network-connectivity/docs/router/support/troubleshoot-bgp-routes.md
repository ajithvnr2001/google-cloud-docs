---
url: https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes/
title: Troubleshoot BGP routes and route selection \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:21.762167+00:00
---

# Troubleshoot BGP routes and route selection  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot BGP routes and route selection

This guide is for troubleshooting Cloud Router issues related to BGP routes, including route selection, route propagation, and route metrics.

For additional troubleshooting information, see the following:

  * [Troubleshoot BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-sessions)
  * [Troubleshoot BGP peering](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-peering)
  * [Troubleshoot Cloud Router log messages](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-log-messages)



## IPv6 BGP session is established but does not exchange IPv4 routes

  1. Verify that the VLAN attachment or HA VPN gateway has the required stack type of `IPV4_IPV6`. If the stack type is incorrect for the VLAN attachment, modify the VLAN attachment. For an HA VPN gateway, recreate the HA VPN gateway and its tunnels.

  2. Ensure that your Cloud Router is configured properly. Run the following command:
         
         gcloud compute routers describe ROUTER-NAME
         

In the output, check the following values:

     * `bgpPeers.enableIpv4` is `true`
     * `bgpPeers.ipv4NexthopAddress` and `bgpPeers.peerIpv4NexthopAddress` are present



## Some on-premises IPv4 or IPv6 prefixes aren't reachable

If you are experiencing traffic loss, ping errors, or other problems when attempting to reach on-premises IPv4 or IPv6 destinations that are within prefixes learned by Cloud Router, there are a variety of possible causes.

### Check for inactive custom learned routes

If you are unable to reach an on-premises destination using a configured custom learned route, do the following:

  * Check that the route is configured properly on the BGP session.
  * Check that the BGP session is up.
  * Check that the on-premises router is filtering some learned routes.



For more information, see [Check the status of custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes#check-status).

### Check for filtered learned routes

To see if a route is filtered, run the following command:
    
    
    gcloud compute routers get-status ROUTER_NAME \
        --region=REGION
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router.
  * `REGION`: the region that your Cloud Router is located in.



The output is similar to the following; look for the `routeStatus` set to `active`:
    
    
    kind: compute#routerStatusResponse
    result:
      bestRoutesForRouter:
      - asPaths:
        - asLists:
          - 65200
          pathSegmentType: AS_SEQUENCE
        creationTimestamp: '2024-03-22T13:57:15.533-07:00'
        destRange: 10.128.0.0/20
        kind: compute#route
        network: https://www.googleapis.com/compute/v1/projects/PROJECT/global/networks/VPC_NAME
        nextHopIp: 169.254.73.246
        nextHopVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/vpnTunnels/VPN_NAME
        priority: 100
        routeStatus: ACTIVE
        routeType: BGP
      bgpPeerStatus:
      - advertisedRoutes:
        - destRange: 10.128.0.0/20
          kind: compute#route
          network: https://www.googleapis.com/compute/v1/projects/PROJECT/global/networks/aneta-vpc
          nextHopIp: 169.254.73.245
          nextHopVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/vpnTunnels/VPN_NAME
          priority: 100
          routeType: BGP
        enableIpv6: false
        ipAddress: 169.254.73.245
        linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/vpnTunnels/VPN_NAME
        md5AuthEnabled: false
        name: aneta-bgp
        numLearnedRoutes: 1
        peerIpAddress: 169.254.73.246
        state: Established
        status: UP
        uptime: 10 hours, 11 minutes, 0 seconds
        uptimeSeconds: '36660'
      network: https://www.googleapis.com/compute/v1/projects/PROJECT/global/networks/VPC_NAME
    
    

The `bestRoutesForRouter.routeStatus` value displays `ACTIVE` for an active route, and `DROPPED` for a filtered route.

### Check quotas and limits

Check that your Cloud Routers haven't exceeded the [quotas](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#quotas) for learned routes. To view the number of learned routes for a Cloud Router, view its [status](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#viewing-router-status).

For information about the quotas, related log messages, and metrics, and how to resolve issues, see the following table.

Topic | Guidance  
---|---  
About the quotas | See [Cloud Router quotas](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#quotas) and [Learned route example](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#learned-route-example).   
Logs | When route usage reaches 75% of either quota, Cloud Router logs a warning. When either quota is exceeded, an error is logged and any dropped routes are listed. These events appear in Cloud Logging in `[router.googleapis.com/route_quota_events](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics#route-quota-events-log)`. For information about the logs, see [Route quota events log](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics#route-quota-events-log) in the Cloud Router documentation.  
Metrics | You can also use the following metrics to understand your current quota availability and usage. These metrics are prepended with `router.googleapis.com/dynamic_routes/learned_routes/`:

  * `used_unique_destinations` Number of unique destinations that are in use in this VPC network. If global dynamic routing is enabled, this metric shows both global and regional usage.
  * `unique_destinations_limit` Number of unique destinations that are allowed to advertise in this VPC network. If global dynamic routing is enabled, this metric shows both global and regional quotas.
  * `any_dropped_unique_destinations` Indicates whether this VPC network has any destinations dropped due to exceeding one or both of the route quotas.

These metrics are available through the `gce_network_region` monitored resource. For more information about Cloud Router metrics and how to view them, see the [Metrics](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics#metrics) section in Viewing logs and metrics.  
Resolving issues | You can do the following to resolve route quota issues. In situations where the number of routes exceeds the available quota by a large amount, it makes sense to do both:

  * Configure your on-premises routers to summarize the routes that you export so that those routes advertise fewer destinations (CIDRs).
  * [Contact Support](https://docs.cloud.google.com/network-connectivity/docs/router/support/getting-support). Support can work with you to increase quotas.

  
  
## Learned routes (routes from an on-premises network) aren't propagated to other VPC networks

A single Cloud Router can't re-advertise routes learned from one BGP peer to other BGP peers, including to Cloud Routers in other VPC networks.

For example, in the following hub and spoke topology, Cloud Router cannot support route advertisement between multiple VPC networks.

[ ![Cloud Router hub and spoke.](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/hub-spoke.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/router/images/hub-spoke.svg) Cloud Router hub and spoke (click to enlarge).

In this case, there isn't an iBGP session between Cloud Routers that share the same VPC network, and Cloud Router only advertises VPC subnets and custom configured routes. Cloud Router doesn't advertise dynamic routes from the VPC network.

To review recommendations for network topologies in Google Cloud, see [Best practices and reference architectures for VPC design](https://docs.cloud.google.com/architecture/best-practices-vpc-design).

In addition, to build and manage hub and spoke topologies in Google Cloud, you can use [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

## IPv6 traffic isn't being routed

If you are experiencing difficulty connecting to IPv6 hosts, do the following:

  1. Verify that IPv4 routes are being correctly advertised. By checking IPv4 traffic first, you can rule out general network issues. If IPv4 routes are not being advertised, perform the general troubleshooting procedures listed in this document.

  2. Inspect [firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) to ensure that you are allowing IPv6 traffic between your VPC network and your on-premises network.

  3. Determine whether you have exceeded your available quota for learned routes. If you have exceeded your quota for learned routes, IPv6 prefixes are dropped before IPv4 prefixes. See Check quotas and limits.

  4. Verify that all components that require IPv6 configuration have been configured correctly.

     * The VPC subnet is configured to use the `IPV4_IPV6` stack type.

     * The VPC subnet has`--ipv6-access-type` set to `INTERNAL`.

     * The Compute Engine VMs on the subnet are configured with IPv6 addresses.

     * The HA VPN gateway or the VLAN attachment for Dedicated Interconnect is configured to use the `IPV4_IPV6` stack type.

     * The BGP session is enabled to advertise IPv6 routes and the next-hop is an IPv6 address.

       * To view Cloud Router status and routes, see [View Cloud Router status and routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#viewing-router-status).

       * To view BGP session configuration, see [View BGP session configuration](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#viewing-router-status).




## Cloud Router doesn't return ICMPv6 ping responses

ICMPv6 `ping` isn't supported for Cloud Router BGP addresses. To test layer 3 connectivity for Cloud Router BGP addresses, use ICMPv4 `ping`.

## What's next

  * For more information about how to use Cloud Logging to monitor Cloud Router, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics).

  * For additional support, see [Getting support](https://docs.cloud.google.com/network-connectivity/docs/router/support/getting-support).

  * For information about BGP session states, see [BGP session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states).

  * For information about diagnostic messages and session states related to Bidirectional Forwarding Detection (BFD), see [BFD diagnostic messages and session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd-states).

  * For issues related to using Cloud Router with Router appliance, see [Troubleshooting Router appliance](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra) in the Network Connectivity Center documentation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
