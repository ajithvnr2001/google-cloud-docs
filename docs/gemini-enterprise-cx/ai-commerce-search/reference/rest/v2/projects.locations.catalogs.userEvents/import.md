---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import/
title: Method: projects.locations.catalogs.userEvents.import \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:18.316972+00:00
---

# Method: projects.locations.catalogs.userEvents.import  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.userEvents.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * UserEventInputConfig
    * JSON representation
  * UserEventInlineSource
    * JSON representation
  * Try it!



Bulk import of User events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events.

`Operation.response` is of type `ImportResponse`. Note that it is possible for a subset of the items to be successfully inserted. `Operation.metadata` is of type `ImportMetadata`.

### HTTP request

`POST https://retail.googleapis.com/v2/{parent=projects/*/locations/*/catalogs/*}/userEvents:import`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. `projects/1234/locations/global/catalogs/default_catalog`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "inputConfig": {
        object ([UserEventInputConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import#UserEventInputConfig))
      },
      "errorsConfig": {
        object ([ImportErrorsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ImportErrorsConfig))
      }
    }  
  
Fields  
---  
`inputConfig` |  `object (`[UserEventInputConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import#UserEventInputConfig)`)` Required. The desired input location of the data.  
`errorsConfig` |  `object (`[ImportErrorsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ImportErrorsConfig)`)` The desired location of errors incurred during the Import. Cannot be set for inline user event imports.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `retail.userEvents.import`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## UserEventInputConfig

The input config source for user events.

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "userEventInlineSource": {
        object ([UserEventInlineSource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import#UserEventInlineSource))
      },
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/GcsSource))
      },
      "bigQuerySource": {
        object ([BigQuerySource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BigQuerySource))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. The source of the input. `source` can be only one of the following:  
`userEventInlineSource` |  `object (`[UserEventInlineSource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import#UserEventInlineSource)`)` Required. The Inline source for the input content for UserEvents.  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/GcsSource)`)` Required. Google Cloud Storage location for the input content.  
`bigQuerySource` |  `object (`[BigQuerySource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BigQuerySource)`)` Required. BigQuery input source.  
  
## UserEventInlineSource

The inline source for the input config for userEvents.import method.

JSON representation  
---  
      
    
    {
      "userEvents": [
        {
          object ([UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent))
        }
      ]
    }  
  
Fields  
---  
`userEvents[]` |  `object (`[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent)`)` Required. A list of user events to import. Recommended max of 10k items.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
