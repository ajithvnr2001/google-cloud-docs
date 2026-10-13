---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Conversation
title: Class Conversation (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:50.588975+00:00
---

# Class Conversation (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Conversation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Conversation (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    Conversation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message for a conversation.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Optional. Identifier. The unique resource name of a conversation. Format: `projects/{project}/locations/{location}/conversations/{conversation_id}` `{conversation_id}` is the resource id and should be 63 characters or less and must match the format described in https://google.aip.dev/122#resource-id-segments Example: `projects/1234567890/locations/global/conversations/my-conversation`. It is recommended to skip setting this field during conversation creation as it will be inferred automatically and overwritten with the {parent}/conversations/{conversation_id}.   
`agents` |  `MutableSequence[str]`   
Required. Agent(s) in the conversation. Currently, only one agent is supported. This field is repeated to allow for future support of multiple agents in a conversation. Format: `projects/{project}/locations/{location}/dataAgents/{agent}`  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Creation timestamp.   
`last_used_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp of the last used conversation.   
`labels` |  `MutableMapping[str, str]`   
Optional. Open-ended and user-defined labels that can be set by the client to tag a conversation (e.g. to filter conversations for specific surfaces/products).   
`title` |  `str`   
Optional. The display name for the conversation (max 63 chars).   
`kms_key` |  `str`   
Optional. Customer managed encryption key (CMEK) to use for encrypting the Conversation resources. Encryption will happen at Titan layer, we will pass the KMS key to Titan. Format: projects/{project_id}/locations/{location}/keyRings/{key_ring_name}/cryptoKeys/{key_name}. This field is a member of `oneof`_ `_kms_key`.   
  
## Classes 

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
