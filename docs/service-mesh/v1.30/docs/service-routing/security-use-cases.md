---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/security-use-cases/
title: Service security use cases \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:27:16.899107+00:00
---

# Service security use cases  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/security-use-cases/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Service security use cases 

This document describes common Cloud Service Mesh security use cases. Use this information to help you determine which security model best suits your needs. This document also provides a high-level overview of what you need to configure for each use case.

For an overview of service security, see [Cloud Service Mesh service security](https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/security-overview).

## Enabling mutual TLS for services in the mesh

In a service mesh, you can enable mutual TLS (mTLS) so that both the client and the server in a communication must prove their identities and encrypt communications.

[ ![Mutual TLS \(mTLS\) authentication in a service mesh.](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/security-httproute-tls.svg)](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/security-httproute-tls.svg) Mutual TLS (mTLS) authentication in a service mesh (click to enlarge)

The following section omits discussion of the `Mesh`, `Gateway` and `Route` resources. These API resources are required to create your mesh and route traffic, but you don't need to update them to enable mTLS.

The preceding pattern can be achieved by configuring the following Compute Engine API resources. This diagram uses sidecar proxies, but configuring a proxyless gRPC application with mTLS uses the same resources.

[ ![Compute Engine API resources for mTLS within a mesh.](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/td-security-mtls.svg)](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/td-security-mtls.svg) Compute Engine API resources for mTLS within a mesh (click to enlarge)

To create this model, do the following:

  1. Create a client transport layer security (TLS) policy.
  2. Create a server TLS policy.
  3. Update the `securitySettings` field in your existing global backend services to reference the new client TLS policy.
  4. Create an endpoint policy:

     1. Reference the server TLS policy in the `server_tls_policy` field.
     2. Define an `EndpointMatcher` to select the Cloud Service Mesh clients that should enforce authentication on inbound traffic.

Selecting Cloud Service Mesh clients is based on labels specified in the Cloud Service Mesh client's bootstrap configuration. These labels can be supplied manually or populated automatically based on labels supplied to your Google Kubernetes Engine (GKE) deployments.

In the preceding diagram, the labels `"mesh-service":"true"` are configured on the endpoint policy and the Cloud Service Mesh clients. You can choose labels that suit your deployment.

     3. Optionally, define a `TrafficPortSelector` that applies the policies only when inbound requests are made to the specified port on the data plane entity.




The following diagram shows the Compute Engine resources that you configure for mTLS, regardless of whether you use Envoy or a proxyless gRPC application.

[ ![Compute Engine API resources for mTLS within a mesh.](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/td-security-mtls-resources.svg)](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/td-security-mtls-resources.svg) Compute Engine API resources for mTLS within a mesh (click to enlarge)

The following diagram shows traffic flow and lists the Compute Engine API resources that you configure to enable mTLS. The local sidecar proxy that sits alongside Service B's GKE Pod is the endpoint in the communication.

[ ![Compute Engine API resources and traffic flow for mTLS within a mesh.](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/td-security-mtls-traffic-flow.svg)](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/td-security-mtls-traffic-flow.svg) Compute Engine API resources and traffic flow for mTLS within a mesh (click to enlarge)

The endpoint policy does the following:

  1. Selects a set of endpoints by using an endpoint matcher and, optionally, ports on those endpoints.

     1. The endpoint matcher lets you specify rules that determine whether a Cloud Service Mesh client receives the configuration. These rules are based on the xDS metadata that the data plane entity provides to the control plane—in this case, Cloud Service Mesh.

You can add labels to the Cloud Service Mesh client as follows:

        * You can manually specify this metadata in your Cloud Service Mesh client's bootstrap file.
        * Alternatively, the metadata can be automatically populated when you use GKE by adding the key-value pairs to the `env` section of the `demo_server.yaml` or `demo_client.yaml` files. These values are provided in the [Envoy setup guide](https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/security-envoy-setup) and [proxyless gRPC setup guide](https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/security-proxyless-setup).

