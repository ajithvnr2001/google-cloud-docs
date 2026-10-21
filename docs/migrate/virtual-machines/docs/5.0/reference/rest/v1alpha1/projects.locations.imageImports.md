---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports
title: REST Resource: projects.locations.imageImports \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:42.953967+00:00
---

# REST Resource: projects.locations.imageImports  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  REST Resource: projects.locations.imageImports Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ImageImport
    * JSON representation
  * Methods



## Resource: ImageImport

ImageImport describes the configuration of the image import to run.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "recentImageImportJobs": [
        {
          object ([ImageImportJob](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports.imageImportJobs#ImageImportJob))
        }
      ],
      "encryption": {
        object ([Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption))
      },
    
      // Union field source can be only one of the following:
      "cloudStorageUri": string
      // End of list of possible types for union field source.
    
      // Union field target_defaults can be only one of the following:
      "diskImageTargetDefaults": {
        object ([DiskImageTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/DiskImageTargetDetails))
      },
      "machineImageTargetDefaults": {
        object ([MachineImageTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails))
      }
      // End of list of possible types for union field target_defaults.
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource path of the ImageImport.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the image import was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`recentImageImportJobs[]` |  `object (`[ImageImportJob](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports.imageImportJobs#ImageImportJob)`)` Output only. The result of the most recent runs for this ImageImport. All jobs for this ImageImport can be listed via ListImageImportJobs.  
`encryption` |  `object (`[Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption)`)` Immutable. The encryption details used by the image import process during the image adaptation for Compute Engine.  
Union field `source`.`source` can be only one of the following:  
`cloudStorageUri` |  `string` Immutable. The path to the Cloud Storage file from which the image should be imported.  
Union field `target_defaults`. The configuration of the resources that will be created in GCP as a result of the ImageImport. `target_defaults` can be only one of the following:  
`diskImageTargetDefaults` |  `object (`[DiskImageTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/DiskImageTargetDetails)`)` Immutable. Target details for importing a disk image, will be used by ImageImportJob.  
`machineImageTargetDefaults` |  `object (`[MachineImageTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/MachineImageTargetDetails)`)` Immutable. Target details for importing a machine image, will be used by ImageImportJob.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports/create)`

|  Creates a new ImageImport in a given project.  
  
### `[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports/delete)`

|  Deletes a single ImageImport.  
  
### `[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports/get)`

|  Gets details of a single ImageImport.  
  
### `[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports/list)`

|  Lists ImageImports in a given project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
