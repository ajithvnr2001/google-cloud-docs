---
url: https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2.types.Comment
title: Class Comment (0.5.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:23.596043+00:00
---

# Class Comment (0.5.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2.types.Comment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Comment (0.5.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.4 (latest)  0.5.3  0.4.0  0.3.0  0.2.0  0.1.19 
    
    
    Comment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A comment associated with a support case.

Case comments are the primary way for Google Support to communicate with a user who has opened a case. When a user responds to Google Support, the user's responses also appear as comments.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Identifier. The resource name of the comment.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the comment was created.   
`creator` |  `[google.cloud.support_v2.types.Actor](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2.types.Actor)`   
Output only. The user or Google Support agent who created the comment.   
`body` |  `str`   
The full comment body. Maximum of 12800 characters.   
`plain_text_body` |  `str`   
Output only. DEPRECATED. DO NOT USE. A duplicate of the `body` field. This field is only present for legacy reasons.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
