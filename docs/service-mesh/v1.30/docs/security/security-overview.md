---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/security/security-overview/
title: Cloud Service Mesh security overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:45.400618+00:00
---

# Cloud Service Mesh security overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/security/security-overview/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh security overview

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview).

Cloud Service Mesh with Istio APIs security helps you _mitigate insider threats_ and _reduce the risk of a data breach_ by ensuring that all communications between workloads are encrypted, mutually authenticated, and authorized.

Traditionally, micro-segmentation that uses IP-based rules has been used to mitigate insider risks. However, the adoption of containers, shared services, and distributed production environments spread across multiple clouds makes this approach harder to configure and even harder to maintain.

With Cloud Service Mesh, you can configure a layer of _service context-aware_ and _request context-aware_ network security that is independent of the security of the underlying network. Because of this, Cloud Service Mesh lets you adopt a defense-in-depth posture that is consistent with _Zero Trust_ security principles. It lets you achieve this posture through declarative policies and without modifying any application code.

## mutual TLS

Cloud Service Mesh uses mutual TLS (mTLS) for peer authentication. Authentication refers to identity: who is this service? who is this end-user? and can I trust that they are who they say they are?

mTLS makes it possible for workloads to verify each other's identities and authenticate with each other. You might be familiar with simple TLS through its use in HTTPS to allow browsers to trust web servers and to encrypt the data that is exchanged. When simple TLS is used, the client establishes that the server can be trusted by validating its certificate. mTLS is an implementation of TLS in which both client and server present certificates to each other and verify each other's identities.

mTLS is the means by which Cloud Service Mesh implements both _authentication_ and _encryption_ between services.

In Cloud Service Mesh, auto mTLS is enabled by default. With auto mTLS, a client sidecar proxy automatically detects if the server has a sidecar. The client sidecar sends mTLS to workloads with sidecars and sends plain text to workloads without sidecars. Note, however, services _accept_ both plain-text and mTLS traffic. To secure your service mesh, we recommend that you migrate your services to only accept mTLS traffic.

