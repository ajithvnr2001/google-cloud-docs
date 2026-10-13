---
url: https://docs.cloud.google.com/python/docs/reference/policytroubleshooter-iam/latest/google.cloud.policytroubleshooter_iam_v3.types.ConditionContext.EffectiveTag
title: Class EffectiveTag (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:32.544346+00:00
---

# Class EffectiveTag (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/policytroubleshooter-iam/latest/google.cloud.policytroubleshooter_iam_v3.types.ConditionContext.EffectiveTag

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class EffectiveTag (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.4.0  0.3.0  0.2.0  0.1.13 
    
    
    EffectiveTag(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A tag that applies to a resource during policy evaluation. Tags can be either directly bound to a resource or inherited from its ancestor. `EffectiveTag` contains the `name` and `namespaced_name` of the tag value and tag key, with additional fields of `inherited` to indicate the inheritance status of the effective tag.

## Attributes  
  
---  
**Name** | **Description**  
`tag_value` |  `str`   
Output only. Resource name for TagValue in the format `tagValues/456`.   
`namespaced_tag_value` |  `str`   
Output only. The namespaced name of the TagValue. Can be in the form `{organization_id}/{tag_key_short_name}/{tag_value_short_name}` or `{project_id}/{tag_key_short_name}/{tag_value_short_name}` or `{project_number}/{tag_key_short_name}/{tag_value_short_name}`.   
`tag_key` |  `str`   
Output only. The name of the TagKey, in the format `tagKeys/{id}`, such as `tagKeys/123`.   
`namespaced_tag_key` |  `str`   
Output only. The namespaced name of the TagKey. Can be in the form `{organization_id}/{tag_key_short_name}` or `{project_id}/{tag_key_short_name}` or `{project_number}/{tag_key_short_name}`.   
`tag_key_parent_name` |  `str`   
The parent name of the tag key. Must be in the format `organizations/{organization_id}` or `projects/{project_number}`  
`inherited` |  `bool`   
Output only. Indicates the inheritance status of a tag value attached to the given resource. If the tag value is inherited from one of the resource's ancestors, inherited will be true. If false, then the tag value is directly attached to the resource, inherited will be false.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
