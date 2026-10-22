---
url: https://docs.cloud.google.com/nat/docs/nat-product-interactions/
title: Cloud NAT product interactions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:43.223140+00:00
---

# Cloud NAT product interactions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/nat-product-interactions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud NAT product interactions

This page describes the important interactions between Cloud NAT and other Google Cloud products.

## Routes interactions

A Public NAT gateway can only use routes whose next hops are the default internet gateway. Each Virtual Private Cloud (VPC) network starts with a default route whose destination is `0.0.0.0/0` and whose next hop is the default internet gateway. For more information, see the [routes overview](https://docs.cloud.google.com/vpc/docs/routes).

The following examples illustrate situations that could cause Public NAT gateways to become inoperable:

  * If you create a static route with next hops set to [any other type of static route next hop](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops), then packets with destination IP addresses matching the destination of the route are sent to that next hop instead of to the default internet gateway. For example, if you use virtual machine (VM) instances running a NAT gateway, firewall, or proxy software, you create static routes to direct traffic to those VMs as the next hop. The next-hop VMs require external IP addresses. Thus, traffic from the VMs that rely upon the next-hop VMs or the next-hop VMs themselves cannot use Public NAT gateways.

  * If you create a custom static route whose next hop is a Cloud VPN tunnel, Public NAT does not use that route. For example, a static route with destination `0.0.0.0/0` and a next hop Cloud VPN tunnel directs traffic to that tunnel, not to the default internet gateway. Therefore, Public NAT gateways cannot use that route. Similarly, Public NAT gateways cannot use static routes with more specific destinations, including `0.0.0.0/1` and `128.0.0.0/1`.

  * If an on-premises router advertises a dynamic route to a Cloud Router managing a Cloud VPN tunnel or VLAN attachment, Public NAT gateways cannot use that route. For example, if your on-premises router advertises a dynamic route with destination `0.0.0.0/0`, `0.0.0.0/0` would be directed to the Cloud VPN tunnel or VLAN attachment. This behavior holds true even for more specific destinations, including `0.0.0.0/1` and `128.0.0.0/1`.




Private NAT uses the following routes:

  * NCC subnet routes and NCC dynamic routes: 
    * For traffic between [VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview), the NAT gateway uses subnet routes.
    * For NCC hubs that have both VPC spokes and [hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#hybrid_spokes), the NAT gateway uses subnet routes and dynamic routes.
  * Local dynamic routes: for Hybrid NAT, the NAT gateway uses dynamic routes that Cloud Router learns through Cloud Interconnect or Cloud VPN.
  * Local subnet routes and local static routes (NAT64 only): the NAT gateway uses these routes for traffic within the same VPC network.



For more information about routing in Private NAT, see [Routes and firewall rules](https://docs.cloud.google.com/nat/docs/private-nat#specs-pvt-nat-routes-firewalls).

## Private Google Access interactions

A Public NAT gateway never performs NAT for traffic sent to the select [external IP addresses for Google APIs and services](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-domain). Instead, Google Cloud automatically enables Private Google Access for a subnet IP address range when you configure a Public NAT gateway to [apply to that subnet range](https://docs.cloud.google.com/nat/docs/public-nat#specs-subnet-ranges), either primary or secondary. As long as the gateway provides NAT for a subnet's range, Private Google Access is in effect for that range and cannot be disabled manually.

A Public NAT gateway does _not_ change the way that Private Google Access works. For more information, see [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).

Private NAT gateways don't apply to Private Google Access.

## Shared VPC interactions

[Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) enables multiple service projects in a single organization to use a common, Shared VPC network in a host project. To provide NAT for VMs in service projects that use a Shared VPC network, you must create Cloud NAT gateways in the host project.

## VPC Network Peering interactions

A Cloud NAT gateway is configured for subnet IP address ranges in a single region and a single VPC network.

Consequently, a Cloud NAT gateway that is created in one VPC network can't provide NAT44 or NAT64 for VMs in other VPC networks, even if those networks are connected through [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) and the VMs are in the same region as the gateway.

Additionally, for [Private NAT](https://docs.cloud.google.com/nat/docs/private-nat), Cloud NAT doesn't support destinations in VPC networks that are connected through VPC Network Peering.

## GKE interactions

A Public NAT gateway can perform NAT for nodes and Pods in a [private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept), which is a type of VPC-native cluster. The Public NAT gateway must be configured to apply to at least the following subnet IP address ranges for the subnet that your cluster uses:

  * Subnet primary IP address range (used by nodes)
  * Subnet secondary IP address range used for Pods in the cluster
  * Subnet secondary IP address range used for Services in the cluster



The simplest way to provide NAT for an entire private cluster is to configure a Public NAT gateway to apply to all the subnet IP address ranges of the cluster's subnet.

For background information about how VPC-native clusters utilize subnet IP address ranges, see [IP ranges for VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing).

When a Public NAT gateway is configured to provide NAT for a private cluster, it reserves NAT source IP addresses and source ports for each node VM. Those NAT source IP addresses and source ports are usable by Pods because Pod IP addresses are implemented as alias IP ranges assigned to each node VM.

Google Kubernetes Engine (GKE) VPC-native clusters always assign each node an alias IP range that contains more than one IP address (netmask smaller than `/32`).

  * If [static port allocation](https://docs.cloud.google.com/nat/docs/ports-and-addresses#static-port) is configured, the Public NAT [port reservation procedure](https://docs.cloud.google.com/nat/docs/ports-and-addresses#port-reservation-procedure) reserves at least 1,024 source ports per node. If the specified value for minimum ports per VM is greater than 1,024, that value is used.

  * If [dynamic port allocation](https://docs.cloud.google.com/nat/docs/ports-and-addresses#dynamic-port) is configured, the specified value for minimum ports per VM is initially allocated per node. The number of allocated ports subsequently varies between the specified values for minimum and maximum ports per VM, based on demand.




For information about Pod IP address ranges and VPC-native clusters, see [Subnet secondary IP address range for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing_secondary_range_pods).

Independent of Public NAT , Google Kubernetes Engine performs source network address translation (source NAT or SNAT) by using software running on each node when Pods send packets to the internet, unless you've changed the cluster's [IP masquerade configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent). If you need granular control over egress traffic from Pods, you can use a [network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).

Under certain circumstances, Public NAT can be useful to non-private VPC-native clusters as well. Because the nodes in a non-private cluster have external IP addresses, packets sent from the node's primary internal IP address are never processed by Cloud NAT. However, if both of the following are true, packets sent from Pods in a non-private cluster can be processed by a Public NAT gateway:

  * For VPC-native clusters, the Public NAT gateway is configured to apply to the secondary IP address range for the cluster's Pods.

  * The cluster's IP masquerade configuration is not configured to perform SNAT within the cluster for packets sent from Pods to the internet.




The following example shows the interaction of Public NAT with GKE:

[ ![Public NAT with GKE.](https://docs.cloud.google.com/static/nat/images/03.svg)](https://docs.cloud.google.com/static/nat/images/03.svg) Public NAT with GKE (click to enlarge).

In this example, you want your containers to be NAT translated. To enable NAT for all the containers and the GKE node, you must choose all the IP address ranges of `Subnet 1` as the NAT candidate:

  * Subnet primary IP address range: `10.240.0.0/24`
  * Subnet secondary IP address range used for Pods: `10.0.0.0/16`



It is not possible to enable NAT for only `Pod1` or `Pod2`.

A Private NAT gateway can perform NAT for nodes and Pods in a private cluster and in a non-private cluster. The Private NAT gateway automatically applies to all the subnet IP address ranges for the private subnet that your cluster uses.

## Direct VPC egress interactions

Cloud NAT gateways can provide NAT for Cloud Run resources that are configured with [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc). To enable Cloud Run to use a Cloud NAT gateway for Public NAT or Private NAT, configure the following:

  * When you [deploy your Cloud Run resources](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-service), set the `--vpc-egress` flag. If you want to use Public NAT, the value must be set to `all-traffic`.

  * Configure the Cloud NAT gateway with the following settings:

    * Specify which source subnet ranges can use the gateway by setting the `--nat-custom-subnet-ip-ranges` flag. Set the value to the subnet names where you deploy your Cloud Run resources.
    * Set the value of the `--endpoint-types` flag to `ENDPOINT_TYPE_VM`.
    * For Public NAT, ensure that the value of the `--min-ports-per-vm` flag is set to two times the number of ports needed by a single Cloud Run instance. For Private NAT, this flag must be set to four times the number of ports needed per Cloud Run instance.

    * If you want to configure manual NAT IP address allocation (Public NAT only), assign a number of IP addresses to your gateway that is sufficient to cover the sum of VM instances and Cloud Run instances that are served by the gateway.




Cloud NAT logs for Direct VPC egress don't display the names of Cloud Run resources.

## Connectivity Tests interactions

You can use Connectivity Tests to check connectivity between network endpoints that use Cloud NAT configurations. You can run Connectivity Tests on networks that use either [Public NAT gateways](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests#vpc-to-non-cloud) or [Private NAT gateways](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests#test-from-vpc-spoke-to-vpc-spoke), or both.

View the NAT configuration details in the **Configuration analysis trace** pane on the **Connectivity test details** page.

## Cloud Load Balancing interactions

Google Cloud [regional internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-int-https-external-backend) and [regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setup-regional-ext-https-external-backend) communicate with multiple [regional internet network endpoint group (NEG) backends](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#nat-support). By configuring Cloud NAT gateways for the regional internet NEGs, you can allocate your own set of external IP address ranges from where the Google Cloud traffic should originate. The health checks and data plane traffic are sourced from the NAT IP addresses that you allocate.

Other Google Cloud external load balancers and health check systems communicate with VMs by using [special routing paths](https://docs.cloud.google.com/vpc/docs/routes#special_return_paths). Backend VMs don't require external IP addresses nor does a Cloud NAT gateway manage communication for load balancers and health checks. For more information, see [Cloud Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) and [Health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

## Private Service Connect propagated connections interactions

When using both [Private NAT for NCC](https://docs.cloud.google.com/nat/docs/about-private-nat-for-ncc) and [Private Service Connect propagated connections](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview) in the same VPC spoke, the following applies:

  * If a subnet is configured with Private NAT, traffic from the subnet to Private Service Connect propagated connections is dropped.

  * To avoid dropping traffic from non-overlapping subnets, consider the following when you configure Private NAT:

    * Specify overlapping subnets by using the `--nat-custom-subnet-ip-ranges` flag.
    * Don't specify non-overlapping subnets that need to access propagated connections.
    * Don't use the `--nat-all-subnet-ip-ranges` flag.



## Hybrid Subnets interactions

[Hybrid NAT](https://docs.cloud.google.com/nat/docs/about-hybrid-nat) isn't supported with [Hybrid Subnets](https://docs.cloud.google.com/vpc/docs/hybrid-subnets).

If traffic originates from a subnet where Hybrid NAT is configured and the destination IP address matches a hybrid subnet route, SNAT isn't performed. This configuration results in unpredictable routing behavior because traffic can reach a non-VPC network by using the original, untranslated source IP address.

Don't use Hybrid Subnets in networks where Hybrid NAT is configured.

## What's next

  * Learn about [IP addresses and ports](https://docs.cloud.google.com/nat/docs/ports-and-addresses)
  * [Set up and manage network address translation with Public NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation)
  * [Set up and manage Cloud NAT rules](https://docs.cloud.google.com/nat/docs/using-nat-rules)
  * [Set up and manage network address translation with Private NAT](https://docs.cloud.google.com/nat/docs/set-up-private-nat)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
