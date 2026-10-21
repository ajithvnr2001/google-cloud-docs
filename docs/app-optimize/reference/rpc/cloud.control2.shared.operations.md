---
url: https://docs.cloud.google.com/app-optimize/reference/rpc/cloud.control2.shared.operations
title: Package cloud.control2.shared.operations \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:15.203314+00:00
---

# Package cloud.control2.shared.operations  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/reference/rpc/cloud.control2.shared.operations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Reference ](https://docs.cloud.google.com/app-optimize/apis)



Send feedback 

#  Package cloud.control2.shared.operations Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[ReconciliationOperationMetadata](https://docs.cloud.google.com/app-optimize/reference/rpc/cloud.control2.shared.operations#cloud.control2.shared.operations.ReconciliationOperationMetadata)` (message)
  * `[ReconciliationOperationMetadata.ExclusiveRepairActionFlag](https://docs.cloud.google.com/app-optimize/reference/rpc/cloud.control2.shared.operations#cloud.control2.shared.operations.ReconciliationOperationMetadata.ExclusiveRepairActionFlag)` (enum)



## ReconciliationOperationMetadata

Operation metadata returned by the CLH during resource state reconciliation.

Fields  
---  
`delete_resource  
**(deprecated)**` |  `bool` This item is deprecated!DEPRECATED. Use exclusive_action instead.  
`exclusive_action` |  `[ExclusiveRepairActionFlag](https://docs.cloud.google.com/app-optimize/reference/rpc/cloud.control2.shared.operations#cloud.control2.shared.operations.ReconciliationOperationMetadata.ExclusiveRepairActionFlag)` Excluisive action returned by the CLH.  
  
## ExclusiveRepairActionFlag

Some action that should be performed externally in order to complete this repair. These actions are exclusive meaning only one of them can be selected. If in the future there actions that can be applied in combination, we will add an InclusiveRepairActionFlag enum and an inclusive_actions repeated field.

Enums  
---  
`UNKNOWN_REPAIR_ACTION` | Unknown repair action.  
`DELETE` | The resource has to be deleted. When using this bit, the CLH should fail the operation. DEPRECATED. Instead use DELETE_RESOURCE OperationSignal in SideChannel.This item is deprecated!  
`RETRY` | This resource could not be repaired but the repair should be tried again at a later time. This can happen if there is a dependency that needs to be resolved first- e.g. if a parent resource must be repaired before a child resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-10 UTC."],[],[]] 
