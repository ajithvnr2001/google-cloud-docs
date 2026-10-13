---
url: https://docs.cloud.google.com/python/docs/reference/privateca/latest/google.cloud.security.privateca_v1beta1.types.ScheduleDeleteCertificateAuthorityRequest
title: Class ScheduleDeleteCertificateAuthorityRequest (1.20.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:29.172732+00:00
---

# Class ScheduleDeleteCertificateAuthorityRequest (1.20.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/privateca/latest/google.cloud.security.privateca_v1beta1.types.ScheduleDeleteCertificateAuthorityRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ScheduleDeleteCertificateAuthorityRequest (1.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.20.0 (latest)  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.3  1.13.1  1.12.2  1.11.0  1.10.3  1.9.0  1.8.1  1.7.1  1.6.1  1.5.0  1.4.3  1.3.2  1.2.4  1.1.0  1.0.6  0.4.0  0.3.0  0.1.1 
    
    
    ScheduleDeleteCertificateAuthorityRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request message for CertificateAuthorityService.ScheduleDeleteCertificateAuthority.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The resource name for this CertificateAuthority in the format `projects/*/locations/*/certificateAuthorities/*`.   
`request_id` |  `str`   
Optional. An ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
