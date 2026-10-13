---
url: https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.namespaces/list/
title: Method: projects.locations.instances.namespaces.list \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:17:10.689997+00:00
---

# Method: projects.locations.instances.namespaces.list  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.namespaces/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Reference ](https://docs.cloud.google.com/data-fusion/docs/reference)



Send feedback 

#  Method: projects.locations.instances.namespaces.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * NamespaceView
  * Namespace
    * JSON representation
  * IAMPolicy
    * JSON representation
  * Try it!



List namespaces in a given instance

### HTTP request

`GET https://datafusion.googleapis.com/v1beta1/{parent=projects/*/locations/*/instances/*}/namespaces`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance to list its namespaces.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of items to return.  
`pageToken` |  `string` The nextPageToken value to use if there are additional results to retrieve for this list request.  
`view` |  `enum (`[NamespaceView](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.namespaces/list#NamespaceView)`)` By default, only basic information about a namespace is returned (e.g. name). When `NAMESPACE_VIEW_FULL` is specified, additional information associated with a namespace gets returned (e.g. IAM policy set on the namespace)  
  
### Request body

The request body must be empty.

### Response body

List namespaces response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "namespaces": [
        {
          object ([Namespace](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.namespaces/list#Namespace))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`namespaces[]` |  `object (`[Namespace](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.namespaces/list#Namespace)`)` List of namespaces  
`nextPageToken` |  `string` Token to retrieve the next page of results or empty if there are no more results in the list.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## NamespaceView

A view for Namespace

Enums  
---  
`NAMESPACE_VIEW_UNSPECIFIED` | Default/unset value, which will use BASIC view.  
`NAMESPACE_VIEW_BASIC` | Show the most basic metadata of a namespace  
`NAMESPACE_VIEW_FULL` | Returns all metadata of a namespace  
  
## Namespace

Represents the information of a namespace

JSON representation  
---  
      
    
    {
      "name": string,
      "iamPolicy": {
        object ([IAMPolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.namespaces/list#IAMPolicy))
      }
    }  
  
Fields  
---  
`name` |  `string` Name of the given namespace.  
`iamPolicy` |  `object (`[IAMPolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.namespaces/list#IAMPolicy)`)` IAM policy associated with this namespace.  
  
## IAMPolicy

IAMPolicy encapsulates the IAM policy name, definition and status of policy fetching.

JSON representation  
---  
      
    
    {
      "policy": {
        object ([Policy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/Shared.Types/Policy))
      },
      "status": {
        object ([Status](https://docs.cloud.google.com/data-fusion/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      }
    }  
  
Fields  
---  
`policy` |  `object (`[Policy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/Shared.Types/Policy)`)` Policy definition if IAM policy fetching is successful, otherwise empty.  
`status` |  `object (`[Status](https://docs.cloud.google.com/data-fusion/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Status of iam policy fetching.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-20 UTC."],[],[]] 
