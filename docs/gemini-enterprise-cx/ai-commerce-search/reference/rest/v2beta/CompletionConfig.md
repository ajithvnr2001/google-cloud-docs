---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/CompletionConfig/
title: CompletionConfig \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:26:26.705598+00:00
---

# CompletionConfig  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/CompletionConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  CompletionConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Catalog level autocomplete config for customers to customize autocomplete feature's settings.

JSON representation  
---  
      
    
    {
      "name": string,
      "matchingOrder": string,
      "maxSuggestions": integer,
      "minPrefixLength": integer,
      "autoLearning": boolean,
      "suggestionsInputConfig": {
        object ([CompletionDataInputConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/CompletionDataInputConfig))
      },
      "lastSuggestionsImportOperation": string,
      "denylistInputConfig": {
        object ([CompletionDataInputConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/CompletionDataInputConfig))
      },
      "lastDenylistImportOperation": string,
      "allowlistInputConfig": {
        object ([CompletionDataInputConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/CompletionDataInputConfig))
      },
      "lastAllowlistImportOperation": string
    }  
  
Fields  
---  
`name` |  `string` Required. Immutable. Fully qualified name `projects/*/locations/*/catalogs/*/completionConfig`  
`matchingOrder` |  `string` Specifies the matching order for autocomplete suggestions, e.g., a query consisting of 'sh' with 'out-of-order' specified would suggest "women's shoes", whereas a query of 'red s' with 'exact-prefix' specified would suggest "red shoes". Currently supported values:

  * 'out-of-order'
  * 'exact-prefix'

Default value: 'exact-prefix'.  
`maxSuggestions` |  `integer` The maximum number of autocomplete suggestions returned per term. Default value is 20. If left unset or set to 0, then will fallback to default value.Value range is 1 to 20.  
`minPrefixLength` |  `integer` The minimum number of characters needed to be typed in order to get suggestions. Default value is 2. If left unset or set to 0, then will fallback to default value.Value range is 1 to 20.  
`autoLearning` |  `boolean` If set to true, the auto learning function is enabled. Auto learning uses user data to generate suggestions using ML techniques. Default value is false. Only after enabling auto learning can users use `cloud-retail` data in `CompleteQueryRequest`.  
`suggestionsInputConfig` |  `object (`[CompletionDataInputConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/CompletionDataInputConfig)`)` Output only. The source data for the latest import of the autocomplete suggestion phrases.  
`lastSuggestionsImportOperation` |  `string` Output only. Name of the LRO corresponding to the latest suggestion terms list import.Can use `[operations.get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.operations/get#google.longrunning.Operations.GetOperation)` API method to retrieve the latest state of the Long Running Operation.  
`denylistInputConfig` |  `object (`[CompletionDataInputConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/CompletionDataInputConfig)`)` Output only. The source data for the latest import of the autocomplete denylist phrases.  
`lastDenylistImportOperation` |  `string` Output only. Name of the LRO corresponding to the latest denylist import.Can use `[operations.get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.operations/get#google.longrunning.Operations.GetOperation)` API to retrieve the latest state of the Long Running Operation.  
`allowlistInputConfig` |  `object (`[CompletionDataInputConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/CompletionDataInputConfig)`)` Output only. The source data for the latest import of the autocomplete allowlist phrases.  
`lastAllowlistImportOperation` |  `string` Output only. Name of the LRO corresponding to the latest allowlist import.Can use `[operations.get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.operations/get#google.longrunning.Operations.GetOperation)` API to retrieve the latest state of the Long Running Operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
