---
url: https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1alpha.types.ScanConfig.Authentication
title: Class Authentication (1.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:43.971806+00:00
---

# Class Authentication (1.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1alpha.types.ScanConfig.Authentication

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Authentication (1.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.22.0 (latest)  1.21.0  1.20.0  1.19.0  1.18.0  1.17.2  1.16.0  1.15.1  1.14.5  1.13.0  1.12.2  1.11.1  1.10.0  1.9.2  1.8.3  1.7.2  1.6.1  1.5.0  1.4.3  1.3.0  1.2.0  1.1.0  1.0.0  0.4.2  0.3.0 
    
    
    Authentication(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Scan authentication configuration.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`google_account` |  `[google.cloud.websecurityscanner_v1alpha.types.ScanConfig.Authentication.GoogleAccount](https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1alpha.types.ScanConfig.Authentication.GoogleAccount)`   
Authentication using a Google account. This field is a member of `oneof`_ `authentication`.   
`custom_account` |  `[google.cloud.websecurityscanner_v1alpha.types.ScanConfig.Authentication.CustomAccount](https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1alpha.types.ScanConfig.Authentication.CustomAccount)`   
Authentication using a custom account. This field is a member of `oneof`_ `authentication`.   
  
## Classes 

### CustomAccount
    
    
    CustomAccount(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes authentication configuration that uses a custom account.

### GoogleAccount
    
    
    GoogleAccount(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes authentication configuration that uses a Google account.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
