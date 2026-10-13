---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.AccessPolicy
title: Class AccessPolicy (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:21.196918+00:00
---

# Class AccessPolicy (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.AccessPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AccessPolicy (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 
    
    
    AccessPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An IAM access policy resource.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name of the access policy. The following formats are supported: \- `projects/{project_id}/locations/{location}/accessPolicies/{policy_id}` \- `projects/{project_number}/locations/{location}/accessPolicies/{policy_id}` \- `folders/{folder_id}/locations/{location}/accessPolicies/{policy_id}` \- `organizations/{organization_id}/locations/{location}/accessPolicies/{policy_id}`  
`uid` |  `str`   
Output only. The globally unique ID of the access policy.   
`etag` |  `str`   
Optional. The etag for the access policy. If this is provided on update, it must match the server's etag.   
`display_name` |  `str`   
Optional. The description of the access policy. Must be less than or equal to 63 characters.   
`annotations` |  `MutableMapping[str, str]`   
Optional. User defined annotations. See https://google.aip.dev/148#annotations for more details such as format and size limitations   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the access policy was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the access policy was most recently updated.   
`details` |  `[google.cloud.iam_v3beta.types.AccessPolicyDetails](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.AccessPolicyDetails)`   
Optional. The details for the access policy.   
  
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
