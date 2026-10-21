---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/mid/
title: Understand Machine ID (MID) \u00a0|\u00a0 Enterprise Knowledge Graph \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:24:01.410934+00:00
---

# Understand Machine ID (MID)  |  Enterprise Knowledge Graph  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/mid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Guides ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview)



Send feedback 

#  Understand Machine ID (MID) Stay organized with collections  Save and categorize content based on your preferences. 

A machine ID, or _MID_ , is a globally unique identifier generated and used by a knowledge graph. In a knowledge graph, every entity has its own MID even though the entities come from different sources. A master entity with a new MID is created after reconciling and merging entities from multiple places. In this way, a knowledge graph tracks the data origin for every data point.

![Enterprise Knowledge Graph MID concept](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/kg-mid.png)

## Cloud Knowledge Graph MID

Google Cloud Knowledge Graph introduces a new format of MID, `c-024dcv3mk`. A single-character namespace `c` is followed by a hyphen and the base-32 representation of an auto-generated alphanumeric ID. This new form of MID without `/` provides an easier way for modern applications to integrate. In Enterprise Knowledge Graph, there are two types of MIDs:

Namespace | Example | Use  
---|---|---  
`c` | `c-024dcv3mk` | Cloud Knowledge Graph MID  
`r` | `r-02b72jsgrbws18` | Candidate MID generated from Entity Reconciliation Job  
`e` | `e-02b72jsgrbws18` | Reconciled master entity MID in private graph  
  
## Crossover to Google Knowledge Graph MID

[The Google Knowledge Graph](https://en.wikipedia.org/wiki/Google_Knowledge_Graph) is a large knowledge base containing facts about people, places, books, and other kinds of entities. Some examples of Google Knowledge Graph entities include:

  * `/m/0dl567` — Taylor Swift

  * `/m/045c7b` — Google




Cloud Knowledge Graph connects existing Google KG MIDs with the new Cloud KG MIDs. If you are already using `/m` or `/g` MIDs, you can continue to look up the entities. However, the return entity uses Cloud KG MID as a primary identifier, and Google Knowledge Graph MID is referenced in the `identifier` section.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
