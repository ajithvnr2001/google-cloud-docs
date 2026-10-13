---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationDescription/
title: TransformationDescription \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:51.146973+00:00
---

# TransformationDescription  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationDescription/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  TransformationDescription Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



A flattened description of a `PrimitiveTransformation` or `RecordSuppression`.

JSON representation  
---  
      
    
    {
      "type": enum ([TransformationType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationType)),
      "description": string,
      "condition": string,
      "infoType": {
        object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
      }
    }  
  
Fields  
---  
`type` |  `enum (`[TransformationType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationType)`)` The transformation type.  
`description` |  `string` A description of the transformation. This is empty for a RECORD_SUPPRESSION, or is the output of calling toString() on the `PrimitiveTransformation` protocol buffer message for any other type of transformation.  
`condition` |  `string` A human-readable string representation of the `RecordCondition` corresponding to this transformation. Set if a `RecordCondition` was used to determine whether or not to apply this transformation.Examples: * (age_field > 85) * (age_field <= 18) * (zip_field exists) * (zip_field == 01234) && (city_field != "Springville") * (zip_field == 01234) && (age_field <= 18) && (city_field exists)  
`infoType` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` Set if the transformation was limited to a specific `InfoType`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
