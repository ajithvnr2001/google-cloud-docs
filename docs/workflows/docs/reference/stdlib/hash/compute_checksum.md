---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/hash/compute_checksum/
title: Function: hash.compute_checksum \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:02.769033+00:00
---

# Function: hash.compute_checksum  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/hash/compute_checksum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: hash.compute_checksum Stay organized with collections  Save and categorize content based on your preferences. 

Computes checksum using a given hashing algorithm.

## Arguments

Arguments  
---  
`data` |  `bytes` The input to compute checksum for.  
`algorithm` |  `string` The hashing algorithm to use. Supported algorithms: `MD5`, `SHA1`, `SHA224`, `SHA256`, `SHA384`, `SHA512`.  
  
## Returns

The computed checksum in bytes.

## Raised exceptions

Exceptions  
---  
`TypeError` | If `data` is not in bytes, or if `algorithm` is not a string.  
`ValueError` | If the provided hashing algorithm is not supported.  
  
## Examples

For more information, see [Returning bytes](https://cloud.google.com/workflows/docs/reference/syntax/datatypes.md#bytes).
    
    
    # Compute SHA-256 checksum of a message (bytes) and return it as a Base64 string
    - assignStep:
        assign:
          - dataBytes: ${text.encode("Hello World", "UTF-8")}
          - algorithmName: "SHA256"
          # Compute SHA-256 checksum of data in bytes
          - checksum: ${hash.compute_checksum(dataBytes, algorithmName)}
    - returnStep:
        # Return checksum encoded to Base64 string: "pZGm1Av0IEBKARczz7exkNYsZb8LzaMrV7J32a2fFG4="
        return: ${base64.encode(checksum)}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
