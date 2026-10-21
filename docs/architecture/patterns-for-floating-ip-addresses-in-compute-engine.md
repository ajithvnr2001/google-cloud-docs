---
url: https://docs.cloud.google.com/architecture/patterns-for-floating-ip-addresses-in-compute-engine/
title: Patterns for using floating IP addresses in Compute Engine \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:52:51.038430+00:00
---

# Patterns for using floating IP addresses in Compute Engine  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/patterns-for-floating-ip-addresses-in-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Patterns for using floating IP addresses in Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-02-03 UTC

This document describes how to use floating IP address implementation patterns when migrating applications to Compute Engine from an on-premises network environment. This document is aimed at network engineers, system administrators, and operations engineers who are migrating applications to Google Cloud.

Also referred to as shared or virtual IP addresses, floating IP addresses are often used to make on-premises network environments highly available. Using floating IP addresses, you can pass an IP address between multiple identically configured physical or virtual servers. This practice allows for failover or for upgrading production software. However, you can't directly implement floating IP addresses in a Compute Engine environment without changing the architecture to one of the patterns described in this document.

The [GitHub repository](https://github.com/GoogleCloudPlatform/solutions-floating-ip-patterns-terraform) that accompanies this document includes sample deployments for each pattern that you can automatically deploy using [Terraform](https://docs.cloud.google.com/docs/terraform).

## Floating IP addresses in on-premises environments

Floating IP addresses are commonly used in on-premises environments. Example use cases are as follows:

  * Highly available physical appliances, such as a set of firewalls or load balancers, often use floating IP addresses for failovers.
  * Servers that require high availability typically use floating IP addresses—for example, relational databases using a primary server and a backup server. A common example, Microsoft SQL Server, uses [AlwaysOn Availability Groups](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server). To learn how to implement these patterns on Google Cloud, see [Configuring SQL Server AlwaysOn availability groups with synchronous commit ](https://docs.cloud.google.com/solutions/sql-server-always-on-compute-engine).
  * Linux environments that implement load balancers or reverse proxies use floating IP addresses, like [IP Virtual Server (IPVS)](http://www.linuxvirtualserver.org/software/ipvs.html), [HAProxy](http://www.haproxy.org/), and [nginx](http://nginx.org/). For detecting node failures and moving floating IP addresses between instances, these environments use daemons such as [Heartbeat](https://en.wikipedia.org/wiki/Linux-HA), [Pacemaker](https://clusterlabs.org/pacemaker/), or [Keepalived](http://www.keepalived.org/).
  * Highly available Windows Services with [Windows Server Failover Clustering](https://docs.microsoft.com/en-us/windows-server/failover-clustering/failover-clustering-overview) use floating IP addresses to ensure high availability. To implement Windows Services using failover clustering on Google Cloud, see [Running Windows Server Failover Clustering](https://docs.cloud.google.com/compute/docs/tutorials/running-windows-server-failover-clustering).



There are several ways to implement floating IP addresses in an on-premises environment. Servers sharing floating IP addresses typically also share state information through a [heartbeat mechanism](https://en.wikipedia.org/wiki/Heartbeat_\(computing\)). This mechanism lets the servers communicate their health status to each other; it also lets the secondary server take over the floating IP address after the primary server fails. This scheme is frequently implemented using the [Virtual Router Redundancy Protocol](https://tools.ietf.org/html/rfc3768), but you can also use other, similar mechanisms.

Once an IP address failover is initiated, the server taking over the floating IP address adds the address to its network interface. The server announces this takeover to other devices using Layer 2 by sending a [gratuitous Address Resolution Protocol (ARP) frame](https://en.wikipedia.org/wiki/Address_Resolution_Protocol#ARP_announcements). Alternatively, sometimes a routing protocol like [Open Shortest Path First (OSPF)](https://en.wikipedia.org/wiki/Open_Shortest_Path_First), announces the IP address to the upstream Layer 3 router.

The following diagram shows a typical setup in an on-premises environment.

![Typical on-premises environment.](https://docs.cloud.google.com/static/solutions/images/floating-ip-on-premises-environment.svg)

The preceding diagram shows how a primary server and a secondary server connected to the same switch exchange responsiveness information through a heartbeat mechanism. If the primary server fails, the secondary server sends a gratuitous ARP frame to the switch to take over the floating IP address.

You use a slightly different setup with on-premises load-balancing solutions, such as Windows Network Load Balancing or a Linux Load Balancing with Direct Server response like IPVS. In these cases, the service also sends out gratuitous ARP frames, but with the MAC address of another server as the gratuitous ARP source. This action essentially spoofs the ARP frames and takes over the source IP address of another server.

This action is done to distribute the load for one IP address between different servers. However, this kind of setup is out of scope for this document. In almost all cases when floating IP addresses are used for on-premises load balancing, migrating to [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs) is preferred.

## Challenges with migrating floating IP addresses to Compute Engine

Compute Engine uses a virtualized network stack in a [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/compute/docs/vpc) network, so typical implementation mechanisms don't work without changes in Google Cloud. For example, the VPC network handles ARP requests in the software-defined network, and ignores gratuitous ARP frames. In addition, it's impossible to directly modify the VPC network routing table with standard routing protocols such as OSPF or Border Gateway Protocol (BGP). The typical mechanisms for floating IP addresses rely on ARP requests being handled by switching infrastructure or they rely on networks programmable by OSPF or BGP. Therefore, IP addresses don't failover using these mechanisms in Google Cloud. If you migrate a virtual machine (VM) image using an on-premises floating IP address, the floating IP address can't fail over without changing the application.

You could use an [overlay network](https://en.wikipedia.org/wiki/Overlay_network) to create a configuration that enables full Layer 2 communication and IP takeover through ARP requests. However, setting up an overlay network is complex and makes managing Compute Engine network resources difficult. That approach is also out of scope for this document. Instead, this document describes patterns for implementing failover scenarios in a Compute Engine networking environment without creating overlay networks.

To implement highly available and reliable applications in Compute Engine, use horizontally scaling architectures. This type of architecture minimizes the effect of a single node failure.

This document describes multiple patterns to migrate an existing application using floating IP addresses from on-premises to Compute Engine, including the following:

  * Patterns using load balancing: 
    * Active-active load balancing
    * Load balancing with failover groups and application-exposed health checks
    * Load balancing with failover groups and heartbeat-exposed health checks
  * Patterns using Google Cloud routes: 
    * Using ECMP routes
    * Using different priority routes
    * Using a heartbeat mechanism to switch a route's next hop
  * Pattern using autohealing: 
    * Using an autohealing single instance



Using [Alias IP addresses](https://docs.cloud.google.com/vpc/docs/alias-ip) that move between VM instances is discouraged as a failover mechanism because it doesn't meet high availability requirements. In certain failure scenarios, like a zonal failure event, you might not be able to remove an Alias IP address from an instance. Therefore, you might not be able to add it to another instance—making failover impossible.

## Selecting a pattern for your use case

Depending on your requirements, one or more of the patterns described in this solution might be useful to implement floating IP addresses in an on-premises environment.

Consider the following factors when deciding what pattern best lets you use an application:

  * **Floating internal or floating external IP address:** Most applications that require floating IP addresses use floating internal IP addresses. Few applications use floating external IP addresses, because typically traffic to external applications should be load balanced.

The table later in this section recommends patterns you can use for floating internal IP addresses and for floating external IP addresses. For use cases that rely on floating internal IP addresses, any of these patterns might be viable for your needs. However, we recommend that use cases relying on floating external IP addresses should be migrated to one of the patterns using load balancing.

  * **Application protocols:** If your VM only uses TCP and UDP, you can use all of the patterns in the table. If it uses other protocols on top of IPv4 to connect, only some patterns are appropriate.

  * **Active-active deployment compatibility:** Some applications, while using floating IP addresses on-premises, can work in an [active-active deployment mode](https://en.wikipedia.org/wiki/High-availability_cluster#Node_configurations). This capability means they don't necessarily require failover from the primary server to the secondary server. You have more choices of patterns to move these kinds of applications to Compute Engine. Applications that require only a single application server to receive traffic at any time aren't compatible with active-active deployment. You can only implement these applications with some patterns in the following table.

  * **Failback behavior after primary VM recovers:** When the original primary VM recovers after a failover, depending on the pattern used, traffic does one of two things. It either immediately moves back to the original primary VM or it stays on the new primary VM until failback is initiated manually or the new primary VM fails. In all cases, only newly initiated connections fail back. Existing connections stay at the new primary VM until they are closed.

  * **Health check compatibility:** If you can't check if your application is responsive using Compute Engine [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts), without difficulty, you can't use some patterns described in the following table.

  * **Instance groups:** Any pattern with health check compatibility is also compatible with [instance groups](https://docs.cloud.google.com/compute/docs/instance-groups). To automatically recreate failed instances, you can use a managed instance group with autohealing. If your VMs keep state, you can use a stateful managed instance group. If your VMs can't be recreated automatically or you require manual failover, use an unmanaged instance group and manually recreate the VMs during failover.

  * **Existing heartbeat mechanisms:** If the high availability setup for your application already uses a heartbeat mechanism to trigger failover, like Heartbeat, Pacemaker, or Keepalived, you can use some patterns described in the following table.




The following table lists pattern capabilities. Each pattern is described in the following sections:

  * Patterns using load balancing
  * Patterns using Google Cloud routes
  * Pattern using autohealing

**Pattern name** | **IP address** | **Supported protocols** | **Deployment mode** | **Failback** | **Application health check compatibility required** | **Can integrate heartbeat mechanism**  
---|---|---|---|---|---|---  
**Patterns using load balancing** |  |  |  |  |  |   
Active-active load balancing | Internal or external | TCP/UDP only | Active-active | N/A | Yes | No  
Load balancing with failover and application-exposed health checks | Internal or external | TCP/UDP only | Active-passive | Immediate (except existing connections) | Yes | No  
Load balancing with failover and heartbeat-exposed health checks | Internal or external | TCP/UDP only | Active-passive | Configurable | No | Yes  
**Patterns using Google Cloud routes** |  |  |  |  |  |   
Using ECMP routes | Internal | All IP protocols | Active-active | N/A | Yes | No  
Using different priority routes | Internal | All IP protocols | Active-passive | Immediate (except existing connections) | Yes | No  
Using a heartbeat mechanism to switch route next hop | Internal | All IP protocols | Active-passive | Configurable | No | Yes  
**Pattern using autohealing** |  |  |  |  |  |   
Using an autohealing single instance | Internal | All IP protocols | N/A | N/A | Yes |  No  
  
Deciding which pattern to use for your use case might depend on multiple factors. The following decision tree can help you narrow your choices to a suitable option.

![A decision tree that helps you pick a load balancer.](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-floating-ip-addresses-in-compute-engine-01.svg)

The preceding diagram outlines the following steps:

  1. Does a single autohealing instance provide good enough availability for your needs? 
     1. If yes, see Using an autohealing single instance later in this document. Autohealing uses a mechanism in a VM instance group to automatically replace a faulty VM instance.
     2. If not, proceed to the next decision point.
  2. Does your application need protocols on top of IPv4 other than TCP and UDP? 
     1. If yes, proceed to the next decision point.
     2. If no, proceed to the next decision point.
  3. Can your application work in active-active mode? 
     1. If yes and it needs protocols on top of IPv4 other than TCP and UDP, see Using equal-cost multipath (ECMP) routes later in this document. ECMP routes distribute traffic among the next hops of all route candidates.
     2. If yes and it doesn't need protocols on top of IPv4 other than TCP and UDP, see Active-active load balancing later in this document. Active-active load balancing uses your VMs as backends for an internal TCP/UDP load balancer.
     3. If not–in either case–proceed to the next decision point.
  4. Can your application expose Google Cloud health checks? 
     1. If yes and it doesn't need protocols on top of IPv4 other than TCP and UDP, see Load balancing with failover and application-exposed health checks later in this document. Load balancing with failover and application-exposed health checks uses your VMs as backends for an internal TCP/UDP load balancer. It also uses the Internal TCP/UDP Load Balancing IP address as a virtual IP address.
     2. If yes and it needs protocols on top of IPv4 other than TCP and UDP, see Using different priority routes later in this document. Using different priority routes helps ensure that traffic always flows to a primary instance unless that instance fails.
     3. If no and it needs protocols on top of IPv4 other than TCP and UDP, see Load balancing with failover and heartbeat-exposed health checks later in this document. In the load balancing with failover and heartbeat-exposed health checks pattern, health checks aren't exposed by the application itself but by a heartbeat mechanism running between both VMs.
     4. If no and it DOES NOT NEED protocols on top of IPv4 other than TCP and UDP, see Using a heartbeat mechanism to switch a route's next hop later in this document. Using a heartbeat mechanism to switch a route's next hop uses a single static route with the next-hop pointing to the primary VM instance.



## Patterns using load balancing

Usually, you can migrate your application using floating IP addresses to an architecture in Google Cloud that uses [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). You can use an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/compute/docs/load-balancing/internal), as this option fits most use cases where the on-premises migrated service is only exposed internally. This load-balancing option is used for all examples in this section and in the sample deployments on GitHub. If you have clients accessing the floating IP address from other [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones), select the [global access option](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#ilb-global-access).

If your application communicates using protocols on top of IPv4, other than TCP or UDP, you must choose a pattern that doesn't use load balancing. Those patterns are described later in this document.

If your application uses HTTP(S), you can use an [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) to implement the active-active pattern.

If the service you are trying to migrate is externally available, you can implement all the patterns that are discussed in this section by using a [regional external passthrough Network Load Balancer](https://docs.cloud.google.com/compute/docs/load-balancing/network). For active-active deployments, you can also use an [external Application Load Balancer](https://docs.cloud.google.com/compute/docs/load-balancing/http), a [TCP proxy](https://docs.cloud.google.com/compute/docs/load-balancing/tcp-ssl/tcp-proxy), or an [SSL proxy](https://docs.cloud.google.com/compute/docs/load-balancing/tcp-ssl) if your application uses protocols and ports supported by those load balancing options.

Consider the following differences between on-premises floating-IP-address-based implementations and all load-balancing-based patterns:

  * **Failover time** : Pairing Keepalived with gratuitous ARP in an on-premises environment might fail over an IP address in a few seconds. In the Compute Engine environment, the mean recovery time from failover depends on the parameters you set. In case the virtual machine (VM) instance or the VM instance service fails, the mean-time-to-failover traffic depends on health check parameters such as `Check Interval` and `Unhealthy Threshold`. With these parameters set to their default values, failover usually takes 15–20 seconds. You can reduce the time by decreasing those parameter values.

In Compute Engine, failovers within zones or between zones take the same amount of time.

  * **Protocols and Ports:** In an on-premises setup, the floating IP addresses accept all traffic. Choose one of the following port specifications in the internal forwarding rule for the internal passthrough Network Load Balancer:

    * Specify at least one port and up to five ports by number.
    * Specify `ALL` to forward traffic on all ports for either TCP or UDP.
    * Use [multiple forwarding rules with the same IP address](https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip) to forward a mix of TCP and UDP traffic or to use more than five ports with a single IP address: 
      * Only TCP or UDP and 1—5 ports: Use one forwarding rule.
      * TCP and UDP and 1—5 ports: Use multiple forwarding rules.
      * 6 or more ports and TCP or UDP: Use multiple forwarding rules.
  * **Health checking:** On-premises, you can check application responsiveness on a machine in the following ways:

    * Receiving a signal from the other host specifying that it is still responsive.
    * Monitoring if the application is still available through the chosen heartbeat mechanism (Keepalived, Pacemaker, or Heartbeat). In Compute Engine, the [health check](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) has to be accessible from outside the host through gRPC, HTTP, HTTP/2, HTTPS, TCP, or SSL. The active-active load balancing and load balancing with failover group and application exposed health checking patterns require that your application expose its health checks. To migrate services using an existing heartbeat mechanism, you can use the load balancing with failover groups and heartbeat-exposed health checks pattern.



### Active-active load balancing

In the active-active load balancing pattern, your VMs are backends for an internal passthrough Network Load Balancer. You use the internal passthrough Network Load Balancer IP address as a virtual IP address. Traffic is equally distributed between the two backend instances. Traffic belonging to the same session goes to the same backend instance as defined in the [session affinity settings](https://docs.cloud.google.com/load-balancing/docs/internal#session_affinity).

Use the active-active load balancing pattern if your application only uses protocols based on TCP and UDP and doesn't require failover between machines. Use the pattern in a scenario where applications can answer requests depending on the content of the request itself. If there is a machine state that isn't constantly synchronized, don't use the pattern—for example, in a primary or secondary database.

The following diagram shows an implementation of the active-active load balancing pattern:

![How an internal client navigates the active-active load balancing pattern.](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-floating-ip-addresses-in-compute-engine-02.svg)

The preceding diagram shows how an internal client accesses a service that runs on two VMs through an internal passthrough Network Load Balancer. Both VMs are part of an instance group.

The active-active load balancing pattern requires your service to expose health checks using one of the [supported health check protocols](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports) to ensure that only responsive VMs receive traffic.

For a full sample implementation of this pattern, see the [example deployment with Terraform on GitHub](https://github.com/GoogleCloudPlatform/solutions-floating-ip-patterns-terraform/tree/main/1-ilb-active-active).

### Load balancing with failover and application-exposed health checks

Similar to the active-active pattern, the load balancing through failover and application-exposed health checks pattern uses your VMs as backends for an internal passthrough Network Load Balancer. It also uses the internal passthrough Network Load Balancer IP address as a virtual IP address. To ensure that only one VM receives traffic at a time, this pattern applies [failover for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview).

This pattern is recommended if your application only has TCP or UDP traffic, but doesn't support an active-active deployment. When you apply this pattern, all traffic flows to either the primary VM or the failover VM.

The following diagram shows an implementation of the load balancing with failover and application-exposed health checks pattern:

![How an internal client navigates a service behind an internal passthrough Network Load Balancer.](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-floating-ip-addresses-in-compute-engine-03.svg)

The preceding diagram shows how an internal client accesses a service behind an internal passthrough Network Load Balancer. Two VMs are in separate instance groups. One instance group is set as a primary backend. The other instance group is set as a failover backend for an internal passthrough Network Load Balancer.

If the service on the primary VM becomes unresponsive, traffic switches over to the failover instance group. Once the primary VM is responsive again, traffic automatically switches back to the primary backend service.

For a full sample implementation of this pattern, see the [example deployment with Terraform on GitHub](https://github.com/GoogleCloudPlatform/solutions-floating-ip-patterns-terraform/tree/main/2-ilb-failover).

### Load balancing with failover and heartbeat-exposed health checks

The load balancing with failover and heartbeat-exposed health checks pattern is the same as the previous pattern. The difference is that health checks aren't exposed by the application itself but by a heartbeat mechanism running between both VMs.

The following diagram shows an implementation of the load balancing with failover and heartbeat-exposed health checks pattern:

![How an internal client accesses a service behind an internal load balancer
  with two VMs in separate instance groups.](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-floating-ip-addresses-in-compute-engine-04.svg)

This diagram shows how an internal client accesses a service behind an internal load balancer. Two VMs are in separate instance groups. One instance group is set as a primary backend. The other instance group is set as a failover backend for an internal passthrough Network Load Balancer. Keepalived is used as a heartbeat mechanism between the VM nodes.

The VM nodes exchange information on the status of the service using the chosen heartbeat mechanism. Each VM node checks its own status and communicates that status to the remote node. Depending on the status of the local node and the status received by the remote node, one node is elected as the primary node and one node is elected as the backup node. You can use this status information to expose a health check result that ensures that the node considered _primary_ in the heartbeat mechanism also receives traffic from the internal passthrough Network Load Balancer.

For example, with Keepalived you can invoke scripts using the `notify_master`, `notify_backup`, and `notify_fault` [configuration variables](https://keepalived.readthedocs.io/en/latest/configuration_synopsis.html) that change the health check status. On transition to the _primary_ state (in Keepalived this state is called `master`), you can start an application that listens on a custom TCP port. When transitioning to a backup or fault state, you can stop this application. The health check can then be a TCP health check that succeeds if this custom TCP port is open.

This pattern is more complex than the pattern using failover with application-exposed health checks. However, it gives you more control. For example, you can configure it to fail back immediately or manually as part of the implementation of the heartbeat mechanism.

For a full sample implementation of this pattern that uses Keepalived, see the [example deployment with Terraform on GitHub](https://github.com/GoogleCloudPlatform/solutions-floating-ip-patterns-terraform/tree/main/3-ilb-keepalived).

## Patterns using Google Cloud routes

In cases where your application uses protocols other than TCP or UDP on top of IPv4, you can migrate your floating IP address to a pattern based on routes.

In this section, mentions of routes always refer to [Google Cloud routes](https://docs.cloud.google.com/vpc/docs/routes) that are part of a VPC network. References to static routes always refer to static routes on Google Cloud.

Using one of these patterns, you set multiple static routes for a specific IP address with the different instances as next-hops. This IP address becomes the floating IP address all clients use. It needs to be outside all [VPC subnet IP address ranges](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) because static routes can't override existing subnet routes. You must [turn on IP address forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward) on the target instances. Enabling IP address forwarding lets you accept traffic for IP addresses not assigned to the instances—in this case the floating IP address.

If you want the floating IP address routes to be available from [peered VPC networks](https://docs.cloud.google.com/vpc/docs/vpc-peering), [export custom routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#importing-exporting-routes) so the floating IP address routes propagate to all peer VPC networks.

To have connectivity from an on-premises network connected through [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect#docs) or [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn), you need to [use custom IP address route advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) to have the floating IP address advertised on-premises.

Route-based patterns have the following advantage over load-balancing-based patterns:

  * **Protocols and Ports:** Route-based patterns apply to all traffic sent to a specific destination. Load-balancing-based patterns only allow for TCP and UDP traffic.



Route-based patterns have the following disadvantages over load-balancing-based patterns:

  * **Health checking:** Health checks can't be attached to Google Cloud routes. Routes are used regardless of the health of the underlying VM services. Whenever the VM is running, routes direct traffic to instances even if the service is unhealthy. [Attaching an autohealing policy](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#setting_up_an_autohealing_policy) to those instances replaces the instances after an unhealthy time period that you specify. However, once those instances restart, traffic resumes immediately—even before the service is up. This service gap can lead to potential service errors when unhealthy instances are still serving traffic or are restarting.
  * **Failover time** : After you delete or stop a VM instance, Compute Engine disregards any static route pointing to this instance. However, since there are no health checks on routes, Compute Engine still uses the static route as long as the instance is still available. In addition, stopping the instance takes time, so failover time is considerably higher than it is with load-balancing-based patterns.
  * **Internal floating IP addresses only:** While you can implement patterns using load balancing with a regional external passthrough Network Load Balancer to create an external floating IP address, route-based patterns only work with internal floating IP addresses.
  * **Floating IP address selection:** You can set routes only to internal floating IP addresses that aren't part of any subnet—subnet routes can't be overwritten in Google Cloud. Track these floating IP addresses so you don't accidentally assign them to another network.
  * **Routes reachability:** To make internal floating IP addresses reachable from on-premises networks or peered networks, you need to distribute those static routes as described previously.



### Using equal-cost multipath (ECMP) routes

The [equal-cost multipath (ECMP) routes](https://en.wikipedia.org/wiki/Equal-cost_multi-path_routing) pattern is similar to the active-active load balancing pattern—traffic is equally distributed between the two backend instances. When you use [static routes](https://docs.cloud.google.com/vpc/docs/static-routes), ECMP distributes traffic among the next hops of all route candidates by using a five-tuple hash for affinity.

You implement this pattern by creating two static routes of equal priority with the Compute Engine instances as next-hops.

The following diagram shows an implementation of the ECMP routes pattern:

![How an internal client accesses a service using one of two ECMP routes.](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-floating-ip-addresses-in-compute-engine-05.svg)

The preceding diagram shows how an internal client accesses a service using one of two routes with the next hop pointing to the VM instances implementing the service.

If the service on one VM becomes unresponsive, autohealing tries to recreate the unresponsive instance. Once autohealing deletes the instance, the route pointing to the instance becomes inactive before the new instance has been created. Once the new instance exists, the route pointed to this instance is immediately used automatically and traffic is equally distributed between instances.

The ECMP routes pattern requires your service to expose health checks using [supported protocols](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports) so autohealing can automatically replace unresponsive VMs.

You can find a sample implementation of this pattern using Terraform in the [GitHub repository](https://github.com/GoogleCloudPlatform/solutions-floating-ip-patterns-terraform/tree/main/4-routes-ecmp) associated with this document.

### Using different priority routes

The different priority routes pattern is similar to the previous pattern, except that it uses different priority static routes so traffic always flows to a primary instance unless that instance fails.

To implement this pattern, follow the same steps in the ECMP routes pattern. When creating the static routes, give the route with the next-hop pointing to the primary instance a lower priority value (primary route). Give the instance with the next-hop pointing to the secondary instance a higher priority value (secondary route).

The following diagram shows an implementation of the different priority routes pattern: ![How an internal client accessing a service uses a primary or secondary route
  based on network circumstances.](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-floating-ip-addresses-in-compute-engine-06.svg)

The preceding diagram shows how an internal client accessing a service uses a primary route with a priority value of 500 pointing to VM 1 as the next hop in normal circumstances. A second route with a priority value of 1,000 is available pointing to VM 2, the secondary VM, as the next hop.

If the service on the primary VM becomes unresponsive, autohealing tries to recreate the instance. Once autohealing deletes the instance, and before the new instance it creates comes up, the primary route, with the primary instance as a next hop, becomes inactive. The pattern then uses the route with the secondary instance as a next hop. Once the new primary instance comes up, the primary route becomes active again and all traffic flows to the primary instance.

Like the previous pattern, the different priority route pattern requires your service to expose health checks using supported protocols so autohealing can replace unresponsive VMs automatically.

You can find a sample implementation of this pattern using Terraform in the [GitHub repository](https://github.com/GoogleCloudPlatform/solutions-floating-ip-patterns-terraform/tree/main/5-routes-priority) that accompanies this document.

### Using a heartbeat mechanism to switch a route's next hop

If your application implements a heartbeat mechanism, like Keepalived, to monitor application responsiveness, you can apply the heartbeat mechanism pattern to change the next hop of the static route. In this case, you only use a single static route with the next-hop pointing to the primary VM instance. On failover, the heartbeat mechanism points the next hop of the route to the secondary VM.

The following diagram shows an implementation of the heartbeat mechanism to switch a route's next hop pattern:

![How an internal client accesses a service where the primary and secondary VM
  exchange heartbeat information.](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-floating-ip-addresses-in-compute-engine-07.svg)

The preceding diagram shows how an internal client accesses a service using a route with the next hop pointing to the primary VM. The primary VM exchanges heartbeat information with the secondary VM through Keepalived. On failover, Keepalived calls a Cloud Run function that uses API calls to point the next hop at the secondary VM.

The nodes use the chosen heartbeat mechanism to exchange information with each other about the status of the service. Each VM node checks its own status and communicates it to the remote VM node. Depending on the status of the local VM node and the status received by the remote node, one VM node is elected as the primary node and one VM node is elected as the backup node. Once a node becomes primary, it points the next hop of the route for the floating IP address to itself. If you use Keepalived, you can invoke a script using the `notify_master` [configuration variable](https://keepalived.readthedocs.io/en/latest/configuration_synopsis.html) that replaces the static route using an [API call](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes#methods) or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

The heartbeat mechanism to switch a route's next-hop pattern doesn't require the VMs to be part of an instance group. If you want the VMs to be automatically replaced on failure, you can put them in an autohealing instance group. You can also manually repair and recreate unresponsive VMs.

Invoking the following procedure on failover ensures that failover time is minimized because traffic fails over after a single API call is completed in Step 1:

  1. Create a new static route with the floating IP address as the destination and the new primary instance as the next hop. The new route should have a different route name and a lower route priority (400, for example) than the original route.
  2. Delete the original route to the old primary VM.
  3. Create a route with the same name and priority as the route that you just deleted. Point it at the new primary VM as the next hop.
  4. Delete the new static route you created. You don't need it to ensure traffic flows to the new primary VM.



Since the original route is replaced, only one route should be active at a time even when there is a split network.

Using the heartbeat mechanism to switch the route priority pattern instead of the other route-based patterns can reduce failover time. You don't have to delete and replace VMs through autohealing for failover. It also gives you more control over when to fail back to the original primary server after it becomes responsive again.

One disadvantage of the pattern is that you have to manage the heartbeat mechanism yourself. Managing the mechanism can lead to more complexity. Another disadvantage is that you have to give privileges to change the global routing table to either the VMs running the heartbeat process or to a serverless function called from the heartbeat process. Changing the global routing table to a serverless function is more secure as it can reduce the scope of the privileges given to the VMs. However, this approach is more complex to implement.

For a full sample implementation of this pattern with Keepalived, see the [example deployment with Terraform on GitHub](https://github.com/GoogleCloudPlatform/solutions-floating-ip-patterns-terraform/tree/main/6-routes-keepalived).

## Pattern using autohealing

Depending on recovery-time requirements, migrating to a single VM instance might be a feasible option when using Compute Engine. This option is true even if multiple servers using a floating IP address were used on-premises. The reason why this pattern can be used sometimes despite the number of VMs being reduced is that you can create a new Compute Engine instance in seconds or minutes, while on-premises failures typically require hours or even days to fix.

### Using an autohealing single instance

Using this pattern you rely on the autohealing mechanism in a VM instance group to automatically replace a faulty VM instance. The application exposes a health check and when the application is unhealthy, autohealing automatically replaces the VM.

The following diagram shows an implementation of the autohealing single instance pattern:

![How an internal client connects directly to a Compute Engine instance.](https://docs.cloud.google.com/static/architecture/images/patterns-for-using-floating-ip-addresses-in-compute-engine-08.svg)

The preceding diagram shows how an internal client connects directly to a Compute Engine instance placed in a managed instance group with a size of 1 and with autohealing turned on.

Compared with patterns using load balancing, the autohealing single instance pattern has the following advantages:

  * **Traffic distribution:** There is only one instance, so the instance always receives all traffic.
  * **Ease of use:** Because there is only one instance, this pattern is the least complicated to implement.
  * **Cost savings:** Using a single VM instance instead of two can cut the cost of the implementation in half.



However, the pattern has the following disadvantages:

  * **Failover time:** This process is much slower than load-balancing-based patterns. After the health checks detect a machine failure, deleting and recreating the failed instance takes at least a minute, but often takes more time. This pattern isn't common in production environments. However, the failover time might be good enough for some internal or experimental services
  * **Reaction to zone failures:** A managed instance group with a size of 1 doesn't survive a zone failure. To react to zone failures, consider adding a [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) alert when the service fails, and create an instance group in another zone upon a zone failure. Because you can't use the same IP address in this case, use a [Cloud DNS private zone](https://docs.cloud.google.com/dns/docs/overview) to address the VM and switch the DNS name to the new IP address.



You can find a sample implementation of this pattern using Terraform in the [GitHub repository](https://github.com/GoogleCloudPlatform/solutions-floating-ip-patterns-terraform/tree/main/7-autohealing-instance).

## What's next

  * [Check out the deployment templates for this document on GitHub](https://github.com/GoogleCloudPlatform/solutions-floating-ip-patterns-terraform).
  * [Learn about internal passthrough Network Load Balancers](https://docs.cloud.google.com/compute/docs/load-balancing/internal).
  * [Learn about failover options for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview).
  * [Learn about routes in Compute Engine](https://docs.cloud.google.com/compute/docs/vpc/routes).
  * [Review the SQL Server Always On Availability Group solution](https://docs.cloud.google.com/solutions/sql-server-always-on-compute-engine).
  * [Learn about running Windows Server Failover Clustering](https://docs.cloud.google.com/compute/docs/tutorials/running-windows-server-failover-clustering).
  * [Learn about building a Microsoft SQL Server Always On Availability Group on Compute Engine](https://docs.cloud.google.com/solutions/sql-server-always-on-compute-engine).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-02-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-03 UTC."],[],[]] 
