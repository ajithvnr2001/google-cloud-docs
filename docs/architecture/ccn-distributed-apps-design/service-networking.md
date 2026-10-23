---
url: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/service-networking/
title: Service networking for distributed applications in Cross-Cloud Network \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:34.031518+00:00
---

# Service networking for distributed applications in Cross-Cloud Network  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/service-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Service networking for distributed applications in Cross-Cloud Network Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-30 UTC

This document is part of a design guide series for Cross-Cloud Network.

The series consists of the following parts:

  * [Cross-Cloud Network for distributed applications](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design)
  * [Network segmentation and connectivity for distributed applications in Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity)
  * Service networking for distributed applications in Cross-Cloud Network (this document)
  * [Network security for distributed applications in Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/security)



This document describes how to assemble an application from a set of chosen or created component services. We recommend you read through the entire document once before following the steps.

This document guides you through the following decisions:

  * Whether you create the individual service yourself or consume a third-party service
  * Whether the service is available globally or regionally
  * Whether the service is consumed from on-premises, from other clouds, or from neither
  * Whether you access the service endpoint through a shared services VPC or distribute the endpoints through all the relevant application VPCs



This document guides you through the following steps:

  1. Deciding if your application is global or regional
  2. Choosing third-party managed services or creating and publishing your own services
  3. Setting up private access to the service endpoints using either a shared or dedicated mode
  4. Assembling the services into applications to match either a global or regional archetype



Developers define the service networking layer for Cross-Cloud Network. By this stage, administrators have designed a [connectivity layer](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity) for Cross-Cloud Network that allows flexibility in the service networking options described in this document. In some cases, constraints from limited cross-VPC transitivity exist. We describe these constraints when they can affect design decisions.

## Decide whether your application is regional or global

Determine if the customers of the application you are creating need a regional or global deployment archetype. You can achieve regional resiliency by spreading loads across the zones of a region. You can achieve global resiliency by spreading loads across regions.

Consider the following factors when choosing an archetype:

  * The availability requirements of the application
  * The location where the application is consumed
  * Cost



For details, see [Google Cloud deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes).

This design guide discusses how to support the following deployment archetypes:

  * [Google Cloud multi-regional deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional)
  * [Google Cloud global deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/global)



In a cross-cloud distributed application, different services of that application can be delivered from different cloud service providers (CSPs) or private data centers. To help ensure a consistent resiliency structure, put services hosted in different CSPs into CSP data centers that are geographically near each other.

The following diagram shows a global application stack that's distributed across clouds and different application services are deployed in different CSPs. Each global application service has workload instances in different regions of the same CSP.

![Global application stack distributed across
clouds.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/global-with-distributed-stack-multi.svg)

## Define and access application services

To assemble your application, you can use existing third-party managed services, create and host your own application services, or use a combination of both.

### Use existing third-party managed services

Decide which third-party managed services you can use for your application. Determine which ones are constructed as regional services or global services. Also, determine which private access options each service supports.

When you know which managed services you can use, you can determine which services you need to create.

### Create and access application services

Each service is hosted by one or more workload instances that can be accessed as a single endpoint or as a group of endpoints.

The general pattern for an application service is shown in the following diagram. The application service is deployed across a collection of workload instances. (In this case, a workload instance could be a Compute Engine VM, a Google Kubernetes Engine (GKE) cluster, or some other backend that runs code.) The workload instances are organized as a set of backends that are associated with a load balancer.

The following diagram shows a generic load balancer with a set of backends.

![Load balancer with backends.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-14.svg)

To achieve the chosen load distribution and to automate failovers, these groups of endpoints use a frontend load balancer. By using managed instance groups (MIGs), you can elastically increase or decrease the capacity of the service by autoscaling the endpoints that form the backend of the load balancer. Furthermore, depending on the requirements of the application service, the load balancer can also provide authentication, TLS termination, and other connection specific services.

### Determine the scope of the service - regional or global

Decide if your service needs and can support regional or global resiliency. A regional software service can be designed for synchronization within a regional latency budget. A global application service can support synchronous failovers across nodes that are distributed across regions. If your application is global, you might want the services supporting it to be global as well. But, if your service requires synchronization among its instances to support failover, you must consider the latency between regions. For your situation, you might have to rely on regional services with redundancy in the same or nearby regions, thus supporting low-latency synchronization for failover.

