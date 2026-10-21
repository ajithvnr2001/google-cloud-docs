---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-security/
title: Gateway security \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:04.634205+00:00
---

# Gateway security  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Gateway security Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes different methods for securing Gateways in Google Kubernetes Engine (GKE). You can also learn how to [Secure a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway).

## How Gateway security works

A Gateway represents the frontend of a load balancer. There are two paths that you can secure with authentication and encryption for Gateways:

  * Client to Gateway: traffic originated at the client and terminated at the Gateway.
  * Gateway to Pod: traffic originated at the Gateway and terminated at the backend Pods.



The following diagram shows both paths to authenticate and encrypt Gateways:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/gateway-encryption.svg)

In addition to encryption, you can secure the Client-to-Gateway path by using authorization policies. Authorization policies enable a zero-trust architecture by inspecting incoming requests and enforcing access control based on client identities, HTTP headers, and requested paths before the traffic is routed to your backend Pods.

This page describes how to secure the client to Gateway path using certificates uploaded and managed at the Gateway level. To learn how to secure Gateway to Pod traffic, see [Secure load balancer to application traffic using TLS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#load-balancer-tls).

## Benefits

You can secure an application in many different ways using Gateway API, which provides flexibility to different roles interacting with the Gateway.

## Who owns domain and TLS configuration?

The Gateway API model introduces two roles that use or deploy Gateways:

  * **Platform admin** : the cluster operator is the administrator for entire clusters. They manage policies, network access, and application permissions.
  * **Application developer** : the application developer defines their application and Service configuration.



The following diagram shows the fields in the Gateway and HTTPRoute resources that influence TLS and domain ownership for two applications, `store-v1` and `store-v2`.

![](https://docs.cloud.google.com/static/kubernetes-engine/images/gateway-secure-influence.svg)

In the diagram, the cluster operator controls:

  * Which domains application developers can use for their apps in each namespace.
  * The specific certificates that terminate different domains.
  * Certificates provided by the Gateway owner.
  * Whether HTTPRoute owners can specify their own hostnames for certificate generation.



Application developers control the hostname that generates a certificate, if the Gateway definition permits it.

This separation of operational tasks enables application developers to deploy and manage their own HTTPRoute for more distributed control and lets platform administrators deploy and manage Gateways for centralized control of TLS.

## Gateway certificate management

You can secure Gateways using any following methods:

  * Kubernetes Secrets
  * SSL certificates
  * Certificate Manager



If you use Kubernetes Secrets or `SslCertificate` resources from the Compute Engine API, you can attach at most 15 certificates to a single Gateway.

Certificate Manager lets you attach up to 10,000,000 certificates per load balancer, if you request a quota increase.

To learn more about Google Cloud SSL certificates, see [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates).

### Kubernetes Secrets

The [Gateway API spec](https://gateway-api.sigs.k8s.io/guides/tls/) supports [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) for storing and attaching certificates to Gateways. You can associate one or more Kubernetes Secrets with a Gateway using the field `Gateway.spec.tls.certificateRef`.

Gateway resources secured through Kubernetes Secrets have the following requirements:

  * You must be set the Gateway listener `port` and `protocol` to `443` and `HTTPS`.
  * You must set the `listener.tls.mode` field to `Terminate`.
  * You must reference the TLS credentials in the `listeners.tls` block.



Gateway resources secured using Kubernetes Secrets have the following limitations:

  * Only HTTPS listeners terminate traffic using the specified Secrets, although you can specify multiple listeners with a mix of HTTP and HTTPS.
  * If you have multiple listeners using HTTPS on the same Gateway, each listener must have a unique hostname.
  * You can only omit a single hostname or assign `*` for each port and protocol pair.
  * You can only assign one default certificate for each Gateway.



To learn how to secure a Gateway using a Kubernetes Secret, see [Secure a Gateway using a Kubernetes Secret](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-secret).

### SSL certificates

SSL certificates store and deliver certificates to load balancers. An SSL certificate can be either self-managed or Google-managed.

  * Self-managed SSL certificates are certificates that you obtain, provision, and renew yourself.
  * Google-managed SSL certificates are certificates that Google Cloud obtains, manages, and renews automatically.



To learn more about the differences between these two types of certificates, see [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates).

The scope and location of the SSL certificate must match the scope and location of the Gateway that is using it. For example, a global SSL certificate cannot be used by a regional Gateway.

The following table lists the scope and location requirements of SSL certificates for each [GatewayClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_resources):

**GatewayClass** | **SSL certificate scope** | **SSL certificate location**  
---|---|---  
`gke-l7-global-external-managed` | Global SSL certificate | Global  
`gke-l7-global-external-managed-mc`  
`gke-l7-gxlb`  
`gke-l7-gxlb-mc`  
`gke-l7-regional-external-managed` | Regional SSL certificate | Must be the same region as the Gateway  
`gke-l7-regional-external-managed-mc`  
`gke-l7-cross-regional-internal-managed-mc`  
`gke-l7-rilb`  
`gke-l7-rilb-mc`  
  
Google-managed SSL Certificates aren't compatible with regional Gateways. To secure regional Gateways use Certificate Manager instead.

To learn how to secure a Gateway using an SSL certificate, see [Secure a Gateway using an SSL certificate](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-ssl-certificate).

### Certificate Manager

[Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs) is a centralized location to manage your TLS certificates.

When you secure a Gateway using Certificate Manager, you can do the following:

  * Reference a `CertificateMap` directly from a Gateway that you created in Certificate Manager.
  * Manage your own certificates.
  * Improve certificate propagation times.
  * Use Cloud Monitoring for expired certificates and certificate propagation.



Certificate Manager supports both self-managed and Google-managed SSL certificates. To learn how to secure a Gateway using Certificate Manager, see [Secure a Gateway using Certificate Manager](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-certificate-manager).

## GatewayClass TLS support

The following table describes the TLS termination methods that GKE supports for each GatewayClass:

**GatewayClass** |  `gke-l7-global-external-managed`  
`gke-l7-global-external-managed-mc`  
`gke-l7-gxlb`  
`gke-l7-gxlb-mc` |  `gke-l7-regional-external-managed`  
`gke-l7-regional-external-managed-mc`  
`gke-l7-rilb`  
`gke-l7-rilb-mc` |  `gke-l7-cross-regional-internal-managed-mc`  
---|---|---|---  
Client to Gateway TLS | Supported | Supported  
Gateway to backend TLS | Supported | Supported  
Google Cloud certificate resource | Global SSL certificate  
`CertificateMap` | Regional SSL certificate  
Self-managed certificates with Kubernetes Secrets | Supported | Supported | Not supported  
Self-managed Compute Engine SSL certificates | Supported | Supported | Not supported  
Google-managed Compute Engine SSL certificates | Supported | Not supported | Not supported  
Self-managed SSL certificates with Certificate Manager | Supported | Supported | Supported  
Google-managed SSL certificates with Certificate Manager | Supported | Supported | Supported  
  
## Authorization and access control

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

GKE Gateways support identity-based access control by using the GCPAuthzPolicy custom resource. This resource lets platform administrators define explicit `ALLOW` or `DENY` rules for north-south traffic.

Additionally, Gateways can integrate with Service Extensions by using the GCPAuthzExtension resource. This resource enables the Gateway to make inline callouts to external, custom, or third-party authorization engines (such as Identity-Aware Proxy) to evaluate requests in real time.

## What's next

  * Learn how to [secure a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway).
  * Learn how to [deploy Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).
  * Learn more about [Gateway API concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).
  * Learn how to [configure Gateway resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources).
  * Learn how to [use GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
