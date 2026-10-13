---
url: https://docs.cloud.google.com/python/docs/reference/policysimulator/latest/google.cloud.policysimulator_v1.types.AccessStateDiff
title: Class AccessStateDiff (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:38:01.948737+00:00
---

# Class AccessStateDiff (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/policysimulator/latest/google.cloud.policysimulator_v1.types.AccessStateDiff

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AccessStateDiff (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.15 
    
    
    AccessStateDiff(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A summary and comparison of the principal's access under the current (baseline) policies and the proposed (simulated) policies for a single access tuple.

## Attributes  
  
---  
**Name** | **Description**  
`baseline` |  `[google.cloud.policysimulator_v1.types.ExplainedAccess](https://docs.cloud.google.com/python/docs/reference/policysimulator/latest/google.cloud.policysimulator_v1.types.ExplainedAccess)`   
The results of evaluating the access tuple under the current (baseline) policies. If the AccessState couldn't be fully evaluated, this field explains why.   
`simulated` |  `[google.cloud.policysimulator_v1.types.ExplainedAccess](https://docs.cloud.google.com/python/docs/reference/policysimulator/latest/google.cloud.policysimulator_v1.types.ExplainedAccess)`   
The results of evaluating the access tuple under the proposed (simulated) policies. If the AccessState couldn't be fully evaluated, this field explains why.   
`access_change` |  `[google.cloud.policysimulator_v1.types.AccessStateDiff.AccessChangeType](https://docs.cloud.google.com/python/docs/reference/policysimulator/latest/google.cloud.policysimulator_v1.types.AccessStateDiff.AccessChangeType)`   
How the principal's access, specified in the AccessState field, changed between the current (baseline) policies and proposed (simulated) policies.   
  
## Classes 

### AccessChangeType
    
    
    AccessChangeType(value)

How the principal's access, specified in the AccessState field, changed between the current (baseline) policies and proposed (simulated) policies.
    
    
        - The principal had access under the current policies
          (`GRANTED`), but their access after the proposed changes
          is `UNKNOWN`.
    
        - The principal's access under the current policies is
          `UNKNOWN`, but they will not have access after the
          proposed changes (`NOT_GRANTED`).
    ACCESS_MAYBE_GAINED (6):
        This result can occur for the following reasons:
    
        - The principal did not have access under the current
          policies (`NOT_GRANTED`), but their access after the
          proposed changes is `UNKNOWN`.
    
        - The principal's access under the current policies is
          `UNKNOWN`, but they will have access after the proposed
          changes (`GRANTED`).
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
