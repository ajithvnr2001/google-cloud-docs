---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.CitationAnchor.TextMessageCitationAnchor
title: Class TextMessageCitationAnchor (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:49.926266+00:00
---

# Class TextMessageCitationAnchor (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.CitationAnchor.TextMessageCitationAnchor

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TextMessageCitationAnchor (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    TextMessageCitationAnchor(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Citation anchor within a TextMessage.

## Attributes  
  
---  
**Name** | **Description**  
`part_index` |  `int`   
Output only. The 0-based index of the part within the TextMessage.parts field.   
`start_offset_bytes` |  `int`   
Output only. The offset, measured in UTF-8 bytes, within the part string where the citation begins (inclusive). Example: For the text "Hello, world" where "world" is cited, the start offset bytes (inclusive) is 7 and the end offset bytes (exclusive) is 12.   
`end_offset_bytes` |  `int`   
Output only. The offset, measured in UTF-8 bytes, within the part string where the citation ends (exclusive). Example: For the text "Hello, world" where "world" is cited, the start offset bytes (inclusive) is 7 and the end offset bytes (exclusive) is 12.   
`source_ids` |  `MutableSequence[str]`   
Output only. The ids of the sources that are cited.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
