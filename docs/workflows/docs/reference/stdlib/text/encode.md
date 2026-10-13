---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/encode/
title: Function: text.encode \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:24.979931+00:00
---

# Function: text.encode  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/encode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: text.encode Stay organized with collections  Save and categorize content based on your preferences. 

Encodes given text to bytes, using the specified character set.

## Arguments

Arguments  
---  
`text` |  `string` The input to be encoded.  
`charset` |  `string` The IANA charset name; e.g. `UTF-8`, `US-ASCII`, `ISO-8859-2`. Case-insensitive. Default: `UTF-8`.  
  
## Returns

The encoded bytes.

## Raised exceptions

Exceptions  
---  
`ValueError` | If the charset is unsupported, or if the text contains codepoints that are not representable in the specified charset.  
  
## Examples
    
    
    # Return Base64 text "SGVsbG8gV29ybGQ=" using `text.encode` function
    - assignStep:
        assign:
          # Encode string to bytes
          - encodedBytes: ${text.encode("Hello World","UTF-8")}
    - returnStep:
        # Encode bytes to Base64 text
        return: ${base64.encode(encodedBytes)}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
