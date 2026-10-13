---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationDetails/
title: TransformationDetails \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:52.064395+00:00
---

# TransformationDetails  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationDetails/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  TransformationDetails Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TransformationResultStatus
    * JSON representation
  * TransformationLocation
    * JSON representation



Details about a single transformation. This object contains a description of the transformation, information about whether the transformation was successfully applied, and the precise location where the transformation occurred. These details are stored in a user-specified BigQuery table.

JSON representation  
---  
      
    
    {
      "resourceName": string,
      "containerName": string,
      "transformation": [
        {
          object ([TransformationDescription](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationDescription))
        }
      ],
      "statusDetails": {
        object ([TransformationResultStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationDetails#TransformationResultStatus))
      },
      "transformedBytes": string,
      "transformationLocation": {
        object ([TransformationLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationDetails#TransformationLocation))
      }
    }  
  
Fields  
---  
`resourceName` |  `string` The name of the job that completed the transformation.  
`containerName` |  `string` The top level name of the container where the transformation is located (this will be the source file name or table name).  
`transformation[]` |  `object (`[TransformationDescription](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationDescription)`)` Description of transformation. This would only contain more than one element if there were multiple matching transformations and which one to apply was ambiguous. Not set for states that contain no transformation, currently only state that contains no transformation is TransformationResultStateType.METADATA_UNRETRIEVABLE.  
`statusDetails` |  `object (`[TransformationResultStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationDetails#TransformationResultStatus)`)` Status of the transformation, if transformation was not successful, this will specify what caused it to fail, otherwise it will show that the transformation was successful.  
`transformedBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of bytes that were transformed. If transformation was unsuccessful or did not take place because there was no content to transform, this will be zero.  
`transformationLocation` |  `object (`[TransformationLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationDetails#TransformationLocation)`)` The precise location of the transformed content in the original container.  
  
## TransformationResultStatus

The outcome of a transformation.

JSON representation  
---  
      
    
    {
      "resultStatusType": enum ([TransformationResultStatusType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationResultStatusType)),
      "details": {
        object ([Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Status))
      }
    }  
  
Fields  
---  
`resultStatusType` |  `enum (`[TransformationResultStatusType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationResultStatusType)`)` Transformation result status type, this will be either SUCCESS, or it will be the reason for why the transformation was not completely successful.  
`details` |  `object (`[Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Status)`)` Detailed error codes and messages  
  
## TransformationLocation

Specifies the location of a transformation.

JSON representation  
---  
      
    
    {
      "containerType": enum ([TransformationContainerType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationContainerType)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "findingId": string,
      "recordTransformation": {
        object ([RecordTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/RecordTransformation))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`containerType` |  `enum (`[TransformationContainerType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationContainerType)`)` Information about the functionality of the container where this finding occurred, if available.  
Location type. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`findingId` |  `string` For infotype transformations, link to the corresponding findings ID so that location information does not need to be duplicated. Each findings ID correlates to an entry in the findings output table, this table only gets created when users specify to save findings (add the save findings action to the request).  
`recordTransformation` |  `object (`[RecordTransformation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/RecordTransformation)`)` For record transformations, provide a field and container information.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
