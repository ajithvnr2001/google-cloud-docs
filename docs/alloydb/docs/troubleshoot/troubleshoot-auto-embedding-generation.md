---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-auto-embedding-generation/
title: Troubleshoot auto embedding issues \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:29.450143+00:00
---

# Troubleshoot auto embedding issues  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-auto-embedding-generation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Troubleshoot auto embedding issues Stay organized with collections  Save and categorize content based on your preferences. 

This document provides workarounds for common issues that you might encounter when generating auto embeddings.

Issue | Cause | Resolution  
---|---|---  
Modifying existing auto embedding configuration | Changing the model, source column, or refresh mode requires clearing the old configuration. | Call `ai.drop_embedding_config` to remove existing settings, then call `ai.initialize_embeddings` again with the new configuration.  
Disabling transactional mode | Transactional mode is enabled using `ai.initialize_embeddings`. | Call `ai.drop_embedding_config` to remove the metadata and the trigger.  
Slow inserts and updates in transactional mode | Embeddings are generated serially within the same transaction, so model latency impacts transaction time. | Check model latency and consider if transactional mode is necessary for your use case.  
Slow auto embedding generation | Might be due to model request quota limits being exceeded. | Examine the model request quota for your embedding model. Adjust the `batch_size`. Contact [support](https://cloud.google.com/support) if the issue persists.  
`Error: 'AutoEmbeddingGeneration: Request size is greater than 4MB'` | The request size for a batch exceeds the maximum supported size of 4MB. | Reduce the `batch_size` value in your function call and retry.  
Permission error calling `initialize_embeddings` in transactional mode | Transactional mode creates triggers, which requires table owner privileges. | Ensure that the user calling the function is the table owner or has the owner role.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
