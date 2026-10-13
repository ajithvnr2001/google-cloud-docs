---
url: https://docs.cloud.google.com/python/docs/reference/cloudchannel/latest/google.cloud.channel_v1.types.RegisterSubscriberRequest
title: Class RegisterSubscriberRequest (1.29.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:11.386198+00:00
---

# Class RegisterSubscriberRequest (1.29.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudchannel/latest/google.cloud.channel_v1.types.RegisterSubscriberRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RegisterSubscriberRequest (1.29.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.29.0 (latest)  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.2  1.21.0  1.20.1  1.19.0  1.18.5  1.17.1  1.15.1  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.3  1.8.1  1.7.1  1.6.3  1.5.0  1.4.0  1.3.2  1.2.3  1.1.1  1.0.0  0.3.0  0.2.1  0.1.0 
    
    
    RegisterSubscriberRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request Message for RegisterSubscriber.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`account` |  `str`   
Optional. Resource name of the account. Required if integrator is not provided. Otherwise, leave this field empty/unset.   
`service_account` |  `str`   
Required. Service account that provides subscriber access to the registered topic.   
`integrator` |  `str`   
Optional. Resource name of the integrator. Required if account is not provided. Otherwise, leave this field empty/unset. This field is a member of `oneof`_ `_integrator`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
