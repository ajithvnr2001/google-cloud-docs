---
url: https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ImportUserEventsRequest
title: Class ImportUserEventsRequest (0.13.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:09.249119+00:00
---

# Class ImportUserEventsRequest (0.13.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ImportUserEventsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ImportUserEventsRequest (0.13.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.2 (latest)  0.13.1  0.12.0  0.11.0  0.10.18  0.9.0  0.8.2  0.7.1  0.6.2  0.5.1  0.4.0  0.3.3  0.2.2  0.1.0 
    
    
    ImportUserEventsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for the ImportUserEvents request.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. `projects/1234/locations/global/catalogs/default_catalog/eventStores/default_event_store`  
`request_id` |  `str`   
Optional. Unique identifier provided by client, within the ancestor dataset scope. Ensures idempotency for expensive long running operations. Server-generated if unspecified. Up to 128 characters long. This is returned as google.longrunning.Operation.name in the response. Note that this field must not be set if the desired input config is catalog_inline_source.   
`input_config` |  `[google.cloud.recommendationengine_v1beta1.types.InputConfig](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.InputConfig)`   
Required. The desired input location of the data.   
`errors_config` |  `[google.cloud.recommendationengine_v1beta1.types.ImportErrorsConfig](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ImportErrorsConfig)`   
Optional. The desired location of errors incurred during the Import.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
