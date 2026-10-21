---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/GoogleSearchSuggestions/
title: GoogleSearchSuggestions \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:39.932882+00:00
---

# GoogleSearchSuggestions  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/GoogleSearchSuggestions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  GoogleSearchSuggestions Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * WebSearchQuery
    * JSON representation



Search suggestions from `[Google Search Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.tools#Tool.GoogleSearchTool)`.

JSON representation  
---  
      
    
    {
      "htmls": [
        string
      ],
      "webSearchQueries": [
        {
          object ([WebSearchQuery](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/GoogleSearchSuggestions#WebSearchQuery))
        }
      ]
    }  
  
Fields  
---  
`htmls[]` |  `string` Compliant HTML and CSS styling for search suggestions. The provided HTML and CSS automatically adapts to your device settings, displaying in either light or dark mode indicated by `@media(prefers-color-scheme)`.  
`webSearchQueries[]` |  `object (`[WebSearchQuery](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/GoogleSearchSuggestions#WebSearchQuery)`)` List of queries used to perform the google search along with the search result URIs forming the search suggestions.  
  
## WebSearchQuery

Represents a single web search query and its associated search uri.

JSON representation  
---  
      
    
    {
      "query": string,
      "uri": string
    }  
  
Fields  
---  
`query` |  `string` The search query text.  
`uri` |  `string` The URI to the Google Search results page for the query.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
