---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores/setBlobStorageSettings/
title: Method: dicomStores.setBlobStorageSettings \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:58.952516+00:00
---

# Method: dicomStores.setBlobStorageSettings  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores/setBlobStorageSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  Method: dicomStores.setBlobStorageSettings Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.dicomStores.setBlobStorageSettings

dicomStores.setBlobStorageSettings sets the blob storage settings of the specified resources.

### HTTP request

`POST https://healthcare.googleapis.com/v1beta1/{resource=projects/*/locations/*/datasets/*/dicomStores/*}:setBlobStorageSettings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`resource` |  `string` Required. The path of the resource to update the blob storage settings in the format of `projects/{projectID}/locations/{locationID}/datasets/{datasetID}/dicomStores/{dicomStoreID}/dicomWeb/studies/{studyUID}`, `projects/{projectID}/locations/{locationID}/datasets/{datasetID}/dicomStores/{dicomStoreID}/dicomWeb/studies/{studyUID}/series/{seriesUID}/`, or `projects/{projectID}/locations/{locationID}/datasets/{datasetID}/dicomStores/{dicomStoreID}/dicomWeb/studies/{studyUID}/series/{seriesUID}/instances/{instanceUID}`. If `filterConfig` is specified, set the value of `resource` to the resource name of a DICOM store in the format `projects/{projectID}/locations/{locationID}/datasets/{datasetID}/dicomStores/{dicomStoreID}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `resource`:

  * `healthcare.dicomStores.dicomWebWrite`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "filterConfig": {
        object([DicomFilterConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/DicomFilterConfig))
      },
      "blobStorageSettings": {
        object([BlobStorageSettings](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/BlobStorageSettings))
      }
    }  
  
Fields  
---  
`filterConfig` |  `object(`[DicomFilterConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/DicomFilterConfig)`)` Optional. A filter configuration. If `filterConfig` is specified, set the value of `resource` to the resource name of a DICOM store in the format `projects/{projectID}/locations/{locationID}/datasets/{datasetID}/dicomStores/{dicomStoreID}`.  
`blobStorageSettings` |  `object(`[BlobStorageSettings](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/BlobStorageSettings)`)` The blob storage settings to update for the specified resources. Only fields listed in `updateMask` are applied.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