For example, with Envoy only, you can prefix the key with the `ISTIO_META_` prefix. Proxy environment variable names that start with `ISTIO_META_` are included in the generated bootstrap and sent to the xDS server.
              
              - name: ISTIO_META_app
                value: 'review'
              - name: ISTIO_META_version
                value: 'canary'
              

     2. If you specify a port, the policies referenced in the endpoint policy are only enforced on inbound requests that specify the same port. If you don't specify a port, the policies are enforced on inbound requests that specify a port that is also in the `TRAFFICDIRECTOR_INBOUND_BACKEND_PORTS` field, which is provided to the Cloud Service Mesh client in its bootstrap information.

  2. References client TLS, server TLS, and authorization policies that configure the endpoints to which requests resolve.




Configuring incompatible TLS modes might result in a disruption of communications. For example, setting `OPEN` on the global backend service or leaving the client TLS policy field empty, and setting `MTLS` as the value of the server TLS policy on the endpoint policy, results in failed communication attempts. This is because endpoints that are configured to only accept mTLS reject attempts to establish unauthenticated communication channels.

Note the distinction between a client TLS policy and a server TLS policy attached to a global backend service and endpoint policy, respectively:

  * The client TLS policy is applied to the global backend service. It tells the Envoy proxy or proxyless client which TLS mode, identity, and peer validation approach to use when addressing the service.
  * The server TLS policy is attached to the endpoint policy. It tells the server which TLS mode, identity, and peer validation approach to use for incoming connections.



## Enabling TLS for an ingress gateway

After you set up mTLS for in-mesh communications, you might want to secure traffic that is entering your mesh, known as _ingress traffic_. Cloud Service Mesh can configure your data plane to require ingress traffic to use TLS-encrypted communications channels.

To achieve this goal, choose one of the following architecture options:

  * Services in the mesh terminate TLS for traffic from a load balancer. In this model, each service in the mesh is configured as a backend in the load balancer's configuration—specifically, in the load balancer's URL map.
  * An ingress gateway terminates TLS for traffic from a load balancer before forwarding traffic to services in the mesh. In this model, a dedicated service in the mesh, the _ingress gateway_ , is configured as a backend in the load balancer's configuration—specifically, in the load balancer's URL map.



Both options are explained in this section.

### Services in the mesh terminate TLS for traffic from a load balancer

If you want to make your services available to clients outside of Google Cloud, you might use an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https). Clients send traffic to the load balancer's global Anycast virtual IP address (VIP), which then forwards that traffic to services in your mesh. This means that there are two connections when an external client needs to reach a service in the mesh.

[ ![TLS to a service in the mesh.](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/td-security-tls-ingress-mesh.svg)](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/td-security-tls-ingress-mesh.svg) TLS to a service in the mesh (click to enlarge)

The same pattern applies when you use an [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal). Traffic from internal clients first reaches the load balancer, which then establishes a connection to the backend.

