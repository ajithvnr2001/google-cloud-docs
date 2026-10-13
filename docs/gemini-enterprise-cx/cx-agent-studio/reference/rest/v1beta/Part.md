---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Part/
title: Part \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:00.376742+00:00
---

# Part  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Part/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Part Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



`Part` represents a container for a section of communication content. Parts can be purely textual, some sort of file (image, video, etc) or a structured data blob (i.e. JSON).

JSON representation  
---  
      
    
    {
      "metadata": {
        object
      },
      "filename": string,
      "mediaType": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": string,
      "raw": string,
      "url": string,
      "data": value
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. metadata associated with this part.  
`filename` |  `string` An optional `filename` for the file (e.g., "document.pdf").  
`mediaType` |  `string` The `mediaType` (MIME type) of the part content (e.g., "text/plain", "application/json", "image/png"). This field is available for all part types.  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `string` The string content of the `text` part.  
`raw` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The `raw` byte content of a file. In JSON serialization, this is encoded as a base64 string.A base64-encoded string.  
`url` |  `string` A `url` pointing to the file's content.  
`data` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Arbitrary structured `data` as a JSON value (object, array, string, number, boolean, or null).  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
