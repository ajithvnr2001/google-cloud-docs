---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/security/best-practices/
title: Cloud Service Mesh security best practices \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:03.116354+00:00
---

# Cloud Service Mesh security best practices  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/security/best-practices/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh security best practices

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview).

This document describes best practices to establish and govern a secure [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview) configuration running on Google Kubernetes Engine (GKE). The guidance in the document goes beyond the settings used to configure and install Cloud Service Mesh and describes how you can use Cloud Service Mesh with other Google Cloud products and features to protect against the security threats that applications in a mesh may face.

The intended audience for this document includes administrators who manage policies in a Cloud Service Mesh and users who run services in a Cloud Service Mesh. The security measures described here are also useful for organizations that need to enhance the security of their service meshes to meet compliance requirements.

The document is organized as follows:

  * Introduction
  * Attack vectors and security risks
    * Attack vectors
    * Security risks
  * Measures to protect a service mesh
    * Security architecture
    * Cluster security
      * Enable strict mutual TLS
      * Enable access controls
        * Enforce Cloud Service Mesh authentication policies
        * JSON Web Token (JWT)
        * Cloud Service Mesh user authentication
        * Enforce authorization policies
        * Enforce token exchange for accessing mesh services
      * Securely handle Cloud Service Mesh policy exceptions
        * Enforce Kubernetes Network Policies
      * Secure control plane access
      * Enforce namespace boundaries
        * Enforce Kubernetes RBAC policies
    * Mesh edge security
      * Cluster ingress access control
      * Regulate cluster egress traffic
      * Use private cluster or VPC Service Control to lock down external accesses
      * Defend against external DDoS attacks
    * Security for mesh administration and automation
      * Segment the roles used for mesh operations
      * Automatically validate policy configurations
        * Use a GitOps approach with Config Sync to prevent configuration drift
      * Enforce Audit Logging and monitoring
      * Protect the certificate authority for in-cluster certificates
    * Workload security
      * Restrict Pod privileges
      * Secure container images
      * Mitigate against mesh vulnerabilities
      * Use Workload Identity Federation for GKE to securely access Google services
      * Monitor security status through security dashboard and telemetry
    * Security for sensitive user data and credentials



## Introduction

Cloud Service Mesh provides features and tools that help you observe, manage, and secure services in a unified way. It takes an application-centric approach and uses trusted application identities rather than a network IP-focused approach. You can deploy a service mesh transparently without the need to modify existing application code. Cloud Service Mesh provides declarative control over network behavior, which helps to decouple the work of teams that are responsible for delivering and releasing application features from the responsibilities of administrators responsible for security and networking.

