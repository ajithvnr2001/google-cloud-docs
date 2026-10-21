---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions
title: REST Resource: projects.deviceSessions \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:58.389674+00:00
---

# REST Resource: projects.deviceSessions  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  REST Resource: projects.deviceSessions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DeviceSession
    * JSON representation
  * SessionState
  * SessionStateEvent
    * JSON representation
  * AndroidDevice
    * JSON representation
  * ClientInfo
    * JSON representation
  * Methods



## Resource: DeviceSession

Protobuf message describing the device message, used from several RPCs.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "state": enum ([SessionState](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#SessionState)),
      "stateHistories": [
        {
          object ([SessionStateEvent](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#SessionStateEvent))
        }
      ],
      "inactivityTimeout": string,
      "createTime": string,
      "activeStartTime": string,
      "androidDevice": {
        object ([AndroidDevice](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#AndroidDevice))
      },
      "clientInfo": {
        object ([ClientInfo](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#ClientInfo))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "ttl": string,
      "expireTime": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Optional. Name of the DeviceSession, e.g. "projects/{projectId}/deviceSessions/{session_id}"  
`displayName` |  `string` Output only. The title of the DeviceSession to be presented in the UI.  
`state` |  `enum (`[SessionState](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#SessionState)`)` Output only. Current state of the DeviceSession.  
`stateHistories[]` |  `object (`[SessionStateEvent](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#SessionStateEvent)`)` Output only. The historical state transitions of the sessionState message including the current session state.  
`inactivityTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The interval of time that this device must be interacted with before it transitions from ACTIVE to TIMEOUT_INACTIVITY.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that the Session was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`activeStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp that the session first became ACTIVE.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`androidDevice` |  `object (`[AndroidDevice](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#AndroidDevice)`)` Required. The requested device.  
`clientInfo` |  `object (`[ClientInfo](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#ClientInfo)`)` Optional. Information about the client which invoked the device session.  
The amount of time that a device will be initially allocated for. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`ttl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The amount of time that a device will be initially allocated for. This can eventually be extended with the deviceSessions.patch RPC. Default: 15 minutes.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. If the device is still in use at this time, any connections will be ended and the SessionState will transition from ACTIVE to FINISHED.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
End of mutually exclusive fields.  
  
## SessionState

The state that the DeviceSession resides.

Enums  
---  
`SESSION_STATE_UNSPECIFIED` | Default value. This value is unused.  
`REQUESTED` | Initial state of a session request. The session is being validated for correctness and a device is not yet requested.  
`PENDING` | The session has been validated and is in the queue for a device.  
`ACTIVE` | The session has been granted and the device is accepting connections.  
`EXPIRED` | The session duration exceeded the device's reservation time period and timed out automatically.  
`FINISHED` | The user is finished with the session and it was canceled by the user while the request was still getting allocated or after allocation and during device usage period.  
`UNAVAILABLE` | Unable to complete the session because the device was unavailable and it failed to allocate through the scheduler. For example, a device not in the catalog was requested or the request expired in the allocation queue.  
`ERROR` | Unable to complete the session for an internal reason, such as an infrastructure failure.  
  
## SessionStateEvent

A message encapsulating a series of Session states and the time that the DeviceSession first entered those states.

JSON representation  
---  
      
    
    {
      "sessionState": enum ([SessionState](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#SessionState)),
      "eventTime": string,
      "stateMessage": string
    }  
  
Fields  
---  
`sessionState` |  `enum (`[SessionState](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#SessionState)`)` Output only. The sessionState tracked by this event  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that the sessionState first encountered that state.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`stateMessage` |  `string` Output only. A human-readable message to explain the state.  
  
## AndroidDevice

A single Android device.

JSON representation  
---  
      
    
    {
      "androidModelId": string,
      "androidVersionId": string,
      "locale": string,
      "orientation": string
    }  
  
Fields  
---  
`androidModelId` |  `string` Required. The id of the Android device to be used. Use the TestEnvironmentDiscoveryService to get supported options.  
`androidVersionId` |  `string` Required. The id of the Android OS version to be used. Use the TestEnvironmentDiscoveryService to get supported options.  
`locale` |  `string` Optional. The locale the test device used for testing. Use the TestEnvironmentDiscoveryService to get supported options.  
`orientation` |  `string` Optional. How the device is oriented during the test. Use the TestEnvironmentDiscoveryService to get supported options.  
  
## ClientInfo

Information about the client which invoked the device session.

JSON representation  
---  
      
    
    {
      "client": string,
      "version": string
    }  
  
Fields  
---  
`client` |  `string` Required. Client name, such as gcloud. The maximum length is 64 characters.  
`version` |  `string` Optional. Client version. The maximum length is 64 characters.  
  
## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/cancel)`

|  Cancel a DeviceSession.  
  
### `[create](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/create)`

|  Creates a DeviceSession.  
  
### `[get](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/get)`

|  Gets a DeviceSession, which documents the allocation status and whether the device is allocated.  
  
### `[list](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/list)`

|  Lists DeviceSessions owned by the project user.  
  
### `[patch](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/patch)`

|  Updates the current DeviceSession to the fields described by the update_mask.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
