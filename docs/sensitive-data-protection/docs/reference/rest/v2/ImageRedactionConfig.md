---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ImageRedactionConfig/
title: ImageRedactionConfig \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:45.726074+00:00
---

# ImageRedactionConfig  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ImageRedactionConfig/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  ImageRedactionConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Configuration for determining how redaction of images should occur.

JSON representation  
---  
      
    
    {
      "redactionColor": {
        object ([Color](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.Color))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "infoType": {
        object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
      },
      "redactAllText": boolean
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`redactionColor` |  `object (`[Color](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.Color)`)` The color to use when redacting content from an image. If not specified, the default is black.  
Type of information to redact from images. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`infoType` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` Only one per infoType should be provided per request. If not specified, and redactAllText is false, the DLP API will redact all text that it matches against all infoTypes that are found, but not specified in another ImageRedactionConfig.  
`redactAllText` |  `boolean` If true, all text found in the image, regardless whether it matches an infoType, is redacted. Only one should be provided.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
