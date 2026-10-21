---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/istio-apis/security/best-practices/
title: Cloud Service Mesh with Istio APIs security best practices \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:23.396423+00:00
---

# Cloud Service Mesh with Istio APIs security best practices  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/istio-apis/security/best-practices/

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



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh with Istio APIs security best practices

This document describes best practices to establish and govern a secure [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview) configuration running on Google Kubernetes Engine (GKE). The guidance in the document goes beyond the settings used to configure and provision Cloud Service Mesh and describes how you can use Cloud Service Mesh with other Google Cloud products and features to protect against the security threats that applications in a mesh might face.

The intended audience for this document includes administrators who manage policies in a Cloud Service Mesh and service owners who run services in an Cloud Service Mesh. The security measures described here are also useful for organizations that need to enhance the security of their service meshes to meet compliance requirements.

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
        * Enforce Kubernetes NetworkPolicies
      * Enforce namespace boundaries
        * Enforce Kubernetes RBAC policies
    * Mesh edge security
      * Cluster ingress access control
      * Regulate cluster egress traffic
      * Use private cluster or VPC Service Controls to lock down external accesses
      * Defend against external DDoS attacks
    * Security for mesh administration and automation
      * Segment the roles used for mesh operations
      * Automatically validate policy configurations
        * Use a GitOps approach with Config Sync to prevent configuration drift
      * Enforce Cloud Audit Logs and monitoring
    * Workload security
      * Restrict Pod privileges
      * Secure container images
      * Mitigate against mesh vulnerabilities
      * Use Workload Identity Federation for GKE to securely access Google services
      * Monitor security status through security dashboard and telemetry
    * Security for sensitive user data and credentials



## Introduction

Cloud Service Mesh provides features and tools that help you observe, manage, and secure services in a unified way. It takes an application-centric approach and uses trusted application identities rather than a network IP-focused approach. You can deploy a service mesh transparently without the need to modify existing application code. Cloud Service Mesh provides declarative control over network behavior, which helps to decouple the work of teams that are responsible for delivering and releasing application features from the responsibilities of administrators who are responsible for security and networking.

