---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/AdbMessage/
title: AdbMessage \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:58.912601+00:00
---

# AdbMessage  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/AdbMessage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  AdbMessage Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Open
    * JSON representation



A message to an ADB server.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "open": {
        object ([Open](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/AdbMessage#Open))
      },
      "streamData": {
        object ([StreamData](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/StreamData))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`open` |  `object (`[Open](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/AdbMessage#Open)`)` Open a new stream.  
`streamData` |  `object (`[StreamData](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/StreamData)`)` Send data to a stream.  
End of mutually exclusive fields.  
  
## Open

Message for opening a new stream.

JSON representation  
---  
      
    
    {
      "streamId": integer,
      "service": string
    }  
  
Fields  
---  
`streamId` |  `integer` Required. The unique ID that will be used to talk to this stream. This should probably just be a number that increments for each new Open request.  
`service` |  `string` Optional. An ADB service to use in the new stream.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
