---
url: https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1beta/projects.locations.services.backups/list/
title: Method: projects.locations.services.backups.list \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:19.210083+00:00
---

# Method: projects.locations.services.backups.list  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1beta/projects.locations.services.backups/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Reference ](https://docs.cloud.google.com/dataproc-metastore/docs/reference)



Send feedback 

#  Method: projects.locations.services.backups.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists backups in a service.

### HTTP request

`GET https://metastore.googleapis.com/v1beta/{parent}/backups`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The relative resource name of the service whose backups to list, in the following form:`projects/{projectNumber}/locations/{locationId}/services/{serviceId}/backups`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `metastore.backups.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of backups to return. The response may contain less than the maximum number. If unspecified, no more than 500 backups are returned. The maximum value is 1000; values above 1000 are changed to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `[DataprocMetastore.ListBackups](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1beta/projects.locations.services.backups/list#google.cloud.metastore.v1beta.DataprocMetastore.ListBackups)` call. Provide this token to retrieve the subsequent page.To retrieve the first page, supply an empty page token.When paginating, other parameters provided to `[DataprocMetastore.ListBackups](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1beta/projects.locations.services.backups/list#google.cloud.metastore.v1beta.DataprocMetastore.ListBackups)` must match the call that provided the page token.  
`filter` |  `string` Optional. The filter to apply to list results.  
`orderBy` |  `string` Optional. Specify the ordering of results as described in [Sorting Order](https://cloud.google.com/apis/design/design_patterns#sorting_order). If not specified, the results will be sorted in the default order.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[DataprocMetastore.ListBackups](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1beta/projects.locations.services.backups/list#google.cloud.metastore.v1beta.DataprocMetastore.ListBackups)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "backups": [
        {
          object ([Backup](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1beta/projects.locations.services.backups#Backup))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`backups[]` |  `object (`[Backup](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1beta/projects.locations.services.backups#Backup)`)` The backups of the specified service.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 
