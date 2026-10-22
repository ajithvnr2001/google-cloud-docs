---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/encryption-in-transit/
title: Encryption in transit \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:44.269128+00:00
---

# Encryption in transit  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/encryption-in-transit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Encryption in transit Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** To access the URLs listed on this page, you must connect to the internet. The URLs are provided to access outside of your air-gapped environment.

This document provides details on Google Distributed Cloud (GDC) air-gapped encryption transit.

## CIO-level summary

  * GDC employs several security measures to help ensure the authenticity, integrity, and confidentiality of data in transit.
  * Depending on the connection that is being made, GDC applies default protections to data in transit for GDC components. For example, we secure communications between the user and the GDC Cloud Service Mesh Ingress Gateway using TLS.



## Introduction

Security is often a deciding factor when choosing a cloud provider. At Google, security is of the utmost importance. We work tirelessly to protect your data — whether it is traveling over your network, moving within Google's infrastructure, or storing on our servers.

Central to Google's security strategy are authentication, integrity, and encryption, for both data at rest and in transit. This paper describes our approach to encryption in transit for Google Distributed Cloud air-gapped (GDC).

For data at rest, see [Encryption at Rest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/encryption-at-rest). For an overview across all of Google Security, see [Google Infrastructure Security Design Overview](https://cloud.google.com/docs/security/infrastructure/design).

**Audience:** this document is aimed at CISOs and security operations teams using or considering GDC.

**Prerequisites:** in addition to this introduction, we assume a basic understanding of [encryption](https://en.wikipedia.org/wiki/Encryption) and [cryptographic primitives](https://en.wikipedia.org/wiki/Cryptographic_primitive).

## Authentication, integrity, and encryption

GDC employs several security measures to help ensure the authenticity, integrity, and confidentiality of data in transit.

  * **Authentication:** we authenticate the destination of the data on the network layer. The source is authenticated by GDC-managed AIS.
  * **Integrity:** we make sure data you send arrives at its destination unaltered, that is protected from unauthorized changes.
  * **Encryption:** we make your data unreadable while in transit to keep it confidential. Encryption is the process through which legible data (plaintext) is made illegible (ciphertext) with the goal of ensuring the plaintext is only accessible by parties authorized by the owner of the data. The algorithms used in the encryption process are public, but the key required for decrypting the ciphertext is private. Encryption in transit often uses asymmetric key exchange, such as elliptic-curve-based Diffie-Hellman, to establish a shared symmetric key that is used for data encryption. For more information on encryption, see [Introduction to Modern Cryptography](https://www.cs.umd.edu/%7Ejkatz/imc.html).



Encryption can be used to protect data in multiple states:

  * **Encryption at rest** protects your data from a system compromise or data exfiltration by encrypting data while stored. The Advanced Encryption Standard (AES) is often used to encrypt data at rest.
  * **Encryption in transit:** protects your data if communications are intercepted while data moves between your site and the cloud provider or between two services. This protection is achieved by encrypting the data before transmission; authenticating the endpoints; and, on arrival, decrypting and verifying that the data was not modified. For example, transport layer security (TLS) is often used to encrypt data in transit for transport security, and Secure/Multipurpose Internet Mail Extensions (S/MIME) is used often for email message encryption.



Encryption is one component of a broader security strategy. Encryption in transit defends your data, after a connection is established and authenticated, against potential attackers by:

  * Removing the need to trust the lower layers of the network which are commonly provided by third parties
  * Reducing the potential attack surface
  * Preventing attackers from accessing data if communications are intercepted



With adequate authentication, integrity, and encryption, data that travels between users, devices, or processes can be protected in a hostile environment. The remainder of this paper explains GDC approach to the encryption of data in transit and where it is applied.

## GDC network infrastructure

### Physical boundaries

A physical boundary is the barrier to a physical space that is controlled by or in coordination with Google, where we can ensure that rigorous security measures are in place. Physical access to these locations is restricted, heavily monitored and audited. Only a small set of approved personnel have access to hardware. Data in transit within these physical boundaries is generally authenticated and encrypted.

For communication that crosses in or out of the physical boundary of GDC, we employ strong authentication and encryption to protect data in transit.

### How traffic gets routed

To understand how encryption in transit works in GDC, it is necessary to explain how traffic gets routed to and through GDC. This section describes how requests get from an end user to the appropriate GDC service or customer application, and how traffic is routed between cross-site services.

A **GDC-managed service** is a modular private cloud service. These services include compute, storage, and machine learning. For example, GDC object storage is a GDC-managed service. A **customer application** is an application hosted on GDC that you, as a GDC customer, can build and deploy using GDC services. Customer applications or partner solutions that are hosted on GDC are not considered GDC-managed services. For example, an application you build using GDC VMs, Database Service, and Vertex AI is a customer application.

Figure 1 shows different kinds of routing requests. Figure 1 shows interactions between the various network components, and the security in place for each connection.

![Inter-site connectivity backbone infrastructure](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/intersite-infra.png)_Figure 1: Inter-site connectivity infrastructure_

#### End user (customer network) to GDC API and managed service

For managed services hosted on Cloud Service Mesh Ingress Gateways, they accept requests from the customer network using Cloud Service Mesh Ingress Gateway. Cloud Service Mesh Ingress Gateway proxies traffic for incoming HTTP(S), and routes and load balances traffic to the GDC-managed services themselves. Another firewall layer provides DDoS attack countermeasures with intrusion detection and prevention. This connection is authenticated and encrypted from Cloud Service Mesh Ingress Gateway to the frontend of the GDC-managed service. Figure 1 shows this interaction as connection A.

Most GDC APIs and managed services are hosted on Cloud Service Mesh Ingress Gateways. However, some services are hosted directly on GDC-managed Layer 4 load balancer. For example, DBS databases are hosted on a GDC external load balancer. These services are configured to authenticate and encrypt connections at the application layer using TLS. Figure 1 shows this interaction as connection B.

#### End user (customer network) to a customer application hosted on GDC

There are several ways to route traffic from the customer network to a customer application hosted on GDC. The way that your traffic is routed depends on your configuration.

##### Expose customer applications through customer API Gateway

GDC supports exposing customer applications through the customer API Gateway. The customer API Gateway service empowers users to develop, deploy, secure, manage, and scale the API as needed. Figure 1 shows this interaction as connection C.

##### Expose containerized customer workloads through customer external load balancer

GDC supports exposing containerized workloads that are managed by the customer through an external load balancer. GDC provides the ability to configure ingress and egress policies to the corresponding personnel. Figure 1 shows this interaction as connection E.

##### Expose virtual machine workloads

GDC supports exposing customer created Virtual Machines to end users. GDC provides an ability to configure ingress and egress policies to the corresponding personnel. Figure 1 shows this interaction as connection F.

#### GDC cross-site interconnect service

Routing from one managed service to another usually occurs entirely within the physical boundary of GDC. In some cases, like cross-site backup, data is routed outside of the physical boundary of GDC. In that case, data is encrypted both at the application layer, for example, TLS, and can also be encrypted at the network layer. Figure 1 shows this interaction as connection G.

#### Virtual machine to virtual machine

VM-to-VM connections within GDC are not encrypted at the network level. Customers are responsible for encrypting data by using appropriate encrypted protocols or specific technologies like IPSecs tunnels.

## Encryption in transit by default

GDC uses various methods of encryption, both default and user configurable, for data in transit. The type of encryption used depends on the OSI layer, the type of service, and the physical component of the infrastructure. This section describes the default protections that Google uses to protect data in transit.

The remainder of this section describes the default protections that Google uses to protect data in transit.

### User to Cloud Service Mesh Ingress Gateway encryption

Today, many systems use HTTPS to communicate over the Internet. HTTPS provides security by using a TLS connection, which ensures the authenticity, integrity, and confidentiality of requests and responses. To accept HTTPS requests, the receiver requires a public–private key pair and an X.509 certificate for server authentication from a Certificate Authority (CA). The key pair and certificate help authenticate a user's requests at the application layer (layer 7) by proving that the receiver owns the domain name for which requests are intended. The following subsections discuss the components of user to Cloud Service Mesh Ingress Gateway encryption, namely: TLS, BoringSSL, and GDC Configurable Certificate Authority.

### Transport layer security (TLS)

When you send a request to a GDC service, we secure the data in transit; providing authentication, integrity, and encryption, using HTTPS with a certificate from a trusted certificate authority. Any data the user sends to the Cloud Service Mesh Ingress Gateway for the GDC-managed service is encrypted in transit with transport layer security (TLS). Cloud Service Mesh Ingress Gateway negotiates a particular encryption protocol with the client depending on what the client can support. GDC Cloud Service Mesh Ingress Gateway enforces only FIPS approved algorithms to provide stronger security.

#### BoringSSL

[BoringSSL](https://boringssl.googlesource.com/boringssl) is a Google-maintained, open source implementation of the TLS protocol, forked from OpenSSL, that is mostly interface-compatible with OpenSSL. [Google forked BoringSSL from OpenSSL](https://www.imperialviolet.org/2015/10/17/boringssl.html) to simplify OpenSSL, both for internal use and to better support the Chromium and Android Open Source Projects. BoringCrypto, the core of BoringSSL, has been validated to FIPS 140-2 level 1.

TLS in the Cloud Service Mesh Ingress Gateway is implemented with BoringSSL. Table 1 shows the encryption protocols that GDC supports when communicating with clients.

Protocols | Authentication | Key exchange | Encryption | Hash Functions  
---|---|---|---|---  
TLS 1.3 | RSA 2048 | Curve25519 | AES-128-GCM | SHA384  
TLS 1.2 | ECDSA P-256 | P-256 (NIST secp256r1) | AES-256-GCM | SHA256  
  
_Table 1: Encryption Implemented in the Cloud Service Mesh Ingress Gateway for GDC Services and Implemented in the BoringSSL Cryptographic Library_

#### GDC configurable Certificate Authority

As part of TLS, a server must prove its identity to the user when it receives a connection request. This identity verification is achieved in the TLS protocol by having the server present a certificate containing its claimed identity. The certificate contains both the server's DNS hostname and its public key. Once presented, the certificate is signed by an issuing Certificate Authority (CA) that is trusted by the user requesting the connection. As a result, users who request connections to the server only need to trust the root CA. If the server wants to be accessed ubiquitously, the root CA needs to be known to any prospective client device. Client browsers and devices are configured with a set of root CAs that they trust, based on the environment that client is operating in.

The root CA for GDC is dependent on the environment in which it is deployed, and the requirements of customers in that environment.

#### Cloud Service Mesh Ingress Gateway to application front ends

Two cases:

  * Cloud Service Mesh Ingress Gateway terminates TLS, re-encrypts mTLS using Cloud Service Mesh Istio certs 
    * mTLS from Ingress Gateway to Istio Sidecar Application Frontend
  * Cloud Service Mesh Ingress Gateway terminates TLS, re-encrypts TLS to some other server, with configured CA.



#### Network encryption of storage traffic

In GDC file and block storage system, traffic is routed between the application using the storage and the storage service. That data is authenticated and encrypted in transit using IPSec. Client-side encryption for the storage traffic is available soon. IPSec transport mode is used between file and block traffic to the host that needs to access storage. Authentication is done by a pre-shared key which is generated on the flight and securely stored in GDC. Once IPSec SAs is established, information is exchanged using the IPSec tunnel. Packets are encrypted and decrypted using the FIPS compliant encryption crypto specified in the IPSec SA.

#### Service-to-service authentication, integrity, and encryption

Within GDC infrastructure, at the application layer (layer 7), we use mTLS or TLS for the authentication, integrity, and encryption of RPC calls from the Cloud Service Mesh Ingress Gateway to a service and from one GDC service to another GDC service. Each service that runs in GDC runs as a service account identity with associated cryptographic credentials. When communicating over mTLS through Cloud Service Mesh, GDC services use client certificates to authenticate to other services. Cloud Service Mesh verifies these certificates using an internal certificate authority. When communicating over TLS, for example, to a GDC Kubernetes API Server, GDC services use Kubernetes service account tokens to authenticate to services. Kubernetes service account tokens are verified using the public keys of the Kubernetes API Server token issuer. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
