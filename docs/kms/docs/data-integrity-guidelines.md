---
url: https://docs.cloud.google.com/kms/docs/data-integrity-guidelines/
title: Verifying end-to-end data integrity \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:40.732432+00:00
---

# Verifying end-to-end data integrity  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/data-integrity-guidelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Verifying end-to-end data integrity Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses using fields in the Cloud Key Management Service API to detect and prevent unintended changes to data as it moves between client systems and Cloud KMS. These guidelines supplement the ways that Google Cloud automatically protects your data at rest and in transit.

## Automatic data protection

All data on Google Cloud is automatically encrypted [in transit](https://docs.cloud.google.com/security/encryption-in-transit) and [at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) within Google Cloud.

Cloud KMS takes extra steps to protect encryption keys at rest by encrypting each encryption key using another cryptographic key called a _key encryption key_ (KEK). To learn more about this technique, refer to [envelope encryption](https://docs.cloud.google.com/kms/docs/envelope-encryption).

Each Cloud KMS cryptographic operation includes automatic checks for data corruption. If corruption is detected, the operation is aborted and a detailed error is logged.

These automatic protections are important, but they don't prevent client-side data corruption. For example, data corruption during encryption can lead to data that can't be decrypted.

This topic discusses ways to detect and prevent client-side data corruption to minimize the risk of data loss.

**Note:** It is strongly recommended that callers utilize the integrity verification scheme described below to minimize the risk of data loss caused by in-transit data corruption.

## Calculating and verifying checksums

Each cryptographic operation's request and response include [CRC32C checksum](http://tools.ietf.org/html/rfc4960#appendix-B) fields, such as `plaintext_crc32c`. You can calculate the checksum and compare the calculated and returned values.

On the server, the Cloud Key Management Service API sets boolean fields, such as `verified_plaintext_crc32c`, to `true` to indicate that it received the relevant checksum, and returns an `INVALID_ARGUMENT` error if the checksum doesn't match the value calculated by the server.

Keep the following guidelines in mind when calculating and comparing checksums:

  * Calculate checksums, using a binary encoding, as soon as data is sent or received.
  * Do not store unencrypted plaintext checksums to or from the Cloud Key Management Service API. For example, do not store the unencrypted contents of the `EncryptRequest.plaintext_crc32c` or `DecryptResponse.plaintext_crc32c` fields. To keep a record of a checksum, serialize it along with the relevant data and pass the compound object to Cloud KMS for encryption. When you decrypt data, you can verify the checksum against your calculated expected value.
  * If a decryption operation results in mismatched checksums, design your application to retry the operation a limited number of times, in case of transient problems.
  * If an encryption operation results in mismatched checksums for the encrypted data (the ciphertext), discard the encrypted result and try again.



For encryption requests:

  * If you include the checksum field in the request, the server sets a related verification field in the response to `true` to indicate that it received the checksum and attempted to verify its value.

  * If you include the checksum field but the response sets the verification field to `false`, the server did not receive the checksum field, and other information may be missing from the response. Retry the request a limited number of times in case the error is transient.

  * If the checksum was received but did not match, an `INVALID_ARGUMENT` error is returned. The error includes the name of the field and the checksum that didn't match. For example:
        
        The checksum in field plaintext_crc32c did not match the data in field plaintext.
        

Retry the request a limited number of times in case the error is transient.




For decryption requests, you can calculate a checksum and compare it to the value of `DecryptResponse.plaintext_crc32c` in the response.

The following checksum fields are included in requests to and responses from the Cloud Key Management Service API.

Field in request | Field in response  
---|---  
`EncryptRequest.plaintext_crc32c` | `EncryptResponse.verified_plaintext_crc32c`  
`EncryptionRequest.additional_authenticated_data_crc32c` | `EncryptionResponse.verified_additional_authenticated_data_crc32c`  
`AsymmetricSignRequest.digest_crc32c` | `AsymmetricSignResponse.verified_digest_crc32c`  
`AsymmetricSignRequest.signature_crc32c` | `AsymmetricSignResponse.verified_signature_crc32c`  
`AsymmetricSignRequest.signature_crc32c` | `AsymmetricSignResponse.verified_signature_crc32c`  
Not applicable | `GetPublicKeyResponse.pem_crc32c`  
Not applicable | `GetPublicKeyResponse.public_key.crc32c_checksum`  
Not applicable | `DecryptResponse.plaintext_crc32c`  
`MacSignRequest.data_crc32c` | `MacSignResponse.verified_data_crc32c`  
`MacVerifyRequest.data_crc32c` | `MacVerifyResponse.verified_data_crc32c`  
`MacVerifyRequest.mac_crc32c` | `MacVerifyResponse.verified_mac_crc32c`  
Not applicable | `MacVerifyResponse.verified_success_integrity`  
`DecapsulateRequest.ciphertext_crc32c` | `DecapsulateResponse.verified_ciphertext_crc32c`  
Not applicable | `DecapsulateResponse.shared_secret_crc32c`  
  
## Verifying resource names

Responses for [Encrypt](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.EncryptResponse), [GetPublicKey](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#publickey), [AsymmetricSign](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#asymmetricsignresponse), [AsymmetricDecrypt](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#asymmetricdecryptresponse), [Decapsulate](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#decapsulateresponse), [MacSign](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#macsignresponse), and [MacVerify](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#macverifyresponse), include a `name` field that contains the name of the relevant Cloud Key Management Service API object. You can compare the value of the `name` field to the value you expect, and discard results that do not match.

**Note:** The `EncryptRequest.name` field can contain either a CryptoKey name or a CryptoKeyVersion name. However, the `EncryptResponse.name` field always contains a `CryptoKeyVersion` name. To convert a `CryptoKeyVersion` name to a CryptoKey name, strip `/cryptoKeyVersions/` and its value (such as `/cryptoKeyVersions/2`) from the field.

## Data verification diagram

This diagram shows when to verify each type of data related to cryptographic operations and when to verify data from each type of source. You can also view a summary of the data verification fields.

![Diagram showing different data verification fields and the actions they correspond to](https://docs.cloud.google.com/static/kms/images/e2e-integrity-flow.svg)

## Data verification field summary

Use this tables when designing your application, to determine which fields you can use to verify your data before and after each cryptographic operation.

### Encrypt

API | Server-side input verification | Client-side resource verification | Client-side output verification | Client-side verification of server-side input  
---|---|---|---|---  
`[EncryptRequest](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.EncryptRequest)` | `plaintext_crc32c`, `additional_authenticated_data_crc32c` |  |  |   
`[EncryptResponse](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.EncryptResponse)` |  | `name` | `ciphertext_crc32c` | `verified_plaintext_crc32c`, `verified_additional_authenticated_data_crc32c`  
  
### Decrypt

API | Server-side input verification | Client-side resource verification | Client-side output verification | Client-side verification of server-side input  
---|---|---|---|---  
`[DecryptRequest](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.DecryptRequest)` | `ciphertext_crc32c`, `additional_authenticated_data_crc32c` |  |  |   
`[DecryptResponse](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.DecryptResponse)` |  |  | `plaintext_crc32c` |   
  
### AsymmetricSign

API | Server-side input verification | Client-side resource verification | Client-side output verification | Client-side verification of server-side input  
---|---|---|---|---  
`[AsymmetricSignRequest](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.AsymmetricSignRequest)` | `digest_crc32c` |  |  |   
`[AsymmetricSignResponse](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.AsymmetricSignResponse)` |  | `name` | `signature_crc32c` | verified_digest_crc32c  
  
### AsymmetricDecrypt

API | Server-side input verification | Client-side resource verification | Client-side output verification | Client-side verification of server-side input  
---|---|---|---|---  
`[AsymmetricDecryptRequest](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.AsymmetricDecryptRequest)` | `ciphertext_crc32c` |  |  |   
`[AsymmetricDecryptResponse](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.AsymmetricDecryptResponse)` |  | `plaintext_crc32c` | `verified_ciphertext_crc32c` |   
  
### Decapsulate

API | Server-side input verification | Client-side resource verification | Client-side output verification | Client-side verification of server-side input  
---|---|---|---|---  
`[DecapsulateRequest](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.DecapsulateRequest)` | `ciphertext_crc32c` |  |  |   
`[DecapsulateResponse](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.DecapsulateResponse)` |  | `shared_secret_crc32c` | `verified_ciphertext_crc32c` |   
  
### PublicKey

API | Server-side input verification | Client-side resource verification | Client-side output verification | Client-side verification of server-side input  
---|---|---|---|---  
`[PublicKey](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.PublicKey)` |  | `name` | `pem_crc32c, public_key.crc32c_checksum` |   
  
### MacSign

API | Server-side input verification | Client-side resource verification | Client-side output verification | Client-side verification of server-side input  
---|---|---|---|---  
`[MacSignRequest](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.MacSignRequest)` | `data_crc32c` |  |  |   
`[MacSignResponse](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.MacSignResponse)` |  | `mac_crc32c` | `verified_data_crc32c` |   
  
### MacVerify

API | Server-side input verification | Client-side resource verification | Client-side output verification | Client-side verification of server-side input  
---|---|---|---|---  
`[MacVerifyRequest](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.MacVerifyRequest)` | `data_crc32c` | `mac_crc32c` |  |  |   
`[MacVerifyResponse](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.MacVerifyResponse)` |  | `verified_data_crc32c` | `verified_mac_crc32c` | `verified_success_integrity` |   
  
## What's next

  * Learn more about [symmetric](https://docs.cloud.google.com/kms/docs/encrypt-decrypt) and [asymmetric](https://docs.cloud.google.com/kms/docs/encrypt-decrypt-rsa) encryption
  * Learn more about [encrypting application data](https://docs.cloud.google.com/kms/docs/encrypting-application-data)
  * Use [Cloud Audit Logs](https://docs.cloud.google.com/kms/docs/audit-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
