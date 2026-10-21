---
url: https://docs.cloud.google.com/vpc/docs/release-notes/
title: VPC release notes \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:10:15.636435+00:00
---

# VPC release notes  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Resources ](https://docs.cloud.google.com/vpc/docs/resources)



Send feedback 

#  VPC release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Virtual Private Cloud (VPC) networking in Google Cloud. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/vpc-release-notes.xml) directly. 

## October 19, 2026

Feature

**General Availability** : VPC Flow Logs adds the following metadata annotations and packet drop reasons for Cloud NAT:

  * Metadata annotations: `connection.nat_ip`, `connection.nat_port`, and `nat_gateway_details`
  * Drop reasons: `NAT_ENDPOINT_INDEPENDENT_CONFLICT`, `NAT_OUT_OF_CONNECTIONS`, and `NAT_OUT_OF_PORTS`



For more information, see [Record format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#record_format) and [Packet drop reasons](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#drop-reason).

## October 07, 2026

Feature

**General Availability** : VPC Flow Logs supports [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging) for VM instances and serverless endpoints. Connection logging captures outbound TCP connection attempts and acknowledged inbound TCP connections.

You can enable this feature in a VPC Flow Logs configuration for a [subnet](https://docs.cloud.google.com/vpc/docs/using-flow-logs#network-management) (through the Network Management API), a [VPC network](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-network), or an [organization](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-organization).

Feature

Service producers can let service consumers establish more connections to a Private Service Connect endpoint or backend by [configuring the target published service (service attachment) to use an additional NAT IP address](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#update-nat-ips-per-endpoint). For more information, see [Maximum connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections).

## October 05, 2026

Feature

**Preview** : External IPv6 addresses are now supported for [Standard Tier](https://docs.cloud.google.com/network-tiers/docs/overview#standard_tier). For more information, see [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

## September 16, 2026

Feature

**General Availability** : You can add Dynamic NICs to the same VPC network used by other network interfaces of a Compute Engine instance. For more information, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#specifications).

Feature

**General Availability** : VPC Flow Logs supports logging for App Engine resources that are configured with [Direct VPC egress](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc). For more information, see [Serverless flows](https://docs.cloud.google.com/vpc/docs/about-traffic-flows#serverless-flows) and [ServerlessDetails field format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#serverless-details).

Feature

**General Availability** : VPC Flow Logs adds the following metadata annotations for Private Service Connect:

  * `src_psc_interface` and `dest_psc_interface`
  * `psc.consumer_connection`
  * `psc.psc_endpoint.name`
  * `psc.psc_attachment.name`



For more information, see [Record format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#record_format).

## September 10, 2026

Feature

**Preview** : [Propagated connections](https://docs.cloud.google.com/vpc/docs/about-propagated-connections) support Private Service Connect [endpoints that access global Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints). With propagated connections, endpoints that access global Google APIs in one consumer VPC spoke can be privately accessed by other consumer VPC spokes that are connected to the same Network Connectivity Center hub.

## August 31, 2026

Feature

**General Availability** : You can create Compute Engine instances that have multiple virtual network interfaces (vNICs) in the same VPC network. For more information, see [Multiple network interfaces in the same VPC network](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#same-vpc).

## August 27, 2026

Feature

**General Availability** : VPC Flow Logs generates log records for dropped traffic. For more information, see [Records for dropped traffic](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#packet-drops).

Feature

**General Availability** : You can reserve static external IPv6 addresses from bring your own IP addresses (BYOIP) sub-prefixes that are in `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode.

You can assign these addresses to forwarding rules for external passthrough Network Load Balancers and external protocol forwarding. You can also promote ephemeral IPv6 BYOIP addresses that are used by external forwarding rules to reserved static IP addresses.

For more information, see [Create external forwarding rules](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#create-subprefix-use).

## August 19, 2026

Feature

**General Availability** : You can use Private Service Connect [endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints) and [backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#multiregional-google-apis) to access multi-regional service endpoints such as `storage.us.rep.googleapis.com`.

## August 03, 2026

Feature

**Preview** : You can create v2 IPv4 public advertised prefixes for bring your own IP addresses (BYOIP) that use [Standard Tier](https://docs.cloud.google.com/network-tiers/docs/overview#standard_tier) IP addresses. For more information, see [Network Service Tiers](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#service-tiers).

## July 30, 2026

Feature

**General Availability** : You can use the **Resolve subnet mask** setting on a subnet to configure all attached Compute Engine instances with the same netmask as the subnet (instead of `/32`). Configuring larger instance netmasks lets compute instances discover the MAC addresses of other machines within the same subnet and directly communicate with them by using destination MAC addresses.

For more information, see [Compute instance netmasks](https://docs.cloud.google.com/vpc/docs/compute-instance-netmasks).

## July 21, 2026

Feature

For Google Cloud resources that are registered as [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) workloads or services, VPC Flow Logs records contain application-specific labels. For more information, see [App Hub labels](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#app-hub).

## July 20, 2026

Feature

**Preview** : You can reserve static external IPv6 addresses from bring your own IP addresses (BYOIP) sub-prefixes that are in `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode.

You can assign these addresses to forwarding rules for external passthrough Network Load Balancers and external protocol forwarding. You can also promote ephemeral IPv6 BYOIP addresses that are used by external forwarding rules to reserved static IP addresses.

For more information, see [Create external forwarding rules](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#create-subprefix-use).

## June 30, 2026

Feature

**General Availability** : If a consumer VPC network uses an [RDMA network profile for Falcon VPC networks](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles#falcon-supported-features), a single Compute Engine instance can connect to it by using multiple virtual Private Service Connect interfaces.

For more information, see [Create VMs with Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/create-manage-private-service-connect-interfaces#create).

## June 24, 2026

Feature

**General Availability** : You can cancel pending deletion requests for VPC Network Peering connections that are in consensus mode. For more information, see [Cancel a deletion request](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#cancel-delete).

## June 23, 2026

Feature

**General Availability** : Service consumers can authorize Private Service Connect interfaces to connect to network attachments by adding service class IDs to a network attachment's accept list.

For more information, see [Authorization policies](https://docs.cloud.google.com/vpc/docs/about-network-attachments#connection-policies).

## June 22, 2026

Feature

**Preview** : RoCE VPC networks for VM instances support assigning alias IP ranges to `MRDMA` vNICs. For more information about these features, see the following:

  * [RDMA network profiles](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles)
  * [Alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip)



## June 01, 2026

Feature

**General Availability** : [Composite Health for Private Service Connect](https://docs.cloud.google.com/vpc/docs/about-composite-health), formerly known as Private Service Connect health, lets service producers define health criteria for published services, enabling automatic cross-region failover for consumers that access the service by using Private Service Connect backends.

## May 19, 2026

Feature

You can cancel pending deletion requests for VPC Network Peering connections that are in consensus mode. This feature is available in **Preview**. For more information, see [Cancel a deletion request](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#cancel-delete).

## May 06, 2026

Feature

Organization Policy Service custom constraints are available in **General Availability** for private services access connections. For more information, see [Restrict private connections with organization policies](https://docs.cloud.google.com/vpc/docs/private-services-access#org-policies).

## April 10, 2026

Feature

Private Service Connect consumers can configure supported load balancers or regional Cloud Service Mesh to access published services through Private Service Connect endpoints. This feature is available in **Preview**.

For more information, see [Published service backends](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#published-service-backends).

## April 03, 2026

Feature

[Hybrid Subnets](https://docs.cloud.google.com/vpc/docs/hybrid-subnets) is available in **General Availability**. Hybrid subnet routing lets a VPC network share a CIDR block with a connected on-premises network. This configuration helps you migrate workloads to Google Cloud without needing to change any IP addresses. During migration, workloads that have migrated to your VPC network can communicate with those remaining in the on-premises network by using internal IP addresses. After all workloads have migrated, you can disable hybrid subnet routing to restore normal routing behavior.

For information about pricing for Hybrid Subnets, see [Virtual Private Cloud pricing](https://docs.cloud.google.com/vpc/pricing?e=0#hybrid-subnets).

## March 30, 2026

Feature

Service producers can [accept or reject connections from individual Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#accept-endpoint). This feature is available in **General Availability**.

## March 18, 2026

Feature

You can [update a service attachment's target service without recreating the service attachment](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#change-service). Consumer connections are preserved during the update, but traffic is briefly disrupted. This feature is available in **General Availability**.

For more information, including a list of supported configurations, see [Service mutability](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-mutability).

## February 26, 2026

Feature

You can create Compute Engine instances that have multiple network interfaces in the same VPC network. This feature is available in **Preview**. For more information, see [Multiple network interfaces in the same VPC network](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#same-vpc).

## February 23, 2026

Feature

You can create a VPC network that supports RDMA over [Falcon transport](https://cloud.google.com/blog/topics/systems/introducing-falcon-a-reliable-low-latency-hardware-transport), which lets you run AI and high performance computing (HPC) workloads on Compute Engine instances that have the `IRDMA` network interface type in Google Cloud, such as H4D instances. This feature is available in **General Availability**.

For more information, see [RDMA network profiles](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).

## February 10, 2026

Feature

You can use constraints in custom organization policies to provide more granular and customizable control over specific fields for internal ranges. For more information, see [Manage VPC resources by using custom organization policies](https://docs.cloud.google.com/vpc/docs/custom-constraints).

## February 09, 2026

Feature

You can bring your own IPv6 global unicast addresses (GUAs) to assign to a [subnet's internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes). Although GUAs are typically public addresses, in this configuration they are used privately and function in the same way as Google Cloud-provisioned ULAs.

For more information, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

## February 04, 2026

Feature

You can create individual static external IPv4 addresses from bring your own IP addresses (BYOIP) prefixes. This feature is available in **General Availability** and only applies to IPv4 regional v2 prefixes that are created after December 13, 2025.

For more information, see [Enhanced IP address allocation](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#enhanced-allocation).

## January 20, 2026

Feature

For auto mode VPC networks, added a new subnet `10.232.0.0/20` for the Bangkok `asia-southeast3` region. For more information, see [Global locations](https://cloud.google.com/about/locations) and [Auto mode IP ranges](https://cloud.google.com/vpc/docs/subnets#ip-ranges).

## November 14, 2025

Feature

Dynamic Private Service Connect interfaces are available in **General Availability**. Private Service Connect interfaces let service producers initiate connections to service consumers. You can update a VM instance to add or remove dynamic Private Service Connect interfaces without needing to restart or recreate the instance.

For more information, see [Private Service Connect interface types](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#types).

## November 10, 2025

Feature

Service producers can [accept or reject connections from individual Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#accept-endpoint). This feature is available in **Preview**.

## November 03, 2025

Feature

VPC Network Peering supports peering connections in consensus mode. This feature is available in **General Availability**. For more information, see [Connection mode](https://docs.cloud.google.com/vpc/docs/about-peering-connections#connection-mode).

## October 30, 2025

Feature

Dynamic Network Interfaces (NICs) are available in **General Availability**.

Dynamic NICs let you update an instance to add or remove network interfaces without having to restart or recreate the instance.

You can also use Dynamic NICs when you need more network interfaces. The maximum number of vNICs for most machine types in Google Cloud is 10; however, you can configure up to 16 total interfaces by using Dynamic NICs.

For more information, see the following:

  * [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#dynamic-nics)
  * [Create a VM instance with Dynamic NICs](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)
  * [Add Dynamic NICs to an existing instance](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics)



## October 29, 2025

Feature

You can specify a `/96` IPv6 address range when reserving static regional IPv6 addresses. For more information, see the following:

  * [Reserve a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address)
  * [Reserve a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address)



This feature is available in **General Availability**.

## October 24, 2025

Feature

You can view IP address utilization when you [list](https://cloud.google.com/vpc/docs/create-modify-vpc-networks#listing_existing_subnets) or [describe](https://cloud.google.com/vpc/docs/create-modify-vpc-networks#describing_an_existing_subnet) subnets. IP address utilization displays the number of free and allocated IP addresses in a subnet. This feature is available in **General Availability**.

## October 20, 2025

Feature

VPC Flow Logs supports logging for Cloud Run resources that are configured with [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc). This feature is available in **General Availability**.

For more information, see [Serverless flows](https://docs.cloud.google.com/vpc/docs/about-traffic-flows#serverless-flows) and [ServerlessDetails field format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#serverless-details).

## October 15, 2025

Feature

Private Service Connect health is available in **Preview**.

Private Service Connect health lets service producers define health states to support automatic cross-region failover for consumers that use Private Service Connect backends. For more information, see [About Private Service Connect health for automatic cross-region failover](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-health).

## September 26, 2025

Feature

The following features of VPC Flow Logs are available in **General Availability** :

  * Logging for [RDMA over Falcon transport](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles#overview)
  * Enhanced round-trip time precision for TCP and Falcon traffic



For more information, see [About VPC Flow Logs records](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#record_format).

## September 25, 2025

Feature

The following features of VPC Flow Logs are available in **General Availability** through the Network Management API:

  * [Enabling VPC Flow Logs for an organization](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-organization)
  * [Enabling VPC Flow Logs for a VPC network](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-network)
  * [Enabling VPC Flow Logs for a subnet](https://docs.cloud.google.com/vpc/docs/using-flow-logs#network-management)



For more information, see [Supported configurations](https://docs.cloud.google.com/vpc/docs/flow-logs#configurations).

## September 23, 2025

Feature

Service producers can publish services that are hosted on [cross-region internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal). This feature is available in **General Availability**. For more information, see [Publish services by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

## September 12, 2025

Feature

You can create a VPC network that supports RDMA over [Falcon transport](https://cloud.google.com/blog/topics/systems/introducing-falcon-a-reliable-low-latency-hardware-transport), which lets you run AI and high performance computing (HPC) workloads on VM instances that have the `IRDMA` network interface type in Google Cloud, such as H4D instances. This feature is available in **Preview**. For more information, see [RDMA network profiles](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).

## August 26, 2025

Feature

IPv6-only subnets and instances are available in **General Availability**. For more information, see the following:

  * [Add an IPv6-only subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6-only)
  * [Create an IPv6-only instance](https://docs.cloud.google.com/compute/docs/instances/create-ipv6-instance#create-vm-ipv6-only)
  * [Configure IPv6-only subnets and instances with DNS64 and NAT64](https://docs.cloud.google.com/vpc/docs/connect-ipv6-to-ipv4)



You can also use an IPv6-only NAT subnet to [publish a service with Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service).

For information about which services support IPv6-only configurations, see [IPv6 support in Google Cloud](https://docs.cloud.google.com/vpc/docs/ipv6-support).

Feature

VPC Flow Logs supports logging for [RDMA flows over Converged Ethernet](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles#overview), such as GPU-to-GPU flows from A3 Ultra, A4, and A4X VMs. This feature is available in **General Availability**. For more information, see [About VPC Flow Logs records](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records).

## August 08, 2025

Feature

VPC Flow Logs includes metadata annotations for Google services such as Google APIs and VPC-hosted services. The following annotations are available in **General Availability** :

  * `service_name`
  * `connectivity`
  * `private_domain`



These annotations are supported for flows between VMs in VPC networks and Google services and for flows between on-premises endpoints and Google services (through Cloud Interconnect and Cloud VPN). For more information, see [GoogleServiceDetails field format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#google-service-details).

## August 04, 2025

Feature

When you reserve an internal range with an automatically allocated IPv4 CIDR block, you can specify the [allocation strategy](https://docs.cloud.google.com/vpc/docs/internal-ranges#allocation-strategies) that is used to select a free block. This feature is available in **General Availability**.

## July 09, 2025

Feature

Dynamic Private Service Connect interfaces are available in **Preview**. You can update VM instances to add or remove dynamic Private Service Connect interfaces without restarting or recreating the instance.

For more information, see [Private Service Connect interface types](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#types).

Feature

VPC Network Peering supports peering connections in consensus mode. This feature is available in **Preview**. For more information, see [Connection mode](https://docs.cloud.google.com/vpc/docs/about-peering-connections#connection-mode).

## July 08, 2025

Feature

The following features of policy-based routes are available in **General Availability** :

  * Applying policy-based routes to IPv6 traffic
  * Using a next hop that is in a peered VPC network



For more information, see [Create policy-based routes](https://docs.cloud.google.com/vpc/docs/use-policy-based-routes#create).

## June 27, 2025

Feature

Private Service Connect service connectivity automation periodically retries endpoint create or delete operations that fail due to errors. This feature is available in **General Availability**. For more information, see [Automatic retries for endpoint failures](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation#endpoint-automation).

## June 18, 2025

Feature

The following features of VPC Flow Logs are available in **Preview** through the Network Management API:

  * [Enabling VPC Flow Logs for an organization](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-organization)
  * [Enabling VPC Flow Logs for a VPC network](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-network)
  * [Enabling VPC Flow Logs for a subnet](https://docs.cloud.google.com/vpc/docs/using-flow-logs#network-management)



For more information, see [Supported configurations](https://docs.cloud.google.com/vpc/docs/flow-logs#configurations).

## June 16, 2025

Feature

VPC Flow Logs annotates RDMA traffic that is reported from A3 Mega VMs. This feature is available in **General Availability**. For more information, see [About VPC Flow Logs records](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records).

## June 13, 2025

Feature

Dynamic Network Interfaces (NICs) are available in **Preview**. 

Dynamic NICs let you update an instance to add or remove network interfaces without having to restart or recreate the instance.

You can also use Dynamic NICs when you need more network interfaces. The maximum number of vNICs for most machine types in Google Cloud is 10; however, you can configure up to 16 total interfaces by using Dynamic NICs.

For more information, see the following:

  * [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#dynamic-nics)
  * [Create a VM instance with Dynamic NICs](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)
  * [Add Dynamic NICs to an existing instance](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics)



## June 05, 2025

Feature

You can [publish a Secure Web Proxy instance](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment) as a Private Service Connect service. Making Secure Web Proxy available as a published service lets you centralize egress traffic management across multiple VPC networks. This feature is available in **General Availability**.

## May 28, 2025

Feature

You can assign IPv6 bring your own IP (BYOIP) addresses to a subnet's external address range. These subnet ranges can only be used by VM instances, either as ephemeral or reserved addresses. To reserve addresses from these ranges, create a static regional external IPv6 address with the VM endpoint type. This feature is available in **General Availability**.

For more information, see [Create and use IPv6 sub-prefixes](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes).

## May 19, 2025

Feature

Service producers can publish services that are hosted on [cross-region internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal). This feature is available in **Preview**. For more information, see [Publish services by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

## May 12, 2025

Feature

You can exclude IP address ranges from being used for automatic IP address allocation for internal ranges. This feature is available in **General Availability**. For more information, see [Reserve internal ranges](https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges#create-internal-ranges).

## May 07, 2025

Feature

The following features of internal ranges are available in **General Availability** :

  * Reserving internal ranges with IPv6 addresses
  * Creating immutable ranges (ranges that can't be edited, except for the description)
  * Editable descriptions



For more information, see [Internal ranges overview](https://docs.cloud.google.com/vpc/docs/internal-ranges).

Feature

When you reserve an internal range with an automatically allocated IPv4 CIDR block, you can specify the [allocation strategy](https://docs.cloud.google.com/vpc/docs/internal-ranges#allocation-strategies) that is used to select a free block. This feature is available in **Preview**.

## April 30, 2025

Feature

If you're a service producer that makes a service available through VPC Network Peering, you can [migrate your service to Private Service Connect](https://docs.cloud.google.com/vpc/docs/about-migrating-peering-services-private-service-connect) without changing the IPv4 address that consumers use to access the service. This feature is available in **General Availability**.

## April 10, 2025

Change

When you [create a Private Service Connect endpoint to connect to a regional endpoint](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints) of a supported service, you can use the [public hostname](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints#specifications) in your configuration—for example, `spanner.me-central2.rep.googleapis.com`.

## March 31, 2025

Feature

You can access global Google APIs by using Private Service Connect backends that are based on cross-region internal Application Load Balancers. This feature is available in **General Availability**. For more information, see [Access global Google APIs through backends](https://docs.cloud.google.com/vpc/docs/access-global-google-apis-backends).

## March 26, 2025

Feature

Support for the following is available in **General availability** for dual-stack configurations:

  * IPv6 static routes with a next hop internal passthrough Network Load Balancer (`next-hop-ilb`) 
  * IPv6 static routes with a next hop instance identified by address (`next-hop-address`) 



For more information, see [Next hops and features](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops) in the static routes overview.

## March 07, 2025

Feature

The following features of internal ranges are available in **Preview** :

  * Reserving internal ranges with IPv6 addresses
  * Creating immutable internal ranges (ranges that can't be updated, except for the description)
  * Editable descriptions



For more information, see [Internal ranges overview](https://docs.cloud.google.com/vpc/docs/internal-ranges).

Feature

You can exclude IP address ranges from internal range automatic IP address allocation. This feature is available in **Preview**. For more information, see [Reserve internal ranges](https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges#create-internal-ranges).

Feature

You can create internal ranges that overlap with routes and subnets. This feature is available in **General Availability**. For more information, see [Internal ranges overview](https://docs.cloud.google.com/vpc/docs/internal-ranges).

## March 04, 2025

Feature

For auto mode VPC networks, added a new subnet `10.226.0.0/20` for the Stockholm `europe-north2` region. For more information, see [Global Locations](https://cloud.google.com/about/locations) and [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).

## February 28, 2025

Feature

Accessing [supported global Google APIs](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#global-google-apis) through Private Service Connect backends is available in **General Availability**.

## February 27, 2025

Feature

The following Private Service Connect monitoring metrics are available for both producers and consumers in **General Availability** :

  * Closed connections count
  * Received packets dropped count
  * Sent packets dropped count
  * New connections count
  * Open connections
  * Received bytes count
  * Received packets count
  * Sent bytes count
  * Sent packets count



Additionally, the NAT IP address capacity metric is available for producers in **General Availability**.

You can use these metrics to help monitor and troubleshoot [published services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#dropped-packets), [endpoints that connect to published services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#dropped-packets), and [backends that connect to published services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls#dropped-packets). For more information, see [Monitor Private Service Connect connections](https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-connections).

## February 26, 2025

Feature

[Private Service Connect propagated connections](https://docs.cloud.google.com/vpc/docs/about-propagated-connections) are available in **General Availability**. With propagated connections, services that are accessible in one consumer VPC spoke through Private Service Connect endpoints can be privately accessed by other consumer VPC spokes that are connected to the same Network Connectivity Center hub.

## February 20, 2025

Feature

Private Service Connect service connectivity automation supports IPv6 connectivity to eligible managed services. This feature is available in **General availability**. For more information, see [Endpoint IP versions](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#ip-versions).

## January 27, 2025

Issue

There is a known issue with global access endpoints that access services that are published by using internal passthrough Network Load Balancers or internal protocol forwarding (target instances). Private Service Connect doesn't validate that the global access setting on the endpoint matches the setting on the producer's load balancer. We recommend the following:

  * If you're a service consumer, only enable global access on an endpoint if you know that the producer's load balancer is configured for global access. For more information, see endpoint [Known issues](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#global-access).

  * If you're a service producer whose services are hosted on internal passthrough Network Load Balancers or internal protocol forwarding (target instances), and those services are accessed through global access endpoints, ensure that global access is enabled on your services' load balancers. For more information, see published services [Known issues](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#global-access-service-attachments).




Feature

VPC Flow Logs metadata annotations include [InstanceGroupDetails](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#instance-group-details). This feature is available in **General Availability**.

## January 16, 2025

Feature

[Private Service Connect endpoints for regional Google APIs](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints) can be [configured with IPv6 addresses](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#create-regional-endpoint) to support access from IPv6 clients. This feature is available in **General Availability**.

## January 15, 2025

Feature

You can create an internal range with the usage type `FOR_MIGRATION` to migrate a CIDR range from one subnet to another. For more information, see [Migrating subnet ranges](https://docs.cloud.google.com/vpc/docs/internal-ranges#for-migration). This feature is available in **General Availability**.

Feature

The network profile resource and an RDMA network profile are available in **General Availability**. You can create a VPC network with the RDMA network profile, which lets you run AI workloads on VM instances that have RDMA network interfaces (NICs). For more information, see the following:

  * [Network profiles overview](https://docs.cloud.google.com/vpc/docs/network-profiles)
  * [RDMA network profile](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles)



Feature

If you're a service producer that makes a service available through VPC Network Peering, you can [migrate your service to Private Service Connect](https://docs.cloud.google.com/vpc/docs/about-migrating-peering-services-private-service-connect) without changing the IP address that consumers use to access the service. This feature is available in **Preview**.

Feature

If you create a Private Service Connect backend to connect to a published service, and the producer has let you know which port the service is available on, you can [include the producer port in the backend configuration](https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends#neg-published-service).

For more information about the producer's configuration, see [Producer port configuration](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#producer-ports).

Specifying the producer port in a Private Service Connect backend is available in **General Availability**.

## January 14, 2025

Feature

VPC Flow Logs can sample traffic that is sent through VLAN attachments for Cloud Interconnect and Cloud VPN tunnels. This feature is available in **General Availability**. To enable VPC Flow Logs for VLAN attachments and Cloud VPN tunnels, see [Configure VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs).

## December 17, 2024

Feature

IPv6-only subnets and instances are available in **Preview**. For more information, see the following:

  * [Add an IPv6-only subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6-only)
  * [Create an IPv6-only instance](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#create-vm-ipv6-only)
  * [Types of subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types)



For information about which services support IPv6-only configurations, see [IPv6 support in Google Cloud](https://docs.cloud.google.com/vpc/docs/ipv6-support).

## December 13, 2024

Feature

Private Service Connect [service connectivity automation](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation) lets you automate connectivity to supported Google service instances that are located in a [different project, folder, or organization](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#custom-scope) than the service consumer (custom scope). This feature is available in **General Availability**.

## December 11, 2024

Feature

[Private Service Connect port mapping](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-port-mapping) is available in **General Availability**. Port mapping lets consumer virtual machine (VM) instances privately communicate with specific service ports on specific producer VMs through a single Private Service Connect endpoint.

## November 18, 2024

Feature

For auto mode VPC networks, added a new subnet `10.224.0.0/20` for the Mexico `northamerica-south1` region. For more information, see [Global Locations](https://cloud.google.com/about/locations) and [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).

## October 31, 2024

Feature

Support for [IPv6 static routes](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops) with a next hop internal passthrough Network Load Balancer (`next-hop-ilb`) is available in **Preview**.

## September 27, 2024

Feature

Private Service Connect supports IPv6 in **General Availability** for the following [supported configurations](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility#endpoints-services):

  * Service consumers can access published services by using [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) that have IPv6 addresses. 
  * Service producers that use [supported load balancers](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#endpoint-support) can [publish services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) by using service attachments that have IPv6 addresses.



For more information, see [IP version translation](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#ip-version-translation).

## September 13, 2024

Feature

You can use Private Service Connect endpoints to [access the regional service endpoints of supported Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints). This feature is available in **General Availability**.

## August 23, 2024

Feature

VPC Flow Logs can sample traffic that is sent through VLAN attachments for Cloud Interconnect and Cloud VPN tunnels. This feature is available in **Preview**. For more information, see [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs).

Breaking

The live migration feature for bring your own IP v1 has been removed. For new configurations, we recommend that you use [bring your own IP v2](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#comparison), which lets you control when prefixes are advertised.

## August 12, 2024

Feature

VPC Flow Logs includes the following metadata annotations in **General Availability** :

  * `src_gateway` and `dest_gateway`
  * `src_google_service` and `dest_google_service`
  * `load_balancing`
  * `network_service`
  * `psc`



For more information, see [Record Format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#record_format).

## July 24, 2024

Feature

The following producer load balancers now support all [Private Service Connect monitoring metrics](https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-connections):

  * Regional internal Application Load Balancer
  * Regional internal proxy Network Load Balancer



Feature

Predefined dashboards for monitoring Private Service Connect connections have been enhanced:

  * The [dashboard for monitoring published services](https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-connections#predefined-producer-dashboards) now includes more metrics.
  * A [new dashboard](https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-connections#predefined-consumer-dashboards) is available for monitoring endpoints that connect to published services.



## July 22, 2024

Feature

In the Google Cloud Console, the **Effective routes** tab on the **Routes** page shows only routes that are effective. You can optionally show suppressed routes by using the **Show suppressed routes** toggle. You can also view the reason why a given route is suppressed. For more information, see [List routes for a VPC network](https://docs.cloud.google.com/vpc/docs/using-routes#listingroutes).

## July 17, 2024

Change

[Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) can be used to reach [regional endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints) for supported Google APIs. Regional endpoints replace locational endpoints for Private Service Connect backends.

Change

The list of [supported regional endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints) that can be accessed by Private Service Connect [endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints) and [backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) is updated to include additional supported Google APIs and regions.

## June 28, 2024

Breaking

Bring your own IP [does not support creating BYOIP addresses in Shared VPC service projects](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#support). This limitation is documented, but was previously not enforced. Enforcement has been added to prevent the creation of BYOIP addresses in service projects. If you're using bring your own IP with Shared VPC, use the project architecture described in [BYOIP addresses administration with Shared VPC](https://docs.cloud.google.com/vpc/docs/byoip-planning#byoip-shared-vpc).

## June 17, 2024

Feature

[Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) support using a [cross-regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) to access [global Google API targets](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#global-google-apis). This feature is available in **Preview**.

## June 14, 2024

Feature

[Private Service Connect port mapping](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-port-mapping) is available in **Preview**. Port mapping lets consumer virtual machine (VM) instances privately communicate with specific service ports on specific producer VMs through a single Private Service Connect endpoint.

Feature

[Private Service Connect propagated connections](https://docs.cloud.google.com/vpc/docs/about-propagated-connections) are available in **Preview**. With propagated connections, services that are accessible in one consumer VPC spoke through Private Service Connect endpoints can be privately accessed by other consumer VPC spokes that are connected to the same Network Connectivity Center hub.

## June 10, 2024

Feature

VPC Flow Logs includes internet routing details for egress flows. For more information, see [InternetRoutingDetails field format](https://docs.cloud.google.com/vpc/docs/flow-logs#InternetRoutingDetails). This field is available in **General Availability**.

Feature

The following features of policy-based routes are available in **Preview** :

  * Applying policy-based routes to IPv6 traffic
  * Using a next hop that is in a peered VPC network



For more information, see [Create policy-based routes](https://docs.cloud.google.com/vpc/docs/use-policy-based-routes#create).

## June 03, 2024

Feature

Bring your own IP lets you [bring your own public IPv6 addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#comparison) to Google Cloud. IPv6 BYOIP addresses can be used with [external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#byoip-ipv6). Bring your own IP for IPv6 addresses is available in **General Availability**.

Feature

Support for [IPv6 static routes](https://docs.cloud.google.com/vpc/docs/routes#static-route-next-hops) with a next hop instance identified by address (`next-hop-address`) is available in **Preview**.

## May 03, 2024

Feature

Private Service Connect supports IPv6 in **Preview** for the following [supported configurations](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility#endpoints-services):

  * Service consumers can access published services by using [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) that have IPv6 addresses. 
  * Service producers that use [supported load balancers](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#endpoint-support) can [publish services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) by using service attachments that have IPv6 addresses.



For more information, see [IP version translation](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#ip-version-translation).

## May 02, 2024

Announcement

Private Service Connect now offers consumers volume-based discounts for consumer data processing. For more information, see [Consumer data processing](https://cloud.google.com/vpc/pricing#psc-consumer-data-processing).

Announcement

Service producers are no longer charged producer data processing for ingress or egress traffic through a Private Service Connect service attachment. For more information, see [pricing for published services](https://cloud.google.com/vpc/pricing#psc-service-attachment).

## April 26, 2024

Feature

[Bring your own IP v2](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#comparison) for regional addresses is available in **General Availability**.

  * v2 public advertised prefixes are provisioned in approximately two weeks.
  * v2 public delegated prefixes are provisioned in minutes.
  * v2 prefixes are not automatically announced when provisioned; you [control when to announce or withdraw advertisements](https://docs.cloud.google.com/vpc/docs/manage-bgp-announcement).



## April 23, 2024

Change

The Private Service Connect interface documentation has been updated. Google recommends avoiding multi-tenant architectures, where multiple consumers connect to the same Private Service Connect interface VM. In a multi-tenant architecture, if one consumer terminates their Private Service Connect interface connection, other consumers that are connected to the same VM also lose connectivity. For more information, see [Limitations](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#limitations).

## April 01, 2024

Feature

You can use [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) to collect IPv6 traffic. This feature is available in **General Availability**.

## March 07, 2024

Feature

[Internal ranges](https://docs.cloud.google.com/vpc/docs/internal-ranges) are available in **General Availability**. Internal ranges let you allocate blocks of private IP addresses in VPC networks and specify how those addresses can be used.

## February 26, 2024

Change

The VPC documentation has been updated with a new page that describes which services in Google Cloud include support for IPv6. For more information, see [IPv6 support in Google Cloud](https://docs.cloud.google.com/vpc/docs/ipv6-support).

## February 05, 2024

Feature

[Support for IPv6 extension headers](https://docs.cloud.google.com/vpc/docs/vpc#supported_protocols) is available in **General Availability**.

## January 31, 2024

Feature

For auto mode VPC networks, added a new subnet `10.218.0.0/20` for the Johannesburg `africa-south1` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).

Feature

[Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) are available in **General Availability**. Private Service Connect interfaces let service producers initiate connections to consumer VPC networks.

## January 11, 2024

Change

Regional service endpoints that are used with [Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) are now referred to as [_locational service endpoints_](https://docs.cloud.google.com/vpc/docs/locational-service-endpoints). Locational service endpoints are different from [regional service endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints#supported).

Feature

Private Service Connect endpoints support [accessing regional service endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints). This feature is available in **Preview**.

## December 19, 2023

Feature

You can use Organization Policy Service custom constraints to provide more granular and customizable control over specific fields for some VPC resources. This feature is available in **General Availability**. For more information, see [Manage VPC resources by using custom organization policies](https://docs.cloud.google.com/vpc/docs/custom-constraints).

Feature

You can use [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) to collect IPv6 traffic. This feature is available in **General Availability**.

This note is incorrect. The feature was released in **Preview** on this date.

## December 13, 2023

Feature

Accessing [supported global Google APIs](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#global-google-apis) through Private Service Connect backends is available in **Preview**.

## November 20, 2023

Feature

You can use [Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) to access published services that are hosted on [regional internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal) and [regional internal proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy).

## October 02, 2023

Feature

[Private Service Connect backends with published service targets](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#published-services) can be added to [global external TCP proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/tcp). This feature is available in **Preview**.

Feature

[Private Service Connect service connectivity automation](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) is available in **General Availability**. Service connectivity automation lets service producers automate deployment and service connectivity to eligible managed services on behalf of consumers.

## September 29, 2023

Feature

[Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) support using an [external regional TCP proxy load balancer](https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends#add-neg-ext-tcp-proxy-lb) or an [internal regional TCP proxy load balancer](https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends#add-neg-tcp-proxy-lb) to access published services. These features are available in **General Availability**.

## September 19, 2023

Feature

For auto mode VPC networks, added a new subnet `10.216.0.0/20` for the Dammam `me-central2` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).

## September 14, 2023

Feature

[Policy-based routing](https://docs.cloud.google.com/vpc/docs/policy-based-routes) is available in **General Availability**. You can select a next hop based on more than a packet's destination IP address. You can match traffic by protocol and source IP address as well.

Issue

If you've used [Google provider for Terraform](https://registry.terraform.io/providers/hashicorp/google/latest) versions earlier than 4.76.0 to create Private Service Connect [service attachments](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-attachments), **do not** upgrade to versions 4.76.0 through 4.81.x. When you run `terraform apply` after the upgrade, Terraform might unintentionally delete and recreate the service attachments and close existing Private Service Connect connections. Recreated service attachments **do not** automatically re-establish Private Service Connect connections.

Upgrading to version 4.82.0 or later ensures that service attachments are not recreated. 

Versions 4.76.0 and later turn on [connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#connection-reconciliation) by default, which might result in different service attachments having different settings for this field, depending on when they were created.

For more information and workarounds, see [Disconnections after upgrading the Google provider for Terraform](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#terraform-versions).

## September 05, 2023

Feature

Support for [IPv6 static routes](https://docs.cloud.google.com/vpc/docs/routes#static-route-next-hops) with the following next hops is generally available ([GA](https://cloud.google.com/products#product-launch-stages)): 

  * `next-hop-gateway`
  * `next-hop-instance`



## August 30, 2023

Feature

You can add Resource Manager tags to supported VPC resources. For more information, see [Create and manage tags for VPC resources](https://docs.cloud.google.com/vpc/docs/create-manage-tags-vpc-resources).

## August 22, 2023

Feature

For auto mode VPC networks, added a new subnet `10.214.0.0/20` for the Berlin `europe-west10` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).

## August 14, 2023

Feature

[Private Service Connect backends with published service targets](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#published-services) can be added to [cross-region Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal). This feature is available in **Preview**.

Change

VLAN attachments for Cloud Interconnect that have Dataplane v1 can access Private Service Connect endpoints from hybrid networks. For more information, see [access endpoints from hybrid networks](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises).

Change

[Private Service Connect endpoints that have global access enabled](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) can access [published services](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services) that are based on the following [load balancer configurations](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#endpoint-support):

  * Internal Application Load Balancer with global access enabled
  * Regional internal proxy Network Load Balancer with global access enabled



## August 02, 2023

Feature

[Connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#connection-reconciliation) is available in **General Availability**. When connection reconciliation is enabled for a service attachment, updating the service attachment's [consumer accept or reject lists](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#consumer-lists) affects existing Private Service Connect connections in addition to new and pending connections.

## July 28, 2023

Change

New pages for Private Service Connect:

  * [Deployment patterns](https://docs.cloud.google.com/vpc/docs/private-service-connect-deployments)
  * [Architecture and performance](https://docs.cloud.google.com/vpc/docs/private-service-connect-architecture)



## July 18, 2023

Change

All service attachments, including those created before March 1, 2023, consume one NAT IP address for each connected endpoint or backend. For more information, see [NAT subnet sizing](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#subnet-capacity).

## July 17, 2023

Feature

You can [publish a service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) that is hosted on an [internal passthrough Network Load Balancer that forwards traffic on all ports (`--ports=all`)](https://docs.cloud.google.com/load-balancing/docs/internal#all_ports). This feature is available in **General Availability**.

## July 10, 2023

Breaking

By default, public advertised prefixes can be used only to create regional public delegated prefixes. If you need to create global public delegated prefixes, you must request access. For more information about this behavior change and how to request access, see [Behavior changes for BYOIP](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#behavior-change).

## July 05, 2023

Feature

[Moving a reserved external IPv4 address](https://docs.cloud.google.com/vpc/docs/move-ip-address-different-project) from one project to another is available in **General Availability**.

## June 30, 2023

Feature

You can use custom constraints to provide more granular and customizable control over specific fields for some VPC resources. For more information, see [Manage VPC resources by using custom constraints](https://docs.cloud.google.com/vpc/docs/custom-constraints). This feature is available in **Preview**.

## June 20, 2023

Feature

Service consumers can use organization policies with the [`compute.restrictPrivateServiceConnectProducer` list constraint](https://docs.cloud.google.com/vpc/docs/private-service-connect-security#consumer-side-org-policies) to block Private Service Connect endpoints and backends from connecting to service attachments in other organizations. For more information, see [Block endpoints and backends from connecting to unauthorized service attachments](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-consumers#add-org-policy).

Service producers can use organization policies with the [`compute.restrictPrivateServiceConnectConsumer` list constraint](https://docs.cloud.google.com/vpc/docs/private-service-connect-security#producer-side-org-policies) to control which endpoints and backends can connect to Private Service Connect service attachments within a producer organization or project. For more information, see [Block unauthorized endpoints and backends from connecting to service attachments](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-producers#block-consumers).

These constraints are available in **General Availability**.

Feature

The [connection preference](https://docs.cloud.google.com/vpc/docs/private-service-connect-security#connection-preference) for a Private Service Connect published service can be configured on the VPC network level in addition to project level. For more information, see [Publish a service with explicit approval](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service-explicit). This feature is available in **General Availability**.

## June 13, 2023

Feature

[Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) are available in **Preview**. Private Service Connect interfaces let service producers initiate connections to consumer VPC networks.

## June 04, 2023

Feature

Support for [IPv6 static routes](https://docs.cloud.google.com/vpc/docs/routes#ipv6_support) with the following next hops is available in **Preview** : 

  * `next-hop-gateway`
  * `next-hop-instance`



## May 26, 2023

Feature

**General Availability** : You can use the `private.googleapis.com` and `restricted.googleapis.com` virtual IP addresses (VIPs) to access Google APIs and services with IPv6 addresses. For more information, see the following pages:

  * [Use the VIPs from VMs with internal IPv6 addresses](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ipv6-support)
  * [Use the VIPs from VMs with external IPv6 addresses](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip#ipv6-support)
  * [Use the VIPs from on-premises hosts with IPv6 addresses](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid#ipv6-support)
  * [Use the VIPs with VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity)



Feature

[Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) support [using an external regional TCP proxy load balancer to access published services](https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends#add-neg-ext-tcp-proxy-lb). This feature is available in **Preview**.

## May 23, 2023

Feature

[Reserving static regional internal IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address#reservenewip) is available in **General Availability**.

Feature

[Reserving static regional external IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#reserve_new_static) is available in **General Availability**.

Feature

[Support for IPv6 extension headers](https://docs.cloud.google.com/vpc/docs/vpc#supported_protocols) is available in **Preview**.

Feature

[Internal ranges](https://docs.cloud.google.com/vpc/docs/internal-ranges) are available in **Preview**. Internal ranges let you allocate blocks of private IP addresses in VPC networks and specify how those addresses can be used.

## May 18, 2023

Feature

[Private Service Connect service connectivity automation](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) is available in **Preview**. Service connectivity automation lets service producers automate deployment and service connectivity to eligible managed services on behalf of consumers.

## May 17, 2023

Feature

[Global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) for Private Service Connect endpoints for published services is available in **General Availability**. When global access is configured, clients in any region can send traffic to Private Service Connect endpoints.

## April 20, 2023

Feature

[Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) support [using an internal regional TCP proxy load balancer to access published services](https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends#add-neg-tcp-proxy-lb). This feature is available in **Preview**.

## April 19, 2023

Feature

Private Service Connect endpoints for published services can be configured with [global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access). When global access is configured, clients in any region can send traffic to endpoints. Global access for endpoints is available in **Preview**.

## April 10, 2023

Change

Documentation updates for Private Service Connect:

  * Private Service Connect endpoints with consumer HTTP(S) controls are now called _Private Service Connect backends_. The documentation is updated to reflect this change.
  * The [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) overview page is updated.
  * New pages for Private Service Connect: 
    * [Private Service Connect compatibility](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility): describes the features and compatibility of all Private Service Connect configurations and supported services.
    * [About accessing published services through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints)
    * [About accessing Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints)
    * [About published services](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services)
    * [DNS configuration for published services](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services)



## April 05, 2023

Feature

**General Availability:** [Private Service Connect endpoints with consumer HTTP(S) controls](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) support accessing regional Google APIs and published services using [the following load balancers](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#supported-lb-targets):

  * Regional internal HTTP(S) load balancer
  * Regional external HTTP(S) load balancer



## March 30, 2023

Feature

For auto mode VPC networks, added a new subnet 10.212.0.0/20 for the Doha me-central1 region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/vpc#ip-ranges).

## March 23, 2023

Feature

For auto mode VPC networks, added a new subnet 10.210.0.0/20 for the Turin europe-west12 region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/vpc#ip-ranges).

## March 20, 2023

Feature

[Managing Shared VPC with the Shared VPC Admin role at the folder level](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#nominating_shared_vpc_admins_for_the_organization) is available in **General Availability**.

## March 14, 2023

Feature

[Hybrid subnets](https://docs.cloud.google.com/vpc/docs/hybrid-subnets) are available in **Preview**. A hybrid subnet combines an on-premises subnet and a VPC subnet into a single logical subnet. You can migrate individual workloads and instances from the on-premises subnet to the VPC subnet over time without needing to change IP addresses.

## March 10, 2023

Feature

Connectivity to Private Service Connect endpoints used to access a managed service is [supported over VLAN attachments for Cloud Interconnect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises). This feature is available in **General Availability**.

Feature

Consumption of IP addresses in Private Service Connect NAT subnets is improved for service attachments that are created after March 1st, 2023. For more information, see [NAT subnets](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#psc-subnets). This improvement is available in **General Availability**.

## January 26, 2023

Feature

[Policy-based routing](https://docs.cloud.google.com/vpc/docs/policy-based-routes) is available in **Preview**. You can select a next hop based on more than a packet's destination IP address. You can match traffic by protocol and source IP address as well.

## December 20, 2022

Feature

**Preview** : You can use [fully qualified domain name (FQDN) objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview) in firewall policy rules to filter incoming or outgoing traffic from specific domain names.

Feature

**Preview** : You can use [Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview) to secure your network by allowing or blocking traffic based on threat intelligence data.

Feature

**Preview** : You can use [address groups](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies) to combine multiple IP addresses and IP ranges into a single named logical unit. You can then use this unit across multiple rules in the same or different firewall policies.

Feature

**Preview** : You can use [geo-location objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview) in firewall policy rules to filter external IPv4 and external IPv6 traffic based on specific geographic locations or regions.

## December 14, 2022

Feature

**General Availability:** VPC Peering supports the [exchange of IPv6 routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#route-exchange-options) between peered VPC networks.

## December 13, 2022

Feature

[Reserving static regional internal IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address#reservenewip) is available in **Preview**.

## November 17, 2022

Feature

**Preview** : Connectivity to Private Service Connect endpoints used to access a managed service is [supported over VLAN attachments for Cloud Interconnect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises)

## November 16, 2022

Feature

**Preview:** [Private Service Connect endpoints with consumer HTTP(S) controls](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) now support accessing regional Google APIs and managed services using the following load balancers:

  * Regional internal HTTP(S) load balancer
  * Regional external HTTP(S) load balancer



## November 08, 2022

Feature

**Preview** : You use the `private.googleapis.com` and `restricted.googleapis.com` VIPs to access Google APIs and services using IPv6 addresses. For more information, see the following pages:

  * [Use the VIPs from VMs with internal IPv6 addresses](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ipv6-support)
  * [Use the VIPs from VMs with external IPv6 addresses](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip#ipv6-support)
  * [Use the VIPs from on-premises hosts with IPv6 addresses](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid#ipv6-support)
  * [Use `restricted.googleapis.com` with VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity)



## November 01, 2022

Feature

Private Service Connect supports [internal regional TCP proxy load balancers as a service attachment target](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid#publish) in **General Availability**. This lets you create hybrid TCP/UDP services where a clients in a VPC network can connect to an on-premise service by going through [Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) and a [TCP proxy with hybrid NEGs](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid) to reach a hybrid endpoint.

## October 21, 2022

Feature

You can specify the [source IP ranges for egress rules](https://docs.cloud.google.com/vpc/docs/firewall-policies-rule-details#hfp-nfp-egress-src) and the [destination IP ranges for ingress rules](https://docs.cloud.google.com/vpc/docs/firewall-policies-rule-details#hfp-nfp-ingress-dest). This feature is available in **Preview**.

## October 14, 2022

Feature

[Moving a reserved external IPv4 address](https://docs.cloud.google.com/vpc/docs/move-ip-address-different-project) from one project to another is available in **Preview**.

## October 05, 2022

Feature

For auto mode VPC networks, added a new subnet `10.208.0.0/20` for the Tel Aviv `me-west1` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).

## October 04, 2022

Feature

[Accessing managed services using Private Service Connect with consumer HTTP(S) controls](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls) is available in **General Availability** for the global external HTTP(S) load balancer.

## September 26, 2022

Feature

**General Availability** : You can monitor the following Private Service Connect producer metrics using Cloud Monitoring:

  * Connected consumer forwarding rules
  * Used NAT IP addresses



For more information, see [Monitor Private Service Connect published services](https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-published-services).

## September 23, 2022

Change

VPC Service Controls ingress and egress rules are no longer required to establish Private Service Connect connections from inside a VPC Service Controls perimeter.

Establishing a Private Service Connect connection between consumer and producer projects that are not in the same VPC Service Controls perimeter does not require explicit authorization with egress policies. However, all communication to VPC Service Controls-supported services through the Private Service Connect endpoint is protected by the VPC Service Controls perimeter.

For more information, see [VPC Service Controls](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#vpc-sc).

## August 08, 2022

Feature

[Internal and external IPv6 addresses](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) are available in all regions in **General Availability** :

  * **Subnets** : [Dual-stack subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6) that have both IPv4 and IPv6 subnet ranges.

  * **Routes** : [Subnet routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes) for IPv6 subnet ranges.

  * **Instances** : [Dual-stack instances with both IPv4 and IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address), including [instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces).




## August 05, 2022

Feature

[Network firewall policies](https://docs.cloud.google.com/vpc/docs/network-firewall-policies) and [regional firewall policies](https://docs.cloud.google.com/vpc/docs/regional-firewall-policies) are now available in **General Availability**.

## July 14, 2022

Feature

Private Service Connect supports [publishing a service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) that is hosted on the following load balancers:

  * [Internal TCP/UDP load balancer with global access enabled](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#ilb-global-access)
  * [Internal protocol forwarding (target instances)](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding)



These features are available in **General Availability**.

## June 22, 2022

Feature

Private Service Connect supports [publishing a service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) that is hosted on an [internal regional TCP proxy load balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) in a service producer VPC network. The backends can be located in Google Cloud, in other clouds, in an on-premises environment, or any combination of these locations.

This feature is available in **Preview**.

## June 13, 2022

Feature

VPC networks now support jumbo frame MTUs within the same subnet. MTU can be set from `1300` to `8896`. For details, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).

## June 07, 2022

Feature

For auto mode VPC networks, added a new subnet `10.206.0.0/20` for the Dallas `us-south1` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).

## May 24, 2022

Feature

For auto mode VPC networks, added a new subnet `10.202.0.0/20` for the Columbus `us-east5` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).

## May 17, 2022

Feature

Accessing Google APIs and services from Compute Engine instances using either internal IPv6 addresses with [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) or [external IPv6 addresses](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip) is available in **General Availability**.

## May 10, 2022

Feature

For auto mode VPC networks, added a new subnet `10.204.0.0/20` for the Madrid `europe-southwest1` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).

## May 09, 2022

Feature

[Reserving static regional external IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#regional-ext-ipv6) is available as a limited **Preview** feature. Contact your sales representative for access.

## May 02, 2022

Feature

For auto mode VPC networks, added a new subnet `10.200.0.0/20` for the Paris `europe-west9` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).

## April 25, 2022

Feature

Automatic DNS configuration for Private Service Connect endpoints is available in **General Availability**.

**For service producers** : When you publish a managed service with Private Service Connect, you can optionally specify a [domain name for the service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#dns-configuration). 

**For service consumers** : When you create a Private Service Connect endpoint to connect to a managed service that has a specified domain name, a [DNS entry for the Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#auto-dns) is created in a Service Directory DNS zone.

## April 20, 2022

Feature

For auto mode VPC networks, added a new subnet `10.198.0.0/20` for the Milan `europe-west8` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).

## January 24, 2022

Feature

Accessing [supported regional service endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints) using [Private Service Connect with consumer HTTP(S) controls](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls) is available in **General Availability**.

Feature

Accessing [managed services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) using [Private Service Connect with consumer HTTP(S) controls](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls) is available in **Preview**.

## January 06, 2022

Change

By default, Google Cloud blocks egress packets sent to TCP destination port 25 of an external IP address (including an external IP address of another Google Cloud resource). This restriction has been removed from projects owned by select Google Cloud customers.

For more information, see [Blocked and limited traffic](https://docs.cloud.google.com/vpc/docs/firewalls#blockedtraffic).

## December 15, 2021

Feature

When you [create a custom mode VPC network](https://docs.cloud.google.com/vpc/docs/using-vpc#create-custom-network), you can select predefined firewall rules which address common use cases for connectivity to instances. This feature is available in **General Availability**.

## December 13, 2021

Feature

[Accessing published services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) using a Private Service Connect endpoint from [on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises) that are connected to a VPC network using Cloud VPN is now available in **General Availability**.

Fixed

[Connectivity from on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises) to a Private Service Connect endpoint that is used to access managed services now correctly establishes for all service attachment configurations.

## November 16, 2021

Feature

For auto mode VPC networks, added a new subnet `10.194.0.0/20` for the Santiago `southamerica-west1` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/vpc#ip-ranges).

## November 12, 2021

Feature

Private Service Connect endpoints used to [access a managed service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) are now [automatically registered](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#dns-endpoint) with Service Directory. This feature is available in **General Availability**.

Feature

[Converting a single-region legacy network](https://docs.cloud.google.com/vpc/docs/legacy#single-region-conversion) to a custom mode VPC network is now available in **Preview**.

## November 02, 2021

Fixed

Changes in status for [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) that you use access managed services are now logged in Cloud Logging.

## October 21, 2021

Fixed

This issue is now fixed: [Connectivity from on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises) to a Private Service Connect endpoint that is used to access published services might not establish for some existing Cloud VPN connections. As a workaround, recreate the VPN gateway and the VPN tunnels.

## October 12, 2021

Feature

[Accessing published services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) using a Private Service Connect endpoint is now available from [on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises) that are connected to a VPC network using Cloud VPN. This feature is available in **Preview**.

Feature

Using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to [publish services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) that are hosted on the backends of an internal HTTP(S) load balancer is now **Generally Available**.

Issue

[Connectivity from on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises) to a Private Service Connect endpoint that is used to access managed services does not establish if both of the following conditions are met:

  * The service is published with explicit project approval

  * Your project is not already approved before you create the endpoint.




See [known issues](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#known-issues) for a workaround while this feature is in Preview.

Issue

[Connectivity from on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises) to a Private Service Connect endpoint that is used to access published services might not establish for some existing Cloud VPN connections. As a workaround, recreate the VPN gateway and the VPN tunnels.

## October 04, 2021

Fixed

The number of [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) that are connected to a [service attachment](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) is now correctly adjusted when an endpoint is deleted.

Fixed

If you are using [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) to access services in another VPC network, and you create more endpoints than are allowed by the limit set by the service producer, any endpoints created after the limit is reached have a status of **Pending** , as expected. Now, if you remove endpoints to get below the limit, the status of those endpoints correctly changes to **Accepted**.

## September 16, 2021

Fixed

Enabling or disabling [PROXY protocol](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#proxy-protocol) after a Private Service Connect service attachment is created now correctly changes the configuration.

## September 14, 2021

Feature

Full control over which protocols are mirrored by [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/using-packet-mirroring#creating) is now available in **General Availability**.

## August 25, 2021

Fixed

Private Service Connect [service attachment deletions](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#delete-attachment) are now logged in Cloud Logging.

## August 23, 2021

Feature

Using [Private Service Connect with consumer HTTP(S) service controls](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls) to access [supported regional service endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints) is now available in **Preview**.

## August 17, 2021

Fixed

If you are using [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) to access services in another VPC network, [deleting an endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#delete-endpoint) no longer fails if you try to delete multiple endpoints in a short period of time.

## August 03, 2021

Feature

For auto mode VPC networks, added a new subnet `10.188.0.0/20` for the Toronto `northamerica-northeast2` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/vpc#ip-ranges).

## July 28, 2021

Feature

[Publishing services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) and [accessing published services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) is now available in **General Availability**.

Issue

The number of [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) that are connected to a [service attachment](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) is not adjusted when an endpoint is deleted. See [workaround information](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#known-issues).

Issue

If you are using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to publish or consume services, the following items are not logged in Cloud Logging: changes in endpoint status, and service attachment deletions.

## July 20, 2021

Feature

[External IPv6 addresses for VM instances](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address) are now available in **General Availability** in [supported regions](https://docs.cloud.google.com/vpc/docs/vpc#ipv6-regions). 

The following features are also available in **General Availability** :

  * System-generated [default IPv6 route](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet) with next-hop default-internet-gateway
  * [Firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) and [hierarchical firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewall-policies#create-rules) that reference IPv6 address ranges.



## July 14, 2021

Fixed

If you're creating a [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) in a Shared VPC network, the endpoint no longer needs to be in the same project that contains the virtual machines (VMs) that send requests to the endpoint.

Fixed

Private Service Connect [service attachment details](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#attachment-details) now correctly shows the status for consumer endpoints. Consumer endpoints can have a status other than Accepted.

## June 30, 2021

Fixed

The billing issue for [non-RFC 1918 addresses for Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#ip-address-requirements) that you use to access Google APIs and services has been fixed.

Feature

[Deleting a private services access connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#removing-connection) now also removes configurations created by the service producer, if Google is the service producer (for example, Cloud SQL). The improved deletion process simplifies administration if you delete a private services access connection, but later want to recreate it. This feature is now available in **General Availability**.

## June 29, 2021

Feature

For auto mode VPC networks, added a new subnet `10.190.0.0/20` for the Delhi `asia-south2` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/vpc#ip-ranges).

## June 23, 2021

Issue

If you are using [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) to access services in another VPC network, and you [delete](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#delete-endpoint) multiple endpoints in a short period of time, one or more of the deletions might fail. To avoid this issue, wait 20 seconds between deletions.

Issue

If you are using [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint) to access services in another VPC network, and you create more endpoints than are allowed by the limit set by the service producer, any endpoints created after the limit is reached have a status of **Pending** , as expected. However, if you remove endpoints to get below the limit, the status of those endpoints does not change to **Accepted**.

## June 21, 2021

Feature

For auto mode VPC networks, added a new subnet `10.192.0.0/20` for the Melbourne `australia-southeast2` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/vpc#ip-ranges).

## June 16, 2021

Fixed

[Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) in consumer networks now won't become unresponsive if they are connected to a service attachment that references a load balancer without backend VMs.

## June 15, 2021

Feature

[Bring your own IP](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) (BYOIP) is now available in **General Availability**.

## June 14, 2021

Issue

Enabling or disabling [PROXY protocol](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#proxy-protocol) after a Private Service Connect service attachment is created does not change the configuration. However, the status shown in the service attachment details incorrectly shows that the status has changed. To enable or disable PROXY protocol, delete the service attachment and recreate it with the correct PROXY protocol configuration.

## June 09, 2021

Fixed

If you enable PROXY protocol for a Private Service Connect service attachment, the [PROXY protocol header value](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#proxy-protocol) was previously either `0xEA` or `0xE0`. Starting today, the value will always be `0xE0`.

## June 04, 2021

Fixed

When a Private Service Connect [consumer endpoint is deleted](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#delete-endpoint), the [service attachment details](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#attachment-details) now correctly reflects this change.

Fixed

The Private Service Connect Published Services tab in the Google Cloud Console now correctly displays service attachments. You can now [view](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#list-services) and [manage](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#access) service attachments using the Console, the gcloud command-line tool, or the API

## June 02, 2021

Feature

[Publishing services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) and [accessing published services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) is now available in **Preview**.

Issue

Private Service Connect [service attachment details](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#attachment-details) always show a status of **Accepted** for consumer endpoints, even if they have a different status. The status is correctly displayed in the [consumer endpoint details](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#endpoint-details).

Issue

When a Private Service Connect [consumer endpoint is deleted](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#delete-endpoint), the [service attachment details](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#attachment-details) do not reflect this change.

Issue

If you enable PROXY protocol for a Private Service Connect service attachment, the [PROXY protocol header value](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#proxy-protocol) might be `0xEA` or `0xE0`. After General Availability, the value will always be `0xE0`.

Issue

If you want to create a [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) in a Shared VPC network, the endpoint must be created in the same project that contains the virtual machines (VMs) that send requests to the endpoint.

Issue

The Private Service Connect Published Services tab in the Google Cloud Console does not display service attachments. Use the gcloud command-line tool or the API to [view](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#list-services) and [manage](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#access) service attachments.

Issue

Updating a Private Service Connect service attachment using the `PATCH` API method requires that you provide all values in the request body, not just the values that you are updating. This affects [Managing access requests for a service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#access) and [Changing the connection preference for a service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#connection-pref).

Issue

If you publish a service using Private Service Connect, and the referenced load balancer does not have any backend VMs, all Private Service Connect endpoints in the consumer network might become unresponsive. Make sure that that all load balancers that are referenced by a service attachment have backend VMs.

## May 07, 2021

Feature

[GRE support](https://docs.cloud.google.com/vpc/docs/vpc#specifications) for VPC networks is now available in **General Availability**.

## April 14, 2021

Feature

Access to Google APIs and services using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) is now available in **General Availability**.

Issue

Using non-RFC 1918 addresses for [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) endpoints results in unexpected costs due to a billing issue. To prevent this issue, avoid using non-RFC 1918 IP addresses and instead use RFC 1918 IP addresses for Private Service Connect endpoints. If you are affected by this issue, contact your account team for remediation.

## March 24, 2021

Feature

For auto mode VPC networks, added a new subnet `10.186.0.0/20` for the Warsaw `europe-central2` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/vpc#ip-ranges).

Feature

The ability to connect [VM interfaces other than nic0](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#multiple-network-interfaces-in-shared-vpc) to a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) is now available in **General Availability** for instance templates and managed instance groups. This feature is available in the `gcloud` command-line tool and the API.

## March 18, 2021

Feature

[Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access) support for [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) is now available in **General availability**.

## February 26, 2021

Feature

[Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) are now available in **General Availability**.

## February 23, 2021

Feature

The ability to connect [VM interfaces other than nic0](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#multiple-network-interfaces-in-shared-vpc) to a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) is now available in **General Availability**. This feature presently only GA for individual VM instances. Support for instance templates and managed instance groups is still **Preview**.

## January 11, 2021

Feature

Support for [1500 MTU for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#interconnect-mtu) is now available in **General Availability.**

## December 16, 2020

Feature

[DNS peering for private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#dns-peering) is now available in **General Availability**.

Feature

Access to Google APIs and services using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) is now available in **Preview**.

## December 15, 2020

Feature

The ability to connect [VM interfaces other than nic0](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#multiple-network-interfaces-in-shared-vpc) to a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) is now available in **Preview**. This feature presently only works with individual VM instances, not with instance templates or managed instance groups.

## December 07, 2020

Feature

[Packet Mirroring direction control](https://docs.cloud.google.com/vpc/docs/packet-mirroring#filtering) is now available in **General Availability**.

Feature

[DNS peering for private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#dns-peering) is now available in **Preview**.

## October 15, 2020

Feature

Support for [1500 MTU in VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#mtu) is now available in **General Availability.**

## September 02, 2020

Feature

[Firewall Rules Logging metadata controls](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging#log-format) is now available in **General Availability**.

## August 13, 2020

Feature

[GRE support](https://docs.cloud.google.com/vpc/docs/vpc#specifications) for VPC networks is now available in **Beta**.

## July 23, 2020

Feature

[Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access) support for [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) is now available in **Beta**.

## June 12, 2020

Feature

[Firewall Rules Logging metadata controls](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging#log-format) is now available in **Beta**.

## June 08, 2020

Feature

For auto mode VPC networks, added a new subnet `10.184.0.0/20` for the Jakarta `asia-southeast2` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/vpc#ip-ranges).

## June 03, 2020

Feature

[Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) are now available in **Beta**.

## May 29, 2020

Feature

GKE annotations and advanced controls for [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) is now available in **General Availability**.

## May 18, 2020

Feature

Subnets in VPC networks now support IP addresses other than RFC 1918 addresses. For more information, see [Subnet ranges](https://docs.cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges).

## April 29, 2020

Change

Google Cloud now encrypts VPC traffic within the boundaries of the data centers in _asia-east2_. We will roll out this feature gradually to other regions. Google Cloud already encrypts VPC traffic _between all data centers_ as described in [Encryption in Transit in Google Cloud](https://docs.cloud.google.com/security/encryption-in-transit#virtual-network).

## April 24, 2020

Feature

[Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/private-access-options#pga-onprem) permits on-premises hosts to send traffic from any internal IP addresses, not just RFC 1918 addresses. This feature is now **Generally Available**.

## April 20, 2020

Feature

For auto mode VPC networks, added a new subnet `10.182.0.0/20` for the Las Vegas `us-west4` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/vpc#ip-ranges).

Change

[Packet Mirroring pricing](https://docs.cloud.google.com/vpc/network-pricing#packet-mirroring) will come into effect from June 20, 2020. There is no charge for Packet Mirroring until that time.

## March 03, 2020

Feature

[Packet MIrroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) is now available in **General Availability**.

## February 24, 2020

Feature

For auto mode VPC networks, added a new subnet `10.180.0.0/20` for the Salt Lake City `us-west3` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/vpc#ip-ranges).

## January 24, 2020

Change

For auto mode VPC networks, added a new subnet `10.178.0.0/20` for the Seoul `asia-northeast3` region. For more information, see [Auto mode IP ranges](https://docs.cloud.google.com/vpc/docs/vpc#ip-ranges).

## January 01, 2020

Change

Google now charges for static external IPv4 addresses that are in use, except for ones that are used by forwarding rules. For more information, see the [Network pricing](https://docs.cloud.google.com/vpc/network-pricing#ipaddress).

## December 19, 2019

Feature

[Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/private-access-options#pga-onprem) now permits on-premises hosts to send traffic from any internal IP addresses, not just RFC 1918 addresses. This feature is now available in **Beta**.

## December 11, 2019

Feature

[Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access) is now **Generally Available**.

## November 22, 2019

Feature

Virtual machines with 2 or 4 vCPUs now have a maximum egress rate of 10 Gbps. This feature is Generally Available. For more information, see [Machine types](http://cloud.google.com/compute/docs/machine-types) in the Compute Engine documentation.

## November 18, 2019

Feature

The `private.googleapis.com` virtual IP address range for [Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/private-access-options) is **Generally Available**.

## November 13, 2019

Feature

For VPC Network Peering, [importing and exporting custom routes](https://docs.cloud.google.com/vpc/docs/vpc-peering) are now **General Available**.

Feature

[Packet MIrroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) is now available in **Beta**.

## September 23, 2019

Change

The [quotas](https://docs.cloud.google.com/vpc/docs/quota) for subnet ranges per network and per peering group have changed.

## September 20, 2019

Feature

[VPC Flow Logs log volume reduction](https://docs.cloud.google.com/vpc/docs/using-flow-logs#log-sampling) is now available in **General Availability**.

## August 13, 2019

Feature

The `private.googleapis.com` virtual IP address range for [Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/private-access-options) is in **Beta**.

## June 19, 2019

Feature

The increased egress rate of [32Gbps of network I/O](https://docs.cloud.google.com/vpc/docs/quota#per_instance) for virtual machines that use either the Skylake CPU platform or ultramem machine types, is now available in **General Availability**.

## April 09, 2019

Feature

[Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access) is now available in **Beta**.

## April 05, 2019

Feature

You can get up to [32Gbps of network I/O](https://docs.cloud.google.com/vpc/docs/quota#per_instance) for virtual machines that use either the Skylake CPU platform or ultramem machine types. This increased egress rate is now available in **Beta**.

## April 04, 2019

Feature

[VPC Flow Logs log volume reduction](https://docs.cloud.google.com/vpc/docs/using-flow-logs#log-sampling) is now available in **Beta**.

## April 01, 2019

Feature

For VPC Network Peering, [importing and exporting custom routes](https://docs.cloud.google.com/vpc/docs/vpc-peering) is now available in **Beta**.

## March 27, 2019

Feature

[Private services access](https://docs.cloud.google.com/vpc/docs/private-access-options) is now available in **General Availability**.

## February 07, 2019

Change

You can disable the [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network) creation for new projects. You must [create an organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) and add the `compute.skipDefaultNetworkCreation` constraint.

## February 01, 2019

Feature

The [private access option](https://docs.cloud.google.com/vpc/docs/private-access-options) for on-premises hosts is now **Generally Available**. On-premises hosts with only private IP addresses can access Google APIs through a Cloud VPN or Cloud Interconnect connections (hybrid connectivity scenarios).

## January 24, 2019

Deprecated

The [IPv4Range](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks) field for creating [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy) is now deprecated and will shut down on **June 1, 2021**.

## January 09, 2019

Feature

[Firewall rules logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging) is now available in **General Availability**.

## December 20, 2018

Feature

IP address allocation for [private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#allocating-range) is now available in **General Availability**.

## October 19, 2018

Feature

[Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/private-access-options) is now available in **Beta**. On-premises hosts with only private IP addresses can now access Google APIs through Cloud VPN or Cloud Interconnect connections (hybrid connectivity scenarios).

## September 26, 2018

Feature

[Private services access](https://docs.cloud.google.com/vpc/docs/private-access-options) provides a private connection between your VPC network and a network owned by Google or a third party. Private services access is in **Beta**.

## September 18, 2018

Feature

[Firewall rules logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging) is now available in **Beta**.

## September 05, 2018

Feature

The ability to [Disable firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#enforcement) is now available in **General Availability**.

## July 31, 2018

Feature

In Shared VPC service projects, [listing usable](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#discovering_subnets_that_can_be_used) subnets in the host project is now available in **General Availability**.

## June 28, 2018

Feature

[VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) are now available in **General Availability**.

## May 09, 2018

Feature

[Folder support for Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_in_shared_vpc) is now available in **Beta**.

## May 01, 2018

Feature

The ability to [Disable firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#enforcement) is now available in **Beta**.

## April 23, 2018

Feature

[Add/Delete Alias IP Ranges](https://docs.cloud.google.com/vpc/docs/alias-ip) is now available in **General Availability**.

## March 29, 2018

Feature

[VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) are now available in **Beta**.

## November 13, 2017

Change

VPC Networks documentation has moved to [https://cloud.google.com/vpc/docs](https://docs.cloud.google.com/vpc/docs).

## September 05, 2017

Feature

[Alias IP Ranges](https://docs.cloud.google.com/vpc/docs/alias-ip) allows you to assign additional IP addresses to a VM instance. These addresses can be used by containers running on the VM. Alias IP Ranges is now available in **General Availability**.

Feature

[Firewall Rules egress and deny rules](https://docs.cloud.google.com/vpc/docs/firewalls) allows you to create firewall rules that govern egress as well as ingress traffic. You can now also create deny rules and you can prioritize the order in which rules are evaluated. Firewall Rules egress and deny rules is now available in **General Availability**.

## August 18, 2017

Feature

[Multiple Network Interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts) allows a VM instance to have more than one virtual network interfaces. Each interface must point to a different VPC network. Multiple Network Interfaces is now available in **General Availability**.

## August 11, 2017

Feature

Add support for specifying a static internal IP to **Beta**. See [Reserving a Static Internal IP Address](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address) for more information.

## July 14, 2017

Feature

[VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) allows you to peer VPC networks, even networks in different organizations, so that the networks can communicate with each other using internal IP addresses. VPC Network Peering is now available in **General Availability**.

## June 21, 2017

Feature

[Multiple Network Interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts) allows a VM instance to have more than one virtual network interface. Each interface must point to a different VPC network. Multiple Network Interfaces is now available in **Beta**.

## June 07, 2017

Feature

[Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) (Previously Cross-Project Networking (XPN)) is now available in **General Availability**.

## May 22, 2017

Feature

[Alias IP Ranges](https://docs.cloud.google.com/vpc/docs/alias-ip) allows you to assign additional IP addresses to a VM instance. These addresses can be used by containers running on the VM. Alias IP Ranges is now available in **Beta**.

## May 08, 2017

Feature

[VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) allows you to peer VPC networks, even networks in different organizations, so that the networks can communicate with each other using internal IP addresses. VPC Network Peering is now available in **Beta**.

## May 04, 2017

Feature

[Private Google Access](https://docs.cloud.google.com/vpc/docs/private-access-options) allows Compute Engine VM instances to access Google APIs using an internal IP address only. Private Google Access is now available in **General Availability**.

## May 01, 2017

Change

Decoupled labels and tags so that creating either a label or a tag will not create the opposing resource. For example, creating a label will no longer create a tag and vice-versa. For more information, read [Relationship between instance labels and network tags](https://docs.cloud.google.com/compute/docs/labeling-resources#labels_tags).

Change

You can now find information about network tags in the [VPC networking](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) documentation.

## April 17, 2017

Feature

[Firewall Rules egress and deny rules](https://docs.cloud.google.com/vpc/docs/firewalls) allows you to create firewall rules that govern egress as well as ingress traffic. You can now also create deny rules and you can prioritize the order in which rules are evaluated. Firewall Rules egress and deny rules is now available in **Beta**.

## March 09, 2017

Feature

[Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) allows you to share a VPC network with other GCP projects. Shared VPC is now available in **Beta**.

## March 07, 2017

Feature

[Private Google Access](https://docs.cloud.google.com/vpc/docs/private-access-options) allows Compute Engine VM instances to access Google APIs using an internal IP address only. Private Google Access is now available in **Beta**.

## December 21, 2016

Feature

Added ICMP support for [forwarding rules](https://docs.cloud.google.com/vpc/docs/forwarding-rules).

## May 11, 2016

Feature

The following VPC IAM roles are now generally available: `roles/compute.networkAdmin`, `roles/compute.securityAdmin`, `roles/iam.serviceAccountActor`

For more information, read the [IAM](https://docs.cloud.google.com/compute/docs/access/iam) documentation.

## November 04, 2014

Change

Lowered network pricing. See [Network pricing](https://docs.cloud.google.com/vpc/network-pricing) for more information.

## May 05, 2014

Change

Updated default firewall rule names. Default firewall rules are automatically created with every project. These rules were previously named `default-internal` and `default-ssh`. New projects will have the same default firewalls but with the following new names:

  * `default-allow-internal` \- Allows network connections of any protocol and port between any two instances.
  * `default-allow-ssh` \- Allows TCP connections from any source to any instance on the network, over port 22.



Change

Introduced new default firewall rule that will be created with each new project.

  * `default-allow-icmp` \- Allows ICMP traffic from any source to any instance on the network.



## December 17, 2013

Feature

Released new Protocol Forwarding feature. [Forwarding rules](https://docs.cloud.google.com/vpc/docs/forwarding-rules) allows you to forward traffic to a single virtual machine instance, using a target.instance. Protocol forwarding provides support for these additional features:

  * `AH`: [IP Authentication Header](http://tools.ietf.org/html/rfc4302.html) protocol
  * `ESP`: [IP Encapsulating Security Payload](http://www.ietf.org/rfc/rfc2406.txt) protocol
  * `SCTP`: [Stream Control Transmission](http://www.ietf.org/rfc/rfc2960.txt) protocol



Feature

Added support for new [Target Instance resources](https://docs.cloud.google.com/load-balancing/docs/forwarding-rules), which allows for non-NAT'ed traffic to be forwarded to a single virtual machine instance. See [Forwarding rules](https://docs.cloud.google.com/vpc/docs/forwarding-rules) for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
