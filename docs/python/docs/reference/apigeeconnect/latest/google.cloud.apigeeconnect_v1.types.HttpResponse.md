---
url: https://docs.cloud.google.com/python/docs/reference/apigeeconnect/latest/google.cloud.apigeeconnect_v1.types.HttpResponse
title: Class HttpResponse (1.17.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:31.476450+00:00
---

# Class HttpResponse (1.17.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/apigeeconnect/latest/google.cloud.apigeeconnect_v1.types.HttpResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class HttpResponse (1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.2  1.11.0  1.10.1  1.9.5  1.8.0  1.7.3  1.6.1  1.5.0  1.4.3  1.3.2  1.2.1  1.1.0  1.0.2  0.2.2  0.1.0 
    
    
    HttpResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The proto definition of http response.

## Attributes  
  
---  
**Name** | **Description**  
`id` |  `str`   
A unique identifier that matches the request ID.   
`status` |  `str`   
Status of http response, e.g. "200 OK".   
`status_code` |  `int`   
Status code of http response, e.g. 200.   
`body` |  `bytes`   
The HTTP 1.1 response body.   
`headers` |  `MutableSequence[[google.cloud.apigeeconnect_v1.types.Header](https://docs.cloud.google.com/python/docs/reference/apigeeconnect/latest/google.cloud.apigeeconnect_v1.types.Header)]`   
The HTTP response headers.   
`content_length` |  `int`   
Content length records the length of the associated content. The value -1 indicates that the length is unknown. Unless http method is "HEAD", values >= 0 indicate that the given number of bytes may be read from Body.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
