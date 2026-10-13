---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.InterconnectDiagnostics.LinkLACPStatus
title: Class LinkLACPStatus (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:33.563803+00:00
---

# Class LinkLACPStatus (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.InterconnectDiagnostics.LinkLACPStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LinkLACPStatus (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.4.0  0.3.0  0.2.0  0.1.18 
    
    
    LinkLACPStatus(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describing the status of a LACP link.

## Attributes  
  
---  
**Name** | **Description**  
`state` |  `[google.cloud.edgenetwork_v1.types.InterconnectDiagnostics.LinkLACPStatus.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.InterconnectDiagnostics.LinkLACPStatus.State)`   
The state of a LACP link.   
`google_system_id` |  `str`   
System ID of the port on Google's side of the LACP exchange.   
`neighbor_system_id` |  `str`   
System ID of the port on the neighbor's side of the LACP exchange.   
`aggregatable` |  `bool`   
A true value indicates that the participant will allow the link to be used as part of the aggregate. A false value indicates the link should be used as an individual link.   
`collecting` |  `bool`   
If true, the participant is collecting incoming frames on the link, otherwise false   
`distributing` |  `bool`   
When true, the participant is distributing outgoing frames; when false, distribution is disabled   
  
## Classes 

### State
    
    
    State(value)

State enum for LACP link.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
