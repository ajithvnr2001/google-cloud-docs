---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-training-pipeline-sample/
title: Create a training pipeline \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:47.204061+00:00
---

# Create a training pipeline  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-training-pipeline-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Create a training pipeline Stay organized with collections  Save and categorize content based on your preferences. 

Creates a training pipeline using the create_training_pipeline method.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[DeployedModelRef](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModelRef.html);
    import com.google.cloud.aiplatform.v1.[EnvVar](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EnvVar.html);
    import com.google.cloud.aiplatform.v1.[FilterSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html);
    import com.google.cloud.aiplatform.v1.[FractionSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html);
    import com.google.cloud.aiplatform.v1.[InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.cloud.aiplatform.v1.[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html);
    import com.google.cloud.aiplatform.v1.[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html).[ExportFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.ExportFormat.html);
    import com.google.cloud.aiplatform.v1.[ModelContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html);
    import com.google.cloud.aiplatform.v1.[PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[Port](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Port.html);
    import com.google.cloud.aiplatform.v1.[PredefinedSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedSplit.html);
    import com.google.cloud.aiplatform.v1.[PredictSchemata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html);
    import com.google.cloud.aiplatform.v1.[TimestampSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html);
    import com.google.cloud.aiplatform.v1.[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import com.google.rpc.[Status](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html);
    import java.io.IOException;
    
    public class CreateTrainingPipelineSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String trainingPipelineDisplayName = "YOUR_TRAINING_PIPELINE_DISPLAY_NAME";
        String project = "YOUR_PROJECT_ID";
        String datasetId = "YOUR_DATASET_ID";
        String trainingTaskDefinition = "YOUR_TRAINING_TASK_DEFINITION";
        String modelDisplayName = "YOUR_MODEL_DISPLAY_NAME";
        createTrainingPipelineSample(
            project, trainingPipelineDisplayName, datasetId, trainingTaskDefinition, modelDisplayName);
      }
    
      static void createTrainingPipelineSample(
          String project,
          String trainingPipelineDisplayName,
          String datasetId,
          String trainingTaskDefinition,
          String modelDisplayName)
          throws IOException {
        [PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html) pipelineServiceSettings =
            [PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html) pipelineServiceClient =
            [PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html).create(pipelineServiceSettings)) {
          String location = "us-central1";
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html) locationName = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location);
    
          String jsonString =
              "{\"multiLabel\": false, \"modelType\": \"CLOUD\", \"budgetMilliNodeHours\": 8000,"
                  + " \"disableEarlyStopping\": false}";
          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).Builder trainingTaskInputs = [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder();
          [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(jsonString, trainingTaskInputs);
    
          [InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html) trainingInputDataConfig =
              [InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html).newBuilder().[setDatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.Builder.html#com_google_cloud_aiplatform_v1_InputDataConfig_Builder_setDatasetId_java_lang_String_)(datasetId).build();
          [Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html) model = [Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html).newBuilder().setDisplayName(modelDisplayName).build();
          [TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html) trainingPipeline =
              [TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html).newBuilder()
                  .setDisplayName(trainingPipelineDisplayName)
                  .[setTrainingTaskDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setTrainingTaskDefinition_java_lang_String_)(trainingTaskDefinition)
                  .[setTrainingTaskInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setTrainingTaskInputs_com_google_protobuf_Value_)(trainingTaskInputs)
                  .[setInputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setInputDataConfig_com_google_cloud_aiplatform_v1_InputDataConfig_)(trainingInputDataConfig)
                  .[setModelToUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setModelToUpload_com_google_cloud_aiplatform_v1_Model_)(model)
                  .build();
    
          [TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html) trainingPipelineResponse =
              pipelineServiceClient.createTrainingPipeline(locationName, trainingPipeline);
    
          System.out.println("Create Training Pipeline Response");
          System.out.format("Name: %s\n", trainingPipelineResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getName__)());
          System.out.format("Display Name: %s\n", trainingPipelineResponse.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getDisplayName__)());
    
          System.out.format(
              "Training Task Definition %s\n", trainingPipelineResponse.[getTrainingTaskDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getTrainingTaskDefinition__)());
          System.out.format(
              "Training Task Inputs: %s\n", trainingPipelineResponse.[getTrainingTaskInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getTrainingTaskInputs__)());
          System.out.format(
              "Training Task Metadata: %s\n", trainingPipelineResponse.[getTrainingTaskMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getTrainingTaskMetadata__)());
          System.out.format("State: %s\n", trainingPipelineResponse.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getState__)());
    
          System.out.format("Create Time: %s\n", trainingPipelineResponse.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getCreateTime__)());
          System.out.format("StartTime %s\n", trainingPipelineResponse.[getStartTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getStartTime__)());
          System.out.format("End Time: %s\n", trainingPipelineResponse.[getEndTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getEndTime__)());
          System.out.format("Update Time: %s\n", trainingPipelineResponse.[getUpdateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getUpdateTime__)());
          System.out.format("Labels: %s\n", trainingPipelineResponse.[getLabelsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getLabelsMap__)());
    
          [InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html) inputDataConfig = trainingPipelineResponse.[getInputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getInputDataConfig__)();
          System.out.println("Input Data Config");
          System.out.format("Dataset Id: %s", inputDataConfig.[getDatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getDatasetId__)());
          System.out.format("Annotations Filter: %s\n", inputDataConfig.[getAnnotationsFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getAnnotationsFilter__)());
    
          [FractionSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html) fractionSplit = inputDataConfig.[getFractionSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getFractionSplit__)();
          System.out.println("Fraction Split");
          System.out.format("Training Fraction: %s\n", fractionSplit.[getTrainingFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html#com_google_cloud_aiplatform_v1_FractionSplit_getTrainingFraction__)());
          System.out.format("Validation Fraction: %s\n", fractionSplit.[getValidationFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html#com_google_cloud_aiplatform_v1_FractionSplit_getValidationFraction__)());
          System.out.format("Test Fraction: %s\n", fractionSplit.[getTestFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html#com_google_cloud_aiplatform_v1_FractionSplit_getTestFraction__)());
    
          [FilterSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html) filterSplit = inputDataConfig.[getFilterSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getFilterSplit__)();
          System.out.println("Filter Split");
          System.out.format("Training Filter: %s\n", filterSplit.[getTrainingFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html#com_google_cloud_aiplatform_v1_FilterSplit_getTrainingFilter__)());
          System.out.format("Validation Filter: %s\n", filterSplit.[getValidationFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html#com_google_cloud_aiplatform_v1_FilterSplit_getValidationFilter__)());
          System.out.format("Test Filter: %s\n", filterSplit.[getTestFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html#com_google_cloud_aiplatform_v1_FilterSplit_getTestFilter__)());
    
          [PredefinedSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedSplit.html) predefinedSplit = inputDataConfig.[getPredefinedSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getPredefinedSplit__)();
          System.out.println("Predefined Split");
          System.out.format("Key: %s\n", predefinedSplit.[getKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedSplit.html#com_google_cloud_aiplatform_v1_PredefinedSplit_getKey__)());
    
          [TimestampSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html) timestampSplit = inputDataConfig.[getTimestampSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getTimestampSplit__)();
          System.out.println("Timestamp Split");
          System.out.format("Training Fraction: %s\n", timestampSplit.[getTrainingFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getTrainingFraction__)());
          System.out.format("Validation Fraction: %s\n", timestampSplit.[getValidationFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getValidationFraction__)());
          System.out.format("Test Fraction: %s\n", timestampSplit.[getTestFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getTestFraction__)());
          System.out.format("Key: %s\n", timestampSplit.[getKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getKey__)());
    
          [Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html) modelResponse = trainingPipelineResponse.[getModelToUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getModelToUpload__)();
          System.out.println("Model To Upload");
          System.out.format("Name: %s\n", modelResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getName__)());
          System.out.format("Display Name: %s\n", modelResponse.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDisplayName__)());
          System.out.format("Description: %s\n", modelResponse.[getDescription](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDescription__)());
    
          System.out.format("Metadata Schema Uri: %s\n", modelResponse.[getMetadataSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getMetadataSchemaUri__)());
          System.out.format("Metadata: %s\n", modelResponse.[getMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getMetadata__)());
          System.out.format("Training Pipeline: %s\n", modelResponse.[getTrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getTrainingPipeline__)());
          System.out.format("Artifact Uri: %s\n", modelResponse.[getArtifactUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getArtifactUri__)());
    
          System.out.format(
              "Supported Deployment Resources Types: %s\n",
              modelResponse.[getSupportedDeploymentResourcesTypesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedDeploymentResourcesTypesList__)());
          System.out.format(
              "Supported Input Storage Formats: %s\n",
              modelResponse.[getSupportedInputStorageFormatsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedInputStorageFormatsList__)());
          System.out.format(
              "Supported Output Storage Formats: %s\n",
              modelResponse.[getSupportedOutputStorageFormatsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedOutputStorageFormatsList__)());
    
          System.out.format("Create Time: %s\n", modelResponse.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getCreateTime__)());
          System.out.format("Update Time: %s\n", modelResponse.[getUpdateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getUpdateTime__)());
          System.out.format("Labels: %sn\n", modelResponse.[getLabelsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getLabelsMap__)());
    
          [PredictSchemata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html) predictSchemata = modelResponse.[getPredictSchemata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getPredictSchemata__)();
          System.out.println("Predict Schemata");
          System.out.format("Instance Schema Uri: %s\n", predictSchemata.[getInstanceSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getInstanceSchemaUri__)());
          System.out.format("Parameters Schema Uri: %s\n", predictSchemata.[getParametersSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getParametersSchemaUri__)());
          System.out.format("Prediction Schema Uri: %s\n", predictSchemata.[getPredictionSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getPredictionSchemaUri__)());
    
          for ([ExportFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.ExportFormat.html) exportFormat : modelResponse.[getSupportedExportFormatsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedExportFormatsList__)()) {
            System.out.println("Supported Export Format");
            System.out.format("Id: %s\n", exportFormat.getId());
          }
    
          [ModelContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html) modelContainerSpec = modelResponse.[getContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getContainerSpec__)();
          System.out.println("Container Spec");
          System.out.format("Image Uri: %s\n", modelContainerSpec.[getImageUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getImageUri__)());
          System.out.format("Command: %s\n", modelContainerSpec.[getCommandList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getCommandList__)());
          System.out.format("Args: %s\n", modelContainerSpec.[getArgsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getArgsList__)());
          System.out.format("Predict Route: %s\n", modelContainerSpec.[getPredictRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getPredictRoute__)());
          System.out.format("Health Route: %s\n", modelContainerSpec.[getHealthRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getHealthRoute__)());
    
          for ([EnvVar](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EnvVar.html) envVar : modelContainerSpec.[getEnvList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getEnvList__)()) {
            System.out.println("Env");
            System.out.format("Name: %s\n", envVar.getName());
            System.out.format("Value: %s\n", envVar.getValue());
          }
    
          for ([Port](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Port.html) port : modelContainerSpec.[getPortsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getPortsList__)()) {
            System.out.println("Port");
            System.out.format("Container Port: %s\n", port.getContainerPort());
          }
    
          for ([DeployedModelRef](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModelRef.html) deployedModelRef : modelResponse.[getDeployedModelsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDeployedModelsList__)()) {
            System.out.println("Deployed Model");
            System.out.format("Endpoint: %s\n", deployedModelRef.getEndpoint());
            System.out.format("Deployed Model Id: %s\n", deployedModelRef.getDeployedModelId());
          }
    
          [Status](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html) status = trainingPipelineResponse.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getError__)();
          System.out.println("Error");
          System.out.format("Code: %s\n", status.[getCode](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html#com_google_rpc_Status_getCode__)());
          System.out.format("Message: %s\n", status.[getMessage](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html#com_google_rpc_Status_getMessage__)());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value
    
    
    def create_training_pipeline_sample(
        project: str,
        display_name: str,
        training_task_definition: str,
        dataset_id: str,
        model_display_name: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[PipelineServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.pipeline_service.PipelineServiceClient.html)(client_options=client_options)
        training_task_inputs_dict = {
            "multiLabel": True,
            "modelType": "CLOUD",
            "budgetMilliNodeHours": 8000,
            "disableEarlyStopping": False,
        }
        training_task_inputs = json_format.ParseDict(training_task_inputs_dict, Value())
    
        training_pipeline = {
            "display_name": display_name,
            "training_task_definition": training_task_definition,
            "training_task_inputs": training_task_inputs,
            "input_data_config": {"dataset_id": dataset_id},
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
