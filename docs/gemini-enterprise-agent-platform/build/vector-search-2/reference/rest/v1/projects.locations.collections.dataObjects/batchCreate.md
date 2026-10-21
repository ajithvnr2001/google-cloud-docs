---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchCreate/
title: Method: projects.locations.collections.dataObjects.batchCreate \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:23:18.983634+00:00
---

# Method: projects.locations.collections.dataObjects.batchCreate  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchCreate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.collections.dataObjects.batchCreate Stay organized with collections  Save and categorize content based on your preferences. 

Creates a batch of dataObjects.

### HTTP request

`POST https://vectorsearch.googleapis.com/v1/{parent}/dataObjects:batchCreate`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the Collection to create the DataObjects in. Format: `projects/{project}/locations/{location}/collections/{collection}`. The parent field in the CreateDataObjectRequest messages must match this field.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object ([CreateDataObjectRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchCreate#CreateDataObjectRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object (`[CreateDataObjectRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchCreate#CreateDataObjectRequest)`)` Required. The request message specifying the resources to create. A maximum of 1000 DataObjects can be created in a batch.  
  
### Response body

Response message for `[DataObjectService.BatchCreateDataObjects](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchCreate#google.cloud.vectorsearch.v1.DataObjectService.BatchCreateDataObjects)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dataObjects": [
        {
          object ([DataObject](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects#DataObject))
        }
      ]
    }  
  
Fields  
---  
`dataObjects[]` |  `object (`[DataObject](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects#DataObject)`)` Output only. DataObjects created.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `vectorsearch.dataObjects.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## CreateDataObjectRequest

Request message for `[DataObjectService.CreateDataObject](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/create#google.cloud.vectorsearch.v1.DataObjectService.CreateDataObject)`.

JSON representation  
---  
      
    
    {
      "parent": string,
      "dataObjectId": string,
      "dataObject": {
        object ([DataObject](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects#DataObject))
      }
    }  
  
Fields  
---  
`parent` |  `string` Required. The resource name of the Collection to create the DataObject in. Format: `projects/{project}/locations/{location}/collections/{collection}`  
`dataObjectId` |  `string` Required. The id of the dataObject to create. The id must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, it must be 1-63 characters long and match the regular expression `[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?`.  
`dataObject` |  `object (`[DataObject](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects#DataObject)`)` Required. The DataObject to create.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
