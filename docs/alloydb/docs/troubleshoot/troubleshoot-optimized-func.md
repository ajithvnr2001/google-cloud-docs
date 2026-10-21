---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-optimized-func/
title: Troubleshoot optimized functions \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:21.227039+00:00
---

# Troubleshoot optimized functions  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-optimized-func/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Troubleshoot optimized functions Stay organized with collections  Save and categorize content based on your preferences. 

This document describes errors you might encounter when you use [optimized AI functions](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions). Examples of errors and recommended fixes are also provided.

## Reduced performance expected. Optimized AI function is not available

### Description

This warning indicates that the query fell back to using the LLM. This occurs when the optimized function is still training, was never prepared, failed the runtime accuracy validation check, or if the content and embedding columns referenced in the `ai.if()` function don't belong to the same table. For smaller tables, the proxy model might not generalize well, and accuracy is generally less than 95%, so AlloyDB uses the LLM by default.

### Sample query that causes the error
    
    
    EXECUTE positive_reviews_query;
    

### Recommended fix

  * Wait for the optimized function training to complete.
  * Make sure that the query is correctly prepared using the `PREPARE` statement.
  * Verify that the content and embedding columns referenced in the `ai.if()` function belong to the same table.
  * Optimized functions ([Preview](https://cloud.google.com/products#product-launch-stages)) are better suited for larger tables. You can also use [array-based AI functions](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators) to improve performance.
  * If you want to bypass the runtime accuracy check (for example, in development environments), set `google_ml_integration.runtime_accuracy_check` to `off` for the entire database environment.
        
        ALTER DATABASE DATABASE_NAME SET google_ml_integration.runtime_accuracy_check = off;
        

Replace `DATABASE_NAME` with the name of your database.




## Query is not processing any rows or model preparation is failing

### Description

If the query isn't processing any rows, the primary reason is that the embeddings aren't generated or when the entire embedding column has `NULL` values. This causes the query preparation to fail, because it doesn't sample any rows that have `NULL` embeddings.

### Recommended fix

  * Generate embeddings for your data before you use optimized functions.
  * Make sure that the embedding column doesn't contain `NULL` values.
  * Queries that differ only in constant values in the `WHERE` clause might still use an existing trained model.



## Slow performance despite using optimized AI functions

### Description

Ensure that you aren't exceeding your Gemini Enterprise Agent Platform quota. Even with optimized AI functions, the initial runtime accuracy check requires calling the remote LLM for a sample of rows. An insufficient quota can cause this initial check to be slow or to fail.

### Recommended fix

Check your Agent Platform quota and request an increase if necessary to ensure that the initial runtime accuracy check can proceed without delays.

## ERROR: function ai.if(prompt => text, embedding => vector) does not exist

### Description

If you pass the `model_id` parameter along with the embedding column when calling the `ai.if()` function, AlloyDB doesn't use the trained proxy model, and generates an error similar to the following:
    
    
    testdb=# select ai.if('Is the rating positive?' || review, review_embedding, 'gemini-2.5-pro') from restaurant_reviews;
    ERROR:  function ai.if(text, vector, unknown) does not exist
    LINE 1: select ai.if('Is the rating positive?' || review, review_embe...
                   ^
    HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
    

### Recommended fix

Ensure that you aren't passing the `model_id` value when you call the `ai.if()` function. This ensures that AlloyDB uses the trained proxy model to process the query.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
