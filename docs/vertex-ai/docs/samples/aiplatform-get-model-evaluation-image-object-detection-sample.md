---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-get-model-evaluation-image-object-detection-sample/
title: Get a model evaluation for image object detection \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:27:00.419147+00:00
---

# Get a model evaluation for image object detection  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-get-model-evaluation-image-object-detection-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Get a model evaluation for image object detection Stay organized with collections  Save and categorize content based on your preferences. 

Gets a model evaluation for image object detection using the get_model_evaluation method.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Evaluate and iterate AutoML image object detection models](https://docs.cloud.google.com/vertex-ai/docs/image-data/object-detection/evaluate-model)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation.html);
    import com.google.cloud.aiplatform.v1.[ModelEvaluationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationName.html);
    import com.google.cloud.aiplatform.v1.[ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.html);
    import com.google.cloud.aiplatform.v1.[ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceSettings.html);
    import java.io.IOException;
    
    public class GetModelEvaluationImageObjectDetectionSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // To obtain evaluationId run the code block below after setting modelServiceSettings.
        //
        // try (ModelServiceClient modelServiceClient = ModelServiceClient.create(modelServiceSettings))
        // {
        //   String location = "us-central1";
        //   ModelName modelFullId = ModelName.of(project, location, modelId);
        //   ListModelEvaluationsRequest modelEvaluationsrequest =
        //   ListModelEvaluationsRequest.newBuilder().setParent(modelFullId.toString()).build();
        //   for (ModelEvaluation modelEvaluation :
        //     modelServiceClient.listModelEvaluations(modelEvaluationsrequest).iterateAll()) {
        //       System.out.format("Model Evaluation Name: %s%n", modelEvaluation.getName());
        //   }
        // }
        String project = "YOUR_PROJECT_ID";
        String modelId = "YOUR_MODEL_ID";
        String evaluationId = "YOUR_EVALUATION_ID";
        getModelEvaluationImageObjectDetectionSample(project, modelId, evaluationId);
      }
    
      static void getModelEvaluationImageObjectDetectionSample(
          String project, String modelId, String evaluationId) throws IOException {
        [ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceSettings.html) modelServiceSettings =
            [ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.html) modelServiceClient = [ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.html).create(modelServiceSettings)) {
          String location = "us-central1";
          [ModelEvaluationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationName.html) modelEvaluationName =
              [ModelEvaluationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationName.html).of(project, location, modelId, evaluationId);
    
          [ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation.html) modelEvaluation = modelServiceClient.getModelEvaluation(modelEvaluationName);
    
          System.out.println("Get Model Evaluation Image Object Detection Response");
          System.out.format("\tName: %s\n", modelEvaluation.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation.html#com_google_cloud_aiplatform_v1_ModelEvaluation_getName__)());
          System.out.format("\tMetrics Schema Uri: %s\n", modelEvaluation.[getMetricsSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation.html#com_google_cloud_aiplatform_v1_ModelEvaluation_getMetricsSchemaUri__)());
          System.out.format("\tMetrics: %s\n", modelEvaluation.[getMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation.html#com_google_cloud_aiplatform_v1_ModelEvaluation_getMetrics__)());
          System.out.format("\tCreate Time: %s\n", modelEvaluation.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation.html#com_google_cloud_aiplatform_v1_ModelEvaluation_getCreateTime__)());
          System.out.format("\tSlice Dimensions: %s\n", modelEvaluation.[getSliceDimensionsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation.html#com_google_cloud_aiplatform_v1_ModelEvaluation_getSliceDimensionsList__)());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample
     * (not necessary if passing values as arguments). To obtain evaluationId,
     * instantiate the client and run the following the commands.
     */
    // const parentName = `projects/${project}/locations/${location}/models/${modelId}`;
    // const evalRequest = {
    //   parent: parentName
    // };
    // const [evalResponse] = await modelServiceClient.listModelEvaluations(evalRequest);
    // console.log(evalResponse);
    
    // const modelId = 'YOUR_MODEL_ID';
    // const evaluationId = 'YOUR_EVALUATION_ID';
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    
    // Imports the Google Cloud Model Service Client library
    const {ModelServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const modelServiceClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function getModelEvaluationImageObjectDetection() {
      // Configure the name resources
      const name = `projects/${project}/locations/${location}/models/${modelId}/evaluations/${evaluationId}`;
      const request = {
        name,
      };
    
      // Create get model evaluation request
      const [response] = await modelServiceClient.getModelEvaluation(request);
    
      console.log('Get model evaluation image object detection response');
      console.log(`\tName : ${response.name}`);
      console.log(`\tMetrics schema uri : ${response.metricsSchemaUri}`);
      console.log(`\tCreate time : ${JSON.stringify(response.createTime)}`);
      console.log(`\tSlice dimensions : ${response.sliceDimensions}`);
    
      const modelExplanation = response.modelExplanation;
      console.log('\tModel explanation');
      if (modelExplanation === null) {
        console.log('\t\t{}');
      } else {
        const meanAttributions = modelExplanation.meanAttributions;
        if (meanAttributions === null) {
          console.log('\t\t\t []');
        } else {
          for (const meanAttribution of meanAttributions) {
            console.log('\t\tMean attribution');
            console.log(
              `\t\t\tBaseline output value : \
                ${meanAttribution.baselineOutputValue}`
            );
            console.log(
              `\t\t\tInstance output value : \
                ${meanAttribution.instanceOutputValue}`
            );
            console.log(
              `\t\t\tFeature attributions : \
                ${meanAttribution.featureAttributions}`
            );
            console.log(`\t\t\tOutput index : ${meanAttribution.outputIndex}`);
            console.log(
              `\t\t\tOutput display name : \
                ${meanAttribution.outputDisplayName}`
            );
            console.log(
              `\t\t\tApproximation error : \
                ${meanAttribution.approximationError}`
            );
          }
        }
      }
    }
    getModelEvaluationImageObjectDetection();

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    
    
    def get_model_evaluation_image_object_detection_sample(
        project: str,
        model_id: str,
        evaluation_id: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        """
        To obtain evaluation_id run the following commands where LOCATION
        is the region where the model is stored, PROJECT is the project ID,
        and MODEL_ID is the ID of your model.
    
        model_client = aiplatform.gapic.ModelServiceClient(
            client_options={
                'api_endpoint':'LOCATION-aiplatform.googleapis.com'
                }
            )
        evaluations = model_client.list_model_evaluations(parent='projects/PROJECT/locations/LOCATION/models/MODEL_ID')
        print("evaluations:", evaluations)
        """
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[ModelServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.model_service.ModelServiceClient.html)(client_options=client_options)
        name = client.[model_evaluation_path](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.model_service.ModelServiceClient.html#google_cloud_aiplatform_v1_services_model_service_ModelServiceClient_model_evaluation_path)(
            project=project, location=location, model=model_id, evaluation=evaluation_id
        )
        response = client.[get_model_evaluation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.model_service.ModelServiceClient.html#google_cloud_aiplatform_v1_services_model_service_ModelServiceClient_get_model_evaluation)(name=name)
        print("response:", response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
