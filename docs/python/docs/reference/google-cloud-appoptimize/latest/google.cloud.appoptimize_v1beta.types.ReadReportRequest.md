---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.ReadReportRequest
title: Class ReadReportRequest (0.2.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:51.036059+00:00
---

# Class ReadReportRequest (0.2.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.ReadReportRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ReadReportRequest (0.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.1 (latest)  0.2.0 
    
    
    ReadReportRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for the `ReadReport` method.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The resource name of the report to query. Format: `projects/{project}/locations/{location}/reports/{report_id}`.   
`page_size` |  `int`   
Optional. The maximum number of rows to return. The service may return fewer than this value. If unspecified, at most 10,000 rows will be returned per page. The maximum allowed value is 25,000; values above 25,000 are coerced to 25,000.   
`page_token` |  `str`   
Optional. A page token, received from a previous `ReadReport` call, to retrieve the subsequent page of results. When `page_token` is specified, `job_reference` must also be provided from the previous response, and the `statement` field must not be set.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
