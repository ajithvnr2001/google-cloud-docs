---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/object-detection/train-model/
title: Train an image object detection model \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:44:40.824124+00:00
---

# Train an image object detection model  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/object-detection/train-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Train an image object detection model Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to train an AutoML object detection model from an image dataset using either the Google Cloud console or the Agent Platform API.

**Note:** AutoML Edge object detection is in maintenance mode. Only severe failures will be addressed. We recommend migrating to alternative solutions such as open source (OSS) models.

## Train an AutoML model

###  Google Cloud console 

  1. In the Google Cloud console, in the Agent Platform section, go to the **Datasets** page.

[Go to the Datasets page](https://console.cloud.google.com/agent-platform/datasets)

  2. Click the name of the dataset you want to use to train your model to open its details page.

  3. Click **Train new model**.

  4. For the training method, select radio_button_checked**AutoML**.

  5. In the **Choose where to use the model** section, choose the model host location: radio_button_checked**Cloud** , radio_button_checked**Edge** , or radio_button_checked**Agent Platform Vision**.

  6. Click **Continue**.

  7. Enter a name for the model.

  8. If you want manually set how your training data is split, expand **Advanced options** and select a data split option. For more information, see [About data splits for AutoML models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/ml-use). 

  9. Click **Start Training**. 

Model training can take many hours, depending on the size and complexity of your data and your training budget, if you specified one. You can close this tab and return to it later. You will receive an email when your model has completed training.




###  API 

Select the tab below for your language or environment:

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: Region where dataset is located and Model is created. For example, `us-central1`.
  * PROJECT: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * TRAININGPIPELINE_DISPLAYNAME: Required. A display name for the trainingPipeline. 
  * DATASET_ID: The ID number for the dataset to use for training.
  * `fractionSplit`: Optional. One of several possible ML use [split options](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines#inputdataconfig) for your data. For `fractionSplit`, values must sum to 1. For example: 
    * `{"trainingFraction": "0.7","validationFraction": "0.15","testFraction": "0.15"}`
  * MODEL_DISPLAYNAME*: A display name for the model uploaded (created) by the TrainingPipeline.
  * MODEL_DESCRIPTION*: A description for the model.
  * modelToUpload.labels*: Any set of key-value pairs to organize your models. For example: 
    * "env": "prod"
    * "tier": "backend"
  * MODELTYPE†: The type of Cloud-hosted model to train. The options are: 
    * `CLOUD_1` \- A model best tailored to be used within Google Cloud, and which _cannot_ be exported. Compared to the CLOUD_HIGH_ACCURACY_1 and CLOUD_LOW_LATENCY_1 models above, it is expected to have higher prediction quality and lower latency.
    * `CLOUD_HIGH_ACCURACY_1` \- A model best tailored to be used within Google Cloud, and which _cannot_ be exported. This model is expected to have a higher latency, but should also have a higher prediction quality than other cloud models.
    * `CLOUD_LOW_LATENCY_1` \- A model best tailored to be used within Google Cloud, and which cannot be exported. This model is expected to have a low latency, but may have lower prediction quality than other cloud models.
Other model type options can be found in the [reference documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.cloud.aiplatform.v1/schema/trainingjob.definition#modeltype_1). 
  * NODE_HOUR_BUDGET†: The actual training cost will be equal or less than this value. For Cloud models the budget must be: 20,000 - 900,000 milli node hours (inclusive). The default value is 216,000 which represents one day in wall time, assuming 9 nodes are used. 
  * PROJECT_NUMBER: Your project's automatically generated [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers)

* | Schema file's description you specify in `trainingTaskDefinition` describes the use of this field.  
---|---  
† | Schema file you specify in `trainingTaskDefinition` declares and describes this field.  
  
HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines

Request JSON body: 
    
    
    {
      "displayName": "TRAININGPIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": "DECIMAL",
          "validationFraction": "DECIMAL",
          "testFraction": "DECIMAL"
        }
      },
      "modelToUpload": {
        "displayName": "MODEL_DISPLAYNAME",
        "description": "MODEL_DESCRIPTION",
        "labels": {
          "KEY": "VALUE"
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_object_detection_1.0.0.yaml",
      "trainingTaskInputs": {
        "modelType": ["MODELTYPE"],
        "budgetMilliNodeHours": NODE_HOUR_BUDGET
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines" | Select-Object -Expand Content

The response contains information about specifications as well as the TRAININGPIPELINE_ID. 

#### Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/trainingPipelines/TRAININGPIPELINE_ID",
      "displayName": "TRAININGPIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": 0.7,
          "validationFraction": 0.15,
          "testFraction": 0.15
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_object_detection_1.0.0.yaml",
      "trainingTaskInputs": {
        "modelType": "MODELTYPE",
        "budgetMilliNodeHours": "NODE_HOUR_BUDGET"
      },
      "modelToUpload": {
        "displayName": "MODEL_DISPLAYNAME",
        "labels": {
          "KEY1": "VALUE1",
          "KEY2": "VALUE2"
        }
      },
      "state": "PIPELINE_STATE_PENDING",
      "createTime": "2020-07-14T17:16:55.098953Z",
      "updateTime": "2020-07-14T17:16:55.098953Z"
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). For more information, see the [Agent Platform Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.util.[ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html);
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
    import com.google.cloud.aiplatform.v1.schema.trainingjob.definition.[AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageObjectDetectionInputs.html);
    import com.google.cloud.aiplatform.v1.schema.trainingjob.definition.[AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageObjectDetectionInputs.html).ModelType;
    import com.google.rpc.[Status](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html);
    import java.io.IOException;
    
    public class CreateTrainingPipelineImageObjectDetectionSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String trainingPipelineDisplayName = "YOUR_TRAINING_PIPELINE_DISPLAY_NAME";
        String project = "YOUR_PROJECT_ID";
        String datasetId = "YOUR_DATASET_ID";
        String modelDisplayName = "YOUR_MODEL_DISPLAY_NAME";
        createTrainingPipelineImageObjectDetectionSample(
            project, trainingPipelineDisplayName, datasetId, modelDisplayName);
      }
    
      static void createTrainingPipelineImageObjectDetectionSample(
          String project, String trainingPipelineDisplayName, String datasetId, String modelDisplayName)
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
          String trainingTaskDefinition =
              "gs://google-cloud-aiplatform/schema/trainingjob/definition/"
                  + "automl_image_object_detection_1.0.0.yaml";
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html) locationName = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location);
    
          [AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageObjectDetectionInputs.html) autoMlImageObjectDetectionInputs =
              [AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageObjectDetectionInputs.html).newBuilder()
                  .setModelType(ModelType.CLOUD_HIGH_ACCURACY_1)
                  .setBudgetMilliNodeHours(20000)
                  .setDisableEarlyStopping(false)
                  .build();
    
          [InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html) trainingInputDataConfig =
              [InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html).newBuilder().[setDatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.Builder.html#com_google_cloud_aiplatform_v1_InputDataConfig_Builder_setDatasetId_java_lang_String_)(datasetId).build();
          [Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html) model = [Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html).newBuilder().setDisplayName(modelDisplayName).build();
          [TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html) trainingPipeline =
              [TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html).newBuilder()
                  .setDisplayName(trainingPipelineDisplayName)
                  .[setTrainingTaskDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setTrainingTaskDefinition_java_lang_String_)(trainingTaskDefinition)
                  .[setTrainingTaskInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setTrainingTaskInputs_com_google_protobuf_Value_)([ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html).[toValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html#com_google_cloud_aiplatform_util_ValueConverter_toValue_com_google_protobuf_Message_)(autoMlImageObjectDetectionInputs))
                  .[setInputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setInputDataConfig_com_google_cloud_aiplatform_v1_InputDataConfig_)(trainingInputDataConfig)
                  .[setModelToUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setModelToUpload_com_google_cloud_aiplatform_v1_Model_)(model)
                  .build();
    
          [TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html) trainingPipelineResponse =
              pipelineServiceClient.createTrainingPipeline(locationName, trainingPipeline);
    
          System.out.println("Create Training Pipeline Image Object Detection Response");
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

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). For more information, see the [Agent Platform Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.\
     * (Not necessary if passing values as arguments)
     */
    
    // const datasetId = 'YOUR_DATASET_ID';
    // const modelDisplayName = 'YOUR_MODEL_DISPLAY_NAME';
    // const trainingPipelineDisplayName = 'YOUR_TRAINING_PIPELINE_DISPLAY_NAME';
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    
    const aiplatform = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    const {definition} =
      aiplatform.protos.google.cloud.aiplatform.v1.schema.trainingjob;
    const ModelType = definition.AutoMlImageObjectDetectionInputs.ModelType;
    
    // Imports the Google Cloud Pipeline Service Client library
    const {PipelineServiceClient} = aiplatform.v1;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const pipelineServiceClient = new [PipelineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function createTrainingPipelineImageObjectDetection() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}`;
    
      const trainingTaskInputsObj =
        new definition.AutoMlImageObjectDetectionInputs({
          disableEarlyStopping: false,
          modelType: ModelType.CLOUD_1,
          budgetMilliNodeHours: 20000,
        });
    
      const trainingTaskInputs = trainingTaskInputsObj.toValue();
      const modelToUpload = {displayName: modelDisplayName};
      const inputDataConfig = {datasetId: datasetId};
      const trainingPipeline = {
        displayName: trainingPipelineDisplayName,
        trainingTaskDefinition:
          'gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_object_detection_1.0.0.yaml',
        trainingTaskInputs,
        inputDataConfig,
        modelToUpload,
      };
      const request = {
        parent,
        trainingPipeline,
      };
    
      // Create training pipeline request
      const [response] =
        await pipelineServiceClient.createTrainingPipeline(request);
    
      console.log('Create training pipeline image object detection response');
      console.log(`Name : ${response.name}`);
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    createTrainingPipelineImageObjectDetection();

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    from google.cloud import aiplatform
    from google.cloud.aiplatform.gapic.schema import trainingjob
    
    
    def create_training_pipeline_image_object_detection_sample(
        project: str,
        display_name: str,
        dataset_id: str,
        model_display_name: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.PipelineServiceClient(client_options=client_options)
        training_task_inputs = trainingjob.definition.AutoMlImageObjectDetectionInputs(
            model_type="CLOUD_HIGH_ACCURACY_1",
            budget_milli_node_hours=20000,
            disable_early_stopping=False,
        ).to_value()
    
        training_pipeline = {
            "display_name": display_name,
            "training_task_definition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_object_detection_1.0.0.yaml",
            "training_task_inputs": training_task_inputs,
            "input_data_config": {"dataset_id": dataset_id},
            "model_to_upload": {"display_name": model_display_name},
        }
        parent = f"projects/{project}/locations/{location}"
        response = client.create_training_pipeline(
            parent=parent, training_pipeline=training_pipeline
        )
        print("response:", response)
    
    

## Control the data split using REST

You can control how your training data is split between the training, validation, and test sets. When using the Agent Platform API, use the [`Split` object](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines#InputDataConfig) to determine your data split. The `Split` object can be included in the `InputConfig` object as one of several object types, each of which provides a different way to split the training data. You can select one method only.

  * `FractionSplit`: 
    * TRAINING_FRACTION: The fraction of the training data to be used for the training set. 
    * VALIDATION_FRACTION: The fraction of the training data to be used for the validation set. Not used for video data. 
    * TEST_FRACTION: The fraction of the training data to be used for the test set. 

If any of the fractions are specified, all must be specified. The fractions must add up to 1.0. The [default values for the fractions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/ml-use#default) differ depending on your data type. [Learn more](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/ml-use#percentages). 
    
    "fractionSplit": {
      "trainingFraction": TRAINING_FRACTION,
      "validationFraction": VALIDATION_FRACTION,
      "testFraction": TEST_FRACTION
    },
    

  * `FilterSplit`: 
    * TRAINING_FILTER: Data items that match this filter are used for the training set. 
    * VALIDATION_FILTER: Data items that match this filter are used for the validation set. Must be "-" for video data. 
    * TEST_FILTER: Data items that match this filter are used for the test set. 



These filters can be used with the `ml_use` label, or with any labels you apply to your data. Learn more about using [the ml-use label](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/ml-use#ml-use) and [other labels](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/ml-use#filter) to filter your data. 

The following example shows how to use the `filterSplit` object with the `ml_use` label, with the validation set included: 
    
    
    "filterSplit": {
    "trainingFilter": "labels.aiplatform.googleapis.com/ml_use=training",
    "validationFilter": "labels.aiplatform.googleapis.com/ml_use=validation",
    "testFilter": "labels.aiplatform.googleapis.com/ml_use=test"
    }
    

[ Previous arrow_back  Create dataset  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/object-detection/create-dataset)

[ Next Evaluate model  arrow_forward  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/object-detection/evaluate-model)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
