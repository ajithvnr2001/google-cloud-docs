---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/hash/compute_hmac/
title: Function: hash.compute_hmac \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:04.480092+00:00
---

# Function: hash.compute_hmac  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/hash/compute_hmac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: hash.compute_hmac Stay organized with collections  Save and categorize content based on your preferences. 

Computes the hash-based message authentication code (HMAC) for data given a secret key and hashing algorithm.

## Arguments

Arguments  
---  
`key` |  `bytes` The secret key to use when computing HMAC hash.  
`data` |  `bytes` The input to compute HMAC for.  
`algorithm` |  `string` The hashing algorithm to use when computing HMAC hash. Supported algorithms: `MD5`, `SHA1`, `SHA224`, `SHA256`, `SHA384`, `SHA512`.  
  
## Returns

The computed HMAC hash in bytes.

## Raised exceptions

Exceptions  
---  
`TypeError` | If `key` and `data` are not in bytes, or if `algorithm` is not a string.  
`ValueError` | If the provided hashing algorithm is not supported.  
  
## Examples

For more information, see [Returning bytes](https://cloud.google.com/workflows/docs/reference/syntax/datatypes.md#bytes).
    
    
    # Compute HMAC SHA-256 hash for message (bytes) using a secret key (bytes)
    - assignStep:
        assign:
          - keyBytes: ${text.encode("key", "UTF-8")}
          - dataBytes: ${text.encode("Hello World", "UTF-8")}
          - algorithmName: "SHA256"
          # Compute HMAC SHA-256 hash for data in bytes
          - hmac: ${hash.compute_hmac(keyBytes, dataBytes, algorithmName)}
    - returnStep:
        # Return HMAC encoded to Base64 string: "QidPcoCDkuWLV9co1+PA5RY+rwfRZdwDEF9iq74afRE="
        return: ${base64.encode(hmac)}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
