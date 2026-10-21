---
url: https://docs.cloud.google.com/compute/docs/network-bandwidth/
title: Network bandwidth \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:58.627359+00:00
---

# Network bandwidth  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/network-bandwidth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Network bandwidth Stay organized with collections  Save and categorize content based on your preferences. 

Most machine types provide only one physical NIC. When you create compute instances using these machine types, each virtual network interface (vNIC) that you configure uses the same physical NIC. For these instances, Google Cloud accounts for bandwidth per virtual machine (VM) instance or bare metal instance, not per virtual network interface (vNIC) or IP address. The instance's [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) defines its maximum possible egress rate; however, you can only achieve that maximum possible egress rate in specific situations.

Some machine types (for example `z4m-highmem-192`) provide multiple physical NICs. When you create compute instances using these machine types, Compute Engine assigns each virtual network interface (vNIC) that you configure to a physical NIC. For Z4D, Z4M, and C4N multi-NIC machine types, Compute Engine uses a round-robin distribution to assign vNICs to physical NICs.

This page outlines the network bandwidth limits, which are useful when planning your deployments. It categorizes bandwidth using two dimensions:

  * **Egress or ingress** : As used on this page, egress and ingress are always from the perspective of a Google Cloud instance: 
    * Packets sent _from_ a Google Cloud instance compose its _egress_ (outbound) traffic.
    * Packets sent _to_ a Google Cloud instance compose its _ingress_ (inbound) traffic.
  * **How the packet is routed** : A packet can be routed from a sending instance or to a receiving instance using routes whose next hops are _within_ a VPC network or routes outside of a VPC network.



All of the information on this page is applicable to Compute Engine compute instances, as well as products that depend on Compute Engine instances. For example, a Google Kubernetes Engine node is a Compute Engine instance.

**Note:** For network bandwidth information for Accelerator-optimized machine series, see [Networking and GPU machines](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth).

## Configurations that impact network bandwidth

For compute instances that have only one physical NIC, you can't increase the ingress or egress bandwidth by using either [additional virtual network interfaces (vNICs)](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts) or additional IP addresses per vNIC. For example, a Compute Engine C3 instance with 22 vCPUs is limited to 23 Gbps total egress bandwidth. If you configure the C3 instance with two vNICs, the instance is still limited to 23 Gbps total egress bandwidth, not 23 Gbps bandwidth per vNIC.

The following sections describe how other compute instance configurations can impact network bandwidth.

### Use per VM Tier_1 networking performance

