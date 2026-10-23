---
url: https://docs.cloud.google.com/load-balancing/docs/network/networklb-target-pools/
title: Target pool-based regional external passthrough Network Load Balancer overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:27.077661+00:00
---

# Target pool-based regional external passthrough Network Load Balancer overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/networklb-target-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Target pool-based regional external passthrough Network Load Balancer overview Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page describes target pool-based regional external passthrough Network Load Balancers. Target pool-based regional external passthrough Network Load Balancers support only IPv4 traffic, and only support the TCP and UDP protocols. 

If you're creating a new regional external passthrough Network Load Balancer, see [Backend service-based regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service) instead. Backend service-based regional external passthrough Network Load Balancers support IPv6 traffic, multiple protocols ( TCP, UDP, ESP, GRE, ICMP, and ICMPv6 ), managed instance group backends, zonal network endpoint group (NEG) backends (including support for [multiple network interfaces](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#zonal-negs)), fine-grained traffic distribution controls ([connection tracking](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#tracking-mode), [connection draining](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#connection_draining), [traffic steering](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#traffic-steering), [weighted load balancing](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#weighted-lb), and [failover policies](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#failover)), and allow you to use non-legacy health checks that match the type of traffic (TCP, SSL, HTTP, HTTPS, or HTTP/2) you are distributing. 

A regional external passthrough Network Load Balancer is a regional, Layer 4 load balancer. Regional external passthrough Network Load Balancers distribute TCP and UDP traffic among backend virtual machine (VM) instances in the same region in a Virtual Private Cloud (VPC) network. A regional external passthrough Network Load Balancer can receive traffic from any of the following:

  * Any client on the internet
  * Google Cloud VMs with external IPs
  * Google Cloud VMs that have internet access through Cloud NAT or instance-based NAT



Depending on the forwarding rule configuration, each target-pool based load balancer supports one of the following types of protocol traffic:

  * TCP
  * UDP
  * TCP and UDP



The scope of the load balancer is regional, not global. This means that all backend instances for a regional external passthrough Network Load Balancer must be located in the same region. You can place backends in any zone of the region.

Regional external passthrough Network Load Balancers support any and all ports. You can use a regional external passthrough Network Load Balancer to load balance either TCP or UDP traffic. Because the load balancer is a pass-through load balancer, your backends terminate the load-balanced TCP connection or UDP packets themselves. For example, you might run an HTTPS web server on your backends and use a regional external passthrough Network Load Balancer to route requests to it, terminating TLS on your backends themselves.

