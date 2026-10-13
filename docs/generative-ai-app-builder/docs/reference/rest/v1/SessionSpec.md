---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SessionSpec/
title: SessionSpec \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:29.227637+00:00
---

# SessionSpec  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SessionSpec/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  SessionSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Session specification.

JSON representation  
---  
      
    
    {
      "queryId": string,
      "searchResultPersistenceCount": integer
    }  
  
Fields  
---  
`queryId` |  `string` If set, the search result gets stored to the "turn" specified by this query ID.Example: Let's say the session looks like this: session { name: ".../sessions/xxx" turns { query { text: "What is foo?" queryId: ".../questions/yyy" } answer: "Foo is ..." } turns { query { text: "How about bar then?" queryId: ".../questions/zzz" } } }The user can call /search API with a request like this:session: ".../sessions/xxx" sessionSpec { queryId: ".../questions/zzz" }Then, the API stores the search result, associated with the last turn. The stored search result can be used by a subsequent /answer API call (with the session ID and the query ID specified). Also, it is possible to call /search and /answer in parallel with the same session ID & query ID.  
`searchResultPersistenceCount` |  `integer` The number of top search results to persist. The persisted search results can be used for the subsequent /answer api call.This field is similar to the `summaryResultCount` field in `[SearchRequest.ContentSearchSpec.SummarySpec.summary_result_count](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/ContentSearchSpec#SummarySpec.FIELDS.summary_result_count)`.At most 10 results for documents mode, or 50 for chunks mode.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-20 UTC."],[],[]] 
