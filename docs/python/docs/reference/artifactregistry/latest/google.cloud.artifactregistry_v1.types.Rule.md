---
url: https://docs.cloud.google.com/python/docs/reference/artifactregistry/latest/google.cloud.artifactregistry_v1.types.Rule
title: Class Rule (1.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:28.339658+00:00
---

# Class Rule (1.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/artifactregistry/latest/google.cloud.artifactregistry_v1.types.Rule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Rule (1.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.23.0 (latest)  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.1  1.15.2  1.14.0  1.13.1  1.12.0  1.11.5  1.10.0  1.9.0  1.8.4  1.7.0  1.6.1  1.5.0  1.4.1  1.3.3  1.2.1  1.1.2  1.0.2  0.5.0  0.4.1  0.3.3  0.2.2  0.1.0 
    
    
    Rule(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A rule defines the deny or allow action of the operation it applies to and the conditions required for the rule to apply. You can set one rule for an entire repository and one rule for each package within.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The name of the rule, for example: `projects/p1/locations/us-central1/repositories/repo1/rules/rule1`.   
`action` |  `[google.cloud.artifactregistry_v1.types.Rule.Action](https://docs.cloud.google.com/python/docs/reference/artifactregistry/latest/google.cloud.artifactregistry_v1.types.Rule.Action)`   
The action this rule takes.   
`condition` |  `google.type.expr_pb2.Expr`   
Optional. A CEL expression for conditions that must be met in order for the rule to apply. If not provided, the rule matches all objects.   
`package_id` |  `str`   
The package ID the rule applies to. If empty, this rule applies to all packages inside the repository.   
  
## Classes 

### Action
    
    
    Action(value)

Defines the action of the rule.

### Operation
    
    
    Operation(value)

The operation the rule applies to.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
