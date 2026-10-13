---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicy.Rule
title: Class Rule (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:20.298835+00:00
---

# Class Rule (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicy.Rule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Rule (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 
    
    
    Rule(mapping=None, *, ignore_unknown_fields=False, **kwargs)

This rule message is a customized version of the one defined in the Organization Policy system. In addition to the fields defined in the original organization policy, it contains additional field(s) under specific circumstances to support analysis results.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`values` |  `[google.cloud.asset_v1.types.AnalyzerOrgPolicy.Rule.StringValues](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicy.Rule.StringValues)`   
List of values to be used for this policy rule. This field can be set only in policies for list constraints. This field is a member of `oneof`_ `kind`.   
`allow_all` |  `bool`   
Setting this to true means that all values are allowed. This field can be set only in Policies for list constraints. This field is a member of `oneof`_ `kind`.   
`deny_all` |  `bool`   
Setting this to true means that all values are denied. This field can be set only in Policies for list constraints. This field is a member of `oneof`_ `kind`.   
`enforce` |  `bool`   
If `true`, then the `Policy` is enforced. If `false`, then any configuration is acceptable. This field can be set only in Policies for boolean constraints. This field is a member of `oneof`_ `kind`.   
`condition` |  `google.type.expr_pb2.Expr`   
The evaluating condition for this rule.   
`condition_evaluation` |  `[google.cloud.asset_v1.types.ConditionEvaluation](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ConditionEvaluation)`   
The condition evaluation result for this rule. Only populated if it meets all the following criteria: \- There is a condition defined for this rule. \- This rule is within AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.consolidated_policy, or AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.consolidated_policy when the AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset has AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.governed_resource.   
  
## Classes 

### StringValues
    
    
    StringValues(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The string values for the list constraints.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
