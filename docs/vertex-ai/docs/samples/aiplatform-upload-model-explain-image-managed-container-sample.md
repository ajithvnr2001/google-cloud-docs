---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-upload-model-explain-image-managed-container-sample/
title: Upload a model for explain image managed container \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:45.210657+00:00
---

# Upload a model for explain image managed container  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-upload-model-explain-image-managed-container-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Upload a model for explain image managed container Stay organized with collections  Save and categorize content based on your preferences. 

Uploads a model for explain image managed container using the upload_model method.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform_v1beta1
    
    
    def upload_model_explain_image_managed_container_sample(
        project: str,
        display_name: str,
        container_spec_image_uri: str,
        artifact_uri: str,
        input_tensor_name: str,
        output_tensor_name: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
        timeout: int = 300,
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform_v1beta1.[ModelServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.services.model_service.ModelServiceClient.html)(client_options=client_options)
    
        # Container specification for deploying the model
        container_spec = {"image_uri": container_spec_image_uri, "command": [], "args": []}
    
        # The explainabilty method and corresponding parameters
        parameters = aiplatform_v1beta1.[ExplanationParameters](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.ExplanationParameters.html)(
            {"xrai_attribution": {"step_count": 1}}
        )
    
        # The input tensor for feature attribution to the output
        # For single input model, y = f(x), this will be the serving input layer.
        input_metadata = aiplatform_v1beta1.[ExplanationMetadata](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.ExplanationMetadata.html).[InputMetadata](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.ExplanationMetadata.InputMetadata.html)(
            {
                "input_tensor_name": input_tensor_name,
                # Input is image data
                "modality": "image",
            }
        )
    
        # The output tensor to explain
        # For single output model, y = f(x), this will be the serving output layer.
        output_metadata = aiplatform_v1beta1.[ExplanationMetadata](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.ExplanationMetadata.html).[OutputMetadata](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.ExplanationMetadata.OutputMetadata.html)(
            {"output_tensor_name": output_tensor_name}
        )
    
        # Assemble the explanation metadata
        metadata = aiplatform_v1beta1.[ExplanationMetadata](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.ExplanationMetadata.html)(
            inputs={"image": input_metadata}, outputs={"prediction": output_metadata}
        )
    
        # Assemble the explanation specification
        explanation_spec = aiplatform_v1beta1.[ExplanationSpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.ExplanationSpec.html)(
            parameters=parameters, metadata=metadata
        )
    
        model = aiplatform_v1beta1.[Model](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.Model.html)(
            display_name=display_name,
            # The Cloud Storage location of the custom model
            artifact_uri=artifact_uri,
            explanation_spec=explanation_spec,
            container_spec=container_spec,
        )
        parent = f"projects/{project}/locations/{location}"
        response = client.[upload_model](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.services.model_service.ModelServiceClient.html#google_cloud_aiplatform_v1beta1_services_model_service_ModelServiceClient_upload_model)(parent=parent, model=model)
        print("Long running operation:", response.operation.name)
        upload_model_response = response.result(timeout=timeout)
        print("upload_model_response:", upload_model_response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
