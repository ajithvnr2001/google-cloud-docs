---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudsecuritycompliance/latest/google.cloud.cloudsecuritycompliance_v1.types.ListFrameworkAuditsRequest
title: Class ListFrameworkAuditsRequest (0.8.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:10.638428+00:00
---

# Class ListFrameworkAuditsRequest (0.8.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudsecuritycompliance/latest/google.cloud.cloudsecuritycompliance_v1.types.ListFrameworkAuditsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListFrameworkAuditsRequest (0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    ListFrameworkAuditsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The request message for [ListFrameworkAudits][].

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent resource where the framework audits are listed. Supported formats are the following: \- `organizations/{organization_id}/locations/{location}` \- `folders/{folder_id}/locations/{location}` \- `projects/{project_id}/locations/{location}`  
`page_size` |  `int`   
Optional. The maximum number of framework audits to return. The service might return fewer audits than this value. If unspecified, a maximum of 10 framework audits are returned. The maximum value is 50; values above 50 are limited to 50.   
`page_token` |  `str`   
Optional. The `next_page_token` value that's returned from a previous list request, if any.   
`filter` |  `str`   
Optional. The filters to apply to the framework audits. Supported filters are `compliance_framework`, `compliance_state`, `create_time,` and `framework_audit_name`. If the filter is invalid, an invalid argument error is returned. For syntax details, see [AIP-160][https://google.aip.dev/160].   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
