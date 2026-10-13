---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/decode/
title: Function: text.decode \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:24.438328+00:00
---

# Function: text.decode  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/decode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: text.decode Stay organized with collections  Save and categorize content based on your preferences. 

Decodes given data to string, assuming the specified character set.

Each byte that cannot be correctly decoded using the specified charset is represented in the output by the `\uFFFD` codepoint.

## Arguments

Arguments  
---  
`data` |  `bytes` The input to be decoded.  
`charset` |  `string` The IANA charset name; e.g. `UTF-8`, `US-ASCII`, `ISO-8859-2`. Case-insensitive. Default: `UTF-8`.  
  
## Returns

The decoded text.

## Raised exceptions

Exceptions  
---  
`ValueError` | If the charset is unsupported.  
  
## Examples
    
    
    # Return "Hello World" using `text.decode` function
    - assignStep:
        assign:
          # Assign Base64 text "Hello World"
          - base64Text: "SGVsbG8gV29ybGQ="
          # Decode Base64 text into bytes
          - decodedBytes: ${base64.decode(base64Text)}
    - returnStep:
        # Decode bytes to string
        return: ${text.decode(decodedBytes, "UTF-8")}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
