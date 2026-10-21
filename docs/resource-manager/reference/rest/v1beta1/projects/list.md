---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/list/
title: Method: projects.list \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:23.834858+00:00
---

# Method: projects.list  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/list/

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



Lists Projects that the caller has the `resourcemanager.projects.get` permission on and satisfy the specified filter.

This method returns Projects in an unspecified order. This method is eventually consistent with project mutations; this means that a newly created project may not appear in the results or recent updates to an existing project may not be reflected in the results. To retrieve the latest state of a project, use the [projects.get][Projects.GetProject] method.

NOTE: If the request filter contains a `parent.type` and `parent.id` and the caller has the `resourcemanager.projects.list` permission on the parent, the results will be drawn from an alternate index which provides more consistent results. In future versions of this API, this List method will be split into List and Search to properly capture the behavioral difference.

### HTTP request

`GET https://cloudresourcemanager.googleapis.com/v1beta1/projects`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`pageToken` |  `string` A pagination token returned from a previous call to `[projects.list](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/list#google.cloudresourcemanager.projects.v1beta1.DeveloperProjects.ListProjects)` that indicates from where listing should continue.Optional.  
`pageSize` |  `integer` The maximum number of Projects to return in the response. The server can return fewer Projects than requested. If unspecified, server picks an appropriate default.Optional.  
`filter` |  `string` An expression for filtering the results of the request. Filter rules are case insensitive. If multiple fields are included in a filter query, the query will return results that match any of the fields. Some eligible fields for filtering are:

  * `name`
  * `id`
  * `labels.<key>` (where _key_ is the name of a label)
  * `parent.type`
  * `parent.id`

Some examples of using labels as filters: | Filter  | Description   
---|---  
name:how*  | The project's name starts with "how".   
name:Howl  | The project's name is `Howl` or `howl`.   
name:HOWL  | Equivalent to above.   
NAME:howl  | Equivalent to above.   
labels.color:*  | The project has the label `color`.   
labels.color:red  | The project's label `color` has the value `red`.   
labels.color:red labels.size:big  | The project's label `color` has the  
value `red` or its label `size` has the value `big`.   
  
If no filter is specified, the call will return projects for which the user has the `resourcemanager.projects.get` permission.

NOTE: To perform a by-parent query (eg., what projects are directly in a Folder), the caller must have the `resourcemanager.projects.list` permission on the parent and the filter must contain both a `parent.type` and a `parent.id` restriction (example: "parent.type:folder parent.id:123"). In this case an alternate search index is used which provides more consistent results.

Optional.  
  
### Request body

The request body must be empty.

### Response body

A page of the response received from the `[projects.list](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/list#google.cloudresourcemanager.projects.v1beta1.DeveloperProjects.ListProjects)` method.

A paginated response where more pages are available has `nextPageToken` set. This token can be used in a subsequent request to retrieve the next request page.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "projects": [
        {
          object ([Project](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects#Project))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`projects[]` |  `object (`[Project](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects#Project)`)` The list of Projects that matched the list filter. This list can be paginated.  
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
