---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api/
title: About Gateway API \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:19.526391+00:00
---

# About Gateway API  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About Gateway API Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the Google Kubernetes Engine (GKE) implementation of the [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) using the GKE Gateway controller.

This page is for Cloud architects and Networking specialists who design and architect their organization's network. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Gateway API is an open source standard for service networking. Gateway API evolves the Ingress resource and improves upon it in the following ways:

  * **Role-oriented:** Gateway API is composed of API resources that correspond to the organizational roles of cluster operator, developer, and infrastructure provider. This lets cluster operators define how shared infrastructure can be used by many different and non-coordinating developer teams.

  * **Portable:** Gateway API is an open source standard with many implementations, enabling the concepts and core resources to be consistent across implementations and environments, reducing complexity, and increasing user familiarity. Its design uses the flexible conformance concept, using a highly portable core API (like Ingress) that still has the flexibility and extensibility to support native capabilities of the environment and implementation.

  * **Expressive:** Gateway API resources provide built-in capabilities for header-based matching, traffic weighting, CORS, and other capabilities that are only possible in Ingress through custom annotations.




## Gateway API resources

Gateway API is a role-oriented resource model, designed for Cloud architects and Networking specialists who interact with Kubernetes networking. As shown by the following diagram, this model enables different non-coordinating service owners to share the same underlying network infrastructure safely in a way that centralizes policy and control for the platform administrator.

