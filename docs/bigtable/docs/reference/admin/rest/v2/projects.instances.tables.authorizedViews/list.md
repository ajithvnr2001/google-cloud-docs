---
url: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables.authorizedViews/list/
title: Method: projects.instances.tables.authorizedViews.list \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:40.799645+00:00
---

# Method: projects.instances.tables.authorizedViews.list  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables.authorizedViews/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback 

#  Method: projects.instances.tables.authorizedViews.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists all AuthorizedViews from a specific table.

### HTTP request

`GET https://bigtableadmin.googleapis.com/v2/{parent=projects/*/instances/*/tables/*}/authorizedViews`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The unique name of the table for which AuthorizedViews should be listed. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `bigtable.authorizedViews.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of results per page.A pageSize of zero lets the server choose the number of items to return. A pageSize which is strictly positive will return at most that many items. A negative pageSize will cause an error.Following the first request, subsequent paginated calls are not required to pass a pageSize. If a pageSize is set in subsequent calls, it must match the pageSize given in the first request.  
`pageToken` |  `string` Optional. The value of `nextPageToken` returned by a previous call.  
`view` |  `enum (`[ResponseView](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/ResponseView)`)` Optional. The resource_view to be applied to the returned AuthorizedViews' fields. Default to NAME_ONLY.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[google.bigtable.admin.v2.BigtableTableAdmin.ListAuthorizedViews](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables.authorizedViews/list#google.bigtable.admin.v2.BigtableTableAdmin.ListAuthorizedViews)`

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "authorizedViews": [
        {
          object ([AuthorizedView](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables.authorizedViews#AuthorizedView))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`authorizedViews[]` |  `object (`[AuthorizedView](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables.authorizedViews#AuthorizedView)`)` The AuthorizedViews present in the requested table.  
`nextPageToken` |  `string` Set if not all tables could be returned in a single response. Pass this value to `pageToken` in another request to get the next page of results.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/bigtable.admin`
  * `https://www.googleapis.com/auth/bigtable.admin.table`
  * `https://www.googleapis.com/auth/cloud-bigtable.admin`
  * `https://www.googleapis.com/auth/cloud-bigtable.admin.table`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-06 UTC."],[],[]] 
