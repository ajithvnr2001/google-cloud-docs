---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview/
title: Subnets and IP addresses in GDC \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:49.048540+00:00
---

# Subnets and IP addresses in GDC  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Subnets and IP addresses in GDC Stay organized with collections  Save and categorize content based on your preferences. 

Subnets are logical subdivisions of an IP address network that provide manageable segments for your services. You can define subnets with specific IP address ranges or configure them for dynamic allocation in Google Distributed Cloud (GDC) air-gapped.

This document is for network administrators within the platform administrator group and application developers within the application operator group who are responsible for managing network traffic for their services. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Networks in GDC

There are two distinct network types available in a GDC organization for which you can allocate IP addresses:

  * **Virtual Private Cloud (VPC)**: a network that is allocated internal IP addresses that are only accessible by workloads inside your organization.
  * **External network segment**: a network that is allocated external IP addresses that are accessible by external networks connected to your organization.



You can allocate subnets within each network type to accomplish specific goals. A _subnet_ is a logical subdivision of an IP address network, defined by classless inter-domain routing (CIDR) ranges. CIDR ranges let you represent IP addresses and their corresponding networks for a service to use. Each network within these network types has an independent subnet tree.

Subnets within a VPC are accessible from within the GDC network and can't be reached outside GDC. VPC subnets are available to allocate internal IP addresses within your organization. Network segment subnets are exposed to external networks connected to an organization, and let you provide external IP addresses available to networks outside of your organization.

Each network organizes subnets into a hierarchical tree structure to provide the logical subdivision and allocation of IP address ranges across different parts of the network, such as zones, services, or workloads. For more information, see Subnet hierarchy.

### VPC network

A VPC network uses internal IP addresses that are only accessible within your organization that can't be reached by networks outside your organization.

