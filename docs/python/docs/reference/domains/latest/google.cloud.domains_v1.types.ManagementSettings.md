---
url: https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1.types.ManagementSettings
title: Class ManagementSettings (1.15.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:35.078811+00:00
---

# Class ManagementSettings (1.15.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1.types.ManagementSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ManagementSettings (1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.2  1.9.0  1.8.1  1.7.5  1.6.0  1.5.2  1.4.1  1.3.0  1.2.3  1.1.3  1.0.0  0.4.3  0.3.0  0.2.3  0.1.0 
    
    
    ManagementSettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Defines renewal, billing, and transfer settings for a `Registration`.

## Attributes  
  
---  
**Name** | **Description**  
`renewal_method` |  `[google.cloud.domains_v1.types.ManagementSettings.RenewalMethod](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1.types.ManagementSettings.RenewalMethod)`   
Output only. The renewal method for this `Registration`.   
`transfer_lock_state` |  `[google.cloud.domains_v1.types.TransferLockState](https://docs.cloud.google.com/python/docs/reference/domains/latest/google.cloud.domains_v1.types.TransferLockState)`   
Controls whether the domain can be transferred to another registrar.   
  
## Classes 

### RenewalMethod
    
    
    RenewalMethod(value)

Defines how the `Registration` is renewed.
    
    
        To disable automatic renewals, delete the resource by
        calling `DeleteRegistration` or export it by calling
        `ExportRegistration`.
    MANUAL_RENEWAL (2):
        The domain must be explicitly renewed each year before its
        `expire_time`. This option is only available when the
        `Registration` is in state `EXPORTED`.
    
        To manage the domain's current billing and renewal settings,
        go to `Google Domains <https://domains.google/>`__.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
