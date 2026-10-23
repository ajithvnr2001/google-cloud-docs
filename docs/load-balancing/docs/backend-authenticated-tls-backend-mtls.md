---
url: https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls/
title: Backend authenticated TLS and backend mTLS overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:57.691814+00:00
---

# Backend authenticated TLS and backend mTLS overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Backend authenticated TLS and backend mTLS overview Stay organized with collections  Save and categorize content based on your preferences. 

When a load balancer connects to backends that are within Google Cloud, the load balancer accepts any certificate that your backends present. In such cases, the load balancer doesn't perform any certificate validation.

With _backend authenticated TLS_ or backend authentication, the load balancer can verify the identity of the backends that it connects to. And with _backend mTLS_ , the load balancer can additionally prove its identity to backends by using a client TLS certificate.

The following diagram shows the difference between frontend and backend mTLS, focusing on the role of the load balancer in each case. In frontend mTLS, the load balancer acts as the _server_ , verifying the client's identity. In backend mTLS, the load balancer acts as the _client_ , proving its identity to the backend.

[ ![Frontend and backend mTLS.](https://docs.cloud.google.com/static/load-balancing/images/mTLS_frontend_backend.svg)](https://docs.cloud.google.com/static/load-balancing/images/mTLS_frontend_backend.svg) Frontend and backend mTLs (click to enlarge).

mTLS operates independently on the frontend and the backend. You can configure mTLS on either the frontend, the backend, or both the frontend and the backend.

This document provides an overview of backend authenticated TLS along with backend mTLS. To learn more about frontend mTLS, see [Mutual TLS overview](https://docs.cloud.google.com/load-balancing/docs/mtls).

Backend authenticated TLS and backend mTLS can be configured on the backend service resource of the following load balancers:

  * Global external Application Load Balancers
  * Regional external Application Load Balancers
  * Regional internal Application Load Balancers
  * Cross-region internal Application Load Balancers



## Features

mTLS uses public key infrastructure (PKI) to authenticate the identity of the entities communicating over the network. The infrastructure includes three components: a client, a server, and a certificate authority (CA). Backend authenticated TLS and backend mTLS add the following capabilities to Application Load Balancers:

  * The load balancer can validate certificates presented by backends against your own trust anchors. You can upload multiple trust anchors to enable seamless migration from an earlier PKI to a new one without downtime.

  * The load balancer can validate TLS certificates of backends against public roots of trust (web PKI).

  * You can configure intermediate certificates in addition to your trust anchors to help construct the backend certificate validation path. The use of intermediate certificates means that your backend servers don't need to provide the complete certificate chain.

  * You can configure a TLS Server Name Indication (SNI) hostname for your backend service. During the TLS handshake, the load balancer includes this SNI hostname in the `ClientHello` message that it sends to the backend. The backend then responds with its TLS certificate, and the load balancer verifies that at least one of this certificate's Subject Alternative Name (SAN) fields matches the hostname or any of the SAN fields configured for the backend service.

  * You can configure your load balancer's backend service to use mTLS so that the load balancer can prove its identity to the backends. This authentication is carried out using a client (load balancer) certificate that the load balancer presents to the backend.




## Certificate requirements

When configuring certificates, ensure that they comply with these requirements:

  * Modern cryptography tools form the basis of mTLS authentication. Certificates must use either RSA or ECDSA algorithms for key exchange. Hashing algorithms must use SHA-256 or a stronger cryptographic hash function. Hashing algorithms such as MD4, MD5, and SHA-1 aren't supported.

  * Leaf server certificates that are provided by the backend have the following requirements:

    * The [basic constraints](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.9) extension _must not_ contain `CA=true`.
    * The [extended key usage](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12) extension _must_ contain `serverAuth`.
    * The [extended key usage](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12) extension _must not_ contain the `codeSigning`, `timeStamping`, or `OCSPSigning` fields.
    * The certificate _must not_ be expired.
  * For leaf client (load balancer) certificates used in backend mTLS, the certificate must be a [Certificate Manager certificate resource](https://docs.cloud.google.com/certificate-manager/docs/overview). The scope of this certificate must be `client-auth`, which indicates that this certificate is used as a client certificate in backend mTLS. 

    * The [basic constraints](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.9) extension _must not_ contain `CA=true`.
    * The [extended key usage](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12) extension _must_ contain `clientAuth`.
    * The [extended key usage](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12) extension _must not_ contain the `codeSigning`, `timeStamping`, or `OCSPSigning` fields.
    * The certificate _must not_ be expired.
  * To authenticate the server certificates that your backend presents to the load balancer, the root and intermediate certificates that are located in the trust config must meet the following requirements:

    * The [basic constraints](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.9) extension _must_ contain `CA=true`.
    * The [key usage](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.3) extension _must be_ set to `keyCertSign`.
    * The [extended key usage](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12) extension _must contain_ the `serverAuth` field.
    * The certificate _must not_ be expired.



## Key components of backend authenticated TLS and backend mTLS

With _backend authenticated TLS_ , the load balancer can verify the identity of the backends that it connects to. You can configure backend authenticated TLS on an HTTP(S) load balancer that uses either HTTPS or HTTP/2 as its backend service protocol. If you don't configure backend authenticated TLS, the load balancer accepts any certificate from the backend. Using _backend mTLS_ , you can additionally configure the load balancer to present its own client certificate to the backend, which the backend can use to authenticate the load balancer.

To configure backend authenticated TLS, you need to do the following:

  * Create a trust config resource.
  * Create a backend authentication config resource.
  * Update the TLS setting attribute on the backend service, pointing it to the backend authentication config resource.



To configure _backend mTLS_ , you must create a client certificate and attach the client certificate to the backend authentication config resource. You cannot attach the client certificate after the backend authentication config resource has been created.

The following diagram shows the different components, attached to the backend service of an Application Load Balancer, that enable backend authenticated TLS and backend mTLS.

[ ![Backend authenticated TLS and backend mTLS components.](https://docs.cloud.google.com/static/load-balancing/images/setup_overview_backend_authenticated_TLS_backend_mTLS.svg)](https://docs.cloud.google.com/static/load-balancing/images/setup_overview_backend_authenticated_TLS_backend_mTLS.svg) Backend authenticated TLS and backend mTLS components (click to enlarge).

The information that follows provides an overview of these different components used to configure backend authenticated TLS and backend mTLS.

### Trust config

To authenticate the server certificates that your backend presents to the load balancer, the load balancer needs to be configured with X.509 certificates that establish a chain of trust to the issuer of the backend's certificate. You configure the trust config by using a [`TrustConfig` resource](https://docs.cloud.google.com/certificate-manager/docs/core-components#trust-configs), which expresses the entire trust config and contains a single trust store.

A trust store encapsulates a trust anchor (root certificate) and, optionally, one or more intermediate certificates. A trust anchor is a certificate representing a root of trust. A valid server certificate must show a chain of trust back to some trust anchor in the trust store.

An intermediate certificate is a certificate that is part of a chain of trust leading back to a trust anchor in the trust store. It is used, along with any additional intermediate CAs included with the leaf certificate, to build the trust chain during the validation process. Creating an intermediate certificate is optional.

If you need to use a certificate that is self-signed, expired, doesn't chain to a specified root of trust, or has failed validation, you can add such a certificate to an allowlist in the trust config. Creating a self-signed certificate that can be added to an allowlist is also optional.

The trust store doesn't contain any private keys because only the certificates are necessary to verify a chain of trust.

### Backend authentication config resource

The backend authentication config ([`BackendAuthenticationConfig` resource](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.backendAuthenticationConfigs)) is attached to the backend service of the load balancer and performs the following functions:

  * Enables backend authenticated TLS (backend authentication) by using the trust config and the public roots of trust
  * Additionally enables backend mTLS by using the client certificate



To enable backend authenticated TLS and backend mTLS, the backend authentication config resource points to the following resources:

  * **Trust config** ([`trustConfig`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.backendAuthenticationConfigs#BackendAuthenticationConfig.FIELDS.trust_config)): the attached trust config used to validate the server certificate provided by the backend. The trust config isn't required when the backend authentication config uses the public roots of trust to validate the server certificate.

  * **Public roots of trust** ([`wellKnownRoots`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.backendAuthenticationConfigs#BackendAuthenticationConfig.FIELDS.well_known_roots)): indicates whether the load balancer trusts backend server certificates that are issued by public CAs, in addition to certificates trusted by the trust config. To learn more, see Use public roots of trust.

  * **Client certificate** ([`clientCertificate`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.backendAuthenticationConfigs#BackendAuthenticationConfig.FIELDS.client_certificate)): the client certificate that the load balancer uses to express its identity to the backend, if the connection to the backend uses mTLS. For backend authenticated TLS (backend authentication), this field can be empty, in which case the load balancer only authenticates the backend, but not itself, to the backend.


**Note:** It is not possible to send a client certificate to the backend without configuring backend authenticated TLS first. This is because the load balancer cannot present its certificate to the backend without first validating the certificate presented by the backend.

### Backend service

Within the backend service, the `tlsSettings` attribute points to the following resources in order to validate the backend certificate.

  * Backend authentication config (`authenticationConfig`)
  * SNI hostname (`sni`)
  * Accepted SANs (`subjectAltNames`)

**Note:** Configuring the SNI hostname and accepted SANs on the backend service in order to verify the backend certificate is optional. However, you _cannot_ validate the backend certificate without configuring the backend authentication config resource on the backend service. In other words, the backend certificate must be validated through a trusted certificate chain, which is expressed by using a trust config.

The SNI (`sni`) and SAN (`subjectAltNames`) fields in the `tlsSettings` attribute control how the load balancer validates the backend's certificate based on the certificate's SAN values. These fields influence the validation process regardless of whether backend authenticated TLS is configured.

When the SNI field is set (`tlsSettings.sni`), the load balancer does the following:

  * Sends the SNI hostname to the backend server during the TLS handshake.
  * Verifies that the backend's TLS certificate includes a SAN that matches the SNI hostname.



By default, the load balancer checks that the backend's TLS certificate includes a SAN that matches the SNI hostname. However, if SANs are configured on the backend service (`tlsSettings.subjectAltNames`), the load balancer does the following:

  * Ignores the SNI hostname for SAN verification.
  * Verifies that the backend's TLS certificate includes a SAN that matches one of the accepted SANs (`subjectAltNames`) configured on the backend service.



### Client certificate

In addition to backend authenticated TLS (backend authentication), you can configure a load balancer's backend service to use mTLS, so that the load balancer can prove its identity to the backend. This authentication uses a client (load balancer) certificate that the load balancer presents to the backend.

To configure backend mTLS, you need to do the following:

  * Create a client certificate resource containing the client (load balancer) certificate and its private key.
  * Attach the client certificate to the backend authentication config resource.



Public PKI managed certificates aren't supported, and all client certificates must have a `client-auth` scope and comply with certificate requirements.

If the backend requests a client certificate, it must be configured to accept the client certificate. If the backend refuses the load balancer's connection, the load balancer returns an HTTP `502` status code for requests that it's proxying and logs a generic status to Cloud Logging.

## Configure backend authenticated TLS and backend mTLS on the load balancer

You can configure backend authenticated TLS and backend mTLS on the load balancer using either a private PKI or public roots of trust.

### Use private PKI

The following is a high-level overview of the key steps that you need to follow to configure backend authenticated TLS and backend mTLS on your load balancer using certificates issued from your private PKI. Private PKI has the advantage of being fully under your control and isolated from the public internet's PKI systems.

  1. Create a trust config resource comprising the trust anchor (root certificate) and intermediate certificates that serve as roots of trust.

  2. To configure backend mTLS, create a client certificate containing the client (load balancer) certificate and its private key.

  3. Create a backend authentication config resource that references the trust config. If you want to configure backend mTLS, the backend authentication config resource references both the trust config and the client certificate.

  4. Attach the backend authentication config resource to the backend service of the load balancer.




Note the following:

  * It is not possible to send a client certificate to the backend without configuring backend authenticated TLS first.

  * If you want to enable backend mTLS, you must create the client certificate before you configure the backend authentication config resource.




To learn more about this setup in detail, see the following guides:

  * [Set up backend authenticated TLS](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-setup)

  * [Set up backend mTLS](https://docs.cloud.google.com/load-balancing/docs/backend-mtls-setup)




### Use public roots of trust

In addition to using certificates issued from your private PKI to enable backend authenticated TLS, you can also use public roots of trust to validate the backend certificate.

To use public roots of trust, you don't need to create a trust config and attach it to the backend authentication config resource. Instead, you need to set `PUBLIC_ROOTS` as a value in the `wellKnownRoots` field of the backend authentication config resource. Having said that, you can also create a trust config that explicitly includes the roots of your publicly issued certificates, in addition to certificates trusted by the trust config.

The `PUBLIC_ROOTS` setting uses a set of root CAs, similar to the set of root CAs trusted by browsers, that is managed by Google and can change over time. This presents a risk of your backend certificates becoming invalid when these roots change. If you need to validate publicly issued certificates, consider choosing a well-established and trustworthy CA and one that uses intermediate cross-signing for issuing your backend certificates to mitigate the risk of a root certificate expiring or being revoked.

### Use managed workload identity

You can achieve mTLS by using [managed workload identities](https://docs.cloud.google.com/load-balancing/docs/about-managed-workload-identities).

When you use a managed workload identity, the managed workload identity creates the following resources automatically:

  * Certificate Manager trust config
  * Certificate Manager managed identity certificate
  * Backend authentication config



To learn more, see [Backend mTLS with managed workload identity overview](https://docs.cloud.google.com/load-balancing/docs/managed-workload-identities-load-balancers-overview).

## Server certificate validation steps

When validating the server certificate during backend authenticated TLS, or backend authentication, the load balancer does the following: 

  1. **Verify that the server possesses the certificate's private key**.

The server proves possession of the private key associated with the certificate it presents to the load balancer by signing a piece of information using its private key and sending it to the load balancer as a part of the `CertificateVerify` message. The load balancer then verifies this signature using the public key from the server's certificate. If the signature verification fails, it indicates that the backend server doesn't possess the private key corresponding to the certificate. In such cases, the load balancer terminates the TLS handshake without logging any errors.

  2. **Verify the chain of trust**.

If the trust config includes at least one trust anchor or has the `wellKnownRoots` attribute set to `PUBLIC_ROOTS`, the load balancer attempts to verify a chain of trust between the server certificate and the configured trust anchor. 

The verification checks include the following:

     * The backend's server certificate, intermediate certificates (if provided), and the configured root certificate comply with the certificate requirements.
     * For all the certificates in the chain of trust, the subject field in the parent certificate matches the issuer field in the child certificate. This verification helps to ensure that the parent certificate's identity (subject) is the same as the identity listed as the issuer in the child certificate.
     * For all the certificates in the chain of trust, the subject key identifier (SKID) of the parent certificate matches the authority key identifier (AKID) in the child certificate. This match confirms that the child certificate was issued by the correct root authority and that it can be trusted because the root's public key is being referenced in the AKID for verifying the certificate's validity.
**Note:** Self-signed client certificates fail to form a valid chain of trust and are always rejected.
  3. **Establish a connection with the backend**.

If certificate validation succeeds, the load balancer proceeds with the connection to the backend.

However, if the certificate validation fails, the load balancer terminates the connection to the backend, sends an HTTP `502` status code to the client, and logs the termination reason to Cloud Logging. In the event of a certificate validation error, subsequent incoming requests trigger the load balancer to reinitiate the backend connection.

The backend connection can also fail if the backend server refuses the connection. With _backend mTLS_ , this can happen because it finds the client certificate to be invalid. When the connection to the backend fails, the load balancer responds to proxied requests with an HTTP `502` status code and logs a generic error reason to Cloud Logging.




### Error handling and logging

Application Load Balancers provide detailed logging capabilities that allow you to monitor server certificate validation, identify potential issues, and troubleshoot connection problems. This section outlines the different types of errors that can occur during mTLS validation and how they are logged.

If the server certificate validation fails, the connection is terminated and the errors are logged to Cloud Logging. These errors are described in the following table.

Server certificate status | Logged error  
---|---  
The server certificate chain is too long (more than 10 intermediate certificates included with the server certificate).  |  `server_cert_chain_exceeded_limit`  
A server or an intermediate certificate has an invalid RSA key size. No validation is performed. RSA keys can range from 2048 to 4096 bits. |  `server_cert_invalid_rsa_key_size`  
A server or an intermediate certificate is using an unsupported elliptic curve. No validation is performed. Valid curves are P-256 and P-384. |  `server_cert_unsupported_elliptic_curve_key`  
A server or an intermediate certificate is using a non-RSA or non-ECDSA algorithm. No validation is performed. |  `server_cert_unsupported_key_algorithm`  
The PKI to be used for validation has more than ten intermediate certificates that share the same Subject and Subject Public Key Info. No validation is performed. |  `server_cert_pki_too_large`  
An intermediate certificate provided for validation had more than 10 name constraints. |  `server_cert_chain_max_name_constraints_exceeded`  
The server certificate has an [`Extended Key Usage (EKU)`](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12) extension field but that field doesn't include `serverAuth`. | `server_cert_chain_invalid_eku`  
The time limit is exceeded while attempting to validate the certificate chain.  |  `server_cert_validation_timed_out`  
The depth or iteration limit is reached while attempting to validate the certificate chain. The maximum depth for a certificate chain is ten, including the root and server certificates. The maximum number of iterations is 100 (certificates examined to validate the server certificate chain). | `server_cert_validation_search_limit_exceeded`  
You configured mTLS without setting up a `TrustConfig` resource. |  `server_cert_validation_not_performed`  
The server did not provide the requested certificate during the handshake. |  `server_cert_not_provided`  
The server certificate failed verification with the `TrustConfig` resource. |  `ssl_certificate_verification_failed`  
Service is unable to perform certificate chain validation. |  `server_cert_validation_unavailable`  
Internal error validating certificate chain.  |  `server_cert_validation_internal_error`  
Matching `TrustConfig` not found. |  `server_cert_trust_config_not_found`  
The server certificate payload (including any intermediate certificates) is too large (more than 16 KB).  |  `server_cert_exceeded_size_limit`  
  
## Limitations

  * Backend authenticated TLS and backend mTLS isn't supported on classic Application Load Balancers.

  * Backend authenticated TLS and backend mTLS isn't supported for the following backend types:

    * Global internet NEG backends

    * App Engine backends

  * Health checks don't support TLS authentication or mTLS capabilities. Health check probers can't present client certificates, nor do they validate server certificates against trust configs. If your backends require client certificates for HTTPS traffic, ensure that health check probes can succeed without mTLS—for example, by using TCP health checks or by configuring a dedicated health check endpoint or port that doesn't require client authentication.

  * The load balancer doesn't pass the client's SNI hostname from the frontend TLS connection when connecting to a backend. However, backends can access the client's SNI hostname using a [custom request header](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers).

  * For backend mTLS, the client certificate keys are restricted to the following:

    * RSA keys can range from 2048 to 4096 bits.
    * ECDSA keys can use the P-256 or P-384 curves.
  * Backend authenticated TLS doesn't support certificate revocation checks.




## Quotas and limits

  * A single trust store can hold up to 200 trust anchors and intermediate certificates combined, with a separate limit of 100 for intermediate certificates. No more than three intermediate certificates can share the same Subject and Subject Public Key information.

  * The maximum depth of a certificate chain is 10 certificates, including the root and leaf certificates. The maximum number of intermediate certificates that can be evaluated while attempting to build the chain of trust is 100.

  * Backend authenticated TLS limits the certificate chain received from the backend to no more than 16 KB and 10 certificates.

  * Root certificates used for validation cannot contain more than 10 name constraints.

  * The maximum number of subject alternative names allowed in the `tlsSettings.subjectAltNames[]` field is 5.




## What's next

  * [Set up backend authenticated TLS using self-managed certificates](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
