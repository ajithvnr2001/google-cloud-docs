---
url: https://docs.cloud.google.com/kms/docs/key-encapsulation-mechanisms/
title: Key encapsulation mechanisms \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:19.656797+00:00
---

# Key encapsulation mechanisms  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/key-encapsulation-mechanisms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Key encapsulation mechanisms Stay organized with collections  Save and categorize content based on your preferences. 

A _key encapsulation mechanism (KEM)_ is a cryptographic process that's used to establish a shared secret between two parties over an untrusted channel. A key encapsulation mechanism involves three main algorithms:

  * **Key generation** : a key pair is generated that consists of a public key and a private key.
  * **Encapsulation** : the public key is used to produce a shared secret and matching ciphertext.
  * **Decapsulation** : the private key is used to recover the shared secret from the ciphertext.



Key encapsulation mechanisms are a fundamental building block for key exchange protocols and [Hybrid Public Key Encryption (HPKE)](https://www.rfc-editor.org/info/rfc9180).

## Encapsulation and decapsulation workflow

The following describes the process for using a KEM key pair to encapsulate and decapsulate data. The two participants in this workflow are a sender and a recipient. The sender creates a ciphertext and a shared secret using the recipient's public key, and then the recipient decrypts the ciphertext using the recipient's private key to retrieve the shared secret. Only someone with knowledge of the private key can decapsulate the ciphertext to retrieve the original shared secret.

  1. The sender retrieves the recipient's public key.

  2. The sender uses the public key to perform the encapsulation step, which generates a shared secret and a corresponding ciphertext.

  3. The sender sends the ciphertext to the recipient.

  4. The recipient uses the recipient's private key to decapsulate the ciphertext. The recipient and the sender now have the same shared secret.




## Post-quantum key encapsulation mechanisms (PQ-KEM)

Quantum computers have the potential to decrypt material encrypted by classical encryption algorithms such as the widely used RSA and ECDSA algorithms, which can make such encrypted material vulnerable to "store now, decrypt later" (SNDL) attacks. In such attacks, adversaries collect today's encrypted data that use classical encryption algorithms and store it, intending to decrypt it later after powerful quantum computers become available. PQ-KEMs are designed to be resistant to quantum attacks, ensuring that data encrypted with them today will remain secure even in the quantum era, preventing future decryption of information stored today.

Cloud Key Management Service supports ML-KEM-768 and ML-KEM-1024, which were standardized by NIST in [FIPS-203](https://csrc.nist.gov/pubs/fips/203/final), and [X-Wing](https://datatracker.ietf.org/doc/html/draft-connolly-cfrg-xwing-kem-06), a hybrid KEM that combines ML-KEM-768 with X25519. These algorithms have the following size values (in bytes):

Algorithm | Public key | Ciphertext | Shared Secret  
---|---|---|---  
ML_KEM_768 | 1184 | 1088 | 32  
ML_KEM_1024 | 1568 | 1568 | 32  
KEM_XWING | 1216 | 1120 | 32  
  
## Cloud KMS KEMs capabilities

Cloud KMS provides the following capabilities related to key encapsulation mechanisms:

  * [Creating a KEM key](https://docs.cloud.google.com/kms/docs/creating-asymmetric-keys) with [key purpose](https://docs.cloud.google.com/kms/docs/algorithms#key_purposes) of `KEY_ENCAPSULATION` and a [key encapsulation algorithm](https://docs.cloud.google.com/kms/docs/algorithms#key_encapsulation_algorithms).

  * [Retrieving the public key](https://docs.cloud.google.com/kms/docs/retrieve-public-key) for a KEM key.

  * [Decapsulating a shared secret using the private key for a KEM key](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/decapsulate).




To encapsulate using Cloud KMS keys, you must use openly available SDKs and tools with the public key. Cloud KMS doesn't provide encapsulation capabilities.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
