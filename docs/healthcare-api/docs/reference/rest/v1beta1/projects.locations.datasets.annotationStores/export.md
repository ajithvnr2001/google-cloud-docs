---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.annotationStores/export/
title: Method: annotationStores.export \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:10.971227+00:00
---

# Method: annotationStores.export  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.annotationStores/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)



Send feedback 

#  Method: annotationStores.export Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.annotationStores.export

Export `[Annotations](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.annotationStores.annotations#Annotation)` from the `[Annotation store](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.annotationStores#AnnotationStore)`. If the request is successful, a detailed response is returned of type `[ExportAnnotationsResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ExportAnnotationsResponse)`, contained in the [response][google.longrunning.Operation.result.response] field when the operation finishes. The `[metadata](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation.FIELDS.metadata)` field type is `[OperationMetadata](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/OperationMetadata)`. Errors are logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)).

### HTTP request

`POST https://healthcare.googleapis.com/v1beta1/{name=projects/*/locations/*/datasets/*/annotationStores/*}:export`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the Annotation store to export annotations to, in the format of `projects/{projectId}/locations/{locationId}/datasets/{datasetId}/annotationStores/{annotationStoreId}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.annotationStores.export`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      // Union field destination can be only one of the following:
      "gcsDestination": {
        object([GcsDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.annotationStores/export#GcsDestination))
      },
      "bigqueryDestination": {
        object([BigQueryDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/BigQueryDestination))
      }
      // End of list of possible types for union field destination.
    }  
  
Fields  
---  
Union field `destination`. Destination for export. `destination` can be only one of the following:  
`gcsDestination` |  `object(`[GcsDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.annotationStores/export#GcsDestination)`)` The Cloud Storage destination, which requires the `roles/storage.objectAdmin` Cloud IAM role.  
`bigqueryDestination` |  `object(`[BigQueryDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/BigQueryDestination)`)` The BigQuery output destination, which requires two IAM roles: `roles/bigquery.dataEditor` and `roles/bigquery.jobUser`.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## GcsDestination

The Cloud Storage location for export.

JSON representation  
---  
      
    
    {
      "uriPrefix": string
    }  
  
Fields  
---  
`uriPrefix` |  `string` The Cloud Storage destination to export to. URI for a Cloud Storage directory where the server writes result files, in the format `gs://{bucket-id}/{path/to/destination/dir}`. If there is no trailing slash, the service appends one when composing the object path. The user is responsible for creating the Cloud Storage bucket referenced in `uriPrefix`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
