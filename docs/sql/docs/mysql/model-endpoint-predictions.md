---
url: https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-predictions/
title: Invoke predictions with model endpoint management \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:01:51.441488+00:00
---

# Invoke predictions with model endpoint management  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-predictions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Invoke predictions with model endpoint management Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-predictions "View this page for the PostgreSQL database engine") | SQL Server

This page describes model endpoint management. Model endpoint management lets you experiment with registering an AI model endpoint and invoking predictions. To use AI models in production environments, see [Invoke online predictions from Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/invoke-online-predictions). 

After the model endpoints are added and registered in model endpoint management, you can reference them using the model ID to invoke predictions.

## Before you begin

Make sure that you complete the following actions:

  * Register your model endpoint with model endpoint management. For more information, see [Register and call remote AI models using model endpoint management](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-register-model).
  * Create or update your Cloud SQL instance so that the instance can integrate with Vertex AI. For more information, see [Enable database integration with Vertex AI](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai#enable-database-integration-with-vertex-ai).



## Invoke predictions for generic models

Use the `mysql.ml_predict_row()` SQL function to call a registered generic model endpoint to invoke predictions. You can use `mysql.ml_predict_row()` function with any model type.
    
    
    SELECT
      mysql.ml_predict_row(
        'MODEL_ID',
        'REQUEST_BODY');
    

Replace the following:

  * `MODEL_ID`: the model ID you defined when registering the model endpoint
  * `REQUEST_BODY`: the parameters to the prediction function, in JSON format



## Examples

To generate predictions for a registered `gemini-flash` model endpoint, run the following statement:
    
    
      SELECT JSON_EXTRACT(
        mysql.ml_predict_row(
          'gemini-2.5-flash',
          '{
                 "contents": [
                 {
                    "role": "user",
                    "parts": [
                        {
                        "text": "For TPCH database schema as mentioned here https://www.tpc.org/TPC_Documents_Current_Versions/pdf/TPC-H_v3.0.1.pdf , generate a SQL query to find allsupplier names which are located in the India nation."
                        } ]}]
                }'
        ),
        '$.candidates[0].content.parts[0].text'
      );
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
