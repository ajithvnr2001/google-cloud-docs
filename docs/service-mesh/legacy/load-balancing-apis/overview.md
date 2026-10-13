---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/overview/
title: Cloud Service Mesh overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:57.729791+00:00
---

# Cloud Service Mesh overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/overview/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh overview

This document is for network administrators and service owners who want to familiarize themselves with Cloud Service Mesh and its capabilities. This is a legacy document that applies to configurations using the load balancing APIs.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

Cloud Service Mesh is a managed control plane for application networking. Cloud Service Mesh lets you deliver global, highly available services with advanced application networking capabilities such as traffic management and observability.

As the number of services and microservices in your deployment grows, you typically start to encounter common application networking challenges such as the following:

  * How do I make my services resilient?
  * How do I get traffic to my services, and how do services know about and communicate with each other?
  * How do I understand what is happening when my services are communicating with each other?
  * How do I update my services without risking an outage?
  * How do I manage the infrastructure that makes my deployment possible?

[ ![Services need to communicate with each other.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-services-communication.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-services-communication.svg) Services need to communicate with each other (click to enlarge)

Cloud Service Mesh helps you solve these types of challenges in a modern, service-based deployment. Cloud Service Mesh relies on Google Cloud-managed infrastructure so that you don't have to manage your own infrastructure. You focus on shipping application code that solves your business problems while letting Cloud Service Mesh manage the application networking complexities.

## Cloud Service Mesh

A common pattern for solving application networking challenges is to use a service mesh. Cloud Service Mesh supports service mesh and other deployment patterns that fit your needs.

[ ![A typical service mesh.](https://docs.cloud.google.com/static/service-mesh/docs/images/service-mesh.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/service-mesh.svg) A typical service mesh (click to enlarge)

In a typical service mesh, the following is true:

  * You deploy your services to a Kubernetes cluster.
  * Each of the services' Pods has a dedicated proxy (usually [Envoy](https://www.envoyproxy.io/)) running as a _sidecar proxy_.
  * Each sidecar proxy talks to the networking infrastructure (a _control plane_) that is installed in your cluster. The control plane tells the sidecar proxies about services, endpoints, and policies in your service mesh.
  * When a Pod sends or receives a request, the request goes to the Pod's sidecar proxy. The sidecar proxy handles the request, for example, by sending it to its intended destination.



In the diagrams in this document and other Cloud Service Mesh documents, the six- sided pink icons represent the proxies. The control plane is connected to each proxy and provides information that the proxies need to handle requests. Arrows between boxes show traffic flows. For example, application code in `Service A` sends a request. The proxy handles the request and forwards it to `Service B`.

This model lets you move networking logic out of your application code. You can focus on delivering business value while letting your infrastructure take care of application networking.

### How Cloud Service Mesh is different

Cloud Service Mesh works similarly to that model, but it's different in important ways. It all starts with the fact that Cloud Service Mesh is a Google Cloud-managed service. You don't install it, it doesn't run in your cluster, and you don't need to maintain it.

In the following diagram, Cloud Service Mesh is the control plane. There are four services in this Kubernetes cluster, each with sidecar proxies that are connected to Cloud Service Mesh. Cloud Service Mesh provides the information that the proxies need to route requests. For example, application code on a Pod that belongs to `Service A` sends a request. The sidecar proxy running alongside this Pod handles the request and routes it to a Pod that belongs to `Service B`.

[ ![An example of a service mesh with Cloud Service Mesh.](https://docs.cloud.google.com/static/service-mesh/docs/images/service-mesh-td.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/service-mesh-td.svg) An example of a service mesh with Cloud Service Mesh (click to enlarge)

## Beyond service mesh

Cloud Service Mesh supports more types of deployments than a typical service mesh.

### Multi-cluster Kubernetes

With Cloud Service Mesh, you get application networking that works across Kubernetes clusters. In the following diagram, Cloud Service Mesh provides the control plane for Kubernetes clusters in `us-central1` and `europe-west1`. Requests can be routed among the three services in `us-central1`, among the two services in `europe-west1`, and between services in the two clusters.

[ ![An example of multi-cluster Kubernetes with Cloud Service Mesh.](https://docs.cloud.google.com/static/service-mesh/docs/images/multi-cluster-service-mesh.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/multi-cluster-service-mesh.svg) An example of multi-cluster Kubernetes with Cloud Service Mesh (click to enlarge)

Your service mesh can extend across multiple Kubernetes clusters in multiple Google Cloud regions. Services in one cluster can talk to services in another cluster. You can even have services that consist of Pods in multiple clusters.

With Cloud Service Mesh's proximity-based global load balancing, requests destined for `Service B` go to the nearest Pod that can serve the request. You also get seamless failover; if a Pod is down, the request automatically fails over to another Pod that can serve the request, even if this Pod is in a different Kubernetes cluster.

### Virtual machines

Kubernetes is becoming increasingly popular, but many workloads are deployed to virtual machine (VM) instances. Cloud Service Mesh solves application networking for these workloads, too; your VM-based workloads interoperate with your Kubernetes-based workloads.

In the following diagram, traffic enters your deployment through the external Application Load Balancer. It is routed to `Service A` in the Kubernetes cluster in `asia-southeast1` and to `Service D` on a VM in `europe-west1`.

[ ![An example of VMs and Kubernetes with Cloud Service Mesh.](https://docs.cloud.google.com/static/service-mesh/docs/images/vms-kubernetes.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/vms-kubernetes.svg) An example of VMs and Kubernetes with Cloud Service Mesh (click to enlarge)

Google provides a seamless mechanism to set up VM-based workloads with Cloud Service Mesh. You only add a flag to your Compute Engine VM instance template, and Google handles the infrastructure setup. This setup includes installing and configuring the proxies that deliver application networking capabilities.

### Proxyless gRPC

[gRPC](https://grpc.io/) is a feature-rich open source RPC framework that you can use to write high-performance microservices. With Cloud Service Mesh, you can bring application networking capabilities (such as service discovery, load balancing, and traffic management) to your gRPC applications. For more information, see [Cloud Service Mesh and gRPC—proxyless services for your service mesh](https://cloud.google.com/blog/products/networking/traffic-director-supports-proxyless-grpc).

In the following diagram, gRPC applications route traffic to services based in Kubernetes clusters in one region and to services running on VMs in different regions. Two of the services include sidecar proxies, and the others are proxyless.

[ ![An example of proxyless gRPC applications with Cloud Service Mesh.](https://docs.cloud.google.com/static/service-mesh/docs/images/proxyless-grpc.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/proxyless-grpc.svg) An example of proxyless gRPC applications with Cloud Service Mesh (click to enlarge)

Cloud Service Mesh supports proxyless gRPC services. These services use a recent version of the open source gRPC library that supports the xDS APIs. Your gRPC applications can connect to Cloud Service Mesh by using the same xDS APIs that Envoy uses.

After your applications are connected, the gRPC library takes care of application networking functions such as service discovery, load balancing, and traffic management. These functions happen natively in gRPC, so service proxies are not required—that's why they're called _proxyless_ gRPC applications.

### Ingress and gateways

For many use cases, you need to [handle traffic that originates from clients that aren't configured by [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/ingress-traffic). For example, you might need to ingress public internet traffic to your microservices. You might also want to configure a load balancer as a reverse proxy that handles traffic from a client before sending it on to a destination.

In the following diagram, an external Application Load Balancer enables ingress for external clients, with traffic routed to services in a Kubernetes cluster. An internal Application Load Balancer routes internal traffic to the service running on the VM.

[ ![Cloud Service Mesh with Cloud Load Balancing for ingress.](https://docs.cloud.google.com/static/service-mesh/docs/images/overview-ingress.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/overview-ingress.svg) Cloud Service Mesh with Cloud Load Balancing for ingress (click to enlarge)

Cloud Service Mesh works with Cloud Load Balancing to provide a managed ingress experience. You set up an external or internal load balancer, and then configure that load balancer to send traffic to your microservices. In the preceding diagram, public internet clients reach your services through the [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https). Clients, such as microservices that reside on your Virtual Private Cloud (VPC) network, use an [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) to reach your services.

For some use cases, you might want to set up Cloud Service Mesh to configure a _gateway_. A gateway is essentially a reverse proxy, typically Envoy running on one or more VMs, that listens for inbound requests, handles them, and sends them to a destination. The destination can be in any Google Cloud region or Google Kubernetes Engine (GKE) cluster. It can even be a destination outside of Google Cloud that is reachable from Google Cloud by using [hybrid connectivity](https://cloud.google.com/hybrid-connectivity). For more information on when to use a gateway, see [Ingress traffic for your mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/ingress-traffic).

In the following diagram, a VM in the `europe-west1` region runs a proxy that acts as a gateway to three services that are not running proxies. Traffic from both an external Application Load Balancer and an internal Application Load Balancer is routed to the gateway and then to the three services.

[ ![Cloud Service Mesh used to configure a gateway.](https://docs.cloud.google.com/static/service-mesh/docs/images/overview-gateway.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/overview-gateway.svg) Cloud Service Mesh used to configure a gateway (click to enlarge)

### Multiple environments

Whether you have services in Google Cloud, on-premises, in other clouds, or all of these, your fundamental application networking challenges remain the same. How do you get traffic to these services? How do these services communicate with each other?

In the following diagram, Cloud Service Mesh routes traffic from services running in Google Cloud to `Service G`, running in another public cloud, and to `Service E` and `Service F`, both running in an on-premises data center. `Service A`, `Service B`, and `Service C` use Envoy as a sidecar proxy, while `Service D` is a proxyless gRPC service.

[ ![Cloud Service Mesh used for communication across environments.](https://docs.cloud.google.com/static/service-mesh/docs/images/overview-multi-environment.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/overview-multi-environment.svg) Cloud Service Mesh used for communication across environments (click to enlarge)

When you use Cloud Service Mesh, you can send requests to destinations outside of Google Cloud. This enables you to use Cloud Interconnect or Cloud VPN to privately route traffic from services inside Google Cloud to services or gateways in other environments.

## Setting up Cloud Service Mesh

Setting up Cloud Service Mesh consists of two steps. After you complete the setup process, your infrastructure handles application networking, and Cloud Service Mesh keeps everything up to date based on changes to your deployment.

### Deploy your applications

First, you deploy your application code to containers or VMs. Google provides mechanisms that let you add application networking infrastructure (typically Envoy proxies) to your VM instances and Pods. This infrastructure is set up to talk to Cloud Service Mesh and learn about your services.

### Configure Cloud Service Mesh

Next, you configure your global services and define how traffic should be handled. To configure Cloud Service Mesh, you can use the Google Cloud console (for some features and configurations), the Google Cloud CLI, the Traffic Director API, or other tooling, such as Terraform.

After you complete these steps, Cloud Service Mesh is ready to configure your application networking infrastructure.

### Infrastructure handles application networking

When an application sends a request to `my-service`, your application networking infrastructure (for example, an Envoy sidecar proxy) handles the request according to information received from Cloud Service Mesh. This enables a request for `my-service` to be seamlessly routed to an application instance that is able to receive the request.

### Monitoring and continuous updates

Cloud Service Mesh monitors the application instances that constitute your services. This monitoring enables Cloud Service Mesh to discover that a service is healthy or that a service's capacity has changed—for example, when a new Kubernetes Pod is created. Based on this information, Cloud Service Mesh continuously updates your application networking infrastructure.

## Features

Cloud Service Mesh's [features](https://docs.cloud.google.com/service-mesh/docs/service-routing/features) deliver application networking capabilities to your microservices. Some highlights are discussed in this section.

### Fully managed control plane, health checking, and load balancing

You want to spend your time delivering business value, not managing infrastructure. Cloud Service Mesh is a fully managed solution, so you don't have to install, configure, or update infrastructure. You benefit from the same infrastructure that Google uses for health checking and global load balancing.

### Built on open source products

Cloud Service Mesh uses the same control plane ([xDS APIs](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol)) that popular open source projects such as [Envoy](http://envoyproxy.io) and [Istio](http://istio.io) use. To view supported API versions, see the [xDS control plane APIs](https://docs.cloud.google.com/service-mesh/docs/service-routing/xds-control-plane-apis).

The infrastructure that delivers application networking capabilities—either Envoy or [gRPC](https://grpc.io/) depending on your use case—is also open source, so you don't need to worry about being locked in to proprietary infrastructure.

### Scale

From one-off application networking solutions to massive service mesh deployments with thousands of services, Cloud Service Mesh is built to meet your scaling requirements.

### Service discovery and tracking your endpoints and backends

When your application sends a request to `my-service`, your infrastructure seamlessly handles the request and sends it to the correct destination. Your application doesn't need to know anything about [IP addresses, protocols, or other networking complexities](https://docs.cloud.google.com/service-mesh/docs/service-routing/features#services_management).

### Global load balancing and failover

Cloud Service Mesh uses Google's [global load balancing](https://docs.cloud.google.com/service-mesh/docs/service-routing/features#load_balancing) and health checking to optimally balance traffic based on client and backend location, backend proximity, health, and capacity. You improve your service availability by having traffic automatically [fail over](https://docs.cloud.google.com/service-mesh/docs/service-routing/features#failover) to healthy backends with capacity. You can [customize load balancing](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-load-balancing-overview) to distribute traffic to properly support your business needs.

### Traffic management

Advanced traffic management, including routing and request manipulation (based on hostname, path, headers, cookies, and more), lets you determine how traffic flows between your services. You can also apply actions like retries, redirects, and weight-based traffic splitting for canary deployments. Advanced patterns like fault injection, traffic mirroring, and outlier detection enable DevOps use cases that improve your resiliency.

### Observability

Your application networking infrastructure collects telemetry information, such as metrics, logs, and traces, that can be aggregated centrally in [Google Cloud Observability](https://cloud.google.com/products/operations). After this information is collected, you can gain insights and create alerts so that if anything goes wrong, you get notified.

### VPC Service Controls

You can use VPC Service Controls to provide additional security for your application's resources and services. You can add projects to service perimeters that protect resources and services (like Cloud Service Mesh) from requests that originate outside the perimeter. To learn more about VPC Service Controls, see the [VPC Service Controls overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

To learn more about using Cloud Service Mesh with VPC Service Controls, see the [Supported products](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) page.

## What's next

This is a legacy document that applies primarily to the load balancing APIs. We strongly recommend that you don't configure Cloud Service Mesh using the load balancing APIs.

  * To deploy Cloud Service Mesh:

    * For Compute Engine with VMs, use the [service routing APIs](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview).
    * For Google Kubernetes Engine with Pods, use the [Gateway APIs](https://docs.cloud.google.com/service-mesh/legacy/gateway/gke-gateway-overview).
  * To find uses cases and architecture patterns for proxyless gRPC services, see the [Proxyless gRPC services overview](https://docs.cloud.google.com/service-mesh/docs/service-routing/proxyless-overview).

  * To learn how traffic management gives you control over how traffic is handled, see the [Advanced traffic management overview](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management).

  * To learn how Cloud Service Mesh supports environments that extend beyond Google Cloud, see the following documents:

    * [Cloud Service Mesh integration with Service Directory](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/service-directory-integration)
    * [Cloud Service Mesh with hybrid connectivity network endpoint groups](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/multi-environment-overview) (legacy APIs only)
    * [Cloud Service Mesh with internet network endpoint groups](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/internet-negs) (legacy APIs only) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
