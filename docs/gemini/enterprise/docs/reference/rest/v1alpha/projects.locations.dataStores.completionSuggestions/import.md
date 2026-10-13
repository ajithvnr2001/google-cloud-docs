---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.completionSuggestions/import/
title: Method: projects.locations.dataStores.completionSuggestions.import \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:29.733431+00:00
---

# Method: projects.locations.dataStores.completionSuggestions.import  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.completionSuggestions/import/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.dataStores.completionSuggestions.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Imports `[CompletionSuggestion](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/InlineSource#CompletionSuggestion)`s for a DataStore.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{parent=projects/*/locations/*/dataStores/*}/completionSuggestions:import`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent data store resource name for which to import customer autocomplete suggestions.Follows pattern `projects/*/locations/*/collections/*/dataStores/*`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "errorConfig": {
        object ([ImportErrorConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/ImportErrorConfig))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "inlineSource": {
        object ([InlineSource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/InlineSource))
      },
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/GcsSource))
      },
      "bigquerySource": {
        object ([BigQuerySource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigQuerySource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`errorConfig` |  `object (`[ImportErrorConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/ImportErrorConfig)`)` The desired location of errors incurred during the Import.  
The source of the autocomplete suggestions. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`inlineSource` |  `object (`[InlineSource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/InlineSource)`)` The Inline source for suggestion entries.  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/GcsSource)`)` Cloud Storage location for the input content.  
`bigquerySource` |  `object (`[BigQuerySource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigQuerySource)`)` BigQuery input source.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.assist.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `discoveryengine.completionSuggestions.import`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
