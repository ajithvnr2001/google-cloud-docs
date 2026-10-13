---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Unit.UnitState
title: Class UnitState (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:54.560609+00:00
---

# Class UnitState (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Unit.UnitState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UnitState (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    UnitState(value)

UnitState annotates what is the current state of the unit itself.

## Enums  
  
---  
**Name** | **Description**  
`UNIT_STATE_UNSPECIFIED` | Unspecified state.  
`UNIT_STATE_NOT_PROVISIONED` | Unit is not provisioned.  
`UNIT_STATE_PROVISIONING` | Unit is being provisioned.  
`UNIT_STATE_UPDATING` | Unit is being updated. This is typically when a unit is being upgraded to a new release or some of the input variables on the Unit is being changed. Certain kinds of updates may cause the Unit to become unusable while the update is in progress.  
`UNIT_STATE_DEPROVISIONING` | Unit is being deleted.  
`UNIT_STATE_READY` | Unit has been provisioned and is ready for use  
`UNIT_STATE_ERROR` | Unit has error, when it is not ready and some error operation  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
