---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ExclusiveRepairActionFlag/
title: ExclusiveRepairActionFlag \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:08.657461+00:00
---

# ExclusiveRepairActionFlag  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ExclusiveRepairActionFlag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  ExclusiveRepairActionFlag Stay organized with collections  Save and categorize content based on your preferences. 

Some action that should be performed externally in order to complete this repair. These actions are exclusive meaning only one of them can be selected. If in the future there actions that can be applied in combination, we will add an InclusiveRepairActionFlag enum and an inclusive_actions repeated field.

Enums  
---  
`UNKNOWN_REPAIR_ACTION` | Unknown repair action.  
`DELETE` | The resource has to be deleted. When using this bit, the CLH should fail the operation. DEPRECATED. Instead use DELETE_RESOURCE OperationSignal in SideChannel.This item is deprecated!  
`RETRY` | This resource could not be repaired but the repair should be tried again at a later time. This can happen if there is a dependency that needs to be resolved first- e.g. if a parent resource must be repaired before a child resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
