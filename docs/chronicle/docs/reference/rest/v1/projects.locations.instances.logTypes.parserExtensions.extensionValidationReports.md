---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.parserExtensions.extensionValidationReports
title: REST Resource: projects.locations.instances.logTypes.parserExtensions.extensionValidationReports \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:12.563628+00:00
---

# REST Resource: projects.locations.instances.logTypes.parserExtensions.extensionValidationReports  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.parserExtensions.extensionValidationReports

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.logTypes.parserExtensions.extensionValidationReports Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ExtensionValidationReport
    * JSON representation
  * Methods



## Resource: ExtensionValidationReport

ExtensionValidationReport describes the validation report of a parser. extension

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "validationErrors": [
        string
      ],
      "hasMoreValidationErrors": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of this extension validation report. Output only. The resource name of the extension validation report. Format: projects/{project}/locations/{location}/instances/{instance}/logTypes/{logType}/parserExtensions/{parserExtension}/extensionValidationReports/{extensionValidationReport}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the validation report was initiated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`validationErrors[]` |  `string` Any validation errors encountered when creating the extension, this have cap of size 10  
`hasMoreValidationErrors` |  `boolean` Output only. true, if there are more validation errors  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.parserExtensions.extensionValidationReports/get)`

|  Get a parser vaildation report.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.parserExtensions.extensionValidationReports/list)`

|  List all parser validation reports for a parser extension.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
