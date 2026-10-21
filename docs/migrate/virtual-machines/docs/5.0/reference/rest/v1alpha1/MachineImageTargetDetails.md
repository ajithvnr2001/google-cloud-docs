---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails/
title: MachineImageTargetDetails \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:11.670028+00:00
---

# MachineImageTargetDetails  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  MachineImageTargetDetails Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SkipOsAdaptation
  * MachineImageParametersOverrides
    * JSON representation
  * ServiceAccount
    * JSON representation
  * ShieldedInstanceConfig
    * JSON representation
  * SecureBoot



The target details of the machine image resource that will be created by the image import job.

JSON representation  
---  
      
    
    {
      "machineImageName": string,
      "targetProject": string,
      "description": string,
      "singleRegionStorage": boolean,
      "encryption": {
        object ([Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption))
      },
      "machineImageParametersOverrides": {
        object ([MachineImageParametersOverrides](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails#MachineImageParametersOverrides))
      },
      "serviceAccount": {
        object ([ServiceAccount](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails#ServiceAccount))
      },
      "additionalLicenses": [
        string
      ],
      "labels": {
        string: string,
        ...
      },
      "tags": [
        string
      ],
      "shieldedInstanceConfig": {
        object ([ShieldedInstanceConfig](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails#ShieldedInstanceConfig))
      },
      "networkInterfaces": [
        {
          object ([NetworkInterface](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface))
        }
      ],
    
      // Union field os_adaptation_config can be only one of the following:
      "osAdaptationParameters": {
        object ([ImageImportOsAdaptationParameters](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ImageImportOsAdaptationParameters))
      },
      "skipOsAdaptation": {
        object ([SkipOsAdaptation](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails#SkipOsAdaptation))
      }
      // End of list of possible types for union field os_adaptation_config.
    }  
  
Fields  
---  
`machineImageName` |  `string` Required. The name of the machine image to be created.  
`targetProject` |  `string` Required. Reference to the TargetProject resource that represents the target project in which the imported machine image will be created.  
`description` |  `string` Optional. An optional description of the machine image.  
`singleRegionStorage` |  `boolean` Optional. Set to true to set the machine image storageLocations to the single region of the import job. When false, the closest multi-region is selected.  
`encryption` |  `object (`[Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption)`)` Immutable. The encryption to apply to the machine image.  
`machineImageParametersOverrides` |  `object (`[MachineImageParametersOverrides](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails#MachineImageParametersOverrides)`)` Optional. Parameters overriding decisions based on the source machine image configurations.  
`serviceAccount` |  `object (`[ServiceAccount](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails#ServiceAccount)`)` Optional. The service account to assign to the instance created by the machine image.  
`additionalLicenses[]` |  `string` Optional. Additional licenses to assign to the instance created by the machine image. Format: <https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/licenses/LICENSE_NAME> Or <https://www.googleapis.com/compute/beta/projects/PROJECT_ID/global/licenses/LICENSE_NAME>  
`labels` |  `map (key: string, value: string)` Optional. The labels to apply to the instance created by the machine image.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`tags[]` |  `string` Optional. The tags to apply to the instance created by the machine image.  
`shieldedInstanceConfig` |  `object (`[ShieldedInstanceConfig](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails#ShieldedInstanceConfig)`)` Optional. Shielded instance configuration.  
`networkInterfaces[]` |  `object (`[NetworkInterface](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface)`)` Optional. The network interfaces to create with the instance created by the machine image. Internal and external IP addresses are ignored for machine image import.  
Union field `os_adaptation_config`.`os_adaptation_config` can be only one of the following:  
`osAdaptationParameters` |  `object (`[ImageImportOsAdaptationParameters](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ImageImportOsAdaptationParameters)`)` Optional. Use to set the parameters relevant for the OS adaptation process.  
`skipOsAdaptation` |  `object (`[SkipOsAdaptation](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails#SkipOsAdaptation)`)` Optional. Use to skip OS adaptation process.  
  
## SkipOsAdaptation

This type has no fields.

Mentions that the machine image import is not using OS adaptation process.

## MachineImageParametersOverrides

Parameters overriding decisions based on the source machine image configurations.

JSON representation  
---  
      
    
    {
      "machineType": string
    }  
  
Fields  
---  
`machineType` |  `string` Optional. The machine type to create the MachineImage with. If empty, the service will choose a relevant machine type based on the information from the source image. For more information about machine types, please refer to <https://cloud.google.com/compute/docs/machine-resource>.  
  
## ServiceAccount

Service account to assign to the instance created by the machine image.

JSON representation  
---  
      
    
    {
      "email": string,
      "scopes": [
        string
      ]
    }  
  
Fields  
---  
`email` |  `string` Required. The email address of the service account.  
`scopes[]` |  `string` Optional. The list of scopes to be made available for this service account.  
  
## ShieldedInstanceConfig

Shielded instance configuration.

JSON representation  
---  
      
    
    {
      "secureBoot": enum ([SecureBoot](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails#SecureBoot)),
      "enableVtpm": boolean,
      "enableIntegrityMonitoring": boolean
    }  
  
Fields  
---  
`secureBoot` |  `enum (`[SecureBoot](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails#SecureBoot)`)` Optional. Defines whether the instance created by the machine image has Secure Boot enabled. This can be set to true only if the image boot option is EFI.  
`enableVtpm` |  `boolean` Optional. Defines whether the instance created by the machine image has vTPM enabled. This can be set to true only if the image boot option is EFI.  
`enableIntegrityMonitoring` |  `boolean` Optional. Defines whether the instance created by the machine image has integrity monitoring enabled. This can be set to true only if the image boot option is EFI, and vTPM is enabled.  
  
## SecureBoot

Possible values for secure boot.

Enums  
---  
`SECURE_BOOT_UNSPECIFIED` | No explicit value is selected. Will use the configuration of the source (if exists, otherwise the default will be false).  
`TRUE` | Use secure boot. This can be set to true only if the image boot option is EFI.  
`FALSE` | Do not use secure boot.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
