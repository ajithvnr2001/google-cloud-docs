---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs
title: REST Resource: projects.locations.imageImports.imageImportJobs \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:31.961925+00:00
---

# REST Resource: projects.locations.imageImports.imageImportJobs  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  REST Resource: projects.locations.imageImports.imageImportJobs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ImageImportJob
    * JSON representation
    * State
    * ImageImportStep
      * JSON representation
    * InitializingImageImportStep
    * LoadingImageSourceFilesStep
    * CreatingImageStep
  * Methods



## Resource: ImageImportJob

ImageImportJob describes the progress and result of an image import.

JSON representation  
---  
      
    
    {
      "name": string,
      "createdResources": [
        string
      ],
      "state": enum ([State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs#ImageImportJob.State)),
      "createTime": string,
      "endTime": string,
      "errors": [
        {
          object ([Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/Status))
        }
      ],
      "warnings": [
        {
          object ([MigrationWarning](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/MigrationWarning))
        }
      ],
      "steps": [
        {
          object ([ImageImportStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs#ImageImportJob.ImageImportStep))
        }
      ],
    
      // Union field source can be only one of the following:
      "cloudStorageUri": string
      // End of list of possible types for union field source.
    
      // Union field target_details can be only one of the following:
      "diskImageTargetDetails": {
        object ([DiskImageTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/DiskImageTargetDetails))
      },
      "machineImageTargetDetails": {
        object ([MachineImageTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/MachineImageTargetDetails))
      }
      // End of list of possible types for union field target_details.
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource path of the ImageImportJob.  
`createdResources[]` |  `string` Output only. The resource paths of the resources created by the image import job.  
`state` |  `enum (`[State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs#ImageImportJob.State)`)` Output only. The state of the image import.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the image import was created (as an API call, not when it was actually created in the target).A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the image import was ended.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`errors[]` |  `object (`[Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/Status)`)` Output only. Provides details on the error that led to the image import state in case of an error.  
`warnings[]` |  `object (`[MigrationWarning](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/MigrationWarning)`)` Output only. Warnings that occurred during the image import.  
`steps[]` |  `object (`[ImageImportStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs#ImageImportJob.ImageImportStep)`)` Output only. The image import steps list representing its progress.  
Union field `source`.`source` can be only one of the following:  
`cloudStorageUri` |  `string` Output only. The path to the Cloud Storage file from which the image should be imported.  
Union field `target_details`. The configuration of the resources that were created in GCP as a result of the image import. `target_details` can be only one of the following:  
`diskImageTargetDetails` |  `object (`[DiskImageTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/DiskImageTargetDetails)`)` Output only. Target details used to import a disk image.  
`machineImageTargetDetails` |  `object (`[MachineImageTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/MachineImageTargetDetails)`)` Output only. Target details used to import a machine image.  
  
### State

Possible states of the image import.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unknown.  
`PENDING` | The image import has not yet started.  
`RUNNING` | The image import is active and running.  
`SUCCEEDED` | The image import has finished successfully.  
`FAILED` | The image import has finished with errors.  
`CANCELLING` | The image import is being cancelled.  
`CANCELLED` | The image import was cancelled.  
  
### ImageImportStep

ImageImportStep holds information about the image import step progress.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
    
      // Union field step can be only one of the following:
      "initializing": {
        object ([InitializingImageImportStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs#ImageImportJob.InitializingImageImportStep))
      },
      "loadingSourceFiles": {
        object ([LoadingImageSourceFilesStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs#ImageImportJob.LoadingImageSourceFilesStep))
      },
      "adaptingOs": {
        object ([AdaptingOSStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/AdaptingOSStep))
      },
      "creatingImage": {
        object ([CreatingImageStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs#ImageImportJob.CreatingImageStep))
      }
      // End of list of possible types for union field step.
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the step has started.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the step has ended.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
Union field `step`.`step` can be only one of the following:  
`initializing` |  `object (`[InitializingImageImportStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs#ImageImportJob.InitializingImageImportStep)`)` Initializing step.  
`loadingSourceFiles` |  `object (`[LoadingImageSourceFilesStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs#ImageImportJob.LoadingImageSourceFilesStep)`)` Loading source files step.  
`adaptingOs` |  `object (`[AdaptingOSStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/AdaptingOSStep)`)` Adapting OS step.  
`creatingImage` |  `object (`[CreatingImageStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs#ImageImportJob.CreatingImageStep)`)` Creating image step.  
  
### InitializingImageImportStep

This type has no fields.

InitializingImageImportStep contains specific step details.

### LoadingImageSourceFilesStep

This type has no fields.

LoadingImageSourceFilesStep contains specific step details.

### CreatingImageStep

This type has no fields.

CreatingImageStep contains specific step details.

## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs/cancel)`

|  Initiates the cancellation of a running clone job.  
  
### `[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs/get)`

|  Gets details of a single ImageImportJob.  
  
### `[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports.imageImportJobs/list)`

|  Lists ImageImportJobs in a given project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
