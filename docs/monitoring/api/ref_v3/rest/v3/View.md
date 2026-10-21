---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/View/
title: View \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:18.622026+00:00
---

# View  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/View/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  View Stay organized with collections  Save and categorize content based on your preferences. 

`ServiceLevelObjective.View` determines what form of `ServiceLevelObjective` is returned from `serviceLevelObjectives.get`, `serviceLevelObjectives.list`, and `versions.list` RPCs.

Enums  
---  
`VIEW_UNSPECIFIED` | Same as FULL.  
`FULL` | Return the embedded `ServiceLevelIndicator` in the form in which it was defined. If it was defined using a `BasicSli`, return that `BasicSli`.  
`EXPLICIT` | For `ServiceLevelIndicator`s using `BasicSli` articulation, instead return the `ServiceLevelIndicator` with its mode of computation fully spelled out as a `RequestBasedSli`. For `ServiceLevelIndicator`s using `RequestBasedSli` or `WindowsBasedSli`, return the `ServiceLevelIndicator` as it was provided.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
