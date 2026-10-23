---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-predict-tabular-regression-sample/
title: Predict for tabular regression \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:41.841551+00:00
---

# Predict for tabular regression  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-predict-tabular-regression-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Predict for tabular regression Stay organized with collections  Save and categorize content based on your preferences. 

Gets prediction for tabular regression using the predict method.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get online inferences and explanations](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/e2e-automl-online-predictions)
  * [Get online inferences for AutoML models](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/classification-regression/get-online-predictions)
  * [Get TabNet online inferences](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/tabnet-online-predictions)
  * [Get Wide & Deep online inferences](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/wide-and-deep-online-predictions)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.util.[ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html);
    import com.google.cloud.aiplatform.v1.[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html);
    import com.google.cloud.aiplatform.v1.[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html);
    import com.google.cloud.aiplatform.v1.schema.predict.prediction.[TabularRegressionPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html);
    import com.google.protobuf.[ListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.IOException;
    import java.util.List;
    
    public class PredictTabularRegressionSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String instance = "[{ “feature_column_a”: “value”, “feature_column_b”: “value”}]";
        String endpointId = "YOUR_ENDPOINT_ID";
        predictTabularRegression(instance, project, endpointId);
      }
    
      static void predictTabularRegression(String instance, String project, String endpointId)
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
    
          Value parameters[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html)lue.newBuilder[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html)tListValue(listValue).build();
          PredictResponse [PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html) =
              predictionServiceClient.predict(endpointName, instanceList, parameters);
          System.out.println("Predict Tabular Regression Response");
          System.out.format("\tDisplay Model Id: %s\n", predictResponse.predictResponse.[getDeployedModelId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html#com_google_cloud_aiplatform_v1_PredictResponse_getDeployedModelId__)().out.println("Predictions");
          for (Value prediction[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html)edictResponse.predictResponse.[getPredictionsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html#com_google_cloud_aiplatform_v1_PredictResponse_getPredictionsList__)()larRegressio[TabularRegressionPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html)uilder =
                TabularRegressio[TabularRegressionPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html)        TabularRegressio[TabularRegressionPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html)      (TabularRegressio[TabularRegressionPredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html).f[ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html)tBuilder, prediction);
    
            System.out.printf("\tUpper bound: %f\n", result.getUpperBresult.[getUpperBound](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html#com_google_cloud_aiplatform_v1_schema_predict_prediction_TabularRegressionPredictionResult_getUpperBound__)()m.out.printf("\tLower bound: %f\n", result.getLowerBresult.[getLowerBound](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html#com_google_cloud_aiplatform_v1_schema_predict_prediction_TabularRegressionPredictionResult_getLowerBound__)()m.out.printf("\tValue: %f\n", result.getValue(result.[getValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.predict.prediction.TabularRegressionPredictionResult.html#com_google_cloud_aiplatform_v1_schema_predict_prediction_TabularRegressionPredictionResult_getValue__)()
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.\
     * (Not necessary if passing values as arguments)
     */
    
    // const endpointId = 'YOUR_ENDPOINT_ID';
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    const aiplatform = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    const {prediction} =
      aiplatform.protos.google.cloud.aiplatform.v1.schema.predict;
    
    // Imports the Google Cloud Prediction service client
    const {PredictionServiceClient} = aiplatform.v1;
    
    // Import the helper module for converting arbitrary protobuf.Value objects.
    const {helpers} = aiplatform;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const predictionServiceClient = new [PredictionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function predictTablesRegression() {
      // Configure the endpoint resource
      const endpoint = `projects/${project}/locations/${location}/endpoints/${endpointId}`;
      const parameters = [helpers](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html).toValue({});
    
      // TODO (erschmid): Make this less painful
      const instance = [helpers](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html).toValue({
        BOOLEAN_2unique_NULLABLE: false,
        DATETIME_1unique_NULLABLE: '2019-01-01 00:00:00',
        DATE_1unique_NULLABLE: '2019-01-01',
        FLOAT_5000unique_NULLABLE: 1611,
        FLOAT_5000unique_REPEATED: [2320, 1192],
        INTEGER_5000unique_NULLABLE: '8',
        NUMERIC_5000unique_NULLABLE: 16,
        STRING_5000unique_NULLABLE: 'str-2',
        STRUCT_NULLABLE: {
          BOOLEAN_2unique_NULLABLE: false,
          DATE_1unique_NULLABLE: '2019-01-01',
          DATETIME_1unique_NULLABLE: '2019-01-01 00:00:00',
          FLOAT_5000unique_NULLABLE: 1308,
          FLOAT_5000unique_REPEATED: [2323, 1178],
          FLOAT_5000unique_REQUIRED: 3089,
          INTEGER_5000unique_NULLABLE: '1777',
          NUMERIC_5000unique_NULLABLE: 3323,
          TIME_1unique_NULLABLE: '23:59:59.999999',
          STRING_5000unique_NULLABLE: 'str-49',
          TIMESTAMP_1unique_NULLABLE: '1546387199999999',
        },
        TIMESTAMP_1unique_NULLABLE: '1546387199999999',
        TIME_1unique_NULLABLE: '23:59:59.999999',
      });
    
      const instances = [instance];
      const request = {
        endpoint,
        instances,
        parameters,
      };
    
      // Predict request
      const [response] = await predictionServiceClient.predict(request);
    
      console.log('Predict tabular regression response');
      console.log(`\tDeployed model id : ${response.deployedModelId}`);
      const predictions = response.predictions;
      console.log('\tPredictions :');
      for (const predictionResultVal of predictions) {
        const predictionResultObj =
          prediction.TabularRegressionPredictionResult.fromValue(
            predictionResultVal
          );
        console.log(`\tUpper bound: ${predictionResultObj.upper_bound}`);
        console.log(`\tLower bound: ${predictionResultObj.lower_bound}`);
        console.log(`\tLower bound: ${predictionResultObj.value}`);
      }
    }
    predictTablesRegression();

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Dict
    
    from google.cloud import aiplatform
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value
    
    
    def predict_tabular_regression_sample(
        project: str,
        endpoint_id: str,
        instance_dict: Dict,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[PredictionServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.prediction_service.PredictionServiceClient.html)(client_options=client_options)
        # for more info on the instance schema, please use get_model_sample.py
        # and look at the yaml found in instance_schema_uri
        instance = json_format.ParseDict(instance_dict, Value())
        instances = [instance]
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
        # See gs://google-cloud-aiplatform/schema/predict/prediction/tabular_regression_1.0.0.yaml for the format of the predictions.
        predictions = response.predictions
        for prediction in predictions:
            print(" prediction:", dict(prediction))
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
