---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/LookupPublicKgResponse/
title: LookupPublicKgResponse \u00a0|\u00a0 Enterprise Knowledge Graph \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:18.497040+00:00
---

# LookupPublicKgResponse  |  Enterprise Knowledge Graph  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/LookupPublicKgResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Reference ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries)



Send feedback 

#  LookupPublicKgResponse Stay organized with collections  Save and categorize content based on your preferences. 

. . . Response message for `[EnterpriseKnowledgeGraphService.LookupPublicKg](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/reference/rest/v1/projects.locations.publicKnowledgeGraphEntities/lookup#google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.LookupPublicKg)`.

JSON representation  
---  
      
    
    {
      "@context": value,
      "@type": value,
      "itemListElement": array
    }  
  
Fields  
---  
`@context` |  `value (`[Value](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value)` format)` The local context applicable for the response. See more details at <https://www.w3.org/TR/json-ld/#context-definitions>.  
`@type` |  `value (`[Value](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value)` format)` The schema type of top-level JSON-LD object, e.g. ItemList.  
`itemListElement` |  `array (`[ListValue](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.ListValue)` format)` The item list of search results.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-03 UTC."],[],[]] 
