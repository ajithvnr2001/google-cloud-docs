---
url: https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.DeleteDestinationRequest
title: Class DeleteDestinationRequest (2.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:35.075104+00:00
---

# Class DeleteDestinationRequest (2.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.DeleteDestinationRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeleteDestinationRequest (2.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.18.0 (latest)  2.17.0  2.16.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1  2.6.0  2.5.1  2.4.5  2.3.0  2.2.0  2.0.2  1.6.1  1.5.0  1.4.4  1.3.2  1.2.2  1.1.0  1.0.1  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    DeleteDestinationRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message to delete a `Destination` resource.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the `Destination` resource to delete.   
`request_id` |  `str`   
Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server can ignore the request if it has already been completed. The server waits for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, can ignore the second request. The request ID must be a valid UUID with the exception that zero UUID (00000000-0000-0000-0000-000000000000) isn't supported.   
`etag` |  `str`   
Optional. The etag is computed by the server, and might be sent with update and delete requests so that the client has an up-to-date value before proceeding.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
