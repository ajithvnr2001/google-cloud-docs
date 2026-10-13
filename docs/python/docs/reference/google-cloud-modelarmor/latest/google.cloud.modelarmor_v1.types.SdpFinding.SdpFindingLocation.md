---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpFinding.SdpFindingLocation
title: Class SdpFindingLocation (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:03.310870+00:00
---

# Class SdpFindingLocation (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpFinding.SdpFindingLocation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SdpFindingLocation (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 
    
    
    SdpFindingLocation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Location of this Sensitive Data Protection Finding within input content.

## Attributes  
  
---  
**Name** | **Description**  
`byte_range` |  `[google.cloud.modelarmor_v1.types.RangeInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RangeInfo)`   
Zero-based byte offsets delimiting the finding. These are relative to the finding's containing element. Note that when the content is not textual, this references the UTF-8 encoded textual representation of the content. Note: Omitted if content is an image.   
`codepoint_range` |  `[google.cloud.modelarmor_v1.types.RangeInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RangeInfo)`   
Unicode character offsets delimiting the finding. These are relative to the finding's containing element. Provided when the content is text. Note: Omitted if content is an image.   
`content_locations` |  `MutableSequence[[google.cloud.modelarmor_v1.types.SdpContentLocation](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SdpContentLocation)]`   
List of nested objects pointing to the precise location of the finding within an image, file or record. For example, a single finding might be detected in two separate bounding boxes within an image (e.g., if it wraps across a line or is partially obscured). In such cases, content_locations would contain two SdpContentLocation entries, each with an image_finding_location pointing to a different bounding box.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
