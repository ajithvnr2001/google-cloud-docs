---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores/exportHistory/
title: Method: fhirStores.exportHistory \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:07.567248+00:00
---

# Method: fhirStores.exportHistory  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores/exportHistory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  Method: fhirStores.exportHistory Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.fhirStores.exportHistory

Export resources including historical versions from the FHIR store to the specified destination. The exported resource, along with previous versions, will be exported in one or more FHIR history bundles.

This method returns an `[Operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)` that can be used to track the status of the export by calling `operations.get`.

Immediate fatal errors appear in the `[error](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation.FIELDS.error)` field, errors are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). Otherwise, when the operation finishes, a detailed response of type `ExportResourcesResponse` is returned in the `[response](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation.FIELDS.response)` field. The `[metadata](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation.FIELDS.metadata)` field type for this operation is `[OperationMetadata](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/OperationMetadata)`.

### HTTP request

`POST https://healthcare.googleapis.com/v1beta1/{name=projects/*/locations/*/datasets/*/fhirStores/*}:exportHistory`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the FHIR store to export resource from, in the format `projects/{projectId}/locations/{locationId}/datasets/{datasetId}/fhirStores/{fhirStoreId}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.fhirStores.export`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "maxResourceVersions": string,
      "_since": string,
      "_type": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsDestination": {
        object([GcsDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/GcsDestination))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`maxResourceVersions` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` If provided and non-zero, places a limit on the number of resource versions that are returned for a given resource. For example, if the limit is `100` and a resource has over 100 versions, only the 100 most recent versions will be returned. Must be positive.  
`_since` |  `string` If provided, only resources versions updated after this time are exported. The time uses the format YYYY-MM-DDThh:mm:ss.sss+zz:zz. For example, `2015-02-07T13:28:17.239+02:00` or `2017-01-01T00:00:00Z`. The time must be specified to the second and include a time zone.  
`_type` |  `string` String of comma-delimited FHIR resource types. If provided, only resources of the specified resource type(s) are exported.  
The output destination of the export.To enable the Cloud Healthcare API to write to resources in your project such as Cloud Storage buckets, you must grant the Healthcare Service Agent account the required permissions. For steps to assign the permissions, see [Exporting data to Cloud Storage](https://cloud.google.com/healthcare/docs/how-tos/permissions-healthcare-api-gcp-products#exporting_data_to_cloud_storage). The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsDestination` |  `object(`[GcsDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/GcsDestination)`)` The Cloud Storage output destination.The Healthcare Service Agent account requires the `roles/storage.objectAdmin` role on the Cloud Storage location.The exported outputs are organized by FHIR resource types. The server creates one or more objects per resource type depending on the volume of the resources exported. When there is only one object per resource type, the object name is in the form of `{operation_id})_history_{resourceType}`. When there are multiple objects for a given resource type, the object names are in the form of `{operation_id}_history_{resourceType}-{index}-of-{total}`.Each object contains newline delimited JSON, and each line is a FHIR history bundle containing the history for a single resource.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
