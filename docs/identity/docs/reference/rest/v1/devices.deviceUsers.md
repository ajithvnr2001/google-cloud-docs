---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers
title: REST Resource: devices.deviceUsers \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:35.312545+00:00
---

# REST Resource: devices.deviceUsers  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: devices.deviceUsers Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: DeviceUser

Represents a user's use of a Device in the Cloud Identity Devices API.

A `[DeviceUser](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers#DeviceUser)` is a resource representing a user's use of a Device

JSON representation  
---  
      
    
    {
      "name": string,
      "userEmail": string,
      "managementState": enum ([ManagementState](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers#ManagementState)),
      "firstSyncTime": string,
      "lastSyncTime": string,
      "userAgent": string,
      "languageCode": string,
      "compromisedState": enum ([CompromisedState](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers#CompromisedState)),
      "passwordState": enum ([PasswordState](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers#PasswordState)),
      "createTime": string
    }  
  
Fields  
---  
`name` |  `string` Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the DeviceUser in format: `devices/{device}/deviceUsers/{deviceUser}`, where `deviceUser` uniquely identifies a user's use of a device.  
`userEmail` |  `string` Email address of the user registered on the device.  
`managementState` |  `enum (`[ManagementState](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers#ManagementState)`)` Output only. Management state of the user on the device.  
`firstSyncTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Most recent time when user registered with this service.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSyncTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last time when user synced with policies.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`userAgent` |  `string` Output only. User agent on the device for this specific user  
`languageCode` |  `string` Output only. Default locale used on device, in IETF BCP-47 format.  
`compromisedState` |  `enum (`[CompromisedState](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers#CompromisedState)`)` Compromised State of the DeviceUser object  
`passwordState` |  `enum (`[PasswordState](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers#PasswordState)`)` Password state of the DeviceUser object  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When the user first signed in to the deviceUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## ManagementState

Possible management states of a user on a device.

Enums  
---  
`MANAGEMENT_STATE_UNSPECIFIED` | Default value. This value is unused.  
`WIPING` | This user's data and profile is being removed from the device.  
`WIPED` | This user's data and profile is removed from the device.  
`APPROVED` | User is approved to access data on the device.  
`BLOCKED` | User is blocked from accessing data on the device.  
`PENDING_APPROVAL` | User is awaiting approval.  
`UNENROLLED` | User is unenrolled from Advanced Windows Management, but the Windows account is still intact.  
  
## CompromisedState

Describes whether the DeviceUser object is compromised or not.

Enums  
---  
`COMPROMISED_STATE_UNSPECIFIED` | Compromised state of Device User account is unknown or unspecified.  
`COMPROMISED` | Device User Account is compromised.  
`NOT_COMPROMISED` | Device User Account is not compromised.  
  
## PasswordState

The password state of the object

Enums  
---  
`PASSWORD_STATE_UNSPECIFIED` | Password state not set.  
`PASSWORD_SET` | Password set in object.  
`PASSWORD_NOT_SET` | Password not set in object.  
  
## Methods  
  
---  
  
### `[approve](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/approve)`

|  Approves device to access user data.  
  
### `[block](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/block)`

|  Blocks device from accessing user data  
  
### `[cancelWipe](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/cancelWipe)`

|  Cancels an unfinished user account wipe.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/delete)`

|  Deletes the specified DeviceUser.  
  
### `[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/get)`

|  Retrieves the specified DeviceUser  
  
### `[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/list)`

|  Lists/Searches DeviceUsers.  
  
### `[lookup](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/lookup)`

|  Looks up resource names of the DeviceUsers associated with the caller's credentials, as well as the properties provided in the request.  
  
### `[wipe](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/wipe)`

|  Wipes the user's account on a device.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-26 UTC."],[],[]] 
