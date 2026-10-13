---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.rbacrolebindings/list/
title: Method: projects.locations.memberships.rbacrolebindings.list \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:08.402434+00:00
---

# Method: projects.locations.memberships.rbacrolebindings.list  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.rbacrolebindings/list/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Method: projects.locations.memberships.rbacrolebindings.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists all Membership RBACRoleBindings.

### HTTP request

`GET https://gkehub.googleapis.com/v1alpha/{parent=projects/*/locations/*/memberships/*}/rbacrolebindings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent (project and location) where the Features will be listed. Specified in the format `projects/*/locations/*/memberships/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `gkehub.rbacrolebindings.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. When requesting a 'page' of resources, `pageSize` specifies number of resources to return. If unspecified or set to 0, all resources will be returned.  
`pageToken` |  `string` Optional. Token returned by previous call to `rbacrolebindings.list` which specifies the position in the list from where to continue listing the resources.  
  
### Request body

The request body must be empty.

### Response body

List of Membership RBACRoleBindings.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "rbacrolebindings": [
        {
          object ([RBACRoleBinding](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.rbacrolebindings#RBACRoleBinding))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`rbacrolebindings[]` |  `object (`[RBACRoleBinding](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.rbacrolebindings#RBACRoleBinding)`)` The list of Membership RBACRoleBindings.  
`nextPageToken` |  `string` A token to request the next page of resources from the `rbacrolebindings.list` method. The value of an empty string means that there are no more resources to return.  
`unreachable[]` |  `string` List of locations that could not be reached while fetching this list.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-12 UTC."],[],[]] 
