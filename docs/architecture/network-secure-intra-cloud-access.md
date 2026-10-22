---
url: https://docs.cloud.google.com/architecture/network-secure-intra-cloud-access/
title: Networking for secure intra-cloud access: Reference architectures \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:31.941452+00:00
---

# Networking for secure intra-cloud access: Reference architectures  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/network-secure-intra-cloud-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Networking for secure intra-cloud access: Reference architectures Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-13 UTC

This document is part of a series that describes networking and security architectures for enterprises that are migrating data center workloads to Google Cloud.

The series consists of the following documents:

  * [Designing networks for migrating enterprise workloads: Architectural approaches](https://docs.cloud.google.com/architecture/network-architecture)
  * Networking for secure intra-cloud access: Reference architectures (this document)
  * [Networking for internet-facing application delivery: Reference architectures](https://docs.cloud.google.com/architecture/network-application-delivery)
  * [Networking for hybrid and multi-cloud workloads: Reference architectures](https://docs.cloud.google.com/architecture/network-hybrid-multicloud)



Workloads for intra-cloud use cases reside in VPC networks and need to connect to other resources in Google Cloud. They might consume services that are provided natively in the cloud, like BigQuery. The security perimeter is provided by a variety of first-party (1P) and third-party (3P) capabilities like firewalls, VPC Service Controls, and network virtual appliances.

In many cases, these workloads span multiple Google Cloud VPC networks, and the boundaries between the VPC networks need to be secured. This document covers these security and connectivity architectures in depth.

## Lift-and-shift architecture

The first scenario for an intra-cloud use case is a lift-and-shift architecture where you're moving established workloads to the cloud as is.

### Cloud NGFW

You can help establish a secure perimeter by configuring [Cloud Next Generation Firewall](https://docs.cloud.google.com/vpc/docs/firewalls). You can use Tags, service accounts, and network tags to apply fine-grained firewall rules to VMs. For implementation guidelines on how to [manage traffic with Google Cloud firewall rules](https://docs.cloud.google.com/architecture/best-practices-vpc-design#manage_traffic_with_gcp_native_firewall_rules), see [Network firewall policies](https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking#network_firewall_policies) in the enterprise foundations blueprint.

You can also use [firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview) to audit and verify the effects of the firewall rule setting.

You can use [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs) for network forensics and also [stream the logs](https://docs.cloud.google.com/pubsub/docs) to integrate with [SIEM](https://wikipedia.org/wiki/Security_information_and_event_management). This overall system can provide real-time monitoring, correlation of events, analysis, and security alerts.

Figure 1 shows how firewall rules can use network tags to help restrict traffic among VMs in a VPC network.

![Network firewall configuration that uses network tags to apply fine-grained egress control.](https://docs.cloud.google.com/static/architecture/images/network-architecture/firewall-example.svg)

**Figure 1**. Network firewall configuration that uses network tags to apply fine-grained egress control.

### Network virtual appliance

A network virtual appliance (NVA) is a VM that has security functions such as web application firewalls (WAF) or security application-level firewalls. NVAs with multiple network interfaces can be used to bridge between VPC networks. You can use NVAs to implement security functions traffic between VPC networks, especially when you're using a hub-spoke configuration, as shown in figure 2.

![Centralized network appliance configuration in a
Shared VPC network.](https://docs.cloud.google.com/static/architecture/images/network-architecture/network-virtual-appliance.svg)

**Figure 2**. Centralized network appliance configuration in a Shared VPC network.

**Note:** In order to enable packets to be forwarded by the network virtual appliance, you need to [enable IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward) when you create the VM. Doing so disables the packet source and destination checking (anti-spoofing). Additionally, you must configure the required static routes with the next hop as the instance name or the internal IP address. For more information, see [Considerations for next hop instances](https://docs.cloud.google.com/vpc/docs/static-routes#next-hop-vm-only) in the routes documentation.

### Cloud IDS

Cloud Intrusion Detection System (Cloud IDS) lets you implement native security inspection and logging by mirroring traffic from a subnet in your VPC network. By using Cloud IDS, you can inspect and monitor a wide variety of threats at the network layer and at the application layer for analysis. You create [Cloud IDS endpoints](https://docs.cloud.google.com/intrusion-detection-system/docs/configuring-ids#create_a_endpoint) in your Google Cloud VPC network. These endpoints monitor ingress and egress traffic to and from that network, as well as intra-VPC network traffic, by using the packet mirroring functionality that's built into the Google Cloud networking stack. You must enable [private services access](https://docs.cloud.google.com/intrusion-detection-system/docs/configuring-ids#set_up_private_services_access) in order to connect to the [service producer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#producer) project (the Google-managed project) that hosts the Cloud IDS processes.

If you have a hub-and-spoke architecture, traffic from each of the spokes can be mirrored to the Cloud IDS instances, as shown in figure 3.

![Cloud IDS configuration to mirror VPC traffic that uses private services access.](https://docs.cloud.google.com/static/architecture/images/network-architecture/ids-configuration.svg)

**Figure 3**. Cloud IDS configuration to mirror VPC traffic that uses private services access.

Cloud IDS can be secured in your VPC Service Controls service perimeter using an [additional step](https://docs.cloud.google.com/intrusion-detection-system/docs/configuring-ids#optional_enable). You can read more about VPC Service Controls support in [supported products](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_ids).

### Network Connectivity Center

[Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview) is an orchestration framework that simplifies network connectivity among resources that are connected to a central management resource called a hub. NCC supports among the following types of networks:

  * Google Cloud VPC networks
  * On-premises and other cloud networks using Cloud Interconnect or HA VPN
  * Encrypted connections anchored by VMs



Network Connectivity Center is the control plane of the architecture. Connections to networks are called spokes. You can use Network Connectivity Center to connect networks together in either a full-mesh or hub-and-spoke topology.

### VPC Network Peering

For applications that span multiple VPC networks, whether they belong to the same Google Cloud project or to the same organization resource, VPC Network Peering enables connectivity between VPC networks. This connectivity lets traffic stay within Google's network so that it does not traverse the public internet.

A hub-and-spoke architecture is a popular model for VPC connectivity. This model is useful when an enterprise has various applications that need to access a common set of services, such as logging or authentication. The model is also useful if the enterprise needs to implement a common set of security policies for traffic that's exiting the network through the hub. For guidance on setting up a hub-and-spoke architecture using VPC Network Peering, see [Cross-Cloud Network inter-VPC connectivity using VPC Network Peering](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-vnp-vpn-ra).

### Shared VPC

You can use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), to maintain centralized control over network resources like subnets, routes, and firewalls in host projects. This level of control lets you implement the security best practice of least privilege for network administration, auditing, and access control because you can delegate network administration tasks to network and security administrators. You can assign the ability to create and manage VMs to instance administrators by using service projects. Using a service project ensures that the VM administrators are only given the ability to create and manage instances, and that they are not allowed to make any network-impacting changes in the Shared VPC network.

For example, you can provide more isolation by defining two VPC networks that are in two host projects and by attaching multiple service projects to each network, one for production and one for testing. Figure 6 shows an architecture that isolates a production environment from a testing environment by using separate projects.

For more information about best practices for building VPC networks, see [Best practices and reference architectures for VPC design](https://docs.cloud.google.com/architecture/best-practices-vpc-design).

![Shared VPC network configuration that uses multiple isolated
hosts and service projects \(test and production environments\).](https://docs.cloud.google.com/static/architecture/images/network-architecture/shared-vpc.svg)

**Figure 6**. Shared VPC network configuration that uses multiple isolated hosts and service projects (test and production environments).

## Hybrid services architecture

The hybrid services architecture provides additional cloud-native services that are designed to let you connect and secure services in a multi-VPC environment. These cloud-native services supplement what is available in the lift-and-shift architecture and can make it easier to manage a VPC-segmented environment at scale.

### Private Service Connect

[Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) lets a service that's hosted in one VPC network be surfaced in another VPC network. There is no requirement that the services be hosted by the same organization resource, so Private Service Connect can be used to privately consume services from another VPC network, even if it's attached to another organization resource.

You can use Private Service Connect in two ways: to access Google APIs or to access services hosted in other VPC networks.

#### Use Private Service Connect to access Google APIs

When you use Private Service Connect, you can expose [Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) by using a Private Service Connect endpoint that's a part of your VPC network, as shown in figure 7.

![Private Service Connect configuration to send
traffic to Google APIs by using a Private Service Connect
endpoint that's private to your VPC network.](https://docs.cloud.google.com/static/architecture/images/network-architecture/private-service-connect.svg)

**Figure 7**. Private Service Connect configuration to send traffic to Google APIs by using a Private Service Connect endpoint that's private to your VPC network.

Workloads can send traffic to a [bundle of global Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#supported-apis) by using a Private Service Connect endpoint. In addition, you can use a [Private Service Connect backend](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) to access a single Google API, extending the security features of load balancers to API services. Figure 8 shows this configuration.

![Private Service Connect configuration to send
traffic to Google APIs by using a Private Service Connect
backend.](https://docs.cloud.google.com/static/architecture/images/network-architecture/psc-w-ilb.svg)

**Figure 8**. Private Service Connect configuration to send traffic to Google APIs by using a Private Service Connect backend.

#### Use Private Service Connect between VPC networks or entities

Private Service Connect also lets a service producer offer services to a service consumer in another VPC network either in the same organization resource or in a different one. A service producer VPC network can [support multiple service consumers](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services). The consumer can connect to the producer service by sending traffic to a Private Service Connect endpoint located in the consumer's VPC network. The endpoint forwards the traffic to the VPC network containing the published service.

**Note:** If you're configuring Private Service Connect by using forwarding rules, the consumer's source IP address is translated by using source NAT (SNAT) to an IP address that's selected from one of the Private Service Connect subnets. If you want to retain the consumer connection IP address information, you need to configure that option. For more information, see [Consumer connection information](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#proxy-protocol).

![Private Service Connect configuration to publish
and consume managed services through an endpoint.](https://docs.cloud.google.com/static/architecture/images/network-architecture/psc-w-vpc.svg)

**Figure 9**. Private Service Connect configuration to publish a managed service through a service attachment and consume the service through an endpoint.

#### Private services access

Private Service Connect is the recommended way for a service producer to provide a service to a service consumer. However, Private Service Connect doesn't support all services. You can use private services access to get access to these [listed services](https://docs.cloud.google.com/vpc/docs/private-services-access#private-services-supported-services).

### VPC serverless access connector

A VPC [serverless access connector](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) handles traffic between your serverless environment and your VPC network. When you create a connector in your Google Cloud project, you attach it to a specific VPC network and [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). You can then configure your serverless services to use the connector for outbound network traffic. You can specify a connector by using a subnet or a CIDR range. Traffic sent through the connector into the VPC network originates from the subnet or the CIDR range that you specified, as shown in figure 10.

![Serverless VPC access connector configuration to
access Google Cloud serverless environments by using internal IP addresses
inside your VPC network.](https://docs.cloud.google.com/static/architecture/images/network-architecture/vpc-serverless-access-connector.svg)

**Figure 10**. Serverless VPC access connector configuration to access Google Cloud serverless environments by using internal IP addresses inside your VPC network.

Serverless VPC Access connectors are supported in every region that supports Cloud Run, Cloud Run functions, or the App Engine standard environment. For more information, see the list of [supported services](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#supported_services) and [supported networking protocols](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access#supported_networking_protocols) for using VPC Serverless access connector.

### Direct VPC egress

[Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) lets your Cloud Run service send traffic to a VPC network without setting up a Serverless VPC Access connector.

### VPC Service Controls

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) helps you prevent data exfiltration from services such as Cloud Storage or BigQuery by preventing unauthorized access from the internet or from projects that are not a part of a security perimeter. For example, consider a scenario where human error or incorrect automation causes IAM policies to be set incorrectly on a service such as Cloud Storage or BigQuery. As a result, resources in these services become publicly accessible. In that case, there is a risk of data exposure. If you have these services configured as part of the VPC Service Controls perimeter, ingress access to the resources is blocked, even if IAM policies allow access.

VPC Service Controls can create perimeters based on client attributes such as identity type (service account or user) and network origin (IP address or VPC network).

VPC Service Controls helps mitigate the following security risks:

  * Access from unauthorized networks that use stolen credentials.
  * Data exfiltration by malicious insiders or compromised code.
  * Public exposure of private data caused by misconfigured IAM policies.



Figure 11 shows how VPC Service Controls lets you establish a service perimeter to help mitigate these risks.

![VPC service perimeter extended to hybrid
environments by using private access services.](https://docs.cloud.google.com/static/architecture/images/network-architecture/vpc-sc.svg)

**Figure 11**. VPC service perimeter extended to hybrid environments by using private access services.

By using ingress and egress rules, you can enable communication between two service perimeters, as shown in figure 12.

![Configuring ingress and egress rules to communicate between
service perimeters.](https://docs.cloud.google.com/static/architecture/images/network-architecture/vpc-sc-rules.svg)

**Figure 12**. Configuring ingress and egress rules to communicate between service perimeters.

For detailed recommendations for VPC Service Controls deployment architectures, see [Design and architect service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/architect-perimeters). For more information about the list of services that are supported by VPC Service Controls, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).

## Zero Trust Distributed Architecture

Network perimeter security controls are necessary but not sufficient to support the security principles of least privilege and defense in depth. Zero Trust Distributed Architectures build on, but don't solely rely on, the network perimeter edge for security enforcement. As distributed architectures, they are composed of microservices with per-service enforcement of security policy, strong authentication, and workload identity.

You can implement Zero Trust Distributed Architectures as services managed by Cloud Service Mesh and Cloud Service Mesh.

### Cloud Service Mesh

[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) provides an out-of-the-box [mTLS](https://docs.cloud.google.com/service-mesh/docs/security/security-overview) Zero Trust Distributed Architecture microservice mesh that's built on Istio foundations. You set up the mesh by using an integrated [flow](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh). [Managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview#managed_anthos_service_mesh), with Google-managed data and control planes, is [supported](https://docs.cloud.google.com/service-mesh/docs/managed/supported-features-mcp#regions) on GKE. An [in-cluster control plane](https://docs.cloud.google.com/service-mesh/docs/overview#in-cluster_control_plane) is also available, which is suitable for [other environments](https://docs.cloud.google.com/service-mesh/docs/supported-features#platform_differences) such as Google Distributed Cloudises or GKE Multi-Cloud. Cloud Service Mesh manages identity and certificates for you, providing an Istio-based [authorization policy model](https://docs.cloud.google.com/service-mesh/docs/security/authorization-policy-overview).

Cloud Service Mesh relies on [fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts) for managing [multi-cluster service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services) deployment configuration and identity. As with Cloud Service Mesh, when your workloads operate in a flat (or shared) VPC network connectivity environment, there are no special network connectivity requirements beyond firewall configuration. When your architecture includes multiple Cloud Service Mesh clusters across separate VPC networks or networking environments, such as across a Cloud Interconnect connection, you also need an [east-west gateway](https://docs.cloud.google.com/service-mesh/docs/unified-install/off-gcp-multi-cluster-setup#install_the_east-west_gateway). Best practices for networking for Cloud Service Mesh are the same as those that are described in [Best practices for GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking).

Cloud Service Mesh also integrates with [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/service-mesh/v1.4/docs/iap-integration). IAP lets you set fine-grained [access policies](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) so that you can control user access to a workload based on attributes of the originating request, such as user identity, IP address, and device type. This level of control enables an end-to-end zero-trust environment.

You need to consider GKE cluster requirements when you use Cloud Service Mesh. For more information, see the [Requirements](https://docs.cloud.google.com/service-mesh/v1.9/docs/scripted-install/asm-onboarding#requirements) section in the "Single project installation on GKE" documentation.

## What's next

  * [Networking for internet-facing application delivery: Reference architectures](https://docs.cloud.google.com/architecture/network-application-delivery).
  * [Networking for hybrid and multi-cloud workloads: Reference architectures](https://docs.cloud.google.com/architecture/network-hybrid-multicloud).
  * [Network security for distributed applications in Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/security).
  * [Migration to Google Cloud](https://docs.cloud.google.com/solutions/migration-to-gcp-getting-started) can help you to plan, design, and implement the process of migrating your workloads to Google Cloud.
  * [Landing zone design in Google Cloud](https://docs.cloud.google.com/architecture/landing-zones) has guidance for creating a landing zone network.
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-13 UTC."],[],[]] 
