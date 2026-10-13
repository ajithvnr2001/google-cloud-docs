---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.Policy
title: Class Policy (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:40.965372+00:00
---

# Class Policy (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.Policy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Policy (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 
    
    
    Policy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Data for an IAM policy.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Immutable. The resource name of the `Policy`, which must be unique. Format: `policies/{attachment_point}/denypolicies/{policy_id}` The attachment point is identified by its URL-encoded full resource name, which means that the forward-slash character, `/`, must be written as `%2F`. For example, `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies/my-deny-policy`. For organizations and folders, use the numeric ID in the full resource name. For projects, requests can use the alphanumeric or the numeric ID. Responses always contain the numeric ID.   
`uid` |  `str`   
Immutable. The globally unique ID of the `Policy`. Assigned automatically when the `Policy` is created.   
`kind` |  `str`   
Output only. The kind of the `Policy`. Always contains the value `DenyPolicy`.   
`display_name` |  `str`   
A user-specified description of the `Policy`. This value can be up to 63 characters.   
`annotations` |  `MutableMapping[str, str]`   
A key-value map to store arbitrary metadata for the `Policy`. Keys can be up to 63 characters. Values can be up to 255 characters.   
`etag` |  `str`   
An opaque tag that identifies the current version of the `Policy`. IAM uses this value to help manage concurrent updates, so they do not cause one update to be overwritten by another. If this field is present in a [CreatePolicy][] request, the value is ignored.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the `Policy` was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the `Policy` was last updated.   
`delete_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the `Policy` was deleted. Empty if the policy is not deleted.   
`rules` |  `MutableSequence[[google.cloud.iam_v2.types.PolicyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.PolicyRule)]`   
A list of rules that specify the behavior of the `Policy`. All of the rules should be of the `kind` specified in the `Policy`.   
`managing_authority` |  `str`   
Immutable. Specifies that this policy is managed by an authority and can only be modified by that authority. Usage is restricted.   
  
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
