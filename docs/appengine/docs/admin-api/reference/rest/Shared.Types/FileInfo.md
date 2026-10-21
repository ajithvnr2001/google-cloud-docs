---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/FileInfo/
title: FileInfo \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:33:08.275056+00:00
---

# FileInfo  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/FileInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)



Send feedback 

#  FileInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Single source file that is part of the version to be deployed. Each source file that is deployed must be specified separately.

JSON representation  
---  
      
    
    {
      "sourceUrl": string,
      "sha1Sum": string,
      "mimeType": string,
    }  
  
Fields  
---  
`sourceUrl` |  `string` URL source to use to fetch this file. Must be a URL to a resource in Google Cloud Storage in the form 'http(s)://storage.googleapis.com/<bucket>/<object>'.   
`sha1Sum` |  `string` The SHA1 hash of the file, in hex.   
`mimeType` |  `string` The MIME type of the file.Defaults to the value from Google Cloud Storage.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
