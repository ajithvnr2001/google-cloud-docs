---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SecurityPolicyRulePreconfiguredWafConfigExclusion
title: Class SecurityPolicyRulePreconfiguredWafConfigExclusion (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:37.993649+00:00
---

# Class SecurityPolicyRulePreconfiguredWafConfigExclusion (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SecurityPolicyRulePreconfiguredWafConfigExclusion

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SecurityPolicyRulePreconfiguredWafConfigExclusion (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    SecurityPolicyRulePreconfiguredWafConfigExclusion(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`request_bodies_to_exclude` |  `MutableSequence[[google.cloud.compute_v1beta.types.SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams)]`   
A list of request body fields to be excluded from inspection during preconfigured WAF evaluation.   
`request_cookies_to_exclude` |  `MutableSequence[[google.cloud.compute_v1beta.types.SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams)]`   
A list of request cookie names whose value will be excluded from inspection during preconfigured WAF evaluation.   
`request_headers_to_exclude` |  `MutableSequence[[google.cloud.compute_v1beta.types.SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams)]`   
A list of request header names whose value will be excluded from inspection during preconfigured WAF evaluation.   
`request_query_params_to_exclude` |  `MutableSequence[[google.cloud.compute_v1beta.types.SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams)]`   
A list of request query parameter names whose value will be excluded from inspection during preconfigured WAF evaluation. Note that the parameter can be in the query string or in the POST body.   
`request_uris_to_exclude` |  `MutableSequence[[google.cloud.compute_v1beta.types.SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams)]`   
A list of request URIs from the request line to be excluded from inspection during preconfigured WAF evaluation. When specifying this field, the query or fragment part should be excluded.   
`target_rule_ids` |  `MutableSequence[str]`   
A list of target rule IDs under the WAF rule set to apply the preconfigured WAF exclusion. If omitted, it refers to all the rule IDs under the WAF rule set.   
`target_rule_set` |  `str`   
Target WAF rule set to apply the preconfigured WAF exclusion. This field is a member of `oneof`_ `_target_rule_set`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
