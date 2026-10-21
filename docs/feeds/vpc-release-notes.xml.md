---
url: https://docs.cloud.google.com/feeds/vpc-release-notes.xml
title: Virtual Private Cloud - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:21.586421+00:00
---

# Virtual Private Cloud - Release notes

> Source: https://docs.cloud.google.com/feeds/vpc-release-notes.xml

tag:google.com,2016:vpc-release-notesVirtual Private Cloud - Release notesGoogle Cloud Platform2026-10-07T00:00:00-07:00October 07, 2026tag:google.com,2016:vpc-release-notes#October_07_20262026-10-07T00:00:00-07:00Feature 

**General Availability** : VPC Flow Logs supports [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging) for VM instances and serverless endpoints. Connection logging captures outbound TCP connection attempts and acknowledged inbound TCP connections.

You can enable this feature in a VPC Flow Logs configuration for a [subnet](https://docs.cloud.google.com/vpc/docs/using-flow-logs#network-management) (through the Network Management API), a [VPC network](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-network), or an [organization](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-organization).

### Feature

Service producers can let service consumers establish more connections to a Private Service Connect endpoint or backend by [configuring the target published service (service attachment) to use an additional NAT IP address](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#update-nat-ips-per-endpoint). For more information, see [Maximum connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections).

]]> October 05, 2026tag:google.com,2016:vpc-release-notes#October_05_20262026-10-05T00:00:00-07:00Feature 

**Preview** : External IPv6 addresses are now supported for [Standard Tier](https://docs.cloud.google.com/network-tiers/docs/overview#standard_tier). For more information, see [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

]]> September 16, 2026tag:google.com,2016:vpc-release-notes#September_16_20262026-09-16T00:00:00-07:00Feature 

**General Availability** : You can add Dynamic NICs to the same VPC network used by other network interfaces of a Compute Engine instance. For more information, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#specifications).

### Feature

**General Availability** : VPC Flow Logs supports logging for App Engine resources that are configured with [Direct VPC egress](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc). For more information, see [Serverless flows](https://docs.cloud.google.com/vpc/docs/about-traffic-flows#serverless-flows) and [ServerlessDetails field format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#serverless-details).

### Feature

**General Availability** : VPC Flow Logs adds the following metadata annotations for Private Service Connect:

  * `src_psc_interface` and `dest_psc_interface`
  * `psc.consumer_connection`
  * `psc.psc_endpoint.name`
  * `psc.psc_attachment.name`



For more information, see [Record format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#record_format).

]]> September 10, 2026tag:google.com,2016:vpc-release-notes#September_10_20262026-09-10T00:00:00-07:00Feature 

**Preview** : [Propagated connections](https://docs.cloud.google.com/vpc/docs/about-propagated-connections) support Private Service Connect [endpoints that access global Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints). With propagated connections, endpoints that access global Google APIs in one consumer VPC spoke can be privately accessed by other consumer VPC spokes that are connected to the same Network Connectivity Center hub.

]]> August 31, 2026tag:google.com,2016:vpc-release-notes#August_31_20262026-08-31T00:00:00-07:00Feature 

**General Availability** : You can create Compute Engine instances that have multiple virtual network interfaces (vNICs) in the same VPC network. For more information, see [Multiple network interfaces in the same VPC network](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#same-vpc).

]]> August 27, 2026tag:google.com,2016:vpc-release-notes#August_27_20262026-08-27T00:00:00-07:00Feature 

