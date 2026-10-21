---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-training-pipeline-custom-training-managed-dataset-sample/
title: Create a training pipeline for custom training managed dataset \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:34:52.490780+00:00
---

# Create a training pipeline for custom training managed dataset  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-training-pipeline-custom-training-managed-dataset-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Create a training pipeline for custom training managed dataset Stay organized with collections  Save and categorize content based on your preferences. 

Creates a training pipeline for custom training managed dataset using the create_training_pipeline method.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html);
    import com.google.cloud.aiplatform.v1.[InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.cloud.aiplatform.v1.[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html);
    import com.google.cloud.aiplatform.v1.[ModelContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html);
    import com.google.cloud.aiplatform.v1.[PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html);
    import com.google.gson.JsonArray;
    import com.google.gson.JsonObject;
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.IOException;
    
    public class CreateTrainingPipelineCustomTrainingManagedDatasetSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "PROJECT";
        String displayName = "DISPLAY_NAME";
        String modelDisplayName = "MODEL_DISPLAY_NAME";
        String datasetId = "DATASET_ID";
        String annotationSchemaUri = "ANNOTATION_SCHEMA_URI";
        String trainingContainerSpecImageUri = "TRAINING_CONTAINER_SPEC_IMAGE_URI";
        String modelContainerSpecImageUri = "MODEL_CONTAINER_SPEC_IMAGE_URI";
        String baseOutputUriPrefix = "BASE_OUTPUT_URI_PREFIX";
        createTrainingPipelineCustomTrainingManagedDatasetSample(
            project,
            displayName,
            modelDisplayName,
            datasetId,
            annotationSchemaUri,
            trainingContainerSpecImageUri,
            modelContainerSpecImageUri,
            baseOutputUriPrefix);
      }
    
      static void createTrainingPipelineCustomTrainingManagedDatasetSample(
          String project,
          String displayName,
          String modelDisplayName,
          String datasetId,
          String annotationSchemaUri,
          String trainingContainerSpecImageUri,
          String modelContainerSpecImageUri,
          String baseOutputUriPrefix)
          throws IOException {
        [PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html) settings =
            [PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
        String location = "us-central1";
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html) client = [PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html).create(settings)) {
          JsonArray jsonArgs = new JsonArray();
          jsonArgs.add("--model-dir=$(AIP_MODEL_DIR)");
          // training_task_inputs
          JsonObject jsonTrainingContainerSpec = new JsonObject();
          jsonTrainingContainerSpec.addProperty("imageUri", trainingContainerSpecImageUri);
          // AIP_MODEL_DIR is set by the service according to baseOutputDirectory.
          jsonTrainingContainerSpec.add("args", jsonArgs);
    
          JsonObject jsonMachineSpec = new JsonObject();
          jsonMachineSpec.addProperty("machineType", "n1-standard-8");
    
          JsonObject jsonTrainingWorkerPoolSpec = new JsonObject();
          jsonTrainingWorkerPoolSpec.addProperty("replicaCount", 1);
          jsonTrainingWorkerPoolSpec.add("machineSpec", jsonMachineSpec);
          jsonTrainingWorkerPoolSpec.add("containerSpec", jsonTrainingContainerSpec);
    
          JsonArray jsonWorkerPoolSpecs = new JsonArray();
          jsonWorkerPoolSpecs.add(jsonTrainingWorkerPoolSpec);
    
          JsonObject jsonBaseOutputDirectory = new JsonObject();
          jsonBaseOutputDirectory.addProperty("outputUriPrefix", baseOutputUriPrefix);
    
          JsonObject jsonTrainingTaskInputs = new JsonObject();
          jsonTrainingTaskInputs.add("workerPoolSpecs", jsonWorkerPoolSpecs);
          jsonTrainingTaskInputs.add("baseOutputDirectory", jsonBaseOutputDirectory);
    
          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).Builder trainingTaskInputsBuilder = [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder();
          [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(jsonTrainingTaskInputs.toString(), trainingTaskInputsBuilder);
          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html) trainingTaskInputs = trainingTaskInputsBuilder.build();
          // model_to_upload
          [ModelContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html) modelContainerSpec =
              [ModelContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html).newBuilder().setImageUri(modelContainerSpecImageUri).build();
          [Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html) model =
              [Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html).newBuilder()
                  .setDisplayName(modelDisplayName)
                  .setContainerSpec(modelContainerSpec)
                  .build();
          [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html) gcsDestination =
              [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html).newBuilder().[setOutputUriPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.Builder.html#com_google_cloud_aiplatform_v1_GcsDestination_Builder_setOutputUriPrefix_java_lang_String_)(baseOutputUriPrefix).build();
    
          // input_data_config
          [InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html) inputDataConfig =
              [InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html).newBuilder()
                  .[setDatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.Builder.html#com_google_cloud_aiplatform_v1_InputDataConfig_Builder_setDatasetId_java_lang_String_)(datasetId)
                  .setAnnotationSchemaUri(annotationSchemaUri)
                  .setGcsDestination(gcsDestination)
                  .build();
    
          // training_task_definition
          String customTaskDefinition =
              "gs://google-cloud-aiplatform/schema/trainingjob/definition/custom_task_1.0.0.yaml";
    
          [TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html) trainingPipeline =
              [TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html).newBuilder()
                  .setDisplayName(displayName)
                  .[setInputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setInputDataConfig_com_google_cloud_aiplatform_v1_InputDataConfig_)(inputDataConfig)
                  .[setTrainingTaskDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setTrainingTaskDefinition_java_lang_String_)(customTaskDefinition)
                  .[setTrainingTaskInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setTrainingTaskInputs_com_google_protobuf_Value_)(trainingTaskInputs)
                  .[setModelToUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setModelToUpload_com_google_cloud_aiplatform_v1_Model_)(model)
                  .build();
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location);
          [TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html) response = client.createTrainingPipeline(parent, trainingPipeline);
          System.out.format("response: %s\n", response);
          System.out.format("Name: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getName__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value
    
    
    def create_training_pipeline_custom_training_managed_dataset_sample(
        project: str,
        display_name: str,
        model_display_name: str,
        dataset_id: str,
        annotation_schema_uri: str,
        training_container_spec_image_uri: str,
        model_container_spec_image_uri: str,
        base_output_uri_prefix: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[PipelineServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.pipeline_service.PipelineServiceClient.html)(client_options=client_options)
    
        # input_data_config
        input_data_config = {
            "dataset_id": dataset_id,
            "annotation_schema_uri": annotation_schema_uri,
            "gcs_destination": {"output_uri_prefix": base_output_uri_prefix},
        }
    
        # training_task_definition
        custom_task_definition = "gs://google-cloud-aiplatform/schema/trainingjob/definition/custom_task_1.0.0.yaml"
    
        # training_task_inputs
        training_container_spec = {
            "imageUri": training_container_spec_image_uri,
            # AIP_MODEL_DIR is set by the service according to baseOutputDirectory.
            "args": ["--model-dir=$(AIP_MODEL_DIR)"],
        }
    
        training_worker_pool_spec = {
            "replicaCount": 1,
            "machineSpec": {"machineType": "n1-standard-8"},
            "containerSpec": training_container_spec,
        }
    
        training_task_inputs_dict = {
            "workerPoolSpecs": [training_worker_pool_spec],
            "baseOutputDirectory": {"outputUriPrefix": base_output_uri_prefix},
        }
    
        training_task_inputs = json_format.ParseDict(training_task_inputs_dict, Value())
    
        # model_to_upload
        model_container_spec = {
            "image_uri": model_container_spec_image_uri,
            "command": [],
            "args": [],
        }
    
        model = {"display_name": model_display_name, "container_spec": model_container_spec}
    
        training_pipeline = {
            "display_name": display_name,
            "input_data_config": input_data_config,
            "training_task_definition": custom_task_definition,
            "training_task_inputs": training_task_inputs,
            "model_to_upload": model,
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
