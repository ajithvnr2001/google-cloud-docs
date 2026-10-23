---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-data-labeling-job-active-learning-sample/
title: Create a data labeling job for active learning \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:22.116809+00:00
---

# Create a data labeling job for active learning  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-data-labeling-job-active-learning-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Create a data labeling job for active learning Stay organized with collections  Save and categorize content based on your preferences. 

Creates a data labeling job for active learning using the create_data_labeling_job method.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[ActiveLearningConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ActiveLearningConfig.html);
    import com.google.cloud.aiplatform.v1.[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob.html);
    import com.google.cloud.aiplatform.v1.[DatasetName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetName.html);
    import com.google.cloud.aiplatform.v1.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html);
    import com.google.cloud.aiplatform.v1.[JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.gson.JsonArray;
    import com.google.gson.JsonObject;
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.IOException;
    
    public class CreateDataLabelingJobActiveLearningSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "PROJECT";
        String displayName = "DISPLAY_NAME";
        String dataset = "DATASET";
        String instructionUri = "INSTRUCTION_URI";
        String inputsSchemaUri = "INPUTS_SCHEMA_URI";
        String annotationSpec = "ANNOTATION_SPEC";
        createDataLabelingJobActiveLearningSample(
            project, displayName, dataset, instructionUri, inputsSchemaUri, annotationSpec);
      }
    
      static void createDataLabelingJobActiveLearningSample(
          String project,
          String displayName,
          String dataset,
          String instructionUri,
          String inputsSchemaUri,
          String annotationSpec)
          throws IOException {
        [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html) settings =
            [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
        String location = "us-central1";
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html) client = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html).create(settings)) {
          JsonArray jsonAnnotationSpecs = new JsonArray();
          jsonAnnotationSpecs.add(annotationSpec);
          JsonObject jsonInputs = new JsonObject();
          jsonInputs.add("annotation_specs", jsonAnnotationSpecs);
          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).Builder inputsBuilder = [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder();
          [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(jsonInputs.toString(), inputsBuilder);
          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html) inputs = inputsBuilder.build();
          [ActiveLearningConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ActiveLearningConfig.html) activeLearningConfig =
              [ActiveLearningConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ActiveLearningConfig.html).newBuilder().[setMaxDataItemCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ActiveLearningConfig.Builder.html#com_google_cloud_aiplatform_v1_ActiveLearningConfig_Builder_setMaxDataItemCount_long_)(1).build();
    
          String datasetName = [DatasetName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetName.html).of(project, location, dataset).toString();
    
          [DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob.html) dataLabelingJob =
              [DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob.html).newBuilder()
                  .setDisplayName(displayName)
                  .addDatasets(datasetName)
                  .[setLabelerCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob.Builder.html#com_google_cloud_aiplatform_v1_DataLabelingJob_Builder_setLabelerCount_int_)(1)
                  .[setInstructionUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob.Builder.html#com_google_cloud_aiplatform_v1_DataLabelingJob_Builder_setInstructionUri_java_lang_String_)(instructionUri)
                  .[setInputsSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob.Builder.html#com_google_cloud_aiplatform_v1_DataLabelingJob_Builder_setInputsSchemaUri_java_lang_String_)(inputsSchemaUri)
                  .setInputs(inputs)
                  .putAnnotationLabels(
                      "aiplatform.googleapis.com/annotation_set_name",
                      "data_labeling_job_active_learning")
                  .[setActiveLearningConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob.Builder.html#com_google_cloud_aiplatform_v1_DataLabelingJob_Builder_setActiveLearningConfig_com_google_cloud_aiplatform_v1_ActiveLearningConfig_)(activeLearningConfig)
                  .build();
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location);
          [DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob.html) response = client.createDataLabelingJob(parent, dataLabelingJob);
          System.out.format("response: %s\n", response);
          System.out.format("Name: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob.html#com_google_cloud_aiplatform_v1_DataLabelingJob_getName__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value
    
    
    def create_data_labeling_job_active_learning_sample(
        project: str,
        display_name: str,
        dataset: str,
        instruction_uri: str,
        inputs_schema_uri: str,
        annotation_spec: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.job_service.JobServiceClient.html)(client_options=client_options)
        inputs_dict = {"annotation_specs": [annotation_spec]}
        inputs = json_format.ParseDict(inputs_dict, Value())
    
        active_learning_config = {"max_data_item_count": 1}
    
        data_labeling_job = {
            "display_name": display_name,
            # Full resource name: projects/{project}/locations/{location}/datasets/{dataset_id}
            "datasets": [dataset],
            "labeler_count": 1,
            "instruction_uri": instruction_uri,
            "inputs_schema_uri": inputs_schema_uri,
            "inputs": inputs,
            "annotation_labels": {
                "aiplatform.googleapis.com/annotation_set_name": "data_labeling_job_active_learning"
            },
            "active_learning_config": active_learning_config,
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
