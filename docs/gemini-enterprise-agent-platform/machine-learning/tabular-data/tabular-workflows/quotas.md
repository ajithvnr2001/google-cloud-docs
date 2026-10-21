---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/tabular-workflows/quotas/
title: Manage quotas for Tabular Workflows \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:33.612558+00:00
---

# Manage quotas for Tabular Workflows  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/tabular-workflows/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Manage quotas for Tabular Workflows Stay organized with collections  Save and categorize content based on your preferences. 

If you receive a quota-related error while running the Tabular Workflow for End-to-End AutoML, request a higher quota. To learn more, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage). 

The following table shows our recommended quota values. We recommend setting the quota values as a function of the number of concurrent training jobs (`num_concurrent_pipeline`) and the number of CPUs in the requested region. The recommended values are valid only if you use the default Compute Engine resource configuration for your workflow.

Service | Quota | Recommendation  
---|---|---  
Compute Engine API | CPUs | `num_concurrent_pipeline` x 440 CPUs  
Compute Engine API | Persistent Disk Standard (GB) | `num_concurrent_pipeline` x 5TB persistent disk  
Agent Platform API | Restricted image training CPUs for N1/E2 machine types per region | `num_concurrent_pipeline` x 440 CPUs  
Agent Platform API | Restricted image training total persistent disk SSD storage (GB) per region | `num_concurrent_pipeline` x 8TB persistent disk  
Agent Platform API | Resource management (CRUD) requests per minute per region | `num_concurrent_pipeline` x 150  
Agent Platform API | Job or LRO submission requests per minute per region | `num_concurrent_pipeline` x 6  
  
## What's next

  * [Train a model using End-to-End AutoML](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/tabular-workflows/e2e-automl-train).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