There are two VPC networks available within your GDC universe:

  * **Default VPC** : a VPC that is allocated IP addresses for internal workloads, such as containers and virtual machines (VM), within and across multiple zones.
  * **Infra VPC** : a system-managed VPC that hosts first-party GDC air-gapped services, such as Vertex AI, Observability APIs, and the GDC console. You only define IP addresses within this VPC when [planning your organization's IP address architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/plan-ip-architecture).



IP addresses within the Default VPC and Infra VPC can't overlap with each other within the same organization. For more information, see Limitations.

[Create a subnet in a VPC network](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-internal-subnets) to allocate additional IP addresses for internal workloads.

### External network segment

An external network segment is allocated external IP addresses that are accessible by external networks connected to your organization. Network segments in GDC are only allocated external IP addresses.

GDC provides the following logically isolated network segments:

  * **Admin Network Segment** : a network that is allocated external IP addresses for administrative services during organization creation, such as the GDC console and management APIs. You only define IP addresses within this network segment when [planning your organization's IP address architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/plan-ip-architecture).
  * **Data Network Segment** : a network that is allocated external IP addresses for services such as [egress network address translation (NAT)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/nat-settings) and [external load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service).



You can use distinct [interconnects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview) to connect network segments to other external networks. IP addresses within the network segments can't overlap with each other. For more information, see Limitations.

[Create a subnet in a network segment](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-external-subnets) to allocate additional external IP addresses for services that must connect to networks outside your GDC organization.

## Subnet hierarchy

Subnets are categorized by their type:

  * **Root** : top-level subnets from which other subnets can be derived. A global root subnet is created in each network during the provisioning of your organization.
  * **Branch** : subnets derived from a root or another branch subnet, used to further subdivide IP address space.
  * **Leaf** : the smallest subdivision, typically used to allocate IP addresses for a specific service or resource.



![You can subdivide your subnets to allocate IP addresses to your networks.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/subnet-types.png)

This example diagram illustrates how the different subnet types connect to each other:

  * A root subnet of `10.0.0.0/16` that serves as the top-level block for major IP address allocations.
  * From the root subnet, two branch subnets with values of `10.0.1.0/24` and `10.0.2.0/24` are derived. These branch subnets represent subdivisions of the root's address space, intended for more specific purposes.
  * The branch subnets are further subdivided into leaf subnets with values like `10.0.1.10/32`, `10.0.1.11/32`, and `10.0.2.12/24`. These leaf subnets are typically the smallest subdivisions, often allocating single IP addresses for specific services or resources.

**Note:** A branch subnet can also be subdivided into other branch subnets.

This subnet hierarchical structure lets you delegate and organize your network efficiently across the zones, workloads, and services that rely on the IP addresses within your network. For additional control of your subnet branching, define your subnet to statically or dynamically allocate CIDR blocks.

## Global and zonal subnets

In GDC, you can provision subnets within two different scopes: zonal and global. Zonal and global subnets are defined and operate within distinct API servers and offer different capabilities.

After your organization is provisioned, each network has a global root subnet that is hosted in the global API server of your organization. To provision IP addresses from the global root subnet, you must create a global `Subnet` resource in the global API server that provisions a CIDR block to a zone or across multiple zones. Within the global subnet, you define the [`propagationStrategy`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/v1/global-ipam-v1#subnetspec) field to indicate how you want to allocate your CIDR block across zones. This IP address range is provisioned to a zone as a zonal root subnet.

**Note:** A zonal root subnet provisioned directly from the global root subnet has the `ipam.gdc.goog/usage: zone-network-root-range` label within its `Subnet` resource. This label is automatically applied by the GDC system.

After a zone has its own zonal root subnet, you can create zonal `Subnet` resources in the zone's management API server to further divide the IP address range of the subnet into additional branch subnets within the zone, or leaf subnets that are available for individual workloads and services within the zone.

### Global subnets

You must create a global subnet to allocate IP addresses from the root subnet hosted in the global API server to a zone or multiple zones in your GDC universe.

Global subnets are created in the global API server using the `ipam.global.gdc.goog/v1` API group, and include optional fields like `zone` and `propagationStrategy` to define their interaction with specific zones.

Global subnets host a CIDR block as a branch subnet range that is consumed by zones across a GDC universe. For more information about where to create your global subnets, see Networks in GDC.

### Zonal subnets

A zonal subnet is linked to a specific operational zone, often including direct network configurations. Zonal subnets operate strictly within a single zone, and are mainly provided for virtual machine and container workloads within that zone. A zonal subnet further allocates IP addresses that have already been provisioned for the zone to use by a global subnet.

For VPC-to-VPC communication across zones to function properly, non-overlapping subnets must be used in each zone.

Zonal subnets are created in the management API server using the `ipam.gdc.goog/v1` API group, and include an optional [`networkSpec`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/v1/ipam-v1#subnetspec) field in their specification, so you can define zone-specific network elements like gateways and VLAN IDs.

## Subnet labeling

There are four types of subnet labels:

  * `ipam.gdc.goog/vpc`: specifies the network of the subnet as a VPC.
  * `ipam.gdc.goog/network-segment`: specifies the network of the subnet as a network segment.
  * `ipam.gdc.goog/usage`: specifies the purpose of the subnet.
  * `ipam.gdc.goog/subnet-group`: specifies the subnet group that the subnet belongs to. For more information, see Subnet groups.



The following table shows the mapping between the networks and the network labels:

Network | Label  
---|---  
Default VPC | `ipam.gdc.goog/vpc: default-vpc`  
Infra VPC | `ipam.gdc.goog/vpc: infra-vpc`  
Admin Network Segment | `ipam.gdc.goog/network-segment: admin`  
Data Network Segment | `ipam.gdc.goog/network-segment: data`  
  
The four networks' CIDR ranges are set in your organization as part of the bootstrap process. The four corresponding global subnets reside in the global API server. Those global subnets are the root-level CIDR range for each network across all the zones in an organization. All the root-level global subnets have another label `ipam.gdc.goog/usage: network-root-range`.

For each zone, a zonal network root subnet is initially available in the global API server that originates from the organization provisioning. You can create additional root subnets to expand your IP address space. Each root subnet hosts a CIDR range for a network in the specific zone, and logically serves as the zonally-scoped root subnet with the label `ipam.gdc.goog/usage: zone-network-root-range`. This root subnet must be initially created in the global API server and is automatically propagated to a specified zone. For more information about subnet scopes, see Global and zonal subnets.

You must use the defined labels when creating a `Subnet` custom resource to apply it to the appropriate GDC network. The following diagram illustrates global and zonal networks within a GDC universe:

![Subnets reside within a zone and in the global API server.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/network-subnets.png)

In this diagram, there are two organizations that span a multi-zone universe. Each organization defines the VPC networks and external network segments. In this example, anycast IP addresses are used to route traffic between the zonal external network segments so the closest or best-performing zone services the networking request. For more information about anycast IP addresses, see IP addresses in GDC.

## Subnet groups

A _subnet group_ is a set of subnets with the same subnet group label, such as `ipam.gdc.goog/subnet-group: subnetgroup1`. Organizing subnets into a group provides the following benefits:

  * A subnet group simplifies scaling up IP address resources that are owned by the same entity or used for the same purpose. A subnet can't be scaled up by itself, but you can scale up a subnet group by attaching a new subnet to it. Users can reference a subnet group as their IP address resource and utilize its scaling convenience.
  * When creating a child subnet, users can reference a subnet group as a parent instead of a single subnet. By using a subnet group in this way, users don't need to find a parent subnet that has available IP address space by themselves. Instead, GDC automatically finds a subnet in the subnet group with enough available IP address space as its parent.
  * When the IP address resources for a single purpose or entity are used up, with the subnet group as the parent, the error information in the child subnet is more straightforward and reduces the toil of checking each subnet.



All of the subnet group features apply to both global subnets and zonal subnets.

### Subnet group creation and scaling

There is no API object for a subnet group. Instead, a subnet group is identified by a label. To create or add to a subnet group, add a subnet group label to an existing subnet, or create a new subnet with a subnet group label.

If the subnet group doesn't exist yet, then a new subnet group is created. If there are other subnets with the same subnet group label already in the same namespace, then the new subnet is added to the existing subnet group.

The following example shows the definition of a subnet that is attached to a subnet group named `default-vpc-us-east67-b-group`:
    
    
    apiVersion: ipam.gdc.goog/v1
    kind: Subnet
    metadata:
      # Several lines of code are omitted here.
      labels:
        ipam.gdc.goog/subnet-group: default-vpc-us-east67-b-group
        ipam.gdc.goog/usage: zone-network-root-range
        ipam.gdc.goog/vpc: default-vpc
      name: default-vpc-us-east67-b-root-cidr
      namespace: platform
      # Several lines of code are omitted here.
    spec:
      ipv4Request:
        cidr: 10.99.0.0/16
      parentReference:
        name: default-vpc-root-cidr
        namespace: platform
        type: SingleSubnet
      type: Branch
    

### Rules for creating and scaling subnet groups

When creating a subnet group, keep the following rules in mind:

  * Subnet groups are defined for each namespace scope. Subnets with the same subnet group label but in two different namespaces are regarded as being part of two different subnet groups.
  * A subnet can't be the descendant of another subnet in the same group.
  * Subnets in the same group must belong to the same VPC or network segment.
  * A subnet can only be attached to one subnet group.



### Subnet groups as a parent

When creating a child subnet, as an alternative to using a single subnet as a parent, you can reference a subnet group as the parent. To reference a subnet group as the parent, you must complete the following:

  1. Explicitly set the `spec.parentReference.type` to `SubnetGroup`. If left empty, the default value is `SingleSubnet`.
  2. If the parent subnet group is in a different namespace than the child subnet, you must specify the `spec.parentReference.namespace` field as the namespace of the parent subnet group.



After a child subnet is created from a subnet group, GDC allocates a CIDR block from the subnet group based on the child subnet's request and the availability of the subnets in the parent subnet group. If a suitable parent subnet is found, the child subnet gets its CIDR block from the parent subnet, and the parent subnet's reference is updated in the child subnet's status.

The subnet in the following example requests a CIDR block from the `default-vpc-zone1-group` subnet group, and is allocated a parent `platform/default-vpc-zone1-root-cidr` CIDR block in the status:
    
    
    apiVersion: ipam.gdc.goog/v1
    kind: Subnet
    metadata:
    # Several lines of code are omitted here.
      labels:
        ipam.gdc.goog/vpc: default-vpc
      name: default-vpc-default-node-subnet
      namespace: platform
    # Several lines of code are omitted here.
    spec:
      ipv4Request:
        prefixLength: 23
      networkSpec:
        enableGateway: true
        enableVLANID: false
      parentReference:
        name: default-vpc-zone1-group
        namespace: platform
        type: SubnetGroup
      type: Branch
    status:
      allocatedParent:
        name: default-vpc-zone1-root-cidr
        namespace: platform
        type: SingleSubnet
    # Several lines of code are omitted here.
    

### Rules for referencing a subnet group as a parent

When referencing a subnet group as a parent, keep the following rules in mind:

  * The creator of the child subnet must have permission to use all the subnets in the subnet group.
  * The child subnet must be in the same VPC or network segment as the subnet group.



## Static and dynamic CIDR configuration

When defining subnets, you can use a static or dynamic configuration for assigning the CIDR blocks.

Static CIDR configuration lets you explicitly specify the exact CIDR block for your subnet. Statically allocate your CIDR block when you require precise control over your IP address space. Use the `spec.ipv4Request.cidr` field in the `Subnet` custom resource to specify the exact, predefined IP address range.

Dynamic CIDR configuration offers greater flexibility by allowing the system to automatically allocate a CIDR block for your subnet. Instead of providing a full CIDR, you specify the required prefix length in the `spec.ipv4Request.prefixLength` field. Dynamically allocate your CIDR block if you prefer the system to automatically delegate IP addresses to your subnets, simplifying network planning and reducing the risk of IP address conflicts. The system selects an available CIDR block of the specified size from the parent network.

For more information, see the [`SubnetRequest`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/v1/ipam-v1#subnetrequest) API.

## IP addresses in GDC

**Important:** GDC only supports IPv4 ranges for subnets created in the Default VPC and Data Network Segment. For more information, see Limitations.

Resources such as VMs and load balancers have IP addresses in GDC. These IP addresses let GDC resources communicate with other resources within an organization or to external networks connected to your organization. The following IP address types are available in a GDC universe:

External IP address
    

External IP addresses are advertised to external networks connected to an organization. Resources with external IP addresses, such as load balancers and NAT, can communicate with external networks. With GDC, you can use private or public IP addresses as external addresses. Provide external IPv4 addresses for resources in the following ways:

  * **Bring your own external IP addresses (BYOIP)** : You provide these external IP addresses for your organization. BYOIP external IP addresses can overlap with other organizations as long as they don't connect to the same external network.
  * **IO-provided external IP addresses** : Organizations can use the external IP addresses provided by the infrastructure operator group when connecting to an external network. The infrastructure operator group is the provider of the connectivity to that network.


Internal IP address
    

Internal IP addresses can't be reached from outside GDC directly and aren't publicly routable. Internal IP addresses are local to a VPC network, a VPC network connected by using VPC network peering, or an on-premises network connected to a VPC network by using Cloud VPN. Resources with internal IP addresses communicate with other resources as if they're all on the same private network.

Anycast IP address
    

Anycast IP addresses are a special type of external address which are always scoped to the entire GDC universe. GDC leverages anycast IP addresses along with Border Gateway Protocol (BGP) to route traffic to the closest or best-performing zone. Each global Layer 4 service running across two or more zones receives an anycast IP address from the anycast subnet, an external subnet. Each zone advertises the same anycast IP address, but your network picks the best one based on its routing rules. If a zone fails, it withdraws its IP address, and your network automatically reroutes traffic to another zone. This automatic routing provides seamless connectivity even during outages.

Private IP address
    

Private IP addresses are addresses that can't be routed on the internet. For a list of private IPv4 ranges, see the entries for private IP address ranges in the Valid IPv4 ranges table.

Public IP address
    

Public IP addresses are internet routable addresses. In GDC, external IP addresses can be public or private. You can also use public IPv4 addresses as internal addresses when you configure the primary IPv4 address range of a subnet in your VPC network. These addresses are referred to as privately used public IP addresses.

## IPv4 address selection

Each network in your GDC universe has a set of valid, prohibited, and unusable IPv4 addresses you must consider when allocating IP addresses.

IPv6 address ranges aren't supported in the Default VPC and Data Network Segment. Reach out to your infrastructure operator group for IPv6 range possibilities in other networks.

### Valid IPv4 ranges

The following table describes valid ranges.

Range | Description  
---|---  
**Private IPv4 address ranges**  
`10.0.0.0/8`  
`172.16.0.0/12`  
`192.168.0.0/16` |  Private IP addresses [RFC 1918](https://tools.ietf.org/html/rfc1918) For information about using `172.17.0.0/16`, see Additional considerations.   
`100.64.0.0/10` | Shared address space [RFC 6598](https://tools.ietf.org/html/rfc6598)  
`192.0.0.0/24` | IETF protocol assignments [RFC 6890](https://tools.ietf.org/html/rfc6890)  
`192.0.2.0/24` (TEST-NET-1)  
`198.51.100.0/24` (TEST-NET-2)  
`203.0.113.0/24` (TEST-NET-3) | Documentation [RFC 5737](https://tools.ietf.org/html/rfc5737)  
`192.88.99.0/24` | IPv6 to IPv4 relay (deprecated) [RFC 7526](https://tools.ietf.org/html/rfc7526)  
`198.18.0.0/15` | Benchmark testing [RFC 2544](https://tools.ietf.org/html/rfc2544)  
`240.0.0.0/4` | Reserved for future use (Class E) as noted in [RFC 5735](https://tools.ietf.org/html/rfc5735) and [RFC 1112](https://tools.ietf.org/html/rfc1112). Some operating systems don't support the use of this range, so verify that your OS supports it before creating subnets that use this range.  
**Privately used public IP address ranges**  
Privately used public IPv4 addresses  |  Privately used public IPv4 addresses have the following characteristics: 

  * Are IPv4 addresses that are normally routable on the internet, but are used privately in a VPC network.
  * Must not belong to a prohibited subnet range.

GDC air-gapped doesn't assume connectivity to the internet. As a result, GDC air-gapped advertises any public IP address ranges as if they are private to your organization. If your imported [bring your own IP (BYOIP) addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-external-subnets) are public IP address ranges, you must verify that they don't cause network issues in any external networks. Your BYOIP addresses must not overlap with other subnets in your organization.  
  
### Prohibited IPv4 subnets

Prohibited subnet ranges include commonly reserved RFC ranges and any globally reserved subnets in your specific GDC universe, as described in the following table. These ranges can't be used for subnets.

**Important:** GDC reserves IP addresses for system usage. Additionally, the infrastructure operator group might have reserved ranges that are unavailable for use by your organization. These ranges differ for each GDC universe and, therefore, can't be documented here. Verify that your infrastructure operator group provides you with these ranges to support your organization's IP address planning efforts.Range | Description  
---|---  
GDC infrastructure range  |  A globally reserved CIDR block used by the GDC system. If this range isn't specified for the `zone-infra-cidr` field of the customer intake questionnaire (CIQ), GDC uses `172.16.0.0/12` as the GDC infrastructure range by default.  
Universe-specific ranges  |  Additional ranges reserved by the infrastructure operator group.   
`0.0.0.0/8` |  Current (local) network [RFC 1122](https://tools.ietf.org/html/rfc1122)  
`127.0.0.0/8` |  Local host [RFC 1122](https://tools.ietf.org/html/rfc1122)  
`169.254.0.0/16` |  Link-local [RFC 3927](https://tools.ietf.org/html/rfc3927)  
`224.0.0.0/4` |  Multicast (Class D) [RFC 5771](https://tools.ietf.org/html/rfc5771)  
`255.255.255.255/32` |  Limited broadcast destination address [RFC 8190](https://tools.ietf.org/html/rfc8190) and [RFC 919](https://tools.ietf.org/html/rfc919)  
  
### Unusable addresses in IPv4 subnets

GDC uses the first two and last two IPv4 addresses in each subnet to host the subnet.

Unusable IPv4 address | Description | Example  
---|---|---  
Network address | First address in the primary IPv4 range. | `10.1.2.0` from range `10.1.2.0/24`  
Default gateway address | Second address in the primary IPv4 range. | `10.1.2.1` from range `10.1.2.0/24`  
Second-to-last address | Second-to-last address in the primary IPv4 range. This range is reserved by Google Cloud for potential future use. | `10.1.2.254` from range `10.1.2.0/24`  
Broadcast address | Last address in the primary IPv4 range. | `10.1.2.255` from range `10.1.2.0/24`  
  
### Additional considerations

Some Google and third-party products use `172.17.0.0/16` for routing within the guest operating system. For example, the default Docker bridge network uses this range. If you depend on a product that uses `172.17.0.0/16`, don't use it as any subnet IPv4 address range.

## Limitations

These limitations apply to VPC network subnets and external network segment subnets in GDC:

  * All subnets must be a unique valid CIDR block.
  * After you create a subnet, it can't be upscaled, replaced, or shrunk.
  * GDC only supports IPv4 ranges for subnets created in the Default VPC and Data Network Segment. Reach out to your infrastructure operator group for IPv6 range possibilities for other networks in your GDC universe.
  * GDC doesn't enforce a limit on how large of a CIDR block can be created. However, for most IP address ranges larger than `/8`, additional validations prevent you from creating a subnet that is this large. For example, a subnet can't overlap with a prohibited subnet. To minimize the chance of choosing an invalid subnet, we recommend that you limit your maximum subnet size to `/8`.
  * You can't create subnets that overlap with any prohibited subnets, any other subnet in the same VPC network, any subnet in an attached external network segment, or any subnet in a peered network. You must work with your infrastructure operator group to make sure that you don't create overlapping subnets in these scenarios.

**Note:** A peered network is any network that exchanges network routes with each other. This includes customer external networks, external network segments of organizations in a common interconnect group, and peered VPC networks. For example, the Infra VPC and Default VPC are peer networks to each other.
  * GDC creates corresponding routes for subnets. VPC network subnets have routes created in your organization's virtual network stack, and external network segment subnets have routes created in your external peered network's routing table.

  * Verify that subnets don't conflict with on-premises IP addressing if you have connected your VPC network to another network using [managed VPN](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/gdc-vpn-overview), or a shared or dedicated [interconnect](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview). 

  * Subnets must not match, be narrower, or be broader than a prohibited range. For example, `169.0.0.0/8` is not a valid subnet because it overlaps with the link-local range `169.254.0.0/16` ([RFC 3927](https://datatracker.ietf.org/doc/html/rfc3927)), which is restricted.

  * Subnets must not span an _RFC range_ , as described in Valid IPv4 ranges, and a privately used public IP address range. For example, `172.0.0.0/10` isn't a valid subnet because it includes both the `172.16.0.0/12` private IP address range and public IP addresses.

  * Subnets must not span multiple RFC ranges. For example, `192.0.0.0/8` isn't a valid subnet because it includes both `192.168.0.0/16` ([RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918)) and `192.0.0.0/24` ([RFC 6890](https://datatracker.ietf.org/doc/html/rfc6890)). However, you can create two subnets, one with `192.168.0.0/16` and one with `192.0.0.0/24`.




## What's next

  * [Networking overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/networking-overview)
  * [Provision IP addresses for workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-internal-subnets)
  * [Bring your own external IP addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-external-subnets)
  * [Zones in GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
