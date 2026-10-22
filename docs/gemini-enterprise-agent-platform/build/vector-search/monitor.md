---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/monitor/
title: Monitor a deployed index \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:46:44.164220+00:00
---

# Monitor a deployed index  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Monitor a deployed index Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise Agent Platform provides two metrics for monitoring the `IndexEndpoint` of a deployed index:

  * `aiplatform.googleapis.com/matching_engine/current_shards`

The number of shards of the `DeployedIndex`. As data is added and deleted, Vector Search automatically reshards the index to achieve optimal performance. This metric indicates the current number of shards of the deployed index.

  * `aiplatform.googleapis.com/matching_engine/current_replicas`

The total number of active replica servers being used by the `DeployedIndex`. To match query volume, Vector Search automatically turns up or down replica servers based on the minimum and maximum replica settings specified when deploying the index.

If the index has multiple shards, each shard can be served by using a different number of replica servers. This metric is the total number of replica servers across all shards of the given index.




### What's next

  * Learn [how to query your indexes to find their nearest neighbors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/query-index-public-endpoint).
  * Learn [how to select, query, and display these metrics in Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-selector).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
