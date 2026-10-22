---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/keyfactor-ejbca-architecture/
title: Keyfactor EJBCA reference architecture \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:13.139222+00:00
---

# Keyfactor EJBCA reference architecture  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/keyfactor-ejbca-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Keyfactor EJBCA reference architecture Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This reference architecture defines the conceptual design for integrating [Keyfactor EJBCA Enterprise](https://www.keyfactor.com/products/ejbca-enterprise/) as a third-party Certificate Authority (CA) on Google Distributed Cloud (GDC) air-gapped.

Keyfactor EJBCA Enterprise is a highly scalable, robust, and FIPS-compliant Certificate Authority platform that enables organizations to manage public key infrastructure (PKI) across heterogeneous environments.

GDC air-gapped includes a [native Certificate Authority service](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/cas-overview) for automated key and certificate management inside the hosted cloud boundary. The native CA service is the recommended solution for most customers, providing fully managed, seamless PKI capabilities within the platform. However, organizations that have standardized their PKI infrastructure on Keyfactor EJBCA for existing workloads outside of GDC may prefer to leverage the same consistent CA architecture and management policies for workloads running within their GDC environments.

### Features and capabilities

The solution provides several core functional components for certificate lifecycle management:

  * **Automated Certificate Lifecycle Management** : Leverage the custom EJBCA issuer inside GDC standard clusters to automate the provisioning, renewal, and revocation of server certificates via cert-manager.
  * **Standardized ACME Automation** : Support for the Automatic Certificate Management Environment (ACME) protocol using DNS-01 challenges, allowing platform services to request and renew certificates seamlessly.
  * **Secure HSM Integration** : Direct cryptographic protection of all CA private keys inside a CC EAL4+ certified Hardware Security Module (HSM), ensuring key material never leaves the physical security boundary. Keyfactor EJBCA Enterprise may either use its own managed HSM or connect to an external HSM.
  * **Air-Gapped Compatibility** : Specialized workflows for mirroring the EJBCA cert-manager issuer image from public registries to the GDC private Harbor registry, ensuring offline availability.
  * **Egress Traffic Isolation** : Outbound network configuration using GDC Subnet and CloudNATGateway resources to restrict GDC API traffic directly to the external EJBCA server IP address.



### Architectural principles

  * **Shared Responsibility Model** : The customer operates the external EJBCA server and HSM, owning the physical PKI infrastructure and CA root keys, while GDC provides the compute, internal DNS, and automated client layers inside the standard cluster.
  * **Security-Focused Design** : Adheres to air-gapped security requirements by utilizing local container image mirrors and enforcing strict egress gating to minimize the network attack surface.
  * **Protocol Standardization** : Prioritizes standard protocols (ACME and mTLS REST) for CA interaction, avoiding proprietary API dependencies and allowing flexible client integrations.



## Architecture

The architecture follows the external Certificate Authority model, where the EJBCA server and its backing Hardware Security Module (HSM) are hosted externally outside the physical GDC boundaries but are network-accessible. The EJBCA server can be deployed externally either as a hardware or software appliance. The core integration described in this guide only requires that the external EJBCA server is reachable via a stable IP address.

![Keyfactor EJBCA architecture diagram.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/ejbca-diagram.png)

Key components of this architecture include:

  * **EJBCA Enterprise Server** : Deployed externally either as a Keyfactor hardware appliance or software appliance, housing the CAs (Root and Subordinate) and generating all CA key material inside a CC EAL4+ certified HSM.
  * **Default VPC** : VPC where user workloads are deployed, either in standard Kubernetes clusters or in virtual machines.
  * **GDC Internal DNS** : Manages local private DNS zones (using the private domain name configured in the environment variables) used for resolving ACME DNS-01 challenges.
  * **GDC Egress NAT Gateway** : Directs outbound traffic from cluster pods to the external EJBCA server IP address.
  * **Harbor Private Registry** : Hosts mirrored container images (such as the EJBCA cert-manager issuer) for air-gapped deployment.



## Concepts and technologies

This section details the functional components, their responsibilities, and how they communicate within the system.

### Infrastructure and platform

  * **GDC Standard Cluster** : The primary compute environment where the EJBCA issuer and cert-manager pods reside, executing certificate automation for workloads.
  * **Harbor Registry** : The secure, local source of truth for all container images in GDC. It provides automated scanning to ensure images are free from known vulnerabilities before deployment.
  * **GDC Egress Gateway** : Platform-native networking resources (Subnet and CloudNATGateway) that govern and secure outbound API traffic from cluster pods to the external CA server.



