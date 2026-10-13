---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1beta.types.CreateFleetPackageRequest
title: Class CreateFleetPackageRequest (0.5.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:38.968674+00:00
---

# Class CreateFleetPackageRequest (0.5.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1beta.types.CreateFleetPackageRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateFleetPackageRequest (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 
    
    
    CreateFleetPackageRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message for creating a FleetPackage

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Value for parent.   
`fleet_package_id` |  `str`   
Required. Id of the requesting object If auto-generating Id server-side, remove this field and fleet_package_id from the method_signature of Create RPC   
`fleet_package` |  `[google.cloud.configdelivery_v1beta.types.FleetPackage](https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1beta.types.FleetPackage)`   
Required. The resource being created.   
`request_id` |  `str`   
Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
