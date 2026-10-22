---
url: https://docs.cloud.google.com/compute/docs/ip-addresses/
title: IP addresses \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:45.553725+00:00
---

# IP addresses  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/ip-addresses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

Many Google Cloud resources can have internal IP addresses and external IP addresses. For example, you can assign an internal and external IP address to Compute Engine instances. The instances use these addresses to communicate with other Google Cloud resources and external systems.

Each network interface of an instance can have the following IP addresses assigned according to its stack type:

Interface stack type | IP addresses  
---|---  
IPv4-only | 

  * An internal IPv4 address (required)
  * An [alias IPv4 range](https://docs.cloud.google.com/vpc/docs/alias-ip) (optional)
  * An external IPv4 address (optional)

  
Dual-stack (IPv4 and IPv6) | 

  * An internal IPv4 address (required)
  * An alias IPv4 range (optional)
  * An external IPv4 address (optional)
  * A `/96` IPv6 address range, either internal or external, but not both (required)

  
IPv6-only | 

  * A `/96` IPv6 address range, either internal or external, but not both (required)

  
  
An instance can communicate with instances on the same Virtual Private Cloud (VPC) network by using the instance's internal IPv4 address, internal IPv6 address, or external IPv6 address. As a best practice, use internal IPv6 addresses for internal communication.

To communicate with the internet, you can use an external IP address configured on the instance. If no external IP address is configured on the instance, Cloud NAT can be used for IPv4 traffic.

Similarly, you must use the instance's external IP address to connect to instances outside of the same VPC network. However, if the networks are connected in some way, such as by using [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), you can use the instance's internal IP address.

For information about identifying the internal and external IP address for your instances, see [View the network configuration for an instance](https://docs.cloud.google.com/compute/docs/instances/view-network-properties).

## Internal IP addresses

The network interfaces for an instance are assigned IP addresses from the subnet that they are connected to. Network interfaces with IPv4 addresses have one primary internal IPv4 address, which is assigned from the subnet's primary IPv4 range. Network interfaces with internal IPv6 addresses have one `/96` IPv6 address range, which is assigned from the subnet's internal `/64` IPv6 range.

Internal IPv4 addresses can be assigned in the following ways:

  * Compute Engine automatically assigns a single IPv4 address from the primary [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges).
  * You assign a specific internal IPv4 address when you create a compute instance, either by using a reserved static internal IPv4 address or by specifying a custom ephemeral internal IPv4 address.



Internal IPv6 addresses can be assigned to instances that are connected to a subnet that has an internal IPv6 range in the following ways:

  * When you [configure an internal IPv6 address on an instance's vNIC](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address), Compute Engine automatically assigns a single `/96` range of IPv6 addresses from the [subnet's internal IPv6 range](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).
  * You assign a specific internal IPv6 address when you create an instance, either by using a reserved static internal IPv6 address or by specifying a custom ephemeral internal IPv6 address.



You can also [reserve a static internal address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip) from the subnet's IPv4 or IPv6 range and later assign it to an instance.

Compute instances can also have [alias IP addresses and ranges](https://docs.cloud.google.com/compute/docs/alias-ip). If you have more than one service running on an instance, you can assign each service its own unique IP address.

## Internal DNS names

Google Cloud automatically resolves the fully qualified DNS name (FQDN) of an instance to the internal IP addresses of the instance. Internal DNS names work only within the instance's VPC network.

For more information about fully qualified domain names (FQDN), see [Internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names).

## External IP addresses

If you need to communicate with the internet or with resources in another VPC network, you can assign an external IPv4 or IPv6 address to an instance. If [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) or [hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) allow the connection, sources from outside a VPC network can reach a specific resource using its external IP address. Only resources with an external IP address can directly communicate with resources outside of the VPC network. Communicating with a resource using an external IP address can cause [additional billed charges](https://cloud.google.com/vpc/network-pricing#externaliptraffic).

External IPv4 addresses can be assigned in the following ways:

  * Compute Engine automatically assigns an IPv4 address from Google's ranges of external IPv4 addresses.
  * You assign a specific external IPv4 address when you create an instance by using a reserved static external IPv4 address.

For more information, see [Where can I find Compute Engine IP ranges](https://docs.cloud.google.com/compute/docs/faq#find_ip_range).




External IPv6 addresses can be assigned to instances that are connected to a subnet that has an external IPv6 range in the following ways:

  * When you [configure an external IPv6 address on an instance's vNIC](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address), Compute Engine automatically assigns a single `/96` range of IPv6 addresses from the [subnet's external IPv6 range](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).
  * You assign a specific external IPv6 address when you create an instance, either by using a [reserved static external IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static) or by specifying a custom ephemeral external IPv6 address.



### Alternatives to using an external IP address

Internal, or private, IP addresses provide a number of advantages over external, or public, IP addresses, including:

  * **Reduced attack surface**. Removing external IP addresses from compute instances makes it more difficult for attackers to reach the instances and exploit potential vulnerabilities.
  * **Increased flexibility**. Introducing a layer of abstraction, such as a load balancer or a NAT service, allows more reliable and flexible service delivery when compared with static, external IP addresses.



The following table summarizes the ways that compute instances can access or be accessed from the internet when they don't have an external IP address.

Access method | Solution | Best used when  
---|---|---  
Interactive | [Configure TCP forwarding for Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview) | You want to use administrative services like SSH and RDP to connect to your backend instances, but the requests must pass authentication and authorization checks before they get to their target resource.  
Fetching | [Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/gce-example) | You want your Compute Engine instances that don't have external IP addresses to connect to the internet (outbound), but hosts outside of your VPC network can't initiate their own connections to your compute instances (inbound). You might use this approach for OS updates or external APIs.  
[Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop) | You need to isolate your Compute Engine instances from the Internet by creating new TCP connections on their behalf, while adhering to the administered security policy.  
Serving | [Create an external load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer) | You want clients to connect to resources without external IP addresses anywhere in Google Cloud while protecting your compute instances from DDoS attacks and direct attacks.  
  
## Regional and global IP addresses

When you list or describe IP addresses in your project, Google Cloud labels addresses as global or regional, which indicates how a particular address is being used. When you associate an address with a regional resource, such as an instance, Google Cloud labels the address as regional. Regions are Google Cloud [regions](https://docs.cloud.google.com/docs/geography-and-regions), such as `us-east4` or `europe-west2`.

Global IP addresses are used in the following configurations:

  * Global internal IP addresses: [Access Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis) or [private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access)
  * Global external IP addresses: [External proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/tcp) and [External Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https) using a [Premium tier network](https://docs.cloud.google.com/network-tiers/docs/overview#premium_tier)



For instructions on how to create a global IP address, see [Reserve a new static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static).

## Overview of the SLA for Compute Engine networking

Compute Engine has a [Service Level Agreement (SLA)](https://cloud.google.com/compute/sla), which defines service level objectives (SLOs) for the monthly uptime percentage for network service tiers.

When you create a Compute Engine instance, by default you get an internal IP address. You can additionally configure an external IP address with either Premium Tier (default) or Standard Tier networking. Which network service tier you choose depends on your cost and quality of service requirements. Each network service tier has a different SLO.

When you create the compute instance, you can configure multiple NICs attached to the instance, and each NIC can have a different network configuration, as shown in the following diagram:

![An instance with three NICs, each of which handles different
network traffic with different network service tiers.](https://docs.cloud.google.com/static/compute/images/networking/network-sla-diagram.svg)

**Figure 1.** An instance with three NICs, each of which handles different network traffic with different network service tiers.

In the preceding diagram, the example instance named **VM appliance** has three NICs, which are configured as follows:

  * `nic0` is configured with an internal IP subnet.
  * `nic1` is configured with an external IP subnet and uses the Standard networking tier.
  * `nic2` is configured with an external IP subnet and uses the Premium networking tier.



In this example, the VM instance is not a memory-optimized VM. Depending on which NIC suffers a connectivity loss, different SLOs are applicable. The following list describes the SLA for the different NICs in this example.

  * `nic0`: A single-instance VM with internal IP addresses. The monthly uptime percentage is 99.9%.
  * `nic1`: A single-instance VM with an external IP address that uses the Standard networking tier. This VM isn't protected by any SLA. Only multiple instances across zones are protected at 99.9% with the Standard networking tier.
  * `nic2`: A single-instance VM with external IP address that uses the Premium networking tier. The monthly uptime percentage is 99.9%. For multiple instances across zones, the monthly uptime percentage is 99.99% with the Premium networking tier. 



## What's next

  * [View the network configuration for an instance](https://docs.cloud.google.com/compute/docs/instances/view-network-properties).
  * [Reserve a new static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static).
  * [Assigning a static external IP to a new instance](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#IP_assign).
  * [Choosing an internal IP address at instance creation](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address#assign_new_instance).
  * [Promoting an ephemeral external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#promote_ephemeral_ip).
  * [Learn how to use internal DNS names](https://docs.cloud.google.com/compute/docs/networking/using-internal-dns#access_by_internal_DNS) to address instances over the internal VPC network.
  * [Learn more about IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses).
  * [Learn more about IPv6](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).
  * [Learn more about IP addresses and load balancing](https://docs.cloud.google.com/load-balancing/docs/features#ip_addresses).
  * [Review external IP address pricing](https://cloud.google.com/vpc/network-pricing#ipaddress).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