Cloud Service Mesh is based on the open source [Istio service mesh](https://istio.io/latest/), which enables sophisticated configurations and topologies. Depending on the structure of your organization, one or more teams or roles might be responsible for installing and configuring a mesh. The default Cloud Service Mesh settings are chosen to protect applications, but in some cases, you might need custom configurations or you might need to grant exceptions by excluding certain apps, ports, or IP addresses from participating in a mesh. Having controls in place to govern mesh configurations and security exceptions is important.

This document compliments [Istio's security best practices documentation](https://istio.io/latest/docs/ops/best-practices/security/), which includes detailed configuration recommendations for mutual TLS (mTLS), authorization policies, gateways, and other security configurations. Treat these recommendations as a foundation to be used together with the best practices discussed in this document. This document describes additional best practices for Cloud Service Mesh and how technologies in Google Cloud can secure all layers, components, and information flows in a mesh.

## Attack vectors and security risks

### Attack vectors

Cloud Service Mesh security follows the zero trust security model, which assumes security threats originate from both inside and outside of an organization's security perimeter. The following are examples of security attack types that might threaten applications in a service mesh:

  * Data exfiltration attacks. For example, attacks that eavesdrop on sensitive data or credentials from service-to-service traffic.
  * Man-in-the-middle attacks. For example, a malicious service that masquerades as a legitimate service to obtain or modify the communication between services.
  * Privilege escalation attacks. For example, attacks that use illicit access to elevated privileges to conduct operations in a network.
  * Denial of service (DoS) attacks.
  * Botnet attacks that try to compromise and manipulate services to launch attacks on other services.



The attacks can also be categorized based on the attack targets:

  * Mesh internal network attacks. Attacks aimed at tampering, eavesdropping, or spoofing the mesh internal service-to-service or service-to-control-plane communication.
  * Control plane attacks. Attacks aimed at causing the control plane to malfunction (such as a DoS attack), or exfiltrating sensitive data from the control plane.
  * Mesh edge attacks. Attacks aimed at tampering, eavesdropping, or spoofing the communication at the mesh ingress or egress.
  * Mesh operation attacks. Attacks aimed at the mesh operations. Attackers might try to obtain elevated privileges to conduct malicious operations in a mesh, such as modifying its security policies and workload images.



### Security risks

Besides security attacks, a mesh also faces other security risks. The following list describes a few possible security risks:

  * Incomplete security protection. A service mesh has not been configured with authentication and authorization policies to protect its security. For example, no authentication or authorization policies are defined for services in a mesh.
  * Security policy exceptions. To accommodate their specific use cases, users might create security policy exceptions for certain traffic (internal or external) to be excluded from Cloud Service Mesh security policies. To securely handle such cases, see Securely handle exceptions to policies, in this document.
  * Neglect of image upgrades. Vulnerabilities might be discovered for the images used in a mesh. You need to keep the mesh component and workload images up-to-date with the latest vulnerability fixes.
  * Lack of maintenance (no expertise or resources). The mesh software and policy configurations need regular maintenance to take advantage of the latest security protection mechanisms.
  * Lack of visibility. Misconfiguration or insecure configurations of mesh policies and abnormal mesh traffic or operations are not brought to the attention of mesh administrators.
  * [Configuration drift](https://docs.cloud.google.com/anthos-config-management/docs/how-to/prevent-config-drift). The configuration of policies in a mesh deviates from the source of truth.



## Measures to protect a service mesh

This section presents an operating manual to secure service meshes.

### Security architecture

The security of a service mesh depends on the security of the components at different layers of the mesh system and its applications. The high-level intention of the proposed Cloud Service Mesh security posture is to secure a service mesh through integrating multiple security mechanisms at different layers, which jointly achieve the overall system security under the zero trust security model. The following diagram shows the proposed Cloud Service Mesh security posture.

![security posture of Cloud Service Mesh](https://docs.cloud.google.com/static/service-mesh/v1.26/docs/images/security-posture-of-anthos-service-mesh.svg)

Cloud Service Mesh provides security at multiple layers, including:

  * Mesh edge security 
    * Cloud Service Mesh ingress security provides access control for external traffic and secures external access to the APIs exposed by the services in the mesh.
    * Cloud Service Mesh egress security regulates the outbound traffic from internal workloads.
    * [Cloud Service Mesh user authentication](https://docs.cloud.google.com/service-mesh/v1.26/docs/unified-install/options/end-user-auth) integrates with Google infrastructure to authenticate external calls from web browsers to the services that run web applications.
    * Cloud Service Mesh [gateway certificate management](https://docs.cloud.google.com/service-mesh/v1.26/docs/automate-tls) protects and rotates the private keys and X.509 certificates used by Cloud Service Mesh ingress and egress gateways using Certificate Authority Service.
    * [VPC and VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) protect the mesh edge through the private network access controls.
  * Cluster security 
    * Cloud Service Mesh mutual TLS (mTLS) enforces workload-to-workload traffic encryption and authentication.
    * Cloud Service Mesh certificate authority securely provisions and manages certificates used by the workloads.
    * Cloud Service Mesh authorization enforces access control for mesh services based on their identities and other attributes.
    * [GKE Enterprise security dashboard](https://docs.cloud.google.com/anthos/docs/concepts/security-monitoring) provides monitoring of the configurations of security policies and Kubernetes NetworkPolicies for the workloads.
    * Kubernetes network policy-enforced Pod access control based on IP addresses, Pod labels, namespaces, and more.
  * Workload security 
    * Stay up-to-date with Cloud Service Mesh security releases to ensure the Cloud Service Mesh binaries running in your mesh are free of publicly known vulnerabilities.
    * [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) enables workloads to obtain credentials to securely call Google services.
    * [Cloud Key Management Service (Cloud KMS)](https://cloud.google.com/security/products/security-key-management) secures sensitive data or credentials through hardware security modules (HSMs). For example, workloads can use Cloud KMS to store credentials or other sensitive data. CA Service, which is used to issue certificates to mesh workloads, supports per-customer and HSM-backed signing keys managed by [Cloud KMS](https://docs.cloud.google.com/kms/docs/hsm).
    * Kubernetes Container Network Interface (CNI) prevents privilege-escalation attacks by eliminating the need for a privileged Cloud Service Mesh init container.
  * Operator security 
    * Kubernetes role-based access control (RBAC) restricts access to Kubernetes resources and confines operator permissions to mitigate attacks originating from malicious operators or operator impersonation.
    * [GKE Enterprise Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) validates and audits policy configurations in the mesh to prevent misconfigurations.
    * [Google Cloud Binary Authorization](https://docs.cloud.google.com/binary-authorization) ensures that the workload images in the mesh are the ones authorized by the administrators.
    * Cloud Audit Logs audits mesh operations.



The following diagram shows the communication and configuration flows with the integrated security solutions in Cloud Service Mesh.

![security traffic flow](https://docs.cloud.google.com/static/service-mesh/v1.26/docs/images/security-diagram-traffic-flow.svg)

### Cluster security

This section describes best practices related to cluster security.

#### Enable strict mutual TLS

A man-in-the-middle (MitM) attack tries to insert a malicious entity between two communicating parties to eavesdrop on or manipulate the communication. Cloud Service Mesh defends against MitM and data exfiltration attacks by enforcing [mTLS authentication and encryption](https://docs.cloud.google.com/service-mesh/v1.26/docs/security/security-overview#mutual_tls) for all communicating parties. Permissive mode uses mTLS when both sides support it but allows connections without mTLS. By contrast, strict mTLS requires that traffic be encrypted and authenticated with mTLS and does not allow plain text traffic.

Cloud Service Mesh lets you [configure the minimum TLS version](https://docs.cloud.google.com/service-mesh/v1.26/docs/security/configuring-mtls#configure_the_minimum_tls_version_for_your_workloads) for the TLS connections among your workloads to meet your security and compliance requirements.

For more information, see [Cloud Service Mesh by example: mTLS | Enforcing mesh-wide mTLS](https://docs.cloud.google.com/service-mesh/v1.26/docs/by-example/mtls#enforcing_mesh-wide_mtls).

#### Enable access controls

We recommend that Cloud Service Mesh security policies (such as authentication and authorization policies) be enforced on all traffic in and out of the mesh unless there are strong justifications for excluding a service or Pod from Cloud Service Mesh security policies. In some cases, users might have legitimate reasons to bypass Cloud Service Mesh security policies for some ports and IP address ranges—for example, to establish native connections with services that are not managed by Cloud Service Mesh. To secure Cloud Service Mesh with such use cases, see Securely handle Cloud Service Mesh policy exceptions.

Service access control is critical to preventing unauthorized access to services. mTLS enforcement encrypts and authenticates a request but a mesh still needs [Cloud Service Mesh authorization policies](https://docs.cloud.google.com/service-mesh/v1.26/docs/security/authorization-policy-overview) to enforce access control on services—for example, by rejecting an unauthorized request coming from an authenticated client.

Cloud Service Mesh authorization policies provide a flexible way to configure access controls to defend your services against unauthorized access. Cloud Service Mesh authorization policies are to be enforced based on the authenticated identities derived from the authentication results; mTLS- or JSON Web Token (JWT)-based authentication can be used together as part of Cloud Service Mesh authorization policies.

### Enforce Cloud Service Mesh authentication policies

When considering Cloud Service Mesh authentication policies, consider the following points.

#### JSON Web Token (JWT)

In addition to mTLS authentication, mesh administrators can require a service to [authenticate and authorize requests based on JWT](https://istio.io/latest/docs/tasks/security/authentication/authn-policy/#end-user-authentication). Cloud Service Mesh does not act as a JWT provider but authenticates JWTs based on the configured JSON web key set (JWKS) endpoints. JWT authentication can be applied to ingress gateways for external traffic or to internal services for in-mesh traffic. JWT authentication can be combined with mTLS authentication when a JWT is used as a credential to represent the end caller and the requested service requires proof that it is being called on behalf of the end caller. Enforcing JWT authentication defends against attacks that access a service without valid credentials and on behalf of a real end user.

#### Cloud Service Mesh user authentication

[Cloud Service Mesh user authentication](https://docs.cloud.google.com/service-mesh/v1.26/docs/unified-install/options/end-user-auth) is an integrated solution for browser-based end-user authentication and access control to your workloads. It integrates a service mesh with existing Identity Providers (IdP) to implement a standard web-based OpenID Connect (OIDC) login and consent flow, and it uses Cloud Service Mesh authorization policies for access control.

#### Enforce authorization policies

Cloud Service Mesh authorization policies control:

  * Who or what is allowed to access a service.
  * Which resources can be accessed.
  * Which operations can be conducted on the allowed resources.



Authorization policies are a versatile way to configure access control based on the actual identities that services run as application layer (layer 7) properties of traffic (for example request headers), and network layer (layer 3 and layer 4) properties like IP ranges and ports.

We recommend that Cloud Service Mesh authorization policies be enforced based on authenticated identities derived from authentication results to defend against unauthorized access to services or data.

By default, deny access to a service unless an authorization policy is explicitly defined to allow access to the service. See [Authorization Policy Best Practices](https://docs.cloud.google.com/service-mesh/v1.26/docs/security/authorization-policy-overview#best_practices) for examples of authorization policies that deny access requests.

Authorization policies are intended to restrict trust as much as possible. For example, the access to a service can be defined based on individual URL paths exposed by a service so that only service A can access the path `/admin` of service B.

Authorization policies can be used together with [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/), which only operate at the network layer (layer 3 and layer 4) and control the network access for IP addresses and ports on Kubernetes Pods and Kubernetes namespaces.

**Note:** Cloud Service Mesh does not handle non-TCP traffic (for example, UDP traffic), so it cannot be controlled by authorization policies. Mesh administrators can use Kubernetes Network Policies to define policies for UDP traffic. For example, if mesh services do not use UDP, then mesh administrators can define a Kubernetes network policy to block UDP traffic.

#### Enforce token exchange for accessing mesh services

To defend against token replay attacks, which steal tokens and re-use the stolen tokens to access mesh services, ensure that a token in a request from outside the mesh is exchanged for a short-lived, mesh-internal token at the mesh edge.

A request from outside the mesh to access a mesh service needs to include a token, such as a JWT or a cookie, to be authenticated and authorized by the mesh service. A token from outside the mesh might be long-lived. To defend against token replay attacks, exchange a token from outside the mesh for a short-lived, mesh-internal token with a limited scope at the ingress of the mesh. The mesh service authenticates a mesh-internal token and authorizes the access request based on the mesh-internal token.

Cloud Service Mesh supports [integration with Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/service-mesh/v1.26/docs/security/iap-integration), which generates a `RequestContextToken` (a short-lived mesh-internal token exchanged from an external token) used in Cloud Service Mesh for authorization. With token exchange, attackers cannot use a token stolen in the mesh to access services. The limited scope and lifetime of the exchanged token greatly reduce the chance of a token replay attack.

**Note:** IAP token exchange is different from Cloud Service Mesh user authentication in that IAP exchanges external tokens for short-lived internal tokens to defend against token replay attacks, whereas Cloud Service Mesh user authentication uses web browser-based external calls to web application services.

#### Securely handle Cloud Service Mesh policy exceptions

You might have special use cases for your service mesh. For example, you might need to expose a certain network port to plain text traffic. To accommodate specific usage scenarios, you might sometimes need to create exceptions to allow certain internal or external traffic to be excluded from Cloud Service Mesh security policies, which creates security concerns.

You might have legitimate reasons to bypass Cloud Service Mesh security policies for some ports and IP ranges. You can add [annotations](https://istio.io/latest/docs/reference/config/annotations/), such as, `excludeInboundPorts`, `excludeOutboundPorts`, and `excludeOutboundIPRanges` to Pods to exclude traffic from being handled by the Envoy sidecar. Besides annotations to exclude traffic, you can bypass the mesh altogether by deploying an application with [sidecar injection disabled](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/#controlling-the-injection-policy)— for example, by adding a label `sidecar.istio.io/inject="false"` to the application Pod.

Bypassing Cloud Service Mesh security policies has a negative impact on overall system security. For example, if Cloud Service Mesh mTLS and authorization policies are bypassed for a network port by means of annotations, there is no access control for traffic on the port, and eavesdropping or traffic modification might be possible. Furthermore, bypassing Cloud Service Mesh policies also affects non-security policies, such as network policies.

When Cloud Service Mesh security policy is bypassed for a port or IP address (either intentionally or unintentionally), we strongly recommend that you put other security measures in place to secure the mesh and monitor security exceptions, potential security loopholes, and overall security enforcement status. To secure your mesh in such scenarios you can:

  * Make sure traffic that is bypassing the sidecars is natively encrypted and authenticated to prevent MitM attacks.
  * Enforce Kubernetes network policies to limit the connectivity of ports with policy exceptions—for example, limit a port with policy exceptions to only allow traffic from another service in the same namespace—or to only allow traffic to go through the ports that have Cloud Service Mesh security policy enforced.



#### Use a GitOps approach with Config Sync to prevent configuration drift

Configuration drift occurs when the configuration of policies in a mesh deviates from their source of truth. You can use Config Sync to [prevent configuration drift](https://docs.cloud.google.com/anthos-config-management/docs/how-to/prevent-config-drift#enable).

#### Enforce Cloud Audit Logs and monitoring

We recommend that mesh administrators monitor the following:

  * [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit)
  * [Cloud Service Mesh audit logging](https://docs.cloud.google.com/service-mesh/v1.26/docs/audit-logging)
  * [Policy constraint audit logging](https://docs.cloud.google.com/anthos-config-management/docs/how-to/auditing-constraints)
  * [Anthos Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/monitoring-config-sync)
  * [Access logs](https://istio.io/latest/docs/tasks/observability/logs/access-log/)
  * [Service-level metrics](https://docs.cloud.google.com/service-mesh/v1.26/docs/observability-overview)
  * [Use Cloud Trace](https://docs.cloud.google.com/service-mesh/v1.26/docs/observability/accessing-traces)



Administrators can use these observability resources to verify that the security configuration is working as expected and to monitor any exceptions to security policy enforcement. For example, access that did not go through sidecars, access that did not have valid credentials but reached a service.

While open source observability software (for example, [Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus)) can be used with Cloud Service Mesh, we highly recommend using [Google Cloud Observability](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/concepts/logging-and-monitoring#logging_and_monitoring). This built-in observability solution for Google Cloud provides logging, metric collection, monitoring, and alerting, which is fully managed.

### Workload security

Workload security protects against attacks that compromise workload Pods and then use the compromised Pods to launch attacks against the cluster (for example, botnet attacks).

#### Restrict Pod privileges

A Kubernetes Pod might have privileges that impact other Pods on the node or the cluster. It is important to enforce security restrictions on workload Pods to prevent a compromised Pod from launching attacks against the cluster.

To enforce the least privilege principle for the workloads on a Pod:

  * The services deployed in a mesh should run with as few privileges as possible.
  * You can configure Cloud Service Mesh to use an init container to configure iptables traffic redirection to the sidecar. This requires the user to create workload deployments that have privileges for deploying containers with NET_ADMIN and NET_RAW capabilities. To avoid the risk of running containers with elevated privileges, mesh administrators can instead [enable](https://docs.cloud.google.com/service-mesh/v1.26/docs/unified-install/options/enable-optional-features#istio_container_network_interface) the [Istio CNI plugin](https://istio.io/latest/docs/setup/additional-setup/cni) for configuring traffic redirection to sidecars.



#### Secure container images

Attackers might launch attacks by exploiting vulnerable container images. Administrators should enforce [Binary Authorization](https://docs.cloud.google.com/binary-authorization) to verify the integrity of container images and ensure only trusted container images are deployed in the mesh.

#### Mitigate against mesh vulnerabilities

  * [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview) can scan and surface vulnerabilities on GKE workloads.
  * Common vulnerabilities and exposures (CVE) handling. After a vulnerability is discovered in a container image, the mesh administrators can fix the vulnerability as soon as possible. Google automatically handles patching CVEs that impact the mesh images.



### Use Workload Identity Federation for GKE to securely access Google services

[Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) is the recommended way for mesh workloads to securely access Google services. The alternative of storing a [service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) in a Kubernetes secret and using the service account key to access Google services is not as secure due to the risks of [credential leakage, privilege escalation, information disclosure, and non-repudiation](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

#### Monitor security status through security dashboard and telemetry

A service mesh might have security exceptions and potential loopholes. It is critical to surface and monitor the security status of a mesh, which includes the security policies enforced, security exceptions, and potential security loopholes in the mesh. You can use the [GKE Enterprise security dashboard](https://docs.cloud.google.com/anthos/docs/concepts/security-monitoring) and telemetry to surface and monitor the mesh security status.

[Telemetry](https://docs.cloud.google.com/anthos/docs/concepts/overview#service_mesh_dashboard) monitors the health and performance of services in a mesh, which enables mesh administrators to observe the behaviors of services (such as SLOs, abnormal traffic, service outage, topology).

The GKE Enterprise security dashboard shows the security policies applied to a workload in a service mesh, including access control policies (Kubernetes Network Policies, Binary Authorization policies, and service access control policies), and authentication policies (mTLS).

### Security for sensitive user data and credentials

If you store sensitive user data or credentials in the cluster persistent storage, such Kubernetes secrets or directly in Pods, the data or credentials can be vulnerable to attacks originating from Pods or malicious operations. The data are also vulnerable to network attacks if they are transferred over the network for authentication to services.

  * If possible, store sensitive user data and credentials in protected storage, such as [Secret Manager](https://docs.cloud.google.com/secret-manager) and [Cloud KMS](https://cloud.google.com/security/products/security-key-management).
  * Designate separate namespaces for Kubernetes Pods that access sensitive data and define Kubernetes policies to make them inaccessible from other namespaces. Segment the roles used for operations and enforce namespace boundaries.
  * Enforce token exchange to prevent the exfiltration of long-lived, highly privileged tokens.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
