---
url: https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.EntityMentionData
title: Class EntityMentionData (1.28.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:43.860063+00:00
---

# Class EntityMentionData (1.28.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.EntityMentionData

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class EntityMentionData (1.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.28.0 (latest)  1.27.0  1.26.0  1.25.0  1.24.0  1.23.3  1.22.0  1.21.0  1.20.0  1.19.1  1.18.0  1.17.5  1.16.0  1.15.0  1.14.1  1.13.0  1.12.0  1.11.1  1.10.0  1.9.1  1.8.0  1.7.0  1.6.1  1.5.0  1.4.5  1.3.2  1.2.1  1.1.0  1.0.0  0.6.1  0.5.0  0.4.0  0.3.1  0.2.0  0.1.1 
    
    
    EntityMentionData(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The data for an entity mention annotation. This represents a mention of an `Entity` in the conversation.

## Attributes  
  
---  
**Name** | **Description**  
`entity_unique_id` |  `str`   
The key of this entity in conversation entities. Can be used to retrieve the exact `Entity` this mention is attached to.   
`type_` |  `[google.cloud.contact_center_insights_v1.types.EntityMentionData.MentionType](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.EntityMentionData.MentionType)`   
The type of the entity mention.   
`sentiment` |  `[google.cloud.contact_center_insights_v1.types.SentimentData](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.SentimentData)`   
Sentiment expressed for this mention of the entity.   
  
## Classes 

### MentionType
    
    
    MentionType(value)

The supported types of mentions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
