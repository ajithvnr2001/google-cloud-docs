---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-explain-tabular-sample/
title: Explain for tabular \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:27:00.695527+00:00
---

# Explain for tabular  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-explain-tabular-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Explain for tabular Stay organized with collections  Save and categorize content based on your preferences. 

Gets explanation for tabular using the explain method.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Dict
    
    from google.cloud import aiplatform_v1beta1
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value
    
    
    def explain_tabular_sample(
        project: str,
        endpoint_id: str,
        instance_dict: Dict,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform_v1beta1.[PredictionServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.services.prediction_service.PredictionServiceClient.html)(client_options=client_options)
        # The format of each instance should conform to the deployed model's prediction input schema.
        instance = json_format.ParseDict(instance_dict, Value())
        instances = [instance]
        # tabular models do not have additional parameters
        parameters_dict = {}
        parameters = json_format.ParseDict(parameters_dict, Value())
        endpoint = client.[endpoint_path](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.services.prediction_service.PredictionServiceClient.html#google_cloud_aiplatform_v1beta1_services_prediction_service_PredictionServiceClient_endpoint_path)(
            project=project, location=location, endpoint=endpoint_id
        )
        response = client.[explain](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.services.prediction_service.PredictionServiceClient.html#google_cloud_aiplatform_v1beta1_services_prediction_service_PredictionServiceClient_explain)(
            endpoint=endpoint, instances=instances, parameters=parameters
        )
        print("response")
        print(" deployed_model_id:", response.deployed_model_id)
        explanations = response.explanations
        for explanation in explanations:
            print(" explanation")
            # Feature attributions.
            attributions = explanation.attributions
            for attribution in attributions:
                print("  attribution")
                print("   baseline_output_value:", attribution.baseline_output_value)
                print("   instance_output_value:", attribution.instance_output_value)
                print("   output_display_name:", attribution.output_display_name)
                print("   approximation_error:", attribution.approximation_error)
                print("   output_name:", attribution.output_name)
                output_index = attribution.output_index
                for output_index in output_index:
                    print("   output_index:", output_index)
        predictions = response.predictions
        for prediction in predictions:
            print(" prediction:", dict(prediction))
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
