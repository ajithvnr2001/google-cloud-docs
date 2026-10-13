---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/getDICOMStoreMetrics/
title: Method: dicomStores.getDICOMStoreMetrics \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:27.959193+00:00
---

# Method: dicomStores.getDICOMStoreMetrics  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/getDICOMStoreMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  Method: dicomStores.getDICOMStoreMetrics Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.dicomStores.getDICOMStoreMetrics

Gets metrics associated with the DICOM store.

### HTTP request

`GET https://healthcare.googleapis.com/v1/{name=projects/*/locations/*/datasets/*/dicomStores/*}:getDICOMStoreMetrics`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the DICOM store to get metrics for. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.dicomStores.get`

  
  
### Request body

The request body must be empty.

### Response body

DicomStoreMetrics contains metrics describing a DICOM store.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "name": string,
      "studyCount": string,
      "seriesCount": string,
      "instanceCount": string,
      "structuredStorageSizeBytes": string,
      "blobStorageSizeBytes": string
    }  
  
Fields  
---  
`name` |  `string` Resource name of the DICOM store, of the form `projects/{projectId}/locations/{locationId}/datasets/{datasetId}/dicomStores/{dicomStoreId}`.  
`studyCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of studies in the store.  
`seriesCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of series in the store.  
`instanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances in the store.  
`structuredStorageSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total structured storage bytes for all instances in the store.  
`blobStorageSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total blob storage bytes for all instances in the store.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
