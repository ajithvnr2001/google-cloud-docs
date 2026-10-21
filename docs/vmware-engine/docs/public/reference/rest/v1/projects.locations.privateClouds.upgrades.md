---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades
title: REST Resource: projects.locations.privateClouds.upgrades \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:19.077348+00:00
---

# REST Resource: projects.locations.privateClouds.upgrades  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.privateClouds.upgrades Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Upgrade
    * JSON representation
  * State
  * Type
  * Schedule
    * JSON representation
  * TimeWindow
    * JSON representation
  * DayOfWeek
  * TimeOfDay
    * JSON representation
  * Constraints
    * JSON representation
  * Interval
    * JSON representation
  * WeeklyTimeInterval
    * JSON representation
  * Editor
  * VmwareUpgradeComponent
    * JSON representation
  * VmwareComponentType
  * State
  * Methods



## Resource: Upgrade

Describes Private cloud Upgrade.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "endTime": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#State)),
      "type": enum ([Type](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#Type)),
      "description": string,
      "estimatedDuration": string,
      "schedule": {
        object ([Schedule](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#Schedule))
      },
      "version": string,
      "etag": string,
      "uid": string,
      "componentUpgrades": [
        {
          object ([VmwareUpgradeComponent](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#VmwareUpgradeComponent))
        }
      ],
      "startVersion": string,
      "targetVersion": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of the private cloud `Upgrade`. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-west1-a/privateClouds/my-cloud/upgrades/my-upgrade`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Output Only. Creation time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Output Only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Output Only. End time of the upgrade.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#State)`)` Output only. The current state of the upgrade.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#Type)`)` Output only. Output Only. The type of upgrade.  
`description` |  `string` Output only. Output Only. The description of the upgrade. This is used to provide additional information about the private cloud upgrade, such as the upgrade's purpose, the changes included in the upgrade, or any other relevant information about the upgrade.  
`estimatedDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. Output Only. The estimated total duration of the upgrade. This information can be used to plan or schedule upgrades to minimize disruptions. Please note that the estimated duration is only an estimate. The actual upgrade duration may vary.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`schedule` |  `object (`[Schedule](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#Schedule)`)` Schedule details for the upgrade.  
`version` |  `string` Output only.   
`etag` |  `string` The etag for the upgrade resource. If this is provided on update, it must match the server's etag.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
`componentUpgrades[]` |  `object (`[VmwareUpgradeComponent](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#VmwareUpgradeComponent)`)` Output only. Output Only. The list of component upgrades.  
`startVersion` |  `string` Output only. Output Only. The start version  
`targetVersion` |  `string` Output only. Output Only. The target version  
  
## State

Possible states of private cloud `Upgrade`.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value should never be used.  
`SCHEDULED` | The upgrade is scheduled but not started yet.  
`ONGOING` | The upgrade is currently in progress and has not completed yet.  
`SUCCEEDED` | The upgrade completed successfully.  
`PAUSED` | The upgrade is currently paused.  
`FAILED` | The upgrade failed.  
`CANCELLING` | The upgrade is in process of being canceled.  
`CANCELLED` | The upgrade is canceled.  
`RESCHEDULING` | The upgrade is in process of being rescheduled.  
  
## Type

Possible upgrade types. More types can be added in future.

Enums  
---  
`TYPE_UNSPECIFIED` | The default value. This value should never be used.  
`VSPHERE_UPGRADE` | Upgrade of vmware components when a major version is available. 7.0u2 -> 7.0u3.  
`VSPHERE_PATCH` | Patching of vmware components when a minor version is available. 7.0u2c -> 7.0u2d.  
`WORKAROUND` | Workarounds are hotfixes for vulnerabilities or issues applied to mitigate the known vulnerability or issue until a patch or update is released. The description of the upgrade will have more details.  
`FIRMWARE_UPGRADE` | Firmware upgrade for VMware product used in the private cloud.  
`SWITCH_UPGRADE` | Switch upgrade.  
`OTHER` | The upgrade type that doesn't fall into any other category.  
`INFRASTRUCTURE_UPGRADE` | Infrastructure upgrade in BM node maintenance.  
  
## Schedule

Schedule for the upgrade.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "weeklyWindows": [
        {
          object ([TimeWindow](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#TimeWindow))
        }
      ],
      "constraints": {
        object ([Constraints](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#Constraints))
      },
      "editWindow": {
        object ([Interval](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#Interval))
      },
      "lastEditor": enum ([Editor](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#Editor))
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The scheduled start time for the upgrade.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`weeklyWindows[]` |  `object (`[TimeWindow](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#TimeWindow)`)` Required. Weekly time windows for upgrade activities. The server performs upgrade activities during these time windows to minimize disruptions.  
`constraints` |  `object (`[Constraints](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#Constraints)`)` Output only. Output Only. Constraints applied to the schedule. These constraints should be applicable at the time of any rescheduling.  
`editWindow` |  `object (`[Interval](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#Interval)`)` Output only. Output Only. The schedule is open for edits during this time interval or window.  
`lastEditor` |  `enum (`[Editor](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#Editor)`)` Output only. Output Only. Indicates who most recently edited the upgrade schedule. The value is updated whenever the upgrade is rescheduled.  
  
## TimeWindow

Represents the time window to perform upgrade activities.

JSON representation  
---  
      
    
    {
      "dayOfWeek": enum ([DayOfWeek](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#DayOfWeek)),
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#TimeOfDay))
      },
      "duration": string
    }  
  
Fields  
---  
`dayOfWeek` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#DayOfWeek)`)` Required. Day of the week for this window.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#TimeOfDay)`)` Required. Time in UTC when the window starts.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. The duration of the window. The max allowed duration for any window is 24 hours.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## DayOfWeek

Represents a day of the week.

Enums  
---  
`DAY_OF_WEEK_UNSPECIFIED` | The day of the week is unspecified.  
`MONDAY` | Monday  
`TUESDAY` | Tuesday  
`WEDNESDAY` | Wednesday  
`THURSDAY` | Thursday  
`FRIDAY` | Friday  
`SATURDAY` | Saturday  
`SUNDAY` | Sunday  
  
## TimeOfDay

Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are `google.type.Date` and `google.protobuf.Timestamp`.

JSON representation  
---  
      
    
    {
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer
    }  
  
Fields  
---  
`hours` |  `integer` Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59.  
`seconds` |  `integer` Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999.  
  
## Constraints

Constraints to be applied while editing a schedule. These constraints ensure that `Upgrade` specific requirements are met.

JSON representation  
---  
      
    
    {
      "minHoursDay": integer,
      "minHoursWeek": integer,
      "rescheduleDateRange": {
        object ([Interval](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#Interval))
      },
      "disallowedIntervals": [
        {
          object ([WeeklyTimeInterval](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#WeeklyTimeInterval))
        }
      ]
    }  
  
Fields  
---  
`minHoursDay` |  `integer` Output only. Minimum number of hours must be allotted for the upgrade activities for each selected day. This is a minimum; the upgrade schedule can allot more hours for the given day.  
`minHoursWeek` |  `integer` Output only. The minimum number of weekly hours must be allotted for the upgrade activities. This is just a minimum; the schedule can assign more weekly hours.  
`rescheduleDateRange` |  `object (`[Interval](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#Interval)`)` Output only. Output Only. The user can only reschedule an upgrade that starts within this range.  
`disallowedIntervals[]` |  `object (`[WeeklyTimeInterval](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#WeeklyTimeInterval)`)` Output only. Output Only. A list of intervals in which maintenance windows are not allowed. Any time window that overlaps with any of these intervals will be considered invalid.  
  
## Interval

Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive).

The start must be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both start and end are unspecified, the interval matches any time.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Inclusive start of the interval.If specified, a Timestamp matching this interval will have to be the same or after the start.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Exclusive end of the interval.If specified, a Timestamp matching this interval will have to be before the end.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## WeeklyTimeInterval

Represents a time interval, spanning across days of the week. Until local timezones are supported, this interval is in UTC.

JSON representation  
---  
      
    
    {
      "startDay": enum ([DayOfWeek](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#DayOfWeek)),
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#TimeOfDay))
      },
      "endDay": enum ([DayOfWeek](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#DayOfWeek)),
      "endTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#TimeOfDay))
      }
    }  
  
Fields  
---  
`startDay` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#DayOfWeek)`)` Output only. The day on which the interval starts.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#TimeOfDay)`)` Output only. The time on the start day at which the interval starts.  
`endDay` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#DayOfWeek)`)` Output only. The day on which the interval ends. Can be same as start day.  
`endTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#TimeOfDay)`)` Output only. The time on the end day at which the interval ends.  
  
## Editor

Possible values of who edited the upgrade schedule Value identifies groups or entities instead of individuals.

Enums  
---  
`EDITOR_UNSPECIFIED` | The default value. This value should never be used.  
`SYSTEM` | The upgrade is scheduled by the System or internal service.  
`USER` | The upgrade is scheduled by the end user.  
  
## VmwareUpgradeComponent

Per component upgrade resource

JSON representation  
---  
      
    
    {
      "componentType": enum ([VmwareComponentType](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#VmwareComponentType)),
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#State_1))
    }  
  
Fields  
---  
`componentType` |  `enum (`[VmwareComponentType](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#VmwareComponentType)`)` Output only. Type of component  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades#State_1)`)` Output only. Component's upgrade state.  
  
## VmwareComponentType

The type of vmware component

Enums  
---  
`VMWARE_COMPONENT_TYPE_UNSPECIFIED` | The default value. This value should never be used.  
`VCENTER` | vcenter  
`ESXI` | esxi nodes + transport nodes  
`NSXT_UC` | nsxt upgrade coordinator  
`NSXT_EDGE` | nsxt edges cluster  
`NSXT_MGR` | nsxt managers/management plane  
`HCX` | hcx  
`VSAN` | VSAN cluster  
`DVS` | DVS switch  
`NAMESERVER_VM` | Nameserver VMs  
`KMS_VM` | KMS VM used for vsan encryption  
`WITNESS_VM` | witness VM in case of stretch PC  
`NSXT` | nsxt  
`CLUSTER` | Cluster is used in case of BM  
`VM_TOOLS` | VMware Tools.  
  
## State

State defines current state of an upgrade

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value should never be used.  
`RUNNING` | Component's upgrade is in progress  
`PAUSED` | The component's upgrade is paused. Will be resumed when upgrade job is resumed  
`SUCCEEDED` | The component's upgrade is successfully completed  
`FAILED` | The component's upgrade has failed. This will move to resume if upgrade is resumed or stay as is  
`NOT_STARTED` | Component's upgrade has not started yet  
`NOT_APPLICABLE` | Component's upgrade is not applicable in this upgrade. It will be skipped.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades/get)`

|  Retrieves a private cloud `Upgrade` resource by its resource name.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades/list)`

|  Lists past, ongoing and upcoming `Upgrades` for the given private cloud.  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.upgrades/patch)`

|  Update the private cloud `Upgrade` resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
