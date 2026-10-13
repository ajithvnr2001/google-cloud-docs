---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest
title: Class GenerateGroundedContentRequest (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:10.165524+00:00
---

# Class GenerateGroundedContentRequest (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GenerateGroundedContentRequest (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    GenerateGroundedContentRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Top-level message sent by the client for the `GenerateGroundedContent` method.

## Attributes  
  
---  
**Name** | **Description**  
`location` |  `str`   
Required. Location resource. Format: `projects/{project}/locations/{location}`.   
`system_instruction` |  `[google.cloud.discoveryengine_v1beta.types.GroundedGenerationContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GroundedGenerationContent)`   
Content of the system instruction for the current API. These instructions will take priority over any other prompt instructions if the selected model is supporting them.   
`contents` |  `MutableSequence[[google.cloud.discoveryengine_v1beta.types.GroundedGenerationContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GroundedGenerationContent)]`   
Content of the current conversation with the model. For single-turn queries, this is a single instance. For multi-turn queries, this is a repeated field that contains conversation history + latest request.   
`generation_spec` |  `[google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GenerationSpec)`   
Content generation specification.   
`grounding_spec` |  `[google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GroundingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GroundingSpec)`   
Grounding specification.   
`user_labels` |  `MutableMapping[str, str]`   
The user labels applied to a resource must meet the following requirements: \- Each resource can have multiple labels, up to a maximum of 64\. \- Each label must be a key-value pair. \- Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters. \- Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed. \- The key portion of a label must be unique. However, you can use the same key with multiple resources. \- Keys must start with a lowercase letter or international character. See `Google Cloud Document   
  
## Classes 

### DynamicRetrievalConfiguration
    
    
    DynamicRetrievalConfiguration(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Describes the options to customize dynamic retrieval.

### GenerationSpec
    
    
    GenerationSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Content generation specification.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### GroundingSource
    
    
    GroundingSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Grounding source.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### GroundingSpec
    
    
    GroundingSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Grounding specification.

### UserLabelsEntry
    
    
    UserLabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
