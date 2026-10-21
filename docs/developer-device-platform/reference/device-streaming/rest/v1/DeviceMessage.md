---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/DeviceMessage/
title: DeviceMessage \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:59.236021+00:00
---

# DeviceMessage  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/DeviceMessage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  DeviceMessage Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * StatusUpdate
    * JSON representation
  * StreamStatus
    * JSON representation
  * Okay
  * Fail
    * JSON representation



A message returned from a device.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "statusUpdate": {
        object ([StatusUpdate](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/DeviceMessage#StatusUpdate))
      },
      "streamStatus": {
        object ([StreamStatus](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/DeviceMessage#StreamStatus))
      },
      "streamData": {
        object ([StreamData](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/StreamData))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`statusUpdate` |  `object (`[StatusUpdate](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/DeviceMessage#StatusUpdate)`)` Information about the device's state.  
`streamStatus` |  `object (`[StreamStatus](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/DeviceMessage#StreamStatus)`)` The result of a device stream from ADB.  
`streamData` |  `object (`[StreamData](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/StreamData)`)` Data from an open stream.  
End of mutually exclusive fields.  
  
## StatusUpdate

A StatusUpdate message given over the ADB protocol for the device state.

JSON representation  
---  
      
    
    {
      "state": enum ([DeviceState](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/DeviceState)),
      "properties": {
        string: string,
        ...
      },
      "features": string
    }  
  
Fields  
---  
`state` |  `enum (`[DeviceState](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/DeviceState)`)` The device's state  
`properties` |  `map (key: string, value: string)` A map of properties with information about this device.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`features` |  `string` A comma-separated list of "features" that this device supports.  
  
## StreamStatus

The result of a stream.

JSON representation  
---  
      
    
    {
      "streamId": integer,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "okay": {
        object ([Okay](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/DeviceMessage#Okay))
      },
      "fail": {
        object ([Fail](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/DeviceMessage#Fail))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`streamId` |  `integer` The unique ID of this stream, assigned by the client.  
The result of the stream. Either "Okay" for success or "Fail" for failure. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`okay` |  `object (`[Okay](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/DeviceMessage#Okay)`)` Okay for success.  
`fail` |  `object (`[Fail](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/DeviceMessage#Fail)`)` Fail for failure.  
End of mutually exclusive fields.  
  
## Okay

This type has no fields.

Message signifying that the stream is open

## Fail

Message signifying that the stream failed to open

JSON representation  
---  
      
    
    {
      "reason": string
    }  
  
Fields  
---  
`reason` |  `string` A user-displayable failure reason.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
