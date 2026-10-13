---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.CreateCustomerRequest
title: Class CreateCustomerRequest (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:07.888338+00:00
---

# Class CreateCustomerRequest (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.CreateCustomerRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateCustomerRequest (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7  0.1.3 
    
    
    CreateCustomerRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request to create a customer

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Parent resource Format: `organizations/{organization}/locations/{location}`  
`customer` |  `[google.cloud.cloudcontrolspartner_v1.types.Customer](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudcontrolspartner/latest/google.cloud.cloudcontrolspartner_v1.types.Customer)`   
Required. The customer to create.   
`customer_id` |  `str`   
Required. The customer id to use for the customer, which will become the final component of the customer's resource name. The specified value must be a valid Google cloud organization id.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
