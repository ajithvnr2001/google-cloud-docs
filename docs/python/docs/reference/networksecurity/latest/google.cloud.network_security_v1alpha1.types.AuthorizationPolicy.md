---
url: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.AuthorizationPolicy
title: Class AuthorizationPolicy (0.13.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:29.695996+00:00
---

# Class AuthorizationPolicy (0.13.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.AuthorizationPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AuthorizationPolicy (0.13.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.4 (latest)  0.13.3  0.12.0  0.11.0  0.10.0  0.9.21  0.8.0  0.7.2  0.6.1  0.5.0  0.4.2  0.3.2  0.2.0  0.1.5 
    
    
    AuthorizationPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

AuthorizationPolicy is a resource that specifies how a server should authorize incoming connections. This resource in itself does not change the configuration unless it's attached to a target https proxy or endpoint config selector resource.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. Name of the AuthorizationPolicy resource. It matches pattern `projects/{project}/locations/{location}/authorizationPolicies/`.   
`description` |  `str`   
Optional. Free-text description of the resource.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the resource was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the resource was updated.   
`labels` |  `MutableMapping[str, str]`   
Optional. Set of label tags associated with the AuthorizationPolicy resource.   
`action` |  `[google.cloud.network_security_v1alpha1.types.AuthorizationPolicy.Action](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.AuthorizationPolicy.Action)`   
Required. The action to take when a rule match is found. Possible values are "ALLOW" or "DENY".   
`rules` |  `MutableSequence[[google.cloud.network_security_v1alpha1.types.AuthorizationPolicy.Rule](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.AuthorizationPolicy.Rule)]`   
Optional. List of rules to match. Note that at least one of the rules must match in order for the action specified in the 'action' field to be taken. A rule is a match if there is a matching source and destination. If left blank, the action specified in the `action` field will be applied on every request.   
  
## Classes 

### Action
    
    
    Action(value)

Possible values that define what action to take.

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
  
### Rule
    
    
    Rule(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specification of rules.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