### Services and logic

  * **EJBCA Enterprise Server** : The external CA engine (software or hardware appliance) responsible for managing CA hierarchies (Root and Subordinate), validating certificate requests, signing certificates, and logging audit records.
  * **Hardware Security Module (HSM)** : The CC EAL4+ compliant cryptographic module that handles key generation and certificate signing, guaranteeing that CA private keys are never exposed.
  * **GDC Internal DNS** : Manages private DNS zones (`ManagedDNSZone` and `ResourceRecordSet`) used by the ACME challenge validating service to verify domain ownership via temporary TXT records.
  * **cert-manager with EJBCA Issuer** : The Kubernetes-native certificate controller that intercepts Certificate requests and leverages the EJBCA issuer to translate them into secure EJBCA API calls.



### Data flow and interfaces

  * **ACME Protocol** : The standard API interface for automated, domain-validated server certificate issuance using the DNS-01 challenge.
  * **EJBCA REST API** : The RESTful interface used for administrative bootstrapping and programmatic operations (such as CSR signing and revocation).
  * **mTLS Client Authentication** : The primary authentication mechanism for the cert-manager integration, verifying client identity via mutual TLS using dedicated client certificates.



## Considerations

  * **Scalability and performance** : 
    * The external EJBCA server must be scaled (CPU, memory, HSM capacity) to handle concurrent validation and signing requests, particularly during burst issuance profiles.
    * GDC egress gateway resources must be sized to ensure minimal latency to the external CA server, preventing timeouts during cert-manager validation cycles.
  * **Security and compliance** : 
    * Isolating the CA root keys within an external HSM meets high security and compliance standards (such as BSI VS-NfD).
    * Administrative access to EJBCA should be strictly bounded using role-based access controls (RBAC) and mapped to unique client certificate serial numbers.
  * **Availability and reliability** : 
    * High-availability deployment of the external EJBCA server across multiple availability zones (using an active-passive or clustered configuration) is recommended to ensure continuous operation and avoid a single point of failure.
    * Deploying multiple cert-manager controller replicas inside GDC ensures that the cluster-side automated certificate issuance remains resilient.
  * **Operational management** : 
    * The customer retains ownership of the EJBCA server, including system patching, HSM key rotation, and CRL publishing.
    * The customer's GDC platform administrators are responsible for maintaining the in-cluster cert-manager and EJBCA issuer controller and managing GDC-side private DNS records.



## Design decision

The primary architectural choices for this solution focus on balancing automation with the constraints of the air-gapped environment.

### EJBCA integration option

GDC's native Certificate Authority service is the recommended PKI solution for most customers, providing fully managed, seamless PKI capabilities within GDC air-gapped environments. However, for organizations that have already standardized their PKI infrastructure on Keyfactor EJBCA for workloads outside of GDC, integrating their existing external CA server is offered as an opt-in option. This allows them to reuse established PKI templates, security policies, and operational models without redesigning their trust hierarchy or migrating core workflows.

### ACME challenge validation options

Both HTTP-01 and DNS-01 ACME challenge validation protocols are fully supported. While this architecture guide highlights the DNS-01 challenge using GDC's internal DNS (which is ideal for isolated, private environments that cannot support inbound public HTTP traffic), customers can select either validation method based on their specific network topology, security policies, and workload requirements.

### mTLS administrative channel recommendation

Using mutual TLS (mTLS) is recommended as a robust authentication method for cert-manager and integration clients. mTLS provides highly secure, cryptographic verification of client identity by leveraging client certificates, though the customer can choose to configure other authentication mechanisms supported by their EJBCA instance according to their corporate security policies.

## Assumptions and limitations

### Assumptions

  * The external EJBCA server is deployed, configured, and reachable via a stable IP address.
  * The EJBCA server is pre-configured with the necessary Root and Subordinate CAs, along with appropriate End Entity profiles.
  * A secure mechanism (such as a bastion node or offline transfer workflow) is available to publish the EJBCA issuer container image to the GDC Harbor registry.
  * Standard Kubernetes clusters inside GDC have cert-manager pre-installed or configured for operation.



### Limitations

  * **External HSM & EJBCA Maintenance**: The GDC control plane does not manage the external EJBCA server or its backing HSM; lifecycle operations (backups, upgrades, key rotations) are handled by the customer's PKI operations team.
  * **DNSSEC Validation Constraint** : Because private internal DNS is used, DNSSEC validation must be disabled server-side in the ACME configuration to avoid resolution failures for local private domains.
  * **Egress Connectivity Dependency** : The automated certificate issuance services are dependent on the availability and latency of the network link between the GDC rack and the external EJBCA server.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
