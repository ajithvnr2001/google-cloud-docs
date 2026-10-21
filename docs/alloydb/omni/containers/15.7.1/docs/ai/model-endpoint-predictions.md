---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/model-endpoint-predictions/
title: Invoke predictions with model endpoint management \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:41:12.406596+00:00
---

# Invoke predictions with model endpoint management  |  AlloyDB Omni for containers: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/model-endpoint-predictions/

This page documents AlloyDB Omni version **15.7.1** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)



Send feedback 

#  Invoke predictions with model endpoint management Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.1keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/model-endpoint-predictions)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/model-endpoint-predictions)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/model-endpoint-predictions)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/model-endpoint-predictions)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/ai/model-endpoint-predictions)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/model-endpoint-predictions)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/model-endpoint-predictions)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/model-endpoint-predictions)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/ai/model-endpoint-predictions)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/model-endpoint-predictions)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/model-endpoint-predictions)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/model-endpoint-predictions)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/model-endpoint-predictions)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/model-endpoint-predictions)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/model-endpoint-predictions)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/model-endpoint-predictions)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/model-endpoint-predictions)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/model-endpoint-predictions)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/model-endpoint-predictions)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/model-endpoint-predictions)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/model-endpoint-predictions)

This page describes how to invoke predictions using the model endpoints registered in the Model endpoint management. 

## Before you begin

Make sure that you have registered your model endpoint with Model endpoint management. For more information, see [Register and call remote AI models in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/register-model-endpoint).

## Invoke predictions for generic models

Use the `google_ml.predict_row()` SQL function to call a registered generic model endpoint to invoke predictions.
    
    
    SELECT
      google_ml.predict_row(
        model_id => 'MODEL_ID',
        request_body => 'REQUEST_BODY');
    

Replace the following:

  * `MODEL_ID`: the model ID you defined when registering the model endpoint.
  * `REQUEST_BODY`: the parameters to the prediction function, in JSON format.



## Examples

This section includes some examples for invoking predictions using registered model endpoints.

To generate predictions for a registered `gemini-1.5-pro:streamGenerateContent` model endpoint, run the following statement:
    
    
      SELECT
      json_array_elements( google_ml.predict_row( model_id => 'gemini-1.5-pro:streamGenerateContent',
          request_body => '{ "contents": [ { "role": "user", "parts": [ { "text": "For TPCH database schema as mentioned here https://www.tpc.org/TPC_Documents_Current_Versions/pdf/TPC-H_v3.0.1.pdf , generate a SQL query to find all supplier names which are located in the India nation." } ] } ] }'))-> 'candidates' -> 0 -> 'content' -> 'parts' -> 0 -> 'text';
    

To generate predictions for a registered `facebook/bart-large-mnli` model endpoint on Hugging Face, run the following statement:
    
    
      SELECT
      google_ml.predict_row(
        model_id => 'facebook/bart-large-mnli',
        request_body =>
          '{
           "inputs": "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!",
        "parameters": {"candidate_labels": ["refund", "legal", "faq"]}
        }'
      );
    

To generate predictions for a registered Anthropic `claude-3-opus-20240229` model endpoint, run the following statement:
    
    
      SELECT
      google_ml.predict_row('anthropic-opus', '{
        "model": "claude-3-opus-20240229",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Hello, world"}
        ]
      }');
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
