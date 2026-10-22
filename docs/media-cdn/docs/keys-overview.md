---
url: https://docs.cloud.google.com/media-cdn/docs/keys-overview/
title: Keys overview \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:40.840711+00:00
---

# Keys overview  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/keys-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Keys overview Stay organized with collections  Save and categorize content based on your preferences. 

Media CDN uses cryptographic key pairs when signing requests. Media CDN uses a _keyset_ to store key pairs that are actively used to sign requests. You can have up to three public keys and three validation shared keys, for a total of six keys per keyset.

You can also remove unused keys from a keyset. Adding and removing a key is typically called _secret rotation_. Secret rotation lets you do the following:

  * Safely add new secrets to a keyset by appending them to the keyset.
  * Generate tokens with the corresponding secret.
  * Remove old secrets after the oldest possible token expires.

For example, say that you set your short-duration tokens to expire after one hour. Then, you'd remove the oldest secret used for the short-duration tokens after new requests serve users for one or more hours.




Before removing an unused secret, verify that it's not referenced or fetched to sign user requests on your application server. Prematurely removing a secret from a keyset prevents Media CDN from validating requests associated with that secret. Affected users are served an `HTTP 403 Forbidden` response.

To optimize performance, reliability, and cost of simultaneous accesses to Secret Manager, your shared validation key secrets are cached for up to one hour. Secret caching may result in continued token access after a secret is deleted from Secret Manager for up to one hour.

As a best practice, rotate keys regularly.

## Known limitations

Media CDN rejects requests that are signed with the symmetric signatures used by Cloud CDN with an `HTTP 403` response. Media CDN currently supports symmetric keys with requests using the token format and keys referenced by Media CDN.

Asymmetric keys must be generated as Ed25519 pairs, with a 512-bit (64-byte) private key, and a 256-bit (32-byte) public key. The [Tink library](https://github.com/google/tink) has support for key generation, signing, and validating Ed25519 signatures with C++, Go, Java, and Objective-C.

Asymmetric keys must have the following characteristics:

  * Be base64-encoded with a length of 44 bytes (padded) or 43 bytes (unpadded). Both padded and unpadded forms of base64 are accepted.

  * The public key must be encoded in [URL-safe base64 format](https://tools.ietf.org/html/rfc4648#section-5). The private key may be encoded in [standard base64 format](https://tools.ietf.org/html/rfc4648#section-4).

  * Have a matching private key.




# What's next?

  * [Create keys](https://docs.cloud.google.com/media-cdn/docs/create-keys)
  * [Create a keyset](https://docs.cloud.google.com/media-cdn/docs/create-keyset)
  * [Rotate secrets](https://docs.cloud.google.com/media-cdn/docs/rotate-secrets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