Cloud Service Mesh is based on the open source [Istio service mesh](https://istio.io/latest/), which enables sophisticated configurations and topologies. Depending on the structure of your organization, one or more teams or roles may be responsible for installing and configuring a mesh. The default Cloud Service Mesh settings are chosen to protect applications, but in some cases, you may need custom configurations or to grant exceptions by excluding certain apps, ports, or IP addresses from participating in a mesh. Having controls in place to govern mesh configurations and security exceptions is important.

**Note:** This guide complements [Istio's security best practices documentation](https://istio.io/latest/docs/ops/best-practices/security/), which includes detailed configuration recommendations for mutual TLS (mTLS), authorization policies, gateways, and other security configurations. You should treat these recommendations as a foundation to be used together with the best practices discussed in this guide. This guide describes additional best practices for Cloud Service Mesh and how technologies in Google Cloud can secure all layers, components, and information flows in a mesh.

## Attack vectors and security risks

### Attack vectors

Cloud Service Mesh security follows the zero trust security model which assumes security threats originate from both inside and outside of an organization's security perimeter. Examples of security attack types that may threaten applications in a service mesh include:

  * Data exfiltration attacks. For example, attacks that eavesdrop on sensitive data or credentials from service-to-service traffic.
  * Man-in-the-middle attacks. For example, a malicious service that masquerades as a legitimate service to obtain or modify the communication between services.
  * Privilege escalation attacks. For example, attacks that use illicit access to elevated privileges to conduct operations in a network.
  * Denial of service (DoS) attacks.
  * Botnet attacks that try to compromise and manipulate services to launch attacks on other services.



The attacks can also be categorized based on the attack targets:

  * Mesh internal network attacks. Attacks aimed at tampering, eavesdropping, or spoofing the mesh internal service-to-service or service-to-control-plane communication.
  * Control plane attacks. Attacks aimed at causing the control plane to malfunction (such as a DoS attack), or exfiltrating sensitive data from the control plane.
  * Mesh edge attacks. Attacks aimed at tampering, eavesdropping, or spoofing the communication at the mesh ingress or egress.
  * Mesh operation attacks. Attacks aimed at the mesh operations. Attackers may try to obtain elevated privileges to conduct malicious operations in a mesh, such as modifying its security policies and workload images.



### Security risks

Besides security attacks, a mesh also faces other security risks. The following list describes a few possible security risks:

  * Incomplete security protection. A service mesh has not been configured with authentication and authorization policies to protect its security. For example, no authentication or authorization policies are defined for services in a mesh.
  * Security policy exceptions. To accommodate their specific use cases, users may create security policy exceptions for certain traffic (internal or external) to be excluded from Cloud Service Mesh security policies. To securely handle such cases, please refer to the section Securely handle exceptions to policies.
  * Neglect of image upgrades. Vulnerabilities may be discovered for the images used in a mesh. You need to keep the mesh component and workload images up-to-date with the latest vulnerability fixes.
  * Lack of maintenance (no expertise or resources). The mesh software and policy configurations need regular maintenance to take advantage of the latest security protection mechanisms.
  * Lack of visibility. Misconfiguration or insecure configurations of mesh policies and abnormal mesh traffic/operations are not brought to the attention of mesh administrators.
  * [Configuration drift](https://cloud.google.com/anthos-config-management/docs/how-to/prevent-config-drift). The configuration of policies in a mesh deviates from the source of truth.



## Measures to protect a service mesh

This section presents an operating manual to secure service meshes.

### Security architecture

The security of a service mesh depends on the security of the components at different layers of the mesh system and its applications. The high-level intention of the proposed Cloud Service Mesh security posture is to secure a service mesh through integrating multiple security mechanisms at different layers, which jointly achieve the overall system security under the zero-trust security model. The following diagram shows the proposed Cloud Service Mesh security posture.

![security posture of Cloud Service Mesh](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/security-posture-of-anthos-service-mesh.svg)

Cloud Service Mesh provides security at multiple layers, including:

  * Mesh edge security 
    * Cloud Service Mesh ingress security provides access control for external traffic and secures external access to the APIs exposed by the services in the mesh.
    * Cloud Service Mesh egress security regulates the outbound traffic from internal workloads.
    * [Cloud Service Mesh User Auth](https://docs.cloud.google.com/service-mesh/v1.29/docs/security/end-user-auth) integrates with Google infrastructure to authenticate external calls from web browsers to the services that run web applications.
    * Cloud Service Mesh [gateway certificate management](https://docs.cloud.google.com/service-mesh/v1.29/docs/tutorials/automate-tls) protects and rotates the private keys and X.509 certificates used by Cloud Service Mesh ingress and egress gateways using Certificate Authority Service.
    * [Cloud Armor](https://cloud.google.com/armor) can defend against external distributed denial-of-service (DDoS) and Layer 7 attacks. It serves as a Web Application Firewall (WAF) to protect the mesh from network attacks. For example, injection and remote code execution attacks.
    * [VPC and VPC Service Controls](https://cloud.google.com/vpc-service-controls) protect the mesh edge through the private network access controls.
  * Cluster security 
    * Cloud Service Mesh mutual TLS (mTLS) enforces workload-to-workload traffic encryption and authentication.
    * Managed CA, such as Cloud Service Mesh certificate authority and Certificate Authority Service, securely provisions and manages certificates used by the workloads.
    * Cloud Service Mesh authorization enforces access control for mesh services based on their identities and other attributes.
    * [GKE Enterprise security dashboard](https://cloud.google.com/anthos/docs/concepts/security-monitoring) provides monitoring of the configurations of security policies and Kubernetes Network Policies for the workloads.
    * Kubernetes Network Policy enforces Pod access control based on IP addresses, Pod labels, namespaces, and more.
    * Control plane security defends against attacks on the control plane. This protection prevents attackers from modifying, exploiting, or leaking service and mesh configuration data.
  * Workload security 
    * Stay up-to-date with Cloud Service Mesh security releases to ensure the Cloud Service Mesh binaries running in your mesh are free of publicly known vulnerabilities.
    * [Workload Identity Federation for GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) enables workloads to obtain credentials to securely call Google services.
    * Kubernetes CNI (Container Network Interface) prevents privilege escalation attacks by eliminating the need for a privileged Cloud Service Mesh init container.
  * Operator security 
    * Kubernetes role-based access control (RBAC) restricts access to Kubernetes resources and confines operator permissions to mitigate attacks originating from malicious operators or operator impersonation.
    * [GKE Enterprise Policy Controller](https://cloud.google.com/anthos-config-management/docs/concepts/policy-controller) validates and audits policy configurations in the mesh to prevent misconfigurations.
    * [Google Cloud Binary Authorization](https://cloud.google.com/binary-authorization) ensures that the workload images in the mesh are the ones authorized by the administrators.
    * Google Cloud Audit Logging audits mesh operations.



The diagram below shows the communication and configuration flows with the integrated security solutions in Cloud Service Mesh.

![security diagram traffic flow](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/security-diagram-traffic-flow.svg)

### Cluster security

#### Enable strict mutual TLS

A man-in-the-middle (MitM) attack tries to insert a malicious entity between two communicating parties in order to eavesdrop on or manipulate the communication. Cloud Service Mesh defends against MitM and data exfiltration attacks by enforcing [mTLS authentication and encryption](https://docs.cloud.google.com/service-mesh/v1.29/docs/security/security-overview#mutual_tls) for all communicating parties. Permissive mode uses mTLS when both sides support it, but allows connections without mTLS. By contrast, strict mTLS requires that traffic be encrypted and authenticated with mTLS and does not allow plain text traffic.

Cloud Service Mesh allows you to [configure the minimum TLS version](https://docs.cloud.google.com/service-mesh/v1.29/docs/security/configuring-mtls#configure_the_minimum_tls_version_for_your_workloads) for the TLS connections among your workloads to meet your security and compliance requirements.

For more information, see [Cloud Service Mesh by example: mTLS | Enforcing mesh-wide mTLS](https://docs.cloud.google.com/service-mesh/v1.29/docs/security/configuring-mtls#enforce_mesh-wide_mtls).

#### Enable access controls

Cloud Service Mesh security policies (such as authentication and authorization policies) should be enforced on all traffic in and out of the mesh unless there are strong justifications to exclude a service or Pod from Cloud Service Mesh security policies. In some cases, users may have legitimate reasons to bypass Cloud Service Mesh security policies for some ports and IP ranges. For example, to establish native connections with services not managed by Cloud Service Mesh. To secure Cloud Service Mesh under such use cases, please refer to Securely handle Cloud Service Mesh policy exceptions.

Service access control is critical in preventing unauthorized access to services. mTLS enforcement encrypts and authenticates a request but a mesh still needs [Cloud Service Mesh authorization policies](https://docs.cloud.google.com/service-mesh/v1.29/docs/security/authorization-policy-overview) to enforce access control on services. For example, rejecting an unauthorized request coming from an authenticated client.

Cloud Service Mesh authorization policies provide a flexible way to configure access controls to defend your services against unauthorized access. Cloud Service Mesh authorization policies should be enforced based on the authenticated identities derived from the authentication results - mTLS or JSON Web Token (JWT) based authentications should be used together as part of Cloud Service Mesh authorization policies.

#### Enforce Cloud Service Mesh authentication policies

**JSON Web Token (JWT)**

In addition to mTLS authentication, mesh administrators can require a service to [authenticate and authorize requests based on JWT](https://istio.io/latest/docs/tasks/security/authentication/authn-policy/#end-user-authentication). Cloud Service Mesh does not act as a JWT provider but authenticates JWTs based on the configured JSON web key set (JWKS) endpoints. JWT authentication can be applied to ingress gateways for external traffic or to internal services for in-mesh traffic. JWT authentication can be combined with mTLS authentication when a JWT is used as a credential to represent the end caller and the requested service requires proof that it is being called on behalf of the end caller. Enforcing JWT authentication defends against attacks that access a service without valid credentials and on behalf of a real end user.

**Cloud Service Mesh user authentication**

[Cloud Service Mesh user authentication](https://docs.cloud.google.com/service-mesh/v1.29/docs/security/end-user-auth) is an integrated solution for browser-based end-user authentication and access control to your workloads. It integrates a service mesh with existing Identity Providers (IdP) to implement a standard web-based OpenID Connect (OIDC) login and consent flow and uses Cloud Service Mesh authorization policies for access control.

**Enforce authorization policies**

Cloud Service Mesh authorization policies control:

  * Who or what is allowed to access a service.
  * Which resources can be accessed.
  * Which operations can be conducted on the allowed resources.



Authorization policies are a versatile way to configure access control based on the actual identities that services run as, application layer (Layer 7) properties of traffic (for example request headers), and network layer (Layer 3 and Layer 4) properties like IP ranges and ports.

Cloud Service Mesh authorization policies should be enforced based on authenticated identities derived from the authentication results to defend against unauthorized access to services or data.

By default, access to a service should be denied unless an authorization policy is explicitly defined to allow access to the service. See [Authorization Policy Best Practices](https://docs.cloud.google.com/service-mesh/v1.29/docs/security/authorization-policy-overview#best_practices) for examples of authorization policies that deny access requests.

Authorization policies should restrict trust as much as possible. For example, the access to a service can be defined based on individual URL paths exposed by a service such that only a service A can access the path `/admin` of a service B.

Authorization policies can be used together with [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/), which only operate at the network layer (Layer 3 and Layer 4) and control the network access for IP addresses and ports on Kubernetes Pods and Kubernetes namespaces.

**Note:** Cloud Service Mesh does not handle non-TCP traffic (for example UDP), so it cannot be controlled by authorization policies. Mesh administrators can use Kubernetes Network Policies to define policies for UDP traffic. For example, if mesh services do not use UDP then mesh administrators can define a Kubernetes network policy to block UDP traffic.

**Enforce token exchange for accessing mesh services**

To defend against token replay attacks which steal tokens and re-use the stolen tokens to access mesh services, a token in a request from outside the mesh should be exchanged for a short-lived mesh-internal token at the mesh edge.

A request from outside the mesh to access a mesh service needs to include a token, such as JWT or cookie, in order to be authenticated and authorized by the mesh service. A token from outside the mesh may be long-lived. To defend against token replay attacks, a token from outside the mesh should be exchanged for a short-lived mesh-internal token with a limited scope at the ingress of the mesh. The mesh service authenticates a mesh-internal token and authorizes the access request based on the mesh-internal token.

## What's next

  * [Review best practices for using Cloud Service Mesh egress gateways on GKE clusters ](https://docs.cloud.google.com/service-mesh/v1.29/docs/security/egress-gateways-best-practices)
  * [Configure transport security](https://docs.cloud.google.com/service-mesh/v1.29/docs/security/configuring-mtls)
  * [Update your authorization policies](https://docs.cloud.google.com/service-mesh/v1.29/docs/security/authorization-policy-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
