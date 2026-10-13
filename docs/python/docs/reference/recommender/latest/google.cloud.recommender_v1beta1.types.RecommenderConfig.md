---
url: https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1beta1.types.RecommenderConfig
title: Class RecommenderConfig (2.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:10.435900+00:00
---

# Class RecommenderConfig (2.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1beta1.types.RecommenderConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RecommenderConfig (2.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.23.0 (latest)  2.22.0  2.21.0  2.20.0  2.19.0  2.18.2  2.17.0  2.16.1  2.15.5  2.14.0  2.13.0  2.12.0  2.11.2  2.10.1  2.9.0  2.8.3  2.7.4  2.6.0  2.5.1  2.4.0  2.3.4  2.2.0  2.1.0  2.0.0  1.1.3  1.0.0  0.3.0  0.2.0  0.1.0 
    
    
    RecommenderConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for a Recommender.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Name of recommender config. Eg, projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config   
`recommender_generation_config` |  `[google.cloud.recommender_v1beta1.types.RecommenderGenerationConfig](https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1beta1.types.RecommenderGenerationConfig)`   
RecommenderGenerationConfig which configures the Generation of recommendations for this recommender.   
`etag` |  `str`   
Fingerprint of the RecommenderConfig. Provides optimistic locking when updating.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Last time when the config was updated.   
`revision_id` |  `str`   
Output only. Immutable. The revision ID of the config. A new revision is committed whenever the config is changed in any way. The format is an 8-character hexadecimal string.   
`annotations` |  `MutableMapping[str, str]`   
Allows clients to store small amounts of arbitrary data. Annotations must follow the Kubernetes syntax. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (\\_), dots (.), and alphanumerics between.   
`display_name` |  `str`   
A user-settable field to provide a human-readable name to be used in user interfaces.   
  
## Classes 

### AnnotationsEntry
    
    
    AnnotationsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
