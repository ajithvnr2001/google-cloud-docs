---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.SignalZoneStateRequest
title: Class SignalZoneStateRequest (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:10:12.933389+00:00
---

# Class SignalZoneStateRequest (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.SignalZoneStateRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SignalZoneStateRequest (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    SignalZoneStateRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A request to signal the state of a zone.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the zone. Format: `projects/{project}/locations/{location}/zones/{zone}`  
`request_id` |  `str`   
Optional. An optional unique identifier for this request. See `AIP-155 `__.   
`state_signal` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.SignalZoneStateRequest.StateSignal](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.SignalZoneStateRequest.StateSignal)`   
Optional. The state signal to send for this zone. Either state_signal or provisioning_state_signal must be set, but not both.   
`provisioning_state_signal` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.SignalZoneStateRequest.ProvisioningStateSignal](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.SignalZoneStateRequest.ProvisioningStateSignal)`   
Optional. The provisioning state signal to send for this zone. Either state_signal or provisioning_state_signal must be set, but not both.   
`step` |  `str`   
Optional. The step being executed. Provides a finer grained status when the state_signal is FACTORY_TURNUP_CHECKS_STARTED or FACTORY_TURNUP_CHECKS_FAILED.   
`details` |  `str`   
Optional. Additional details, such as an error message when state_signal is FACTORY_TURNUP_CHECKS_FAILED.   
  
## Classes 

### ProvisioningStateSignal
    
    
    ProvisioningStateSignal(value)

Valid provisioning state signals for a zone.

### StateSignal
    
    
    StateSignal(value)

Valid state signals for a zone.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
