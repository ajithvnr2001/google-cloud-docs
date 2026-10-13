---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm
title: Google Cloud Key Management Service v1 API - Enum CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:01.096626+00:00
---

# Google Cloud Key Management Service v1 API - Enum CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Enum CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public enum CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm

Reference documentation and code samples for the Google Cloud Key Management Service v1 API enum CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.

The algorithm of the [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion], indicating what parameters must be used for each cryptographic operation.

The [GOOGLE_SYMMETRIC_ENCRYPTION][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.GOOGLE_SYMMETRIC_ENCRYPTION] algorithm is usable with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT].

Algorithms beginning with `RSA_SIGN_` are usable with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] [ASYMMETRIC_SIGN][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ASYMMETRIC_SIGN].

The fields in the name after `RSA_SIGN_` correspond to the following parameters: padding algorithm, modulus bit length, and digest algorithm.

For PSS, the salt length used is equal to the length of digest algorithm. For example, [RSA_SIGN_PSS_2048_SHA256][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.RSA_SIGN_PSS_2048_SHA256] will use PSS with a salt length of 256 bits or 32 bytes.

Algorithms beginning with `RSA_DECRYPT_` are usable with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] [ASYMMETRIC_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ASYMMETRIC_DECRYPT].

The fields in the name after `RSA_DECRYPT_` correspond to the following parameters: padding algorithm, modulus bit length, and digest algorithm.

Algorithms beginning with `EC_SIGN_` are usable with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] [ASYMMETRIC_SIGN][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ASYMMETRIC_SIGN].

The fields in the name after `EC_SIGN_` correspond to the following parameters: elliptic curve, digest algorithm.

Algorithms beginning with `HMAC_` are usable with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] [MAC][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.MAC].

The suffix following `HMAC_` corresponds to the hash algorithm being used (eg. SHA256).

Algorithms beginning with `PQ_` are post-quantum.

