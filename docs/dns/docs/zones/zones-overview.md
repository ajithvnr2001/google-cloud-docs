---
url: https://docs.cloud.google.com/dns/docs/zones/zones-overview/
title: DNS zones overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:21.340099+00:00
---

# DNS zones overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/zones/zones-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  DNS zones overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud DNS supports different types of [public](https://docs.cloud.google.com/dns/docs/dns-overview#public_zone) and [private](https://docs.cloud.google.com/dns/docs/dns-overview#private_zone) zones. This document provides details about different zone types and when you can use one or the other.

## Forwarding zones

Cloud DNS forwarding zones let you configure target name servers for specific private zones. Using a forwarding zone is one way to implement outbound DNS forwarding from your VPC network.

A Cloud DNS forwarding zone is a special type of Cloud DNS private zone. Instead of creating records within the zone, you specify a set of forwarding targets. Each forwarding target is a fully qualified domain name (FQDN) or IP address of a DNS server, located in your VPC network, or in an on-premises network connected to your VPC network by Cloud VPN or Cloud Interconnect.

### Forwarding targets and routing methods

Cloud DNS supports four types of targets and offers standard or private routing methods for connectivity.

Forwarding target | Description | Standard routing supports | Private routing supports | Source of requests  
---|---|---|---|---  
Type 1 | An [internal IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) of a Google Cloud VM or an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) in _the same_ VPC network that is authorized to use the forwarding zone. | Only RFC 1918 IP addresses—traffic always routed through an authorized VPC network. | Any internal IP address, such as an RFC 1918 private address, a non-RFC 1918 private IP addresses, or a privately reused external IP address, except for a prohibited forwarding target IP address —traffic always routed through an authorized VPC network. | `35.199.192.0/19`  
Type 2 | An IP address of an on-premises system, connected to the VPC network authorized to query the forwarding zone, using Cloud VPN or Cloud Interconnect. | Only RFC 1918 IP addresses—traffic always routed through an authorized VPC network. | Any internal IP address, such as an RFC 1918 private address, a non-RFC 1918 private IP addresses, or a privately reused external IP address, except for a prohibited forwarding target IP address — traffic always routed through an authorized VPC network. | `35.199.192.0/19`  
Type 3 | An [external IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) of a DNS name server accessible to the internet _or_ the external IP address of a Google Cloud resource; for example, the external IP address of a VM in another VPC network. | Only internet-routable external IP addresses—traffic always routed to the internet or to the external IP address of a Google Cloud resource. | Private routing isn't supported—make sure that private routing is not selected. | [Google Public DNS source ranges](https://developers.google.com/speed/public-dns/faq#locations)  
Type 4 | A fully qualified domain name of a target name server that can resolve to both IPv4 and IPv6 addresses through [ VPC network resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order#vpc_steps). | Depending on the resolved forwarding target's network, traffic is routed in one of two ways: 

  * RFC 1918 IP addresses—traffic always routed through an authorized VPC network.
  * Internet-routable external IP addresses—traffic always routed to the internet or to the external IP address of a Google Cloud resource.

| Depending on the resolved forwarding target's network, traffic is routed through any internal IP address, such as an RFC 1918 private address, a non-RFC 1918 private IP address, or a privately reused external IP address, except for a prohibited forwarding target IP address—traffic always routed through an authorized VPC network. If the DNS name server resolved to a external IP address accessible to the internet or the external IP address, private routing isn't supported. | 

  * 35.199.192.0/19
  * [Google Public DNS source ranges](https://developers.google.com/speed/public-dns/faq#locations)

  
  
You can choose one of the two following routing methods when you add the forwarding target to the forwarding zone:

  * **Standard routing:** Routes traffic through an authorized VPC network or over the internet based on whether the forwarding target is an RFC 1918 IP address. If the forwarding target is an RFC 1918 IP address, Cloud DNS classifies the target as either a Type 1 or Type 2 target, and routes requests through an authorized VPC network. If the target is not an RFC 1918 IP address, Cloud DNS classifies the target as Type 3, and expects the target to be internet accessible.

  * **Private routing:** Always routes traffic through an authorized VPC network, regardless of the target's IP address (RFC 1918 or not). Consequently, only Type 1 and Type 2 targets are supported.




If you use an FQDN for your forwarding target, your routing method must match your network type. When your domain name server resolves to a public IP address, you must use standard routing.

To access a Type 1 or a Type 2 forwarding target, Cloud DNS uses routes in the authorized VPC network where the DNS client is located. These routes define a secure path to the forwarding target:

  * To send traffic to Type 1 targets, Cloud DNS uses automatically created [subnet routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes). To reply, Type 1 targets use a [special routing path for Cloud DNS responses](https://docs.cloud.google.com/vpc/docs/routes#cloud-dns).

  * To send traffic to Type 2 targets, Cloud DNS can use either [custom dynamic routes or custom static routes](https://docs.cloud.google.com/vpc/docs/routes#custom-routes), except for custom static routes with network tags. To reply, Type 2 forwarding targets use routes in your on-premises network.




For additional guidance about network requirements for Type 1 and Type 2 targets, see [forwarding target network requirements](https://docs.cloud.google.com/dns/docs/zones/forwarding-zones#firewall-rules).

**Important:** A Type 1 forwarding target _cannot_ be a VM located in another Google Cloud VPC network that's connected to a VPC network authorized to query the forwarding zone. It doesn't matter _how_ the two VPC networks are connected—either using VPC Network Peering or Cloud VPN. If you have a forwarding target in a second VPC network, create a forwarding zone and authorize that zone for the second network, and then create a peering zone in the first VPC network.

To access a Type 4 forwarding target, Cloud DNS first resolves the domain name, and then uses the source network's routing method. For example, if `subdomain.example.com` resolves to an IP address of an on-premises system that is connected to the VPC network authorized to query the forwarding zone through Cloud VPN, it uses the same routing rules as a Type 2 forwarding target.

When using an FQDN as a forwarding target, you can only use one. The forwarding target can resolve to up to 50 IP addresses.

#### Prohibited forwarding target IP addresses

You cannot use the following IP addresses for Cloud DNS forwarding targets: 

  * `169.254.0.0/16`
  * `192.0.0.0/24`
  * `192.0.2.0/24`
  * `192.88.99.0/24`
  * `198.51.100.0/24`
  * `203.0.113.0/24`
  * `224.0.0.0/4`
  * `240.0.0.0/4`
  * `::1/128`
  * `::/128`
  * `2001:db8::/32`
  * `fe80::/10`
  * `fec0::/10`
  * `ff00::/8`



### Forwarding target selection order

Cloud DNS lets you configure a list of forwarding targets for a forwarding zone.

When you configure two or more forwarding targets, Cloud DNS uses an internal algorithm to select a forwarding target. This algorithm ranks each forwarding target.

When you use an FQDN as a forwarding target, Cloud DNS resolves the domain name into a set of up to 50 IP addresses and then applies the same algorithm to those IP addresses.

To process a request, Cloud DNS first tries a DNS query by contacting the forwarding target with the highest ranking. If that server does not respond, Cloud DNS repeats the request to the next highest ranked forwarding target. If no forwarding targets reply, Cloud DNS synthesizes a [SERVFAIL](https://docs.cloud.google.com/dns/docs/troubleshooting#outbound-forwarded-queries-receive-servfail-errors) response.

The ranking algorithm is automatic, and the following factors increase the ranking of a forwarding target:

  * The higher the number of successful DNS responses processed by the forwarding target. Successful DNS responses include NXDOMAIN responses.
  * The lower the latency (round-trip time) for communicating with the forwarding target.



### Use forwarding zones

VMs in a VPC network can use a Cloud DNS forwarding zone in the following cases:

  * The VPC network has been authorized to use the Cloud DNS forwarding zone. To use the forwarding zone, you can authorize multiple VPC networks in the same project or across projects, as long as the VPC networks are within the same organization.

  * The guest operating system of each VM in the VPC network uses the VM's metadata server `169.254.169.254` as its name server.




If you use an FQDN as the target name server, review the following items:

  * You can only have a single forwarding target.
  * FQDN target resolution through another forwarding zone isn't supported.
  * You can't use an FQDN as an alternative name server in server policies.
  * An FQDN target can resolve to up to 50 associated IP addresses. Any resolved addresses over 50 are truncated.



#### Overlapping forwarding zones

Because Cloud DNS forwarding zones are a type of Cloud DNS managed private zone, you can create multiple zones that overlap. VMs configured as described earlier resolve a record according to the [name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order), using the zone with the longest suffix. For more information, see Overlapping zones.

### Caching and forwarding zones

Cloud DNS caches responses for queries sent to Cloud DNS forwarding zones. Cloud DNS maintains a cache of responses from reachable forwarding targets for the _shorter_ of the following time spans:

  * 60 seconds
  * The duration of the record's time to live (TTL)



When _all_ of the forwarding targets for a forwarding zone become unreachable, Cloud DNS maintains its cache of the previously requested records in that zone for the duration of each record's TTL.

#### When to use peering instead

Cloud DNS cannot use transitive routing to connect to a forwarding target. To illustrate an invalid configuration, consider the following scenario:

  * You've used Cloud VPN or Cloud Interconnect to connect an on-premises network to a VPC network named `vpc-net-a`.

  * You've used VPC Network Peering to connect VPC network `vpc-net-a` to `vpc-net-b`. You've configured `vpc-net-a` to export custom routes, and `vpc-net-b` to import them.

  * You've created a forwarding zone whose forwarding targets are located in the on-premises network to which `vpc-net-a` is connected. You've authorized `vpc-net-b` to use that forwarding zone.




Resolving a record in a zone served by the forwarding targets fails in this scenario, even though there is connectivity from `vpc-net-b` to your on-premises network. To demonstrate this failure, perform the following tests from a VM in `vpc-net-b`:

  * Query the VM's metadata server `169.254.169.254` for a record defined in the forwarding zone. This query fails (expectedly) because Cloud DNS does not support transitive routing to forwarding targets. To use a forwarding zone, a VM must be configured to use its metadata server.

  * Query the forwarding target directly for that same record. Although Cloud DNS does not use this path, this query demonstrates that transitive connectivity succeeds.




You can use a Cloud DNS peering zone to fix this invalid scenario:

  1. Create a Cloud DNS peering zone authorized for `vpc-net-b` that targets `vpc-net-a`.
  2. Create a forwarding zone authorized for `vpc-net-a` whose forwarding targets are on-premises name servers.



You can perform these steps in any order. After completing these steps, Compute Engine instances in both `vpc-net-a` and `vpc-net-b` can query the on-premises forwarding targets.

**Note:** You can use VPC Network Peering to leave VPC networks `vpc-net-a` and `vpc-net-b` connected; however, VPC Network Peering is not required for the Cloud DNS peering zone to operate. Peering zones don't depend on VPC Network Peering.

For information about how to create forwarding zones, see [Create a forwarding zone](https://docs.cloud.google.com/dns/docs/zones/forwarding-zones).

## Peering zones

A _peering zone_ is a Cloud DNS private zone that lets you send DNS requests between Cloud DNS zones in different VPC networks. For example, a software as a service (SaaS) provider can give customers access to their managed DNS records in Cloud DNS.

To provide DNS peering, you must create a Cloud DNS _private peering zone_ and configure it to perform DNS lookups in a VPC network where the records for that zone's namespace are available. The VPC network where the DNS peering zone performs lookups is called the _DNS producer network_.

The peering zone is only visible to VPC networks that are selected during zone configuration. The VPC network that is authorized to use the peering zone is called the _DNS consumer network_.

After Google Cloud resources in the DNS consumer network are authorized, they can perform lookups for records in the peering zone's namespace as if they were in the DNS producer network. Lookups for records in the peering zone's namespace follow the DNS producer network's name resolution order.

Therefore, Google Cloud resources in the DNS consumer network can look up records in the zone's namespace from the following sources available in the DNS producer network:

  * Cloud DNS managed private zones authorized for use by the DNS producer network.
  * Cloud DNS managed forwarding zones authorized for use by the DNS producer network.
  * Compute Engine internal DNS names in the DNS producer network.
  * An alternative name server, if an outbound server policy has been configured in the DNS producer network.



With DNS peering, you can have one network (_DNS consumer network_) forward DNS requests to another network (_DNS producer network_), which then performs DNS lookups.

### DNS peering limitations and key points

Keep the following in mind when configuring DNS peering:

  * DNS peering is a one-way relationship. It allows Google Cloud resources in the DNS consumer network to look up records in the peering zone's namespace as if the Google Cloud resources were in the DNS producer network.
  * The DNS producer and consumer networks must be VPC networks.
  * While DNS producer and consumer networks are typically part of the same organization, cross-organizational DNS peering is also supported.
  * DNS peering and [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) are different services. VPC Network Peering doesn't automatically share DNS information. DNS peering can be used with VPC Network Peering, but VPC Network Peering is _not_ required for DNS peering.
  * Transitive DNS peering is supported, but only through a single transitive hop. In other words, no more than three VPC networks (with the network in the middle being the transitive hop) can be involved. For example, you can create a peering zone in `vpc-net-a` that targets `vpc-net-b`, and then create a peering zone in `vpc-net-b` that targets `vpc-net-c`.
  * If you are using DNS peering to target a forwarding zone while global dynamic routing is disabled on the producer VPC network, the target VPC network with the forwarding zone must contain a VM, a VLAN attachment, or a Cloud VPN tunnel located in the same region as the source VM that uses the DNS peering zone. For details about this limitation, see [Forwarding queries from VMs in a consumer VPC network to a producer VPC network not working](https://docs.cloud.google.com/dns/docs/troubleshooting#forwarding-queries-from-consumer-vpc-to-producer-vpc-not-working).



For instructions about how to create a peering zone, see [Create a peering zone](https://docs.cloud.google.com/dns/docs/zones/peering-zones). 

## Managed reverse lookup zones

A managed reverse lookup zone is a private zone with a special attribute that instructs Cloud DNS to perform a PTR lookup against Compute Engine DNS data.

### PTR records for RFC 1918 addresses in private zones

To perform reverse lookups with custom PTR records for [RFC 1918 addresses](https://wikipedia.org/wiki/Private_network#Private_IPv4_addresses), you must create a Cloud DNS private zone that is at least as specific as one of the following example zones. This is a consequence of the longest suffix matching described in [Name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order).

Example zones include the following:

  * `10.in-addr.arpa.`
  * `168.192.in-addr.arpa.`
  * `16.172.in-addr.arpa.`, `17.172.in-addr.arpa.`, ... through `31.172.in-addr.arpa.`



If you create a Cloud DNS private zone for RFC 1918 addresses, custom PTR records that you create for VMs in that zone are overridden by the PTR records that [internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns) creates automatically. This is because internal DNS PTR records are created in the previous list of more specific zones.

For example, suppose you create a managed private zone for `in-addr.arpa.` with the following PTR record for a VM whose IP address is `10.1.1.1`:

`1.1.1.10.in-addr.arpa. -> test.example.domain`

In this example, the PTR record in your Cloud DNS private zone for `in-addr.arpa.` is ignored. Any PTR queries for `1.1.1.10.in-addr.arpa.` are answered by the more specific `10.in-addr.arpa.` internal DNS zone.

To override the automatically created internal DNS PTR records for VMs, make sure that you create your custom PTR records in a private zone that is at least as specific as one of the zones presented in this section. For example, if you create the following PTR record in a private zone for `10.in-addr.arpa.`, your record overrides the automatically generated one: `1.1.1.10.in-addr.arpa. -> test.example.domain`.

If you only need to override a portion of a network block, you can create more specific reverse Cloud DNS private zones. For example, a private zone for `5.10.in-addr.arpa.` can be used to hold PTR records that override any internal DNS PTR records that are automatically created for VMs with IP addresses in the `10.5.0.0/16` address range.

For instructions on how to create a managed reverse lookup zone, see [Create a managed reverse lookup zone](https://docs.cloud.google.com/dns/docs/zones/managed-reverse-lookup-zones). 

## Overlapping zones

Two zones _overlap_ with each other when the origin domain name of one zone is either identical to or is a subdomain of the origin of the other zone. For example:

  * A zone for `gcp.example.com` and another zone for `gcp.example.com` overlap because the domain names are identical.
  * A zone for `dev.gcp.example.com` and a zone for `gcp.example.com` overlap because `dev.gcp.example.com` is a subdomain of `gcp.example.com`.



### Rules for overlapping zones

Cloud DNS enforces the following rules for overlapping zones: * Overlapping public zones are not allowed on the same Cloud DNS name servers. When you create overlapping zones, Cloud DNS attempts to put them on different name servers. If that is not possible, Cloud DNS fails to create the overlapping zone.

  * A private zone can overlap with any public zone. 
  * Private zones scoped for different VPC networks can overlap with each other. For example, two VPC networks can each have a database VM named `database.gcp.example.com` in a zone `gcp.example.com`. Queries for `database.gcp.example.com` receive different answers according to the zone records defined in the zone authorized for each VPC network.

  * Two private zones that have been authorized to be accessible from the same VPC network cannot have identical origins unless one zone is a subdomain of the other. The metadata server uses longest suffix matching to determine which origin to query for records in a given zone.




### Query resolution examples

Google Cloud resolves Cloud DNS zones as described in [Name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order). When determining the zone to query for a given record, Cloud DNS tries to find a zone that matches as much of the requested record as possible (longest suffix matching).

Unless you have specified an alternative name server in an outbound server policy, Google Cloud first attempts to find a record in a private zone (or forwarding zone or peering zone) authorized for your VPC network _before_ it looks for the record in a public zone. The following examples illustrate the order that the metadata server uses when querying DNS records. For each of these examples, suppose that you have created two private zones, `gcp.example.com` and `dev.gcp.example.com`, and authorized access to them from the same VPC network. Google Cloud handles the DNS queries from VMs in a VPC network in the following way:

  * The metadata server uses public name servers to resolve a record for `myapp.example.com.` (note the trailing dot) because there is no private zone for `example.com` that has been authorized for the VPC network. Use `dig` from a Compute Engine VM to query the VM's default name server:
        
        dig myapp.example.com.
        

For details, see [Query for the DNS name using the metadata server](https://docs.cloud.google.com/dns/docs/troubleshooting#query-dns-name-using-metadata-server).

  * The metadata server resolves the record `myapp.gcp.example.com` using the authorized private zone `gcp.example.com` because `gcp.example.com` is the longest common suffix between the requested record name and available authorized private zones. `NXDOMAIN` is returned if there's no record for `myapp.gcp.example.com` defined in the `gcp.example.com` private zone, _even if there is a record for`myapp.gcp.example.com` defined in a public zone_.

  * Similarly, queries for `myapp.dev.gcp.example.com` are resolved according to records in the authorized private zone `dev.gcp.example.com`. `NXDOMAIN` is returned if there is no record for `myapp.dev.gcp.example.com` in the `dev.gcp.example.com` zone, _even if there is a record for`myapp.dev.gcp.example.com` in another private or public zone_.

  * Queries for `myapp.prod.gcp.example.com` are resolved according to records in the private zone `gcp.example.com` because `gcp.example.com` is the longest common suffix between the requested DNS record and the available private zones. 




### Split horizon DNS example

You can use a combination of public and private zones in a split horizon DNS configuration. Private zones enable you to define different responses to a query for the same record when the query originates from a VM within an authorized VPC network. Split horizon DNS is useful whenever you need to provide different records for the same DNS queries depending on the originating VPC network.

Consider the following split horizon example:

  * You've created a public zone, `gcp.example.com`, and you've configured its registrar to use Cloud DNS name servers.
  * You've created a private zone, `gcp.example.com`, and you've authorized your VPC network to access this zone.



In the private zone, you've created a single record as shown in the following table.

Record | Type | TTL (seconds) | Data  
---|---|---|---  
myrecord1.gcp.example.com | A | 5 | 10.128.1.35  
  
In the public zone, you've created two records.

Record | Type | TTL (seconds) | Data  
---|---|---|---  
myrecord1.gcp.example.com | A | 5 | 104.198.6.142  
myrecord2.gcp.example.com | A | 50 | 104.198.7.145  
  
The following queries are resolved as described:

  * A query for `myrecord1.gcp.example.com` from a VM in your VPC network returns `10.128.1.35`.
  * A query for `myrecord1.gcp.example.com` from the internet returns `104.198.6.142`.
  * A query for `myrecord2.gcp.example.com` from a VM in your VPC network returns an `NXDOMAIN` error because there's no record for `myrecord2.gcp.example.com` in the private zone `gcp.example.com`.
  * A query for `myrecord2.gcp.example.com` from the internet returns `104.198.7.145`. 



## Cross-project binding

Cross-project binding lets you keep the ownership of the DNS namespace of the service project independent of the ownership of the DNS namespace of the entire VPC network.

A typical Shared VPC setup has service projects that take ownership of a virtual machine (VM) application or services, while the host project takes ownership of the VPC network and network infrastructure. Often, a DNS namespace is created from the VPC network's namespace to match the service project's resources. For such a setup, it can be easier to _delegate_ the administration of each service project's DNS namespace to the administrators of each service project (which are often different departments or businesses). Cross-project binding lets you separate the ownership of the DNS namespace of the service project from the ownership of the DNS namespace of the entire VPC network.

The following figure shows a typical Shared VPC setup with DNS peering.

[ ![A Shared VPC setup with DNS peering.](https://docs.cloud.google.com/static/dns/images/Diagram-1-with-peering-no-cross-project-binding.svg)](https://docs.cloud.google.com/static/dns/images/Diagram-1-with-peering-no-cross-project-binding.svg) A Shared VPC setup with DNS peering (click to enlarge)

The following figure shows a setup using cross-project binding. Cloud DNS lets each service project create and own its DNS zones, but still have it bound to the shared network that the host project owns. This allows for better autonomy and a more precise permission boundary for DNS zone administration.

[ ![A setup with cross-project binding.](https://docs.cloud.google.com/static/dns/images/Diagram-2-with-cross-project-binding.svg)](https://docs.cloud.google.com/static/dns/images/Diagram-2-with-cross-project-binding.svg) A setup with cross-project binding (click to enlarge)

Cross-project binding provides the following:

  * Service project administrators and users can create and manage their own DNS zones.
  * You don't need to create a placeholder VPC network.
  * Host project administrators don't have to manage the service project.
  * IAM roles still apply at the project level.
  * All the DNS zones are directly associated with the Shared VPC network.
  * Any-to-any DNS resolution is readily available. Any VM in the Shared VPC network can resolve associated zones.
  * There is no transitive hop limit. You can manage it in a hub and spoke design.



For instructions on how to create a zone with cross-project binding enabled, see [Create a cross-project binding zone](https://docs.cloud.google.com/dns/docs/zones/cross-project-binding).

## Zonal Cloud DNS zones

Zonal Cloud DNS lets you create private DNS zones that are scoped to a Google Cloud zone only. Zonal Cloud DNS zones are created for GKE when you choose a [cluster scope](https://docs.cloud.google.com/dns/docs/zones/configure-scopes).

The default Cloud DNS service is global in nature and DNS names are visible globally within your VPC network. This configuration exposes your service to global outages. Zonal Cloud DNS is a new private Cloud DNS service that exists within each Google Cloud zone. The failure domain is contained within that Google Cloud zone. Zonal Cloud DNS private zones are not impacted when global outages occur. Any Google Cloud zonal outages only affect that specific Google Cloud zone and Cloud DNS zones within that Google Cloud zone. Note that any resource created in a zonal service is only visible to that Google Cloud zone.

To learn how to configure a zonal Cloud DNS cluster-scoped zone, see [Configure a zonal GKE cluster-scoped zone](https://docs.cloud.google.com/dns/docs/zones/configure-zonal-cluster-scopes).

### Zonal Cloud DNS support

The following table lists the Cloud DNS resources and features that are supported by zonal Cloud DNS services.

Resource or feature | Available on global Cloud DNS | Available on zonal Cloud DNS  
---|---|---  
Managed public zones  |  |   
Managed private zones (network or VPC-scoped)  |  |   
Managed private zones (GKE-scoped)  |  |   
Forwarding zones1 |  |   
Peering zones  |  |   
Managed reverse lookup zones  |  |   
Create changes or manage records2 |  |   
Service Directory zones  |  |   
Policies  |  |   
Response policies (network scoped)  |  |   
Response policies (GKE cluster scoped)  |  |   
Response policy rules  |  |   
  
1Zonal Cloud DNS supports only forwarding zones scoped to a GKE cluster.

2The GKE controller overwrites any changes to the records when it restarts.

### Billing for zonal Cloud DNS zones

Billing for zonal Cloud DNS zones and response policies works the same way as their global counterparts.

## What's next

  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
