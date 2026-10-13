---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.parsers.validationReports
title: REST Resource: projects.locations.instances.logTypes.parsers.validationReports \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:33.314230+00:00
---

# REST Resource: projects.locations.instances.logTypes.parsers.validationReports  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.parsers.validationReports

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.logTypes.parsers.validationReports Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ValidationReport
    * JSON representation
  * Methods



## Resource: ValidationReport

ValidationReport describes the validation status of a parser/extension when it was created.

JSON representation  
---  
      
    
    {
      "name": string,
      "verdict": enum ([Verdict](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.parserExtensions.validationReports#ValidationReport.Verdict)),
      "stats": {
        object ([Stats](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.parserExtensions.validationReports#ValidationReport.Stats))
      },
      "error": {
        object ([ParsingValidationErrors](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.parserExtensions.validationReports#ValidationReport.ParsingValidationErrors))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. name of the validation report resource.  
`verdict` |  `enum (`[Verdict](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.parserExtensions.validationReports#ValidationReport.Verdict)`)` Verdict of the validation.  
`stats` |  `object (`[Stats](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.parserExtensions.validationReports#ValidationReport.Stats)`)` Stats of the validation.  
`error` |  `object (`[ParsingValidationErrors](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.parserExtensions.validationReports#ValidationReport.ParsingValidationErrors)`)` Errors occurred during validation.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes.parsers.validationReports/get)`

|  Get a validation report.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
