---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-add-hashing-algorithm/
title: Apply a hashing algorithm \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:30.427595+00:00
---

# Apply a hashing algorithm  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-add-hashing-algorithm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Apply a hashing algorithm Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to apply a hashing algorithm to column values when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio.

In Wrangler, you can apply a hashing algorithm, such as SHA, to a column of values. The result is a unique, fixed-length string called the _hash value_ or _message digest_.

When you apply the `hash` directive to a string column, Wrangler replaces the content of the column with the message digest. No new columns are created when you apply the `hash` directive.

You can choose to encode the message digest. If you encode the message digest, Wrangler encodes the values in the column as `hex` with left-padding zeros.

Cloud Data Fusion supports he following hashing algorithms in the Wrangler workspace:

  * BLAKE2B-160
  * BLAKE2B-256
  * BLAKE2B-384
  * BLAKE2B-512
  * GOST3411
  * GOST3411-2012-256
  * GOST3411-2012-512
  * KECCAK-224
  * KECCAK-256
  * KECCAK-288
  * KECCAK-384
  * KECCAK-512
  * MD2
  * MD4
  * MD5
  * RIPEMD128
  * RIPEMD160
  * RIPEMD256
  * RIPEMD320
  * SHA
  * SHA-1
  * SHA-224
  * SHA-256
  * SHA-384
  * SHA-512
  * SHA-512/224
  * SHA-512/256
  * SHA3-224
  * SHA3-256
  * SHA3-384
  * SHA3-512
  * Skein-1024-1024
  * Skein-1024-384
  * Skein-1024-512
  * Skein-256-128
  * Skein-256-160
  * Skein-256-224
  * Skein-256-256
  * Skein-512-128
  * Skein-512-160
  * Skein-512-224
  * Skein-512-256
  * Skein-512-384
  * Skein-512-512
  * SM3
  * Tiger
  * WHIRLPOOL



## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
