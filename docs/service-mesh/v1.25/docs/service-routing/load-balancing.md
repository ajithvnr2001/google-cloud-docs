---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/load-balancing/
title: Cloud Service Mesh load balancing \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:30:55.708095+00:00
---

# Cloud Service Mesh load balancing  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/load-balancing/

You are viewing archived v1.25 Service Mesh documentation.

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
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh load balancing

Cloud Service Mesh uses sidecar proxies or proxyless gRPC to deliver global load balancing for your internal microservices. You can deploy internal microservices (sidecar proxy-based or proxyless gRPC-based) with instances in multiple regions. Cloud Service Mesh provides health, routing, and backend information to the sidecar proxies or proxyless gRPC, enabling them to perform optimal traffic routing to application instances in multiple cloud regions for a service.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview).

In the following diagram, user traffic enters a Google Cloud deployment through an external global load balancer. The external load balancer distributes traffic to the Front End microservice in either `us-central1` or `asia-southeast1`, depending on the location of the end user.

The internal deployment features three global microservices: Front End, Shopping Cart, and Payments. Each service runs on managed instance groups (MIGs) in two regions, `us-central1` and `asia-southeast1`. Cloud Service Mesh uses a global load-balancing algorithm that directs traffic from the user in California to the microservices deployed in `us-central1`. Requests from the user in Singapore are directed to the microservices in `asia-southeast1`.

An incoming user request is routed to the Front End microservice. The service proxy installed on the host with the Front End then directs traffic to the Shopping Cart. The sidecar proxy installed on the host with the Shopping Cart directs traffic to the Payments microservice. In a proxyless gRPC environment, your gRPC application would handle traffic management.

[ ![Cloud Service Mesh in a global load-balancing deployment.](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/td-global-lb.svg)](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/td-global-lb.svg) Cloud Service Mesh in a global load-balancing deployment (click to enlarge)

In the following example, if Cloud Service Mesh receives health check results that indicate that the virtual machine (VM) instances running the Shopping Cart microservice in `us-central1` are unhealthy, Cloud Service Mesh instructs the sidecar proxy for the Front End microservices to fail over traffic to the Shopping Cart microservice running in `asia-southeast1`. Because autoscaling is integrated with traffic management in Google Cloud, Cloud Service Mesh notifies the MIG in `asia-southeast1` of the additional traffic, and the MIG increases in size.

Cloud Service Mesh detects that all backends of the Payments microservice are healthy, so Cloud Service Mesh instructs Envoy's proxy for the Shopping Cart to send a portion of the traffic—up to the customer's configured capacity—to `asia-southeast1` and overflow the rest to `us-central1`.

[ ![Failover with Cloud Service Mesh in a global load-balancing deployment.](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/td-global-lb-failover.svg)](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/td-global-lb-failover.svg) Failover with Cloud Service Mesh in a global load-balancing deployment (click to enlarge)

## Load-balancing components in Cloud Service Mesh

During Cloud Service Mesh setup, you configure several load-balancing components:

  * The backend service, which contains configuration values.
  * A health check, which provides health checking for the VMs and Google Kubernetes Engine (GKE) Pods in your deployment.
  * With the service routing APIs, a `Mesh` or `Gateway` resource and a `Route` resource.
  * With the load balancing APIs, a global forwarding rule, which includes the VIP address, a target proxy, and a URL map.



An xDS API-compatible sidecar proxy (such as Envoy) runs on a client VM instance or in a Kubernetes Pod. Cloud Service Mesh serves as the control plane and uses xDS APIs to communicate directly with each proxy. In the data plane, the application sends traffic to the VIP address configured in the forwarding rule or `Mesh` resource. The sidecar proxy or your gRPC application intercepts the traffic and redirects it to the appropriate backend.

The following diagram shows an application running on Compute Engine VMs or GKE Pods, the components, and the traffic flow in a Cloud Service Mesh deployment. It shows Cloud Service Mesh and the Cloud Load Balancing resources that are used to determine traffic routing. The diagram shows the older load balancing APIs.

[ ![Cloud Service Mesh resources to be configured.](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/td-resources.svg)](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/td-resources.svg) Cloud Service Mesh resources to be configured (click to enlarge)

## What's next

  * To learn about configuring advance load balancing features, see [Advanced load balancing overview](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/advanced-load-balancing-overview).
  * To learn more about service discovery and traffic interception, see [Cloud Service Mesh service discovery](https://docs.cloud.google.com/service-mesh/v1.25/docs/traffic-management/service-discovery).
  * To learn more about Cloud Service Mesh with the service routing APIs, see the [overview](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
