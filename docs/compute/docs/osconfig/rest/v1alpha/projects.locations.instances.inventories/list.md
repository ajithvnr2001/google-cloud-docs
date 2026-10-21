---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories/list/
title: Method: projects.locations.instances.inventories.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:24.495529+00:00
---

# Method: projects.locations.instances.inventories.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: projects.locations.instances.inventories.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



List inventory data for all VM instances in the specified zone.

### HTTP request

`GET https://osconfig.googleapis.com/v1alpha/{parent=projects/*/locations/*/instances/*}/inventories`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name.Format: `projects/{project}/locations/{location}/instances/-`For `{project}`, either `project-number` or `project-id` can be provided.  
  
### Query parameters

Parameters  
---  
`view` |  `enum (`[InventoryView](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/InventoryView)`)` Inventory view indicating what information should be included in the inventory resource. If unspecified, the default view is BASIC.  
`pageSize` |  `integer` The maximum number of results to return.  
`pageToken` |  `string` A pagination token returned from a previous call to `inventories.list` that indicates where this listing should continue from.  
`filter` |  `string` If provided, this field specifies the criteria that must be met by a `Inventory` API resource to be included in the response.  
  
### Request body

The request body must be empty.

### Response body

A response message for listing inventory data for all VMs in a specified location.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "inventories": [
        {
          object ([Inventory](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#Inventory))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`inventories[]` |  `object (`[Inventory](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories#Inventory)`)` List of inventory objects.  
`nextPageToken` |  `string` The pagination token to retrieve the next page of inventory objects.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `osconfig.inventories.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
