---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-training-pipeline-tabular-forecasting-sample/
title: Create a training pipeline for tabular forecasting \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:34:51.195026+00:00
---

# Create a training pipeline for tabular forecasting  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-training-pipeline-tabular-forecasting-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Create a training pipeline for tabular forecasting Stay organized with collections  Save and categorize content based on your preferences. 

Creates a training pipeline for tabular forecasting using the create_training_pipeline method.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value
    
    
    def create_training_pipeline_tabular_forecasting_sample(
        project: str,
        display_name: str,
        dataset_id: str,
        model_display_name: str,
        target_column: str,
        time_series_identifier_column: str,
        time_column: str,
        time_series_attribute_columns: str,
        unavailable_at_forecast: str,
        available_at_forecast: str,
        forecast_horizon: int,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[PipelineServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.pipeline_service.PipelineServiceClient.html)(client_options=client_options)
        # set the columns used for training and their data types
        transformations = [
            {"auto": {"column_name": "date"}},
            {"auto": {"column_name": "state_name"}},
            {"auto": {"column_name": "county_fips_code"}},
            {"auto": {"column_name": "confirmed_cases"}},
            {"auto": {"column_name": "deaths"}},
        ]
    
        data_granularity = {"unit": "day", "quantity": 1}
    
        # the inputs should be formatted according to the training_task_definition yaml file
        training_task_inputs_dict = {
            # required inputs
            "targetColumn": target_column,
            "timeSeriesIdentifierColumn": time_series_identifier_column,
            "timeColumn": time_column,
            "transformations": transformations,
            "dataGranularity": data_granularity,
            "optimizationObjective": "minimize-rmse",
            "trainBudgetMilliNodeHours": 8000,
            "timeSeriesAttributeColumns": time_series_attribute_columns,
            "unavailableAtForecast": unavailable_at_forecast,
            "availableAtForecast": available_at_forecast,
            "forecastHorizon": forecast_horizon,
        }
    
        training_task_inputs = json_format.ParseDict(training_task_inputs_dict, Value())
    
        training_pipeline = {
            "display_name": display_name,
            "training_task_definition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_forecasting_1.0.0.yaml",
            "training_task_inputs": training_task_inputs,
            "input_data_config": {
                "dataset_id": dataset_id,
                "fraction_split": {
                    "training_fraction": 0.8,
                    "validation_fraction": 0.1,
                    "test_fraction": 0.1,
                },
            },
            "model_to_upload": {"display_name": model_display_name},
        }
        parent = f"projects/{project}/locations/{location}"
        response = client.[create_training_pipeline](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.pipeline_service.PipelineServiceClient.html#google_cloud_aiplatform_v1_services_pipeline_service_PipelineServiceClient_create_training_pipeline)(
            parent=parent, training_pipeline=training_pipeline
        )
        print("response:", response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