To secure both connections, do the following:

  1. Secure the connection between the client and the load balancer by using an external Application Load Balancer.
  2. Configure the load balancer to use the HTTPS or HTTP/2 protocols when it attempts to [establish a connection with services in the mesh](https://docs.cloud.google.com/load-balancing/docs/https#how-connections-work).
  3. Configure Cloud Service Mesh so that your Cloud Service Mesh clients terminate HTTPS and present certificates to the client, which, in this case, is the load balancer.



For more information about steps 1 and 2, see [Setting up a multi-region, content-based external HTTPS load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https).

When you set up Cloud Service Mesh security, you configure various Compute Engine API resources. These resources are separate from the resources that you configure for the load balancer. You create a set of Compute Engine API resources (global forwarding rule, target proxy, URL map, and global backend services) for the load balancer and configure Cloud Service Mesh with the service routing APIs. In addition, in the backend service resource, the load balancer has the load balancing scheme `INTERNAL_MANAGED` and Cloud Service Mesh has the load balancing scheme `INTERNAL_SELF_MANAGED`.

In step 3, you configure Cloud Service Mesh so that your Cloud Service Mesh clients terminate HTTPS and present certificates to clients.

[ ![Compute Engine API resources for TLS to service in mesh.](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/td-security-apis-tls.svg)](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/td-security-apis-tls.svg) Compute Engine API resources for TLS to service in mesh (click to enlarge)

In this model, you do the following:

  1. Create a `serverTlsPolicy`: configure `serverCertificate` on the `serverTlsPolicy` resource.
  2. Create an endpoint policy: 
     1. Reference the server TLS policy in the `authentication` field.
     2. Define an `EndpointMatcher` to select the xDS data plane entities that should enforce authentication on inbound traffic.
     3. Optionally, define a `TrafficPortSelector` that applies the policies only when inbound requests are made to the specified port on the Cloud Service Mesh client.



Because the external Application Load Balancer is already configured to initiate TLS connections to services in your mesh, Cloud Service Mesh only needs to configure your Cloud Service Mesh clients to terminate TLS connections.

### Ingress gateway terminates TLS for traffic from a load balancer before forwarding traffic to services in the mesh

If you only want to expose an ingress gateway to your load balancer, you can use the ingress gateway deployment pattern. In this pattern, the load balancer does not directly address services in your mesh. Instead, a middle proxy sits at the edge of your mesh and routes traffic to services inside the mesh, based on the configuration that it receives from Cloud Service Mesh. The middle proxy can be an Envoy proxy that you deployed on virtual machine (VM) instances in a Compute Engine managed instance group.

[ ![TLS to an ingress gateway with mTLS within a mesh.](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/td-security-ingress-mtls.svg)](https://docs.cloud.google.com/static/service-mesh/v1.30/docs/images/td-security-ingress-mtls.svg) TLS to an ingress gateway with mTLS within a mesh (click to enlarge)

From a security perspective, you configure the ingress gateway to terminate TLS, and then optionally configure connections within your mesh so that they are protected by mTLS. These include connections between the ingress gateway and your in-mesh services, and connections among your in-mesh services.

From a configuration perspective, you do the following:

  1. Configure your service mesh and enable mTLS for communications within the mesh (as explained earlier).
  2. Configure your load balancer to route traffic to the ingress gateway and initiate connections by using the HTTPS protocol (as explained earlier).
  3. Create a set of Compute Engine API resources that represent the ingress gateway and its server TLS policy.



For the third step, configure Cloud Service Mesh to terminate HTTPS and present certificates as follows:

  1. Create a `Mesh` resource to represent the mesh.

  2. Create a `Route` resource that points to the correct global backend services and attach the `Route` resource to the `Mesh` resource.

  3. Create a server TLS policy: configure `serverCertificate`.

  4. Create a `Gateway` resource to represent the Cloud Service Mesh managed ingress gateway.

  5. Attach the server TLS policy resource to the `Gateway` resource.




The ingress gateway pattern is especially useful in large organizations that use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc). In such a setting, a team might only allow access to its services through an ingress gateway. In the preceding diagram, when you configure the global forwarding rule for the load balancer, you supply a different IP address (in this example, `10.0.0.2`) than the one supplied when you configure the mesh (in this example, the mesh address is `10.0.0.1`). Clients that communicate through a Cloud Service Mesh-configured xDS data plane entity can use this address to access the ingress gateway.

As an example, assume the following:

  * Two service projects (1 and 2), both attached to the same Shared VPC network.
  * Service project 1 contains a service mesh configured by Cloud Service Mesh.

Service project 1 has configured a mesh and an ingress gateway. This ingress gateway is reachable on the `10.0.0.2` address/VIP.

  * Service project 2 contains a service mesh configured by Cloud Service Mesh.

Service project 2 might or might not have its own ingress gateway.

  * Cloud Service Mesh configures the Cloud Service Mesh clients in each service project. The clients are bootstrapped to use the same network.




Given this configuration, clients in service project 2's mesh can communicate with the ingress gateway in service project 1 by using the `10.0.0.2` VIP. This enables the owners of service project 1 to configure routing, security, and other policies that are specific to traffic entering the mesh. In effect, the owners of service project 1 can tell others that _clients in your mesh can reach my services on`10.0.0.2`_.

## Limitations

Cloud Service Mesh service security is supported only with GKE. You cannot deploy service security with Compute Engine.

## What's next

  * To configure Cloud Service Mesh service security with Envoy proxies, see [Setting up Cloud Service Mesh service security with Envoy](https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/security-envoy-setup).
  * To configure Cloud Service Mesh service security with proxyless gRPC applications, see [Setting up Cloud Service Mesh service security with proxyless gRPC](https://docs.cloud.google.com/service-mesh/v1.30/docs/service-routing/security-proxyless-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
