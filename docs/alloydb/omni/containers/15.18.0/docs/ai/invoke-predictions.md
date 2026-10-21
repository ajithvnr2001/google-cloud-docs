---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/invoke-predictions/
title: Invoke online predictions from AlloyDB databases \u00a0|\u00a0 AlloyDB Omni using containers: 15.18.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:40:17.028222+00:00
---

# Invoke online predictions from AlloyDB databases  |  AlloyDB Omni using containers: 15.18.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/invoke-predictions/

This page documents AlloyDB Omni version **15.18.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/overview)



Send feedback 

#  Invoke online predictions from AlloyDB databases Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.18.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/invoke-predictions)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/invoke-predictions)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/invoke-predictions)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/invoke-predictions)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/ai/invoke-predictions)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/invoke-predictions)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/invoke-predictions)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/invoke-predictions)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/ai/invoke-predictions)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/invoke-predictions)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/invoke-predictions)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/invoke-predictions)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/invoke-predictions)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/invoke-predictions)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/invoke-predictions)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/invoke-predictions)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/invoke-predictions)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/invoke-predictions)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/invoke-predictions)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/invoke-predictions)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/invoke-predictions)



This page shows how to invoke online predictions from an AlloyDB Omni database.

AlloyDB gives you the ability to get online predictions in your SQL code by calling the `ml_predict_row()` function. For more information about using machine learning (ML) models with AlloyDB, see [Build generative AI applications](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/overview-ai).

## Before you begin

Before you can invoke online predictions from an AlloyDB database, you must prepare your database and select an appropriate ML model.

### Prepare your database

  1. [Set up integration between your database and Vertex AI](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/install-with-alloydb-ai).

  2. Grant permission for database users to execute the `ml_predict_row()` function to run predictions:

     1. Connect a `psql` client to the cluster's primary instance, as described in [Connect a psql client to an instance](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/run-connect#connect).

     2. At the psql command prompt, connect to the database and grant permissions:
            
            \c DB_NAME
            
            GRANT EXECUTE ON FUNCTION ml_predict_row TO USER_NAME;
            

Replace the following:

        * DB_NAME: the name of the database on which the permissions must be granted.

        * USER_NAME: the name of the user for whom the permissions must be granted.




### Select an ML model

When you call the `ml_predict_row()` function, you must specify the location of an ML model. The model that you specify can be one of these:

  * A model that's running in [the Vertex AI Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models).

The `ml_predict_row()` function supports invoking predictions only on tabular or custom models.

  * A Vertex AI model with an active endpoint that you have Identity and Access Management (IAM) permission to access.

AlloyDB doesn't support [private endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/using-private-endpoints) for getting online predictions.




## Invoke online predictions

Use the `ml_predict_row()` SQL function to invoke online predictions against your data.

The format of the function's initial argument depends on whether the ML model that you want to use is in the Vertex AI Model Garden or is an endpoint running in a Google Cloud project.

### Use a model in the Vertex AI Model Garden

To invoke an online prediction using an ML model that's running in the Vertex AI Model Garden, use the following syntax for the `ml_predict_row()` SQL function:
    
    
    SELECT ml_predict_row('projects/PROJECT_ID/locations/REGION_ID/publishers/google/models/MODEL_ID', '{ CONTENTS }');
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project

  * `REGION_ID`: the ID of the Google Cloud region that the model is located in—for example, `us-central1` for gemini-2.5-flash

  * `MODEL_ID`: the ID of the ML model to use—for example, gemini-2.5-flash

  * `CONTENTS`: the inputs to the prediction call, in JSON format




If the ML model is stored in the same project and region as your AlloyDB cluster, then you can abbreviate this function's first argument:
    
    
    SELECT ml_predict_row('publishers/google/models/MODEL_ID', '{ CONTENTS }');
    

For information about the model's JSON response messages, see [Generative AI foundational model reference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference).

For examples, see Example invocations.

### Use a Vertex AI model endpoint

To invoke an online prediction using a Vertex AI model endpoint, use the following syntax for the `ml_predict_row()` SQL function:
    
    
    SELECT ml_predict_row('projects/PROJECT_ID/locations/REGION_ID/endpoints/ENDPOINT_ID', '{ CONTENTS }');
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that the model is located in

  * `REGION_ID`: the ID of the Google Cloud region the model is located in—for example, `us-central1`

  * `ENDPOINT_ID`: the ID of the model endpoint

  * `CONTENTS`: the inputs to the prediction call, in JSON format




If the endpoint is located in the same project and region as your AlloyDB cluster, then you can abbreviate this function's first argument:
    
    
    SELECT ml_predict_row('endpoints/ENDPOINT_ID', '{ CONTENTS }');
    

For information about the model's JSON response messages, see [PredictResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PredictResponse).

### Example invocations

The following example uses [gemini-2.5-flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference), available in the Model Garden, to generate text based on a short prompt that is provided as a literal argument to `ml_predict_row()`:
    
    
    select ML_PREDICT_ROW('projects/PROJECT_ID/locations/us-central1/publishers/google/models/gemini-2.5-flash:generateContent', '{
      "contents": [{
        "role": "user",
        "parts": [{
          "text": "What is AlloyDB?"
        }]
      }]
    }');
    

The response is a JSON object. For more information about the format of the object, see [Response body](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference#response).

The next example modifies the previous one in the following ways:

  * The example uses the contents of the current database's `messages.message` column as input.

  * The example demonstrates the use of [the `json_build_object()` function](https://www.postgresql.org/docs/current/functions-json.html) as an aid to formatting the function parameters.



    
    
    select ML_PREDICT_ROW('projects/PROJECT_ID/locations/us-central1/publishers/google/models/gemini-2.5-flash:generateContent', json_build_object('contents', json_build_object('text', message))) from messages;
    

The returned JSON object now contains one entry in its `candidates` array for every row in the `messages` table.

Because the response is a JSON object, you can pull specific fields from it using the PostgreSQL arrow operator:
    
    
    select ML_PREDICT_ROW('projects/PROJECT_ID/locations/us-central1/publishers/google/models/gemini-2.5-flash:generateContent', json_build_object('contents', json_build_object('text', message)))->'candidates'->0->'content'->'parts'->0->'text' FROM messages;
    

For more example arguments to `ml_predict_row()`, see [Quickstart using the Vertex AI API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
