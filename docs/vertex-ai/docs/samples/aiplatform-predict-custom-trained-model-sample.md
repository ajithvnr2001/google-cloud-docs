---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-predict-custom-trained-model-sample/
title: Predict for custom trained model \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:26:59.260692+00:00
---

# Predict for custom trained model  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-predict-custom-trained-model-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Predict for custom trained model Stay organized with collections  Save and categorize content based on your preferences. 

Gets prediction for custom trained model using the predict method.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get online inferences from a custom trained model](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-online-predictions)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html);
    import com.google.cloud.aiplatform.v1.[PredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequest.html);
    import com.google.cloud.aiplatform.v1.[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html);
    import com.google.protobuf.[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.IOException;
    import java.util.List;
    
    public class PredictCustomTrainedModelSample {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String instance = "[{ “feature_column_a”: “value”, “feature_column_b”: “value”}]";
        String project = "YOUR_PROJECT_ID";
        String endpointId = "YOUR_ENDPOINT_ID";
        predictCustomTrainedModel(project, endpointId, instance);
      }
    
      static void predictCustomTrainedModel(String project, String endpointId, String instance)
          throws IOException {
        PredictionServic[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html)ceSettings =
            PredictionServic[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html)          .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (PredictionServic[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html)ceClient =
            PredictionServic[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html)onServiceSettings)) {
          String location = "us-central1";
          EndpointName end[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html)EndpointName.of([EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html)ation, endpointId);
    
          ListValue.Builde[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html)ue = ListValue.newBui[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html)     JsonFormat.parse[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html)instance, listValue);
          List<Value> instan[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html)listValue.getValuesList();
    
          PredictRequest p[PredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequest.html)=
              PredictRequest.n[PredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequest.html)            .setEndpoint(endpointName.toSendpointName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html#com_google_cloud_aiplatform_v1_EndpointName_toString__)().addAllInstances(instanceList)
                  .build();
          PredictResponse [PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html) = predictionServiceClient.predict(predictRequest);
    
          System.out.println("Predict Custom Trained model Response");
          System.out.format("\tDeployed Model Id: %s\n", predictResponse.predictResponse.[getDeployedModelId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html#com_google_cloud_aiplatform_v1_PredictResponse_getDeployedModelId__)()out.println("Predictions");
          for (Value prediction[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)edictResponse.predictResponse.[getPredictionsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html#com_google_cloud_aiplatform_v1_PredictResponse_getPredictionsList__)()em.out.format("\tPrediction: %s\n", prediction);
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
    const util = require('util');
    const {readFile} = require('fs');
    const readFileAsync = util.promisify(readFile);
    
    // Imports the Google Cloud Prediction Service Client library
    const {PredictionServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const predictionServiceClient = new [PredictionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function predictCustomTrainedModel() {
      // Configure the parent resource
      const endpoint = `projects/${project}/locations/${location}/endpoints/${endpointId}`;
      const parameters = {
        structValue: {
          fields: {},
        },
      };
      const instanceDict = await readFileAsync(filename, 'utf8');
      const instanceValue = JSON.parse(instanceDict);
      const instance = {
        structValue: {
          fields: {
            Age: {stringValue: instanceValue['Age']},
            Balance: {stringValue: instanceValue['Balance']},
            Campaign: {stringValue: instanceValue['Campaign']},
            Contact: {stringValue: instanceValue['Contact']},
            Day: {stringValue: instanceValue['Day']},
            Default: {stringValue: instanceValue['Default']},
            Deposit: {stringValue: instanceValue['Deposit']},
            Duration: {stringValue: instanceValue['[Duration](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.duration.html)']},
            Housing: {stringValue: instanceValue['Housing']},
            Job: {stringValue: instanceValue['Job']},
            Loan: {stringValue: instanceValue['Loan']},
            MaritalStatus: {stringValue: instanceValue['MaritalStatus']},
            Month: {stringValue: instanceValue['Month']},
            PDays: {stringValue: instanceValue['PDays']},
            POutcome: {stringValue: instanceValue['POutcome']},
            Previous: {stringValue: instanceValue['Previous']},
          },
        },
      };
    
      const instances = [instance];
      const request = {
        endpoint,
        instances,
        parameters,
      };
    
      // Predict request
      const [response] = await predictionServiceClient.predict(request);
    
      console.log('Predict custom trained model response');
      console.log(`\tDeployed model id : ${response.deployedModelId}`);
      const predictions = response.predictions;
      console.log('\tPredictions :');
      for (const prediction of predictions) {
        console.log(`\t\tPrediction : ${JSON.stringify(prediction)}`);
      }
    }
    predictCustomTrainedModel();

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Dict, List, Union
    
    from google.cloud import aiplatform
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value
    
    
    def predict_custom_trained_model_sample(
        project: str,
        endpoint_id: str,
        instances: Union[Dict, List[Dict]],
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        """
        `instances` can be either single instance of type dict or a list
        of instances.
        """
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[PredictionServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.prediction_service.PredictionServiceClient.html)(client_options=client_options)
        # The format of each instance should conform to the deployed model's prediction input schema.
        instances = instances if isinstance(instances, list) else [instances]
        instances = [
            json_format.ParseDict(instance_dict, Value()) for instance_dict in instances
        ]
        parameters_dict = {}
        parameters = json_format.ParseDict(parameters_dict, Value())
        endpoint = client.[endpoint_path](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.prediction_service.PredictionServiceClient.html#google_cloud_aiplatform_v1_services_prediction_service_PredictionServiceClient_endpoint_path)(
            project=project, location=location, endpoint=endpoint_id
        )
        response = client.[predict](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.prediction_service.PredictionServiceClient.html)(
            endpoint=endpoint, instances=instances, parameters=parameters
        )
        print("response")
        print(" deployed_model_id:", response.deployed_model_id)
        # The predictions are a google.protobuf.Value representation of the model's predictions.
        predictions = response.predictions
        for prediction in predictions:
            print(" prediction:", prediction)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