![GKE provides Gateway classes. Cluster operators
        create Gateway resources based on these classes. Application developers
        create HTTPRoute resources that bind to Gateway resources.](https://docs.cloud.google.com/static/kubernetes-engine/images/gateway-architecture.png)**Figure:** Gateway API overview

Gateway API contains the following resource types:

  * **GatewayClass** : Defines a cluster-scoped resource that's a template for creating load balancers in a cluster. GKE provides GatewayClasses that can be used in GKE clusters.
  * **Gateway** : Defines where and how the load balancers listen for traffic. Cluster operators create Gateways in their clusters based on a GatewayClass. GKE creates load balancers that implement the configuration defined in the Gateway resource.
  * **HTTPRoute** : Defines protocol-specific rules for routing requests from a Gateway to Kubernetes services. GKE supports HTTPRoutes for HTTP(S)-based traffic routing. Application developers create HTTPRoutes to expose their HTTP applications using Gateways.
  * **Policy** : Defines a set of implementation-specific characteristics of a Gateway resource. You can attach a policy to a Gateway, a Route, or a Kubernetes Service.
  * **ReferenceGrant** : Enables cross-namespace references within Gateway API. To refer to an object outside its namespace, you must create a ReferenceGrant resource.



### GatewayClass

A GatewayClass is a resource that defines a template for HTTP(S) (Layer 7) load balancers in a Kubernetes cluster. GKE provides GatewayClasses as cluster-scoped resources. Cluster operators specify a GatewayClass when creating Gateways in their clusters.

The different GatewayClasses correspond to different [Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). When you create a Gateway based on a GatewayClass, a corresponding load balancer is created to implement the specified configuration.

Some GatewayClasses support multi-cluster load balancing.

The following table lists the GatewayClasses available in GKE clusters and their underlying load balancer type. For complete details on the GatewayClasses, see the [GatewayClass capabilities and specifications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

GatewayClass name | Description  
---|---  
`gke-l7-global-external-managed` | Global external Application Load Balancer(s) built on the [global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)  
`gke-l7-regional-external-managed` | Regional external Application Load Balancer(s) built on the [regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb)  
`gke-l7-rilb` | Internal Application Load Balancer(s) built on the [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)  
`gke-l7-gxlb` | Global external Application Load Balancer(s) built on the [classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)  
`gke-l7-cross-regional-internal-managed-mc` | Multi-cluster Cross-region internal Application Load Balancer(s) built on the [cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal)  
`gke-l7-global-external-managed-mc` | Multi-cluster Global external Application Load Balancer(s) built on the [global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)  
`gke-l7-regional-external-managed-mc` | Multi-cluster Regional external Application Load Balancer(s) built on the [regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb)  
`gke-l7-rilb-mc` | Multi-cluster Internal Application Load Balancer(s) built on the [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)  
`gke-l7-gxlb-mc` | Multi-cluster Global external Application Load Balancer(s) built on the [classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)  
`gke-td` | Multi-cluster [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/gateway/overview)  
`asm-l7-gxlb` | Global external Application Load Balancer(s) built on [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview)  
  
Each GatewayClass is subject to the limitations of the underlying load balancer.

**Note:** When considering the deployment of a Global external Application Load Balancer, we do recommend to use the `gke-l7-global-external-managed(-mc)` GatewayClasses over the `gke-l7-gxlb(-mc)` GatewayClasses to benefit from the advanced security and [traffic management](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management) capabilities. To learn more about the different features supported with each GatewayClass, see [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

### Gateway

Cluster operators create Gateways to define where and how the load balancers listen for traffic. Gateways take their behavior (that is, how they are implemented) from their associated GatewayClass.

The Gateway specification includes the GatewayClass for the Gateway, which ports and protocols to listen on, and which Routes can bind to the Gateway. A Gateway selects routes based on the Route metadata; specifically the kind, namespace, and labels of Route resources.

For an example of deploying a Gateway, see [Deploying Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).

For an example of deploying a multi-cluster Gateway, see [Deploying multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways).

### HTTPRoute

An HTTPRoute defines how HTTP and HTTPS requests received by a Gateway are directed to Services. Application developers create HTTPRoutes to expose their applications through Gateways.

An HTTPRoute defines which Gateways it can route traffic from, which Services to route to, and rules that define what traffic the HTTPRoute matches. Gateway and Route binding is bidirectional, which means that both resources must select each other for them to bind. HTTPRoutes can match requests based on details in the request header. HTTPRoutes also support filters for header modification, redirect, rewrite, and CORS.

**Note:** When multiple HTTPRoute resources reference the same Gateway, they are all compiled into a single URL map on the underlying Google Cloud infrastructure. As a result, all HTTPRoutes attached to a single Gateway are subject to the same URL map [quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas#url_maps).

### Policy

A Policy defines characteristics of a Gateway resource, typically implementation-specific, that cluster operators can attach to a Gateway, a Route, or a Kubernetes Service. A Policy defines how the underlying Google Cloud infrastructure should function.

A Policy is typically attached to a namespace and can reference a resource in the same namespace and access is granted using RBAC. The hierarchical nature of the Gateway API lets you attach a Policy to a top resource (Gateway) in a namespace, and have all the resources underneath in different namespaces receive the characteristics of that policy.

The GKE Gateway controller supports the following Policies:

  * **HealthCheckPolicy** : defines the parameters and behavior of the health check used to check the health status of the backend Pods.
  * **GCPGatewayPolicy** : defines specific parameters of the frontend of the Google Cloud load balancer. This policy is similar to a FrontendConfig for an Ingress resource.
  * **GCPBackendPolicy** : defines how the backend services of the load balancer distribute traffic to the endpoints (backends). This policy is similar to a BackendConfig for an Ingress resource and supports features like the `CUSTOM_METRICS` balancing mode, which enables routing decisions based on user-defined application metrics reported through ORCA load reports.
  * **GCPTrafficDistributionPolicy** : defines how traffic is distributed across endpoints within a backend. This policy is similar to how you would configure specific traffic balancing algorithms for the backend service that are referenced by an Ingress resource.
  * **GCPAuthzPolicy** : defines identity-based access control policies that enforce zero-trust authorization directly at the GKE Gateway layer for all incoming (north-south) traffic. This policy lets administrators set granular access rules based on client identities, such as restricting access to specific paths or headers.

**Note:** Google Cloud has replaced the LbPolicy policy with the GCPBackendPolicy policy. The LbPolicy is still supported, but without additional attributes.

### ReferenceGrant

ReferenceGrant enables resources like HTTPRoute or Gateway to reference backend services or secrets located in different namespaces through cross-namespace referencing. ReferenceGrant acts as a permission provider, specifying which resources (`from`) are allowed to reference other resources (`to`). To enable cross-namespace references, you need a ReferenceGrant in the namespace of the resource being referenced.

In the following example, the HTTPRoute in the `frontend` namespace needs to route traffic to a Service in the `backend` namespace. You create a ReferenceGrant in the `backend` namespace where:

  * The `from` field lists the source namespace and resource type allowed to make references, that is, HTTPRoute in the `frontend` namespace.
  * The `to` field specifies the target resource type that can be referenced, that is, Services in the `backend` namespace.


    
    
    apiVersion: gateway.networking.k8s.io/v1beta1
    kind: ReferenceGrant
    metadata:
      name: allow-frontend-to-access-backend
      namespace: backend
    spec:
      from:
      - group: gateway.networking.k8s.io
        kind: HTTPRoute
        namespace: frontend
      to:
      - group: ""
        kind: Service
    

If you receive error message "No valid reference grant found" in your gateway status, verify that the `group`, `kind`, `namespace` and `name` values defined in the `from` and `to` sections are valid.

## Gateway ownership and usage patterns

Gateway and Route resources provide flexibility in how they are owned and deployed within an organization. This means that a single load balancer can be deployed and managed by an infrastructure team, but routing under a particular domain or path can be delegated to another team in another Kubernetes Namespace. The GKE Gateway controller supports multi-tenant usage of a load balancer, shared across Namespaces, clusters, and regions. Gateways also don't have to be shared if more distributed ownership is required. The following are some of the most common usage patterns for Gateways in GKE.

### Self-managed Gateway

A single owner can deploy a Gateway and Route just for their applications and use them exclusively. Gateways and Routes deployed in this manner are similar to Ingress. The following diagram shows two different service owners who deploy and manage their own Gateways. Similar to Ingress, each Gateway corresponds to its own unique IP address and load balancer. TLS, routing, and other policies are fully controlled by the service owner.

![A single owner can have full control of both the Gateway and the Route](https://docs.cloud.google.com/static/kubernetes-engine/images/model-single-owner.svg)

This usage pattern is common for Ingress but is challenging to scale across many teams because of the lack of shared resources. The Gateway API resource model enables the following usage patterns which provide a spectrum of options for distributed control and ownership.

### Platform-managed Gateway per Namespace

Separation between Gateway and Route resources lets platform administrators control Gateways on behalf of service owners. Platform admins can deploy a Gateway per Namespace or team, giving that Namespace exclusive access to use the Gateway. This gives the service owner full control over the routing rules without any risk of conflict from other teams. This lets the platform administrator control aspects such as IP allocation, port exposure, protocols, domains, and TLS. Platform admins can also decide which kinds of Gateways are available to teams, such as internal or external Gateways. This usage pattern creates a clean separation of responsibilities between different roles.

[Cross-Namespace routing](https://gateway-api.sigs.k8s.io/guides/multiple-ns/) is what lets Routes to attach to Gateways across Namespace boundaries. Gateways can restrict from which Namespaces Routes can attach. Similarly, Routes specify the Gateways that they attach to, but they can only attach to a Gateway that has permitted the Route's Namespace. This [bi-directional attachment](https://gateway-api.sigs.k8s.io/concepts/api-overview/#attaching-routes-to-gateways) provides each side with flexible controls that enable this diversity of usage patterns.

In the following diagram, the platform administrator has deployed a Gateway for exclusive access for each Namespace. For example, the `store` Gateway is configured so that only Routes from the `store` Namespace can attach to it. Each Gateway represents a unique, load balanced IP address and so it lets each team deploy any number of Routes against the Gateway for any domains or routes it chooses.

![A Gateway per Namespace provides exclusive access of a Gateway to that Namespace.](https://docs.cloud.google.com/static/kubernetes-engine/images/model-gateway-per-namespace.svg)

### Shared Gateway per cluster

Sharing Gateways across Namespaces offers an even more centralized form of ownership to platform administrators. This lets different service owners, running in different Namespaces, share the same IP address, DNS domain, certificates, or paths for fine grained routing between services. Gateways provide control to platform administrators over which Namespaces can route for a specific domain. This is similar to the previous example except Gateways permit Route attachment from multiple Namespaces.

In the following diagram, the platform administrator has deployed two Gateways into the `infra` Namespace. The `external` Gateway permits Routes from the `web` and `mobile` Namespaces to attach to the Gateway. Routes from the `accounts` Namespace cannot use the `external` Gateway because the `accounts` Namespace is only for internal services. The `internal` Gateway lets internal clients communicate privately within the VPC using private IP addresses.

![A Gateway per cluster allows different Namespaces inside a cluster to share a single Gateway](https://docs.cloud.google.com/static/kubernetes-engine/images/model-gateway-per-cluster.svg)

The `m.example.com` domain is delegated to the `mobile` Namespace which lets mobile service owners configure any routing rules they need under the `m.example.com` domain. This gives the service owners a greater degree of control for introducing new API endpoints and controlling traffic without requesting a change from administrators.

### Shared Gateway per Fleet

Using [multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways), a Gateway can be shared across both Namespaces, clusters, and regions. Large organizations with geographically distributed apps might benefit from multi-cluster Gateways because they can granularly control global traffic while also delegating routing ownership. Similar to the previous examples, a platform administrator manages the Gateway and delegates routing. The major addition to this use case is that Routes reference multi-cluster Services, which are deployed across clusters. Traffic can be routed in an explicit manner, traffic to `store.example.com/us` goes to `gke-us` Pods, or in an implicit manner, traffic to `example.com/*` gets routed to the closest cluster to the client. This flexibility lets service owners define the optimal routing strategy for their application.

![A Gateway per fleet provides multi-cluster, multi-regional load balancing](https://docs.cloud.google.com/static/kubernetes-engine/images/model-gateway-per-fleet.svg)

## GKE Gateway controller

The GKE Gateway controller is Google's implementation of the Gateway API for Cloud Load Balancing. Similar to the GKE Ingress controller, the Gateway controller watches a Kubernetes API for Gateway API resources and reconciles Cloud Load Balancing resources to implement the networking behavior specified by the Gateway resources.

There are two versions of the GKE Gateway controller:

  * **Single-cluster** : manages single-cluster Gateways for a single GKE cluster.
  * **Multi-cluster:** manages multi-cluster Gateways for one or more GKE clusters.



Both Gateway controllers are Google-hosted controllers that watch the Kubernetes API for GKE clusters. Unlike the GKE Ingress controller, the Gateway controllers are not hosted on GKE control planes or in the user project, enabling them to be more scalable and robust. Both Gateway controllers are Generally Available (GA).

_The Gateway controllers themselves are not a networking data plane and they do not process any traffic._ They sit out of band from traffic and manage various data planes that process traffic. The following diagram shows the architecture of the single-cluster and multi-cluster GKE Gateway controllers. The underlying controller that is used depends on the GatewayClass of the deployed Gateway.

![The multi-cluster and single-cluster Gateway controllers deploy and manage load
balancers for GKE, but don't process network traffic themselves.](https://docs.cloud.google.com/static/kubernetes-engine/images/gateway-controller-architecture.svg)

Controller | Single-cluster Gateway controller | Multi-cluster Gateway controller  
---|---|---  
Managed by | Google Cloud | Google Cloud  
Cluster scope | Single cluster Gateways | Multi-cluster Gateways  
Deployment location | Deployed regionally in the same region as its GKE cluster. | Deployed globally across multiple Google Cloud regions.  
How to enable | Enabled by default in GKE. | Enabled through the Multi Cluster Ingress API and registration into a fleet. See [Enabling multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enabling-multi-cluster-gateways).  
Supported GatewayClasses | 

  * gke-l7-global-external-managed [GA](https://cloud.google.com/products#product-launch-stages)
  * gke-l7-regional-external-managed [GA](https://cloud.google.com/products#product-launch-stages)
  * gke-l7-rilb [GA](https://cloud.google.com/products#product-launch-stages)
  * gke-l7-gxlb [GA](https://cloud.google.com/products#product-launch-stages)
  * asm-l7-gxlb [Preview](https://cloud.google.com/products#product-launch-stages)

| 

  * gke-l7-global-external-managed-mc [GA](https://cloud.google.com/products#product-launch-stages)
  * gke-l7-regional-external-managed-mc [GA](https://cloud.google.com/products#product-launch-stages)
  * gke-l7-cross-regional-internal-managed-mc [GA](https://cloud.google.com/products#product-launch-stages)
  * gke-l7-rilb-mc [GA](https://cloud.google.com/products#product-launch-stages)
  * gke-l7-gxlb-mc [GA](https://cloud.google.com/products#product-launch-stages)
  * gke-td [Preview](https://cloud.google.com/products#product-launch-stages)

  
  
You can use multiple Gateway controllers, including controllers not provided by Google, in a GKE cluster simultaneously. Every GatewayClass is supported by one and only one Gateway controller, which enables single and multi-cluster load balancing to be used simultaneously.

### Service Extensions

The GKE Gateway controller supports Service Extensions, which let you add custom logic into Cloud Load Balancing.

**Note:** Support for Service Extensions is in the ([Preview](https://cloud.google.com/products#product-launch-stages)) stage.

The GKE Gateway controller supports the following types of extensions:

  * **GCPTrafficExtension** : this extension provides a way to add custom logic into Cloud Load Balancing. The extension service can modify the headers and payloads of both requests and responses without impacting the choice of backend services, or any other security policies that are associated with the backend service.
  * **GCPRoutingExtension** : this extension provides a way to add custom logic into Cloud Load Balancing to control where traffic is routed to for a given request.
  * **GCPAuthzExtension** : this extension provides a way to delegate authorization decisions to custom or third-party authorization engines with service callouts. This extension enables real-time inspection and authorization of traffic in transit, which supports integrations such as Identity-Aware Proxy.



For more information about how to configure GKE Gateway controllers, see [Customize GKE Gateway traffic using Service Extensions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions).

## Ingress and Gateway

Ingress and Gateway are both open source standards for routing traffic, but they have key differences.

### Comparison of Ingress and Gateway

Gateway and Ingress are both open source standards for routing traffic and can be used simultaneously without conflict. Over time, we recommend transitioning to using Gateway and Route resources due to their increased capabilities. Gateway was designed by the Kubernetes community, drawing on lessons learned from the Ingress and the service mesh ecosystems. Gateway is an evolution of Ingress that serves the same function, delivered as a superset of the Ingress capabilities.

In GKE all Ingress resources are directly convertible to Gateway and HTTPRoute resources. A single Ingress corresponds to both a Gateway (for frontend configuration) and an HTTPRoute (for routing configuration). The following example shows what the corresponding Gateway and HTTPRoute configuration looks like. Note that the Gateway and HTTPRoute resources can be created separately, also by different users. Gateways can have many Routes and a Route can also attach to more than one Gateway. The relationships between Gateways and Routes is discussed in Gateway usage patterns.

### Ingress
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: my-ingress
      annotations:
        kubernetes.io/ingress.class: "gce-internal"
    spec:
      rules:
      - host: "example.com"
        http:
          paths:
          - pathType: Prefix
            path: /
            backend:
              service:
                name: site
                port:
                  number: 80
          - pathType: Prefix
            path: /shop
            backend:
              service:
                name: store
                port:
                  number: 80
    

### Gateway
    
    
    apiVersion: gateway.networking.k8s.io/v1
    kind: Gateway
    metadata:
      name: my-gateway
    spec:
      gatewayClassName: gke-l7-rilb
      listeners:
      - name: http
        protocol: HTTP
        port: 80
        allowedRoutes:
          kinds:
          - kind: HTTPRoute
    

### Route
    
    
    apiVersion: gateway.networking.k8s.io/v1
    kind: HTTPRoute
    metadata:
      name: my-route
    spec:
      parentRefs:
      - name: my-gateway
      hostnames:
      - "example.com"
      rules:
      - matches:
        - path:
            value: /
        backendRefs:
        - name: site
          port: 80
      - matches:
        - path:
            value: /shop
        backendRefs:
        - name: store
          port: 80
    

## Integrating Gateway API with Service Meshes

You can configure a Cloud Service Mesh using Gateway API. This enables service-to-service communications, traffic management, global load balancing, and security policy enforcement for service mesh use cases. For complete information about using Cloud Service Mesh with Gateway API, including deployment setup guides, see [Cloud Service Mesh Overview](https://docs.cloud.google.com/service-mesh/docs/gateway/overview).

## Pricing

All Compute Engine resources deployed through the Gateway controllers are charged against the project in which your GKE clusters reside. The single-cluster Gateway controller is offered at no additional charge as a part of GKE Standard and Autopilot pricing. Pricing for multi-cluster Gateways is described in the [Multi Cluster Gateway and Multi Cluster Ingress pricing page](https://cloud.google.com/kubernetes-engine/pricing#multi-cluster-gateway-and-multi-cluster-ingress).

## What's next

  * Learn how to [Configure Gateway resources using Policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources)
  * Learn about [Deploying Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).
  * Learn about [Deploying multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways).
  * For complete information about using Cloud Service Mesh with Gateway API, see [Cloud Service Mesh Overview](https://docs.cloud.google.com/service-mesh/docs/gateway/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
