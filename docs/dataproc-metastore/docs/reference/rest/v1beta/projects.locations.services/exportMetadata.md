---
url: https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1beta/projects.locations.services/exportMetadata/
title: Method: projects.locations.services.exportMetadata \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:41.281710+00:00
---

# Method: projects.locations.services.exportMetadata  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1beta/projects.locations.services/exportMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Reference ](https://docs.cloud.google.com/dataproc-metastore/docs/reference)



Send feedback 

#  Method: projects.locations.services.exportMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Exports metadata from a service.

### HTTP request

`POST https://metastore.googleapis.com/v1beta/{service}:exportMetadata`

### Path parameters

Parameters  
---  
`service` |  `string` Required. The relative resource name of the metastore service to run export, in the following form:`projects/{projectId}/locations/{locationId}/services/{serviceId}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `service`:

  * `metastore.services.export`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requestId": string,
      "databaseDumpType": enum ([Type](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1beta/Type)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "destinationGcsFolder": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`requestId` |  `string` Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format). A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.  
`databaseDumpType` |  `enum (`[Type](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1beta/Type)`)` Optional. The type of the database dump. If unspecified, defaults to `MYSQL`.  
Required. Destination that metadata is exported to. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`destinationGcsFolder` |  `string` A Cloud Storage URI of a folder, in the format `gs://<bucket_name>/<path_inside_bucket>`. A sub-folder `<export_folder>` containing exported files will be created below it.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
