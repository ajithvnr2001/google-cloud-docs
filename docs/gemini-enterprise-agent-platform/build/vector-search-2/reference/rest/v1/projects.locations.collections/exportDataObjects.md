---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections/exportDataObjects/
title: Method: projects.locations.collections.exportDataObjects \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:41:44.626606+00:00
---

# Method: projects.locations.collections.exportDataObjects  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections/exportDataObjects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.collections.exportDataObjects Stay organized with collections  Save and categorize content based on your preferences. 

Initiates a Long-Running Operation to export DataObjects from a Collection.

### HTTP request

`POST https://vectorsearch.googleapis.com/v1/{name}:exportDataObjects`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the Collection from which we want to export Data Objects. Format: `projects/{project}/locations/{location}/collections/{collection}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      // Union field destination can be only one of the following:
      "gcsDestination": {
        object ([GcsExportDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections/exportDataObjects#GcsExportDestination))
      }
      // End of list of possible types for union field destination.
    }  
  
Fields  
---  
Union field `destination`. The configuration for the export data. `destination` can be only one of the following:  
`gcsDestination` |  `object (`[GcsExportDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections/exportDataObjects#GcsExportDestination)`)` The Cloud Storage location where user wants to export Data Objects.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `vectorsearch.dataObjects.export`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## GcsExportDestination

Google Cloud Storage configuration for the export.

JSON representation  
---  
      
    
    {
      "exportUri": string,
      "format": enum ([Format](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections/exportDataObjects#Format))
    }  
  
Fields  
---  
`exportUri` |  `string` Required. URI prefix of the Cloud Storage where to export Data Objects. The bucket is required to be in the same region as the collection.  
`format` |  `enum (`[Format](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections/exportDataObjects#Format)`)` Required. The format of the exported Data Objects.  
  
## Format

Options for the format of the exported Data Objects.

Enums  
---  
`FORMAT_UNSPECIFIED` | Unspecified format.  
`JSONL` | Exports Data Objects in `JSONL` format.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
