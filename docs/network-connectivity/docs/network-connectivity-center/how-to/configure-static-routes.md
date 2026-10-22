---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/configure-static-routes/
title: Configure static routes \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:24.176590+00:00
---

# Configure static routes  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/configure-static-routes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Configure static routes Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure static routes for Network Connectivity Center (NCC).

You can configure static routes for NCC to control traffic flow and establish advanced network topologies. For example, direct traffic through a Network Virtual Appliance (NVA) in a transit VPC to manage complex connectivity across your VPC networks. Static routes help you connect different VPC networks, integrate on-premises environments, or incorporate Router appliance VMs into your network architecture.

If you are new to static routes, see the [Static routes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/static-routes-overview).

When you select the IP address of the internal passthrough Network Load Balancer, its forwarding rule's `--load-balancing-scheme` must be INTERNAL. You can use any `--destination-range` that meets the following criteria:

  * The `--destination-range` doesn't exactly match the destination of a subnet route.
  * The `--destination-range` doesn't have a longer subnet mask than the destination of a subnet route.



For more information about destination range requirements, see [destination IP address range](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#destination_range).

## Create static routes

You can create static routes for NCC spokes by using the [`gcloud compute routes create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/create). The following example shows you how to create a static route for a NCC spoke:
    
    
      gcloud compute routes create ROUTE_NAME \
          --network=HOME_VPC \
          --destination-range=DESTINATION_RANGE \
          --priority=PRIORITY \
          --next-hop-ilb=FORWARDING_RULE
    

Replace the following:

  * `ROUTE_NAME`: the name of the route.
  * `HOME_VPC`: the name of the VPC network that contains the route.
  * `DESTINATION_RANGE`: the destination IPv4 addresses to which this route applies. The broadest possible destination is `0.0.0.0/0`.
  * `PRIORITY`: the route priority, which can be from `0` (the highest priority) to `65535` (the lowest priority). For more information about route priority, see [Routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).
  * `FORWARDING_RULE`: IP address of a forwarding rule for an internal passthrough Network Load Balancer.



The following sections demonstrate two use cases, highlighting the differences in how you create static routes for mesh and star topologies.

### Create static routes in a mesh topology

For this example, assume that you have two spoke VPCs, `vpc-1` and `vpc-2`, which are connected to the same NCC hub. Suppose that you also have a transit VPC `transit` that is connected to `vpc-2` through a network virtual appliance (NVA). You want to reach the `transit` VPC from the `vpc-1` and `vpc-2` spokes, so you configure static routes using the following steps:

  1. First, create a static route in spoke `vpc-1` with the `transit` VPC's IP address as the destination, and `vpc-2`'s internal passthrough Network Load Balancer IP address as the next hop:
         
         gcloud compute routes create ROUTE_NAME \
             --network=vpc-1 \
             --destination-range=DESTINATION_RANGE \
             --priority=PRIORITY \
             --next-hop-ilb=FORWARDING_RULE
         

Replace the following:

     * `ROUTE_NAME`: the name of the route
     * `DESTINATION_RANGE`: the destination IPv4 addresses for the `transit` VPC.
     * `PRIORITY`: the route priority, which can be from `0` (the highest priority) to `65535` (the lowest priority). For more information about route priority, see [Routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).
     * `FORWARDING_RULE`: IP address of a forwarding rule for a internal passthrough Network Load Balancer in `vpc-2`.
  2. Create a static route in spoke `vpc-2` with the `transit` VPC's IP address as the destination, and the `transit` VPC's internal passthrough Network Load Balancer IP address as the next hop:
         
         gcloud compute routes create ROUTE_NAME \
             --network=vpc-2 \
             --destination-range=DESTINATION_RANGE \
             --priority=PRIORITY \
             --next-hop-ilb=FORWARDING_RULE
         

Replace the following:

     * `ROUTE_NAME`: the name of the route
     * `DESTINATION_RANGE`: the destination IPv4 addresses for the `transit` VPC
     * `PRIORITY`: the route priority, which can be from `0` (the highest priority) to `65535` (the lowest priority); for more information about route priority, see [Routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).
     * `FORWARDING_RULE`: IP address of a forwarding rule for an internal passthrough Network Load Balancer in the `transit` VPC
  3. Create a return route in the `transit` VPC to `vpc-2`, with `vpc-2`'s IP address as the destination, and `vpc-2`'s internal passthrough Network Load Balancer IP address as the next hop:
         
         gcloud compute routes create ROUTE_NAME \
             --network=transit \
             --destination-range=DESTINATION_RANGE \
             --priority=PRIORITY \
             --next-hop-ilb=FORWARDING_RULE
         

Replace the following:

     * `ROUTE_NAME`: the name of the route
     * `DESTINATION_RANGE`: the destination IPv4 address for `vpc-2`
     * `PRIORITY`: the route priority, which can be from `0` (the highest priority) to `65535` (the lowest priority); for more information about route priority, see [Routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).
     * `FORWARDING_RULE`: IP address of a forwarding rule for an internal passthrough Network Load Balancer in `vpc-2`
  4. Next, create a return route in the `transit` VPC to `vpc-1`, with `vpc-1`'s IP address as the destination, and `vpc-2`'s internal passthrough Network Load Balancer IP address as the next hop:
         
         gcloud compute routes create ROUTE_NAME \
             --network=transit \
             --destination-range=DESTINATION_RANGE \
             --priority=PRIORITY \
             --next-hop-ilb=FORWARDING_RULE
         

Replace the following:

     * `ROUTE_NAME`: the name of the route
     * `DESTINATION_RANGE`: the destination IPv4 addresses for `vpc-2`
     * `PRIORITY`: the route priority, which can be from `0` (the highest priority) to `65535` (the lowest priority); for more information about route priority, see [Routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).
     * `FORWARDING_RULE`: IP address of a forwarding rule for an internal passthrough Network Load Balancer in `vpc-2`
  5. Finally, create a return route in `vpc-2` to `vpc-1`, with `vpc-1`'s IP address as the destination, and `vpc-1`'s internal passthrough Network Load Balancer IP address as the next hop:
         
         gcloud compute routes create ROUTE_NAME \
             --network=vpc-2 \
             --destination-range=DESTINATION_RANGE \
             --priority=PRIORITY \
             --next-hop-ilb=FORWARDING_RULE
         

Replace the following:

     * `ROUTE_NAME`: the name of the route
     * `DESTINATION_RANGE`: the destination IPv4 addresses for `vpc-1`
     * `PRIORITY`: the route priority, which can be from `0` (the highest priority) to `65535` (the lowest priority); for more information about route priority, see [Routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).
     * `FORWARDING_RULE`: IP address of a forwarding rule for a internal passthrough Network Load Balancer in `vpc-1`



For more information about NVAs, see [Network virtual appliances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connect-vpc-networks).

### Create static routes in a star topology

For this example, assume that you have two edge VPCs, `edge-1` and `edge-2` that are connected to center VPC `center`. Suppose that you also have a transit VPC `transit` that is connected to `center` through a network virtual appliance (NVA). You want to reach the `transit` VPC from `edge-1`, so you configure static routes using the following steps:

  1. First, create a static route in `edge-1` with the `transit` VPC's IP address as the destination, and `center`'s internal passthrough Network Load Balancer IP address as the next hop:
         
         gcloud compute routes create ROUTE_NAME \
             --network=edge-1 \
             --destination-range=DESTINATION_RANGE \
             --priority=PRIORITY \
             --next-hop-ilb=FORWARDING_RULE
         

Replace the following:

     * `ROUTE_NAME`: the name of the route
     * `DESTINATION_RANGE`: the destination IPv4 addresses for the `transit` VPC
     * `PRIORITY`: the route priority, which can be from `0` (the highest priority) to `65535` (the lowest priority); for more information about route priority, see [Routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).
     * `FORWARDING_RULE`: IP address of a forwarding rule for an internal passthrough Network Load Balancer in `center`
  2. Create a static route in `center` with the `transit` VPC's IP address as the destination, and the `transit` VPC's internal passthrough Network Load Balancer IP address as the next hop:
         
         gcloud compute routes create ROUTE_NAME \
             --network=vpc-1 \
             --destination-range=DESTINATION_RANGE \
             --priority=PRIORITY \
             --next-hop-ilb=FORWARDING_RULE
         

Replace the following:

     * `ROUTE_NAME`: the name of the route
     * `DESTINATION_RANGE`: the destination IPv4 addresses for the `transit` VPC
     * `PRIORITY`: the route priority, which can be from `0` (the highest priority) to `65535` (the lowest priority); for more information about route priority, see [Routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).
     * `FORWARDING_RULE`: IP address of a forwarding rule for an internal passthrough Network Load Balancer in the `transit` VPC
  3. Create a return route in the `transit` VPC to `center`, with `center`'s IP address as the destination, and `center`'s internal passthrough Network Load Balancer IP address as the next hop:
         
         gcloud compute routes create ROUTE_NAME \
             --network=transit \
             --destination-range=DESTINATION_RANGE \
             --priority=PRIORITY \
             --next-hop-ilb=FORWARDING_RULE
         

Replace the following:

     * `ROUTE_NAME`: the name of the route
     * `DESTINATION_RANGE`: the destination IPv4 addresses for `center`
     * `PRIORITY`: the route priority, which can be from `0` (the highest priority) to `65535` (the lowest priority); for more information about route priority, see [Routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).
     * `FORWARDING_RULE`: IP address of a forwarding rule for an internal passthrough Network Load Balancer in `center`
  4. Next, create a return route in the `transit` VPC to `edge-1`, with `edge-1`'s IP address as the destination, and `center`'s internal passthrough Network Load Balancer IP address as the next hop:
         
         gcloud compute routes create ROUTE_NAME \
             --network=transit \
             --destination-range=DESTINATION_RANGE \
             --priority=PRIORITY \
             --next-hop-ilb=FORWARDING_RULE
         

Replace the following:

     * `ROUTE_NAME`: the name of the route
     * `DESTINATION_RANGE`: the destination IPv4 addresses for `edge-1`
     * `PRIORITY`: the route priority, which can be from `0` (the highest priority) to `65535` (the lowest priority); for more information about route priority, see [Routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).
     * `FORWARDING_RULE`: IP address of a forwarding rule for an internal passthrough Network Load Balancer in `center`
  5. Next, create a return route in `center` to `edge-1`, with `edge-1`'s IP address as the destination, and `edge-1`'s internal passthrough Network Load Balancer IP address as the next hop:
         
         gcloud compute routes create ROUTE_NAME \
             --network=center \
             --destination-range=DESTINATION_RANGE \
             --priority=PRIORITY \
             --next-hop-ilb=FORWARDING_RULE
         

Replace the following:

     * `ROUTE_NAME`: the name of the route
     * `DESTINATION_RANGE`: the destination IPv4 addresses for `edge-1`
     * `PRIORITY`: the route priority, which can be from `0` (the highest priority) to `65535` (the lowest priority); for more information about route priority, see [Routing order](https://docs.cloud.google.com/vpc/docs/routes#routeselection).
     * `FORWARDING_RULE`: IP address of a forwarding rule for an internal passthrough Network Load Balancer in `edge-1`



## Delete static routes

Use the following [`gcloud compute routes delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/delete) to delete a static route, replacing`ROUTE_NAME` with the name of the route:
    
    
      gcloud compute routes delete ROUTE_NAME
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
