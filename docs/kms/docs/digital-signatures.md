---
url: https://docs.cloud.google.com/kms/docs/digital-signatures/
title: Digital signatures \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:38.921089+00:00
---

# Digital signatures  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/digital-signatures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Digital signatures Stay organized with collections  Save and categorize content based on your preferences. 

A _digital signature_ is a cryptographic output used to verify the authenticity of data. A digital signature algorithm allows for two distinct operations:

  * a signing operation, which uses a signing key to produce a signature over raw data

  * a verification operation, where the signature can be validated by a party who has no knowledge of the signing key




The main purposes of a digital signature are:

  * verification of the integrity of the signed data
  * non-repudiation if the signer claims the signature is not authentic



Digital signatures rely on asymmetric cryptography, also known as public key cryptography. An asymmetric key consists of a public/private key pair. The private key is used to create a signature, and the corresponding public key is used to verify the signature.

## Post-quantum cryptography (PQC) digital signature

Quantum computers have the potential to decrypt material encrypted by classical encryption algorithms such as the widely used RSA and ECDSA, which could make such encrypted material vulnerable. Post-quantum cryptographic algorithms are designed to use classical hardware and software to resist quantum attacks, helping to ensure the continued validity of digital signatures. PQC signatures are based on different mathematical problems that are difficult for both classical and quantum computers to solve.

NIST has published two PQC signature standards: ML-DSA ([FIPS-204](https://csrc.nist.gov/pubs/fips/204/final)) and SLH-DSA ([FIPS-205](https://csrc.nist.gov/pubs/fips/205/final)). You can use the pure randomized variants `ML-DSA-44`, `ML-DSA-65`, `ML-DSA-87` (or their external-μ variants) and `SLH-DSA-SHA2-128s` (or its pre-hash variant) with Cloud KMS. The NIST standards define the following size values for keys and signatures (in bytes):

Algorithm | Private key | Public key | Signature | NIST Security Category  
---|---|---|---|---  
SLH_DSA_SHA2_128s | 64 | 32 | 7856 | 1  
ML_DSA_44 | 2560 | 1312 | 2420 | 2  
ML_DSA_65 | 4032 | 1952 | 3309 | 3  
ML_DSA_87 | 4896 | 2592 | 4627 | 5  
**Note:** Due to the lack of a standard for hybridization of post-quantum and classical digital signatures, only the standalone implementations are supported.

## Example use cases for a digital signature

You can validate builds using digital signatures. For example, given a binary that is digitally signed by a private key, you can check its validity by using the public key corresponding to the private key. If the binary's signature is not valid, the binary has been tampered with and/or corrupted.

Another example is validating the subject of a certificate issued by a Certificate Authority (CA). A CA issues a certificate to a subject based on the subject's ownership of the private key portion of a public/private key. The certificate contains a digital signature created with the subject's private key. The certificate also contains the subject's public key portion of the public/private key. An entity that is interacting with the subject uses the subject's public key, and additional certificate verification rules, to validate the signature. If the signature does not correspond to the data in question, or if the verification rules prescribed by the certificate are violated, the signature will be found invalid.

## Digital signing workflow

The following describes the flow for creating and validating a signature. The two participants in this workflow consist of the signer of data, and the data recipient.

  1. The signer creates an asymmetric key that supports digital signing.

The signer can use this key to create multiple signatures.

  2. The signer performs a private key operation over the data to create a digital signature.

  3. The signer provides the data and the digital signature to the data recipient.

  4. The recipient uses the public key portion of the signer's public/private key pair to verify the digital signature. If verification is unsuccessful, then the data has been altered.




## Signing algorithms

Cloud Key Management Service supports elliptic curve (EC) and RSA algorithms for digital signing. Both of these industry standard algorithms offer choices of key size and digest algorithm.

Elliptic curve cryptography relies on one-way hash functions and point multiplication to compute points on an elliptic curve, combined with the intractability of determining the multiplicand for a point given its origin. This difficulty in determining the multiplicand is the cryptographic benefit of EC cryptography. The larger the size of the curve, the more difficult it is to compute the multiplicand. A benefit of EC cryptography is that an EC key's size is smaller than an RSA key but offers the same cryptographic strength.

RSA cryptography relies on the difficulty in factoring a large integer into two or more factors. The larger the key size, the more difficult it is to factor the integers.

## Cloud KMS digital signature functionality

Cloud KMS provides the following functionality related to creating and validating digital signatures.

  * Ability to [create an asymmetric key](https://docs.cloud.google.com/kms/docs/creating-asymmetric-keys) with [key purpose](https://docs.cloud.google.com/kms/docs/algorithms#key_purposes) of `ASYMMETRIC_SIGN`. Cloud KMS keys for asymmetric signing support both [elliptic curve signing algorithms](https://docs.cloud.google.com/kms/docs/algorithms#elliptic_curve_signing_algorithms) and [RSA signing algorithms](https://docs.cloud.google.com/kms/docs/algorithms#rsa_signing_algorithms).

  * Ability to [create a digital signature](https://docs.cloud.google.com/kms/docs/create-validate-signatures#create_signature).

  * Ability to [retrieve the public key](https://docs.cloud.google.com/kms/docs/retrieve-public-key) for an asymmetric key.




Cloud KMS does not directly provide the ability to validate a digital signature. Instead, you validate a digital signature using openly available SDKs and tools, such as [OpenSSL](https://www.openssl.org/). These SDKs and tools require the public key that you retrieve from Cloud KMS. For information on how to use open SDKs and tools, see [validating an elliptic curve signature](https://docs.cloud.google.com/kms/docs/create-validate-signatures#validate_ec_signature) and [validating an RSA signature](https://docs.cloud.google.com/kms/docs/create-validate-signatures#validate_rsa_signature).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