**General Availability** : VPC Flow Logs generates log records for dropped traffic. For more information, see [Records for dropped traffic](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#packet-drops).

### Feature

**General Availability** : You can reserve static external IPv6 addresses from bring your own IP addresses (BYOIP) sub-prefixes that are in `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode.

You can assign these addresses to forwarding rules for external passthrough Network Load Balancers and external protocol forwarding. You can also promote ephemeral IPv6 BYOIP addresses that are used by external forwarding rules to reserved static IP addresses.

For more information, see [Create external forwarding rules](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#create-subprefix-use).

]]> August 19, 2026tag:google.com,2016:vpc-release-notes#August_19_20262026-08-19T00:00:00-07:00Feature 

**General Availability** : You can use Private Service Connect [endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints) and [backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#multiregional-google-apis) to access multi-regional service endpoints such as `storage.us.rep.googleapis.com`.

]]> August 03, 2026tag:google.com,2016:vpc-release-notes#August_03_20262026-08-03T00:00:00-07:00Feature 

**Preview** : You can create v2 IPv4 public advertised prefixes for bring your own IP addresses (BYOIP) that use [Standard Tier](https://docs.cloud.google.com/network-tiers/docs/overview#standard_tier) IP addresses. For more information, see [Network Service Tiers](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#service-tiers).

]]> July 30, 2026tag:google.com,2016:vpc-release-notes#July_30_20262026-07-30T00:00:00-07:00Feature 

**General Availability** : You can use the **Resolve subnet mask** setting on a subnet to configure all attached Compute Engine instances with the same netmask as the subnet (instead of `/32`). Configuring larger instance netmasks lets compute instances discover the MAC addresses of other machines within the same subnet and directly communicate with them by using destination MAC addresses.

For more information, see [Compute instance netmasks](https://docs.cloud.google.com/vpc/docs/compute-instance-netmasks).

]]> July 21, 2026tag:google.com,2016:vpc-release-notes#July_21_20262026-07-21T00:00:00-07:00Feature 

For Google Cloud resources that are registered as [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) workloads or services, VPC Flow Logs records contain application-specific labels. For more information, see [App Hub labels](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#app-hub).

]]> July 20, 2026tag:google.com,2016:vpc-release-notes#July_20_20262026-07-20T00:00:00-07:00Feature 

**Preview** : You can reserve static external IPv6 addresses from bring your own IP addresses (BYOIP) sub-prefixes that are in `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode.

You can assign these addresses to forwarding rules for external passthrough Network Load Balancers and external protocol forwarding. You can also promote ephemeral IPv6 BYOIP addresses that are used by external forwarding rules to reserved static IP addresses.

For more information, see [Create external forwarding rules](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#create-subprefix-use).

]]> June 30, 2026tag:google.com,2016:vpc-release-notes#June_30_20262026-06-30T00:00:00-07:00Feature 

**General Availability** : If a consumer VPC network uses an [RDMA network profile for Falcon VPC networks](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles#falcon-supported-features), a single Compute Engine instance can connect to it by using multiple virtual Private Service Connect interfaces.

For more information, see [Create VMs with Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/create-manage-private-service-connect-interfaces#create).

]]> June 24, 2026tag:google.com,2016:vpc-release-notes#June_24_20262026-06-24T00:00:00-07:00Feature 

**General Availability** : You can cancel pending deletion requests for VPC Network Peering connections that are in consensus mode. For more information, see [Cancel a deletion request](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#cancel-delete).

]]> June 23, 2026tag:google.com,2016:vpc-release-notes#June_23_20262026-06-23T00:00:00-07:00Feature 

**General Availability** : Service consumers can authorize Private Service Connect interfaces to connect to network attachments by adding service class IDs to a network attachment's accept list.

For more information, see [Authorization policies](https://docs.cloud.google.com/vpc/docs/about-network-attachments#connection-policies).

]]> June 22, 2026tag:google.com,2016:vpc-release-notes#June_22_20262026-06-22T00:00:00-07:00Feature 

**Preview** : RoCE VPC networks for VM instances support assigning alias IP ranges to `MRDMA` vNICs. For more information about these features, see the following:

  * [RDMA network profiles](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles)
  * [Alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip)

]]> June 01, 2026tag:google.com,2016:vpc-release-notes#June_01_20262026-06-01T00:00:00-07:00Feature 

**General Availability** : [Composite Health for Private Service Connect](https://docs.cloud.google.com/vpc/docs/about-composite-health), formerly known as Private Service Connect health, lets service producers define health criteria for published services, enabling automatic cross-region failover for consumers that access the service by using Private Service Connect backends.

]]> May 19, 2026tag:google.com,2016:vpc-release-notes#May_19_20262026-05-19T00:00:00-07:00Feature 

You can cancel pending deletion requests for VPC Network Peering connections that are in consensus mode. This feature is available in **Preview**. For more information, see [Cancel a deletion request](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#cancel-delete).

]]> May 06, 2026tag:google.com,2016:vpc-release-notes#May_06_20262026-05-06T00:00:00-07:00Feature 

Organization Policy Service custom constraints are available in **General Availability** for private services access connections. For more information, see [Restrict private connections with organization policies](https://docs.cloud.google.com/vpc/docs/private-services-access#org-policies).

]]> April 10, 2026tag:google.com,2016:vpc-release-notes#April_10_20262026-04-10T00:00:00-07:00Feature 

Private Service Connect consumers can configure supported load balancers or regional Cloud Service Mesh to access published services through Private Service Connect endpoints. This feature is available in **Preview**.

