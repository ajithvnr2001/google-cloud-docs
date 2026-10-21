---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list/
title: Method: projects.list \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:30.409702+00:00
---

# Method: projects.list  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: projects.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists projects that are direct children of the specified folder or organization resource. `list()` provides a strongly consistent view of the projects underneath the specified parent resource. `list()` returns projects sorted based upon the (ascending) lexical ordering of their `displayName`. The caller must have `resourcemanager.projects.list` permission on the identified parent.

### HTTP request

`GET https://cloudresourcemanager.googleapis.com/v3/projects`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`parent` |  `string` Required. The name of the parent resource whose projects are being listed. Only children of this parent resource are listed; descendants are not listed.If the parent is a folder, use the value `folders/{folder_id}`. If the parent is an organization, use the value `organizations/{org_id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `resourcemanager.projects.list`

  
`pageToken` |  `string` Optional. A pagination token returned from a previous call to `[projects.list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list#google.cloud.resourcemanager.v3.Projects.ListProjects)` that indicates from where listing should continue.  
`pageSize` |  `integer` Optional. The maximum number of projects to return in the response. The server can return fewer projects than requested. If unspecified, server picks an appropriate default.  
`showDeleted` |  `boolean` Optional. Indicate that projects in the `DELETE_REQUESTED` state should also be returned. Normally only `ACTIVE` projects are returned.  
  
### Request body

The request body must be empty.

### Response body

A page of the response received from the `[projects.list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list#google.cloud.resourcemanager.v3.Projects.ListProjects)` method.

A paginated response where more pages are available has `nextPageToken` set. This token can be used in a subsequent request to retrieve the next request page.

NOTE: A response may contain fewer elements than the request `pageSize` and still have a `nextPageToken`.

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
`projects[]` |  `object (`[Project](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects#Project)`)` The list of Projects under the parent. This list can be paginated.  
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
