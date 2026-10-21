---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/LineageSubgraph/
title: LineageSubgraph \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:57:25.687357+00:00
---

# LineageSubgraph  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/LineageSubgraph/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  LineageSubgraph Stay organized with collections  Save and categorize content based on your preferences. 

A subgraph of the overall lineage graph. Event edges connect Artifact and Execution nodes.

Fields  
  
`artifacts[]` `object (`[Artifact](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.artifacts#Artifact)`)` The Artifact nodes in the subgraph. | `executions[]` `object (`[Execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions#Execution)`)` The Execution nodes in the subgraph. | `events[]` `object (`[Event](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Event)`)` The Event edges between Artifacts and Executions in the subgraph. | JSON representation  
---  
      
    
    {
      "artifacts": [
        {
          object ([Artifact](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.artifacts#Artifact))
        }
      ],
      "executions": [
        {
          object ([Execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions#Execution))
        }
      ],
      "events": [
        {
          object ([Event](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Event))
        }
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
