---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/CompletionConfig/
title: CompletionConfig \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:22.452166+00:00
---

# CompletionConfig  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/CompletionConfig/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  CompletionConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EnableMode



Config to customize Autocomplete API response for both engines and data stores. Some fields are applicable to only one of them.

JSON representation  
---  
      
    
    {
      "name": string,
      "matchingOrder": string,
      "maxSuggestions": integer,
      "minPrefixLength": integer,
      "queryModel": string,
      "queryFrequencyThreshold": integer,
      "numUniqueUsersThreshold": integer,
      "shouldServeContentSuggestions": boolean,
      "filterPiiSuggestionsUsingDlp": boolean,
      "enableMode": enum ([EnableMode](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/CompletionConfig#EnableMode))
    }  
  
Fields  
---  
`name` |  `string` Required. Immutable. Fully qualified name `projects/*/locations/*/dataStores/*/completionConfig` `projects/*/locations/*/collections/*/dataStores/*/completionConfig` `projects/*/locations/*/collections/*/engines/*/completionConfig`  
`matchingOrder` |  `string` The matching order for autocomplete suggestions, e.g., a query consisting of `sh` with `out-of-order` specified would suggest `women's shoes`, whereas a query of `red s` with `exact-prefix` specified would suggest `red shoes`. Currently supported values:

  * `out-of-order`
  * `exact-prefix`

Default value: `exact-prefix`.  
`maxSuggestions` |  `integer` The maximum number of autocomplete suggestions returned per term.maxSuggestions must lie within the range of [1, 20]. If not set or set to 0, it will be set to the default of 20 suggestions.  
`minPrefixLength` |  `integer` The minimum number of characters needed to be typed in order to get suggestions.minPrefixLength must lie within the range of [1, 20]. If not set or set to 0, it will be set to the default of 1 character.  
`queryModel` |  `string` The data model of query suggestions for serving.Currently supported values:

  * `automatic` \- autocomplete backend automatic selects or mixes suggestions from different models.
  * `document` \- Using suggestions generated from user-imported documents.
  * `search-history` \- Using suggestions generated from the past history of `[SearchService.Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.servingConfigs/search#google.cloud.discoveryengine.v1alpha.SearchService.Search)` API calls. Do not use it when there is no traffic for Search API.
  * `user-event` \- Using suggestions generated from user-imported search events.
  * `document-completable` \- Using suggestions taken directly from user-imported document fields marked as completable.

If query model is empty, the serving applies the "automatic" model by default.  
`queryFrequencyThreshold` |  `integer` This field is only meaningful for suggestions generated from user events or search history. If a query shows up less than this threshold, it may indicate that the query is rarely searched and thus will not be generated as a suggestion. This is field can be helpful for preventing PII queries becoming suggestions, as those queries are usually uniquely searched. If not set, the default value is 8 used in the generation pipeline.  
`numUniqueUsersThreshold` |  `integer` This field is only meaningful for suggestions generated from user events or search history, which may have user ids attached. If the number of unique users that have searched a query is less than this threshold, the query will not be generated as a suggestion. This is field can be helpful for preventing PII queries becoming suggestions, as those queries are usually uniquely searched. If not set, the default value is 3 used in the generation pipeline.  
`shouldServeContentSuggestions` |  `boolean` Whether to generate and serve content suggestions. This allows for content suggestions to be served in addition to query suggestions.  
`filterPiiSuggestionsUsingDlp  
**(deprecated)**` |  `boolean` This item is deprecated!Deprecated: this field has no effect. As of May 2025, PII suggestion filtering using [DLP](https://cloud.google.com/security/products/dlp) is always on for all data stores and can't be configured per data store.  
`enableMode` |  `enum (`[EnableMode](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/CompletionConfig#EnableMode)`)` The enable mode of autocomplete generation pipelines. If this field is unset, the server behavior defaults to `[CompletionConfig.EnableMode.AUTOMATIC](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/CompletionConfig#EnableMode.ENUM_VALUES.AUTOMATIC)`. Applies to DataStore only. Ignored for Engine.  
  
## EnableMode

Specifies the enable mode of autocomplete generation pipelines.

Enums  
---  
`ENABLE_MODE_UNSPECIFIED` | When AutoComplete enable mode unspecified, it defaults to AUTOMATIC mode.  
`AUTOMATIC` | AutoComplete will be enabled when the data store meets criteria.  
`MANUAL` | AutoComplete will be enabled regardless of UCS data requirements.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-14 UTC."],[],[]] 
