---
url: https://docs.cloud.google.com/bigquery/docs/choose-text-generation-function/
title: Choose a text generation function \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:04.220129+00:00
---

# Choose a text generation function  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/choose-text-generation-function/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Choose a text generation function

This document provides a comparison of the BigQuery ML [`AI.GENERATE_TEXT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-text) and [`AI.GENERATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate) text generation functions. You can use the information in this document to help you decide which function to use in cases where the functions have overlapping capabilities.

## Function similarities

The `AI.GENERATE_TEXT` and `AI.GENERATE` functions are similar in the following ways:

  * **Purpose** : Generate text by passing a prompt to a large language model (LLM).
  * **Billing** : Incur BigQuery ML charges for data processed. For more information, see [BigQuery ML pricing](https://cloud.google.com/bigquery/pricing#bigquery-ml-pricing). Incur Gemini Enterprise Agent Platform charges for calls to the LLM. If you are using a Gemini 2.0 or greater model, the call is billed at the batch API rate. For more information, see [Cost of building and deploying AI models in Agent Platform](https://docs.cloud.google.com/vertex-ai/generative-ai/pricing).
  * **Scalability** : Process between 1 million and 10 million rows for each a 6-hour query job. Actual throughput depends on factors like the average token length in the input rows. For more information, see [Generative AI functions](https://docs.cloud.google.com/bigquery/quotas#generative_ai_functions).
  * **Input data** : Support both text and unstructured data from BigQuery standard tables and object tables.



## Function differences

Use the following table to evaluate the differences between the `AI.GENERATE_TEXT` and `AI.GENERATE` functions:

| `AI.GENERATE_TEXT` | `AI.GENERATE`  
---|---|---  
Function signature | A table-valued function that takes a table as input and returns a table as output. | A scalar function that takes a single value as input and returns a single value as output.  
Supported LLMs | 

  * Gemini models
  * Partner models such as Anthropic Claude, Llama, and Mistral AI
  * open models

| Gemini models  
Function output content |  Function output content for Gemini models:

  * Generated text
  * Responsible AI (RAI) results
  * Google Search grounding results, if enabled
  * LLM call status

Function output content for other types of models:

  * Generated text
  * LLM call status

| 

  * Generated text
  * Full model response in JSON format
  * LLM call status

  
Function output format | Generated values are returned in a single JSON column or in separate table columns, depending on the `flatten_json_output` argument value. | Generated values are returned as fields in a `STRUCT` object.  
User journey | You must create a [remote model](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model#create_model_syntax) before using the function. | You can use the function directly, without the need to create a remote model.  
Permission setup  | You must manually create a BigQuery connection, and grant the Agent Platform User role permission to the service account of the connection. You can skip this step if you are using the BigQuery [default connection](https://docs.cloud.google.com/bigquery/docs/default-connections#example-remote-model). | You can call this function using your [end-user credentials](https://docs.cloud.google.com/bigquery/docs/permissions-for-ai-functions).  
Advantages | Allows for more flexible input and output formats. | Easier to integrate into SQL queries.  
Extended functions | You can use the [`AI.GENERATE_TABLE` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-table) to generate output that is structured according to a SQL output schema that you specify. | You can use the [`AI.GENERATE_BOOL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-bool), [`AI.GENERATE_INT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-int), and [`AI.GENERATE_DOUBLE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-double) functions to generate different types of scalar values.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
