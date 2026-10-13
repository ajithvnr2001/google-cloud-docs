---
url: https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1.types.Xxe
title: Class Xxe (1.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:35.412820+00:00
---

# Class Xxe (1.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1.types.Xxe

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Xxe (1.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.22.0 (latest)  1.21.0  1.20.0  1.19.0  1.18.0  1.17.2  1.16.0  1.15.1  1.14.5  1.13.0  1.12.2  1.11.1  1.10.0  1.9.2  1.8.3  1.7.2  1.6.1  1.5.0  1.4.3  1.3.0  1.2.0  1.1.0  1.0.0  0.4.2  0.3.0 
    
    
    Xxe(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Information reported for an XXE.

## Attributes  
  
---  
**Name** | **Description**  
`payload_value` |  `str`   
The XML string that triggered the XXE vulnerability. Non-payload values might be redacted.   
`payload_location` |  `[google.cloud.websecurityscanner_v1.types.Xxe.Location](https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1.types.Xxe.Location)`   
Location within the request where the payload was placed.   
  
## Classes 

### Location
    
    
    Location(value)

Locations within a request where XML was substituted.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
