---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.completionConfig/completeQuery/
title: Method: projects.locations.dataStores.completionConfig.completeQuery \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:56.581114+00:00
---

# Method: projects.locations.dataStores.completionConfig.completeQuery  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.completionConfig/completeQuery/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.dataStores.completionConfig.completeQuery Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Completes the user input with advanced keyword suggestions.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{completionConfig=projects/*/locations/*/dataStores/*/completionConfig}:completeQuery`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`completionConfig` |  `string` Required. The completionConfig of the parent dataStore or engine resource name for which the completion is performed, such as `projects/*/locations/global/collections/default_collection/dataStores/*/completionConfig` `projects/*/locations/global/collections/default_collection/engines/*/completionConfig`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "query": string,
      "queryModel": string,
      "userPseudoId": string,
      "userInfo": {
        object ([UserInfo](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/UserInfo))
      },
      "includeTailSuggestions": boolean,
      "boostSpec": {
        object ([BoostSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/BoostSpec))
      },
      "suggestionTypes": [
        enum ([SuggestionType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SuggestionType))
      ],
      "suggestionTypeSpecs": [
        {
          object ([SuggestionTypeSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SuggestionTypeSpec))
        }
      ],
      "experimentIds": [
        string
      ]
    }  
  
Fields  
---  
`query` |  `string` Required. The typeahead input used to fetch suggestions. Maximum length is 128 characters.The query can not be empty for most of the suggestion types. If it is empty, an `INVALID_ARGUMENT` error is returned. The exception is when the suggestionTypes contains only the type `RECENT_SEARCH`, the query can be an empty string. The is called "zero prefix" feature, which returns user's recently searched queries given the empty query.  
`queryModel` |  `string` Specifies the autocomplete query model, which only applies to the QUERY SuggestionType. This overrides any model specified in the Configuration > Autocomplete section of the Cloud console. Currently supported values:

  * `document` \- Using suggestions generated from user-imported documents.
  * `search-history` \- Using suggestions generated from the past history of `[SearchService.Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.servingConfigs/search#google.cloud.discoveryengine.v1alpha.SearchService.Search)` API calls. Do not use it when there is no traffic for Search API.
  * `user-event` \- Using suggestions generated from user-imported search events.
  * `document-completable` \- Using suggestions taken directly from user-imported document fields marked as completable.

Default values:

  * `document` is the default model for regular dataStores.
  * `search-history` is the default model for site search dataStores.

  
`userPseudoId` |  `string` Optional. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.This field should NOT have a fixed value such as `unknown_visitor`.This should be the same identifier as `[UserEvent.user_pseudo_id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.userEvents#UserEvent.FIELDS.user_pseudo_id)` and `[SearchRequest.user_pseudo_id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.user_pseudo_id)`.The field must be a UTF-8 encoded string with a length limit of 128  
`userInfo` |  `object (`[UserInfo](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/UserInfo)`)` Optional. Information about the end user.This should be the same identifier information as `[UserEvent.user_info](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.userEvents#UserEvent.FIELDS.user_info)` and `[SearchRequest.user_info](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.user_info)`.  
`includeTailSuggestions` |  `boolean` Indicates if tail suggestions should be returned if there are no suggestions that match the full query. Even if set to true, if there are suggestions that match the full query, those are returned and no tail suggestions are returned.  
`boostSpec` |  `object (`[BoostSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/BoostSpec)`)` Optional. Specification to boost suggestions matching the condition.  
`suggestionTypes[]` |  `enum (`[SuggestionType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SuggestionType)`)` Optional. Suggestion types to return. If empty or unspecified, query suggestions are returned. Only one suggestion type is supported at the moment.  
`suggestionTypeSpecs[]` |  `object (`[SuggestionTypeSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SuggestionTypeSpec)`)` Optional. Specification of each suggestion type.  
`experimentIds[]` |  `string` Optional. experiment ids for this request.  
  
### Response body

If successful, the response body contains an instance of `[AdvancedCompleteQueryResponse](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/AdvancedCompleteQueryResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud_search.query`
  * `https://www.googleapis.com/auth/discoveryengine.assist.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.complete_query`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `completionConfig` resource:

  * `discoveryengine.completionConfigs.completeQuery`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
