---
url: https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots/list/
title: Method: projects.locations.instances.snapshots.list \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:47.808311+00:00
---

# Method: projects.locations.instances.snapshots.list  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Reference ](https://docs.cloud.google.com/filestore/docs/apis)



Send feedback 

#  Method: projects.locations.instances.snapshots.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all snapshots in a project for either a specified location or for all locations.

### HTTP request

`GET https://file.googleapis.com/v1/{parent=projects/*/locations/*/instances/*}/snapshots`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance for which to retrieve snapshot information, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of items to return.  
`pageToken` |  `string` The nextPageToken value to use if there are additional results to retrieve for this list request.  
`orderBy` |  `string` Sort results. Supported values are "name", "name desc" or "" (unsorted).  
`filter` |  `string` List filter.  
`returnPartialSuccess` |  `boolean` Optional. If true, allow partial responses for multi-regional Aggregated List requests.  
  
### Request body

The request body must be empty.

### Response body

ListSnapshotsResponse is the result of ListSnapshotsRequest.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "snapshots": [
        {
          object ([Snapshot](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots#Snapshot))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`snapshots[]` |  `object (`[Snapshot](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots#Snapshot)`)` A list of snapshots in the project for the specified instance.  
`nextPageToken` |  `string` The token you can use to retrieve the next page of results. Not returned if there are no more results in the list.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-11 UTC."],[],[]] 
