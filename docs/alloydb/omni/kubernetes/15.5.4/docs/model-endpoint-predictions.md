---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/model-endpoint-predictions/
title: Invoke predictions with model endpoint management \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:25:23.891315+00:00
---

# Invoke predictions with model endpoint management  |  AlloyDB Omni for Kubernetes: 15.5.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/model-endpoint-predictions/

This page documents AlloyDB Omni version **15.5.4** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/overview)



Send feedback 

#  Invoke predictions with model endpoint management Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.4keyboard_arrow_down

  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/model-endpoint-predictions)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/model-endpoint-predictions)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-predictions)



**Preview — Model endpoint management**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes a preview that lets you experiment with registering an AI model endpoint and invoking predictions with Model endpoint management. For using AI models in production environments, see [Build generative AI applications using AlloyDB AI](https://docs.cloud.google.com/alloydb/docs/ai).

After the model endpoints are added and registered in the Model endpoint management, you can reference them using the model ID to invoke predictions.

## Before you begin

Make sure that you have registered your model endpoint with Model endpoint management. For more information, see [Register a model endpoint with model endpoint management](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/model-endpoint-register-model)

## Invoke predictions for generic models

Use the `google_ml.predict_row()` SQL function to call a registered generic model endpoint to invoke predictions. You can use `google_ml.predict_row()` function with any model type.
    
    
    SELECT
      google_ml.predict_row(
        model_id => 'MODEL_ID',
        request_body => 'REQUEST_BODY');
    

Replace the following:

  * `MODEL_ID`: the model ID you defined when registering the model endpoint.
  * `REQUEST_BODY`: the parameters to the prediction function, in JSON format.



## Examples

Some examples for invoking predictions using registered model endpoints are listed in this section.

To generate predictions for a registered `gemini-pro` model endpoint, run the following statement:
    
    
        SELECT
            json_array_elements(
            google_ml.predict_row(
                model_id => 'gemini-pro',
                request_body => '{
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": "For TPCH database schema as mentioned here https://www.tpc.org/TPC_Documents_Current_Versions/pdf/TPC-H_v3.0.1.pdf , generate a SQL query to find all supplier names which are located in the India nation."
                        }
                    ]
                }
            ]
            }'))-> 'candidates' -> 0 -> 'content' -> 'parts' -> 0 -> 'text';
    

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
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
