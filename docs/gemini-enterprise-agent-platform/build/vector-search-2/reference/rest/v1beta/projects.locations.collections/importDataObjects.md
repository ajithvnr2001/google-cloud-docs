---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections/importDataObjects/
title: Method: projects.locations.collections.importDataObjects \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:19.961455+00:00
---

# Method: projects.locations.collections.importDataObjects  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections/importDataObjects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.collections.importDataObjects Stay organized with collections  Save and categorize content based on your preferences. 

Initiates a Long-Running Operation to import DataObjects into a Collection.

### HTTP request

`POST https://vectorsearch.googleapis.com/v1beta/{name}:importDataObjects`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the Collection to import DataObjects into. Format: `projects/{project}/locations/{location}/collections/{collection}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      // Union field config can be only one of the following:
      "gcsImport": {
        object ([GcsImportConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections/importDataObjects#GcsImportConfig))
      }
      // End of list of possible types for union field config.
    }  
  
Fields  
---  
Union field `config`. The configuration for the import data and error results. `config` can be only one of the following:  
`gcsImport` |  `object (`[GcsImportConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections/importDataObjects#GcsImportConfig)`)` The Cloud Storage location of the input content.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `vectorsearch.dataObjects.import`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## GcsImportConfig

Google Cloud Storage configuration for the import.

JSON representation  
---  
      
    
    {
      "contentsUri": string,
      "errorUri": string,
      "outputUri": string
    }  
  
Fields  
---  
`contentsUri` |  `string` Required. URI prefix of the Cloud Storage DataObjects to import.  
`errorUri` |  `string` Required. URI prefix of the Cloud Storage location to write any errors encountered during the import.  
`outputUri` |  `string` Optional. URI prefix of the Cloud Storage location to write DataObject `IDs` and `etags` of DataObjects that were successfully imported. The service will write the successfully imported DataObjects to sharded files under this prefix. If this field is empty, no output will be written.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
