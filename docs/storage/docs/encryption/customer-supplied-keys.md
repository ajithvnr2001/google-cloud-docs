---
url: https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys/
title: Customer-supplied encryption keys \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:24.611976+00:00
---

# Customer-supplied encryption keys  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Customer-supplied encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

[Setup](https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys)

This page discusses customer-supplied encryption keys. For other encryption options, see [Data Encryption Options](https://docs.cloud.google.com/storage/docs/encryption).

## Overview

As an additional layer on top of [standard Cloud Storage encryption](https://docs.cloud.google.com/storage/docs/encryption/default-keys), you can choose to provide your own AES-256 encryption key, encoded in [standard Base64](https://datatracker.ietf.org/doc/html/rfc4648#section-4). This key is known as a _customer-supplied encryption key_. If you provide a customer-supplied encryption key, Cloud Storage does not permanently store your key in its servers or otherwise manage your key.

Instead, you provide your key for each Cloud Storage operation, and your key is purged from Cloud Storage servers after the operation is complete. Cloud Storage stores only a cryptographic hash of the key so that future requests can be validated against the hash. Your key cannot be recovered from this hash, and the hash cannot be used to decrypt your data.

We recommend you back up each key to a secure location and take precautions to ensure that your keys are not shared with untrusted parties. If any file or machine containing your encryption key is compromised, you should immediately [perform key rotation](https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#rotating) for all objects encrypted with the compromised key.

### When is the key used?

When you apply a customer-supplied encryption key to an object, Cloud Storage uses the key when encrypting:

  * The object's data.
  * The object's CRC32C checksum.
  * The object's MD5 hash.



Standard Cloud Storage encryption is used to encrypt the remaining [metadata](https://docs.cloud.google.com/storage/docs/metadata) for the object, including the object's name. This lets you read and update general metadata, as well as list, overwrite, and delete objects, without needing the customer-supplied encryption key. However, to perform any of these actions, you must have sufficient [permission](https://docs.cloud.google.com/storage/docs/access-control) to do so.

For example, if an object is encrypted with a customer-supplied encryption key, the key must be used to perform operations on the object such as downloading or moving it. If you attempt to read the object's metadata without providing the key, you receive metadata such as the object name and `Content-Type`, but not the object's CRC32C checksum or MD5 hash. If you do supply your key with the request for the object metadata, the object's CRC32C checksum and MD5 hash are included with the metadata.

**Note:** Because most metadata can be read regardless of encryption method, do not include sensitive information in your object and bucket metadata or names.

### Rewrite behavior

If you [rewrite](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) an object encrypted with a customer-supplied encryption key without supplying a key for encrypting the rewritten object, the following happens:

  * If you include an appropriate decryption key in the request, the rewritten object becomes encrypted using the destination bucket's [default Cloud Key Management Service encryption key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#set-default-key), or, in the absence of such a key, by [standard Cloud Storage encryption](https://docs.cloud.google.com/storage/docs/encryption/default-keys).

  * If you don't include an appropriate decryption key in your request, you receive an error.




### HTTPS check

To protect your data as it travels over the Internet during read and write operations, use Transport Layer Security, commonly known as TLS or HTTPS. TLS is required when you provide an encryption key. If you accidentally use your encryption key over an unencrypted (HTTP) connection, it is possible for an attacker to intercept your key. Because of this possibility, the Cloud Storage API returns an error message warning you that your key may be compromised. If this occurs, you should immediately [rotate your keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#rotating).

## Restrictions

The following restrictions apply when using customer-supplied encryption keys:

  * You cannot use the Google Cloud console to download objects that are encrypted with a customer-**supplied** encryption key. Similarly, when you use the Google Cloud console to upload an object, you cannot encrypt the object with a customer-**supplied** encryption key.

  * [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer) and [Cloud Dataflow](https://docs.cloud.google.com/dataflow) don't support objects encrypted with customer-supplied encryption keys.

  * You can only set customer-supplied encryption keys on individual objects. You cannot set a default customer-supplied encryption key for a bucket.

  * If you are performing a `compose` operation on objects encrypted by customer-supplied encryption keys, the component objects must be encrypted by the same key, and you need to provide the key with the compose request. The resulting composite object is encrypted by the same key.

  * When serving an object encrypted by a customer-supplied encryption key, Cloud Storage ignores [`Cache-Control` metadata](https://docs.cloud.google.com/storage/docs/metadata#cache-control) associated with the object and serves the object with `Cache-Control` set to `private, max-age=0`.




## Encryption keys with REST APIs

When you use a customer-supplied encryption key and work directly with the [JSON](https://docs.cloud.google.com/storage/docs/json_api) or [XML](https://docs.cloud.google.com/storage/docs/xml-api/overview) API, you must provide both the AES-256 key and a SHA256 hash of the key. You should store both the AES-256 key and the SHA256 hash of the key securely. Cloud Storage stores the SHA256 hash of your key in the object's metadata, where you can retrieve it later. This SHA256 hash cannot be used by Cloud Storage (or anyone else) to decrypt your data. It is stored as a way to uniquely identify the AES-256 key that was used to encrypt a particular object.

**Note:** Unlike typical [object listing with the JSON API](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list), list results for encrypted objects do not return the CRC32C or MD5 hashes of those objects, even if you supply the encryption key in the request.

#### Request headers

Include the following HTTP headers in your JSON or XML request:

Header name | Value | Description  
---|---|---  
`x-goog-encryption-algorithm` | string | The encryption algorithm to use. You must use the value `AES256`.  
`x-goog-encryption-key` | string | An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of your AES-256 encryption key.  
`x-goog-encryption-key-sha256` | string | An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of the SHA256 hash of your encryption key.  
  
If you are performing a [rewrite](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) operation with the JSON API, the headers listed above are used for encrypting the destination object, and the following headers are used for decrypting the source object:

Header name | Value | Description  
---|---|---  
`x-goog-copy-source-encryption-algorithm` | string | The encryption algorithm to use. You must use the value `AES256`.  
`x-goog-copy-source-encryption-key` | string | An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of the source object's AES-256 encryption key.  
`x-goog-copy-source-encryption-key-sha256` | string | An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of the SHA256 hash of the source object's encryption key.  
  
#### Response

### JSON

When using the JSON API, the metadata for a customer-supplied encryption key is returned in the response body, which includes the following properties:

Property name | Value | Description  
---|---|---  
`customerEncryption` | object | Information about the encryption used for the request.  
`customerEncryption.encryptionAlgorithm` | string | The encryption algorithm that was used. Always contains the value `AES256`.  
`customerEncryption.keySha256` | string | An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of the SHA256 hash of your encryption key. You can use this SHA256 hash to uniquely identify the AES-256 encryption key required to decrypt the object, which you must store securely.  
  
### XML

When using the XML API, the response includes the following headers:

Header name | Value | Description  
---|---|---  
`x-goog-encryption-algorithm` | string | The encryption algorithm that was used. Always contains the value `AES256`.  
`x-goog-encryption-key-sha256` | string | An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of the SHA256 hash of your encryption key. You can use this SHA256 hash to uniquely identify the AES-256 encryption key required to decrypt the object, which you must store securely.  
  
You receive an HTTP 400 error in the following cases:

  * You upload an object using a customer-supplied encryption key, and you attempt to perform another operation on the object (other than requesting or updating most metadata or deleting the object) without providing the key.
  * You upload an object using a customer-supplied encryption key, and you attempt to perform another operation on the object with an incorrect key.
  * You upload an object without providing a customer-supplied encryption key, and you attempt to perform another operation on the object with a customer-supplied encryption key.
  * You specify an encryption algorithm, key, or SHA256 hash that is not valid.



## Encryption keys with `gcloud storage`

The [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage) supports the use of customer-supplied encryption keys. When using the gcloud CLI with customer-supplied encryption keys, keep in mind the following:

  * The key specified as the encryption key is used in commands as both an encryption key and, when needed, as a decryption key.

  * You can optionally specify up to 100 decryption keys, which are used only to [decrypt objects](https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#download-decrypt).

  * When decrypting, the SHA256 hash of any supplied encryption and decryption keys is calculated, and the correct key to use for a particular object is selected by matching the SHA256 hash in the object's metadata.

  * When adding or [rotating](https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#rotating) a customer-supplied encryption key for an existing object, the object is rewritten as part of the request. This is true even for the [`gcloud storage objects update` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update).

  * List commands that can return the MD5 or CRC32C hash for objects encrypted with a customer-supplied key perform an additional metadata `GET` request for each such object. These additional requests can make listing substantially slower than listing objects encrypted with standard Cloud Storage encryption.

  * In situations where the encryption key can or does change during a partially-completed write or copy operation, such as when you re-run a `cp` upload after force quitting or encountering a network timeout, the operation restarts to ensure that the destination object is written with the new key.




## Encryption key rotation

If an object is encrypted using a customer-supplied encryption key, you can rotate the object's key by [rewriting the object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite). Rewrites are supported through the JSON API, but not the XML API. See [Rotating an encryption key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#rotating) for examples of key rotation.

**Note:** If your bucket uses [object versioning](https://docs.cloud.google.com/storage/docs/object-versioning), be sure to delete the noncurrent versions of your objects after you rotate the key. Noncurrent versions are not deleted automatically and remain encrypted with the old key.

## What's next

  * Learn how to [use customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys).
  * [Configure which encryption methods are allowed or restricted](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in your buckets.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
