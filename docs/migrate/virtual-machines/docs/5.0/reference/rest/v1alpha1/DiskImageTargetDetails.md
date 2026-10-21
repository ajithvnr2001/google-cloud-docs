---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/DiskImageTargetDetails/
title: DiskImageTargetDetails \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:51.078040+00:00
---

# DiskImageTargetDetails  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/DiskImageTargetDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  DiskImageTargetDetails Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DataDiskImageImport



The target details of the image resource that will be created by the import job.

JSON representation  
---  
      
    
    {
      "imageName": string,
      "targetProject": string,
      "description": string,
      "familyName": string,
      "labels": {
        string: string,
        ...
      },
      "additionalLicenses": [
        string
      ],
      "singleRegionStorage": boolean,
      "encryption": {
        object ([Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption))
      },
    
      // Union field os_adaptation_config can be only one of the following:
      "osAdaptationParameters": {
        object ([ImageImportOsAdaptationParameters](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ImageImportOsAdaptationParameters))
      },
      "dataDiskImageImport": {
        object ([DataDiskImageImport](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/DiskImageTargetDetails#DataDiskImageImport))
      }
      // End of list of possible types for union field os_adaptation_config.
    }  
  
Fields  
---  
`imageName` |  `string` Required. The name of the image to be created.  
`targetProject` |  `string` Required. Reference to the TargetProject resource that represents the target project in which the imported image will be created.  
`description` |  `string` Optional. An optional description of the image.  
`familyName` |  `string` Optional. The name of the image family to which the new image belongs.  
`labels` |  `map (key: string, value: string)` Optional. A map of labels to associate with the image.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`additionalLicenses[]` |  `string` Optional. Additional licenses to assign to the image. Format: <https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/licenses/LICENSE_NAME> Or <https://www.googleapis.com/compute/beta/projects/PROJECT_ID/global/licenses/LICENSE_NAME>  
`singleRegionStorage` |  `boolean` Optional. Set to true to set the image storageLocations to the single region of the import job. When false, the closest multi-region is selected.  
`encryption` |  `object (`[Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption)`)` Immutable. The encryption to apply to the image.  
Union field `os_adaptation_config`.`os_adaptation_config` can be only one of the following:  
`osAdaptationParameters` |  `object (`[ImageImportOsAdaptationParameters](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ImageImportOsAdaptationParameters)`)` Optional. Use to set the parameters relevant for the OS adaptation process.  
`dataDiskImageImport` |  `object (`[DataDiskImageImport](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/DiskImageTargetDetails#DataDiskImageImport)`)` Optional. Use to skip OS adaptation process.  
  
## DataDiskImageImport

This type has no fields.

Mentions that the image import is not using OS adaptation process.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
