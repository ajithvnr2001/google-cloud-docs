---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/list/
title: Method: projects.instances.databases.list \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:06.067242+00:00
---

# Method: projects.instances.databases.list  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists Cloud Spanner databases.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`GET https://spanner.googleapis.com/v1/{parent=projects/*/instances/*}/databases`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance whose databases should be listed. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.databases.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Number of databases to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`pageToken` |  `string` If non-empty, `pageToken` should contain a `[nextPageToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/list#body.ListDatabasesResponse.FIELDS.next_page_token)` from a previous `[ListDatabasesResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/list#body.ListDatabasesResponse)`.  
  
### Request body

The request body must be empty.

### Response body

The response for `[databases.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/list#google.spanner.admin.database.v1.DatabaseAdmin.ListDatabases)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "databases": [
        {
          object ([Database](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#Database))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`databases[]` |  `object (`[Database](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#Database)`)` Databases that matched the request.  
`nextPageToken` |  `string` `nextPageToken` can be sent in a subsequent `[databases.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/list#google.spanner.admin.database.v1.DatabaseAdmin.ListDatabases)` call to fetch more of the matching databases.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
