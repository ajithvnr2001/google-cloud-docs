---
url: https://docs.cloud.google.com/sql/docs/mysql/invoke-online-predictions/
title: Invoke online predictions from Cloud SQL instances \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:08.351000+00:00
---

# Invoke online predictions from Cloud SQL instances  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/invoke-online-predictions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Invoke online predictions from Cloud SQL instances Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/invoke-online-predictions "View this page for the PostgreSQL database engine") | SQL Server

This page shows you how to invoke online predictions from a Cloud SQL instance.

Cloud SQL lets you get online predictions in your SQL code by calling the `mysql.ml_predict_row()` function.

## Before you begin

Before you can invoke online predictions from a Cloud SQL instance, you must prepare your database and select an appropriate ML model.

### Prepare your database

To prepare your database, [set up integration between Cloud SQL and Vertex AI.](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai)

### Select an ML model

When you call the `mysql.ml_predict_row()` function, you must specify the location of an ML model. The model that you specify can be one of these:

  * A model that's running in the [Vertex AI Model Garden](https://docs.cloud.google.com/vertex-ai/docs/start/explore-models).

The `mysql.ml_predict_row()` function supports invoking predictions only on tabular or custom models.

  * A Vertex AI model with an active endpoint that you have Identity and Access Management (IAM) permission to access.

Cloud SQL doesn't support [private endpoints](https://docs.cloud.google.com/vertex-ai/docs/predictions/using-private-endpoints) for getting online predictions.




## Invoke online predictions

You can use the `mysql.ml_predict_row()` SQL function to invoke online predictions against your data.

The format of the function's initial argument depends on whether the ML model that you want to use is in the Vertex AI Model Garden or is an endpoint running in a Google Cloud project.

### Use a model in the Vertex AI Model Garden

To invoke an online prediction using an ML model that's running in the Vertex AI Model Garden, use the following syntax for the `mysql.ml_predict_row()` SQL function:
    
    
    SELECT mysql.ML_PREDICT_ROW('publishers/google/models/MODEL_ID', '{ "instances": [ INSTANCES ], "parameters":
    PARAMETERS }');
    

Make the following replacements:

  * MODEL_ID: the ID of the ML model to use (for example, `gemini-2.0`)

  * INSTANCES: the inputs to the prediction call, in JSON format

  * PARAMETERS: the parameters to the prediction call, in JSON format


**Note:** You must store the ML model in the same project and region as your Cloud SQL instance.
    
    
    SELECT mysql.ML_PREDICT_ROW('publishers/google/models/MODEL_ID', '{ "instances": [ INSTANCES ], "parameters":
    PARAMETERS }');
    

For information about the model's JSON response messages, see [Generative AI foundational model reference](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/model-reference/overview#models). For examples, see Example invocations. 

### Use a Vertex AI model endpoint

To invoke an online prediction using a Vertex AI model endpoint, use the following syntax for the `mysql.ml_predict_row()` SQL function:
    
    
    SELECT mysql.ML_PREDICT_ROW('endpoints/ENDPOINT_ID', '{ "instances": [ INSTANCES ], "parameters":
    PARAMETERS }');
    

Make the following replacements:

  * ENDPOINT_ID: the ID of the model's endpoint

  * INSTANCES: the inputs to the prediction call, in JSON format

  * PARAMETERS: the parameters to the prediction call, in JSON format 


**Note:** The endpoint must be located in the same project and region as your Cloud SQL instance.

For information about the model's JSON response messages, see [PredictResponse](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/PredictResponse).

### Example invocations

The following example uses [Gemini 2.5 Flash](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini), available in the Model Garden, to generate text based on a short prompt that's provided as a literal argument to `mysql.ml_predict_row()`:

`sql select mysql.ML_PREDICT_ROW('publishers/google/models/gemini-2.0-flash:generateContent', '{ "contents": [{ "role": "user", "parts": [{ "text": "Write me a short poem about MySQL" }] }] }');` **Note:** You can use Gemini foundation models only in regions where Vertex AI supports Gemini.

The response is a JSON object. For more information about the format of the object, see [Response body](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#response_body).

The next example modifies the previous one in the following ways:

  * The example uses the contents of the current database's `messages.message` column as input.

  * The example demonstrates the use of the `json_object()` function as an aid to formatting the function's parameters.



    
    
    select mysql.ML_PREDICT_ROW('projects/PROJECT_ID/locations/us-central1/publishers/google/models/text-bison', json_object('instances', json_object('prompt', message), 'parameters', json_object('maxOutputTokens', 1024,'topK', 40,'topP', 0.8,'temperature', 0.2))) from messages;
    

For every row in the `messages` table, the returned JSON object now contains one entry in its `candidates` array.

Because the response is a JSON object, you can pull specific fields from it:
    
    
    select JSON_EXTRACT(mysql.ml_PREDICT_ROW('publishers/google/models/gemini-2.0-flash:generateContent', JSON_OBJECT(
      'contents', JSON_ARRAY(
        JSON_OBJECT(
          'role', 'user',
          'parts', JSON_ARRAY(
            JSON_OBJECT(
              'text', message
            )
          )
        )
      )
    )), '$.candidates[0].content.parts[0].text') from messages;
    

For more example arguments to `ml_predict_row()`, see [Try the Vertex AI Gemini API](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/start/quickstarts/api-quickstart).

## What's next

  * [Build generative AI applications using Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/ai-overview)

  * [Integrate Cloud SQL with Vertex AI](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai)

  * [Understand an example of an embedding workflow](https://docs.cloud.google.com/sql/docs/mysql/understand-example-embedding-workflow)

  * [Build LLM-powered applications using LangChain](https://docs.cloud.google.com/sql/docs/mysql/langchain)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
