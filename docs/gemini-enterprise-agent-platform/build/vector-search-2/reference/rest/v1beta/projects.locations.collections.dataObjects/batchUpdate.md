---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchUpdate/
title: Method: projects.locations.collections.dataObjects.batchUpdate \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:11:20.827009+00:00
---

# Method: projects.locations.collections.dataObjects.batchUpdate  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchUpdate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.collections.dataObjects.batchUpdate Stay organized with collections  Save and categorize content based on your preferences. 

Updates dataObjects in a batch.

### HTTP request

`POST https://vectorsearch.googleapis.com/v1beta/{parent}/dataObjects:batchUpdate`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the Collection to update the DataObjects in. Format: `projects/{project}/locations/{location}/collections/{collection}`. The parent field in the UpdateDataObjectRequest messages must match this field.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object ([UpdateDataObjectRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchUpdate#UpdateDataObjectRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object (`[UpdateDataObjectRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchUpdate#UpdateDataObjectRequest)`)` Required. The request message specifying the resources to update. A maximum of 1000 DataObjects can be updated in a batch.  
  
### Response body

If successful, the response body is empty.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `vectorsearch.dataObjects.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## UpdateDataObjectRequest

Request message for `[DataObjectService.UpdateDataObject](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/patch#google.cloud.vectorsearch.v1beta.DataObjectService.UpdateDataObject)`.

JSON representation  
---  
      
    
    {
      "dataObject": {
        object ([DataObject](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects#DataObject))
      },
      "updateMask": string
    }  
  
Fields  
---  
`dataObject` |  `object (`[DataObject](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects#DataObject)`)` Required. The DataObject which replaces the resource on the server.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The update mask applies to the resource. See `[google.protobuf.FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)`.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
