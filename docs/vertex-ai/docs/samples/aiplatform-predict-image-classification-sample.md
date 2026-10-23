---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-predict-image-classification-sample/
title: Predict for image classification \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:26:59.359890+00:00
---

# Predict for image classification  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-predict-image-classification-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Predict for image classification Stay organized with collections  Save and categorize content based on your preferences. 

Gets prediction for image classification using the predict method.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.util.[ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html);
    import com.google.cloud.aiplatform.v1.[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html);
    import com.google.cloud.aiplatform.v1.[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html);
    import com.google.cloud.aiplatform.v1.schema.predict.[instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).[ImageClassificationPredictionInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.instance.ImageClassificationPredictionInstance.html);
    import com.google.cloud.aiplatform.v1.schema.predict.params.[ImageClassificationPredictionParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.params.ImageClassificationPredictionParams.html);
    import com.google.cloud.aiplatform.v1.schema.predict.prediction.[ClassificationPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.ClassificationPredictionResult.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    import java.util.ArrayList;
    import java.util.Base64;
    import java.util.List;
    
    public class PredictImageClassificationSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String fileName = "YOUR_IMAGE_FILE_PATH";
        String endpointId = "YOUR_ENDPOINT_ID";
        predictImageClassification(project, fileName, endpointId);
      }
    
      static void predictImageClassification(String project, String fileName, String endpointId)
          throws IOException {
        [PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html) settings =
            [PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html) predictionServiceClient =
            [PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html).create(settings)) {
          String location = "us-central1";
          [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html) endpointName = [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html).of(project, location, endpointId);
    
          byte[] contents = Base64.getEncoder().encode(Files.readAllBytes(Paths.get(fileName)));
          String content = new String(contents, StandardCharsets.UTF_8);
    
          [ImageClassificationPredictionInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.instance.ImageClassificationPredictionInstance.html) predictionInstance =
              [ImageClassificationPredictionInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.instance.ImageClassificationPredictionInstance.html).newBuilder().setContent(content).build();
    
          [List<Value>](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html) instances = new ArrayList<>();
          instances.add([ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html).[toValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html#com_google_cloud_aiplatform_util_ValueConverter_toValue_com_google_protobuf_Message_)(predictionInstance));
    
          [ImageClassificationPredictionParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.params.ImageClassificationPredictionParams.html) predictionParams =
              [ImageClassificationPredictionParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.params.ImageClassificationPredictionParams.html).newBuilder()
                  .setConfidenceThreshold((float) 0.5)
                  .setMaxPredictions(5)
                  .build();
    
          [PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html) predictResponse =
              predictionServiceClient.predict(
                  endpointName, instances, [ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html).[toValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html#com_google_cloud_aiplatform_util_ValueConverter_toValue_com_google_protobuf_Message_)(predictionParams));
          System.out.println("Predict Image Classification Response");
          System.out.format("\tDeployed Model Id: %s\n", predictResponse.[getDeployedModelId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html#com_google_cloud_aiplatform_v1_PredictResponse_getDeployedModelId__)());
    
          System.out.println("Predictions");
          for ([Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html) prediction : predictResponse.[getPredictionsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html#com_google_cloud_aiplatform_v1_PredictResponse_getPredictionsList__)()) {
    
            [ClassificationPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.ClassificationPredictionResult.html).Builder resultBuilder =
                [ClassificationPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.ClassificationPredictionResult.html).newBuilder();
            // Display names and confidences values correspond to
            // IDs in the ID list.
            [ClassificationPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.ClassificationPredictionResult.html) result =
                ([ClassificationPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.ClassificationPredictionResult.html)) [ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html).fromValue(resultBuilder, prediction);
            int counter = 0;
            for (Long id : result.[getIdsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.ClassificationPredictionResult.html#com_google_cloud_aiplatform_v1_schema_predict_prediction_ClassificationPredictionResult_getIdsList__)()) {
              System.out.printf("Label ID: %d\n", id);
              System.out.printf("Label: %s\n", result.[getDisplayNames](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.ClassificationPredictionResult.html#com_google_cloud_aiplatform_v1_schema_predict_prediction_ClassificationPredictionResult_getDisplayNames_int_)(counter));
              System.out.printf("Confidence: %.4f\n", result.[getConfidences](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.ClassificationPredictionResult.html#com_google_cloud_aiplatform_v1_schema_predict_prediction_ClassificationPredictionResult_getConfidences_int_)(counter));
              counter++;
            }
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.\
     * (Not necessary if passing values as arguments)
     */
    
    // const filename = "YOUR_PREDICTION_FILE_NAME";
    // const endpointId = "YOUR_ENDPOINT_ID";
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    const aiplatform = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    const {instance, params, prediction} =
      aiplatform.protos.google.cloud.aiplatform.v1.schema.predict;
    
    // Imports the Google Cloud Prediction Service Client library
    const {PredictionServiceClient} = aiplatform.v1;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const predictionServiceClient = new [PredictionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function predictImageClassification() {
      // Configure the endpoint resource
      const endpoint = `projects/${project}/locations/${location}/endpoints/${endpointId}`;
    
      const parametersObj = new params.ImageClassificationPredictionParams({
        confidenceThreshold: 0.5,
        maxPredictions: 5,
      });
      const parameters = parametersObj.toValue();
    
      const fs = require('fs');
      const image = fs.readFileSync(filename, 'base64');
      const instanceObj = new instance.ImageClassificationPredictionInstance({
        content: image,
      });
      const instanceValue = instanceObj.toValue();
    
      const instances = [instanceValue];
      const request = {
        endpoint,
        instances,
        parameters,
      };
    
      // Predict request
      const [response] = await predictionServiceClient.predict(request);
    
      console.log('Predict image classification response');
      console.log(`\tDeployed model id : ${response.deployedModelId}`);
      const predictions = response.predictions;
      console.log('\tPredictions :');
      for (const predictionValue of predictions) {
        const predictionResultObj =
          prediction.ClassificationPredictionResult.fromValue(predictionValue);
        for (const [i, label] of predictionResultObj.displayNames.entries()) {
          console.log(`\tDisplay name: ${label}`);
          console.log(`\tConfidences: ${predictionResultObj.confidences[i]}`);
          console.log(`\tIDs: ${predictionResultObj.ids[i]}\n\n`);
        }
      }
    }
    predictImageClassification();

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    
    from google.cloud import aiplatform
    from google.cloud.aiplatform.gapic.schema import predict
    
    
    def predict_image_classification_sample(
        project: str,
        endpoint_id: str,
        filename: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[PredictionServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.prediction_service.PredictionServiceClient.html)(client_options=client_options)
        with open(filename, "rb") as f:
            file_content = f.read()
    
        # The format of each instance should conform to the deployed model's prediction input schema.
        encoded_content = base64.b64encode(file_content).decode("utf-8")
        instance = predict.instance.[ImageClassificationPredictionInstance](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.v1.schema.predict.instance_v1.types.ImageClassificationPredictionInstance.html)(
            content=encoded_content,
        ).to_value()
        instances = [instance]
        # See gs://google-cloud-aiplatform/schema/predict/params/image_classification_1.0.0.yaml for the format of the parameters.
        parameters = predict.params.[ImageClassificationPredictionParams](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.v1.schema.predict.params_v1.types.ImageClassificationPredictionParams.html)(
            confidence_threshold=0.5,
            max_predictions=5,
        ).to_value()
        endpoint = client.[endpoint_path](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.prediction_service.PredictionServiceClient.html#google_cloud_aiplatform_v1_services_prediction_service_PredictionServiceClient_endpoint_path)(
            project=project, location=location, endpoint=endpoint_id
        )
        response = client.[predict](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.prediction_service.PredictionServiceClient.html)(
            endpoint=endpoint, instances=instances, parameters=parameters
        )
        print("response")
        print(" deployed_model_id:", response.deployed_model_id)
        # See gs://google-cloud-aiplatform/schema/predict/prediction/image_classification_1.0.0.yaml for the format of the predictions.
        predictions = response.predictions
        for prediction in predictions:
            print(" prediction:", dict(prediction))
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
