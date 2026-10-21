---
url: https://docs.cloud.google.com/architecture/build-apps-using-gateway-and-cloud-service/
title: From edge to multi-cluster mesh: Globally distributed applications exposed through GKE Gateway and Cloud Service Mesh \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:17.471298+00:00
---

# From edge to multi-cluster mesh: Globally distributed applications exposed through GKE Gateway and Cloud Service Mesh  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/build-apps-using-gateway-and-cloud-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  From edge to multi-cluster mesh: Globally distributed applications exposed through GKE Gateway and Cloud Service Mesh Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-06-04 UTC

This reference architecture describes the benefits of exposing applications externally through Google Kubernetes Engine (GKE) Gateways running on multiple GKE clusters within a service mesh. This guide is intended for platform administrators.

You can increase the resiliency and redundancy of your services by deploying applications consistently across multiple GKE clusters, where each cluster becomes an additional failure domain. For example, a service's compute infrastructure with a service level objective (SLO) of 99.9% when deployed in a single GKE cluster achieves an SLO of 99.9999% when deployed across two GKE clusters (1 - (0.001)2). You can also provide users with an experience where incoming requests are automatically directed to the least latent and available mesh ingress gateway.

If you're interested in the benefits of exposing service-mesh-enabled applications that run on a single cluster, see [From edge to mesh: Expose service mesh applications through GKE Gateway](https://docs.cloud.google.com/architecture/exposing-service-mesh-apps-through-gke-ingress).

## Architecture

The following architecture diagram shows how data flows through cloud ingress and mesh ingress:

![TLS encryption from the client, a load balancer, and from the mesh.](https://docs.cloud.google.com/static/architecture/images/build-apps-using-gateway-and-cloud-service-ad.svg)

The preceding diagram shows the following data flow scenarios:

  * From the client terminating at the Google Cloud load balancer using its own Google-managed TLS certificate.
  * From the Google Cloud load balancer to the mesh ingress proxy using its own self-signed TLS certificate.
  * From the mesh ingress gateway proxy to the workload sidecar proxies using service mesh-enabled mTLS.



This reference architecture contains the following two ingress layers:

  * **Cloud ingress:** in this reference architecture, you use the [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) (and the [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_controller)) to program the external, multi-cluster HTTP(S) load balancing layer. The load balancer check the mesh ingress proxies across multiple regions, sending requests to the nearest healthy cluster. It also implements a [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) security policy.
  * **Mesh ingress:** In the mesh, you perform health checks on the backends directly so that you can run load balancing and traffic management locally.



When you use the ingress layers together, there are complementary roles for each layer. To achieve the following goals, Google Cloud optimizes the most appropriate features from the cloud ingress layer and the mesh ingress layer:

  * Provide low latency.
  * Increase availability.
  * Use the security features of the cloud ingress layer.
  * Use the security, authorization, and observability features of the mesh ingress layer.



### Cloud ingress

When paired with mesh ingress, the cloud ingress layer is best used for edge security and global load balancing. Because the cloud ingress layer is integrated with the following services, it excels at running those services at the edge, outside the mesh:

  * DDoS protection
  * Cloud firewalls
  * Authentication and authorization
  * Encryption



The routing logic is typically straightforward at the cloud ingress layer. However, it can be more complex for multi-cluster and multi-region environments.

Because of the critical function of internet-facing load balancers, the cloud ingress layer is likely managed by a platform team that has exclusive control over how applications are exposed and secured on the internet. This control makes this layer less flexible and dynamic than a developer-driven infrastructure. Consider these factors when determining administrative access rights to this layer and how you provide that access.

### Mesh ingress

When paired with cloud ingress, the mesh ingress layer provides a point of entry for traffic to enter the service mesh. The layer also provides backend mTLS, authorization policies, and flexible regex matching.

Deploying external application load balancing outside of the mesh with a mesh ingress layer offers significant advantages, especially for internet traffic management. Although service mesh and Istio ingress gateways provide advanced routing and traffic management in the mesh, some functions are better served at the edge of the network. Taking advantage of internet-edge networking through Google Cloud's external Application Load Balancer might provide significant performance, reliability, or security-related benefits over mesh-based ingress.

**Note:** This reference architecture refers to the routing for cloud ingress layers as north-south routing. The routing between mesh ingress layers and service layers, or the routing from service layers to service layers, is referred to as east-west routing.

## Products and features used

The following list summarizes of all the Google Cloud products and features that this referenence architecture uses:

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/overview): A managed Kubernetes service that you can use to deploy and operate containerized applications at scale using Google's infrastructure. For the purpose of this reference architecture, each of the GKE clusters serving an application must be in the same fleet.
  * [Fleets](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview) and [multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways): Services that are used to create containerized applications at enterprise scale using Google's infrastructure and GKE.
  * [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview): A service that helps you to protect your applications and websites against denial of service and web attacks.
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview): A fully managed service mesh based on Envoy and Istio
  * [Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer): A proxy-based L7 load balancer that lets you run and scale your services.
  * [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/overview): A service that lets you acquire and manage TLS certificates for use with Cloud Load Balancing.



