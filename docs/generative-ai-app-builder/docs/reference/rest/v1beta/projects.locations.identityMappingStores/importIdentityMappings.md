---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.identityMappingStores/importIdentityMappings/
title: Method: projects.locations.identityMappingStores.importIdentityMappings \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:11:29.116218+00:00
---

# Method: projects.locations.identityMappingStores.importIdentityMappings  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.identityMappingStores/importIdentityMappings/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.identityMappingStores.importIdentityMappings Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * InlineSource
    * JSON representation



Imports a list of Identity Mapping Entries to an Identity Mapping Store.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1beta/{identityMappingStore=projects/*/locations/*/identityMappingStores/*}:importIdentityMappings`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`identityMappingStore` |  `string` Required. The name of the Identity Mapping Store to import Identity Mapping Entries to. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "inlineSource": {
        object ([InlineSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.identityMappingStores/importIdentityMappings#InlineSource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The source of the input. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`inlineSource` |  `object (`[InlineSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.identityMappingStores/importIdentityMappings#InlineSource)`)` The inline source to import identity mapping entries from.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `identityMappingStore` resource:

  * `discoveryengine.identityMappingStores.importIdentityMappings`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## InlineSource

The inline source to import identity mapping entries from.

JSON representation  
---  
      
    
    {
      "identityMappingEntries": [
        {
          object ([IdentityMappingEntry](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/IdentityMappingEntry))
        }
      ]
    }  
  
Fields  
---  
`identityMappingEntries[]` |  `object (`[IdentityMappingEntry](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/IdentityMappingEntry)`)` A maximum of 10000 entries can be imported at one time  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
