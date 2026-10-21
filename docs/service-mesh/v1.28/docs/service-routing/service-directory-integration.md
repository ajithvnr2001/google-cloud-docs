---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/service-directory-integration/
title: Cloud Service Mesh integration with Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:03.149986+00:00
---

# Cloud Service Mesh integration with Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/service-directory-integration/

You are viewing v1.28 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh integration with Service Directory

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Deprecated:** Cloud Service Mesh's integration with Service Directory is going to be deprecated. Creating new service binding resources will be disabled.

This document provides an overview of how to use Service Directory's service registry with Cloud Service Mesh, which lets Cloud Service Mesh route traffic to and apply traffic policies to services registered with Service Directory. This document is for Cloud Service Mesh developers who want to integrate their applications with other services in Google Cloud.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview).

[Service Directory](https://docs.cloud.google.com/service-directory) is a _service registry_ that stores information about network services that are registered with it, including their names, locations, and attributes. You can register your services automatically, capturing all details, and all services can be registered, regardless of their infrastructure.

The registry can contain not only Google Cloud services, but also hybrid services running on-premises or in other public clouds. To best understand the information in this document, we recommend that you familiarize yourself with [the basics of Service Directory operations](https://docs.cloud.google.com/service-directory/docs/overview).

When you use Service Directory's service registry with Cloud Service Mesh, the integration makes services in the service registry available to the applications in your mesh and to gateways configured by Cloud Service Mesh. [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)'s integration with Service Directory is supported, with Envoy and with proxyless gRPC, for Service Directory integrations with [internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal), [internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal), and [L4 Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).

To integrate your services, you register a service with Service Directory, then bind the service to a Cloud Service Mesh backend service. After a binding is established, Cloud Service Mesh queries Service Directory to obtain information about the registered service and how that service can be reached. Cloud Service Mesh also tracks any changes to the service. Using the integration allows your service mesh and self- managed gateway to send traffic to these services. It also lets you enforce policies—for example, advanced traffic management policies—that you configure in Cloud Service Mesh.

When you use this integration, the service binding acts as a backend, regardless of the type of backend used by the service itself. The integration simplifies your Cloud Service Mesh deployment, because Cloud Service Mesh can send traffic to the service without regard to the type of backend.

When a service is registered with Service Directory, you don't need to configure instance groups or different types of network endpoint groups (NEGs) to get access to services you need. You can automatically register Google Kubernetes Engine, internal load balancers, and Private Service Connect to Service Directory, further simplifying Cloud Service Mesh's access to these services.

## Resources used by the integration

The integration between Cloud Service Mesh and Service Directory uses the following resources.

### Service Directory services

Service Directory is a service registry. Service Directory lets you register various types of services, including services based in Google Cloud or other environments (for example, an on-premises data center). Each service consists of a unique name and zero or more service endpoints. A service endpoint consists of an address, port, properties, and metadata. If there are zero endpoints,you cannot route traffic to the service.

### Service bindings

A _service binding_ is a resource that includes the fully qualified domain name (FQDN) of the Service Directory service. For example, `projects/test-proj/locations/us-east1/namespaces/test-namespace/services/test-service` is an FQDN for a Service Directory service.

### Backend services

Backend services are configuration resources that provide information to Cloud Service Mesh, including the backends, such as managed instance groups, to which the backend service routes traffic. Backend services that reference service bindings cannot have backends. To use the Cloud Service Mesh integration with Service Directory, you create a new backend service to reference service bindings.

A backend service can have multiple service bindings. This configuration is useful in a situation where you have regional deployments of the same application. You might register each regional deployment to a regional instance of Service Directory, as regional service 1 and regional service 2. Each of these regional Service Directory services can then be associated with the same backend service, using two service bindings. Global service binding 1 would be associated with regional service 1 in region A and global service binding 2 would be associated with regional service 2 in region B.

## Use cases

Integrating your Cloud Service Mesh deployment with Service Directory enables new use cases that are helpful when you depend on services that other teams or organizations own or publish.

### Make existing services available to Cloud Service Mesh

Service Directory integrates with Google Cloud products such as GKE, internal passthrough Network Load Balancers, and internal Application Load Balancers. When service producers create a GKE service or a load balancer, they can register it with Service Directory.

After a service is registered with Service Directory, you can configure Cloud Service Mesh to communicate with that service. Cloud Service Mesh clients can then communicate with services that run behind internal passthrough Network Load Balancers and internal Application Load Balancers.

### Improve coordination between service producers and consumers

Large enterprises have many independent developer teams. These teams make their services available to other teams so that more teams can use the capabilities provided by the shared service. This creates cross-team dependencies. While these dependencies enable teams to share their efforts, dependencies also create coordination overhead.

When you use Service Directory, one team (the _producer_) registers a service that it wants to make available to other teams or organizations (_consumers_). The producer shares a reference to this service with a consumer. The consumer can use this reference to look up the producer's service in Service Directory and discover the service's endpoints. For example, the endpoint might be a virtual IP address (VIP) on which the producer's service expects to receive traffic.

Cloud Service Mesh's integration with Service Directory lets you automate the process by binding a Service Directory service to a Cloud Service Mesh backend service, which has the following advantages:

  * Cloud Service Mesh automatically resolves the service's endpoints by synchronizing them from Service Directory. If the Service Directory service's endpoints are updated, Cloud Service Mesh automatically synchronizes these changes.
  * You can set various routing and traffic management policies, such as timeouts, in Cloud Service Mesh. These policies let you fine-tune how your applications issue requests to the Service Directory service. For information about routing and traffic management in Cloud Service Mesh, see [Advanced traffic management](https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/advanced-traffic-management).
  * Cloud Service Mesh uses traffic management capabilities such as proximity-based load balancing to optimally direct traffic from applications to endpoints—for example, by minimizing round-trip time.

[ ![Using Service Directory for service discovery.](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/service-discovery.svg)](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/service-discovery.svg) Using Service Directory for service discovery (click to enlarge)

When you, a consumer, use Cloud Service Mesh and attach a backend service to a Service Directory service, cross-team coordination overhead is reduced.

  * You attach the service, `Payments`, by name.
  * Cloud Service Mesh shares information about the `Payments` service with its clients.

    * For example, the sidecar proxies running in your service mesh now know the endpoint (for example `10.0.0.1:80`) at which the service can be reached.
  * Your applications can call this service by name without you or your application needing to know anything about the external service's endpoint. In the diagram, the service is the `Payments` service.

  * When the service producer updates the external service (for example, changing its endpoint), Cloud Service Mesh picks up the update and seamlessly shares it with its clients.




### Access services within a perimeter using an ingress point

A team might group a collection of services within a VPC Service Controls _perimeter_ and expose those services through a single ingress point. This ingress point can be registered to Service Directory and made available to users who want to access the services within the perimeter. For more information about VPC Service Controls perimeters, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

For example, a team creates an ingress gateway by using an internal Application Load Balancer that distributes requests to a collection of Kubernetes services in a cluster. This ingress gateway is automatically registered as a service to Service Directory. A consumer who wants to access the Kubernetes services can look up this ingress gateway in Service Directory. The consumer can then configure the Cloud Service Mesh mesh to access services within the perimeter through the gateway.

### Connect services across domains

You might have services in different domains that you need to connect.

#### Connect services across organizations

You might want access to services owned by another organization, such as Google APIs (for example, Cloud SQL) or third-party managed services.

Service Directory supports [Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-consumer#ip-address-requirements). When you create a Private Service Connect endpoint in your network, the endpoint can be registered as a service with Service Directory. You can then attach this service to Cloud Service Mesh, so that mesh clients, such as Envoy and gRPC clients, and self-managed gateways, such as Apigee, can call on these services.

[ ![Using Service Directory for service discovery with Private Service Connect.](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/service-discovery-psc.svg)](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/service-discovery-psc.svg) Using Service Directory for service discovery with Private Service Connect (click to enlarge)

The preceding example, using Cloud Storage, illustrates how you can use Private Service Connect to call Google APIs using an endpoint in your Virtual Private Cloud network.

#### Connect services across VPC networks

Some companies use multiple VPC networks as part of their Google Cloud deployment. In such cases, a service in one VPC network might need to access a service in a different VPC network. You can configure VPC peering to access a service in a different VPC network, but this configuration creates complications when there are overlapping IP address ranges between peered networks.

Private Service Connect can securely and privately make a service in one VPC network accessible to services in another VPC network, using a single `IP:port` endpoint.

[ ![Detailed view of using Service Directory for service discovery with Private Service Connect.](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/service-discovery-detail.svg)](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/service-discovery-detail.svg) Detailed view of using Service Directory for service discovery with Private Service Connect (click to enlarge)

#### Additional examples across domains

The previous two examples illustrate cases where you might need to cross domains, but there are many additional examples. For example, you create a gateway that sits at the intersection of two Google Cloud regions. Services in one region can reach services in another region through this gateway. You register the gateway as a service in Service Directory, then use the gateway with Cloud Service Mesh as described in this document.

### Apply policies when services are accessed

Cloud Service Mesh supports capabilities such as advanced traffic management that are configurable using policies. For example, you can set a traffic mirroring policy so that anytime a client sends a request to a particular backend service, the traffic also gets sent to a second backend service.

When you bind a Service Directory service to a Cloud Service Mesh backend service, you can configure these types of policies in Cloud Service Mesh. Your sidecar proxies, middle or edge proxies, and proxyless clients learn about these policies and enforce them.

Some examples:

  * Weight-based traffic splitting—for example, between two Service Directory services
  * Traffic mirroring—for example, to an audit service

[ ![Requests for `users` service are mirrored to `audit` service](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/traffic-management-policies.svg)](https://docs.cloud.google.com/static/service-mesh/v1.28/docs/images/traffic-management-policies.svg) Requests for `users` service are mirrored to `audit` service (click to enlarge)

## Support for Cloud Service Mesh and existing clients

Even when Cloud Service Mesh is deployed in your organization, you might have clients that don't use Cloud Service Mesh. For example, you might need to access a service from a virtual machine that isn't part of a service mesh.

When you bind a Service Directory service to a Cloud Service Mesh backend service, Cloud Service Mesh's clients automatically get up-to-date information about that service. Your clients that don't use Cloud Service Mesh can look up and use service information in Service Directory.

## Limitations

Cloud Service Mesh does not support FQDN NEGs (`INTERNET_FQDN_PORT` NEGs) in the Service Directory integration.

## What's next

  * Learn to [set up the integration](https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/service-directory-integration-setup).
  * For information about observability with this integration, see [Observability and debugging with Service Directory](https://docs.cloud.google.com/service-mesh/v1.28/docs/service-routing/service-directory-observability).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
