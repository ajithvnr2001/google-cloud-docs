---
url: https://docs.cloud.google.com/nat/docs/ports-and-addresses/
title: IP addresses and ports \u00a0|\u00a0 Cloud NAT \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:40.698918+00:00
---

# IP addresses and ports  |  Cloud NAT  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/ports-and-addresses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IP addresses and ports

This page describes how Cloud NAT gateways use IP addresses and how they allocate source ports to Compute Engine virtual machine (VM) instances and Google Kubernetes Engine (GKE) nodes that use the gateways.

Before reviewing this information, familiarize yourself with the [Cloud NAT overview](https://docs.cloud.google.com/nat/docs/overview).

## Public NAT IP addresses

A _Public NAT IP address_ is a regional external IP address that is routable on the internet. A VM without an external IP address, which is in a subnetwork (subnet) served by a Public NAT gateway, uses a Public NAT IP address when it sends packets to a destination on the internet.

To assign network address translation (NAT) IP addresses to a Public NAT gateway, use one of the following methods:

  * **Automatic NAT IP address allocation.** When you select this method, or choose Google Cloud defaults, Public NAT automatically adds regional external IP addresses to your gateway based on the following:

    * The network tier that you select
    * The number of VMs that use the gateway
    * The number of ports that are reserved for each VM

Public NAT also automatically removes a NAT IP address when it no longer needs any source ports on that NAT IP address.

The following are the characteristics of automatic NAT IP address allocation:

    * When a Public NAT gateway adds a NAT IP address, it creates a static (reserved) regional external IP address in the network tier that you have selected at the time of configuring the gateway. For example, if you have selected Premium Tier, then the Public NAT gateway creates the IP address in that tier. The supported network tiers are Premium Tier (default option) and Standard Tier.

The automatically added NAT IP addresses can be viewed in the [list of static external IP addresses](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#list_ip). These addresses don't count toward [per-project quotas](https://docs.cloud.google.com/vpc/docs/quota#per_project).

**Note:** When you use the automatic Public NAT IP address allocation method, Cloud NAT logging does not log the reservation of a static external IP address as an event. So, you cannot monitor the scaling of automatically allocated Public NAT IP addresses.
    * If you change the network tier of a Public NAT gateway, the existing IP addresses for that gateway are released, and a new set of IP addresses from the selected tier is assigned.
    * With automatic allocation, you cannot predict the next IP address that is allocated. If you depend on knowing the set of possible NAT IP addresses ahead of time (for example, to create an allowlist), you should use manual NAT IP address assignment instead.
    * When automatically added NAT IP addresses are no longer in use, they are removed. However, Public NAT only deallocates an address when the last VM assigned to the address is no longer using any ports. As such, when the number of VMs using Public NAT goes down, you might not see a reduction in IP . The reason is that Cloud NAT does not dynamically reallocate VMs from one IP address to another because reallocation would disrupt established connections. As long as at least one VM is using an IP address, the IP address stays active and new VMs can be assigned to it.

If you want to be able to manually reallocate VMs from one IP address to another in order to minimize IP address usage, use manual NAT IP address assignments. Manual NAT IP address assignment allows draining of Public NAT IP addresses.

    * If you switch to manual NAT IP address assignment later, the automatically reserved regional external IP addresses are deleted. For more information, see Switching assignment method.

  * **Manual NAT IP address assignment.** When you select this option, you create and manually assign static (reserved) regional external IP addresses to your Public NAT gateway. You can manually assign IP addresses either from Premium Tier, from Standard Tier, or from both, subject to conditions.

    * You can increase or decrease the number of manually assigned NAT IP addresses by editing the Cloud NAT gateway.
    * When using manual NAT IP address assignment, you must calculate the number of regional external IP addresses that you need for the Public NAT gateway. If your gateway runs out of NAT IP addresses, Public NAT drops packets. Dropped packets are logged when you use [Cloud NAT logging](https://docs.cloud.google.com/nat/docs/monitoring) to turn on error logging.
    * For example calculations, see the port reservation example.



For the maximum number of automatically allocated or manually assigned NAT IP addresses, see [Cloud NAT limits](https://docs.cloud.google.com/nat/quota#limits).

### Assign a mix of Premium Tier and Standard Tier IP addresses manually

When you create a Public NAT gateway with the manual NAT IP address assignment method, you can assign a mix of Premium Tier and Standard Tier IP addresses as long as the IP addresses of different network tiers do not belong to the same rule (including the default rule).

Inside a rule (including the default rule), all IP addresses assigned to active ranges _must_ be of the same network tier. If you try to use IP addresses of different tiers as part of the same rule, Google Cloud rejects the configuration.

### Switch assignment method

You can switch a Public NAT gateway from automatic NAT IP address allocation to manual NAT IP address assignment; however, the NAT IP addresses cannot be preserved. Even though automatically allocated NAT IP addresses are static, they _cannot_ be moved to a manual NAT IP address assignment. For example, you cannot start using a Public NAT gateway with automatically allocated NAT IP addresses and later use the same addresses when you switch to manually assigned NAT IP addresses.

The set of regional external IP addresses that Public NAT uses for automatic NAT IP address allocation is different from the set of regional external IP addresses that you can manually choose.

**Note:** Switching the assignment method is disruptive, and it breaks all active NAT connections.

### Drain Public NAT IP addresses

When you configure a Public NAT gateway with manual NAT IP address assignment, you can choose what happens when you need to reduce the number of NAT IP addresses that the gateway uses:

  * If you remove a manually assigned NAT IP address, established NAT connections are broken immediately.

  * You can choose to _drain_ a manually assigned NAT IP address instead. Draining instructs the Public NAT gateway to stop using the NAT IP address for new connections, but continue using it for established connections. Established connections are permitted to close normally instead of being abruptly terminated. To drain an IP address that is associated with a Public NAT gateway that does not use NAT rules, see [Drain external IP addresses associated with NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#draining). To drain an IP address that is associated with a NAT gateway that uses NAT rules, see [Update NAT rules](https://docs.cloud.google.com/nat/docs/using-nat-rules#update_nat_rules).


**Note:** You cannot add a new, manually assigned NAT IP address without marking it as immediately eligible for use by the Public NAT gateway. Draining is only applicable when removing manually assigned NAT IP addresses.

## Private NAT IP addresses

A _Private NAT address_ is a regional internal IPv4 address that comes from the primary IPv4 address range of a _Private NAT subnet_ located in the same region and VPC network as a Private NAT gateway. A Private NAT IP address is not routable on the internet. IP addresses from primary IPv4 address ranges of Private NAT subnets can be used only by Private NAT gateways. To create a Private NAT subnet, [add an IPv4 only subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets) using the Google Cloud CLI and the `--purpose=PRIVATE_NAT` flag.

After you configure a Private NAT gateway to provide NAT services for a subnet in a VPC network, VMs with network interfaces in that subnet can send packets to resources located in other networks such as VPC networks attached to the same Network Connectivity Center hub as the network that hosts the Private NAT gateway or networks outside of Google Cloud that are connected to Google Cloud through Cloud Interconnect or Cloud VPN. On egress, Google Cloud changes the source IP address to an IP address from the Private NAT subnet that is associated with the gateway.

The following are characteristics of Private NAT IP addresses:

  * You cannot automatically assign Private NAT IP addresses to a Private NAT gateway. Instead, when you create a rule in a Private NAT gateway, you manually specify the Private NAT subnet or subnets. Private NAT subnets must be located in the same VPC network and region as the gateway. The gateway uses IP addresses only from the primary IPv4 address ranges of the Private NAT subnets.
  * To determine how many NAT IP addresses each Private NAT subnet can provide, use the following formula: `2(32 - PREFIX_LENGTH) - 4`, where `PREFIX_LENGTH` is the subnet mask length of the Private NAT subnet's primary IPv4 address range. [Four IP addresses are unusable](https://docs.cloud.google.com/vpc/docs/subnets#unusable-ip-addresses-in-every-subnet) in every subnet's primary IPv4 address range.



## Ports

Each NAT IP address on a Cloud NAT gateway (both Public NAT and Private NAT) offers 64,512 TCP source ports and 64,512 UDP source ports. TCP and UDP each support 65,536 ports per IP address. Cloud NAT doesn't use the well-known (privileged) ports (0 through 1,023).

When a Cloud NAT gateway performs source network address translation (SNAT) on a packet sent by a VM, it changes the packet's NAT source IP address and source port.

When you create a Cloud NAT gateway, you choose whether to use static port allocation or dynamic port allocation. You can change the port allocation method after creating the gateway. For information about how changing the port allocation method for a Cloud NAT gateway affects established connections, see Switch port allocation method.

If you have manually assigned multiple static (reserved) regional external IP addresses to your Public NAT gateway, a single VM that uses the gateway can get the required ports from any of the assigned NAT IP addresses—even from multiple NAT IP addresses at the same time.

**Note:** NAT IP address and port mapping may change over time based on the VM's usage. So, you shouldn't create network configurations based on the current mapping that you see in your NAT configuration.

### Static port allocation

When you configure static port allocation, you specify a _minimum number of ports per VM instance_. If you don't specify the minimum number of ports per VM, Google Cloud uses the default value.

Static port allocation is enabled, by default, for Public NAT. Private NAT, on the other hand, uses dynamic port allocation by default.

Because all VMs are allocated the same number of ports, static port allocation works best if all VMs have similar egress usage. When static port allocation is configured, the number of ports allocated to each VM is fixed and doesn't change if some VMs use more ports than others or if a VM exhausts all its ports. If egress usage varies, consider configuring dynamic port allocation.

If you want to configure endpoint-independent mapping (EIM) on your Public NAT gateway, you must use static port allocation. Endpoint-independent mapping is not available for Private NAT gateways.

### Dynamic port allocation

When you configure dynamic port allocation, you specify a _minimum number of ports per VM instance_ and a _maximum number of ports per VM instance_.

Dynamic port allocation is enabled, by default, for Private NAT. Public NAT uses static port allocation by default.

Configuring dynamic port allocation lets the same Cloud NAT gateway allocate different numbers of ports per VM, based on the VM's usage. Initially, a VM is allocated the minimum number of ports per VM instance. If a VM is close to exhausting all the ports that are allocated to it, the number of ports assigned to the VM is doubled. The VM can repeatedly request more ports up to the maximum number of ports per VM instance. When the port usage significantly decreases, the ports are deallocated and can be allocated to other VMs that use the same NAT gateway.

Dynamic port allocation has the following benefits:

  * The number of ports that are allocated but not being used are reduced.

  * The NAT gateway monitors each VM's port usage and modifies the number of ports allocated to each VM, based on need. You don't need to monitor the port usage or adjust the NAT gateway configuration.




Before using dynamic port allocation, consider the following:

  * If endpoint-independent mapping is enabled on the Cloud NAT gateway, you cannot configure dynamic port allocation. If you need endpoint-independent mapping, use static port allocation.

  * While additional ports are being allocated to VMs, you might see connection timeouts or latency. For strategies to help prevent connections drops, see [Reduce dropped connections with dynamic port allocation](https://docs.cloud.google.com/nat/docs/troubleshooting#dpa-drops).




### Switch port allocation method

You can switch between static port allocation and dynamic port allocation for a given Cloud NAT gateway.

Switching to the dynamic port allocation method breaks the existing NAT connections only if either of the following conditions is met:

  * You set the maximum number of ports per VM to a value that is less than the minimum number of ports per VM that is specified in the previous NAT configuration (with static port allocation).

If in the previous configuration, the minimum number of ports per VM was set to more than `1024`, and if you specify `1024` as the maximum number of ports per VM in the new configuration, then the existing connections break because the first condition takes precedence.

  * You set the maximum number of ports per VM to a value that is less than `1024`.




Unless either of the preceding conditions is met, switching to dynamic port allocation _does not_ break existing NAT connections.

Disabling dynamic port allocation and switching to static port allocation is disruptive, and it breaks all active NAT connections.

### Port reservation procedure

Cloud NAT uses the following procedure to provision NAT source IP address and source port tuples for each VM that the Cloud NAT (both Public NAT and Private NAT) gateway serves.

**Note:** When you use a Cloud NAT gateway to provide NAT services for a [private Google Kubernetes Engine cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept), the NAT source IP address and source port tuples are assigned to the node VM, shared by all Pods on the node.

  1. **Cloud NAT determines the VM IP addresses for which NAT should be performed.** Cloud NAT can perform NAT for internal IPv4 addresses (NAT44) and internal and external IPv6 addresses (NAT64).

For NAT44, the VM internal IP addresses are determined by the [subnet IP address ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges) that the gateway is configured to serve:

     * If the Public NAT gateway is configured to perform NAT for the primary IPv4 address range of the subnet used by the VM's network interface, the gateway performs NAT for _both_ the VM's primary internal IPv4 address and any of the VM's [alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip) from the subnet's primary IPv4 address range.

     * If the Public NAT gateway is configured to perform NAT for a secondary IPv4 address range of the subnet used by the VM's network interface, the gateway performs NAT for any alias IP ranges from that subnet's secondary IPv4 address range.

     * A Cloud NAT gateway for Private NAT automatically performs NAT for all IPv4 address ranges within the VM's subnet.

For NAT64, the Cloud NAT gateway performs NAT for internal and external IPv6 addresses.

  2. **Cloud NAT adjusts the minimum ports per VM instance if necessary.** If static port allocation is configured, and the gateway performs NAT for alias IP ranges that have more than one address (netmask smaller than `/32`), Cloud NAT adjusts the minimum ports per VM to be the maximum of these two values:

     * The _minimum ports per VM instance_ that you specify

     * The number 1,024

In all other situations, including when dynamic port allocation is configured, the Cloud NAT gateway proceeds to the next step by using the specified minimum ports per VM instance as input. If you do not specify the minimum ports per VM instance, then the default value is used: `64` for static port allocation and `32` for dynamic port allocation.

  3. **Cloud NAT reserves NAT source IP address and source port tuples for each VM.** The Cloud NAT gateway uses the given or adjusted minimum ports per VM instance from the previous step to calculate the number of _NAT source IP address and source port tuples_ to assign to the VM.

For Public NAT, Google Cloud allocates NAT source IP address and source port tuples using multiples of powers of two, so the number of NAT source IP address and source port tuples is greater than or equal to the minimum ports per VM instance that you specify.

For Private NAT, Google Cloud allocates twice the number of required minimum ports per VM for reliability. Ensure that the subnet from which Private NAT assigns IP addresses and ports is sized appropriately.

     * If the Cloud NAT gateway uses two or more NAT IP addresses, then it's possible for the NAT source IP address and source port tuples to span more than one NAT IP address. A single NAT IP address might not have enough available source ports to accommodate the number of NAT source IP address and source port tuples that a VM needs.

     * The Cloud NAT gateway allocates source IP address and source port tuples to each VM.

       * If you have configured static port allocation, the number of source IP addresses and source port tuples is fixed. Each VM can use no more than its allocated number of source IP address and source port tuples, even during traffic bursts.

       * If you have configured dynamic port allocation, the number of source IP addresses and source port tuples can change based on demand. If a VM is close to exhausting its current port allocation, the Cloud NAT allocates additional ports, up to the specified _maximum ports per VM instance_ value. After the VM's port usage reduces below a threshold, the ports are released and can be allocated to other VMs.




### Increase ports per VM

If you have configured a Cloud NAT gateway with static port allocation, when you increase the minimum ports per VM on the gateway, there is no interruption to traffic.

If you have configured a Cloud NAT gateway with dynamic port allocation, then increasing the minimum, maximum, or both number of ports per VM _does not_ break the existing NAT connections or disrupt traffic flowing through the NAT gateway.

Consider the following when you increase the number of ports ver VM:

  * When using Public NAT with manual NAT IP address assignment, you must calculate the number of NAT source IP addresses that you need. Before increasing the minimum ports per VM, assign at least that many NAT IP addresses to the Public NAT gateway.

  * When using Public NAT with automatic NAT IP address allocation, increasing the minimum number of ports per VM causes the Public NAT gateway to acquire and allocate more regional external IP addresses automatically.

  * When using Private NAT, ensure that the subnet from which the gateway allocates IP addresses has an adequate number of IP addresses.




### Reduce ports per VM

If you have configured a Cloud NAT gateway with static port allocation, and you reduce the minimum ports per VM on the gateway, there is no connection draining. Established NAT connections are broken immediately and clients must establish new TCP connections.

If you have configured a Cloud NAT gateway with dynamic port allocation, then the following statements are true:

  * Reducing the minimum number of ports per VM _does not_ break the existing NAT connections or disrupt traffic flowing through the NAT gateway.
  * Reducing the maximum number of ports per VM _breaks_ all existing NAT connections immediately, and the number of allocated ports for all VMs is temporarily reset to the value specified for the minimum number of ports per VM.



## Ports and connections

The number of NAT source IP address and source port tuples that a Cloud NAT gateway reserves for a VM restricts the number of connections that the VM can make to a unique destination:

  * A _unique destination_ means a unique 3-tuple consisting of a destination IP address, a destination port, and an IP protocol (such as TCP or UDP).

  * A _connection_ means a unique 5-tuple consisting of the NAT source IP address and source port tuple combined with a unique destination 3-tuple. Because the UDP protocol is connectionless, the concept of connection is reduced to a 5-tuple associated with a unique UDP datagram.




Suppose that a Cloud NAT gateway calculates 1,024 for the fixed number of ports for a VM by following the port reservation procedure. The Cloud NAT gateway reserves 1,024 unique combinations of NAT source IP address and source port tuples for the VM. The Cloud NAT gateway can process 1,024 simultaneous connections to _each_ unique destination 3-tuple. However, Cloud NAT considers closed connections to be [unusable](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts) for the duration of the TCP TIME_WAIT timeout, which can affect the number of connections in use at a time.

Examples:

  * The gateway supports 1,024 simultaneous connections to destination IP address `203.0.113.99` on port `80` using the TCP protocol.

  * The gateway supports _another_ 1,024 simultaneous connections to that same destination IP address on port `443`, also using the TCP protocol.

  * The gateway supports _another_ 1,024 simultaneous connections to a different destination IP address on port `80`, also using the TCP protocol.




### Simultaneous port reuse and endpoint-independent mapping

**Note:** The information in this section only applies if you have [endpoint-independent mapping](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#set-mapping) enabled in Public NAT.

As long as _at least one piece of information_ in the destination 3-tuple changes—the destination IP address, the destination port, the protocol—the same NAT source IP address and source port tuple can be simultaneously used for many different connections.

Public NAT uses _endpoint-independent mapping_ , as defined in [Section 2.3 of RFC 5128](https://tools.ietf.org/html/rfc5128#section-2.3). As a result, the number of simultaneous connections that a client VM can make to a unique destination 3-tuple might be reduced if Public NAT assigns the same NAT source IP address and source port tuple to more than one internal IP address and ephemeral source port of a client VM. The chances of this happening increase if the client VM has a large number of internal source IP addresses and makes a large number of connections to the same destination 3-tuple. The first time a client VM sends a packet from an internal IP address and ephemeral source port, Public NAT creates a many-to-one endpoint-independent mapping between the following:

  * The internal IP address and ephemeral source port tuple
  * A unique NAT source IP address and source port tuple



For example, when a client VM sends a packet from its internal IP address `10.0.0.2` by using ephemeral source port `10001`, Public NAT assigns `10.0.0.2:10001`. This NAT source IP address and source port tuple is then used for _all subsequent connections from`10.0.0.2:10001` to any destination 3-tuple_.

If the same VM uses a different ephemeral source port to send a packet, for example, `10.0.0.2:20002`, Public NAT also assigns a NAT source IP address and source port tuple for all subsequent connections from `10.0.0.2:20002` to any destination 3-tuple. It's possible that Public NAT could assign the same NAT source IP address and source port tuple to _both_ of these internal IP address and ephemeral source port tuples causing an _endpoint independent conflict_ in certain situations.

For a more detailed example, see endpoint-independent mapping conflict example.

### Reduce endpoint independent conflicts

**Note:** The information in this section only applies if you have [endpoint-independent mapping](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#set-mapping) enabled in Public NAT.

You can make configuration changes to reduce endpoint independent conflicts. For more information, see [Packets dropped with reason endpoint independent conflict](https://docs.cloud.google.com/nat/docs/troubleshooting#endpoint-independent-conflict).

### Delay for TCP source port reuse

When a VM that uses a Cloud NAT gateway closes a TCP connection, two independent delays take effect:

  * **The Cloud NAT`TIME_WAIT` timeout**: Cloud NAT enforces a delay before it can map a new connection to the same post-NAT 5-tuple (NAT source IP address, NAT source port, destination IP address, destination port, and protocol). This delay is controlled by the [TCP TIME_WAIT Timeout](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts) setting. The default value for the Cloud NAT `TIME_WAIT` is either 30 seconds or 120 seconds, depending on when you created the gateway. For information about how to configure a custom Cloud NAT `TIME_WAIT` timeout value, see [Change NAT timeouts](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#change-conn-timeouts).

  * **The VM's`TIME_WAIT` timeout**: the operating system of the client VM has its own `TIME_WAIT`, which represents the delay before the client VM can create a new connection using the same pre-NAT 5-tuple (original source IP address, source port, destination IP address, destination port, and protocol). Linux systems use a default `TIME_WAIT` of 60 seconds, and Windows systems use a default `TIME_WAIT` of 240 seconds.




The client VM's `TIME_WAIT` can be greater than or equal to the Cloud NAT `TIME_WAIT`. Lowering the Cloud NAT `TIME_WAIT` timeout doesn't require a corresponding reduction in the client VM's `TIME_WAIT`.

A shorter Cloud NAT `TIME_WAIT` timeout is useful for client VMs that need to rapidly open and close TCP connections to the same destination 3-tuple (destination IP address, destination port, and protocol) because the gateway can map a new connection to a previously used post-NAT 5-tuple more quickly.

### Source ports and security

If you depend on source port randomization as a security measure, you need to consider the following:

  * Increase the minimum number of ports per VM instance so that the port reservation procedure assigns the VM more NAT source IP address and source port tuples. Increasing the minimum number of ports per VM instance assigns a range of ports randomly to each VM; however, the source port chosen from that range is sequential.

  * [Assign an external IP address to the VM](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#IP_assign) instead of using Public NAT.




## Examples

The following examples demonstrate how Cloud NAT reserves NAT source IP addresses and source ports for a VM and how it performs NAT for packets sent to the internet.

### Port reservation

The following examples demonstrate applications of the port reservation procedure.

Suppose you're configuring a Public NAT gateway to provide NAT for the primary IP address range of a subnet, and the VMs that use that subnet do not have any alias IP ranges from the subnet's primary IP address range. Round down the result of any division operation to the closest integer. ⌊⌋ is [the floor (greatest integer) function](https://wikipedia.org/wiki/Floor_and_ceiling_functions), meaning discard any fractional result of division.

  * If you configure the Public NAT gateway with a single NAT IP address using manual assignment, and you set the minimum number of ports per VM instance to 64, the gateway can provide NAT services for up to 1,008 VMs:

⌊(1 NAT IP address) × (64,512 ports per address) / (64 ports per VM)⌋ = 1,008 VMs

  * If you need to support more than 1,008 VMs, you can assign a second NAT IP address to the Cloud NAT gateway. With two NAT IP addresses, keeping the minimum number of ports per VM at 64, you can support 2,016 VMs:

⌊(2 NAT IP addresses) × (64,512 ports per address) / (64 ports per VM)⌋ = 2,016 VMs

  * If you set the minimum number of ports per VM to 4,096, each NAT IP address can support 15 VMs. This calculation is rounded down to the closest integer:

⌊(1 NAT IP addresses) × (64,512 ports per address) / (4,096 ports per VM)⌋ = 15 VMs




Suppose you're configuring a Private NAT gateway to provide NAT for all IP addresses of a subnet:

  * The minimum subnet size that you can create is eight IPv4 addresses, which is a subnet mask of `/29`. If you configure a Private NAT gateway with a NAT subnet of minimum size, and you set the minimum number of ports per VM instance to 64, the gateway can provide NAT services for up to 2,016 VMs:

⌊(2(32-29) \- 4) NAT IP addresses × (64,512 ports per address) / (64 ports per VM × 2)⌋ = 2,016 VMs

**Note:** There are [four unusable IP addresses](https://docs.cloud.google.com/vpc/docs/subnets#unusable_ip_addresses_in_every_subnet) in a NAT subnet, so the number of available IP addresses is 2(32 \- `PREFIX_LENGTH`) - 4. 

Google Cloud allocates double the number of required ports per VM for reliability.

In the previous example, if you set the minimum number of ports per VM instance to 1024, the gateway can provide NAT services for up to 126 VMs:

⌊(2(32-29) \- 4) NAT IP addresses × (64,512 ports per address) / (1024 ports per VM × 2)⌋ = 126 VMs

  * If you configure a Private NAT gateway with a NAT subnet mask of `/28`, and you set the minimum number of ports per VM instance to 64, the gateway can provide NAT services for up to 6,048 VMs:

⌊(2(32-28) \- 4) NAT IP addresses × (64,512 ports per address) / (64 ports per VM × 2)⌋ = 6,048 VMs




### Endpoint-independent mapping conflict

**Note:** The information in this section only applies if you have [endpoint-independent mapping](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#set-mapping) enabled in Public NAT.

The following example illustrates how endpoint-independent mapping might reduce the number of _simultaneous connections_ from a client VM _to the same destination 3-tuple_ , even when there is a sufficient number of free NAT source IP address and source port tuples available for the client VM.

Suppose you've configured a Public NAT gateway to provide NAT for the primary IP address range of a subnet. You've created a client VM with one network interface whose primary internal IP address is `10.0.0.2` in that subnet. The example VM does not have an external IP address assigned to its network interface.

  1. The VM opens a connection with these characteristics:

     * Source internal IP address and port: `10.0.0.2:10001`
     * Destination 3-tuple: `203.0.113.1:80` using TCP
     * Public NAT uses the following NAT source IP address and source port tuple: `192.0.2.10:30009`
  2. The VM opens a second connection with these characteristics:

     * Source internal IP address and port: `10.0.0.2:10002`
     * Destination 3-tuple: `203.0.113.2:80` using TCP
     * Public NAT might choose to use _the same_ NAT source IP address and source port tuple,`192.0.2.10:30009`, for this connection as well. Using the same NAT source IP address and source port tuple for a different client IP address and ephemeral source port is possible.
  3. While both the first and the second connections are active, Public NAT cannot open a third TCP connection with these characteristics:

     * Same source internal IP address and port as the first connection: `10.0.0.2:10001`
     * Same destination 3-tuple as the second connection: `203.0.113.2:80` using TCP

This third connection attempt is dropped with an endpoint independent conflict error because the endpoint-independent mapping established by the first connection mandates that all connections from `10.0.0.2:10001` must use the same NAT source IP address and source port tuple, `192.0.2.10:30009`. However, `192.0.2.10:30009` is already being used by the second TCP connection to `203.0.113.2:80`.

  4. To dispel ambiguity, a subsequent connection attempt in this example is successful as long as one of the following is true:

     * **The first TCP connection has been closed.** Closing the connection removes the endpoint-independent mapping between `10.0.0.2:10001` and `192.0.2.10:30009`, so the third connection can be mapped to a different NAT source IP address and source port tuple to communicate with `203.0.113.2:80` using TCP.
     * **The second TCP connection has been closed.** Closing the connection frees up `10.0.0.2:10001` to use the NAT source IP address and source port `192.0.2.10:30009` to communicate with `203.0.113.2:80` using TCP.
     * **The third connection attempt selects a different ephemeral (internal) source port.** In this example, an endpoint-independent mapping established a many-to-one mapping for internal NAT source IP addresses and source ports `10.0.0.2:10001` and `10.0.0.2:10002` to use `192.0.2.10:30009` when communicating with `203.0.113.2:80` using TCP. If the third connection attempt uses an ephemeral source port different from both `10001` and `10002`, there's a chance that a different NAT source IP address and source port can be used to communicate with `203.0.113.2:80` using TCP.
     * **Toggling endpoint independence off**. The toggling allows the new connection from `10.0.0.2:10001` to not need to use `192.0.2.10:30009`, allowing it to use a different NAT source IP address and port.



For techniques that you can use to avoid conflicts, see Reducing endpoint independent conflicts.

## What's next

  * [Set up and manage network address translation with Public NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation)
  * [Set up and manage network address translation with Private NAT](https://docs.cloud.google.com/nat/docs/set-up-private-nat)
  * [Use Public NAT with Compute Engine](https://docs.cloud.google.com/nat/docs/gce-example) (tutorial)
  * [Use Public NAT with GKE](https://docs.cloud.google.com/nat/docs/gke-example) (tutorial)
  * [Troubleshoot configuration](https://docs.cloud.google.com/nat/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
