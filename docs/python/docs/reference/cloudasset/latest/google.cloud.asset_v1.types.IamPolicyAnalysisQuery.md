---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery
title: Class IamPolicyAnalysisQuery (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:28.029570+00:00
---

# Class IamPolicyAnalysisQuery (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class IamPolicyAnalysisQuery (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 
    
    
    IamPolicyAnalysisQuery(mapping=None, *, ignore_unknown_fields=False, **kwargs)

IAM policy analysis query message.

## Attributes  
  
---  
**Name** | **Description**  
`scope` |  `str`   
Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed. This can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345"). To know how to get organization ID, visit `here `__. To know how to get folder or project ID, visit `here `__.   
`resource_selector` |  `[google.cloud.asset_v1.types.IamPolicyAnalysisQuery.ResourceSelector](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery.ResourceSelector)`   
Optional. Specifies a resource for analysis.   
`identity_selector` |  `[google.cloud.asset_v1.types.IamPolicyAnalysisQuery.IdentitySelector](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery.IdentitySelector)`   
Optional. Specifies an identity for analysis.   
`access_selector` |  `[google.cloud.asset_v1.types.IamPolicyAnalysisQuery.AccessSelector](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery.AccessSelector)`   
Optional. Specifies roles or permissions for analysis. This is optional.   
`options` |  `[google.cloud.asset_v1.types.IamPolicyAnalysisQuery.Options](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery.Options)`   
Optional. The query options.   
`condition_context` |  `[google.cloud.asset_v1.types.IamPolicyAnalysisQuery.ConditionContext](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery.ConditionContext)`   
Optional. The hypothetical context for IAM conditions evaluation.   
  
## Classes 

### AccessSelector
    
    
    AccessSelector(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specifies roles and/or permissions to analyze, to determine both the identities possessing them and the resources they control. If multiple values are specified, results will include roles or permissions matching any of them. The total number of roles and permissions should be equal or less than 10.

### ConditionContext
    
    
    ConditionContext(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The IAM conditions context.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### IdentitySelector
    
    
    IdentitySelector(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specifies an identity for which to determine resource access, based on roles assigned either directly to them or to the groups they belong to, directly or indirectly.

### Options
    
    
    Options(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Contains query options.

### ResourceSelector
    
    
    ResourceSelector(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specifies the resource to analyze for access policies, which may be set directly on the resource, or on ancestors such as organizations, folders or projects.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
