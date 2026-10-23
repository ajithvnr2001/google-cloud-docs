---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-data-labeling-job-image-segmentation-sample/
title: Create a data labeling job for image segmentation \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:38.674983+00:00
---

# Create a data labeling job for image segmentation  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-data-labeling-job-image-segmentation-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Create a data labeling job for image segmentation Stay organized with collections  Save and categorize content based on your preferences. 

Creates a data labeling job for image segmentation using the create_data_labeling_job method.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value
    
    
    def create_data_labeling_job_image_segmentation_sample(
        project: str,
        display_name: str,
        dataset: str,
        instruction_uri: str,
        inputs_schema_uri: str,
        annotation_spec: dict,
        annotation_set_name: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.job_service.JobServiceClient.html)(client_options=client_options)
        inputs_dict = {"annotationSpecColors": [annotation_spec]}
        inputs = json_format.ParseDict(inputs_dict, Value())
    
        data_labeling_job = {
            "display_name": display_name,
            # Full resource name: projects/{project}/locations/{location}/datasets/{dataset_id}
            "datasets": [dataset],
            "labeler_count": 1,
            "instruction_uri": instruction_uri,
            "inputs_schema_uri": inputs_schema_uri,
            "inputs": inputs,
            "annotation_labels": {
                "aiplatform.googleapis.com/annotation_set_name": annotation_set_name
            },
        }
        parent = f"projects/{project}/locations/{location}"
        response = client.[create_data_labeling_job](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.job_service.JobServiceClient.html#google_cloud_aiplatform_v1_services_job_service_JobServiceClient_create_data_labeling_job)(
            parent=parent, data_labeling_job=data_labeling_job
        )
        print("response:", response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
