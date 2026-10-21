---
url: https://docs.cloud.google.com/vpc/docs/ip-addresses/
title: IP addresses \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:10.366301+00:00
---

# IP addresses  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/ip-addresses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IP addresses

Resources such as VM instances and load balancers have IP addresses in Google Cloud. These IP addresses let Google Cloud resources communicate with other resources in Google Cloud, in on-premises networks, or on the public internet. This page describes the IP address categorization used by Google Cloud.

Google Cloud uses the following labels to describe different IP address types. For example, an _internal_ IP address is not publicly routed. An _external_ IP address is a publicly routed IP address. You can assign an external IP address to the network interface of a Google Cloud VM.

External IP address
    

External IP addresses are publicly advertised, meaning they are reachable by any host on the internet. External IP addresses must be [publicly routable IP addresses](https://wikipedia.org/wiki/IP_address#Public_address). Resources with external IP addresses can communicate with the public internet.

External IPv4 addresses for resources can be provided by Google Cloud, or you can [bring your own IP (BYOIP)](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) addresses to Google Cloud. Although BYOIP addresses are static external IPv4 addresses and can be used with most resources that support static external IPv4 addresses, there are some [exceptions](https://docs.cloud.google.com/vpc/docs/using-bring-your-own-ip#support).

External IPv6 addresses can be provided by Google Cloud, or you can BYOIP addresses to Google Cloud. IPv6 BYOIP addresses can only be used by forwarding rules for regional external passthrough Network Load Balancers or subnets that can only host VMs. For more information, see [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

For a list of external IPv4 and IPv6 address ranges that can be provided by Google Cloud, see [Google Cloud external IP ranges](https://www.gstatic.com/ipranges/cloud.json). 

Internal IP address
    

Internal IP addresses cannot be reached from the internet and are not publicly routable.

    

Internal IP addresses are local to a VPC network, a VPC network connected by using VPC Network Peering, or an on-premises network connected to a VPC network by using Cloud VPN, Cloud Interconnect, or a Router appliance. Resources with internal IP addresses communicate with other resources as if they're all on the same private network.

Internal IPv4 addresses can be private IPv4 addresses, or they can be privately used public IPv4 addresses. For a list of valid internal IPv4 addresses, see [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).

Internal IPv6 addresses are unique within Google Cloud. For more information, see [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

For details about how internal IP addresses are advertised when you connect your VPC network to another network, see [Route advertisements and internal IP addresses](https://docs.cloud.google.com/vpc/docs/vpc#route-adverts-internal-ip).

Private IP address
    

Private IP addresses are addresses that [cannot be routed on the internet](https://wikipedia.org/wiki/IP_address#Private_addresses).

In Google Cloud, private IP addresses can only be used as internal IP addresses within a VPC network or an on-premises network connected to a VPC network.

For a list of private IPv4 ranges, see the entries for **Private IP address ranges** in the [valid internal IPv4 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) table.

[Unique local addresses (ULAs)](https://datatracker.ietf.org/doc/html/rfc4193) are private IPv6 addresses. ULAs are used for internal [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

Public IP address
    

Public IP addresses are internet routable. In Google Cloud, external IPv4 and IPv6 addresses are always public IP addresses.

You can also use public IPv4 addresses as internal addresses when you configure the primary or secondary IPv4 address range of a subnet in your VPC network. These addresses are referred to as [privately used public IP addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).

## Regional and global IP addresses

When you list or describe IP addresses in your project, Google Cloud labels addresses as global or regional, which indicates how a particular address is being used. When you associate an address with a regional resource, such as a VM, Google Cloud labels the address as regional. Regions are Google Cloud regions, such as `us-east4` or `europe-west2`. 

For more information about global and regional resources, see [Global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources) in the Compute Engine documentation.

### Summary of IP address types

The following tables describes examples of different regional and global IP addresses.

#### Internal IP addresses

Internal IP addresses are always Premium Tier.

Classification | Definition and Tier | Purpose  
---|---|---  
Regional internal IPv4 address | A [valid IPv4 range](https://docs.cloud.google.com/vpc/docs/subnets) used as a [subnet primary IPv4 range or subnet secondary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges) | Addresses from a subnet primary IPv4 or secondary IPv4 range can be used as described in [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges).  
Regional internal IPv6 address | An internal IPv6 range assigned to a [subnet IPv6 range](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) | Regional internal IPv6 addresses can be used as described in [Internal IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6).   
Global internal IPv4 addresses | Private Service Connect endpoints for Google APIs  
  
Allocated ranges for private services access | For more information, see [Access Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis) or [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access).  
  
#### External IP addresses

Some External IP addresses can be Standard Tier as well as Premium Tier.

Classification | Definition and Tier | Purpose  
---|---|---  
Regional external IPv4 address |  Each region has its own [ set of external IP addresses](https://www.gstatic.com/ipranges/cloud.json) for use by zonal or regional resources. Regional external IPv4 addresses can be provided by Google Cloud, or you can [bring your own IPv4 address ranges](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) to Google Cloud. | Premium Tier regional external IPv4 addresses can be used by:  


  * Compute Engine VM network interfaces (in a one-to-one NAT configuration)
  * External protocol forwarding
  * Regional external passthrough Network Load Balancers
  * External proxy Network Load Balancers and external Application Load Balancers

  
Standard Tier regional external IPv4 addresses can be used by:  


  * Compute Engine VM network interfaces (in a one-to-one NAT configuration)
  * External protocol forwarding
  * Regional external passthrough Network Load Balancers
  * External proxy Network Load Balancers and external Application Load Balancers

  
Regional external IPv4 addresses are also used by:  


  * External addresses for Cloud NAT
  * External addresses for Cloud VPN

  
Regional external IPv6 address  
  
Available in Premium Tier and Standard Tier ([Preview](https://cloud.google.com/products#product-launch-stages))  
| An external IPv6 range allocated to an [IPv6 subnet range](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) or [regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer). Regional external IPv6 addresses can be provided by Google Cloud, or you can bring your own IPv6 address ranges to Google Cloud. | Regional external IPv6 addresses can be used as described in [External IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#external-ipv6).   
Global external IPv4 addresses  
  
Exclusive to Premium tier | Internet accessible anycast external IPv4 addresses for global load balancing.  
  
Global external IPv4 addresses can be provided by Google Cloud, or you can bring your own IPv4 address ranges to Google Cloud. | Global external IPv4 addresses always use Premium Tier. They can be used by:  


  * External proxy Network Load Balancers
  * External Application Load Balancers
  * Global external passthrough Network Load Balancers

  
Global external IPv6 addresses  
  
Exclusive to Premium tier | Internet accessible anycast external IPv6 addresses for global load balancing. | Global external IPv6 addresses always use Premium Tier. They can be used by:  


  * External proxy Network Load Balancers
  * External Application Load Balancers
  * Global external passthrough Network Load Balancers

  
  
## Ephemeral and static IP addresses

Internal and external IP addresses can be ephemeral or static.

An ephemeral IP address is an IP address that doesn't persist beyond the life of the resource. In general, ephemeral IP addresses are released if you stop or delete the associated resource.

IP addresses can be assigned to resources, such as instances and forwarding rules, in the following ways:

  * If you don't specify an IP address, Google Cloud automatically assigns an ephemeral IP address.
  * You can specify an IP address by using a reserved static IP address.
  * For VM instances and forwarding rules, you can specify an IP address by using a custom ephemeral IP address. This method isn't supported for external IPv4 addresses or global IPv6 forwarding rules.



Reserving a static IP address assigns the address to your project until you explicitly release it. This is useful if you are dependent on a specific IP address for your service and need to prevent another resource from being able to use the address. Static addresses are useful if you need to move an IP address from one Google Cloud resource to another.

Some services have exceptions to the previous definitions:

  * For HA VPN, you cannot manually assign a static IPv4 address to the interface of an HA VPN gateway. Cloud VPN creates two regional external IPv4 addresses for you when you create the gateway, and those addresses remain assigned to the gateway until you delete it.

  * For Cloud NAT, when you configure Cloud NAT to automatically allocate external IPv4 addresses, those addresses appear as static; however, they are deleted if you delete the Cloud NAT gateway or if you change the Cloud NAT gateway to use manual addresses.




## What's next

  * For more information about reserving static IP addresses, see [Reserve a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address) or [Reserve a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
