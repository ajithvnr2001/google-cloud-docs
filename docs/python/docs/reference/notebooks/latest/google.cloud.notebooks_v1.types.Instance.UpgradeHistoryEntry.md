---
url: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.UpgradeHistoryEntry
title: Class UpgradeHistoryEntry (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:43.011814+00:00
---

# Class UpgradeHistoryEntry (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.UpgradeHistoryEntry

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UpgradeHistoryEntry (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.3  1.12.0  1.11.1  1.10.5  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.4  1.3.2  1.2.1  1.1.1  1.0.0  0.4.3  0.3.2  0.2.0  0.1.2 
    
    
    UpgradeHistoryEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The entry of VM image upgrade history.

## Attributes  
  
---  
**Name** | **Description**  
`snapshot` |  `str`   
The snapshot of the boot disk of this notebook instance before upgrade.   
`vm_image` |  `str`   
The VM image before this instance upgrade.   
`container_image` |  `str`   
The container image before this instance upgrade.   
`framework` |  `str`   
The framework of this notebook instance.   
`version` |  `str`   
The version of the notebook instance before this upgrade.   
`state` |  `[google.cloud.notebooks_v1.types.Instance.UpgradeHistoryEntry.State](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.UpgradeHistoryEntry.State)`   
The state of this instance upgrade history entry.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time that this instance upgrade history entry is created.   
`target_image` |  `str`   
Target VM Image. Format: `ainotebooks-vm/project/image-name/name`.   
`action` |  `[google.cloud.notebooks_v1.types.Instance.UpgradeHistoryEntry.Action](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.UpgradeHistoryEntry.Action)`   
Action. Rolloback or Upgrade.   
`target_version` |  `str`   
Target VM Version, like m63.   
  
## Classes 

### Action
    
    
    Action(value)

The definition of operations of this upgrade history entry.

### State
    
    
    State(value)

The definition of the states of this upgrade history entry.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