Cloud Load Balancing supports endpoints that are hosted either within a single region or distributed across regions. Thus, you can create a global customer-facing layer that speaks to global, regional, or hybrid service layers. Choose your service deployments to ensure that dynamic network failover (or load balancing across regions) aligns with the resiliency state and capabilities of your application logic.

The following diagram shows how a global service that's built from regional load balancers can reach backends in other regions, thus providing automatic failover across regions. In this example, the application logic is global and the chosen backend supports synchronization across regions. Each load balancer primarily sends requests to the local region, but can failover to remote regions.

![Load balancers with backends in different regions.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-15.svg)

  * A global backend is a collection of regional backends that are accessed by one or more load balancers.
  * Although the backends are global, the frontend of each load balancer is regional.
  * In this architecture pattern, load balancers primarily distribute traffic only within their region, but can also balance traffic to other regions when the resources in the local region are unavailable.
  * A set of regional load balancer frontends, each accessible from other regions and each able to reach backends in other regions, form an aggregate global service.
  * To assemble a global application stack, as discussed in Design global application stacks, you can use DNS routing and health checks to achieve cross-regional failover of the frontends.
  * The load balancer frontends are themselves accessible from other regions using [global access](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#global-access) (not shown in diagram).



This same pattern can be used to include published services with global failover. The following diagram depicts a published service that uses global backends.

![Load balancers accessible from different regions.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-16.svg)

In the diagram, note that the published service has global failover implemented in the producer environment. The addition of global failover in the consumer environment enables resilience to regional failures in the consumer load balancing infrastructure. Cross-regional failover of the service must be implemented both in the service application logic and in the load balancing design of the service producer. Other mechanisms can be implemented by the service producers.

To determine which Cloud Load Balancing product to use, you must first determine what traffic type your load balancers must handle. Consider the following general rules:

  * Use an Application Load Balancer for HTTP(S) traffic.
  * Use a proxy Network Load Balancer for non-HTTP(S) TCP traffic. This proxy load balancer also supports TLS offload.
  * Use a passthrough Network Load Balancer to preserve the client source IP address in the header, or to support additional protocols like UDP, ESP, and ICMP.



For detailed guidance on selecting the best load balancer for your use case, see [Choose a load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer).

### Services with serverless backends

A service can be defined using serverless backends. The backend in the producer environment can be organized in a [Serverless NEG](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) as a backend to a load balancer. This service can be published using Private Service Connect by creating a service attachment that's associated with the frontend of the producer load balancer. The published service can be consumed through Private Service Connect endpoints or Private Service Connect backends. If the service requires producer-initiated connections, you can use a [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) connector to let Cloud Run, App Engine standard, and Cloud Run functions environments send packets to the internal IPv4 addresses of resources in a VPC network. Serverless VPC Access also supports sending packets to other networks connected to the selected VPC network.

### Methods for accessing services privately

Your application can consist of managed services provided by Google, third-party services provided by outside vendors or peer groups in your organization, and services that your team develops. Some of those services might be accessible over the internet using public IP addresses. This section describes the methods you can use to access those services using the private network. The following service types exist:

  * Google public APIs
  * Google serverless APIs
  * Published managed services from Google
  * Published managed services from vendors and peers
  * Your published services



Keep these options in mind when reading subsequent sections. Depending on how you allocate your services, you can use one or more of the private access options described.

**Note:** This guide assumes that all interaction between services happens privately. However, if you are using two external services and those services interact directly, how they interact is outside the scope of this guide.

The organization (or group within an organization) that assembles, publishes, and manages a service is referred to as the service producer. You and your application are referred to as the service consumer.

Some managed services are published exclusively using [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access). The network designs recommended in [Internal connectivity and VPC networking](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity#internal-connectivity-and-vpc-networking) accommodate services published with private service access and Private Service Connect.

For an overview of the options for accessing services privately, see [Private access options for services](https://docs.cloud.google.com/vpc/docs/private-access-options).

We recommend using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to connect to managed services whenever possible. For more information on deployment patterns for Private Service Connect, see [Private Service Connect deployment patterns](https://docs.cloud.google.com/vpc/docs/private-service-connect-deployments).

There are two types of Private Service Connect, and the different services can be published as either type:

  * [Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints)
  * [Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends)



Services published as Private Service Connect endpoints can be consumed directly by other workloads. The services rely on the authentication and resiliency provisioned by the producer of the service. If you want additional control over the service authentication and resiliency, you can use Private Service Connect backends to add a layer of load balancing for authentication and resiliency in the consumer network.

The following diagram shows services being accessed through Private Service Connect endpoints:

![Accessing services through Private Service Connect endpoints.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-26.svg)

The diagram shows the following pattern:

  * A Private Service Connect endpoint is deployed in the consumer VPC, which makes the producer service available to VMs and GKE nodes.
  * Both the consumer and producer networks must be deployed in the same region.



The preceding diagram shows endpoints as regional resources. Endpoints are reachable from other regions because of [global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access).

For more information on deployment patterns, see [Private Service Connect deployment patterns](https://docs.cloud.google.com/vpc/docs/private-service-connect-deployments).

Private Service Connect backends use a load balancer configured with Private Service Connect network endpoint group (NEG) backends. For a list of supported load balancers, see [About Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends).

Private Service Connect backends let you create the following backend configurations:

  * Customer-owned domains and certificates in front of managed services
  * Consumer-controlled failover between managed services in different regions
  * Centralized security configuration and access control for managed services



In the following diagram, the global load balancer uses a Private Service Connect NEG as a backend that establishes communication to the service provider. No further networking configuration is required and the data is carried over Google's SDN fabric.

![Global load balancer using network endpoint group.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-29.svg)

Most services are designed for connections that the consumer initiates. When services need to initiate connections from the producer, use [Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces).

A key consideration when deploying private service access or Private Service Connect is transitivity. Private Service Connect consumer access points are reachable over Network Connectivity Center. Published services are not reachable across a VPC Network Peering connection for either Private Service Connect or private services access consumer access points. In the absence of inter-VPC transitivity for all service consumer access points, the location of the service access subnet or endpoints in the VPC topology dictates whether you design the network for shared or dedicated service deployment.

Options such as HA VPN and customer managed proxies provide methods to allow inter-VPC transitive communication.

Private Service Connect Endpoints aren't reachable over VPC Network Peering. If you require this type of connectivity, deploy an internal load balancer and Private Service Connect NEG as a backend, as shown in the following diagram:

![Using NEGs to provide reachability.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-30.svg)

Google APIs can be accessed privately by using [Private Service Connect endpoints and backends](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints). The use of endpoints is generally recommended as the Google API producer provides resiliency and certificate based authentication.

Create a Private Service Connect endpoint in every VPC in which the service needs to be accessed. Because the consumer IP address is a private global IP address, a single DNS mapping for each service is required, even if there are endpoint instances in multiple VPCs, as shown in the following diagram:

![Private Service Connect with Google APIs.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-25.svg)

## Define consumption patterns for published services

Published services can run in a variety of locations: your VPC network, another VPC network, in an on-premises data center, or in the cloud. Regardless of where the service workload runs, your application consumes those services by using an access point, such as one of the following:

  * An IP address in a private services access subnet
  * A Private Service Connect endpoint
  * A VIP for a load balancer using Private Service Connect NEGs



The consumer access points can be shared across networks or dedicated to a single network. Decide whether to create shared or dedicated consumer access points based on whether your organization delegates the task of creating consumer service access points to each application group or manages the access to services in a consolidated manner.

The management of service access involves the following activities:

  * Creating the access points
  * Deploying the access points in a services access VPC, which is a VPC that has the appropriate type of reachability
  * Registering the consumer access points' IP addresses and URLs in DNS
  * Managing security certificates and resiliency for the service in the consumer space, when adding load balancing in front of the consumer access points



For some organizations, it might be viable to assign service access management to a central team, while others might be structured to give more independence to each consumer or application team. A byproduct of operating in the dedicated mode is that some of the elements are replicated. For example, a service is registered with multiple DNS names by each application group and manages multiple sets of TLS certificates.

The VPC design described in [Network segmentation and connectivity for distributed applications in Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity) enables reachability for deploying service access points in either a shared or dedicated mode. Shared consumer access points are deployed in service access VPCs, which can be accessed from any other VPC or external network. Dedicated consumer access points are deployed in application VPCs, which can be accessed only from resources within that application VPC.

The main difference between a service access VPC and an application VPC is the service access point transitive connectivity that a service access VPC enables. Service access VPCs aren't limited to hosting consumer access points. A VPC can host application resources, as well as shared consumer access points. In such a case, the VPC should be configured and handled as a service VPC.

### Shared managed services access

For all service consumption methods, including Private Service Connect, ensure that you do the following tasks:

  * Deploy the services consumer access points in a services VPC. Service VPCs have transitive reachability to other VPCs.
  * If the service access VPC is connected with HA VPN, advertise the subnet for the consumer access point as a [custom route advertisement](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) from the Cloud Router that peers to other networks over HA VPN. For Google APIs, advertise the host IP address of the API.
  * Update multicloud firewall rules to allow the private services access subnet.



For private service access specifically, ensure that you can fulfill the following additional requirements:

  * Export custom routes to the service producer's network. For more information, see [On-premises hosts can't communicate with the service producer's network](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#on-prem)
  * Create ingress firewall rules to allow the private services access subnet into the application VPCs
  * Create ingress firewall rules to allow the private services access subnet into the services VPC



For serverless service access, ensure that you can fulfill the following requirements:

  * Access connector requires a dedicated /28 regular subnet
  * Cloud Router advertises regular subnets by default
  * Create ingress firewall rules to all allow VPC access subnet within the VPC(s)
  * Update multicloud firewall rules to allow the VPC access connector subnet
  * Create ingress firewall rule(s) to allow the private services access subnet into the application VPC(s)



### Dedicated managed services access

Ensure that you do the following tasks:

  * In each application VPC where access is needed, deploy a forwarding rule for the service to create an access point.
  * For private service access, create ingress firewall rule(s) to allow the private services access subnet into the application VPC(s).



For serverless service access, ensure that you can fulfill the following requirements:

  * Access connector requires a dedicated /28 regular subnet
  * Create ingress firewall rules to allow the VPC Access connector subnet within the application VPC(s)



## Assemble the application stack

This section describes assembling a regional or global application stack.

### Design regional application stacks

When an application follows the regional or multi-regional deployment archetypes, use regional application stacks. Regional application stacks can be thought of as a concatenation of regional application service layers. For example, a regional web service layer that talks with an application layer in the same region, that in turn talks to a database layer in the same region, is a regional application stack.

Each regional application service layer uses load balancers to distribute traffic across the endpoints of the layer in that region. Reliability is achieved by distributing the backend resources across three or more zones in the region.

Application service layers in other CSPs or on-premises data centers should be deployed in equivalent regions in the external networks. Also, make published services available in the region of the stack. To align the application stack within a region, the application service layer URLs have to resolve to the specific load balancer frontend regional IP address. These DNS mappings are registered in the relevant DNS zone for each application service.

The following diagram shows a regional stack with active-standby resiliency:

![Regional stack with active-standby resiliency.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-2.svg)

A complete instance of the application stack is deployed in each region across the different cloud data centers. When a regional failure occurs on any of the application service layers, the stack in the other region takes over delivery of the entire application. This failover is done in response to out-of-band monitoring of the different application service layers.

When a failure is reported for one of the service layers, the frontend of the application is re-anchored to the backup stack. The application is written to reference a set of regional name records that reflect the regional IP address stack in DNS so that each layer of the application maintains its connections within the same region.

### Design global application stacks

When an application follows the global application deployment archetype, each application service layer includes backends in multiple regions. Including backends in multiple regions expands the resiliency pool for the application service layer beyond a single region and enables automated failover detection and reconvergence.

The following diagram shows a global application stack:

![Global stack using a hub project and application project.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-17.svg)

The preceding diagram shows a global application assembled from the following components:

  * Services running in on-premises data centers with load balancer frontends. The load balancer access points are reachable over Cloud Interconnect from the transit VPC.
  * A transit VPC hosts hybrid connections between the external data center and the application VPC.
  * An application VPC that hosts the core application running on workload instances. These workload instances are behind load balancers. The load balancers are reachable from any region in the network and they can reach backends in any region in the network.
  * A services VPC that hosts access points for services running in other locations, such as in third party VPCs. These service access points are reachable over the HA VPN connection between the services VPC and the transit VPC.
  * Service producer VPCs that are hosted by other organizations or the primary organization and applications that run in other locations. The relevant services are made reachable by Private Service Connect backends deployed as global backends to regional load balancers hosted in the services VPC. The regional load balancers are reachable from any other region.



If you want the created application to be reachable from the internet, you can add a [global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) that points to the application workloads in the application VPC (not shown in the diagram).

To support a global application stack, we used global backends for each application layer. This allows recovery from a failure of all backend endpoints in one region. Each region has a regional load balancer frontend for each application service layer. When a regional failover occurs, the internal regional load balancer frontends can be reached across regions, because they use global access. Because the application stack is global, [DNS geolocation routing policies](https://docs.cloud.google.com/blog/products/networking/dns-based-traffic-routing-for-global-application-deployment) are used to select the most appropriate regional frontend for a particular request or flow. In case of a frontend failure, [DNS health checks](https://cloud.google.com/blog/products/networking/introducing-automated-failover-for-private-workloads-using-cloud-dns-routing-policies-with-health-checks) can be used to automate the failover from one frontend to another.

Services published using Private Service Connect backends benefit from [Private Service Connect global access](https://cloud.google.com/blog/products/networking/access-managed-services-globally-with-private-service-connect). This feature allows a Private Service Connect backend to be reachable from any region and lessens disruptions from application service layer failures. This means the Private Service Connect backends can be leveraged as global backends as described in [Determine the scope of the Service - regional or global](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/service-networking#determine_the_scope_of_the_service_-_regional_or_global).

### Provide private access to services hosted in external networks

You might want to publish a local access point for a service hosted in another network. In these cases, you can use an [internal regional TCP proxy load balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid) using hybrid NEGs. You can create a service producer that's hosted on-premises or in other cloud environments that are available to service consumers (clients) in your VPC network, as shown in the following diagram:

![Local access point using hybrid NEGs.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-28.svg)

If you want to make the hybrid service available in a VPC network other than the one hosting the load balancer, you can use Private Service Connect to [publish the service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer). By placing a service attachment in front of your internal regional TCP proxy load balancer, you can let clients in other VPC networks reach the hybrid services running on-premises or in other cloud environments.

In a cross-cloud environment, the use of a hybrid NEG allows for secure application-to-application communication.

When a different organization publishes an application service, use a hybrid NEG to extend private access abstractions for that service. The following diagram illustrates this scenario:

![Hybrid NEGs in front of services in other networks.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-19.svg)

In the preceding diagram, the application service layer is fully composed in the neighboring CSP, which is highlighted in the parts of the diagram that aren't grayed out. The hybrid load balancers are used in conjunction with Private Service Connect service attachments as a mechanism to publish the external application service for private consumption within Google Cloud. The hybrid load balancers with hybrid NEGs and Private Service Connect service attachments are in a VPC that's part of a service producer project. This service producer project might usually be a different VPC than the transit VPC, because it is within the administrative scope of the producer organization or project, and therefore separate from the common transit services. The producer VPC doesn't need to be connected over VPC peering or HA VPN with the consumer VPC (which is the Services Shared VPC in the diagram).

### Centralize service access

Service access can be centralized into a VPC network and accessed from other application networks. The following diagram shows the common pattern that enables the centralization of the access points:

![Dedicated services VPC.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-30a.svg)

The following diagram shows all services being accessed from a dedicated services VPC:

![Dedicated services VPC with centralized load balancers.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-20.svg)

When services are frontended with application load balancers, you can consolidate onto fewer load balancers by using URL maps to steer traffic for different service backends instead of using different load balancers for each service. In principle, an application stack could be fully composed using a single application load balancer plus service backends and appropriate URL mappings.

In this implementation, you must use hybrid NEGs across VPCs for most backend types. The exception is a Private Service Connect NEG or backend, as described in [Explicit Chaining of Google Cloud L7 Load Balancers with Private Service Connect](https://codelabs.developers.google.com/codelabs/l7lb-chain-psc#0).

The use of hybrid NEGs across VPCs comes at the expense of foregoing autohealing and autoscaling for the backends. Published services already have a load balancer in the producer tenant that provides autoscaling. Therefore, you only run into the limitations of the hybrid NEGs if you centralize the load balancing function for service layers being composed natively rather than consumed from publication.

When using this service networking pattern, remember that the services are consumed through an additional layer of load balancing.

Private Service Connect service endpoints are reachable across NCC spoke VPCs.

The centralized mode adds a layer of load balancing on the consumer side of the service. When you use this mode, you also need to manage certificates, resiliency, and additional DNS mappings in the consumer project.

## Other considerations

This section contains considerations for common products and services not explicitly covered in this document.

### GKE control plane considerations

The GKE control plane is deployed in a Google managed tenant project that's connected to the customer's VPC using VPC Network Peering. Because VPC Network Peering isn't transitive, direct communication to the control plane over a hub and spoke VPC peered networking topology isn't possible.

When considering GKE design options, such as centralized or decentralized, direct access to the control plane from multicloud sources is a key consideration. If GKE is deployed in a centralized VPC, access to the control plane is available across clouds and within Google Cloud. However, if GKE is deployed in decentralized VPCs, direct communication to the control plane isn't possible. If an organization's requirements necessitate access to the GKE control plane in addition to adopting the decentralized design pattern, network administrators can deploy a [connect agent](https://docs.cloud.google.com/anthos/fleet-management/docs/connect-agent/what-uses-connect) that acts as a proxy, thus overcoming the non-transitive peering limitation to the GKE control plane.

### Security - VPC Service Controls

For workloads involving sensitive data, use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs) to configure service perimeters around your VPC resources and Google-managed services, and control the movement of data across the perimeter boundary. Using VPC Service Controls, you can group projects and your on-premises network into a single perimeter that prevents data access through Google-managed services. VPC Service Controls [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) can be used to allow projects and services in different service perimeters to communicate (including [VPC networks that aren't inside the perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-perimeters-management)).

For recommended deployment architectures, a comprehensive onboarding process, and operational best practices, see the [Best practices for VPC Service Controls for enterprises](https://docs.cloud.google.com/architecture/vpc-service-controls-enterprise-best-practices) and [Security Foundations Blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations).

### DNS for APIs/Services

Service producers can [publish services by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer). The service producer can optionally configure a DNS domain name to associate with the service. If a domain name is configured, and a [service consumer creates an endpoint that targets that service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services), Private Service Connect and Service Directory automatically create DNS entries for the service in a private DNS zone in the service consumer's VPC network.

## What's next

  * Design the [network security](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/security) for Cross-Cloud Network applications.
  * Learn more about the Google Cloud products used in this design guide: 
    * [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc)
    * [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc)
    * [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)
    * [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect)
    * [Private services access](https://docs.cloud.google.com/vpc/docs/private-services-access)
    * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)
    * [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
    * [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking
  * [Ghaleb Al-habian](https://www.linkedin.com/in/galhabian) | Network Specialist
  * Deepak Michael | Networking Specialist Customer Engineer
  * [Osvaldo Costa](https://www.linkedin.com/in/osvaldocostajr) | Networking Specialist Customer Engineer
  * [Jonathan Almaleh](https://www.linkedin.com/in/jonathan-almaleh) | Staff Technical Solutions Consultant



Other contributors: 

  * [Zach Seils](https://www.linkedin.com/in/zachseils) | Networking Specialist
  * [Christopher Abraham](https://www.linkedin.com/in/christopher-abraham-33291b) | Networking Specialist Customer Engineer
  * [Emanuele Mazza](https://www.linkedin.com/in/emanuelemazza) | Networking Product Specialist
  * [Aurélien Legrand](https://www.linkedin.com/in/aurelienlegrand) | Strategic Cloud Engineer
  * [Eric Yu](https://www.linkedin.com/in/eyu719) | Networking Specialist Customer Engineer
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking
  * [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer
  * [Ammett Williams](https://www.linkedin.com/in/ammett) | Developer Relations Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-30 UTC."],[],[]] 
