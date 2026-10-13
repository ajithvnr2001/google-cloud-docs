---
url: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Model.PeriodicTuningState
title: Class PeriodicTuningState (2.14.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:49.662166+00:00
---

# Class PeriodicTuningState (2.14.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Model.PeriodicTuningState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PeriodicTuningState (2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.14.0 (latest)  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.2  1.20.1  1.19.1  1.18.0  1.17.0  1.16.3  1.15.1  1.14.1  1.13.0  1.12.0  1.11.0  1.10.2  1.9.0  1.8.1  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.2  0.4.2  0.3.1  0.2.0  0.1.0 
    
    
    PeriodicTuningState(value)

Describes whether periodic tuning is enabled for this model or not. Periodic tuning is scheduled at most every three months. You can start a tuning process manually by using the `TuneModel` method, which starts a tuning process immediately and resets the quarterly schedule. Enabling or disabling periodic tuning does not affect any current tuning processes.

## Enums  
  
---  
**Name** | **Description**  
`PERIODIC_TUNING_STATE_UNSPECIFIED` | Unspecified default value, should never be explicitly set.  
`PERIODIC_TUNING_DISABLED` | The model has periodic tuning disabled. Tuning can be reenabled by calling the `EnableModelPeriodicTuning` method or by calling the `TuneModel` method.  
`ALL_TUNING_DISABLED` | The model cannot be tuned with periodic tuning OR the `TuneModel` method. Hide the options in customer UI and reject any requests through the backend self serve API.  
`PERIODIC_TUNING_ENABLED` | The model has periodic tuning enabled. Tuning can be disabled by calling the `DisableModelPeriodicTuning` method.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
