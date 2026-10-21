---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/traffic-management/service-discovery/
title: Service discovery \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:14.357321+00:00
---

# Service discovery  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/traffic-management/service-discovery/

You are viewing archived v1.26 Service Mesh documentation.

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
  * [ v1.26 ](https://docs.cloud.google.com/service-mesh/v1.26/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Service discovery

Cloud Service Mesh provides service and endpoint discovery. These features let you group the virtual machine (VM) instances and container instances that run your code as _endpoints_ of your services.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview).

Cloud Service Mesh monitors these services so that it can share up-to-date [health check](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) information with its clients. Therefore, when one of your applications uses its Cloud Service Mesh client (such as an Envoy sidecar proxy or a proxyless gRPC application) to send a request, it benefits from up-to-date information about your services.

In the context of Cloud Service Mesh, a _client_ is application code that runs on a VM or container that formulates requests to send to a server. A _server_ is application code that receives such requests. A _Cloud Service Mesh client_ is an Envoy or gRPC or other xDS client that is connected to Cloud Service Mesh and is part of the data plane.

In the data plane, Envoy or gRPC does the following:

  1. It examines a request and matches the request to a _backend service_ , a resource that you configure during deployment.
  2. After the request is matched, Envoy or gRPC applies any previously configured traffic or security policies, chooses a backend or endpoint, and directs the request to that backend or endpoint.



## Service discovery

Cloud Service Mesh provides service discovery. When you configure Cloud Service Mesh, you create backend services. You also define routing rules that specify how an _outbound request_ (a request sent by your application code and handled by a Cloud Service Mesh client) is matched to a particular service. When a Cloud Service Mesh client handles a request that matches a rule, it can choose the service that should receive the request.

For example:

  * You have a VM running your application. This VM has an Envoy sidecar proxy that is connected to Cloud Service Mesh and handles outbound requests on behalf of the application.
  * You configured a backend service named `payments`. This backend service has two network endpoint group (NEG) backends that point to various container instances that run the code for your `payments` service.
  * You configured a `Mesh` resource defining a mesh called `sidecar-mesh`.
  * You configured a `Route` resource that defines traffic destinations for the backend service `payments` and the hostname `helloworld-gce`.



With this configuration, when your application (on the VM) sends an HTTP request to `payments.example.com`, the Cloud Service Mesh client knows that this request is destined for the `payments` service.

When you use Cloud Service Mesh with proxyless gRPC services, service discovery works similarly. However, a gRPC library acting as a Cloud Service Mesh client only gets information about the services for which you specify an xDS resolver. By default, Envoy gets information about all services configured on the Virtual Private Cloud (VPC) network specified in the Envoy bootstrap file.

## Endpoint discovery

Service discovery enables clients to know about your services. Endpoint discovery enables clients to know about the instances that are running your code.

When you create a service, you also specify the backends for that service. These backends are either VMs in managed instance groups (MIGs) or containers in NEGs. Cloud Service Mesh monitors these MIGs and NEGs so that it knows when instances and endpoints are created and removed.

Cloud Service Mesh continuously shares up-to-date information about these services with its clients. This information enables clients to avoid sending traffic to endpoints that no longer exist. It also enables clients to learn about new endpoints and take advantage of the additional capacity that these endpoints provide.

Beyond adding endpoints into MIGs or NEGs and setting up Cloud Service Mesh, you don't need any additional configuration to enable service discovery with Cloud Service Mesh.

## Sidecar proxy traffic interception in Cloud Service Mesh

Cloud Service Mesh supports the sidecar proxy model. Under this model, when an application sends traffic to its destination, the traffic is intercepted and redirected it to a port on the sidecar proxy on the host where the application is running. The sidecar proxy decides how to load balance the traffic, and then sends the traffic to its destination.

With Cloud Service Mesh and the service routing APIs, traffic interception is managed automatically.

## What's next

  * To learn how Cloud Service Mesh delivers global load balancing for your internal microservices with sidecar proxies, see [Cloud Service Mesh load balancing](https://docs.cloud.google.com/service-mesh/v1.26/docs/service-routing/load-balancing).
  * To learn more about Cloud Service Mesh, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
