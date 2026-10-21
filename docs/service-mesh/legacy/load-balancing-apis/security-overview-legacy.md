---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-overview-legacy/
title: Service security (legacy) \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:09.234315+00:00
---

# Service security (legacy)  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-overview-legacy/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Service security (legacy)

This document provides an overview of service security with Cloud Service Mesh using the load balancing APIs. It is intended for Cloud Service Mesh users who want to add authentication, encryption, and authorization to their deployments. This document assumes that you are familiar with [Cloud Service Mesh with Envoy](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/overview) and [with proxyless gRPC applications](https://docs.cloud.google.com/service-mesh/docs/service-routing/proxyless-overview).

This document applies to configurations using the load balancing APIs. If you are using the service routing APIs, see [Service security](https://docs.cloud.google.com/service-mesh/docs/service-routing/security-overview). This is a legacy document.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

Cloud Service Mesh lets you secure service-to-service communications in your mesh. In the mesh, each service has an identity. The following features help support secure communications:

  * Authentication and encryption that use transport layer security (TLS) and mutual TLS (mTLS) for both Cloud Service Mesh with Envoy and Cloud Service Mesh with proxyless gRPC applications. Client TLS policies and server TLS policies control whether services need to prove their identities to each other and use encrypted communication channels.
  * Authorization, based on characteristics of the client and the request. _Authorization policies_ control whether a service is permitted to access another service and which actions are allowed.



Using certificates and keys provided by a private certificate authority (CA), [Google's Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs), makes it easier for you to maintain service security. CA Service provides _GKE mesh certificates_. The GKE mesh certificates feature and Cloud Service Mesh enable you to automatically deploy these certificates and have workloads use them. You modify your Pods to allow workloads to receive and use mTLS credentials. Cloud Service Mesh service security is available only for GKE-based workloads.

In modern microservice-based architectures, smaller, more focused services replace large monolithic applications. Service calls communicate with each other over the network. These calls, which were in-process calls in monolithic applications, present security challenges, so it's best to authenticate, encrypt, and authorize them. These steps support the _zero trust_ principle, in which all network traffic is assumed to be at risk, regardless of whether the traffic originates inside or outside the network.

The service mesh design pattern separates any complexity related to service-to-service communications from the business logic. Instead, the data plane handles this complexity. In addition to reducing application complexity, the service mesh design pattern enables security patterns that might otherwise be difficult to implement and manage.

In this model, proxyless gRPC or Envoy sidecars securely authenticate and encrypt communications by obtaining configuration information from Cloud Service Mesh and certificates from a [CA Service pool](https://docs.cloud.google.com/certificate-authority-service/docs/best-practices).

These security features make your Cloud Service Mesh deployment process easier by providing the following:

  * Automatic provisioning of keys and certificates to all services in your mesh.
  * Automatic rotation of keys and certificates to provide additional security.
  * Integration with Google Kubernetes Engine (GKE) to use all of its capabilities, such as deployment descriptors and labels.
  * High availability of Google managed services, including Cloud Service Mesh and CA Service managed private certificate authority pools.
  * Security tied to Google Identity and Access Management (IAM): service authorization based on authorized Google service accounts.
  * Seamless interoperability with your Envoy-based and proxyless workloads. For example, a service can be behind an Envoy proxy, but the client uses gRPC proxyless service mesh security. Conversely, a service can be behind gRPC proxyless service mesh security, but the client uses an Envoy proxy.



## Secure service-to-service communications

Cloud Service Mesh provides authorization as well as service-to-service security with encryption and authentication that use TLS. Client TLS policies and server TLS policies let services do the following:

  * Assert and validate their identities.
  * Encrypt communication sessions by using TLS or mTLS.



In a service mesh, the data plane handles this type of security so that applications don't need to make special provisions to be secure.

Authorization policies enable you to deny or allow access according to rules that you define.

### Use TLS for encryption

When a service calls on another service by using the HTTP, HTTP/2, or gRPC protocol, traffic that transits the network is in plain text. This traffic might be subject to [person-in-the-middle attacks](https://wikipedia.org/wiki/Man-in-the-middle_attack), in which an attacker intercepts the traffic and inspects or manipulates its contents.

To mitigate this potential issue, you can use HTTP, HTTP/2, or gRPC over TLS with Cloud Service Mesh. When you use these protocols over TLS, traffic between the client and the server is encrypted by using TLS that is based on the server's certificate. Traffic is no longer in plain text, reducing the likelihood that an attacker can intercept and inspect or manipulate its contents.

### Use TLS for authentication

When a service calls on another service, consider the following questions:

  * How does a client know that it is receiving a response from the correct server rather than an imposter? For example, in a typical request-response interaction based on HTTP, the client does not verify the server's identity.

  * What happens if an attacker intercepts that traffic? For example, HTTP traffic is not encrypted, so anyone who receives the traffic can inspect its contents. This is known as a person-in-the-middle attack.




To mitigate these issues, you can use HTTP, HTTP/2, and gRPC over TLS. In these exchanges between a client and a server, the server must use a server certificate to prove its identity to the client. Requests and responses are then encrypted using TLS.

#### Mutual TLS authentication

When Cloud Service Mesh configures application networking for both the client and server—for example, by configuring an Envoy proxy on the client side and another Envoy proxy on the server side—you can take advantage of advanced authentication patterns such as mutual authentication.

In a typical HTTP over TLS exchange, which is not based on mutual authentication, the server has a certificate that it uses to encrypt communications between the client and the server. The client can verify the server's identity by checking the signature that the server sends back during the TLS handshake. However, the server does not verify the client's identity.

When mutual authentication is enabled, the client also has a certificate. The client verifies the server's identity, as described in the previous paragraph, and the server can also verify the client's identity. Both the client and server certificates are used to encrypt the communication channel. This also enables the server to authorize clients based on verified client identity.

[ ![Mutual TLS \(mTLS\) authentication in a service mesh.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-security-mtls.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-security-mtls.svg) Mutual TLS (mTLS) authentication in a service mesh (click to enlarge)

### Authorize service calls

You can choose to allow or deny service access by using authorization policies. Using Cloud Service Mesh, you can define allow and deny rules to authorize access based on request parameters. You can base these rules on Layer 3 and Layer 7 parameters, including client ID, which is derived from the `client-cert` in an mTLS connection, source IP address, host match, method match, and header match. The following diagram shows authorization with Envoy proxies. The process is similar with gRPC clients.

[ ![Authorization in a service mesh.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-security-authz.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-security-authz.svg) Authorization in a service mesh using Envoy (click to enlarge)

### Restrict access using authorization

A best practice within a service mesh is to adhere to the principle of least privilege. You can adhere to this principle by restricting service access to only those callers that depend on the service. When a caller attempts to access a service for which it is not authorized, the attempt is rejected.

With Cloud Service Mesh, you can configure authorization policies that enable your data plane to allow or deny service access based on rules that you define. These policies consist of two components:

  * An action: allow or deny
  * A list of rules



When a request or RPC is sent, the Cloud Service Mesh client on the called service determines whether there is a rule match. If a match is found, the request or RPC is allowed or denied. You can define a rule to match on attributes such as the following:

  * When mTLS is used, the calling service's Kubernetes service account
  * The calling service's IP address (or range of addresses)
  * The destination service's ports
  * The request's HTTP attributes, including hostnames, methods, and user-defined HTTP headers.

**Caution:** If you configure `DENY` rules in conjunction with request attributes such as hosts, ports, and other header matches, we strongly recommend that the rules deny all traffic. Certain requests might be incorrectly allowed. For example, if you configure a `DENY` rule that denies all traffic with `host: service-test`, an attacker who has direct access to your backend might send a request with `service-test:80`. Because this does not match `service-test`, the request is incorrectly allowed and the backend serves the request.

### Secure naming

As an extra security mechanism, you can configure _secure naming_ with Cloud Service Mesh. This lets you define a list of allowed names, or SPIFFE (Secure Production Identity Framework for Everyone) identities, for a particular service that a client is attempting to connect to. During the TLS exchange, the service's backend returns an X.509 certificate to the client. The client then inspects the certificate to confirm that the X.509 certificate matches one of the names or SPIFFE identities. For more information about SPIFFE identities, see [Secure Production Identity Framework for Everyone](https://spiffe.io/).

### Secure traffic at a gateway

To configure your _gateways_ , you can use Cloud Service Mesh. A gateway is a standalone Envoy proxy that typically acts as one of the following:

  * An _ingress gateway_ that handles traffic that is entering a mesh or some other domain
  * An _egress gateway_ that handles traffic that is exiting a mesh or some other domain
  * A reverse proxy or middle proxy that distributes inbound traffic among one or more services



Clients that want to send traffic into the mesh or out of the mesh send traffic to the gateway. The gateway then handles requests according to the rules that you have set up with Cloud Service Mesh. For example, you can enforce that traffic entering your mesh (though the ingress gateway) must be encrypted by using TLS.

## Security components

Cloud Service Mesh service security supports client TLS policies, server TLS policies, and authorization policies. You create these policies so that Cloud Service Mesh can configure your data plane and enable security capabilities. To create or update these policies, you don't need to make changes to your applications.

### Encryption and supported authentication modes

When a service calls on another service, the first step in establishing secure communications is to have each service prove its identity to the other service. The degree to which a service needs to prove its identity is based on the TLS mode that you configure.

You can configure the following levels of security:

  * Unencrypted/unauthenticated
  * TLS
  * Mutual TLS (mTLS)
  * Permissive: mTLS or unencrypted/unauthenticated, depending on how the client initiates the connection



### Certificates and certificate authorities

Certificates and a trusted certificate authority (CA) provide the foundation for trust in a distributed system such as a service mesh. Using certificates, services can prove their identities and verify the identities presented to them in the following ways:

  * A service that wants to prove its identity to another service presents its certificate to the other service. A CA that both services trust cryptographically signs and issues this certificate.
  * The service that receives this certificate can verify that the certificate originated from a CA that it trusts.



Cloud Service Mesh is not a certificate authority. To enable secure communications, you must set up a mechanism that does the following:

  * Provisions identities and certificates
  * Makes the certificates available to Cloud Service Mesh clients, such as Envoy proxies, that Cloud Service Mesh configures



Cloud Service Mesh supports Google's CA Service. The setup guides for Envoy and proxyless gRPC include instructions for setting this up (for details, see What's next).

## Architecture and resources

Cloud Service Mesh includes the Network Security API namespace, which consists of three Google Cloud API resources that let you specify the security policies that should be applied to your data plane.

Two Google Cloud API resources support authentication in the mesh: client TLS policies and server TLS policies. A third resource, the authorization policy, supports authorization.

The Network Services API namespace includes the endpoint policy resource, which enables Cloud Service Mesh to supply configuration (server TLS, client TLS, and authorization policies) to _endpoints_. Endpoints are the Cloud Service Mesh clients that terminate an inbound communication from another Cloud Service Mesh client.

To enable the security service, use the target HTTPS proxy or target gRPC proxy in your deployment. You cannot use the target HTTP proxy or target TCP proxy.

### Client TLS policy

A client TLS policy lets you specify the client-side TLS mode and the certificate provider information to be applied to your data plane. Client TLS policies support TLS and mTLS authentication. Client TLS policies must be attached to a global backend service resource.

When you configure TLS, you must provide a mechanism by which the client validates the certificate that it receives from the server during the TLS exchange by using the `serverValidationCa` API field. The client uses this information to obtain a validation certificate that it can use to validate the server certificate.

When you configure mTLS, you must also provide a mechanism by which the client obtains its certificate and private key by using the `clientCertificate` API field. The client uses this information to present a certificate to the server during the TLS handshake.

In this release, Cloud Service Mesh supports a managed certificate authority, [CA Service](https://docs.cloud.google.com/certificate-authority-service/docs). Configuration is straightforward: you specify the `google_cloud_private_spiffe` plugin name when you configure the certificate provider. This causes your xDS clients to load certificates and keys from a static location. As prerequisites, you must configure CA Service pools and enable mesh certificates on your GKE cluster.

### Server TLS policy

A server TLS policy (`ServerTlsPolicy` resource) lets you specify the server-side TLS mode and the certificate provider information to be applied to your data plane. Server TLS policies support TLS, mTLS, and, with Envoy only, `Open_or_mTLS` authentication. Server TLS policies can be attached to the target HTTPS proxy resource or an endpoint policy resource.

#### Subject alternative names

When you configure a global backend service's `securitySettings` field, you can supply a list of subject alternative names in the `subjectAltNames` field. When a client initiates a TLS handshake with one of the service's backends, the server presents its X.509 certificate. The client inspects the certificate's `subjectAltName` field. If the field contains one of the specified values, the communication continues. This mechanism is described earlier in Secure naming.

### Authorization policy

An authorization policy (`AuthorizationPolicy` resource) specifies how a server authorizes incoming requests or RPCs. It can be configured to allow or deny an incoming request or RPC based on various parameters, such as the identity of the client that sent the request, host, headers, and other HTTP attributes. An authorization policy can be attached to the target HTTPS proxy resource or an endpoint policy resource.

## Limitations

Cloud Service Mesh service security is supported only with GKE. You cannot deploy service security with Compute Engine.

### Limitations with proxyless gRPC applications

Service security for proxyless gRPC services has the following limitations:

  * This release is limited to Java, Python, C++, and Go.



## What's next

  * To learn more about configuration options, see [Cloud Service Mesh service security use cases (legacy)](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-use-cases-legacy).
  * To configure service security with Envoy proxies, see [Setting up Cloud Service Mesh service security with Envoy (legacy)](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-envoy-setup-legacy).
  * To configure service security with proxyless gRPC applications, see [Setting up Cloud Service Mesh service security with proxyless gRPC applications (legacy)](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-proxyless-setup-legacy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
