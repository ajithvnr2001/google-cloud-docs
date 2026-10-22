---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/upgrade/v1/upgrade-v1/
title: KRM API upgrade.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:50.977217+00:00
---

# KRM API upgrade.gdc.goog/v1  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/upgrade/v1/upgrade-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  KRM API upgrade.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## upgrade.gdc.goog/v1

### ComponentOverride

ComponentOverride changes the upgrade for an Operable Component (OC).

_Appears in:_ \- OrganizationUpgradeExecutionOverrideSpec

Field | Description  
---|---  
`name` _string_ | Name is the Operable Component (OC) name this override applies to.  
`subcomponents` _SubcomponentOverride array_ | Subcomponents is the list of Subcomponent upgrades to change.  
`tasks` _TaskOverride array_ | Tasks is the list of upgrade tasks to change.  
  
### ErrorStatus

_Appears in:_ \- OrganizationUpgradeExecutionOverrideStatus

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
`upgradeType` _UpgradeType_ | UpgradeType indicates the type of the MaintenanceWindow, which is one of `UpgradeTypeMinor` and `UpgradeTypePatch`.  
`recurrence` _string_ | Recurrence encodes a RRULE string to indicate how the window recurs. https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html Ex. TimeWindow.StartTime = 2022-04-18T02:00:00Z TimeWindow.EndTime = 2022-04-18T06:00:00Z Recurrence = FREQ=WEEKLY;BYDAY=MO,WE These parameters would create a schedule that starts on 04/18/2022 from 2 a.m to 6 a.m. Every Monday and Wednesday after, the same 2.am-6.am pattern would recur.  
`timeWindow` _TimeWindow_ | TimeWindow contains the start and end times for the MaintenanceWindow.  
`exclusions` _TimeWindow array_ | Exclusions is an array of TimeWindows that were skipped. Exclusions will only contain times specific up to the hour.  
  
### OrganizationUpgradeExecutionOverride

OrganizationUpgradeExecutionOverride defines ways to modify the execution of an upgrade for a version of GDC. This impacts all upgrades, both current and future.

_Appears in:_ \- OrganizationUpgradeExecutionOverrideList

Field | Description  
---|---  
`apiVersion` _string_ | `upgrade.gdc.goog/v1`  
`kind` _string_ | `OrganizationUpgradeExecutionOverride`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _OrganizationUpgradeExecutionOverrideSpec_ |   
`status` _OrganizationUpgradeExecutionOverrideStatus_ |   
  
### OrganizationUpgradeExecutionOverrideList

OrganizationUpgradeExecutionOverrideList is a collection of OrganizationUpgradeExecutionOverrides.

Field | Description  
---|---  
`apiVersion` _string_ | `upgrade.gdc.goog/v1`  
`kind` _string_ | `OrganizationUpgradeExecutionOverrideList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _OrganizationUpgradeExecutionOverride array_ |   
  
### OrganizationUpgradeExecutionOverrideSpec

OrganizationUpgradeExecutionOverrideSpec is the desired changes for an OrganizationUpgrade.

_Appears in:_ \- OrganizationUpgradeExecutionOverride

Field | Description  
---|---  
`for` _OrganizationUpgradeSelector_ | For specifies which OrganizationUpgrades this applies to.  
`components` _ComponentOverride array_ | Components is the list of Component upgrades to change.  
  
### OrganizationUpgradeExecutionOverrideStatus

OrganizationUpgradeExecutionOverrideStatus is the observed state for an OrganizationUpgradeExecutionOverride.

_Appears in:_ \- OrganizationUpgradeExecutionOverride

Field | Description  
---|---  
`errorStatus` _ErrorStatus_ | ErrorStatus records errors for this OrganizationUpgradeExecutionOverride.  
  
### OrganizationUpgradeSelector

OrganizationUpgradeSelector matches OrganizationUpgrades.

_Appears in:_ \- OrganizationUpgradeExecutionOverrideSpec

Field | Description  
---|---  
`version` _SemanticVersion_ | Version is the version of GDC an Organization is being upgraded to. Sometimes also called the GDC upgrade "target" version.  
  
### SemanticVersion

Wrapper/alias type for `semver.Version` (Semantic Version). Extended to support KRM APIs.

_Appears in:_ \- OrganizationUpgradeSelector

Field | Description  
---|---  
`major` _integer_ |   
`minor` _integer_ |   
`patch` _integer_ |   
`pre` _string_ |   
`metadata` _string_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`original` _string_ |   
  
### SubcomponentOverride

SubcomponentOverride changes the upgrade for an Operable Component's Subcomponent.

_Appears in:_ \- ComponentOverride

Field | Description  
---|---  
`name` _string_ | Name is the Subcomponent name this override applies to.  
`upgrade` _SubcomponentUpgradeOverride_ | Upgrade defines how the upgrade of this subcomponent should be overridden.  
  
### SubcomponentUpgradeOverride

_Underlying type:_ `string` SubcomponentUpgradeOverride is how the subcomponent upgrade should be overridden.

_Appears in:_ \- SubcomponentOverride

### TaskExecutionOverride

_Underlying type:_ `string` TaskExecutionOverride is how the upgrade task execution should be overridden.

_Appears in:_ \- TaskOverride

### TaskOverride

TaskOverride changes the execution of an upgrade task for an Operable Component.

_Appears in:_ \- ComponentOverride

Field | Description  
---|---  
`name` _string_ | Name is the upgrade task's name.  
`execution` _TaskExecutionOverride_ | Execution defines how the upgrade task's execution should be changed.  
  
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
