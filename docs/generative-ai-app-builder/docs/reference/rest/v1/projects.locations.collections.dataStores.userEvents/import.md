---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.userEvents/import/
title: Method: projects.locations.collections.dataStores.userEvents.import \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:46.407967+00:00
---

# Method: projects.locations.collections.dataStores.userEvents.import  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.userEvents/import/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataStores.userEvents.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Bulk import of user events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events.

Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully inserted. Operation.metadata is of type ImportMetadata.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:import`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent DataStore resource name, of the form `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "errorConfig": {
        object ([ImportErrorConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/ImportErrorConfig))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "inlineSource": {
        object (InlineSource)
      },
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/GcsSource))
      },
      "bigquerySource": {
        object ([BigQuerySource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/BigQuerySource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`errorConfig` |  `object (`[ImportErrorConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/ImportErrorConfig)`)` The desired location of errors incurred during the Import. Cannot be set for inline user event imports.  
Required - The desired input source of the user event data. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`inlineSource` |  `object (`InlineSource`)` The Inline source for the input content for UserEvents.  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/GcsSource)`)` Cloud Storage location for the input content.  
`bigquerySource` |  `object (`[BigQuerySource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/BigQuerySource)`)` BigQuery input source.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.assist.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `discoveryengine.userEvents.import`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