For more information, see [Key purposes and algorithms](https://cloud.google.com/kms/docs/algorithms).

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`Aes128Cbc` | AES-CBC (Cipher Block Chaining Mode) using 128-bit keys.  
`Aes128Ctr` | AES-CTR (Counter Mode) using 128-bit keys.  
`Aes128Gcm` | AES-GCM (Galois Counter Mode) using 128-bit keys.  
`Aes256Cbc` | AES-CBC (Cipher Block Chaining Mode) using 256-bit keys.  
`Aes256Ctr` | AES-CTR (Counter Mode) using 256-bit keys.  
`Aes256Gcm` | AES-GCM (Galois Counter Mode) using 256-bit keys.  
`Aes256Kwp` | AES key wrap with zero padding algorithm (RFC 5649). Can only be used by keys with purpose AES_WRAPPING.  
`EcSignEd25519` | EdDSA on the Curve25519 in pure mode (taking data as input).  
`EcSignP256Sha256` | ECDSA on the NIST P-256 curve with a SHA256 digest. Other hash functions can also be used: <https://cloud.google.com/kms/docs/create-validate-signatures#ecdsa_support_for_other_hash_algorithms>  
`EcSignP384Sha384` | ECDSA on the NIST P-384 curve with a SHA384 digest. Other hash functions can also be used: <https://cloud.google.com/kms/docs/create-validate-signatures#ecdsa_support_for_other_hash_algorithms>  
`EcSignSecp256K1Sha256` | ECDSA on the non-NIST secp256k1 curve. This curve is only supported for HSM protection level. Other hash functions can also be used: <https://cloud.google.com/kms/docs/create-validate-signatures#ecdsa_support_for_other_hash_algorithms>  
`ExternalSymmetricEncryption` | Algorithm representing symmetric encryption by an external key manager.  
`GoogleSymmetricEncryption` | Creates symmetric encryption keys.  
`HmacSha1` | HMAC-SHA1 signing with a 160 bit key.  
`HmacSha224` | HMAC-SHA224 signing with a 224 bit key.  
`HmacSha256` | HMAC-SHA256 signing with a 256 bit key.  
`HmacSha384` | HMAC-SHA384 signing with a 384 bit key.  
`HmacSha512` | HMAC-SHA512 signing with a 512 bit key.  
`KemXwing` | X-Wing hybrid KEM combining ML-KEM-768 with X25519 following datatracker.ietf.org/doc/draft-connolly-cfrg-xwing-kem/.  
`MlKem1024` | ML-KEM-1024 (FIPS 203)  
`MlKem768` | ML-KEM-768 (FIPS 203)  
`PqSignHashSlhDsaSha2128SSha256` | The post-quantum stateless hash-based digital signature algorithm, at security level 1. Randomized pre-hash version supporting SHA256 digests.  
`PqSignMlDsa44` | The post-quantum Module-Lattice-Based Digital Signature Algorithm, at security level 1. Randomized version.  
`PqSignMlDsa44ExternalMu` | The post-quantum Module-Lattice-Based Digital Signature Algorithm, at security level 1. Randomized version supporting externally-computed message representatives.  
`PqSignMlDsa65` | The post-quantum Module-Lattice-Based Digital Signature Algorithm, at security level 3. Randomized version.  
`PqSignMlDsa65ExternalMu` | The post-quantum Module-Lattice-Based Digital Signature Algorithm, at security level 3. Randomized version supporting externally-computed message representatives.  
`PqSignMlDsa87` | The post-quantum Module-Lattice-Based Digital Signature Algorithm, at security level 5. Randomized version.  
`PqSignMlDsa87ExternalMu` | The post-quantum Module-Lattice-Based Digital Signature Algorithm, at security level 5. Randomized version supporting externally-computed message representatives.  
`PqSignSlhDsaSha2128S` | The post-quantum stateless hash-based digital signature algorithm, at security level 1. Randomized version.  
`RsaDecryptOaep2048Sha1` | RSAES-OAEP 2048 bit key with a SHA1 digest.  
`RsaDecryptOaep2048Sha256` | RSAES-OAEP 2048 bit key with a SHA256 digest.  
`RsaDecryptOaep3072Sha1` | RSAES-OAEP 3072 bit key with a SHA1 digest.  
`RsaDecryptOaep3072Sha256` | RSAES-OAEP 3072 bit key with a SHA256 digest.  
`RsaDecryptOaep4096Sha1` | RSAES-OAEP 4096 bit key with a SHA1 digest.  
`RsaDecryptOaep4096Sha256` | RSAES-OAEP 4096 bit key with a SHA256 digest.  
`RsaDecryptOaep4096Sha512` | RSAES-OAEP 4096 bit key with a SHA512 digest.  
`RsaSignPkcs12048Sha256` | RSASSA-PKCS1-v1_5 with a 2048 bit key and a SHA256 digest.  
`RsaSignPkcs13072Sha256` | RSASSA-PKCS1-v1_5 with a 3072 bit key and a SHA256 digest.  
`RsaSignPkcs14096Sha256` | RSASSA-PKCS1-v1_5 with a 4096 bit key and a SHA256 digest.  
`RsaSignPkcs14096Sha512` | RSASSA-PKCS1-v1_5 with a 4096 bit key and a SHA512 digest.  
`RsaSignPss2048Sha256` | RSASSA-PSS 2048 bit key with a SHA256 digest.  
`RsaSignPss3072Sha256` | RSASSA-PSS 3072 bit key with a SHA256 digest.  
`RsaSignPss4096Sha256` | RSASSA-PSS 4096 bit key with a SHA256 digest.  
`RsaSignPss4096Sha512` | RSASSA-PSS 4096 bit key with a SHA512 digest.  
`RsaSignRawPkcs12048` | RSASSA-PKCS1-v1_5 signing without encoding, with a 2048 bit key.  
`RsaSignRawPkcs13072` | RSASSA-PKCS1-v1_5 signing without encoding, with a 3072 bit key.  
`RsaSignRawPkcs14096` | RSASSA-PKCS1-v1_5 signing without encoding, with a 4096 bit key.  
`Unspecified` | Not specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
