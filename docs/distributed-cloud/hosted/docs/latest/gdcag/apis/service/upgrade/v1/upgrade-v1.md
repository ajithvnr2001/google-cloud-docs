---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/upgrade/v1/upgrade-v1/
title: KRM API upgrade.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:11.723806+00:00
---

# KRM API upgrade.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/upgrade/v1/upgrade-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API upgrade.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## upgrade.gdc.goog/v1

### MaintenanceWindow

MaintenanceWindow specifies a recurring time window for applying for patch and minor version upgrades.

_Appears in:_ \- MaintenanceWindowList

Field | Description  
---|---  
`apiVersion` _string_ | `upgrade.gdc.goog/v1`  
`kind` _string_ | `MaintenanceWindow`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _MaintenanceWindowSpec_ |   
  
### MaintenanceWindowList

MaintenanceWindowList represents a collection of MaintenanceWindows.

Field | Description  
---|---  
`apiVersion` _string_ | `upgrade.gdc.goog/v1`  
`kind` _string_ | `MaintenanceWindowList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _MaintenanceWindow array_ |   
  
### MaintenanceWindowSpec

MaintenanceWindowSpec provides the specification (i.e., desired state) of a MaintenanceWindow.

_Appears in:_ \- MaintenanceWindow

Field | Description  
---|---  
`upgradeType` _UpgradeType_ | UpgradeType indicates the type of the MaintenanceWindow, which is one of "MinorUpgrade" and "PatchUpgrade".  
`recurrence` _string_ | Recurrence encodes a RRULE string to indicate how the window recurs. https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html Ex. TimeWindow.StartTime = 2022-04-18T02:00:00Z TimeWindow.EndTime = 2022-04-18T06:00:00Z Recurrence = FREQ=WEEKLY;BYDAY=MO,WE These parameters would create a schedule that starts on 04/18/2022 from 2 a.m to 6 a.m. Every Monday and Wednesday after, the same 2.am-6.am pattern would recur.  
`timeWindow` _TimeWindow_ | TimeWindow contains the start and end times for the MaintenanceWindow.  
`exclusions` _TimeWindow array_ | Exclusions is an array of TimeWindows that were skipped. Exclusions will only contain times specific up to the hour.  
  
### TimeWindow

TimeWindow defines a chunk of time.

_Appears in:_ \- MaintenanceWindowSpec

Field | Description  
---|---  
`start` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Start indicates the start of the window.  
`end` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | End indicates the end of the window.  
  
### UpgradeType

_Underlying type:_ `string` UpgradeType specifies the type of an upgrade. Only one of the following upgrade types may be specified.

_Appears in:_ \- MaintenanceWindowSpec

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
