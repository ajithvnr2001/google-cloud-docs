---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/in-band-integration-overview/
title: In-band integration overview \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:20.459496+00:00
---

# In-band integration overview  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/in-band-integration-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  In-band integration overview Stay organized with collections  Save and categorize content based on your preferences. 

Network Security Integration in-band integration lets you insert your own network security appliances, such as firewalls or intrusion detection systems, directly in the network traffic path for inspection. You can use these network appliances to inspect the traffic for any identified threats before the traffic reaches its destination.

Network Security Integration offers in-band integration using [Cloud Next Generation Firewall](https://docs.cloud.google.com/firewall/docs/about-firewalls) and Packet Intercept technologies, providing a service-centric approach to packet processing pipelines. Packet Intercept is a Google Cloud capability that lets you insert network appliances in the path of network traffic without modifying any existing routing policies.

Packet processing occurs before outbound packets are routed and after inbound routed packets are received. In-band integration uses [Generic Network Virtualization Encapsulation (GENEVE) encapsulation](https://docs.cloud.google.com/network-security-integration/docs/understand-geneve) to securely transport packets between the sending or receiving virtual machines (VMs), and the packet processing VMs (your network appliances).

## Benefits of in-band integration

In-band integration provides the following benefits:

  * **Scalability** : deploys packet processing VMs that function as VM-based firewalls, intrusion detection systems, or network appliances. You can scale the packet processing VMs to meet your needs.
  * **Geneve encapsulation** : preserves the original packet, including its source and destination IP addresses as the packet is transported between a sending or receiving VM, and the packet processing VMs for inspection. For more information about GENEVE, see [GENEVE RFC](https://datatracker.ietf.org/doc/html/rfc8926).
  * **Cloud NGFW technology** : configures packet inspection by using ingress or egress rules in hierarchical firewall policies or global network firewall policies with the `apply_security_profile_group` action. This removes the dependency on routes in a VPC network. For more information, see How in-band integration works.
  * **Direct internet egress** : lets network security appliances route inspected outbound traffic directly to the internet. For more information, see Direct internet egress.



## Producer and consumer model

In-band integration uses a [producer-consumer](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview#service_producers_and_consumers) model with the following set up:

  * Service producers provide a scalable set of packet inspection VMs.
  * Service consumers use firewall rules in [hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies) or global [network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies) to specify which traffic to inspect.



### Service producer

A service producer offers packet inspection services through VMs. The VMs can be network appliances, or instances running a custom software solution. The producer is responsible for configuring, scaling, and maintaining the VMs.

A service producer deploys and manages [internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal) that use backend VMs for packet inspection services. The producer makes the packet inspection services available to consumers through zonal intercept deployments, which are grouped into global intercept deployment groups. For more information, see [Set up producer services](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-producer-service).

A service producer uses the following key components to offer packet inspection services:

  * **VM instances** : host a network appliance or a custom software solution. The producer is responsible for configuring, scaling, and maintaining the VMs. The producer can use either zonal unmanaged or zonal managed instance groups to host the packet inspection VMs.

  * **[Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal)** : distributes the traffic to backend packet inspection VMs. The forwarding rule of the load balancer acts as the entry point for traffic that needs inspection.

  * **[Intercept deployment](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployments-overview)** : a zonal resource that references the forwarding rule of the internal passthrough Network Load Balancer. The intercept deployment represents the producer's inspection service offering for the zone.

  * **[Intercept deployment group](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployment-groups-overview)** : a global resource that contains multiple zonal intercept deployments.




### Service consumer

A service consumer uses the packet inspection services offered by a service producer.

You can use packet inspection services with multiple producers in a VPC network. You can also configure a [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints) with Cloud Next Generation Firewall Enterprise in the same VPC network. Firewall endpoints and packet inspection services using in-band integration are not mutually exclusive. You can use them in parallel to meet your security requirements. For more information, see [Set up consumer services](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-consumer-service).

A service consumer uses the following key components to send traffic to a producer's packet inspection services:

  * **[Intercept endpoint group](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview)** : a global, per-project resource that references the service producer's intercept deployment group.

The intercept endpoint group expresses the consumer's intent to use packet inspection services offered by a service producer's intercept deployment group, in one or more zones of the consumer VPC network.

  * **[Intercept endpoint group association](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview)** : a global, per-project resource that logically connects an intercept endpoint group to one or more consumer VPC networks.

  * **[Firewall rules](https://docs.cloud.google.com/network-security-integration/docs/in-band/firewall-policies-overview)** : hierarchical firewall policy or global network firewall policy rules that direct traffic to packet inspection VMs.

  * **[Security profile](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profiles-overview)** : a global resource that references an intercept endpoint group.

  * **[Security profile group](https://docs.cloud.google.com/network-security-integration/docs/in-band/security-profile-groups-overview)** : a global, organization-level and project-level resource that references a security profile. Rules in a firewall policy reference the security profile group and use the `apply_security_profile_group` action to send packets to a producer's packet inspection service.




Intercept firewall rules are stateful. When a new session matches a rule, all subsequent ingress and egress packets associated with that session are intercepted and encapsulated with the appropriate security profile group in the GENEVE header.

**Caution:** Intercept rules can't process partial TCP sessions. Non-SYN TCP packets that match a rule but don't belong to a known, tracked active connection will be dropped.

## In-band integration deployment model

In-band integration is based on a producer-consumer model.

Figure 1 shows the high-level deployment architecture of in-band integration service.

[ ![High-level deployment architecture of in-band integration service](https://docs.cloud.google.com/static/network-security-integration/images/in-band/in-band-overview.svg)](https://docs.cloud.google.com/static/network-security-integration/images/in-band/in-band-overview.svg) **Figure 1.** High-level deployment architecture of in-band integration service

The diagram shows the following producer-consumer setup:

  * The `producer-project1` is a service producer project that contains one VPC network, `producer-vpc`. The network is configured with the following set up:

    * The service producer provides packet inspection services in the `us-west1-a` and `us-west1-b` zones.
    * Each zone has a set of packet inspection VMs, an internal passthrough Network Load Balancer, and an intercept deployment.
    * The service producer's packet inspection services are grouped into a single intercept deployment group.
  * The `consumer-project1` is a service consumer project that contains two VPC networks, `consumer-vpc1` and `consumer-vpc2`. Both networks are configured to use the producer's packet intercept service with the following set up:

    * The firewall policy and rule evaluation order of each network is set to `BEFORE_CLASSIC_FIREWALL`.

    * Each network has its own intercept endpoint group association that references a common intercept endpoint group. In the diagram, the common intercept endpoint group is in the `consumer-project2` consumer project. The intercept endpoint group expresses the consumer's intent to use the producer's intercept deployment group.

    * In the consumer's organization, the customer has created a security profile group containing a security profile. The security profile references the same intercept endpoint group that's associated with the `consumer-vpc1` and `consumer-vpc2` VPC networks.

    * To direct packets to the producer's packet inspection services, the consumer uses ingress or egress rules in a firewall policy.




## Direct internet egress

In-band integration supports the _direct internet egress_ deployment model. In this model, the network appliance in the producer network inspects internet-bound traffic and sends it directly to the public internet through its external network interface. The appliance then routes the internet response packet directly to the consumer VM using GENEVE.

To use the direct internet egress deployment model, configure your network appliance for direct internet egress as described in the appliance's documentation. You don't need additional configuration on your producer or consumer VPC networks or in-band resources. The consumer VPC networks also don't require Cloud NAT or default internet routes.

### Compare the in-band traffic flows

When a network appliance is not configured for direct internet egress, internet-bound traffic crosses the boundary between VPC networks twice in each direction, for a total of four hops:

  1. **Hop 1:** the consumer VM sends the outbound packet across the boundary from the consumer VPC network to the network appliance in the producer VPC network over the GENEVE tunnel.
  2. **Hop 2:** the network appliance inspects the packet and sends the original packet across the boundary back to the consumer VPC network over the GENEVE tunnel. The consumer VM then routes the packet to the internet through Cloud NAT or an external IP address.
  3. **Hop 3:** the consumer VM receives the internet response packet and sends it across the boundary to the network appliance in the producer VPC network over the GENEVE tunnel for inbound inspection.
  4. **Hop 4:** the network appliance inspects the response and sends it back across the boundary to the consumer VM over the GENEVE tunnel.



When a network appliance is configured for direct internet egress, internet-bound traffic crosses the boundary between VPC networks once in each direction, for a total of two hops:

  1. **Hop 1:** the consumer VM sends the outbound packet across the VPC network boundary to the network appliance in the producer VPC network over the GENEVE tunnel. After inspection, the appliance routes the packet directly to the internet through its external interface.
  2. **Hop 2:** the network appliance receives the internet response packet on its external interface, inspects it, and sends the packet across the boundary back to the consumer VPC network over the GENEVE tunnel.



With direct internet egress, outbound packets bypass the return hop to the consumer VPC network. You don't need to configure Cloud NAT gateways or external IP addresses in consumer VPC networks. This approach centralizes internet-facing infrastructure and costs.

## How in-band integration works

In in-band integration, a packet in a consumer's traffic is intercepted when it matches a firewall rule that uses the `apply_security_profile_group` action. Packets that match the firewall rule are sent to the internal passthrough Network Load Balancer in the service producer's VPC network.

### Requirements for packet inspection

For a firewall rule to successfully intercept consumer traffic, the following conditions must be met:

  * The firewall rule that uses the `apply_security_profile_group` action must belong to a hierarchical firewall policy or a global network firewall policy associated with a consumer VPC network.
  * The consumer's interception endpoint group association must associate the consumer's VPC network with the correct intercept endpoint group.
  * The firewall rule's security profile group must contain the security profile that references the correct intercept endpoint group.

Packets aren't intercepted if the intercept endpoint group referenced by the firewall rule's security profile doesn't match the intercept endpoint group associated with the VPC network.




### Zonal affinity

To optimize latency and improve throughput, you can use [zonal affinity](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity) for Network Security Integration deployments and configure zonal interception with regional backends. When you enable zonal affinity, your zonal intercept deployment references a regional internal passthrough Network Load Balancer that has backends in multiple zones within the same region. If healthy VM instances exist in the same zone as the originating traffic, then this configuration prefers to route packets to inspection VM instances within that same zone.

### Packet flow

When a packet matches a firewall rule that meets the requirements for packet inspection, Google Cloud processes the packet as follows:

  1. Intercept packet in the zone of the consumer VPC network.

Google Cloud intercepts packets based on the direction of the traffic:

     * **Egress traffic (packets sent from a VM)** : packets that match an egress firewall rule for packet inspection are intercepted _before_ the packet is routed.

If a VM has an external IPv4 address assigned to its NIC or if a VM NIC uses a Cloud NAT gateway, Google Cloud changes the source IPv4 address of the packet after processing egress firewall rules and packet inspection, but before routing the outbound packet.

     * **Ingress traffic (packets received by a VM)** : packets that match an ingress firewall rule for packet inspection are intercepted _after_ the packet has been routed.

If a VM has an external IPv4 address [assigned to its NIC](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#IP_assign) or if a VM NIC uses a [Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/overview), Google Cloud changes the destination IPv4 address of the packet after receiving the routed inbound packet, but before processing ingress firewall rules and packet inspection.

  2. Encapsulate the packet.

During the firewall processing stage, the original egress or ingress packet is encapsulated using the GENEVE protocol. This encapsulation preserves the source and destination IP addresses of the original packet within the GENEVE packet's payload.

  3. Send the encapsulated packet to the service producer.

The encapsulated packet is sent to a backend VM of an internal passthrough Network Load Balancer in the service producer's VPC network. The specific load balancer is selected based on the zone of the VM whose traffic was intercepted and the configuration of the intercept deployment group that was referenced by the intercept endpoint group.

  4. Process the packet.

The producer's backend VMs receive the GENEVE encapsulated packets on the `UDP` port `6081`. Each packet processing VM has software that understands how to extract the original packet from the GENEVE packet.

The inspection software on the VMs extracts the original packet, inspects it and, if the traffic is permitted, re-encapsulates it using GENEVE without altering the original packet's IP addresses, protocols, and ports.

  5. Return the packet.

The packet processing VM sends the re-encapsulated packet back to the consumer network using direct server return (DSR). In this process, the response traffic goes directly from the network appliance to the client, bypassing the load balancer to improve efficiency. For more information, see [How internal passthrough Network Load Balancers work](https://docs.cloud.google.com/load-balancing/docs/internal#how_ilb_works).


**Note:** If the network appliance supports direct internet egress, the appliance routes permitted outbound packets directly to the internet, and returns the internet response packet to the consumer VPC network using DSR.

## Limitations

  * When network packets match any interception rule, Compute Engine processes the packets at a slower rate. The rate of packet processing depends on the machine type, packet size, and CPU utilization, and is similar to the [egress rates to destinations outside of a VPC network](https://docs.cloud.google.com/compute/docs/network-bandwidth#vm-out-dest-e).
  * Regional network firewall policies don't support Packet Intercept.
  * Producer intercept deployments don't support instances with Dynamic NICs as backends.
  * Intercepted TCP sessions must begin with a SYN packet, allowing the intercepting appliance to observe the full session. For unknown connections, the appliance drops any non-SYN packets before interception.

A SYN packet is the very first packet that initiates a new TCP connection. A non-SYN packet is any other packet within that connection. If your traffic patterns include non-SYN initiators or split routing, contact Cloud Support for advice.




## What's next

  * [Set up producer services](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-producer-service)
  * [Set up consumer services](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-consumer-service)
  * [In-band integration partner providers](https://docs.cloud.google.com/network-security-integration/docs/in-band/in-band-partners)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