If you are building applications in GKE, we recommend that you use the built-in [GKE Service controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service), which deploys Google Cloud load balancers on behalf of GKE users. This is the same as the standalone load balancing architecture, except that its lifecycle is fully automated and controlled by GKE. For details, see [Expose apps using services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps#creating_a_service_of_type_loadbalancer).

## Architecture

The load balancer is made up of several configuration components. A single load balancer can have the following:

  * One target pool
  * Multiple forwarding rules



A regional external passthrough Network Load Balancer always has one target pool. Multiple forwarding rules can reference the target pool.

The target pool is a backend for the load balancer. It specifies the backend instances among which traffic is load balanced. Each forwarding rule is a frontend for the load balancer. Keep in mind that there are [limits](https://docs.cloud.google.com/load-balancing/docs/quotas) to the number of forwarding rules and target pools per project.

The regional external passthrough Network Load Balancers balance the load on your systems based on incoming IP protocol data, such as address, port, and protocol type.

The regional external passthrough Network Load Balancer is a pass-through load balancer, so your backends receive the original client request. The regional external passthrough Network Load Balancer doesn't do any Transport Layer Security (TLS) offloading or proxying. Traffic is directly routed to your VMs.

When you create a forwarding rule for the load balancer, you receive an ephemeral virtual IP address (VIP) or reserve a VIP that originates from a regional network block.

You then associate that forwarding rule with your target pools. The VIP is anycasted from Google's global points of presence, but the backends are regional. The load balancer cannot have backends that span multiple regions.

You can use Google Cloud firewalls to control or filter access to the backend VMs.

The regional external passthrough Network Load Balancer examines the source and destination ports, IP address, and protocol to determine how to forward packets. For TCP traffic, you can modify the forwarding behavior of the load balancer by configuring session affinity. The regional external passthrough Network Load Balancer forwards packets to the first network interface (`nic0`) of the instances in the target pool.

The load balancer preserves the source IP addresses of incoming packets. The destination IP address for incoming packets is the regional external IP address associated with the load balancer's forwarding rule.

### Load distribution algorithm

By default, to distribute traffic to instances, the [session affinity](https://docs.cloud.google.com/load-balancing/docs/target-pools#sessionaffinity) value is set to `NONE`. Cloud Load Balancing picks an instance based on a hash of the source IP and port, destination IP and port, and protocol. This means that incoming TCP connections are spread across instances, and each new connection might go to a different instance. All packets for a connection are directed to the same instance until the connection is closed. Established connections are not taken into account in the load balancing process.

Regardless of the session affinity setting, all packets for a connection are directed to the chosen instance until the connection is closed. An existing connection has no impact on load balancing decisions for new incoming connections. This can result in an imbalance among backends if long-lived TCP connections are in use.

You can choose a different session affinity setting if you need multiple connections from a client to go to the same instance.

### Target pools

A [target pool](https://docs.cloud.google.com/load-balancing/docs/target-pools) resource defines a group of instances that should receive incoming traffic from forwarding rules. When a forwarding rule directs traffic to a target pool, Cloud Load Balancing picks an instance from these target pools based on a hash of the source IP and port and the destination IP and port. Each target pool operates in a single region and distributes traffic to the first network interface (`nic0`) of the backend instance. For more information about how traffic is distributed to instances, see the Load distribution algorithm section.

The regional external passthrough Network Load Balancers are not proxies. Responses from the backend VMs go directly to the clients, not back through the load balancer. The load balancer preserves the source IP addresses of packets. The destination IP address for incoming packets is the regional external IP address associated with the load balancer's forwarding rule. Consequently:

  * Instances that participate as backend VMs for regional external passthrough Network Load Balancers must be running the appropriate [Linux guest environment](https://docs.cloud.google.com/compute/docs/instances/linux-guest-environment), [Windows guest environment](https://github.com/GoogleCloudPlatform/compute-image-windows), or other processes that provide equivalent capability.

The guest OS environment (or an equivalent process) is responsible for configuring local routes on each backend VM. These routes allow the VM to accept packets that have a destination that matches the IP address of the load balancer's forwarding rule.

  * On the backend instances that accept load-balanced traffic, you must configure the software to bind to the IP address associated with the load balancer's forwarding rule (or to any IP address, `0.0.0.0/0`).




Regional external passthrough Network Load Balancers support [Compute Engine autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler), which allows users to perform autoscaling on the instance groups in a target pool based on backend utilization. For more information, see [Scaling based on CPU utilization](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cpu#scaling_based_on_cpu_utilization).

If you intend for your target pool to contain a single VM instance, you should consider using the [protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding) feature instead.

Target pools can only be used with forwarding rules that handle TCP and UDP traffic. For all other protocols, you must create a target instance. You must create a target pool before you can use it with a forwarding rule. Each project can have up to 50 target pools.

### Forwarding rules

[Forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) work in conjunction with target pools to support load balancing. To use load balancing, you must create a forwarding rule that directs traffic to specific target pools. It is not possible to load balance your traffic without a forwarding rule.

Each forwarding rule matches a particular IP address, protocol, and optionally, port range to a single target pool. When traffic is sent to an external IP address that is served by a forwarding rule, the forwarding rule directs that traffic to the corresponding target pool.

If you are load balancing UDP packets that are likely to be fragmented before arriving at your Google Cloud VPC network, see Load balancing and fragmented UDP packets.

Target pool-based regional external passthrough Network Load Balancers support the following protocols for each forwarding rule: `TCP` or `UDP`. If you want the load balancer to forward _all_ IP protocol traffic, you must use a [Backend service-based regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service).

#### Multiple forwarding rules

You can configure multiple regional external forwarding rules for the same regional external passthrough Network Load Balancer. Optionally, each forwarding rule can have a different regional external IP address, or multiple forwarding rules can have the same regional external IP address.

Configuring multiple regional external forwarding rules can be useful for these use cases:

  * You need to configure more than one external IP address for the same target pool.
  * You need to configure different port ranges or different protocols by using the same external IP address for the same target pool.



When using multiple forwarding rules, make sure that you configure the software running on your backend VMs so that it binds to all necessary IP addresses. This is required because the destination IP address for packets delivered through the load balancer is the regional external IP address associated with the respective regional external forwarding rule.

### Health checks

[Health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) ensure that Compute Engine forwards new connections only to instances that are up and ready to receive them. Compute Engine sends health check requests to each instance at the specified frequency. After an instance exceeds its allowed number of health check failures, it is no longer considered an eligible instance for receiving new traffic.

To allow for graceful shutdown and closure of TCP connections, existing connections are not actively terminated. However, existing connections to an unhealthy backend are not guaranteed to remain viable for long periods of time. If possible, you should begin a graceful shutdown process as soon as possible for your unhealthy backend.

The health checker continues to query unhealthy instances, and returns an instance to the pool when the specified number of successful checks occur. If all instances are marked as `UNHEALTHY`, the load balancer directs new traffic to all existing instances.

Regional external passthrough Network Load Balancers rely on legacy HTTP [health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#legacy-health-checks) to determine instance health. Even if your service does not use HTTP, you must run a basic web server on each instance that the health check system can query.

Legacy HTTPS health checks aren't supported for regional external passthrough Network Load Balancers and cannot be used with most other types of load balancers.

### Firewall rules

Health checks for regional external passthrough Network Load Balancers are sent from [these IP ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). You'll need to create ingress allow firewall rules that permit traffic from those ranges.

**Note:** In addition to the IP ranges for health check probes, your backends might also receive health check traffic from their metadata servers, `169.254.169.254`. Each backend VM can receive packets from its metadata server because that is [always allowed traffic](https://docs.cloud.google.com/vpc/docs/firewalls#alwaysallowed).

Regional external passthrough Network Load Balancers are passthrough load balancers, which means that your firewall rules must allow traffic from the client source IP addresses. If your service is open to the internet, it is easiest to allow traffic from all IP ranges. If you want to restrict access so that only certain source IP addresses are allowed, you can set up firewall rules to enforce that restriction, but you must allow access from the health check IP ranges.

For a firewall rule example and a configuration example, see [Firewall rules for regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-netlb).

### IP addresses for request and return packets

When a backend VM receives a load-balanced packet from a client, the packet's source and destination are as follows:

  * **Source** : an external IP address associated with the client, a Google Cloud VM or a system on the internet.
  * **Destination** : the IP address of the load balancer's forwarding rule.

Because the load balancer is a passthrough load balancer (not a proxy), packets arrive bearing the IP address of the load balancer's forwarding rule. 

Although the guest environment automatically configures local routes so that the VM's operating system accepts traffic destined for the load balancer's IP address, the operating system cannot deliver these packets to your application if the application is configured to listen only on the VM's assigned internal IP address.

To ensure that the operating system delivers packets to your application, configure the application running on backend VMs to do the following:

  * Listen on (bind to) the load balancer's forwarding rule IP address or any IP address (`0.0.0.0` or `::`)


  * If the load balancer forwarding rule's protocol supports ports, listen on (bind to) a port that's included in the load balancer's forwarding rule



Return packets are sent directly from the load balancer's backend VMs to the client. The return packet's source IP address depends on the protocol:

  * TCP is connection-oriented so backend VMs must reply with packets whose source IP addresses match the destination IP address of the requesting packet so that the client can associate the response packets with the appropriate TCP connection.
  * UDP is connectionless, so backend VMs can send response packets whose source IP addresses either match the forwarding rule's IP address or match any assigned IP address for the VM. Practically speaking, most clients expect the response to come from the same IP address to which they sent packets.



The following table summarizes the source and destination IP addresses for response packets:

Traffic type | Source | Destination  
---|---|---  
TCP | The requesting packet's destination | The requesting packet's source  
UDP | For most use cases, the requesting packet's destination1 | The requesting packet's source  
  
1 When a VM has an external IP address or when you are using Cloud NAT, it is also possible to set the response packet's source IP address to the VM NIC's primary internal IPv4 address. Google Cloud or Cloud NAT changes the response packet's source IP address to either the NIC's external IPv4 address or a Cloud NAT external IPv4 address in order to send the response packet to the client's external IP address. Not using the forwarding rule's IP address as a source is an advanced scenario because the client receives a response packet from an external IP address that doesn't match the IP address to which it sent a request packet.

### Special routing paths

Google Cloud uses special routes not defined in your VPC network for health checks. For more information, see [Paths for health checks](https://docs.cloud.google.com/vpc/docs/routes#health_checks_for_all_load_balancer_types).

## Shared VPC architecture

The following table summarizes Shared VPC components for regional external passthrough Network Load Balancers:

IP address | Forwarding rule | Backend components  
---|---|---  
A [ regional external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static) must be defined in the same project as the instances being load balanced. | A [ regional external forwarding rule](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules) must be defined in the same project as the instances in the target pool (the service project). | The  target pool must be defined in the same project and same region where the instances in the target pool exist. Health checks associated with the target pool must be defined in the same project as well.  
  
## Traffic distribution

The way a target pool-based regional external passthrough Network Load Balancer distributes new connections depends on how session affinity has been configured.

### Session affinity

Session affinity controls the hashing method used to distribute new connections from clients to the load balancer's backend VMs. Target pool-based load balancers use the `sessionAffinity` parameter to configure session affinity.

For more information, see [Using target pools](https://docs.cloud.google.com/load-balancing/docs/target-pools#sessionaffinity).

### Load balancing and fragmented UDP packets

If you are load balancing UDP packets, be aware of the following:

  1. Unfragmented packets are handled normally in all configurations.
  2. UDP packets might become fragmented before reaching Google Cloud. Intervening networks might wait for all fragments to arrive before forwarding them, causing delay, or might drop fragments. Google Cloud does not wait for all fragments; it forwards each fragment as soon as it arrives.
  3. Because subsequent UDP fragments don't contain the destination port, problems can occur in these situations:

     * If the target pools session affinity is set to `NONE` (5-tuple affinity), the subsequent fragments might be dropped because the load balancer cannot calculate the 5-tuple hash.
     * If there is more than one UDP forwarding rule for the same load-balanced IP address, subsequent fragments might arrive at the wrong forwarding rule.



If you expect fragmented UDP packets, do the following:

  * Set session affinity to `NONE`, `CLIENT_IP_PROTO` or `CLIENT_IP`. 
    * Setting session affinity to `NONE` indicates that maintaining affinity is not required. Hence the load balancer uses a 5-tuple hash to select a backend for unfragmented packets, but 3-tuple hash for fragmented packets.
    * Setting session affinity to `CLIENT_IP_PROTO` or `CLIENT_IP` means that the source and destination ports are not used for hashing, and therefore the same hash is calculated for both fragmented and unfragmented packets.
  * Use only one UDP forwarding rule per load-balanced IP address. This ensures that all fragments arrive at the same forwarding rule.



With these settings, UDP fragments from the same packet are forwarded to the same instance for reassembly.

#### Using target instances as backends

If you're using [target instances](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding#targetinstances) as backends for the regional external passthrough Network Load Balancer and you expect fragmented UDP packets, use only one UDP forwarding rule per load-balanced IP address, and configure the forwarding rule to accept traffic on all ports 0-65535. This ensures that all fragments arrive at the same forwarding rule even if they don't have the same destination port.

## Limitations

  * You can't use the Google Cloud console to create target pool-based regional external passthrough Network Load Balancers. Instead, use either gcloud or the REST API.
  * Target pool-based regional external passthrough Network Load Balancers don't support Cloud Logging.



## What's next

  * Cloud Armor supports advanced network DDoS protection for regional external passthrough Network Load Balancers. For more information, see [Configure advanced network DDoS protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos).
  * To configure a regional external passthrough Network Load Balancer and distribute traffic across a set of Apache instances, see [Set up a regional external passthrough Network Load Balancer with target pools](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network).
  * To learn how regional external passthrough Network Load Balancers work with regional backend services instead of target pools, see: 
    * [Backend service-based regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
    * [Set up a regional external passthrough Network Load Balancer with backend services](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service)
    * [Transition regional external passthrough Network Load Balancers from target pools to backend services](https://docs.cloud.google.com/load-balancing/docs/network/transition-to-backend-services)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
