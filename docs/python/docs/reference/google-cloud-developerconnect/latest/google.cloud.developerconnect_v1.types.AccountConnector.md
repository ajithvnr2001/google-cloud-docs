---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AccountConnector
title: Class AccountConnector (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:28.665033+00:00
---

# Class AccountConnector (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AccountConnector

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AccountConnector (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    AccountConnector(mapping=None, *, ignore_unknown_fields=False, **kwargs)

AccountConnector encapsulates what a platform administrator needs to configure for users to connect to the service providers, which includes, among other fields, the OAuth client ID, client secret, and authorization and token endpoints.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`provider_oauth_config` |  `[google.cloud.developerconnect_v1.types.ProviderOAuthConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ProviderOAuthConfig)`   
Optional. Provider OAuth config. This field is a member of `oneof`_ `account_connector_config`.   
`name` |  `str`   
Identifier. The resource name of the accountConnector, in the format `projects/{project}/locations/{location}/accountConnectors/{account_connector_id}`.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the accountConnector was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the accountConnector was updated.   
`annotations` |  `MutableMapping[str, str]`   
Optional. Allows users to store small amounts of arbitrary data.   
`etag` |  `str`   
Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels as key value pairs   
`oauth_start_uri` |  `str`   
Output only. Start OAuth flow by clicking on this URL.   
  
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