For second and third generation compute instances, to get the highest possible ingress and egress bandwidth, [configure Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#create-high-bandwidth-vms). Fourth generation and later machine series provide a multi-NIC, network-optimized machine series for higher network bandwidth instead of using Tier_1 networking.

### Dynamic Network Interfaces

Dynamic Network Interfaces use the bandwidth of their parent vNIC. There is no traffic isolation within a parent vNIC. Network traffic from a Dynamic NIC can starve the other Dynamic NICs associated with the same parent vNIC. To avoid this conflict, you can use Linux traffic control (TC) to craft application-specific traffic shaping policies. These policies help you implement fairness or prioritization for network traffic.

To prioritize network traffic, you map traffic (for example for Dynamic NICs) to a traffic class, and then map that traffic class to a quality of service. For an example of this approach, see [Traffic shaping with Red Hat](https://carroll.net/blog/traffic-shaping-with-red-hat/).

Dynamic NICs aren't supported for Compute Engine instances that run a Windows OS.

### Bandwidth sharing with Cloud RDMA

Applications using Cloud RDMA typically use both TCP and RDMA traffic. For example, during high performance computing (HPC) jobs, applications commonly use TCP for communication during load and store phases, and RDMA for compute stages. The following machine series support Cloud RDMA:

  * H4D instances provide up to 200 Gbps network bandwidth.
  * Z4M instances provide up to 400 Gbps network bandwidth with two physical NICs.



When you configure a compute instance to use Cloud RDMA, the network bandwidth is shared among the configured network interfaces.

Network bandwidth allocation between Cloud RDMA traffic and TCP traffic is done dynamically:

  * When both network interface types are in use, the bandwidth is shared between Cloud RDMA traffic and TCP traffic.
  * The gVNIC or IDPF network interface can use all of the available bandwidth when the Cloud RDMA network interface isn't being used.
  * The Cloud RDMA network interface can use all of the available bandwidth when the gVNIC or IDPF network interface isn't being used.



## Bandwidth summary

The following table illustrates the maximum possible bandwidth based on whether a packet is sent from (egress) or received by (ingress) a compute instance and the packet routing method.

###  Egress bandwidth limits 

Routing within  
a VPC network | 

  * Primarily defined by a per-instance maximum egress bandwidth based on the sending instance's machine type and whether Tier_1 networking is enabled.
    * N2, N2D, C2, C2D, M3, and C4A VMs with Tier_1 networking support egress bandwidth limits up to 100 Gbps.
    * H3 VMs support VM-to-VM egress bandwidth limits up to 200 Gbps.
    * H4D instances support VM-to-VM egress bandwidth of up to 200 Gbps for Cloud RDMA and gVNIC combined.
    * X4, M4, A2, and G2 instances support egress bandwidth limits up to 100 Gbps.
    * X5 instances support egress bandwidth limits up to 200 Gbps.
    * G4 instances support egress bandwidth limits up to 400 Gbps.
    * A4X Max instances support egress bandwidth limits up to 3,600 Gbps.
    * A4X instances support egress bandwidth limits up to 2,000 Gbps.
    * A4 and A3 instances support egress bandwidth limits up to 3,600 Gbps.
    * C4, C4D, C3, C3D, and Z3 instances support up to 200 Gbps egress bandwidth limits with Tier_1 networking.
    * Z4D, Z4M, and M4N instances with two physical NICs support up to 400 Gbps VM-to-VM egress bandwidth.
    * C4N instances with two physical NICs support up to 400 Gbps VM-to-VM egress bandwidth, up to 95,000,000 packets-per-second (PPS), and up to 50 Gbps single-flow bandwidth between C4N instances routed within the same VPC network.
  * For other factors, definitions, and scenarios, see Egress to destinations routable within a VPC network. 

  
---|---  
Routing outside  
a VPC network | 

  * For H3 and H4D instances, outbound data transfer to a destination outside of its VPC network is limited to 1 Gbps.
  * For C4N instances, the limit is:
    * 100 Gbps per physical NIC, or 200 Gbps for dual-NIC instances
    * 24,000,000 PPS per physical NIC, or 48,000,000 PPS for dual-NIC instances
  * For all other machine series, the limit is primarily defined by a per-instance maximum egress bandwidth based on the sending instance's machine type and whether Tier_1 networking is enabled. A sending instance's maximum possible egress bandwidth to a destination outside of its VPC network can't exceed the following:
    * 3 Gbps per flow
    * When Tier_1 networking is enabled: 25 Gbps total
    * When Tier_1 networking isn't enabled or isn't supported, the following total bandwidth is available per machine series: 
      * For Z4M instances, 50 Gbps total for instances with 192 vCPUs and up to 25 Gbps total for instances with 96 vCPUs or fewer, depending on the machine type size.
      * For Z4D instances, 50 Gbps total for instances with 384 vCPUs and up to 25 Gbps total for instances with 192 vCPUs or fewer, depending on the machine type size.
      * For G4 instances: 25 Gbps total for machine types with 48 or more vCPUs, and 7 Gbps total for machine types with fewer than 48 vCPUs.
      * For machine series that support multiple physical NICs, such as M4N, A3, A4, A4X, and A4X Max instances, 7 Gbps per NIC
      * For all other machine series, 7 Gbps total
  * For other factors, definitions, and caveats, see Egress to destinations outside of a VPC network.

  
  
###  Ingress bandwidth limits

Routing within  
a VPC network | 

  * Generally, ingress rates are similar to the egress rates for a machine type.
  * To get the highest possible ingress bandwidth, use a multi-NIC instance, or [enable Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#create-high-bandwidth-vms), if supported.
  * The size of your compute instance, the capacity of the server NIC, the traffic coming into other compute instances running on the same host hardware, your guest OS network configuration, and the number of disk reads performed by your instance can all impact the ingress rate.
  * Google Cloud doesn't impose any additional limitations on ingress rates within a VPC network.
  * For other factors, definitions, and scenarios, see Ingress to destinations routable within a VPC network. 

  
---|---  
Routing outside  
a VPC network | 

  * Google Cloud protects each compute instance by limiting ingress traffic routed outside a VPC network. The limit is the first of the following rates encountered:
    * 1,800,000 pps (packets per second)
    * 30 Gbps
  * For C4N instances, the limit is the first of the following rates encountered: 
    * 24,000,000 packets per second (PPS) per physical NIC or 48,000,000 PPS for dual-NIC instances
    * 90 Gbps per physical NIC or 180 Gbps for dual-NIC instances
  * For a machine series that supports multiple physical NICs, such as M4N, Z4D, Z4M, A3, A4, A4X, and A4X Max instances, the limit is the first of the following rates encountered:
    * 1,800,000 pps (packets per second) per physical NIC
    * 30 Gbps per physical NIC
  * For other factors, definitions, and scenarios, see Ingress to destinations outside of a VPC network.

  
  
## Egress bandwidth

Google Cloud limits outbound (egress) bandwidth using per-instance maximum egress rates. These rates are based the machine type of the compute instance that is sending the packet and whether the packet's destination is accessible using routes within a VPC network or routes outside of a VPC network. Outbound bandwidth includes packets emitted by all of the instance's NICs and data transferred to all Hyperdisk and Persistent Disk volumes connected to the instance.

### Per-instance maximum egress bandwidth

Per-instance maximum egress bandwidth is generally 2 Gbps per vCPU, but there are some differences and exceptions, depending on the machine series. The following table shows the range of maximum limits for egress bandwidth for traffic routed within a VPC network.

The following table summarizes the maximum egress bandwidth for each machine series. You can find the per-instance maximum egress bandwidth for every machine type listed on its specific machine family page (using the links for each machine series in the table).

For network egress bandwidth limits for compute instances with attached GPUs, see [Networking and GPU machines](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth).

| Maximum per-instance egress limit  
---|---  
Machine series | Standard | Tier_1 networking  
[C4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_machine_types) | 400 Gbps | Not applicable  
[C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_machine_types) and [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_machine_types) | 100 Gbps | 200 Gbps  
[C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_machine_types) | 50 Gbps | 100 Gbps  
[C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_machine_types) and [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_machine_types) | 100 Gbps | 200 Gbps  
[C2](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2_machine_types) and [C2D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2d_machine_types) | 32 Gbps | 100 Gbps  
[E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types_table) | 16 Gbps | Not available  
E2 shared-core | 2 Gbps | Not available  
[H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types) and [H3](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_machine_types) | 200 Gbps | Not available  
[M4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#m4n_machine_types) | 400 Gbps | Not applicable  
[M4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_machine_types) | 100 Gbps | Not available  
[M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_machine_types) | 32 Gbps | 100 Gbps  
[M2](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_machine_types) | 32 Gbps on Intel Cascade Lake or later CPU  
16 Gbps on other CPU platforms | Not available  
[M1](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_machine_types) | 32 Gbps | Not available  
[N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_machine_types), [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_machine_types), and [N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_machine_types) | 50 Gbps | Not applicable  
[N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_machine_types) and [N2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machine_types) | 32 Gbps | 100 Gbps  
[N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machine_types) (excluding VMs with 1 vCPU) | 32 Gbps on Intel Skylake and later CPU  
16 Gbps on earlier CPU platforms | Not available  
N1 machine types with 1 vCPU | 2 Gbps | Not available  
N1 shared-core (f1-micro and g1-small) | 1 Gbps | Not available  
[T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machine_types) and [T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machine_types) | 32 Gbps | Not available  
[X5](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x5_machine_types) | 200 Gbps | N/A  
[X4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_machine_types) | 100 Gbps | Not applicable  
[Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_machine_types) | 100 Gbps | 200 Gbps  
[Z4D](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_machine_types) | 400 Gbps | Not applicable  
[Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_machine_types) | 400 Gbps | Not applicable  
  
Per-instance maximum egress bandwidth is not a guarantee. The actual egress bandwidth can be lowered according to factors such as the following non-exhaustive list:

  * Using VirtIO instead of [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) with compute instances that support both network interface drivers
  * Packet size
  * Protocol overhead
  * The number of flows
  * Ethernet driver settings of the compute instance's guest OS, such as checksum offload and TCP segmentation offload (TSO)
  * Network congestion
  * In a situation where Persistent Disk I/Os compete with other network egress traffic, 60% of the maximum network bandwidth is given to Persistent Disk writes, leaving 40% for other network egress traffic. See [Factors that affect disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#performance_factors) for more details.



To get the largest possible per-instance maximum egress bandwidth:

  * Use a machine type from the network-optimized machine series and configure two network interfaces when creating the compute instance to get the highest possible bandwidth.
  * Use third generation or later machine series that use [Titanium](https://cloud.google.com/titanium) to offload network processing from the host CPU.
  * If using a second or third generation machine series, enable [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#bandwidth-tiers) with larger machine types.
  * Use the largest VPC network [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) supported by your network topology. Larger MTUs can reduce packet-header overhead and increase payload data throughput.
  * Use the latest gVNIC driver version, if supported by your instance and guest OS.



### Egress to destinations routable within a VPC network

From the perspective of a sending instance and for destination IP addresses accessible by means of routes _within a VPC network_ , Google Cloud limits outbound traffic using these rules:

  * **Per-VM maximum egress bandwidth:** The per-instance maximum egress bandwidth described in the Per-instance maximum egress bandwidth section.
  * **Per-project inter-regional egress bandwidth:** If a sending instance and an internal destination or its next hop are in different regions, Google Cloud enforces a quota based on the region and project of the sending instance and the region of the internal destination or next hop. For more information about this quota, see [Inter-region network egress bandwidth (Mbps) from Compute instances](https://docs.cloud.google.com/vpc/docs/quota#per_project) in the VPC quotas and limits documentation.
  * **Cloud VPN and Cloud Interconnect limits:** When sending traffic from an instance to an internal IP address destination routable by a next hop Cloud VPN tunnel or Cloud Interconnect VLAN attachment, egress bandwidth is limited by: 
    * [Maximum packet rate and bandwidth per Cloud VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/quotas#limits)
    * [Maximum packet rate and bandwidth per VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas#limits)
    * To fully use the bandwidth of multiple next hop Cloud VPN tunnels or Cloud Interconnect VLAN attachments using ECMP routing, you must use multiple TCP connections (unique 5-tuples).



Destinations routable within a VPC network include all of the following destinations, each of which is accessible from the perspective of the sending instance by a route whose next hop is _not_ the default internet gateway:

  * Regional internal IPv4 addresses in [subnet primary IPv4 and subnet secondary IPv4 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges), including private IPv4 address ranges and privately used public IPv4 address ranges, used by these destination resources: 
    * The primary internal IPv4 address of a receiving instance's network interface (vNIC). (When a sending instance connects to another instance's vNIC _external_ IPv4 address, packets are routed using a next hop default internet gateway, so Egress to destinations outside of a VPC network applies instead.)
    * An internal IPv4 address in an alias IP range of a receiving instance's vNIC.
    * An internal IPv4 address of an internal forwarding rule for either protocol forwarding or for an internal passthrough Network Load Balancer.
  * Global internal IPv4 addresses for these destination resources: 
    * [Private Service Connect endpoints for Google Cloud APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis)
    * [Allocated ranges for private services access](https://docs.cloud.google.com/vpc/docs/private-services-access)
  * [Internal IPv6 subnet address ranges](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6) used by these destination resources: 
    * An IPv6 address from the `/96` IPv6 address range assigned to a dual-stack or IPv6-only receiving instance's vNIC.
    * An IPv6 address from the `/96` IPv6 address range of an internal forwarding rule for either protocol forwarding or for an internal passthrough Network Load Balancer.
  * [External IPv6 subnet address ranges](https://docs.cloud.google.com/vpc/docs/subnets#external-ipv6) used by these destination resources _when packets are routed using subnet routes or peering subnet routes within the VPC network or by custom routes within the VPC network that do not use the default internet gateway next hop_ : 
    * An IPv6 address from the `/96` IPv6 address range assigned to a dual-stack or IPv6-only receiving instance's vNIC.
    * An IPv6 address from the `/96` IPv6 address range of an external forwarding rule for either protocol forwarding or for a regional external passthrough Network Load Balancer.
  * Other destinations accessible using the following VPC network routes: 
    * [Dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes)
    * [Static routes](https://docs.cloud.google.com/vpc/docs/static-routes) _except_ those that use a default internet gateway next hop
    * [Peering custom routes](https://docs.cloud.google.com/vpc/docs/routes#peering-custom-routes)



The following list ranks traffic from sending instances to internal destinations, from highest possible bandwidth to lowest:

  * Between compute instances in the same zone
  * Between compute instances in different zones of the same region
  * Between compute instances in different regions
  * From a compute instance to Google Cloud APIs and services using [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) or [accessing Google APIs from an instance's external IP address](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip). This includes [Private Service Connect endpoints for Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints).



### Egress to destinations outside of a VPC network

From the perspective of a sending instance and for destination IP addresses _outside of a VPC network_ , Google Cloud limits outbound traffic to whichever of the following rates is reached first:

  * **Per-instance egress bandwidth:** The maximum bandwidth for all connections from a compute instance to destinations outside of a VPC network is the smaller of the Per-instance maximum egress bandwidth and one of these rates:

    * If Tier_1 networking is enabled: 25 Gbps
    * If Tier_1 networking isn't enabled or isn't supported: 
      * For C4N instances: Up to 100 Gbps per physical NIC or 200 Gbps for dual-NIC instances
      * For Z4D and Z4M instances: 7 Gbps total for machine types with fewer than 48 vCPUs, and up to 25 Gbps per physical NIC for machine types with 48 or more vCPUs
      * For G4 instances: 7 Gbps total for machine types with fewer than 48 vCPUs, and 25 Gbps total for machine types with 48 or more vCPUs
      * For H4D and H3 instances: 1 Gbps
      * For machine series that support multiple physical NICs, such as M4N, A3, A4, A4X, and A4X Max instances: 7 Gbps per physical NIC
      * For all other machine series: 7 Gbps
**Note:** Maximum egress bandwidth can be achieved when the packet size matches the default MTU value of 1,460 bytes. As the packet size decreases, the maximum achievable bandwidth also declines due to limitations on the number of packets per second that the compute instance can handle.

For example, even though a `c3-standard-44` VM has a per-instance _maximum_ egress bandwidth of 32 Gbps, the per-instance egress bandwidth from a `c3-standard-44` VM to external destinations is either 25 Gbps or 7 Gbps, depending on whether Tier_1 networking is enabled.

  * **Per-flow maximum egress rate:** The maximum bandwidth for _each_ unique 5-tuple connection, from a compute instance to a destination outside of a VPC network is 3 Gbps, except for H4D and H3 instances, where it is 1 Gbps.

  * **Per-project internet egress bandwidth:** The maximum bandwidth for all connections from compute instances in _each_ region of a project to destinations outside of a VPC network is defined by the project's [Internet egress bandwidth](https://console.cloud.google.com/iam-admin/quotas?metric=compute.googleapis.com/vm_to_internet_egress_bandwidth) quotas.




Destinations outside of a VPC network include all of the following destinations, each of which is accessible by a route in the sending instance's VPC network whose next hop _is_ the default internet gateway:

  * Global external IPv4 and IPv6 addresses for external proxy Network Load Balancers and external Application Load Balancers
  * Regional external IPv4 addresses for Google Cloud resources, including the vNIC external IPv4 addresses for an instance, external IPv4 addresses for external protocol forwarding, regional external passthrough Network Load Balancers, and response packets to Cloud NAT gateways.
  * Regional external IPv6 addresses in dual-stack or IPv6-only subnets with [external IPv6 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#external-ipv6) used by external IPv6 addresses of dual-stack or IPv6-only instances, external protocol forwarding, and regional external passthrough Network Load Balancers. The subnet must be located in a separate, non-peered VPC network. The destination IPv6 address range must be accessible using a route in the sending instance's VPC network whose next hop _is_ the default internet gateway. If a dual-stack or IPv6-only subnet with an external IPv6 address range is located in the same VPC network or in a peered VPC network, see Egress to destinations routable within a VPC network instead.
  * Other external destinations accessible using a static route in the sending instance's VPC network provided that the next hop for the route _is_ the default internet gateway.



For details about which Google Cloud resources use what types of external IP addresses, see [External IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses#external).

## Ingress bandwidth

Google Cloud handles inbound (ingress) bandwidth depending on how the incoming packet is routed to a receiving compute instance.

### Ingress to destinations routable within a VPC network

A receiving compute instance can handle as many incoming packets as its machine type, operating system, and other network conditions permit. For other machine series, Google Cloud doesn't implement any purposeful bandwidth restriction on incoming packets delivered to an instance if the incoming packet is delivered using routes _within_ a VPC network:

  * Subnet routes in the receiving instance's VPC network
  * Peering subnet routes in a peered VPC network
  * Routes in another network whose next hops are Cloud VPN tunnels, Cloud Interconnect (VLAN) attachments, or Router appliance instances located in the receiving instance's VPC network



Destinations for packets that are routed within a VPC network include:

  * The primary internal IPv4 address of the receiving instance's virtual network interface (vNIC). Primary internal IPv4 addresses are regional internal IPv4 addresses that come from a [subnet's primary IPv4 address range](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges).
  * An internal IPv4 address from an alias IP range of the receiving instance's vNIC. Alias IP ranges can come from either a subnet's primary IPv4 address range or one of its secondary IPv4 address ranges.
  * An IPv6 address from the `/96` IPv6 address range assigned to a dual-stack or IPv6-only receiving instance's vNIC. Compute instance IPv6 ranges can come from these subnet IPv6 ranges: 
    * An [internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6).
    * An [external IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#external-ipv6) _when the incoming packet is routed internally to the receiving instance using one of the VPC network routes listed previously in this section_.
  * An internal IPv4 address of a forwarding rule used by internal protocol forwarding to the receiving instance or internal passthrough Network Load Balancer where the receiving instance is a backend of the load balancer. Internal forwarding rule IPv4 addresses come from a subnet's primary IPv4 address range.
  * An internal IPv6 address from the `/96` IPv6 range of a forwarding rule used by internal protocol forwarding to the receiving instance or internal passthrough Network Load Balancer where the receiving instance is a backend of the load balancer. Internal forwarding rule IPv6 addresses come from a subnet's internal IPv6 address range.
  * An external IPv6 address from the `/96` IPv6 range of a forwarding rule used by external protocol forwarding to the receiving instance or regional external passthrough Network Load Balancer. The receiving instance is a backend of the load balancer _when the incoming packet is routed within the VPC network using one of the routes listed previously in this section_. External forwarding rule IPv6 addresses come from a subnet's external IPv6 address range.
  * An IP address within the destination range of a custom static route that uses the receiving instance as a next hop instance (`next-hop-instance` or `next-hop-address`).
  * An IP address within the destination range of a custom static route using an internal passthrough Network Load Balancer (`next-hop-ilb`) next hop, if the receiving instance is a backend for that load balancer.



### Ingress to destinations outside of a VPC network

Google Cloud implements the following bandwidth limits for incoming packets delivered to a receiving instance using routes _outside_ a VPC network. When load balancing is involved, the bandwidth limits are applied individually to each receiving instance.

For machine series that don't support multiple physical NICs, the applicable inbound bandwidth restriction applies collectively to all virtual network interfaces (vNICs). The limit is the first of the following rates encountered:

  * 1,800,000 packets per second
  * 30 Gbps



For machine series that support multiple physical NICs the applicable inbound bandwidth restriction applies individually to each physical NIC. The limit is the first of the following rates encountered:

  * For C4N instances: 
    * 24,000,000 PPS per physical NIC (or 48,000,000 PPS for dual-NIC instances)
    * 90 Gbps per physical NIC (or 180 Gbps for dual-NIC instances)
  * For other instance types: 
    * 1,800,000 PPS per physical NIC
    * 30 Gbps per physical NIC

**Note:** Depending on the machine type of your compute instance and other factors, actual inbound traffic might be less than 30 Gbps or 1,800,000 packets per second. Bandwidth from the internet is not covered by any SLA and is subject to network conditions.

Destinations for packets that are routed using routes outside of a VPC network include:

  * An external IPv4 address assigned in a one-to-one NAT access configuration on one of the receiving instance's network interfaces (NICs).
  * An external IPv6 address from the `/96` IPv6 address range assigned to a vNIC of a dual-stack or IPv6-only receiving instance _when the incoming packet is routed using a route outside of the receiving instance's VPC network._
  * An external IPv4 address of a forwarding rule used by external protocol forwarding to the receiving instance or regional external passthrough Network Load Balancer where the receiving instance is a backend of the load balancer.
  * An external IPv6 address from the `/96` IPv6 range of a forwarding rule used by external protocol forwarding to the receiving instance or regional external passthrough Network Load Balancer. The receiving instance must be a backend of the load balancer _when the incoming packet is routed using a route outside of a VPC network._
  * Established inbound responses processed by Cloud NAT.



## Use jumbo frames to maximize network bandwidth

To receive and send [jumbo frames](https://en.wikipedia.org/wiki/Jumbo_frame), configure the VPC network used by your compute instances; set the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) to a larger value, up to `8896`.

Higher MTU values increase the packet size and reduce the packet-header overhead, which increases payload data throughput.

You can use jumbo frames on compute instances that use the gVNIC driver version 1.3 or later, or with the IDPF driver on bare metal instances. Not all Google Cloud public images include these drivers. For more information about operating system support for jumbo frames, see the **Networking features** tab on the [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#network-features) page.

**Note:** The image versions that indicate full support for jumbo frames include the updated gVNIC driver, even if the guest OS shows the gve driver version as `1.0.0`.

If you are using an OS image that doesn't have full support for jumbo frames, you can manually install gVNIC driver version v1.3.0 or later. Google recommends installing the gVNIC driver version marked `Latest` to benefit from additional features and bug fixes. You can download the gVNIC drivers from [GitHub](https://github.com/GoogleCloudPlatform/compute-virtual-ethernet-linux/releases).

To manually update the gVNIC driver version in your guest OS, see [Use on non-supported operating systems](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup).

### Jumbo frames and GPU machines

For GPU machine types, use the recommended MTU settings for Jumbo frames. For more information, see [Recommended MTU settings for Jumbo frames](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mtu-gpu).

## Receive and transmit queues

Each NIC (physical NIC or virtual NIC) for a compute instance is assigned a number of receive and transmit queues for processing packets from the network.

  * Receive Queue (RX): Queue to receive packets. When the NIC receives a packet from the network, the NIC selects the descriptor for an incoming packet from the queue, processes it and hands the packet to the guest OS over a packet queue attached to a vCPU core using an interrupt. If the RX queue is full and there is no buffer available to place a packet, then the packet is dropped. This can typically happen if an application is over-utilizing a vCPU core that is also attached to the selected packet queue.
  * Transmit Queue (TX): Queue to transmit packets. When the guest OS sends a packet, a descriptor is allocated and placed in the TX queue. The NIC then processes the descriptor and transmits the packet.



### Default queue allocation

Unless you explicitly assign queue counts for NICs, you can model the algorithm Google Cloud uses to assign a fixed number of RX and TX queues per vNIC as described in the following table:

Compute instance configuration | Maximum queue count per vNIC | Maximum queue count per instance  
---|---|---  
Bare metal instances | 16 | 16  
Network-optimized C4N instances | 64 | The number of vCPUs  
Storage-optimized Z4D and Z4M instances (including bare metal machine types) | 16 | The number of vCPUs  
C4 instances with 2 vCPUs | 1 | 2  
C4 instances with 4 vCPUs | 2 | 8  
Third generation (excluding M3) and later VM instances that use gVNIC with [Titanium](https://cloud.google.com/titanium), including Z4D  |  Divide the number of vCPUs by the number of vNICs (`num_vcpus/num_vnics`) and discard any remainder.

  * If the calculated number is less than 1, then the maximum queue count per vNIC is 1.
  * If the calculated number is greater than 16, then the maximum queue count is 16 for each vNIC.
  * Otherwise, the maximum queue count per vNIC is the calculated number

| The number of vCPUs  
M3, or first and second generation VMs that use gVNIC |  Divide the number of vCPUs by the number of vNICs, and then divide the result by 2 (`num_vcpus/num_vnics/2`). Discard any remainder.

  * If the calculated number is less than 1, then the maximum queue count per vNIC is 1.
  * If the calculated number is greater than 16, then the maximum queue count per vNIC is 16.
  * Otherwise, the maximum queue count per vNIC is the calculated number.

| The number of vCPUs / 2  
First and second generation VMs that use the VirtIO network interface or a custom driver |  Divide the number of vCPUs by the number of vNICs (`num_vcpus/num_vnics`), and discard any remainder.

  * If the calculated number is less than 1, then the maximum queue count per vNIC is 1.
  * If the calculated number is greater than 32, then the maximum queue count per vNIC is 32.
  * Otherwise, the maximum queue count per vNIC is the calculated number.

| The number of vCPUs  
H4D instances with Cloud RDMA | 16 | 16, or 32 if using Cloud RDMA  
Confidential VM instances | 16 | 16  
  
#### Examples

The following examples show how to calculate the default number of queues for a VM instance:

  * If a VM instance uses VirtIO and has 16 vCPUs and four vNICs, the calculated number is `[16/4] = 4`. Google Cloud assigns each vNIC four queues.

  * If a VM instance uses gVNIC with Titanium offloads, and has 128 vCPUs and two vNICs, then the calculated number is `[128/2] = 64`. Google Cloud assigns each vNIC the maximum number of queues per vNIC, which is `16`.




On Linux systems, you can use `ethtool` to configure a vNIC with fewer queues than the number of queues Google Cloud assigns per vNIC.

### Queue counts when using Dynamic Network Interface

If you use Dynamic Network Interfaces with your network interfaces, the queue counts don't change. A Dynamic NIC doesn't have its own receive and transmit queues; it uses the same queues as the parent vNIC.

### Custom queue allocation for VM instances

Instead of the default queue allocation, you can assign a custom queue count (total of both RX and TX) to each vNIC when you create a new compute instance by using the Compute Engine API.

The number of custom queues you specify must adhere to the following rules:

  * The minimum queue count you can assign per vNIC is one.

  * The maximum queue count that you can assign to each vNIC of a compute instance is the lower of the vCPU count or the per-vNIC maximum queue count, based on the network interface type:

    * Using [virtIO](https://ozlabs.org/%7Erusty/virtio-spec/virtio-0.9.5.pdf) or a custom driver, the maximum queue count is `32`.
    * Using [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic), the maximum queue count is `16`, except for the following: 
      * C4N, Z4D, and Z4M instances have a maximum queue count of 64 per NIC.
      * A2 or G2 instances have a maximum queue count of 32 per NIC.
      * [TPU instances](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute) have a maximum queue count of 32.
      * C2, C2D, N2, or N2D instances with Tier_1 networking enabled have a maximum queue count of 32 per NIC.
    * Using [IRDMA](https://docs.cloud.google.com/compute/docs/networking/using-irdma), the maximum queue count is 8.
    * Using an [IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf) network interface, the maximum queue count is 16, except for Z4D and Z4M bare metal instances, which have a maximum queue count of 64.
    * The following [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) configurations have a maximum queue count of `8`:

      * AMD SEV on C2D and N2D machine types
      * AMD SEV-SNP on N2D machine types
  * The sum of queue counts across _all_ NICs configured for the compute instance must adhere to one of the following rules:

    * The maximum value is the lesser of: 
      * `[number of vCPUS]`
      * `[number of NICs] * [max number of queues per NIC]`
    * If using queue oversubscription, the maximum value is: 
      * `[number of vNICs] * 16`



With _queue oversubscription_ , you can assign up to 16 queues for each vNIC of a VM instance, even if the total queue count for the VM exceeds the number of vCPUs. To oversubscribe the custom queue count, the VM instance must satisfy the following conditions:

  * Uses gVNIC as the vNIC type for all vNICs configured for the instance.
  * Uses a machine type in the N2, N2D, C2, or C2D machine series.
  * Has Tier_1 networking enabled.
  * Specifies a custom queue count for all vNICs configured for the VM instance.



With queue oversubscription, the maximum queue count for the VM instance is 16 times the number of vNICs. So, if you have six vNICs configured for an instance with 30 vCPUs, you can configure a maximum of `(16 * 6)`, or 96 custom queues for your VM instance.

**Examples**

  * For an N2 VM instance with eight vCPUs and four vNICs:

    * You can assign a maximum of eight queues across the four vNICs. For example, you can assign one queue to `nic0`, four queues to `nic1`, and three queues to `nic2`.
    * Queue oversubscription isn't possible because Tier_1 networking with N2 requires a VM with at least 32 vCPUs.
  * If a VM has 48 vCPUs and 4 NICs:

    * If you use the virtIO driver for the NICs, then you can assign a maximum of 48 queues across the 4 NICs, with a maximum queue count of 32 for any vNIC. For example, you could have 12 queues on each vNIC, or you could have 32 queues on one of the NICs, 14 queues on another vNIC, and 1 queue on the remaining 2 NICs.
    * If you use the gVNIC driver for the NICs, then you can assign a maximum of 48 queues across the 4 NICs, with a maximum queue count of 16 for any vNIC. For example, you could have 15 queues on 3 NICs, and 3 queues on the remaining vNIC, or you could have 12 queues on each vNIC.
    * If you use gVNIC and queue oversubscription, then you can assign up to 16 queues for each vNIC, for a total of 64 queues total.
  * For an N2D VM with 224 vCPUs and 8 NICs:

    * If you use the virtIO driver for the NICs, then you can assign a maximum of 224 queues across the 8 NICs, with a maximum queue count of 32 for any vNIC. For example, you could have 32 queues on 6 of the NICs, and then 16 queues on the remaining 2 NICs.
    * If you use the gVNIC driver for the NICs, then you can use the maximum queue count of 16 for all 8 NICs. The maximum sum of the queue counts is 128.



It's also possible to assign a custom queue count for _only some vNICs_ , letting Compute Engine assign queues to the remaining vNICs. The number of queues that you can assign per vNIC is still subject to the rules mentioned previously. You can model the feasibility of your configuration, and the number of queues that Compute Engine assigns to the remaining vNICs, with this process:

  1. Calculate the sum of queues for the vNICs that have a custom queue assignment.

  2. Subtract the sum of custom-assigned queues from the number of vCPUs. If the difference is less than the number of remaining vNICs for which Compute Engine must assign queues, then Compute Engine returns an error because each vNIC must have at least one queue.

  3. Divide the difference from the previous step by the number of vNICs without a custom queue count and discard any remainder:
         
         [(number of vCPUs - sum of assigned queues)/(number of remaining vNICs)]
         

This calculation always results in a whole number (not a fraction) that is at least equal to one because each vNIC must have at least one queue.

  4. Compute Engine assigns each remaining vNIC a queue count as follows:

     * If the calculated number is less than the maximum number of queues per vNIC, then the queue count is set to the calculated number.
     * If the calculated number is greater than the maximum number of queues per vNIC, then the queue count for the vNIC is set to the maximum number of queues.



**Example**

Assume you have a VM with 20 vCPUs and 6 NICs, and that you assigned 5 queues to `nic0`, 6 queues to `nic1`, 4 queues to `nic2`, and let Compute Engine assign queue counts for `nic3`, `nic4`, and `nic5`.

  1. The sum of the custom-assigned queues is `5 + 6 + 4 = 15`.

  2. Compute Engine has `20 - 15 = 5` queues left to assign to the remaining three vNICs (`nic3`, `nic4`, `nic5`). The difference (`5`) is greater than the number of vNICs that don't have a custom queue count (`3`).

  3. The difference of `5` is divided by `3`, and the remainder discarded. This leaves a value of `1`.

  4. Because the calculated number (`1`) is less than the maximum number of queues per vNIC, the queue count for the remaining vNICs is set to `1`.




### Configure custom queue counts

To create a compute instance that uses a custom queue count for one or more NICs or vNICs, complete the following steps.

In the following code examples, the VM instance is created with the network interface type set to `GVNIC` and per VM Tier_1 networking performance enabled. You can use these code examples to specify the maximum queue counts and queue oversubscription that is available for the supported machine types.

###  gcloud 

  1. If you don't already have a [VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) with a subnet for each vNIC interface you plan to configure, create them.
  2. Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create the compute instance. Repeat the `--network-interface` flag for each vNIC that you want to configure for the instance, and include the `queue-count` option.


    
    
        gcloud compute instances create INSTANCE_NAME \
            --zone=ZONE \
            --machine-type=MACHINE_TYPE \
            --network-performance-configs=total-egress-bandwidth-tier=TIER_1  \
            --network-interface=network=NETWORK_NAME_1,subnet=SUBNET_1,nic-type=GVNIC,queue-count=QUEUE_SIZE_1 \
            --network-interface=network=NETWORK_NAME_2,subnet=SUBNET_2,nic-type=GVNIC,queue-count=QUEUE_SIZE_2
    

Replace the following:

  * `INSTANCE_NAME`: a [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new compute instance
  * `ZONE`: the zone to create the instance in
  * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) of the instance. To oversubscribe the queue count, you must use a machine type from the N2, N2D, C2 or C2D machine series that uses gVNIC and Tier_1 networking.
  * `NETWORK_NAME`: the name of the network created previously
  * `SUBNET_*`: the name of one of the subnets created previously
  * `QUEUE_SIZE`: the number of queues for the vNIC, subject to the rules discussed in Custom queue allocation.



###  Terraform 

  1. If you don't already have a [VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) with a subnet for each vNIC interface you plan to configure, create them.
  2. Create a compute instance with specific queue counts for vNICs using the [`google_compute_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance). Repeat the `--network-interface` parameter for each vNIC you want to configure for the compute instance, and include the `queue-count` parameter.
         
         # Queue oversubscription instance
         resource "google_compute_instance" "INSTANCE_NAME" {
         project      = "PROJECT_ID"
         boot_disk {
           auto_delete = true
           device_name = "DEVICE_NAME"
           initialize_params {
              image="IMAGE_NAME"
              size = DISK_SIZE
              type = "DISK_TYPE"
           }
         }
         machine_type = "MACHINE_TYPE"
         name         = "INSTANCE_NAME"
         zone         = "ZONE"
         
         network_performance_config {
             total_egress_bandwidth_tier = "TIER_1"
         }
         
         network_interface {
             nic_type = "GVNIC"
             queue_count = QUEUE_COUNT_1
             subnetwork_project = "PROJECT_ID"
             subnetwork = "SUBNET_1"
          }
         
         network_interface {
             nic_type = "GVNIC"
             queue_count = QUEUE_COUNT_2
             subnetwork_project = "PROJECT_ID"
             subnetwork = "SUBNET_2"
         }
         
         network_interface {
             nic_type = "GVNIC"
             queue_count = QUEUE_COUNT_3
             subnetwork_project = "PROJECT_ID"
             subnetwork = "SUBNET_3""
         }
         
         network_interface {
             nic_type = "GVNIC"
             queue_count = QUEUE_COUNT_4
             subnetwork_project = "PROJECT_ID"
             subnetwork = "SUBNET_4""
         }
         
         }
         
         




Replace the following:

  * `INSTANCE_NAME`: a [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new compute instance
  * `PROJECT_ID`: ID of the project to create the instance in. Unless you are using a Shared VPC network, the project that you specify must be the same one in which all the subnets and networks were created.
  * `DEVICE_NAME`: The name to associate with the boot disk in the guest OS
  * `IMAGE_NAME`: the name of an image, for example, `"projects/debian-cloud/global/images/debian-12-bookworm-v20250311"`.
  * `DISK_SIZE`: the size of the boot disk, in GiB
  * `DISK_TYPE`: the type of disk to use for the boot disk, for example, `pd-standard`
  * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) of the instance. To oversubscribe the queue count, you must use a machine type from the N2, N2D, C2 or C2D machine series that uses gVNIC and Tier_1 networking.
  * `ZONE`: the zone to create the instance in
  * `QUEUE_COUNT`: the number of queues for the vNIC, subject to the rules discussed in Custom queue allocation.
  * `SUBNET_*`: the name of the subnet that the network interface connects to



###  REST 

  1. If you don't already have a [VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) with a subnet for each vNIC interface you plan to configure, create them.
  2. Create a compute instance with specific queue counts for vNICs using the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). You can repeat the `networkInterfaces` property to configure multiple network interfaces.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
         {
         "name": "INSTANCE_NAME",
         "machineType": "machineTypes/MACHINE_TYPE",
         "networkPerformanceConfig": {
             "totalEgressBandwidthTier": TIER_1
         },
         "networkInterfaces": [
             {
               "nicType": gVNIC,
               "subnetwork":"regions/region/subnetworks/SUBNET_1",
               "queueCount": "QUEUE_COUNT_1"
             } ],
         "networkInterfaces": [
             {
               "nicType": gVNIC,
               "subnetwork":"regions/region/subnetworks/SUBNET_2",
               "queueCount": "QUEUE_COUNT_2"
             } ]
         }
         

Replace the following:

     * `PROJECT_ID`: ID of the project to create the compute instance in
     * `ZONE`: zone to create the compute instance in
     * `INSTANCE_NAME`: [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new compute instance
     * `MACHINE_TYPE`: machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type), for the new compute instance. To oversubscribe the queue count, you must use a machine type from the N2, N2D, C2 or C2D machine series that uses gVNIC and Tier_1 networking.
     * `SUBNET_*`: the name of the subnet that the network interface connects to
     * `QUEUE_COUNT`: Number of queues for the vNIC, subject to the rules discussed in Custom queue allocation.



### Queue allocations and changing the machine type

Compute instances are created with a [default queue allocation](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx-equations), or you can assign a [custom queue count](https://docs.cloud.google.com/compute/docs/network-bandwidth#assign-rx-tx-queues) to each virtual network interface card (vNIC) when you create a new compute instance by using the Compute Engine API. The default or custom vNIC queue assignments are only set when creating a compute instance. If your instance has vNICs that use default queue counts, you can [change its machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance#changing_a_machine_type). If the machine type that you are changing to has a different number of vCPUs, the default queue counts for your instance are recalculated based on the new machine type.

If your VM has vNICs which use custom, non-default queue counts, then you can change the machine type by using the Google Cloud CLI or Compute Engine API to [update the instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties). The conversion succeeds if the resulting VM supports the same queue count per vNIC as the original instance. For VMs that use the VirtIO-Net interface and have a custom queue count that is higher than 16 per vNIC, you can't change the machine type to a third generation or later machine type, because they use only gVNIC. Instead, you can migrate your VM to a third generation or later machine type by following the instructions in [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).

## What's next

  * [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
  * [Configure per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for a compute instance.
  * Learn about [TCP optimization for network performance](https://docs.cloud.google.com/compute/docs/networking/tcp-optimization-for-network-performance-in-gcp-and-hybrid)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
