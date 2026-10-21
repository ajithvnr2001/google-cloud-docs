---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Fact/
title: Fact \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:31:01.504690+00:00
---

# Fact  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Fact/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Fact Stay organized with collections  Save and categorize content based on your preferences. 

The fact used in grounding.

Fields  
  
`query` `string` Query that is used to retrieve this fact. | `title` `string` If present, it refers to the title of this fact. | `uri` `string` If present, this uri links to the source of the fact. | `summary` `string` If present, the summary/snippet of the fact. | `vectorDistance  
**(deprecated)**` `number` This item is deprecated!If present, the distance between the query vector and this fact vector. | `score` `number` If present, according to the underlying Vector DB and the selected metric type, the score can be either the distance or the similarity between the query and the fact and its range depends on the metric type.For example, if the metric type is COSINE_DISTANCE, it represents the distance between the query and the fact. The larger the distance, the less relevant the fact is to the query. The range is [0, 2], while 0 means the most relevant and 2 means the least relevant. | `chunk` `object (`[RagChunk](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagChunk)`)` If present, chunk properties. | JSON representation  
---  
      
    
    {
      "query": string,
      "title": string,
      "uri": string,
      "summary": string,
      "vectorDistance": number,
      "score": number,
      "chunk": {
        object ([RagChunk](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagChunk))
      }
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
