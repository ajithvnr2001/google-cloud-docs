---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/search/
title: Method: projects.search \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:07:00.994718+00:00
---

# Method: projects.search  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: projects.search Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Search for projects that the caller has the `resourcemanager.projects.get` permission on, and also satisfy the specified query.

This method returns projects in an unspecified order.

This method is eventually consistent with project mutations; this means that a newly created project may not appear in the results or recent updates to an existing project may not be reflected in the results. To retrieve the latest state of a project, use the `[projects.get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/get#google.cloud.resourcemanager.v3.Projects.GetProject)` method.

### HTTP request

`GET https://cloudresourcemanager.googleapis.com/v3/projects:search`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`query` |  `string` Optional. A query string for searching for projects that the caller has `resourcemanager.projects.get` permission to. If multiple fields are included in the query, then it will return results that match any of the fields. Some eligible fields are:
    
    
    | Field                   | Description                                  |
    |-------------------------|----------------------------------------------|
    | displayName, name       | Filters by displayName.                      |
    | parent                  | Project's parent (for example: folders/123, organizations/*). Prefer parent field over parent.type and parent.id.|
    | parent.type             | Parent's type: `folder` or `organization`.   |
    | parent.id               | Parent's id number (for example: 123)        |
    | id, projectId           | Filters by projectId.                        |
    | state, lifecycleState   | Filters by state.                            |
    | labels                  | Filters by label name or value.              |
    | labels.\<key\> (where *key* is the name of a label) | Filters by label name.|
    

Search expressions are case insensitive.Some examples queries:
    
    
    | Query            | Description                                         |
    |------------------|-----------------------------------------------------|
    | name:how*        | The project's name starts with "how".               |
    | name:Howl        | The project's name is `Howl` or `howl`.             |
    | name:HOWL        | Equivalent to above.                                |
    | NAME:howl        | Equivalent to above.                                |
    | labels.color:*   | The project has the label `color`.                  |
    | labels.color:red | The project's label `color` has the value `red`.    |
    | labels.color:red labels.size:big | The project's label `color` has the
    value `red` or its label `size` has the value `big`.                     |
    

If no query is specified, the call will return projects for which the user has the `resourcemanager.projects.get` permission.  
`pageToken` |  `string` Optional. A pagination token returned from a previous call to `[projects.list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list#google.cloud.resourcemanager.v3.Projects.ListProjects)` that indicates from where listing should continue.  
`pageSize` |  `integer` Optional. The maximum number of projects to return in the response. The server can return fewer projects than requested. If unspecified, server picks an appropriate default.  
  
### Request body

The request body must be empty.

### Response body

A page of the response received from the `[projects.search](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/search#google.cloud.resourcemanager.v3.Projects.SearchProjects)` method.

A paginated response where more pages are available has `nextPageToken` set. This token can be used in a subsequent request to retrieve the next request page.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "projects": [
        {
          object ([Project](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects#Project))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`projects[]` |  `object (`[Project](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects#Project)`)` The list of Projects that matched the list filter query. This list can be paginated.  
`nextPageToken` |  `string` Pagination token.If the result set is too large to fit in a single response, this token is returned. It encodes the position of the current result cursor. Feeding this value into a new list request with the `pageToken` parameter gives the next page of the results.When `nextPageToken` is not filled in, there is no next page and the list returned is the last page in the result set.Pagination tokens have a limited lifetime.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/cloudplatformprojects`
  * `https://www.googleapis.com/auth/cloudplatformprojects.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
