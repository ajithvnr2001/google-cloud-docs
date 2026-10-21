---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineTargetDetails/
title: ComputeEngineTargetDetails \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:50.586525+00:00
---

# ComputeEngineTargetDetails  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineTargetDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  ComputeEngineTargetDetails Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



ComputeEngineTargetDetails is a collection of details for creating a VM in a target Compute Engine project.

JSON representation  
---  
      
    
    {
      "vmName": string,
      "project": string,
      "zone": string,
      "machineTypeSeries": string,
      "machineType": string,
      "networkTags": [
        string
      ],
      "networkInterfaces": [
        {
          object ([NetworkInterface](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface))
        }
      ],
      "serviceAccount": string,
      "diskType": enum ([ComputeEngineDiskType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineDiskType)),
      "labels": {
        string: string,
        ...
      },
      "licenseType": enum ([ComputeEngineLicenseType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineLicenseType)),
      "appliedLicense": {
        object ([AppliedLicense](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/AppliedLicense))
      },
      "computeScheduling": {
        object ([ComputeScheduling](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeScheduling))
      },
      "secureBoot": boolean,
      "enableVtpm": boolean,
      "enableIntegrityMonitoring": boolean,
      "bootOption": enum ([ComputeEngineBootOption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineBootOption)),
      "metadata": {
        string: string,
        ...
      },
      "additionalLicenses": [
        string
      ],
      "hostname": string,
      "encryption": {
        object ([Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption))
      },
      "bootConversion": enum ([BootConversion](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/BootConversion))
    }  
  
Fields  
---  
`vmName` |  `string` The name of the VM to create.  
`project` |  `string` The Google Cloud target project ID or project name.  
`zone` |  `string` The zone in which to create the VM.  
`machineTypeSeries` |  `string` The machine type series to create the VM with.  
`machineType` |  `string` The machine type to create the VM with.  
`networkTags[]` |  `string` A list of network tags to associate with the VM.  
`networkInterfaces[]` |  `object (`[NetworkInterface](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface)`)` List of NICs connected to this VM.  
`serviceAccount` |  `string` The service account to associate the VM with.  
`diskType` |  `enum (`[ComputeEngineDiskType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineDiskType)`)` The disk type to use in the VM.  
`labels` |  `map (key: string, value: string)` A map of labels to associate with the VM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`licenseType` |  `enum (`[ComputeEngineLicenseType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineLicenseType)`)` The license type to use in OS adaptation.  
`appliedLicense` |  `object (`[AppliedLicense](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/AppliedLicense)`)` The OS license returned from the adaptation module report.  
`computeScheduling` |  `object (`[ComputeScheduling](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeScheduling)`)` Compute instance scheduling information (if empty default is used).  
`secureBoot` |  `boolean` Defines whether the instance has Secure Boot enabled. This can be set to true only if the VM boot option is EFI.  
`enableVtpm` |  `boolean` Optional. Defines whether the instance has vTPM enabled.  
`enableIntegrityMonitoring` |  `boolean` Optional. Defines whether the instance has integrity monitoring enabled.  
`bootOption` |  `enum (`[ComputeEngineBootOption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineBootOption)`)` The VM Boot Option, as set in the source VM.  
`metadata` |  `map (key: string, value: string)` The metadata key/value pairs to assign to the VM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`additionalLicenses[]` |  `string` Additional licenses to assign to the VM.  
`hostname` |  `string` The hostname to assign to the VM.  
`encryption` |  `object (`[Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption)`)` Optional. The encryption to apply to the VM disks.  
`bootConversion` |  `enum (`[BootConversion](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/BootConversion)`)` Optional. By default the virtual machine will keep its existing boot option. Setting this property will trigger an internal process which will convert the virtual machine from using the existing boot option to another.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