For more information, see [Published service backends](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#published-service-backends).

]]> April 03, 2026tag:google.com,2016:vpc-release-notes#April_03_20262026-04-03T00:00:00-07:00Feature 

[Hybrid Subnets](https://docs.cloud.google.com/vpc/docs/hybrid-subnets) is available in **General Availability**. Hybrid subnet routing lets a VPC network share a CIDR block with a connected on-premises network. This configuration helps you migrate workloads to Google Cloud without needing to change any IP addresses. During migration, workloads that have migrated to your VPC network can communicate with those remaining in the on-premises network by using internal IP addresses. After all workloads have migrated, you can disable hybrid subnet routing to restore normal routing behavior.

For information about pricing for Hybrid Subnets, see [Virtual Private Cloud pricing](https://docs.cloud.google.com/vpc/pricing?e=0#hybrid-subnets).

]]> March 30, 2026tag:google.com,2016:vpc-release-notes#March_30_20262026-03-30T00:00:00-07:00Feature 

Service producers can [accept or reject connections from individual Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#accept-endpoint). This feature is available in **General Availability**.

]]> March 18, 2026tag:google.com,2016:vpc-release-notes#March_18_20262026-03-18T00:00:00-07:00Feature 

You can [update a service attachment's target service without recreating the service attachment](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#change-service). Consumer connections are preserved during the update, but traffic is briefly disrupted. This feature is available in **General Availability**.

For more information, including a list of supported configurations, see [Service mutability](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-mutability).

]]> February 26, 2026tag:google.com,2016:vpc-release-notes#February_26_20262026-02-26T00:00:00-08:00Feature 

You can create Compute Engine instances that have multiple network interfaces in the same VPC network. This feature is available in **Preview**. For more information, see [Multiple network interfaces in the same VPC network](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#same-vpc).

]]> February 23, 2026tag:google.com,2016:vpc-release-notes#February_23_20262026-02-23T00:00:00-08:00Feature 

You can create a VPC network that supports RDMA over [Falcon transport](https://cloud.google.com/blog/topics/systems/introducing-falcon-a-reliable-low-latency-hardware-transport), which lets you run AI and high performance computing (HPC) workloads on Compute Engine instances that have the `IRDMA` network interface type in Google Cloud, such as H4D instances. This feature is available in **General Availability**.

For more information, see [RDMA network profiles](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).

]]> February 10, 2026tag:google.com,2016:vpc-release-notes#February_10_20262026-02-10T00:00:00-08:00Feature 

You can use constraints in custom organization policies to provide more granular and customizable control over specific fields for internal ranges. For more information, see [Manage VPC resources by using custom organization policies](https://docs.cloud.google.com/vpc/docs/custom-constraints).

]]> February 09, 2026tag:google.com,2016:vpc-release-notes#February_09_20262026-02-09T00:00:00-08:00Feature 

You can bring your own IPv6 global unicast addresses (GUAs) to assign to a [subnet's internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes). Although GUAs are typically public addresses, in this configuration they are used privately and function in the same way as Google Cloud-provisioned ULAs.

For more information, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

]]> February 04, 2026tag:google.com,2016:vpc-release-notes#February_04_20262026-02-04T00:00:00-08:00Feature 

You can create individual static external IPv4 addresses from bring your own IP addresses (BYOIP) prefixes. This feature is available in **General Availability** and only applies to IPv4 regional v2 prefixes that are created after December 13, 2025.

For more information, see [Enhanced IP address allocation](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#enhanced-allocation).

]]> January 20, 2026tag:google.com,2016:vpc-release-notes#January_20_20262026-01-20T00:00:00-08:00Feature 

For auto mode VPC networks, added a new subnet `10.232.0.0/20` for the Bangkok `asia-southeast3` region. For more information, see [Global locations](https://cloud.google.com/about/locations) and [Auto mode IP ranges](https://cloud.google.com/vpc/docs/subnets#ip-ranges).

]]> November 14, 2025tag:google.com,2016:vpc-release-notes#November_14_20252025-11-14T00:00:00-08:00Feature 

Dynamic Private Service Connect interfaces are available in **General Availability**. Private Service Connect interfaces let service producers initiate connections to service consumers. You can update a VM instance to add or remove dynamic Private Service Connect interfaces without needing to restart or recreate the instance.

For more information, see [Private Service Connect interface types](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#types).

]]> November 10, 2025tag:google.com,2016:vpc-release-notes#November_10_20252025-11-10T00:00:00-08:00Feature 

Service producers can [accept or reject connections from individual Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#accept-endpoint). This feature is available in **Preview**.

]]>
