---
url: https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.ListDataPoliciesRequest
title: Class ListDataPoliciesRequest (0.10.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:33.520408+00:00
---

# Class ListDataPoliciesRequest (0.10.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.ListDataPoliciesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListDataPoliciesRequest (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.10.0  0.9.0  0.8.0  0.7.0  0.6.16  0.5.3  0.4.0  0.3.2  0.2.0  0.1.1 
    
    
    ListDataPoliciesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for the ListDataPolicies method.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Resource name of the project for which to list data policies. Format is `projects/{project_number}/locations/{location_id}`.   
`page_size` |  `int`   
Optional. The maximum number of data policies to return. Must be a value between 1 and 1000. If not set, defaults to 50.   
`page_token` |  `str`   
Optional. The `nextPageToken` value returned from a previous list request, if any. If not set, defaults to an empty string.   
`filter` |  `str`   
Optional. Filters the data policies by policy tags that they are associated with. Currently filter only supports "policy_tag" based filtering and OR based predicates. Sample filter can be "policy_tag: projects/1/locations/us/taxonomies/2/policyTags/3". You may also use wildcard such as "policy_tag: projects/1/locations/us/taxonomies/2\\*". Please note that OR predicates cannot be used with wildcard filters.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
