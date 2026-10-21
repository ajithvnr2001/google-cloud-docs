---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ImageImportOsAdaptationParameters/
title: ImageImportOsAdaptationParameters \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:39.939477+00:00
---

# ImageImportOsAdaptationParameters  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ImageImportOsAdaptationParameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  ImageImportOsAdaptationParameters Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Parameters affecting the OS adaptation process.

JSON representation  
---  
      
    
    {
      "generalize": boolean,
      "licenseType": enum ([ComputeEngineLicenseType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineLicenseType))
    }  
  
Fields  
---  
`generalize` |  `boolean` Optional. Set to true in order to generalize the imported image. The generalization process enables co-existence of multiple VMs created from the same image. For Windows, generalizing the image removes computer-specific information such as installed drivers and the computer security identifier (SID).  
`licenseType` |  `enum (`[ComputeEngineLicenseType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineLicenseType)`)` Optional. Choose which type of license to apply to the imported image.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
