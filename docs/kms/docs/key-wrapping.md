---
url: https://docs.cloud.google.com/kms/docs/key-wrapping/
title: Key wrapping \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:30.328197+00:00
---

# Key wrapping  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/key-wrapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Key wrapping Stay organized with collections  Save and categorize content based on your preferences. 

_Key wrapping_ is the process of encrypting one key using another key, in order to securely store it or transmit it over an untrusted channel. Key wrapping may rely on either symmetric or asymmetric cryptography, depending on the context.

In Cloud Key Management Service, key wrapping is used to securely import user-provided cryptographic keys. Importing keys requires an _import job_ , and each import job has an _import method_ that specifies the key wrapping protocol to use.

Cloud KMS expects specific formats for imported key material. Before your key material is wrapped for import, you may need to convert it to the format expected by Cloud KMS. [Formatting keys for import](https://docs.cloud.google.com/kms/docs/formatting-keys-for-import) contains details of the required formats, and provides instructions on how you can convert your keys to the required format if necessary.

Once your key material is formatted properly, the Google Cloud CLI can automatically wrap your key material before securely transmitting it to Cloud KMS. For details, see [Importing a key](https://docs.cloud.google.com/kms/docs/importing-a-key). Alternatively, you may manually wrap your keys using the appropriate cryptographic protocols. [Wrapping a key using OpenSSL on Linux](https://docs.cloud.google.com/kms/docs/wrapping-a-key) provides one example of how you can do this.

## Import methods

Cloud KMS provides the following import methods:

Import method | Import job key type | Key wrapping algorithm  
---|---|---  
RSA_OAEP_3072_SHA1_AES_256 | 3072-bit RSA | RSAES-OAEP with SHA-1 + AES-KWP  
RSA_OAEP_4096_SHA1_AES_256 | 4096-bit RSA | RSAES-OAEP with SHA-1 + AES-KWP  
RSA_OAEP_3072_SHA256_AES_256 **(recommended)** | 3072-bit RSA | RSAES-OAEP with SHA-256 + AES-KWP  
RSA_OAEP_4096_SHA256_AES_256 | 4096-bit RSA | RSAES-OAEP with SHA-256 + AES-KWP  
RSA_OAEP_3072_SHA256 | 3072-bit RSA | RSAES-OAEP with SHA-256  
RSA_OAEP_4096_SHA256 | 4096-bit RSA | RSAES-OAEP with SHA-256  
  
## Key wrapping algorithms

The import methods provided by Cloud KMS correspond to the following key wrapping algorithms:

### RSAES-OAEP with SHA-1/SHA-256 + AES-KWP

This key wrapping algorithm is a hybrid encryption scheme that consists of both an asymmetric key wrapping operation and a symmetric key wrapping operation:

  1. The public key from the import job is used to encrypt a one-time-use AES-256 key. Encryption is performed using RSAES-OAEP and MGF-1, along with the digest algorithm specified by the import method. The one-time-use AES-256 key is generated at the time the wrapping is performed.
  2. The one-time-use AES-256 key from step 1 is used to encrypt the target key material using [AES Key Wrap with Padding](https://tools.ietf.org/html/rfc5649).



The wrapped key material for import is a single byte array consisting of the results of step 1, followed by the results of step 2. In other words, the results of steps 1 and 2 are concatenated together to form the wrapped key material.

This algorithm is the same as the PKCS #11 key wrapping algorithm [CKM_RSA_AES_KEY_WRAP](http://docs.oasis-open.org/pkcs11/pkcs11-curr/v2.40/cos01/pkcs11-curr-v2.40-cos01.html#_Toc408226908). If you are importing a key from an HSM, and your HSM supports this algorithm, you may use it directly. Alternatively, steps 1 and 2 above can be performed with the PKCS #11 mechanisms [CKM_RSA_PKCS_OAEP](http://docs.oasis-open.org/pkcs11/pkcs11-curr/v2.40/cos01/pkcs11-curr-v2.40-cos01.html#_Toc228894637) and [CKM_AES_KEY_WRAP_PAD](http://docs.oasis-open.org/pkcs11/pkcs11-curr/v2.40/cos01/pkcs11-curr-v2.40-cos01.html#_Toc228894722) respectively.

If your source HSM (or other key provider if not using HSM) does not support the RSA AES key wrap mechanism, you need to manually wrap your key material using your import job's public key. For one example of how to do this using OpenSSL, see [Wrapping a key using OpenSSL on Linux](https://docs.cloud.google.com/kms/docs/wrapping-a-key).

### RSAES-OAEP with SHA-256

This is an asymmetric key wrapping operation that uses the public key from the import job with RSAES-OAEP, using MGF-1 and the SHA-256 digest algorithm, to directly encrypt the target key material. It is based on the PKCS #11 RSA OAEP mechanism [CKM_RSA_PKCS_OAEP](http://docs.oasis-open.org/pkcs11/pkcs11-curr/v2.40/cos01/pkcs11-curr-v2.40-cos01.html#_Toc228894637). The size limitations associated with this import method make it unsuitable for importing RSA private keys.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
