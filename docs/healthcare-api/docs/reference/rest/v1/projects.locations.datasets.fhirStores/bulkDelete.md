---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/bulkDelete/
title: Method: fhirStores.bulkDelete \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:05.209496+00:00
---

# Method: fhirStores.bulkDelete  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/bulkDelete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  Method: fhirStores.bulkDelete Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.fhirStores.bulkDelete

Bulk deletes the FHIR resources from the given FHIR store.

This method returns an `[Operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)` that can be used to track the progress of the deletion by calling `operations.get`. The success and secondarySuccess counters correspond to the deleted current version and historical versions, respectively.

### HTTP request

`POST https://healthcare.googleapis.com/v1/{name=projects/*/locations/*/datasets/*/fhirStores/*}:bulkDelete`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the FHIR store to bulk delete resources from, in the format of `projects/{projectId}/locations/{locationId}/datasets/{datasetId}/fhirStores/{fhirStoreId}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.fhirStores.bulkDelete`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "versionConfig": enum([VersionConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/bulkDelete#VersionConfig)),
      "until": string,
      "type": string,
      "gcsDestination": {
        object([GcsDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/GcsDestination))
      },
      "validateOnly": boolean,
      "gcsSource": {
        object([GcsSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/GcsSource))
      }
    }  
  
Fields  
---  
`versionConfig` |  `enum(`[VersionConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/bulkDelete#VersionConfig)`)` Optional. Specifies which version of the resources to delete.  
`until` |  `string` Optional. If provided, only resources updated before or atthis time are deleted. The time uses the format YYYY-MM-DDThh:mm:ss.sss+zz:zz. For example, `2015-02-07T13:28:17.239+02:00` or `2017-01-01T00:00:00Z`. The time must be specified to the second and include a time zone.  
`type` |  `string` Optional. String of comma-delimited FHIR resource types. If provided, only resources of the specified resource type(s) will be deleted.  
`gcsDestination` |  `object(`[GcsDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/GcsDestination)`)` Optional. The Cloud Storage output destination.The Healthcare Service Agent account requires the `roles/storage.objectAdmin` role on the Cloud Storage location.The deleted resources outputs are organized by FHIR resource types. The server creates one or more objects per resource type. Each object contains newline delimited strings in the format {resourceType}/{resourceId}.  
`validateOnly` |  `boolean` Optional. If set to `true`, the request will only perform a dry run. By default this will default to `false`.  
`gcsSource` |  `object(`[GcsSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/GcsSource)`)` Optional. Specifies the Cloud Storage source data location containing the list of resource IDs to delete. Each file inside `gcsSource` must contain newline-delimited strings in the format `{resourceType}/{resourceId}`. This field is mutually exclusive with filter parameters such as `type` and `until`.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## VersionConfig

List of version configs for bulk delete FHIR resources.

Enums  
---  
`VERSION_CONFIG_UNSPECIFIED` | Unspecified version config. Defaults to ALL.  
`ALL` | Delete the current version and all history versions.  
`CURRENT_ONLY` | Delete the current version only and create a historical version of the deleted resource.  
`HISTORY_ONLY` | Delete all history versions only.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
