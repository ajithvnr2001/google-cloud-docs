---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/StreamData/
title: StreamData \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:59.094679+00:00
---

# StreamData  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/StreamData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  StreamData Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Close



Data for a stream.

JSON representation  
---  
      
    
    {
      "streamId": integer,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "data": string,
      "close": {
        object ([Close](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/StreamData#Close))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`streamId` |  `integer` Required. The unique ID of this stream, assigned by the client.  
The data of the stream, either bytes or "Close", indicating that the stream is done. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Data in the stream.A base64-encoded string.  
`close` |  `object (`[Close](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/StreamData#Close)`)` The stream is closing. EOF.  
End of mutually exclusive fields.  
  
## Close

This type has no fields.

Message signifying that the stream closed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
