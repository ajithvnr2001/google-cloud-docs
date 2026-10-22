---
url: https://docs.cloud.google.com/load-balancing/docs/mtls/
title: Mutual TLS overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:59.935382+00:00
---

# Mutual TLS overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/mtls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Mutual TLS overview Stay organized with collections  Save and categorize content based on your preferences. 

Mutual TLS, or mTLS, is an industry standard protocol for mutual authentication between a client and a server. It ensures that both the client and server authenticate each other by verifying that each holds a valid certificate issued by a trusted certificate authority (CA). Unlike standard TLS, where only the server is authenticated, mTLS requires the client and server to present certificates, confirming the identities of both parties before communication is established.

mTLS is configured on the target HTTPS proxy resource of all the Application Load Balancers:

  * Global external Application Load Balancer
  * Classic Application Load Balancer
  * Regional external Application Load Balancer
  * Regional internal Application Load Balancer
  * Cross-region internal Application Load Balancer



mTLS uses Public Key Infrastructure (PKI) to authenticate the identity of the entities communicating over the network. The infrastructure includes three components: a client, a server, and a Certificate Authority (CA). mTLS for load balancers supports the following features:

  * Verify that the client presenting the certificate possesses its private key.

  * Validate client certificates in either of the two modes:

    * Reject invalid certificates: Enforces strict authentication by rejecting requests if the client certificate chain cannot be validated.

    * Allow invalid or missing certificates: Provides flexibility by passing all requests to the backend, even if a client certificate is missing or invalid.

  * Validate client certificates against an uploaded PKI anchor (root certificate), with the option to add multiple anchors separately to enable seamless migration from an old PKI to a new one without downtime.

  * Provide additional intermediate certificates to help construct the client certificate validation path against specified PKI anchors (root certificates). These intermediate certificates allow mTLS to work with clients that don't provide the complete certificate chain.

  * Generate and pass a fingerprint of the certificate to the backend as a custom request header.

  * Pass selected fields extracted from the certificate to the backend by using custom headers.

  * Pass the validation result and any validation errors to the backend by using custom headers.




## Certificate requirements

