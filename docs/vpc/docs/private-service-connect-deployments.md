---
url: https://docs.cloud.google.com/vpc/docs/private-service-connect-deployments/
title: Private Service Connect deployment patterns \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:18:21.977436+00:00
---

# Private Service Connect deployment patterns  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/private-service-connect-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private Service Connect deployment patterns

This page outlines some common ways to deploy and access Private Service Connect.

## Single-tenant services

Single-tenant services are services that are dedicated to a single consumer or tenant. The service instance is typically hosted in a separate VPC network dedicated for that tenant to isolate it from other tenant VPC networks in the producer organization. Each service uses a [consumer accept list](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#access) to control which projects can connect to the service. Using the accept list, you can limit access to a single tenant. Although only a single tenant can connect to the service, the tenant might create multiple endpoints or backends if they are connecting from multiple VPC networks.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-single-tenant.svg)](https://docs.cloud.google.com/static/vpc/images/psc-single-tenant.svg)

**Figure 1.** In a single-tenant managed service, the producer deploys a service in a separate VPC network that is dedicated to that consumer (click to enlarge).

## Multi-tenant services

Multi-tenant services are services that multiple consumers or tenants can access. The producer configures the service's consumer accept list so that multiple consumers can connect to the service.

The consumer accept list also lets the producer control the number of Private Service Connect connections that consumers can create. These limits help the producer prevent resource or quota exhaustion. If the producer needs to identify which tenant is the source of traffic, they can enable the [PROXY protocol](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#proxy-protocol) on the service.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-multi-tenant.svg)](https://docs.cloud.google.com/static/vpc/images/psc-multi-tenant.svg)

**Figure 2.** In a multi-tenant managed service, a service in one VPC network can be accessed by multiple consumers (click to enlarge). 

## Multi-point access

Multi-point access is when multiple Private Service Connect endpoints or backends connect to the same service attachment. Multi-point Private Service Connect is useful for multi-tenant services because it allows multiple, independent consumers to connect to the same service. It's also useful for single-tenant services for cases such as creating service connectivity across multiple VPC networks within a single consumer.

To support security for multi-tenant services that use multi-point access, you can specify individual Private Service Connect endpoints in a service's consumer accept list. In this configuration, only specifically authorized Private Service Connect endpoints can connect the service.

Not all services producers choose to support multi-point access in their managed service. Contact your service producer to verify if their service attachments support multi-point access.

## Multi-region access

Multi-region managed services are services that are deployed or accessed across multiple regions. Clients might access services in a different region because the service doesn't exist in their local region or for high availability and [multi-region failover](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#failover). Because Google Cloud supports global VPC networks, [Private Service Connect global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) lets clients reach Private Service Connect endpoints from any region. Client traffic can be from Compute Engine virtual machine (VM) instances, Cloud VPN tunnels, and VLAN attachments for Cloud Interconnect.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-multi-region.svg)](https://docs.cloud.google.com/static/vpc/images/psc-multi-region.svg)

**Figure 3.** Private Service Connect endpoints with global access can be accessed from any region (click to enlarge). 

## On-premises and hybrid access

You can connect on-premises networks or other cloud providers to your VPC network by using VLAN attachments for Cloud Interconnect and Cloud VPN tunnels. Because [endpoints for Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) and [endpoints for published services](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints) are both globally accessible, clients in connected networks can send requests to endpoints in any region. However, you can deploy endpoints in multiple regions to more granularly control routing from hybrid networks. You can route hybrid traffic from a specific region to a local endpoint which optimizes the shortest route for the traffic path.

[ ![](https://docs.cloud.google.com/static/vpc/images/hybrid-access.svg)](https://docs.cloud.google.com/static/vpc/images/hybrid-access.svg)

**Figure 4.** Private Service Connect endpoints and backends can be accessed from connected networks (click to enlarge). 

## Bidirectional connectivity

Although consumer clients typically initiate connections to managed services, managed services sometimes need to initiate connections to consumer-owned services.

### Reverse private connectivity

_Reverse private connectivity_ is when a consumer lets VMs and GKE clusters in a producer VPC network initiate traffic to a consumer VPC network by deploying Private Service Connect _in reverse_. In this case, the consumer deploys an internal load balancer and service attachment, which publishes their service to producers. Together, producers and consumers can use Private Service Connect in a forward and reverse direction together to create bidirectional connectivity with each other.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-reverse.svg)](https://docs.cloud.google.com/static/vpc/images/psc-reverse.svg)

**Figure 5.** Reverse private connectivity lets consumers and producers create bidirectional connectivity with each other (click to enlarge). 

### Private Service Connect interfaces

[Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) create bidirectional, transitive connections between consumer and producer VPC networks. Resources in both the consumer and producer VPC networks can initiate connections over the Private Service Connect interface. Additionally, because the connection is transitive, resources in the producer VPC network can communicate with [other workloads that are connected to the consumer VPC network](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces#other-networks). For example, a VM in the producer VPC network can reach workloads in networks that are connected to the consumer VPC network through Cloud Interconnect or VPC Network Peering.

## Hybrid services

Hybrid services that are not located in Google Cloud can be in other clouds, in an on-premises environment, or any combination of these locations. Private Service Connect lets you make a hybrid service accessible in another VPC network.

Hybrid services can be accessed through [hybrid NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts) which are compatible with [supported load balancers](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility#endpoints-services).

Often this configuration is used as a form of reverse private connectivity, with service producers making connections to consumer services that are hosted in on-premises networks. Private Service Connect lets the producer reach the consumer hybrid networks without establishing connectivity directly with those networks.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-hybrid.svg)](https://docs.cloud.google.com/static/vpc/images/psc-hybrid.svg)

**Figure 6.** Reverse private connectivity lets consumers and producers create bidirectional connectivity with each other (click to enlarge). 

For an example configuration, see [Publish a hybrid service by using Private Service Connect](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid#publish).

## Shared VPC

Private Service Connect resources can be deployed in standalone VPC networks or Shared VPC networks. Private Service Connect endpoints, backends, and service attachments can be deployed in host projects or service projects.

For example, a consumer service administrator can deploy Private Service Connect endpoints and backends in service projects using IP addresses from subnets in the host project. With this configuration, the endpoints and backends can be reached from other service projects in the same Shared VPC network.

All clients within a Shared VPC network have connectivity to a Private Service Connect endpoint regardless of which project it's deployed in. However, the choice of project does affect visibility, IAM access, and which project the hourly resource billing is charged to.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-shared-vpc.svg)](https://docs.cloud.google.com/static/vpc/images/psc-shared-vpc.svg)

**Figure 7.** You can make Private Service Connect resources available in all service projects associated with a Shared VPC network (click to enlarge). 

## What's next

  * Learn more about [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).
  * View [Private Service Connect compatibility information](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
