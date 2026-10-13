---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationOverview/
title: TransformationOverview \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:51.620493+00:00
---

# TransformationOverview  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationOverview/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  TransformationOverview Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TransformationSummary
    * JSON representation
  * SummaryResult
    * JSON representation
  * TransformationResultCode



Overview of the modifications that occurred.

JSON representation  
---  
      
    
    {
      "transformedBytes": string,
      "transformationSummaries": [
        {
          object ([TransformationSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationOverview#TransformationSummary))
        }
      ]
    }  
  
Fields  
---  
`transformedBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total size in bytes that were transformed in some way.  
`transformationSummaries[]` |  `object (`[TransformationSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationOverview#TransformationSummary)`)` Transformations applied to the dataset.  
  
## TransformationSummary

Summary of a single transformation. Only one of 'transformation', 'field_transformation', or 'recordSuppress' will be set.

JSON representation  
---  
      
    
    {
      "infoType": {
        object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
      },
      "field": {
        object ([FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FieldId))
      },
      "transformation": {
        object ([PrimitiveTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.PrimitiveTransformation))
      },
      "fieldTransformations": [
        {
          object ([FieldTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.FieldTransformation))
        }
      ],
      "recordSuppress": {
        object ([RecordSuppression](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.RecordSuppression))
      },
      "results": [
        {
          object ([SummaryResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationOverview#SummaryResult))
        }
      ],
      "transformedBytes": string
    }  
  
Fields  
---  
`infoType` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` Set if the transformation was limited to a specific InfoType.  
`field` |  `object (`[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FieldId)`)` Set if the transformation was limited to a specific FieldId.  
`transformation` |  `object (`[PrimitiveTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.PrimitiveTransformation)`)` The specific transformation these stats apply to.  
`fieldTransformations[]` |  `object (`[FieldTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.FieldTransformation)`)` The field transformation that was applied. If multiple field transformations are requested for a single field, this list will contain all of them; otherwise, only one is supplied.  
`recordSuppress` |  `object (`[RecordSuppression](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.RecordSuppression)`)` The specific suppression option these stats apply to.  
`results[]` |  `object (`[SummaryResult](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationOverview#SummaryResult)`)` Collection of all transformations that took place or had an error.  
`transformedBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total size in bytes that were transformed in some way.  
  
## SummaryResult

A collection that informs the user the number of times a particular `TransformationResultCode` and error details occurred.

JSON representation  
---  
      
    
    {
      "count": string,
      "code": enum ([TransformationResultCode](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationOverview#TransformationResultCode)),
      "details": string
    }  
  
Fields  
---  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of transformations counted by this result.  
`code` |  `enum (`[TransformationResultCode](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationOverview#TransformationResultCode)`)` Outcome of the transformation.  
`details` |  `string` A place for warnings or errors to show up if a transformation didn't work as expected.  
  
## TransformationResultCode

Possible outcomes of transformations.

Enums  
---  
`TRANSFORMATION_RESULT_CODE_UNSPECIFIED` | Unused  
`SUCCESS` | Transformation completed without an error.  
`ERROR` | Transformation had an error.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
