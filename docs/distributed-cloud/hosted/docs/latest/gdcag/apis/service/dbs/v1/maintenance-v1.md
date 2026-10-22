---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/dbs/v1/maintenance-v1/
title: KRM API maintenance.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:03.324833+00:00
---

# KRM API maintenance.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/dbs/v1/maintenance-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API maintenance.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## maintenance.goog/v1

Package v1 contains API Schema definitions for the Maintenace Policy v1 API group

### DateTimeRange

_Appears in:_ \- MaintenanceExclusion

Field | Description  
---|---  
`startDateTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Deny period start date. Date matching this period will have to be the same or after the start.  
`endDateTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Deny period end date. Date matching this period will have to be before the end.  
  
### DayOfWeek

_Underlying type:_ `string`

_Appears in:_ \- WeeklyCycle

### MaintenanceExclusion

MaintenanceExclusion is a period of time when maintenance is forbidden even if otherwise allowed by maintenance window. Ranges in MaintenanceExclusion use inclusive start values and exclusive end values (half-closed intervals). In interval notation, this is [start, end).

_Appears in:_ \- MaintenancePolicySpec

Field | Description  
---|---  
`dateTimeRange` _DateTimeRange_ | Period of time when maintenance is forbidden.  
  
### MaintenancePolicy

_Appears in:_ \- MaintenancePolicyList

Field | Description  
---|---  
`apiVersion` _string_ | `maintenance.goog/v1`  
`kind` _string_ | `MaintenancePolicy`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _MaintenancePolicySpec_ |   
`status` _MaintenancePolicyStatus_ |   
  
### MaintenancePolicyBinding

_Appears in:_ \- MaintenancePolicyBindingList

Field | Description  
---|---  
`apiVersion` _string_ | `maintenance.goog/v1`  
`kind` _string_ | `MaintenancePolicyBinding`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _MaintenancePolicyBindingSpec_ |   
`status` _MaintenancePolicyBindingStatus_ |   
  
### MaintenancePolicyBindingList

Field | Description  
---|---  
`apiVersion` _string_ | `maintenance.goog/v1`  
`kind` _string_ | `MaintenancePolicyBindingList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _MaintenancePolicyBinding array_ |   
  
### MaintenancePolicyBindingSpec

_Appears in:_ \- MaintenancePolicyBinding

Field | Description  
---|---  
`maintenancePolicy` _MaintenancePolicyRef_ |   
`resource` _MaintenancePolicyResourceRef_ |   
  
### MaintenancePolicyBindingStatus

_Appears in:_ \- MaintenancePolicyBinding

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions contain conditions for MaintenancePolicyBindings. The maintenance policy binding controller sets the Valid condition. The following are known values for the reason field: - BindingDuplicated: The controller found more than one binding assigned to a given resource, the status of the condition will be False. - MaintenancePolicyMissing: The maintenance policy the binding is pointing to is missing, t the status of the condition will be False. - ResourceMissing: The resource the binding is pointing to is missing, the status of the condition will be False. - Valid: There is a single binding for given resource, which both ends are referencing existing entities, the status of the condition will be True.  
  
### MaintenancePolicyList

Field | Description  
---|---  
`apiVersion` _string_ | `maintenance.goog/v1`  
`kind` _string_ | `MaintenancePolicyList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _MaintenancePolicy array_ |   
  
### MaintenancePolicyRef

_Appears in:_ \- MaintenancePolicyBindingSpec

Field | Description  
---|---  
`apiGroup` _string_ |   
`kind` _string_ |   
`name` _string_ |   
  
### MaintenancePolicyResourceRef

_Appears in:_ \- MaintenancePolicyBindingSpec

Field | Description  
---|---  
`apiGroup` _string_ |   
`kind` _string_ |   
`name` _string_ |   
  
### MaintenancePolicySpec

_Appears in:_ \- MaintenancePolicy

Field | Description  
---|---  
`maintenanceWindow` _MaintenanceWindow_ | Maintenance window that is applied to services covered by this policy.  
`maintenanceExclusions` _object (keys:string, values:MaintenanceExclusion)_ | Named periods when maintenance is forbidden even if otherwise allowed by maintenanceWindow.  
  
### MaintenancePolicyStatus

_Appears in:_ \- MaintenancePolicy

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions field contain conditions for MaintenancePolicies. The maintenance policy controller sets the "MaintenanceAllowed" condition. The following are known values for the reason field: - InsideMaintenanceWindow: We are currently inside the scheduled Maintenance Window and the maintenance is allowed. The status of the condition will be True. - OutsideMaintenanceWindow: We are currently inside the Maintenance Window, but the exclusion is in effect, the maintenance is not allowed. The status of the condition will be False. - InsideMaintenanceExclusion: We are currently outside the Maintenance Window, the maintenance is not allowed. The status of the condition will be False.  
  
### MaintenanceWindow

MaintenanceWindow represents a period of time when maintenance is allowed. One and only one of the fields must be present.

_Appears in:_ \- MaintenancePolicySpec

Field | Description  
---|---  
`weeklyCycle` _WeeklyCycle_ | Weekly cycle.  
  
### TimeOfDay

_Underlying type:_ `string` TimeOfDay is the time in the text format "HH:mm"

_Appears in:_ \- WeeklyCycle

### WeeklyCycle

WeeklyCycle represents the weekly-recurring time window for operations.

_Appears in:_ \- MaintenanceWindow

Field | Description  
---|---  
`daysOfWeek` _DayOfWeek array_ | Day of the week when the operations can be started. One or more days may be specified.  
`startTime` _TimeOfDay_ | Time within the day to start the operations. UTC timezone is assumed.  
`duration` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | Duration of the time window.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
