---
url: https://docs.cloud.google.com/service-mesh/v1.21/docs/overview/
title: Cloud Service Mesh overview \u00a0|\u00a0 Cloud Service Mesh v1.21 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:02.030232+00:00
---

# Cloud Service Mesh overview  |  Cloud Service Mesh v1.21  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.21/docs/overview/

You are viewing archived v1.21 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.21 ](https://docs.cloud.google.com/service-mesh/v1.21/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.21/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh overview

Cloud Service Mesh is a service mesh available on Google Cloud and across supported GKE Enterprise platforms. It supports services running on a range of computing infrastructures. Cloud Service Mesh is controlled by APIs designed for Google Cloud, for open source, or for both.

This document is for you if you're a new Cloud Service Mesh user or a continuing Anthos Service Mesh or Traffic Director customer.

## What is a service mesh?

A service mesh is an architecture that enables managed, observable, and secure communication among your services, making it easier for you to create robust enterprise applications made up of many microservices on your chosen infrastructure. Service meshes manage the common requirements of running a service, such as monitoring, networking, and security, with consistent, powerful tools, making it easier for service developers and operators to focus on creating and managing great applications for their users.

Architecturally, a service mesh consists of one or more control planes and a data plane. The service mesh monitors all traffic into and out of your services. On Kubernetes, a proxy is deployed by a [sidecar pattern](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) to the microservices in the mesh. On Compute Engine, you can deploy proxies on VMs or use proxyless gRPC for the data plane.

This pattern decouples application or business logic from network functions, and enables developers to focus on the features that the business needs. Service meshes also let operations teams and development teams decouple their work from one another.

Architecting your applications as microservices provides many benefits. However, your workloads can become more complex and fragmented as they scale. Service mesh helps solve the fragmentation problem and makes it easier to manage your microservices.

## What is Cloud Service Mesh?

Cloud Service Mesh is Google's solution for both Google Cloud and supported GKE Enterprise environments.

  * On Google Cloud: Cloud Service Mesh provides APIs that are specific to the computing infrastructure on which your workloads run. 
    * For Compute Engine workloads, Cloud Service Mesh uses [Google Cloud-specific service routing APIs](https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/service-routing-overview).
    * For Google Kubernetes Engine (GKE) workloads, Cloud Service Mesh uses the open source Istio APIs.
  * Off Google Cloud: With Distributed Cloud or GKE multicloud, Cloud Service Mesh supports the Istio APIs for Kubernetes workloads.



Whether on or off Google Cloud, Cloud Service Mesh lets you manage, observe, and secure your services without having to change your application code.

Cloud Service Mesh reduces the toil for your operations and development teams by simplifying service delivery, from traffic management and mesh telemetry to securing communications between services. Google's fully managed service mesh lets you manage complex environments and enjoy the benefits they promise.

## Features

Cloud Service Mesh has a suite of features for traffic management, observability and telemetry, and security.

### Traffic management

Cloud Service Mesh controls the flow of traffic among services in the mesh, into the mesh (ingress), and to outside services (egress). You configure and deploy resources to manage this traffic at the application (L7) layer. For example, you can do the following:

  * Use service discovery.
  * Configure load balancing among services.
  * Create canary and blue-green deployments.
  * Finely control routing for your services.
  * Set up circuit breakers.



Cloud Service Mesh maintains a list of all services in the mesh by name and by their respective endpoints. It maintains this list to manage the flow of traffic (for example, Kubernetes Pod IP addresses or the IP addresses of Compute Engine VMs in a [Managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups)). By using this service registry, and by running the proxies side-by-side with the services, the mesh can direct traffic to the appropriate endpoint. [Proxyless gRPC workloads](https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/proxyless-overview) can also be used in parallel with workloads using Envoy proxies.

### Observability insights

The Cloud Service Mesh user interface in the Google Cloud console provides insights into your service mesh. These metrics are automatically generated for workloads configured through the Istio APIs.

  * Service metrics and logs for HTTP traffic within your mesh's GKE cluster are automatically ingested to Google Cloud.
  * Preconfigured service dashboards give you the information you need to understand your services.
  * In-depth telemetry—powered by [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs), [Cloud Logging](https://docs.cloud.google.com/logging/docs), and [Cloud Trace](https://docs.cloud.google.com/trace/docs)—lets you dig deep into your service metrics and logs. You can filter and segment your data on a wide variety of attributes.
  * Service-to-service relationships help you understand at a glance inter-service dependences and who connects to each service.
  * You can quickly see the communication security posture not only of your service, but its relationships to other services.
  * Service level objectives (SLOs) give you insight into the health of your services. You can define an SLO and alert on your own standards of service health.



Learn more about Cloud Service Meshs observability features in our [Observability guide](https://docs.cloud.google.com/service-mesh/v1.21/docs/observability-overview).

### Security benefits

Cloud Service Mesh provides you with many security benefits.

  * Mitigates risk of replay or impersonation attacks that use stolen credentials. Cloud Service Mesh relies on mutual TLS (mTLS) certificates to authenticate peers, rather than bearer tokens such as [JSON Web Tokens (JWT)](https://jwt.io/introduction/).
  * Ensures encryption in transit. Using mTLS for authentication also ensures that all TCP communications are encrypted in transit.
  * Mitigates the risk that unauthorized clients can access a service with sensitive data, irrespective of the network location of the client and the application-level credentials.
  * Mitigates the risk of user data breach within your production network. You can ensure that insiders can only access sensitive data through authorized clients.
  * Identifies which clients accessed a service with sensitive data. Cloud Service Mesh access logging captures the mTLS identity of the client in addition to the IP address.
  * All in-cluster control plane components are built with [FIPS 140-2 validated](https://cloud.google.com/security/compliance/fips-140-2-validated) encryption modules.



Learn more about Service Mesh's security benefits and features in the [Security guide](https://docs.cloud.google.com/service-mesh/v1.21/docs/security/security-overview).

### Deployment options

You have the following deployment options in Cloud Service Mesh:

  * On Google Cloud 
    * Managed Cloud Service Mesh - managed control and data plane for GKE (recommended)
    * Managed Cloud Service Mesh - managed control and data plane for Compute Engine with VMs (recommended)
    * In-cluster control plane for GKE with Istio APIs (Discouraged)
  * Off Google Cloud 
    * In-cluster control plane for Kubernetes with Istio APIs



## Managed Cloud Service Mesh

Managed Cloud Service Mesh consists of the managed control plane for all infrastructures and the managed data plane for GKE. With Managed Cloud Service Mesh, Google handles upgrades, scaling, and security for you, minimizing manual user maintenance. This covers the control plane, data plane, and related resources.

### Data plane implementation

If you use Google Cloud APIs, your data plane can be provided by Envoy proxies or by proxyless gRPC applications. If you are updating an existing application, the sidecar-based approach allows for integration into the mesh without changing your application. If you want to avoid the overhead of running a sidecar, you can update your application to use gRPC.

Envoy proxies and proxyless gRPC both use the xDS API to connect to the control plane. If you use proxyless gRPC, you have a choice of supported languages for your applications, including Go, C++, Java, and Python.

If you use open source Istio APIs, your data plane is provided by Envoy proxies.

### Control plane implementation

Your Cloud Service Mesh control plane depends on whether your configuration is on or off Google Cloud and whether you are a new customer.

#### Control plane implementation for existing users

  * If your configuration is off Google Cloud, you are using Cloud Service Mesh's in-cluster, unmanaged control plane. For more information, see [In-cluster control plane supported features](https://docs.cloud.google.com/service-mesh/v1.21/docs/supported-features-in-cluster).
  * If you were an Anthos Service Mesh user on Google Cloud, you are using Istio APIs. For more information, see [Supported features using Istio APIs (managed control plane) ](https://docs.cloud.google.com/service-mesh/v1.21/docs/supported-features-managed).
  * If you were a Traffic Director user, you are using Cloud Service Mesh's managed control plane with Google Cloud APIs. For more information, see [Cloud Service Mesh with Google Cloud APIs supported features](https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/features).



To determine your current control plane, read [Identify control plane implementation](https://docs.cloud.google.com/service-mesh/v1.21/docs/supported-features-managed#identify_control_plane_implementation). For more information on control planes and control plane migration, see [Managed control plane overview for continuing customers](https://docs.cloud.google.com/service-mesh/v1.21/docs/overview/).

#### Control plane implementation for new users

  * If you are planning an off-Google Cloud configuration, you are choosing Cloud Service Mesh's in-cluster, unmanaged control plane. For more information, see [In-cluster control plane supported features](https://docs.cloud.google.com/service-mesh/v1.21/docs/supported-features-in-cluster).
  * If you are planning an on-Google Cloud configuration on Kubernetes, you are choosing Istio APIs, but your control plane uses the Traffic Director implementation, except in certain cases that are detailed in [What determines control plane implementation](https://docs.cloud.google.com/service-mesh/v1.21/docs/supported-features-managed#what_determines_control_plane_implementation). See [Supported features using Istio APIs (managed control plane)](https://docs.cloud.google.com/service-mesh/v1.21/docs/supported-features-managed) for more details.
  * If you are planning an on-Google Cloud configuration on Compute Engine VMs, your control plane uses the global, multi-tenant control plane, known as the Traffic Director implementation. For more information, see [Cloud Service Mesh with Google Cloud APIs supported features](https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/features).



### Control plane migration

If you are a continuing Anthos Service Mesh customer and you use the Istio APIs, your clusters will start migrating to the Traffic Director control plane. You can continue to use the Istio APIs for configuration.

To determine whether your clusters still use the Istio control plane or have migrated to the new global control plane, read [Identify control plane implementation](https://docs.cloud.google.com/service-mesh/v1.21/docs/supported-features-managed#identify_control_plane_implementation).

## What's next

  * If you're a continuing user, read [Managed control plane for continuing customers](https://docs.cloud.google.com/service-mesh/v1.21/docs/managed-control-plane-overview).
  * If you plan to set up with GKE, read [Provision a control plane](https://docs.cloud.google.com/service-mesh/v1.21/docs/onboarding/provision-control-plane).
  * If you plan to set up with Compute Engine and VMs, read [Prepare to set up on service routing APIs with Envoy and proxyless workloads](https://docs.cloud.google.com/service-mesh/v1.21/docs/onboarding/prepare-service-routing-envoy-proxyless).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
