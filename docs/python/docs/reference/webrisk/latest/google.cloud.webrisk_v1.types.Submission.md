---
url: https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.Submission
title: Class Submission (1.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:51.285744+00:00
---

# Class Submission (1.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.Submission

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Submission (1.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.23.0 (latest)  1.22.0  1.21.0  1.20.0  1.19.0  1.18.1  1.17.0  1.16.0  1.15.1  1.14.5  1.13.0  1.12.1  1.11.1  1.10.1  1.9.0  1.8.4  1.7.2  1.6.1  1.5.0  1.4.3  1.3.0  1.2.0  1.1.0  1.0.1  0.3.3  0.2.0 
    
    
    Submission(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Wraps a URI that might be displaying malicious content.

## Attributes  
  
---  
**Name** | **Description**  
`uri` |  `str`   
Required. The URI that is being reported for malicious content to be analyzed.   
`threat_types` |  `MutableSequence[[google.cloud.webrisk_v1.types.ThreatType](https://docs.cloud.google.com/python/docs/reference/webrisk/latest/google.cloud.webrisk_v1.types.ThreatType)]`   
Output only. ThreatTypes found to be associated with the submitted URI after reviewing it. This might be empty if the URI was not added to any list.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
