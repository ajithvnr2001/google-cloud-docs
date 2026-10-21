---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ExportOptions/
title: ExportOptions \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:46:12.247687+00:00
---

# ExportOptions  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ExportOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  ExportOptions Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ExportOptions.ExportFormat



Options for exporting CES evaluation resources.

JSON representation  
---  
      
    
    {
      "exportFormat": enum ([ExportOptions.ExportFormat](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ExportOptions#ExportOptions.ExportFormat)),
      "gcsUri": string
    }  
  
Fields  
---  
`exportFormat` |  `enum (`[ExportOptions.ExportFormat](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ExportOptions#ExportOptions.ExportFormat)`)` Optional. The format to export the evaluation results in. Defaults to JSON if not specified.  
`gcsUri` |  `string` Optional. The Google Cloud Storage URI to write the exported Evaluation Results to.  
  
## ExportOptions.ExportFormat

The format to export the items in. Defaults to JSON if not specified.

Enums  
---  
`EXPORT_FORMAT_UNSPECIFIED` | Unspecified format.  
`JSON` | JSON format.  
`YAML` | YAML format.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
