---
url: https://docs.cloud.google.com/python/docs/reference/composer/latest/google.cloud.orchestration.airflow.service_v1beta1.types.ListWorkloadsRequest
title: Class ListWorkloadsRequest (1.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:43:11.185918+00:00
---

# Class ListWorkloadsRequest (1.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/composer/latest/google.cloud.orchestration.airflow.service_v1beta1.types.ListWorkloadsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListWorkloadsRequest (1.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.23.0 (latest)  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.5  1.16.1  1.15.1  1.14.0  1.13.1  1.12.2  1.11.1  1.10.0  1.9.1  1.8.0  1.7.1  1.6.1  1.5.0  1.4.4  1.3.2  1.2.1  1.1.0  1.0.0  0.1.3 
    
    
    ListWorkloadsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request for listing workloads in a Cloud Composer environment.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The environment name to get workloads for, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}".   
`page_size` |  `int`   
Optional. The maximum number of environments to return.   
`page_token` |  `str`   
Optional. The next_page_token value returned from a previous List request, if any.   
`filter` |  `str`   
Optional. The list filter. Currently only supports equality on the type field. The value of a field specified in the filter expression must be one ComposerWorkloadType enum option. It's possible to get multiple types using "OR" operator, e.g.: "type=SCHEDULER OR type=CELERY_WORKER". If not specified, all items are returned.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
