---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.identityMappingStores/purgeIdentityMappings/
title: Method: projects.locations.identityMappingStores.purgeIdentityMappings \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:12.592560+00:00
---

# Method: projects.locations.identityMappingStores.purgeIdentityMappings  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.identityMappingStores/purgeIdentityMappings/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.identityMappingStores.purgeIdentityMappings Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * InlineSource
    * JSON representation



Purges specified or all Identity Mapping Entries from an Identity Mapping Store.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{identityMappingStore=projects/*/locations/*/identityMappingStores/*}:purgeIdentityMappings`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`identityMappingStore` |  `string` Required. The name of the Identity Mapping Store to purge Identity Mapping Entries from. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "filter": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "inlineSource": {
        object ([InlineSource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.identityMappingStores/purgeIdentityMappings#InlineSource))
      }
      // End of mutually exclusive fields.
      "force": boolean
    }  
  
Fields  
---  
`filter` |  `string` Filter matching identity mappings to purge. The eligible field for filtering is:

  * `updateTime`: in ISO 8601 "zulu" format.
  * `externalId`

Examples:

  * Deleting all identity mappings updated in a time range: `updateTime > "2012-04-23T18:25:43.511Z" AND updateTime < "2012-04-23T18:30:43.511Z"`
  * Deleting all identity mappings for a given externalId: `externalId = "id1"`
  * Deleting all identity mappings inside an identity mapping store: `*`

The filtering fields are assumed to have an implicit AND. Should not be used with source. An error will be thrown, if both are provided.  
The source of the input. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`inlineSource` |  `object (`[InlineSource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.identityMappingStores/purgeIdentityMappings#InlineSource)`)` The inline source to purge identity mapping entries from.  
End of mutually exclusive fields.  
`force` |  `boolean` Actually performs the purge. If `force` is set to false, return the expected purge count without deleting any identity mappings. This field is only supported for purge with filter. For input source this field is ignored and data will be purged regardless of the value of this field.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `identityMappingStore` resource:

  * `discoveryengine.identityMappingStores.purgeIdentityMappings`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## InlineSource

The inline source to purge identity mapping entries from.

JSON representation  
---  
      
    
    {
      "identityMappingEntries": [
        {
          object ([IdentityMappingEntry](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/IdentityMappingEntry))
        }
      ]
    }  
  
Fields  
---  
`identityMappingEntries[]` |  `object (`[IdentityMappingEntry](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/IdentityMappingEntry)`)` A maximum of 10000 entries can be purged at one time  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