### Fleets

To manage multi-cluster deployments, GKE and Google Cloud use fleets to logically group and normalize Kubernetes clusters.

Using one or more fleets can help you uplevel management from individual clusters to entire groups of clusters. To reduce cluster-management friction, use the fleet principle of namespace sameness. For each GKE cluster in a fleet, ensure that you configure all mesh ingress gateways the same way.

Also, consistently deploy application services so that the service balance-reader in the namespace account relates to an identical service in each GKE cluster in the fleet. The principles of sameness and trust that are assumed within a fleet are what let you use the full range of fleet-enabled features in GKE and Google Cloud.

East-west routing rules within the service mesh and traffic policies are handled at the mesh ingress layer. The mesh ingress layer is deployed on every GKE cluster in the fleet. Configure each mesh ingress gateway in the same manner, adhering to the fleet's principle of namespace sameness.

Although there's a single configuration cluster for [GKE Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api), you should synchronize your GKE Gateway configurations across all GKE clusters in the fleet.

If you need to nominate a new configuration cluster, use [ConfigSync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview). ConfigSync helps ensure that all such configurations are synchronized across all GKE clusters in the fleet and helps avoid reconciling with a non-current configuration.

### Mesh ingress gateway

Istio 0.8 introduced the mesh [ingress gateway](https://istio.io/latest/docs/concepts/traffic-management/#gateways). The gateway provides a dedicated set of proxies whose ports are exposed to traffic coming from outside the service mesh. These mesh ingress proxies let you control network exposure behavior separately from application routing behavior.

The proxies also let you apply routing and policy to mesh-external traffic before it arrives at an application sidecar. Mesh ingress defines the treatment of traffic when it reaches a node in the mesh, but external components must define how traffic first arrives at the mesh.

To manage external traffic, you need a load balancer that's external to the mesh. To automate deployment, this reference architecture uses Cloud Load Balancing, which is provisioned through GKE Gateway resources.

### GKE Gateway and multi-cluster services

There are many ways to provide application access to clients that are outside the cluster. GKE Gateway is an implementation of the [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/). GKE Gateway [evolves and improves the Ingress resource](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).

As you deploy GKE Gateway resources to your GKE cluster, the Gateway controller watches the Gateway API resources. The controller reconciles Cloud Load Balancing resources to implement the networking behavior that's specified by the Gateway resources.

When using GKE Gateway, the type of load balancer you use to expose applications to clients depends largely on the following factors:

  * Whether the backend services are in a single GKE cluster or distributed across multiple GKE clusters (in the same fleet).
  * The status of the clients (external or internal).
  * The required capabilities of the load balancer, including the capability to integrate with Cloud Armor security policies.
  * The spanning requirements of the service mesh. Service meshes can span multiple GKE clusters or can be contained in a single cluster.



In Gateway, this behavior is controlled by specifying the appropriate [GatewayClass](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities). When referring to Gateway classes, those classes which can be used in multi-cluster scenarios have a class name ending in `-mc`.

This reference architecture discusses how to expose application services externally through an external Application Load Balancer. However, when using Gateway, you can also create a multi-cluster regional internal Application Load Balancer.

To deploy application services in multi-cluster scenarios you can define the Google Cloud load balancer components in the following two ways:

  * [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress) and [MultiClusterService resources](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress#multiclusterservice_resources)
  * [Multi-cluster Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enabling-multi-cluster-gateways) and [Multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#mcs)



For more information about these two approaches to deploying application services, see [Choose your multi-cluster load balancing API for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-mc-lb-api).

**Note:** Both multi-cluster Ingress and multi-cluster GKE Gateway use multi-cluster services. Multi-cluster services can be deployed across GKE clusters in a fleet, and are identical for the purposes of cross-cluster service discovery. However, the manner in which these services are exposed across clusters within the fleet differ.

Multi Cluster Ingress relies on creating [`MultiClusterService`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress#multiclusterservice_resources) resources. Multi-cluster Gateway relies on creating [`ServiceExport`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#mcs) resources, and referring to [`ServiceImport`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#mcs) resources.

When you use a multi-cluster Gateway, you can enable the additional capabilities of the underlying Google Cloud load balancer by creating [Policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources). The deployment guide associated with this reference architecture shows how to [configure a Google Cloud Armor security policy](https://docs.cloud.google.com/armor/docs/configure-security-policies) to help protect backend services from [cross-site scripting](https://docs.cloud.google.com/armor/docs/waf-rules#cross-site_scripting_xss).

These policy resources target the backend services in the fleet that are exposed across multiple clusters. In multi-cluster scenarios, all such policies must reference the [`ServiceImport` resource and API group](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_cloud_armor).

### Health checking

One complexity of using two layers of L7 load balancing is health checking. You must configure each load balancer to check the health of the next layer. The GKE Gateway checks the health of the mesh ingress proxies, and the mesh, in return, checks the health of the application backends.

  * **Cloud ingress** : In this reference architecture, you configure the Google Cloud load balancer through GKE Gateway to check the health of the mesh ingress proxies on their exposed health check ports. If a mesh proxy is down, or if the cluster, mesh, or region is unavailable, the Google Cloud load balancer detects this condition and doesn't send traffic to the mesh proxy. In this case, traffic would be routed to an alternate mesh proxy in a different GKE cluster or region.
  * **Mesh ingress** : In the mesh application, you perform health checks on the backends directly so that you can run load balancing and traffic management locally.



## Design considerations

This section provides guidance to help you use this reference architecture to develop an architecture that meets your specific requirements for security and compliance, reliability, and cost.

### Security, privacy, and compliance

The architecture diagram in this document contains several security elements. The most critical elements are how you configure encryption and deploy certificates. GKE Gateway integrates with Certificate Manager for these security purposes.

Internet clients authenticate against public certificates and connect to the external load balancer as the first hop in the Virtual Private Cloud (VPC). You can refer to a Certificate Manager [`CertificateMap` in your Gateway definition](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-certificate-manager). The next hop is between the Google Front End (GFE) and the mesh ingress proxy. That hop is [encrypted by default](https://docs.cloud.google.com/load-balancing/docs/backend-service#encryption_between_the_load_balancer_and_backends).

Network-level encryption between the GFEs and their backends is applied automatically. If your security requirements dictate that the platform owner retain ownership of the encryption keys, you can enable HTTP/2 with TLS encryption between the cluster gateway (the GFE) and the mesh ingress (the envoy proxy instance).

When you enable HTTP/2 with TLS encryption between the cluster gateway and the mesh ingress, you can use a self-signed or a public certificate to encrypt traffic. You can use a self-signed or a public certificate because the GFE doesn't authenticate against it. This additional layer of encryption is demonstrated in the deployment guide associated with this reference architecture.

If you want to use HTTP/2 for the GFE-to-mesh connection but you don't need your own encryption, then you can use [H2C](https://docs.cloud.google.com/load-balancing/docs/https#protocol-to-backends).

To help prevent the mishandling of certificates, don't reuse public certificates. Use separate certificates for each load balancer in the service mesh.

To help create external DNS entries and TLS certificates, the deployment guide for this reference architecture uses [Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs). Using Cloud Endpoints lets you create an externally available `cloud.goog` subdomain. In enterprise-level scenarios, use a more appropriate domain name, and create an A record that points to the global Application Load Balancer IP address in your DNS service provider.

If the service mesh you're using mandates TLS, then all traffic between sidecar proxies and all traffic to the mesh ingress is encrypted. The architecture diagram shows HTTPS encryption from the client to the Google Cloud load balancer, from the load balancer to the mesh ingress proxy, and from the ingress proxy to the sidecar proxy.

### Reliability and resiliency

A key advantage of the multi-cluster, multi-regional edge-to-mesh pattern is that it can use all of the features of service mesh for east-west load balancing, like traffic between application services.

This reference architecture uses a multi-cluster GKE Gateway to route incoming cloud-ingress traffic to a GKE cluster. The system selects a GKE cluster based on its proximity to the user (based on latency), and its availability and health. When traffic reaches the Istio ingress gateway (the mesh ingress), it's routed to the appropriate backends through the service mesh.

An alternative approach for handling the east-west traffic is through multi-cluster services for all application services deployed across GKE clusters. When using multi-cluster services across GKE clusters in a fleet, service endpoints are collected together in a [`ClusterSet`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#consuming_cross-cluster_services). If a service needs to call another service, then it can target any healthy endpoint for the second service. Because endpoints are chosen on a rotating basis, the selected endpoint could be in a different zone or a different region.

A key advantage of using service mesh for east-west traffic rather than using multi-cluster services is that service mesh can use locality load balancing. Locality load balancing isn't a feature of multi-cluster services, but you can configure it through a [`DestinationRule`](https://istio.io/latest/docs/tasks/traffic-management/locality-load-balancing/failover/).

Once configured, a call from one service to another first tries to reach a service endpoint in the same zone, then it tries in the same region as the calling service. Finally, the call only targets an endpoint in another region if a service endpoint in the same zone or same region is unavailable.

## Deployment

To deploy this architecture, see [From edge to multi-cluster mesh: Deploy globally distributed applications through GKE Gateway and Cloud Service Mesh](https://docs.cloud.google.com/architecture/build-apps-using-gateway-and-cloud-service/deployment).

## What's next

  * Learn about [more features offered by GKE Gateway that you can use with your service mesh](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).
  * Learn about [the different types of Cloud Load Balancing available for GKE](https://cloud.google.com/blog/products/containers-kubernetes/exposing-services-on-gke).
  * Learn about [the features and functionality offered by Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Alex Mattson](https://www.linkedin.com/in/alex-m-b505564) | Application Specialist Engineer
  * [Mark Chilvers](https://www.linkedin.com/in/mark-c-77b3a03a) | Application Specialist Engineer



Other contributors: 

  * [Abdelfettah Sghiouar](https://www.linkedin.com/in/sabdelfettah) | Cloud Developer Advocate
  * [Arunkumar Jayaraman](https://www.linkedin.com/in/arunkumar-jayaraman-9252463) | Principal Engineer
  * [Greg Bray](https://www.linkedin.com/in/gregorysbray) | Customer Engineer
  * [Megan Yahya](https://www.linkedin.com/in/meganyahya) | Product Manager
  * [Paul Revello](https://www.linkedin.com/in/paul-revello) | Cloud Solutions Architect
  * [Valavan Rajakumar](https://www.linkedin.com/in/valavanr) | Key Enterprise Architect
  * [Maridi (Raju) Makaraju](https://www.linkedin.com/in/mmraju) | Supportability Tech Lead



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-04 UTC."],[],[]] 
