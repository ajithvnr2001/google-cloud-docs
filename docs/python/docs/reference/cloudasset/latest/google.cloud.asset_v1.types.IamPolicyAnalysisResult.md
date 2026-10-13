---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisResult
title: Class IamPolicyAnalysisResult (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:28.887586+00:00
---

# Class IamPolicyAnalysisResult (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class IamPolicyAnalysisResult (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 
    
    
    IamPolicyAnalysisResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

IAM Policy analysis result, consisting of one IAM policy binding and derived access control lists.

## Attributes  
  
---  
**Name** | **Description**  
`attached_resource_full_name` |  `str`   
The `full resource name   
`iam_binding` |  `google.iam.v1.policy_pb2.Binding`   
The IAM policy binding under analysis.   
`access_control_lists` |  `MutableSequence[[google.cloud.asset_v1.types.IamPolicyAnalysisResult.AccessControlList](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisResult.AccessControlList)]`   
The access control lists derived from the iam_binding that match or potentially match resource and access selectors specified in the request.   
`identity_list` |  `[google.cloud.asset_v1.types.IamPolicyAnalysisResult.IdentityList](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisResult.IdentityList)`   
The identity list derived from members of the iam_binding that match or potentially match identity selector specified in the request.   
`fully_explored` |  `bool`   
Represents whether all analyses on the iam_binding have successfully finished.   
  
## Classes 

### Access
    
    
    Access(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An IAM role or permission under analysis.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### AccessControlList
    
    
    AccessControlList(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An access control list, derived from the above IAM policy binding, which contains a set of resources and accesses. May include one item from each set to compose an access control entry.

NOTICE that there could be multiple access control lists for one IAM policy binding. The access control lists are created based on resource and access combinations.

For example, assume we have the following cases in one IAM policy binding:

  * Permission P1 and P2 apply to resource R1 and R2;
  * Permission P3 applies to resource R2 and R3;



This will result in the following access control lists:

  * AccessControlList 1: [R1, R2], [P1, P2]
  * AccessControlList 2: [R2, R3], [P3]



### Edge
    
    
    Edge(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A directional edge.

### Identity
    
    
    Identity(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An identity under analysis.

### IdentityList
    
    
    IdentityList(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The identities and group edges.

### Resource
    
    
    Resource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A Google Cloud resource under analysis.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
