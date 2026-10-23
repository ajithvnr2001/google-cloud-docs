---
url: https://docs.cloud.google.com/architecture/exposing-service-mesh-apps-through-gke-ingress/
title: From edge to mesh: Expose service mesh applications through GKE Gateway \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:01.808250+00:00
---

# From edge to mesh: Expose service mesh applications through GKE Gateway  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/exposing-service-mesh-apps-through-gke-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  From edge to mesh: Expose service mesh applications through GKE Gateway Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-05-28 UTC

This reference architecture shows how to combine Cloud Service Mesh with Cloud Load Balancing to expose applications in a service mesh to internet clients.

Cloud Service Mesh is a managed service mesh, based on Istio, that provides a security-enhanced, observable, and standardized communication layer for applications. A service mesh provides a holistic communications platform for clients that are communicating in the mesh. However, a challenge remains in how to connect clients that are outside the mesh to applications hosted inside the mesh.

You can expose an application to clients in many ways, depending on where the client is. This reference architecture is intended for advanced practitioners who run Cloud Service Mesh but it works for Istio on Google Kubernetes Engine (GKE) too.

## Mesh ingress gateway

Istio 0.8 introduced the mesh [ingress gateway](https://istio.io/latest/docs/concepts/traffic-management/#gateways). The gateway provides a dedicated set of proxies whose ports are exposed to traffic coming from outside the service mesh. These mesh ingress proxies let you control network exposure behavior separately from application routing behavior. 

The proxies also let you apply routing and policy to mesh-external traffic before it arrives at an application sidecar. Mesh ingress defines the treatment of traffic when it reaches a node in the mesh, but external components must define how traffic first arrives at the mesh.

To manage this external traffic, you need a load balancer that is external to the mesh. This reference architecture uses Google Cloud Load Balancing provisioned through GKE Gateway resources to automate deployment.

For Google Cloud, the [canonical example](https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/#determining-the-ingress-ip-and-ports) of this setup is an external load balancing service that deploys a public network load balancer (L4). That load balancer points at the NodePorts of a GKE cluster. These NodePorts expose the Istio ingress gateway Pods, which route traffic to downstream mesh sidecar proxies. 

## Architecture

The following diagram illustrates this topology. Load balancing for internal private traffic looks similar to this architecture, except that you deploy an internal passthrough Network Load Balancer instead.

![An external load balancer routes external clients to the mesh through ingress gateway proxies.](https://docs.cloud.google.com/static/architecture/images/exposing-service-mesh-apps-through-gke-ingress-standard-approach.svg)

The preceding diagram shows that using L4 transparent load balancing with a mesh ingress gateway offers the following advantages:

  * The setup simplifies deploying the load balancer.
  * The load balancer provides a stable virtual IP address (VIP), health checking, and reliable traffic distribution when cluster changes, node outages, or process outages occur.
  * All routing rules, TLS termination, and traffic policy is handled in a single location at the mesh ingress gateway.

**Note:** For applications in Cloud Service Mesh, deployment of the external TCP/UDP load balancer is the default exposure type. You deploy the load balancer through the Kubernetes Service, which selects the Pods of the mesh ingress proxies.

## GKE Gateway and Services

You can provide access to applications for clients that are outside the cluster in many ways. GKE Gateway is an implementation of the [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/). GKE Gateway [evolves the Ingress resource and improves it](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).

As you deploy GKE Gateway resources to your GKE cluster, the Gateway controller watches the Gateway API resources and reconciles Cloud Load Balancing resources to implement the networking behavior that's specified by the GKE Gateway resources.

When using GKE Gateway, the type of load balancer you use to expose applications to clients depends largely on the following factors:

  * The status of the clients (external or internal).
  * The required capabilities of the load balancer, including the capability to integrate with Google Cloud Armor security policies.
  * The spanning requirements of the service mesh. Service meshes can span multiple GKE clusters or can be contained in a single cluster.



In GKE Gateway, this behavior is controlled by specifying the appropriate [GatewayClass](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

**Note:** Although you can expose applications hosted in Cloud Service Mesh through Node IP addresses directly, we don't recommend this approach for most production environments. Direct exposure through Node IP addresses is fragile and can also become a security risk. To direct traffic to applications hosted in Cloud Service Mesh, we recommend that you use an L4 or L7 load balancer.

Although the default load balancer for Cloud Service Mesh is the Network Load Balancer, this reference architecture focuses on the external Application Load Balancer (L7). The external Application Load Balancer provides integration with edge services like Identity-Aware Proxy and Google Cloud Armor, URL redirects and rewrites, as well as a globally distributed network of edge proxies. The next section describes the architecture and advantages of using two layers of HTTP load balancing.

## Cloud ingress and mesh ingress

Deploying external L7 load balancing outside of the mesh along with a mesh ingress layer offers significant advantages, especially for internet traffic. Even though Cloud Service Mesh and Istio ingress gateways provide advanced routing and traffic management in the mesh, some functions are better served at the edge of the network. Taking advantage of internet-edge networking through Google Cloud's external Application Load Balancer might provide significant performance, reliability, or security-related benefits over mesh-based ingress. These benefits include the following:

  * [Global Anycast VIP advertisement and globally distributed TLS and HTTP termination](https://docs.cloud.google.com/docs/security/infrastructure/design#google-frontend-service)
  * [DDoS defense and traffic filtering at the edge with Google Cloud Armor](https://docs.cloud.google.com/armor/docs/security-policy-concepts)
  * [API gateway functionality with IAP](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto)
  * [Automatic public certificate creation and rotation with Google Certificate Manager](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway)
  * [Multi-cluster and multi-regional load balancing at the edge with Multi Cluster Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enabling-multi-cluster-gateways)



This external layer of L7 load balancing is referred to as _cloud ingress_ because it is built on cloud-managed load balancers rather than the self-hosted proxies that are used by mesh ingress. The combination of cloud ingress and mesh ingress uses complementary capabilities of the Google Cloud infrastructure and the mesh. The following diagram illustrates how you can combine cloud ingress (through GKE gateway) and mesh ingress to serve as two load balancing layers for internet traffic.

![Cloud ingress acts as the gateway for external traffic to the mesh through the VPC network.](https://docs.cloud.google.com/static/architecture/images/exposing-service-mesh-apps-through-gke-ingress-topology.svg)

In the topology of the preceding diagram, the cloud ingress layer sources traffic from outside of the service mesh and directs that traffic to the mesh ingress layer. The mesh ingress layer then directs traffic to the mesh-hosted application backends.

## Cloud and mesh ingress topology

This section describes the complementary roles that each ingress layer fulfills when you use them together. These roles aren't concrete rules, but rather guidelines that use the advantages of each layer. Variations of this pattern are likely, depending on your use case.

  * **Cloud ingress:** When paired with mesh ingress, the cloud ingress layer is best used for edge security and global load balancing. Because the cloud ingress layer is integrated with DDoS protection, cloud firewalls, authentication, and encryption products at the edge, this layer excels at running these services outside of the mesh. The routing logic is typically straightforward at this layer, but the logic can be more complex for multi-cluster and multi-region environments. Because of the critical function of internet-facing load balancers, the cloud ingress layer is likely managed by an infrastructure team that has exclusive control over how applications are exposed and secured on the internet. This control also makes this layer less flexible and dynamic than a developer-driven infrastructure, a consideration that could impact who and how you provide administrative access to this layer.
  * **Mesh ingress:** When paired with cloud ingress, the mesh ingress layer provides flexible routing that is close to the application. Because of this flexibility, the mesh ingress is better than cloud ingress for complex routing logic and application-level visibility. The separation between ingress layers also makes it easier for application owners to directly control this layer without affecting other teams. To help secure applications When you expose service mesh applications through an L4 load balancer instead of an L7 load balancer, you should terminate client TLS at the mesh ingress layer inside the mesh.



### Health checking

One complexity of using two layers of L7 load balancing is health checking. You must configure each load balancer to check the health of the next layer to ensure that it can receive traffic. The topology in the following diagram shows how cloud ingress checks the health of the mesh ingress proxies, and the mesh, in return, checks the health of the application backends.

![Cloud ingress checks the health of the mesh ingress, and the mesh ingress checks the health of the application backends.](https://docs.cloud.google.com/static/architecture/images/exposing-service-mesh-apps-through-gke-ingress-health-checking.svg)

The preceding topology has the following considerations:

  * **Cloud ingress:** In this reference architecture, you configure the Google Cloud load balancer through the Gateway to check the health of the mesh ingress proxies on their exposed health check ports. If a mesh proxy is down, or if the cluster, mesh, or [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) is unavailable, the Google Cloud load balancer detects this condition and doesn't send traffic to the mesh proxy.
  * **Mesh ingress:** In the mesh application, you perform health checks on the backends directly so that you can execute load balancing and traffic management locally.



## Security

The preceding topology also involves several security elements. One of the most critical elements is in how you configure encryption and deploy certificates. [GKE Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) integrates with [Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/overview). You can refer to a Certificate Manager [`CertificateMap` in your Gateway definition](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-certificate-manager). Internet clients authenticate against the public certificates and connect to the external load balancer as the first hop in the Virtual Private Cloud (VPC).

The next hop, which is between the Google Front End (GFE) and the mesh ingress proxy, is [encrypted by default](https://docs.cloud.google.com/load-balancing/docs/backend-service#encryption_between_the_load_balancer_and_backends). Network-level encryption between the GFEs and their backends is applied automatically. However, if your security requirements dictate that the platform owner retain ownership of the encryption keys, then you can optionally enable HTTP/2 with TLS encryption between the cluster gateway (the GFE) and the mesh ingress (the envoy proxy instance). When you enable HTTP/2 with TLS encryption for this path, you can use a self-signed or public certificate to encrypt traffic because [the GFE doesn't authenticate against it](https://docs.cloud.google.com/load-balancing/docs/backend-service#encryption_between_the_load_balancer_and_backends) This additional layer of encryption is demonstrated in the associated [deployment guide](https://docs.cloud.google.com/architecture/exposing-service-mesh-apps-through-gke-ingress/deployment). To help prevent the mishandling of certificates, don't use the public certificate for the public load balancer elsewhere. Instead, we recommend that you use separate certificates in the service mesh. If you want to use HTTP/2 for the GFE-to-mesh connection but you don't need your own encryption, then you can use [H2C](https://docs.cloud.google.com/load-balancing/docs/https#protocol-to-backends).

If the service mesh mandates TLS, then all traffic is encrypted between sidecar proxies and to the mesh ingress. The following diagram illustrates HTTPS encryption from the client to the Google Cloud load balancer, from the load balancer to the mesh ingress proxy, and from the ingress proxy to the sidecar proxy.

![Security is implemented using managed certificates outside of the mesh and internal certificates inside the mesh.](https://docs.cloud.google.com/static/architecture/images/exposing-service-mesh-apps-through-gke-ingress-security.svg)

## Cost optimization

In this document, you use the following billable components of Google Cloud:

  * [ Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [ Compute Engine](https://cloud.google.com/compute/all-pricing)
  * [ Cloud Load Balancing](https://docs.cloud.google.com/vpc/network-pricing#cloud-load-balancing)
  * [ Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/pricing)
  * [ Google Cloud Armor](https://docs.cloud.google.com/armor/pricing)
  * [ Cloud Endpoints](https://docs.cloud.google.com/endpoints/pricing)



## Deployment

To deploy this architecture, see [From edge to mesh: Deploy service mesh applications through GKE Gateway](https://docs.cloud.google.com/architecture/exposing-service-mesh-apps-through-gke-ingress/deployment).

## What's next

  * Learn about the [additional features offered by GKE Gateway that you can use with your service mesh](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).
  * Learn about [the different types of cloud load balancing available for GKE](https://cloud.google.com/blog/products/containers-kubernetes/exposing-services-on-gke).
  * Learn about [the features and functionality offered by Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-28 UTC."],[],[]] 