When configuring certificates for mTLS, ensure they comply with these requirements:

  * Modern cryptography tools form the basis of mTLS authentication. Certificates must use either RSA or ECDSA algorithms for key exchange. Hashing algorithms must use SHA-256 or a stronger cryptographic hash function. Hashing algorithms such as MD4, MD5, and SHA-1 aren't supported.
  * For client (leaf) certificates: 
    * The [Basic Constraints](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.9) extension must _not_ contain `CA=true`.
    * The [Extended Key Usage](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12) extension must contain `clientAuth`.
    * The [Extended Key Usage](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12) extension must _not_ contain the `codeSigning`, `timeStamping`, or `OCSPSigning` fields.
    * The certificate must not be expired.
    * The client certificate cannot be a [self-signed certificate](https://en.wikipedia.org/wiki/Self-signed_certificate).
  * For root and intermediate certificates: 
    * The [Basic Constraints](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.9) extension must contain `CA=true`.
    * The [Key Usage](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.3) extension must be set to `keyCertSign`.
    * The [Extended Key Usage](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12) extension should contain the `clientAuth` field.
    * The certificate must not be expired.



## Architecture of an mTLS deployment

With mTLS, you can configure a trust config resource, which contains a trust store. The trust store encapsulates a trust anchor (root certificate) and, optionally, one or more intermediate certificates. When the load balancer receives a client certificate, the load balancer validates it by establishing a chain of trust from the client certificate back to the configured trust anchor.

The following is a brief overview of the different resources you need to configure to set up mTLS for the load balancer:

  * **Trust config.** Contains a single trust store resource, which in turn encapsulates a trust anchor (root certificate) and, optionally, one or more intermediate certificates. The trust config is used to establish a chain of trust between the client certificate and the trust anchor. For more information, see [Trust configs](https://docs.cloud.google.com/certificate-manager/docs/core-components#trust-configs).

Optionally, if you need to use a certificate that has been self-signed, is expired, or is otherwise invalid, or if you don't have access to the root and intermediate certificates, you can add that certificate to the trust config in the `allowlistedCertificates` field. You don't need a trust store to add a certificate to an allowlist.

Adding a certificate to the allowlist means that the certificate is always considered valid as long as the certificate is parseable, proof of private key possession is established, and constraints on the SAN field of the certificate are met.

  * **Trust store.** Contains the trust anchor and intermediate certificate authority (CA) certificates that is used to establish a chain of trust and validate the client certificate. A CA is used to issue trusted certificates for the client. The CA is identified by the load balancer's trust anchor (root certificate) or the intermediate CA certificates.

You can upload the following types of root and intermediate certificates to the trust store:

    * Certificates issued by third-party CAs of your choice.
    * Certificates issued by private CAs in your control, as described in [Set up mutual TLS with a private CA](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ca-ccm).
    * User-provided certificates, as described in [Set up mutual TLS with user-provided certificates](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm).
  * **Client Authentication (also known as[`ServerTLSPolicy`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies)).** Specifies the client validation mode and the trust config resource to use when validating client certificates. When the client presents an invalid certificate or no certificate to the load balancer, the client validation mode specifies how the client connection is handled. You can specify all the mTLS authentication related parameters in the server TLS policies. The Client Authentication (`ServerTLSPolicy`) resource is attached to the target HTTPS proxy resource.




The following diagrams show the different mTLS components attached to the target HTTPS proxy resource of global and regional Application Load Balancers.

### global

The following diagram shows the components of an external Application Load Balancer deployment. This architecture also applies to the cross-region internal Application Load Balancer, which is an internal Application Load Balancer that uses global components.

[ ![Mutual TLS with global external Application Load Balancer components.](https://docs.cloud.google.com/static/load-balancing/images/mtls_l7xlb.svg)](https://docs.cloud.google.com/static/load-balancing/images/mtls_l7xlb.svg) Mutual TLS with global external Application Load Balancer components (click to enlarge).

### regional

The following diagram shows the components of a regional internal Application Load Balancer deployment. This architecture also applies to the regional external Application Load Balancer, which is an external Application Load Balancer that uses regional components.

[ ![Mutual TLS with regional internal Application Load Balancer components.](https://docs.cloud.google.com/static/load-balancing/images/mtls_rilb.svg)](https://docs.cloud.google.com/static/load-balancing/images/mtls_rilb.svg) Mutual TLS with regional internal Application Load Balancer components (click to enlarge).

## Client validation mode

When the client presents an invalid certificate or no certificate to the load balancer, the [`clientValidationMode`](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies#mtlspolicy) attribute on the Client Authentication (`ServerTLSPolicy`) resource specifies how the load balancer handles the client connection.

The values of the client validation mode are as follows:

  * `ALLOW_INVALID_OR_MISSING_CLIENT_CERT`. Allows the connection from the client even if the validation of the client certificate failed or no client certificate was presented. In this mode, the load balancer allows the connection from the client and passes all requests to the backend regardless of whether or not a chain of trust can be established.

The proof of possession of the private key is always checked when the client certificate is presented. If the client cannot prove the possession of the private key, the TLS handshake is terminated even if the client validation mode allows invalid or a missing client certificate.

  * `REJECT_INVALID`. Rejects the connection if a client does not provide a certificate or if the certificate validation failed. In this mode, the load balancer terminates the connection from the client if it cannot establish a chain of trust from the client certificate back to the trust anchor.




## Configure mTLS on the load balancer

The following is a high-level overview of the key steps that you need to follow to configure mTLS on your load balancer:

  1. Create a trust config resource comprising the trust anchor (root certificate) and intermediate certificates that serve as roots of trust.

  2. Link the trust config to the Client Authentication (`ServerTLSPolicy`) resource, which defines the client validation mode of either `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` or `REJECT_INVALID`.

  3. Attach the Client Authentication (`ServerTLSPolicy`) resource to the target HTTPS proxy resource of the load balancer.

  4. Optional: You can use custom mTLS headers to pass information about the mTLS connection to a backend service or a URL map.




To learn more about this setup in detail, see the following guides:

  * [Set up mutual TLS with user-provided certificates](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm)
  * [Set up mutual TLS with a private CA](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ca-ccm)



## Client certificate validation steps

When validating the client certificate, the load balancer does the following:

  1. **Verify that the client possesses the private key**.

The client proves possession of the private key associated with the public key in the certificate by generating a signature during the handshake process. The load balancer verifies this signature using the client's public key. If the signature verification fails, it means that the client is not the owner of the certificate, in which case, the TLS handshake is terminated even if your configuration allows invalid or a missing client certificate. No errors are logged for global external Application Load Balancers, but a TLS error is logged in the `proxyStatus` field for regional external Application Load Balancers and internal Application Load Balancers.

  2. **Verify the chain of trust**.

The load balancer verifies the chain of trust between the client certificate and the configured trust config. The verification checks include the following:

     * The client, intermediate, and root certificates comply with the certificate requirements.
     * The subject field in the parent certificate matches the issuer field in the child certificate. This verification ensures that the parent certificate's identity (subject) is the same as the identity listed as the issuer in the child certificate.
     * The Subject Key Identifier (SKID) of the parent certificate matches the Authority Key identifier (AKID) in the child certificate. This match confirms that the child certificate was issued by the correct root authority and that it can be trusted because the root's public key is being referenced in the AKID for verifying the certificate's validity.
     * The subject alternative name (SAN) of a child certificate does not violate the `NameConstraints` field in the parent certificate.
**Note:** Self-signed client certificates fail to form a valid chain of trust and are always rejected.
  3. **Forward the request to the backend**.

If the client certificate validation succeeds, the request is forwarded to the backend using custom mTLS headers.

However, if the validation fails, the action taken depends on the value of the client validation mode:

     * `ALLOW_INVALID_OR_MISSING_CLIENT_CERT`: The request is forwarded with custom mTLS headers indicating the reason for validation failure. For cross-region internal Application Load Balancers, regional external Application Load Balancers, and regional internal Application Load Balancers, in addition to custom mTLS headers, you can configure mTLS [optional fields](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#optional_fields) to check the reason for the failure.

     * `REJECT_INVALID`: The connection is terminated and the errors are logged to Cloud Logging.




### Custom mTLS headers passed to the backend

The following table shows the [custom mTLS header variables](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-global#mtls-variables) that are available to be passed to the backend, both when the client certificate passes validation and when it fails. If the client certificate fails validation, requests are passed to the backend only when the client validation mode is set to `ALLOW_INVALID_OR_MISSING_CLIENT_CERT`.

These variables can also be set on [URL map](https://docs.cloud.google.com/load-balancing/docs/l7-internal/custom-headers#mtls-variables).

Client certificate status | Client validation mode | Custom headers  
---|---|---  
The client certificate chain is too long (more than 10 intermediate certificates included with the client certificate). | `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` |  `client_cert_present: true` `client_cert_chain_verified: false` `client_cert_error: client_cert_chain_exceeded_limit` `client_cert_sha256_fingerprint: <cert hash>`  
A client or an intermediate certificate has an invalid RSA key size. No validation is performed. RSA keys can range from 2048 to 4096 bits. | `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` |  `client_cert_present: true` `client_cert_chain_verified: false` `client_cert_error: client_cert_invalid_rsa_key_size` `client_cert_sha256_fingerprint: <cert hash>`  
A client or an intermediate certificate is using an unsupported elliptic curve. No validation is performed. Valid elliptic curves are P-256 and P-384. | `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` |  `client_cert_present: true` `client_cert_chain_verified: false` `client_cert_error: client_cert_unsupported_elliptic_curve_key` `client_cert_sha256_fingerprint: <cert hash>`  
A client or an intermediate certificate is using a non-RSA, non-ECDSA algorithm. No validation is performed. | `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` |  `client_cert_present: true` `client_cert_chain_verified: false` `client_cert_error: client_cert_unsupported_key_algorithm` `client_cert_sha256_fingerprint: <cert hash>`  
The PKI to be used for validation has more than ten intermediate certificates that share the same Subject and Subject Public Key Info. No validation is performed. | `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` |  `client_cert_present: true` `client_cert_chain_verified: false` `client_cert_error: client_cert_pki_too_large` `client_cert_sha256_fingerprint: <cert hash>`  
An intermediate certificate provided for validation had more than 10 name constraints. | `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` |  `client_cert_present: true` `client_cert_chain_verified: false` `client_cert_error: client_cert_chain_max_name_constraints_exceeded` `client_cert_sha256_fingerprint: <cert hash>`  
The client certificate doesn't have [`Extended Key Usage (EKU)`](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12) extension that includes `clientAuth`. | `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` |  `client_cert_present: true` `client_cert_chain_verified: false` `client_cert_error: client_cert_chain_invalid_eku` `client_cert_sha256_fingerprint: <cert hash>`  
The time limit is exceeded while attempting to validate the certificate chain.  | `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` |  `client_cert_present: true` `client_cert_chain_verified: false` `client_cert_error: client_cert_validation_timed_out` `client_cert_sha256_fingerprint: <cert hash>`  
The depth or iteration limit is reached while attempting to validate the certificate chain. The maximum depth for a certificate chain is ten, including the root and client certificates. The maximum iterations is 100 (certificates examined to validate the client certificate chain). | `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` |  `client_cert_present: true` `client_cert_chain_verified: false` `client_cert_error: client_cert_validation_search_limit_exceeded` `client_cert_sha256_fingerprint: <cert hash>`  
You configured mTLS without setting up a `TrustConfig` resource. No validation can be performed, but the cert hash is forwarded to the backend. | `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` |  `client_cert_present: true` `client_cert_chain_verified: false` `client_cert_error: client_cert_validation_not_performed` `client_cert_sha256_fingerprint: <cert hash>`  
No client certificate.  | `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` |  `client_cert_present: false` `client_cert_chain_verified: false` `client_cert_error: client_cert_not_provided` `client_cert_sha256_fingerprint: <empty>`  
Client certificate fails validation against the `TrustConfig` resource.  | `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` |  `client_cert_present: true` `client_cert_chain_verified: false` `client_cert_error: client_cert_validation_failed` `client_cert_sha256_fingerprint: <cert hash>`  
Client certificate passes cert verifier validation.  | Not applicable  |  `client_cert_present: true` `client_cert_chain_verified: true` `client_cert_error: <empty>` `client_cert_sha256_fingerprint: <cert hash>` `client_cert_serial_number: <serial_number>` `client_cert_valid_not_before: <date>` `client_cert_valid_not_after: <date>` `client_cert_uri_sans: <list>` `client_cert_dnsname_sans: <list>` `client_cert_issuer_dn: <issuer>` `client_cert_subject_dn: <subject>` `client_cert_leaf: <certificate>` `client_cert_chain: <list>`  
  
#### Parse custom header variable values passed to the backend

Some [custom mTLS header variable values](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers#mtls-variables) are Base64-encoded string representations of binary Distinguished Encoding Rules (DER) certificate data. You can decode Base64-encoded strings using your choice of tools or software libraries. The following are some examples:

  * macOS and Linux systems can use the command-line `base64` tool, which is a core utility included in both operating systems. To decode Base64-encoded strings using the `base64` utility, pass the encoded string as standard input to the `base64` command and use the `-d` flag to decode the string as follows:
        
        echo BASE_64_ENCODED_STRING | base64 -d
        

  * Python includes the [base64 module](https://docs.python.org/3/library/base64.html), which can be used to decode Base64-encoded strings as follows:
        
        import base64
        encoded_string=BASE_64_ENCODED_STRING
        decoded_string=base64.b64decode(encoded_string).decode()
        print(decoded_string) # Note that a newline character (\n) is added to the end of the string.
        




### Error handling and logging

Application Load Balancers provide detailed logging capabilities that allow you to monitor client certificate validation, identify potential issues, and troubleshoot connection problems. This section outlines the different types of errors that can occur during mTLS validation and how they are logged.

#### Logged errors in `REJECT_INVALID` mode

If the client certificate validation fails, and the client validation mode is set to `REJECT_INVALID`, the connection is terminated and the errors are logged to Cloud Logging. These errors are described in the following table.

Client certificate status | Logged error  
---|---  
The client certificate chain is too long (more than 10 intermediate certificates included with the client certificate).  |  `client_cert_chain_exceeded_limit`  
A client or an intermediate certificate has an invalid RSA key size. No validation is performed. RSA keys can range from 2048 to 4096 bits. |  `client_cert_invalid_rsa_key_size`  
A client or an intermediate certificate is using an unsupported elliptic curve. No validation is performed. Valid curves are P-256 and P-384. |  `client_cert_unsupported_elliptic_curve_key`  
A client or an intermediate certificate is using a non-RSA or non-ECDSA algorithm. No validation is performed. |  `client_cert_unsupported_key_algorithm`  
The PKI to be used for validation has more than ten intermediate certificates that share the same Subject and Subject Public Key Info. No validation is performed. |  `client_cert_pki_too_large`  
An intermediate certificate provided for validation had more than 10 name constraints. |  `client_cert_chain_max_name_constraints_exceeded`  
The client certificate does not have an [`Extended Key Usage (EKU)`](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.12) extension that includes `clientAuth`. | `client_cert_chain_invalid_eku`  
The time limit is exceeded while attempting to validate the certificate chain.  |  `client_cert_validation_timed_out`  
The depth or iteration limit is reached while attempting to validate the certificate chain. The maximum depth for a certificate chain is ten, including the root and client certificates. The maximum number of iterations is 100 (certificates examined to validate the client certificate chain). | `client_cert_validation_search_limit_exceeded`  
You configured mTLS without setting up a `TrustConfig` resource.  |  `client_cert_validation_not_performed`  
The client did not provide the requested certificate during the handshake.  |  `client_cert_not_provided`  
The client certificate fails validation with the `TrustConfig` resource.  |  `client_cert_validation_failed`  
  
#### Logged errors for closed connections

When the client validation mode is set to either `ALLOW_INVALID_OR_MISSING_CLIENT_CERT` or `REJECT_INVALID`, certain errors result in closed connections and are logged to Cloud Logging. These errors are described in the following table.

Client certificate status | Request | Logged error  
---|---|---  
Client certificate fails signature match during handshake.  | Terminate SSL handshake  | None   
Service is unable to perform certificate chain validation.  | Terminate connection  |  `client_cert_validation_unavailable`  
Internal error validating certificate chain.  | Terminate connection  |  `client_cert_validation_internal_error`  
Matching `TrustConfig` not found.  | Terminate connection  |  `client_cert_trust_config_not_found`  
The client certificate payload (including any intermediate certificates) is too large (more than 16 KB).  | Terminate connection  |  `client_cert_exceeded_size_limit`  
  
If logging is enabled on the backend service, you can [view logged errors for closed connections during mTLS client certificate validation](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#log-fwd-rule).

## Limitations

  * The load balancer doesn't perform revocation checks on client certificates.

  * Application Load Balancers let you upload a trust config with a single trust store, that contains at most: 200 of combined number of trust anchors and intermediate certificates (number of intermediate certificates is limited to 100) and 500 certificates that are added to an allowlist. All intermediate certificates must not have more than three certificates that share the same Subject and Subject Public Key info. For more information, see [Quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas#trust-config).

  * The maximum depth for a certificate chain is ten, including the root and client certificates. The maximum number of times that intermediate certificates can be evaluated when attempting to build the chain of trust is 100. For more information, see [Quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas#trust-config).

  * Keys of certificates uploaded and passed from the client are restricted to the following:

    * RSA keys can range from 2048 to 4096 bits. For more information, see [Quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas#trust-config).
    * ECDSA keys can use the P-256 or P-384 curves.
  * The accepted certificate chain received from the client is limited to up to 16 KB and 10 certificates. For more information, see [Quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas#trust-config).

  * Root certificates used for validation cannot contain more than 10 name constraints. For more information, see [Quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas#trust-config).

  * The Layer 1 [Google Front Ends (GFEs)](https://docs.cloud.google.com/docs/security/infrastructure/design#google-frontend-service) enforces a non-configurable timeout of 10 seconds for the client to present its certificate during the TLS handshake. Under peak load, this timeout might be shorter. Clients must complete certificate presentation within this timeframe to successfully establish an mTLS connection.




## What's next

  * [Set up mutual TLS with user-provided certificates](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm)

  * [Set up mutual TLS with a private CA](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ca-ccm)

  * [Variables that can appear in the header value](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-global#variables)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
