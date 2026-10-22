---
url: https://docs.cloud.google.com/certificate-authority-service/docs/certificate-profile/
title: Certificate profiles \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:48.172221+00:00
---

# Certificate profiles  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/certificate-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Reference ](https://docs.cloud.google.com/certificate-authority-service/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Certificate profiles

This topic provides certificate profiles that you can use for various certificate issuance scenarios. You can reference these certificate profiles when creating a certificate or a certificate authority (CA) using the Google Cloud CLI or the Google Cloud console.

Use the `gcloud` references specified in this document along with the `--use-preset-profile` flag to utilize the certificate profile that fits your needs.

## Unconstrained

Unconstrained certificate profiles add no constraints or limits.

### Root unconstrained

**Accessible as** : `root_unconstrained`

The following certificate profile has neither extended key usage nor path-length constraints.

This CA can issue any type of certificate, including subordinate CAs. These values are appropriate for a self-signed root CA but you can also use them for an unconstrained subordinate CA.
    
    
    keyUsage:
      baseKeyUsage:
        certSign: true
        crlSign: true
    caOptions:
      isCa: true
    

### Subordinate unconstrained with path length of zero

**Accessible as** : `subordinate_unconstrained_pathlen_0`

You can use the following certificate profile to configure a CA that has no Extended Key Usage (EKU) constraints, but has a path-length restriction that doesn't allow the issuing of any subordinate CAs. These values are appropriate for CAs issuing end-entity certificates.
    
    
    keyUsage:
      baseKeyUsage:
        certSign: true
        crlSign: true
    caOptions:
      isCa: true
      maxIssuerPathLength: 0
    

## Mutual TLS

Mutual Transport Layer Security (mTLS) certificates can be used for server TLS, client TLS, or mutual TLS authentication.

### Subordinate mTLS

**Accessible as** : `subordinate_mtls_pathlen_0`

You can use the following certificate profile to configure a CA that can issue end-entity certificates usable for server TLS, client TLS, or mutual TLS authentication. This certificate profile has a path-length restriction that does not allow further subordinate CAs. These values are appropriate for a subordinate CA but they can also be used for a self-signed CA that directly issues end-entity certificates.
    
    
    keyUsage:
      baseKeyUsage:
        certSign: true
        crlSign: true
      extendedKeyUsage:
        serverAuth: true
        clientAuth: true
    caOptions:
      isCa: true
      maxIssuerPathLength: 0
    

### End-entity mTLS

**Accessible as** : `leaf_mtls`

You can use the following certificate profile to configure end-entity certificates that are compatible with client TLS, server TLS, or mTLS. For example, [SPIFFE](https://spiffe.io/) certificates.
    
    
    keyUsage:
      baseKeyUsage:
        digitalSignature: true
        keyEncipherment: true
      extendedKeyUsage:
        serverAuth: true
        clientAuth: true
    caOptions:
      isCa: false
    

**Note:** The `keyEncipherment` field is required only when the accompanying public key uses the RSA encryption algorithm, and the TLS handshake uses an RSA key exchange.

## Client TLS

Client TLS certificates are used to authenticate a client.

### Subordinate client TLS

**Accessible as** : `subordinate_client_tls_pathlen_0`

You can use the following certificate profile to configure a CA that can issue end-entity certificates usable for client TLS. This certificate profile has a path-length restriction that does not allow further subordinate CAs. These values are appropriate for a subordinate CA but they can also be used for a self-signed CA that directly issues end-entity certificates.
    
    
    keyUsage:
      baseKeyUsage:
        certSign: true
        crlSign: true
      extendedKeyUsage:
        clientAuth: true
    caOptions:
      isCa: true
      maxIssuerPathLength: 0
    

### End-entity client TLS

**Accessible as** : `leaf_client_tls`

You can use the following certificate profile to configure end-entity certificates that are compatible with client TLS. For example, a client authenticating itself to a TLS firewall.
    
    
    keyUsage:
      baseKeyUsage:
        digitalSignature: true
        keyEncipherment: true
      extendedKeyUsage:
        clientAuth: true
    caOptions:
      isCa: false
    

**Note:** The `keyEncipherment` field is required only when the accompanying public key uses the RSA encryption algorithm, and the TLS handshake uses an RSA key exchange.

## Server TLS

Server TLS certificates are used to authenticate a server.

### Subordinate server TLS

**Accessible as** : `subordinate_server_tls_pathlen_0`

You can use the following certificate profile to configure a CA that can issue end-entity certificates usable for server TLS. This certificate profile has a path-length restriction that does not allow further subordinate CAs. These values are appropriate for a subordinate CA but they can also be used for a self-signed CA that directly issues end-entity certificates.
    
    
    keyUsage:
      baseKeyUsage:
        certSign: true
        crlSign: true
      extendedKeyUsage:
        serverAuth: true
    caOptions:
      isCa: true
      maxIssuerPathLength: 0
    

### End-entity server TLS

**Accessible as** : `leaf_server_tls`

You can use the following certificate profile to configure end-entity certificates that are compatible with server TLS.
    
    
    keyUsage:
      baseKeyUsage:
        digitalSignature: true
        keyEncipherment: true
      extendedKeyUsage:
        serverAuth: true
    caOptions:
      isCa: false
    

**Note:** The `keyEncipherment` field is required only when the accompanying public key uses the RSA encryption algorithm, and the TLS handshake uses an RSA key exchange.

## Code signing

Digital signatures are used for code authentication.

### Subordinate code signing

**Accessible as** : `subordinate_code_signing_pathlen_0`

You can use the following certificate profile to configure a CA that can issue end-entity certificates usable for code signing. This certificate profile has a path-length restriction that does not allow further subordinate CAs. These values are appropriate for a subordinate CA but they can also work for a self-signed CA that directly issues end-entity certificates.
    
    
    keyUsage:
      baseKeyUsage:
        certSign: true
        crlSign: true
      extendedKeyUsage:
        codeSigning: true
    caOptions:
      isCa: true
      maxIssuerPathLength: 0
    

### End-entity code signing

**Accessible as** : `leaf_code_signing`

You can use the following certificate profile to configure end-entity certificates that are compatible with code signing.
    
    
    keyUsage:
      baseKeyUsage:
        digitalSignature: true
        contentCommitment: true
      extendedKeyUsage:
        codeSigning: true
    caOptions:
      isCa: false
    

## S/MIME

S/MIME is an email-signing protocol that helps improve email security.

### Subordinate S/MIME

**Accessible as** : `subordinate_smime_pathlen_0`

You can use the following certificate profile to configure a CA that can issue end-entity certificates usable for S/MIME. This certificate profile has a path-length restriction that does not allow further subordinate CAs. These values are appropriate for a subordinate CA but they can also be used for a self-signed CA that directly issues end-entity certificates.
    
    
    keyUsage:
      baseKeyUsage:
        certSign: true
        crlSign: true
      extendedKeyUsage:
        emailProtection: true
    caOptions:
      isCa: true
      maxIssuerPathLength: 0
    

### End-entity S/MIME

**Accessible as** : `leaf_smime`

You can use the following certificate profile to configure end-entity certificates that are compatible with S/MIME. S/MIME is often used for end-to-end email integrity or encryption.
    
    
    keyUsage:
      baseKeyUsage:
        digitalSignature: true
        contentCommitment: true
      extendedKeyUsage:
        emailProtection: true
    caOptions:
      isCa: false
    

## What's next

  * Learn more about [certificate templates](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-template).
  * Learn more about [policy controls](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls).
  * Learn more about [using an issuance policy](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
