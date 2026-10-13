---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-devicestreaming/latest/google.cloud.devicestreaming_v1.types.DeviceSession.SessionState
title: Class SessionState (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:00.991362+00:00
---

# Class SessionState (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-devicestreaming/latest/google.cloud.devicestreaming_v1.types.DeviceSession.SessionState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SessionState (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    SessionState(value)

The state that the DeviceSession resides.

## Enums  
  
---  
**Name** | **Description**  
`SESSION_STATE_UNSPECIFIED` | Default value. This value is unused.  
`REQUESTED` | Initial state of a session request. The session is being validated for correctness and a device is not yet requested.  
`PENDING` | The session has been validated and is in the queue for a device.  
`ACTIVE` | The session has been granted and the device is accepting connections.  
`EXPIRED` | The session duration exceeded the device's reservation time period and timed out automatically.  
`FINISHED` | The user is finished with the session and it was canceled by the user while the request was still getting allocated or after allocation and during device usage period.  
`UNAVAILABLE` | Unable to complete the session because the device was unavailable and it failed to allocate through the scheduler. For example, a device not in the catalog was requested or the request expired in the allocation queue.  
`ERROR` | Unable to complete the session for an internal reason, such as an infrastructure failure.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