For more information on enforcing only mTLS, see [Cloud Service Mesh by example: mTLS](https://docs.cloud.google.com/service-mesh/v1.30/docs/tutorials/mtls).

## Security benefits

Cloud Service Mesh provides the following security benefits:

  * **Mitigates risk of replay or impersonation attacks that use stolen credentials.** Cloud Service Mesh relies on mTLS certificates to authenticate peers, rather than bearer tokens such as [JSON Web Tokens](https://jwt.io/introduction/) (JWT). Because mTLS certificates are bound to the TLS channel, it is not possible for an entity within your production environment to impersonate another by replaying the authentication token without access to the private keys.

  * **Ensures encryption in transit.** Using mTLS for authentication also ensures that all TCP communications are encrypted in transit.

  * **Ensures that only authorized clients can access a service with sensitive data.** Only authorized clients can access a service with sensitive data irrespective of the network location of the client and the application-level credentials. You can specify that only clients with authorized service identities or in authorized Kubernetes namespaces can access a service. You can also use IP-based access policies to grant access to clients deployed outside the clients outside the mesh.

  * **Mitigates the risk of user data breach within your production network.** You can ensure that insiders can only access sensitive data through authorized clients. Furthermore, you can ensure that certain clients can only gain access to user data if the client can present a valid and short-lived user token. This mitigates the risk that the compromise of a single client credential grants an attacker access to all user data.

  * **Identifies which clients accessed a service with sensitive data.** Cloud Service Mesh access logging captures the mTLS identity of the client in addition to the IP address. Thus, you can understand which workload accessed a service even if the workload is ephemeral and dynamically deployed, and in a different cluster or Virtual Private Cloud (VPC) network.




## Features

This section describes the features that Cloud Service Mesh provides to realize its security benefits.

### Automatic certificate and key rotation

Using mTLS based on service identities makes it possible to encrypt all TCP communications and provides a more secure non-replayable credential for access control. One of the key challenges of using mTLS at scale is managing the keys and certificates for all target workloads. Cloud Service Mesh takes care of rotating mTLS keys and certificates for mesh workloads without disrupting communications. Configuration of smaller cert refresh intervals is possible to reduce risk.

### Cloud Service Mesh certificate authority

Cloud Service Mesh includes a managed multi-regional private certificate authority, _Cloud Service Mesh certificate authority_ , for issuing certificates for mTLS. Cloud Service Mesh certificate authority is a highly reliable and scalable service that is optimized for dynamically scaled workloads on a cloud platform. With Cloud Service Mesh certificate authority, Google manages the security and availability of the CA backend. Cloud Service Mesh certificate authority lets you rely on a single root of trust across clusters. When using Cloud Service Mesh certificate authority, you can rely on workload identity pools to provide coarse-grained isolation. By default, authentication fails if the client and the server are not in the same workload identity pool.

Certificates from Cloud Service Mesh certificate authority include the following data about your application's services:

  * The Google Cloud project ID
  * The GKE namespace
  * The GKE service account name

**Important:** The certificates issued by Cloud Service Mesh certificate authority should only be used to enable secure service-to-service communication within your service mesh, and not be used for any other purpose. These certificates are sent whenever services attempt to communicate with each other using mutual TLS. Make sure that you don't inadvertently expose confidential information by using these certificates when communicating outside your service mesh.

### Certificate Authority Service

As an alternative to Cloud Service Mesh certificate authority, you can configure Cloud Service Mesh to use Certificate Authority Service, which is suitable for the following use cases:

  * If you need different certificate authorities to sign workload certificates on different clusters.
  * If you need to back your signing keys in a managed HSM.
  * If you are in a highly regulated industry and are subject to compliance.
  * If you want to chain your Cloud Service Mesh CA to a custom enterprise root certificate to sign workload certificates.



The cost of Cloud Service Mesh certificate authority is included in the Cloud Service Mesh pricing. The cost of CA Service isn't included in the base Cloud Service Mesh price and is charged separately. Additionally, CA Service comes with an explicit SLA, but Cloud Service Mesh certificate authority does not.

For this integration, all workloads in Cloud Service Mesh are granted two IAM roles:

  * [privateca.workloadCertificateRequester](https://docs.cloud.google.com/certificate-authority-service/docs/reference/permissions-and-roles)
  * [privateca.auditor](https://docs.cloud.google.com/certificate-authority-service/docs/reference/permissions-and-roles)



### Identity-aware access control (firewall) policies

With Cloud Service Mesh, you can configure network security policies that are based on the mTLS identity versus the IP address of the peer. This lets you create policies that are independent of the network location of the workload. Only communications across clusters in the same Google Cloud project are supported.

### Request claims-aware access control (firewall) policies

In addition to the mTLS identity, you can grant access based on request claims in the JWT header of HTTP or gRPC requests. Cloud Service Mesh lets you assert that a JWT is signed by a trusted entity. This means that you can configure policies that allow access from certain clients only if a request claim exists or matches a specified value.

### User authentication with Identity-Aware Proxy

You authenticate users who are accessing any service exposed on a Cloud Service Mesh ingress gateway by using [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap). IAP can authenticate users who are logging in from a browser, integrate with custom identity providers, and issue a short-lived JWT token or an RCToken that can then be used to grant access at the Ingress gateway or a downstream service (by using a side-car). For more information, see [Integrating IAP with Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/iap-integration).

### User authentication with your existing Identity Provider

You can integrate your existing Identity Provider with Cloud Service Mesh to provide browser-based end-user authentication and access control to your deployed workloads. For more information, see [Configuring Cloud Service Mesh user authentication](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/end-user-auth).

### Access logging and monitoring

Cloud Service Mesh ensures that access logs and metrics are available in [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs), and provides an integrated dashboard to understand access patterns for a service or workload based on this data.

### FIPS compliant

The data plane component uses [FIPS 140-3 validated](https://cloud.google.com/security/compliance/fips-140-2-validated) encryption modules.

## Limitations

Cloud Service Mesh security has the following limitation:

  * User authentication that uses IAP requires that a service be published to the internet. IAP and Cloud Service Mesh let you configure policies that can restrict access to authorized users and clients in an allowed IP range. If you choose to only expose the service to clients within the same network, you need to configure a custom policy engine for user authentication and token issuance.



## What's next

  * [Cloud Service Mesh security best practices](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/anthos-service-mesh-security-best-practices)
  * [Configure transport security](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/configuring-mtls)
  * [Update your authorization policies](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/authorization-policy-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
