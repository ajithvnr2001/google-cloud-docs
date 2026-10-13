---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/multi-environment-overview/
title: Cloud Service Mesh with hybrid connectivity network endpoint groups \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:05:03.051933+00:00
---

# Cloud Service Mesh with hybrid connectivity network endpoint groups  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/multi-environment-overview/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh with hybrid connectivity network endpoint groups

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

Cloud Service Mesh supports environments that extend beyond Google Cloud, including on-premises data centers and other public clouds that you can use [hybrid connectivity](https://cloud.google.com/hybrid-connectivity) to reach.

You configure Cloud Service Mesh so that your service mesh can send traffic to endpoints that are outside of Google Cloud. These endpoints include the following:

  * On-premises load balancers.
  * Server applications on a virtual machine (VM) instance in another cloud.
  * Any other destination that you can reach with hybrid connectivity and that can be reached with an IP address and a port.



You add each endpoint's IP address and port to a hybrid connectivity network endpoint group (NEG). Hybrid connectivity NEGs are of type `NON_GCP_PRIVATE_IP_PORT`.

Cloud Service Mesh's support for on-premises and multi-cloud services lets you do the following:

  * Route traffic globally, including to the endpoints of on-premises and multi-cloud services.
  * Bring the benefits of Cloud Service Mesh and service mesh—including capabilities such as service discovery and advanced traffic management—to services running on your existing infrastructure outside of Google Cloud.
  * Combine Cloud Service Mesh capabilities with Cloud Load Balancing to bring Google Cloud networking services to multi-environments.



Hybrid connectivity NEGs (`NON_GCP_PRIVATE_IP_PORT` NEGs) are not supported with proxyless gRPC clients.

## Use cases

Cloud Service Mesh can configure networking between VM-based and container-based services in multiple environments, including:

  * Google Cloud
  * On-premises data centers
  * Other public clouds



### Route mesh traffic to an on-premises location or another cloud

The simplest use case for this feature is traffic routing. Your application is running a Cloud Service Mesh Envoy proxy . Cloud Service Mesh tells the client about your services and each service's endpoints.

[ ![Routing mesh traffic to an on-premises location or another cloud.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-on-prem-route-cloud.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-on-prem-route-cloud.svg) Routing mesh traffic to an on-premises location or another cloud (click to enlarge)

In the preceding diagram, when your application sends a request to the `on-prem` service, the Cloud Service Mesh client inspects the outbound request and updates its destination. The destination gets set to an endpoint associated with the `on-prem` service (in this case, `10.2.0.1`). The request then travels over [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) to its intended destination.

If you need to add more endpoints, you update Cloud Service Mesh to add them to your service. You don't need to change your application code.

### Migrate an existing on-premises service to Google Cloud

Sending traffic to a non-Google Cloud endpoint lets you route traffic to other environments. You can combine this capability with advanced traffic management to migrate services between environments.

[ ![Migrating from an on-premises location to Google Cloud.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-on-prem-migrate.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-on-prem-migrate.svg) Migrating from an on-premises location to Google Cloud (click to enlarge)

The preceding diagram extends the previous pattern. Instead of configuring Cloud Service Mesh to send all traffic to the `on-prem` service, you configure Cloud Service Mesh to use weight-based traffic splitting to split traffic across two services.

Traffic splitting lets you start by sending 0% of traffic to the `cloud` service and 100% to the `on-prem` service. You can then gradually increase the proportion of traffic sent to the `cloud` service. Eventually, you send 100% of traffic to the `cloud` service, and you can retire the `on-prem` service.

### Google Cloud network edge services for on-premises and multi-cloud deployments

Finally, you can combine this functionality with Google Cloud's existing networking solutions. Google Cloud offers a wide range of network services, such as global external load balancing with Google Cloud Armor for distributed denial-of-service (DDoS) protection, that you can use with Cloud Service Mesh to bring new capabilities to your on-premises or multi-cloud services. Best of all, you don't need to expose these on-premises or multi-cloud services to the public internet.

[ ![Deployments spanning multiple environments.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-on-prem-mesh2.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-on-prem-mesh2.svg) Deployments spanning multiple environments (click to enlarge)

In the preceding diagram, traffic from clients on the public internet enters Google Cloud's network from a Google Cloud load balancer, such as our global external Application Load Balancer. When traffic reaches the load balancer, you can apply network edge services such as Cloud Armor DDoS protection or Identity-Aware Proxy (IAP) user authentication. For more information, see [Network edge services for multi-environment deployments](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/network-edge-services-multi-environment).

After you apply these services, the traffic makes a brief stop in Google Cloud, where an application or standalone proxy (configured by Cloud Service Mesh) forwards the traffic across Cloud VPN or Cloud Interconnect to your on-premises service.

## Google Cloud resources and architecture

This section provides background information about the Google Cloud resources that you can use to provide a Cloud Service Mesh-managed service mesh for on-premises and multi-cloud environments.

The following diagram depicts the Google Cloud resources that enable on-premises and multi-cloud services support for Cloud Service Mesh. The key resource is the NEG and its network endpoints. The other resources are the resources that you configure as part of a standard Cloud Service Mesh setup. For simplicity, the diagram does not show options such as multiple global backend services.

[ ![Compute Engine resources for on-premises and multi-cloud services.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-on-prem-resources.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-on-prem-resources.svg) Compute Engine resources for on-premises and multi-cloud services (click to enlarge)

When you configure Cloud Service Mesh, you use the global backend services API resource to create services. A service is a logical construct that combines the following:

  1. Policies to apply when a client tries to send traffic to the service.
  2. One or more backends or endpoints that handle the traffic that is destined for the service.



On-premises and multi-cloud services are like any other service that Cloud Service Mesh configures. The key difference is that you use a _hybrid connectivity NEG_ to configure the endpoints of these services. These NEGs have the _network endpoint type_ set to `NON_GCP_PRIVATE_IP_PORT`. The endpoints that you add to hybrid connectivity NEGs must be valid `IP:port` combinations that your clients can reach—for example, through hybrid connectivity such as Cloud VPN or Cloud Interconnect.

Each NEG has a network endpoint type and can only contain network endpoints of the same type. This type determines the following:

  * The destination to which your services can send traffic.
  * Health checking behavior.



When you create your NEG, configure it as follows so that you can send traffic to an on-premises or multi-cloud destination.

**Note:** Hybrid connectivity NEGs are not supported in the Google Cloud console. To create or delete hybrid connectivity NEGs, you must use the Google Cloud CLI.

  * Set the network endpoint type to `NON_GCP_PRIVATE_IP_PORT`. This represents a reachable IP address. If this IP address is on-premises or at another cloud provider, it must be reachable from Google Cloud by using hybrid connectivity, such as the connectivity provided by Cloud VPN or Cloud Interconnect.
  * [Specify a Google Cloud _zone_](https://docs.cloud.google.com/compute/docs/regions-zones#locations) that minimizes the geographic distance between Google Cloud and your on-premises or multi-cloud environment. For example, if you are hosting a service in an on-premises environment in Frankfurt, Germany, you can specify the `europe-west3-a` Google Cloud zone when you create the NEG.



Health checking behavior for network endpoints of this type differs from health checking behavior for other types of network endpoints. While other network endpoint types use Google Cloud's centralized health checking system, `NON_GCP_PRIVATE_IP_PORT` network endpoints use Envoy's distributed health checking mechanism. For more details, see the Limitations and other considerations section.

## Connectivity and networking considerations

Your Cloud Service Mesh clients, such as Envoy proxies, must be able to connect to Cloud Service Mesh at `trafficdirector.googleapis.com:443`. If you lose connectivity to the Cloud Service Mesh control plane, the following happens:

  * Existing Cloud Service Mesh clients cannot receive configuration updates from Cloud Service Mesh. They continue to operate based on their current configuration.
  * New Cloud Service Mesh clients cannot connect to Cloud Service Mesh. They cannot use the service mesh until connectivity is re-established.



If you want to send traffic between Google Cloud and on-premises or multi-cloud environments, the environments must be connected through hybrid connectivity. We recommend a high availability connection enabled by Cloud VPN or Cloud Interconnect.

On-premises, other cloud, and Google Cloud subnet IP addresses and IP address ranges must not overlap.

## Limitations and other considerations

The following are limitations of using hybrid connectivity NEGs.

### Setting `proxyBind`

You can only set the value of `proxyBind` when you create a `targetHttpProxy`. You can't update an existing `targetHttpProxy`.

### Connectivity and disruption to connectivity

For details about connectivity requirements and limitations, see the Connectivity and networking considerations section.

### Mixed backend types

A backend service can have VM or NEG backends. If a backend service has NEG backends, all NEGs must contain the same network endpoint type. You cannot have a backend service with multiple NEGs, each with different endpoint types.

A URL map can have host rules that resolve to different backend services. You might have a backend service with only hybrid connectivity NEGs (with on-premises endpoints) and a backend service with standalone NEGs (with GKE endpoints). The URL map can contain rules, for example, weight-based traffic splitting, that split traffic across each of these backend services.

### Using a NEG with endpoints of type `NON_GCP_PRIVATE_IP_PORT` with Google Cloud backends

It is possible to create a backend service with a hybrid connectivity NEG that points to backends in Google Cloud. However, we do not recommend this pattern because hybrid connectivity NEGs don't benefit from centralized health checking. For an explanation of centralized health checking and distributed health checking, see the Health checking section.

### Endpoint registration

If you want to add an endpoint to a NEG, you must update the NEG. This can either be done manually, or it can be automated by using the Google Cloud NEG REST APIs or the Google Cloud CLI.

When a new instance of a service starts, you can use the Google Cloud APIs to register the instance with the NEG that you configured. When using Compute Engine managed instance groups (MIGs) or GKE (in Google Cloud), the MIG or NEG controller automatically handles endpoint registration, respectively.

### Health checking

When you use hybrid connectivity NEGs, health checking behavior differs from the standard centralized health checking behavior in the following ways:

  * For network endpoints of type `NON_GCP_PRIVATE_IP_PORT`, Cloud Service Mesh configures its clients to use the data plane to handle health checking. To avoid sending requests to unhealthy backends, Envoy instances [perform their own health checks and use their own mechanisms](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/health_checking#arch-overview-health-checking).
  * Because your data plane handles health checks, you cannot use the Google Cloud console, the API, or the Google Cloud CLI to retrieve health check status.



In practice, using `NON_GCP_PRIVATE_IP_PORT` means the following:

  * Because Cloud Service Mesh clients each handle health checking in a distributed fashion, you might see an increase in network traffic because of health checking. The increase depends on the number of Cloud Service Mesh clients and the number of endpoints that each client needs to health check. For example: 
    * When you add another endpoint to a hybrid connectivity NEG, existing Cloud Service Mesh clients might begin to health check the endpoints in hybrid connectivity NEGs.
    * When you add another instance to your service mesh (for example, a VM instance that runs your application code as well as a Cloud Service Mesh client), the new instance might begin to health check the endpoints in hybrid connectivity NEGs.
    * Network traffic because of health checks increases at a quadratic (`O(n^2)`) rate.



### VPC network

A service mesh is uniquely identified by its Virtual Private Cloud (VPC) network name. Cloud Service Mesh clients receive configuration from Cloud Service Mesh based on the VPC network specified in the bootstrap configuration. Therefore, even if your mesh is entirely outside of a Google Cloud data center, you must supply a valid VPC network name in your bootstrap configuration.

### Service account

Within Google Cloud, the default Envoy bootstrap is configured to read service account information from either or both of the Compute Engine and GKE deployment environments. When running outside of Google Cloud, you must explicitly specify a service account, network name, and project number in your Envoy bootstrap. This service account must have [sufficient permissions to connect with the Cloud Service Mesh API](https://docs.cloud.google.com/service-mesh/docs/service-routing/prepare-for-envoy-setup#grant-permissions).

## What's next

  * To configure Cloud Service Mesh for on-premises and multi-cloud deployments, see [Network edge services for multi-environment deployments](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/network-edge-services-multi-environment).
  * To learn more about Cloud Service Mesh, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/service-routing/overview).
  * To learn about internet NEGs, see [Cloud Service Mesh with internet network endpoint groups](https://docs.cloud.google.com/service-mesh/docs/service-routing/internet-negs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
