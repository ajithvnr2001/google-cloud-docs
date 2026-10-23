---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemma2-predict-tpu/
title: Generate text with Gemma2 model with TPU accelerators \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:50.189348+00:00
---

# Generate text with Gemma2 model with TPU accelerators  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemma2-predict-tpu/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Generate text with Gemma2 model with TPU accelerators Stay organized with collections  Save and categorize content based on your preferences. 

This code sample demonstrates how to run interference on a Gemma2 model deployed to a Vertex AI endpoint with TPU accelerators.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Deploy and inference Gemma using Model Garden and Gemini Enterprise Agent Platform TPU-backed endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/deploy-and-inference-tutorial-tpu)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/aiplatform/apiv1/aiplatformpb"
    
    	"google.golang.org/protobuf/types/known/structpb"
    )
    
    // predictTPU demonstrates how to run interference on a Gemma2 model deployed to a Vertex AI endpoint with TPU accelerators.
    func predictTPU(w io.Writer, client PredictionsClient, projectID, location, endpointID string) error {
    	ctx := context.Background()
    
    	// Note: client can be initialized in the following way:
    	// apiEndpoint := fmt.Sprintf("%s-aiplatform.googleapis.com:443", location)
    	// client, err := aiplatform.NewPredictionClient(ctx, option.WithEndpoint(apiEndpoint))
    	// if err != nil {
    	// 	return fmt.Errorf("unable to create prediction client: %v", err)
    	// }
    	// defer client.Close()
    
    	gemma2Endpoint := fmt.Sprintf("projects/%s/locations/%s/endpoints/%s", projectID, location, endpointID)
    	prompt := "Why is the sky blue?"
    	parameters := map[string]interface{}{
    		"temperature":     0.9,
    		"maxOutputTokens": 1024,
    		"topP":            1.0,
    		"topK":            1,
    	}
    
    	// Encapsulate the prompt in a correct format for TPUs.
    	// Example format: [{'prompt': 'Why is the sky blue?', 'temperature': 0.9}]
    	promptValue, err := structpb.NewValue(map[string]interface{}{
    		"prompt":     prompt,
    		"parameters": parameters,
    	})
    	if err != nil {
    		fmt.Fprintf(w, "unable to convert prompt to Value: %v", err)
    		return err
    	}
    
    	req := &aiplatformpb.[PredictRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1/aiplatformpb.html#cloud_google_com_go_aiplatform_apiv1_aiplatformpb_PredictRequest){
    		Endpoint:  gemma2Endpoint,
    		Instances: []*structpb.[Value](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1/aiplatformpb.html#cloud_google_com_go_aiplatform_apiv1_aiplatformpb_Value){promptValue},
    	}
    
    	resp, err := client.[Predict](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1/aiplatformpb.html#cloud_google_com_go_aiplatform_apiv1_aiplatformpb_UnimplementedPredictionServiceServer_Predict)(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	prediction := resp.GetPredictions()
    	value := prediction[0].GetStringValue()
    	fmt.Fprintf(w, "%v", value)
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html);
    import com.google.cloud.aiplatform.v1.[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html);
    import com.google.gson.Gson;
    import com.google.protobuf.[InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    
    public class Gemma2PredictTpu {
      private final [PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html) predictionServiceClient;
    
      // Constructor to inject the PredictionServiceClient
      public Gemma2PredictTpu([PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html) predictionServiceClient) {
        this.predictionServiceClient = predictionServiceClient;
      }
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR_PROJECT_ID";
        String endpointRegion = "us-west1";
        String endpointId = "YOUR_ENDPOINT_ID";
    
        [PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html) predictionServiceSettings =
            [PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html).newBuilder()
                .setEndpoint(String.format("%s-aiplatform.googleapis.com:443", endpointRegion))
                .build();
        [PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html) predictionServiceClient =
            [PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html).create(predictionServiceSettings);
        Gemma2PredictTpu creator = new Gemma2PredictTpu(predictionServiceClient);
    
        creator.gemma2PredictTpu(projectId, endpointRegion, endpointId);
      }
    
      // Demonstrates how to run inference on a Gemma2 model
      // deployed to a Vertex AI endpoint with TPU accelerators.
      public String gemma2PredictTpu(String projectId, String region,
               String endpointId) throws IOException {
        Map<String, Object> paramsMap = new HashMap<>();
        paramsMap.put("temperature", 0.9);
        paramsMap.put("maxOutputTokens", 1024);
        paramsMap.put("topP", 1.0);
        paramsMap.put("topK", 1);
        [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html) parameters = mapToValue(paramsMap);
        // Prompt used in the prediction
        String instance = "{ \"prompt\": \"Why is the sky blue?\"}";
        [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).Builder instanceValue = [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder();
        [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(instance, instanceValue);
        // Encapsulate the prompt in a correct format for TPUs
        // Example format: [{'prompt': 'Why is the sky blue?', 'temperature': 0.9}]
        [List<Value>](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html) instances = new ArrayList<>();
        instances.add(instanceValue.build());
    
        [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html) endpointName = [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html).of(projectId, region, endpointId);
    
        [PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html) predictResponse = this.predictionServiceClient
            .predict(endpointName, instances, parameters);
        String textResponse = predictResponse.[getPredictions](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html#com_google_cloud_aiplatform_v1_PredictResponse_getPredictions_int_)(0).getStringValue();
        System.out.println(textResponse);
        return textResponse;
      }
    
      private static [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html) mapToValue(Map<String, Object> map) throws [InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html) {
        Gson gson = new Gson();
        String json = gson.toJson(map);
        [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).Builder builder = [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder();
        [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(json, builder);
        return [builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree.html#com_google_protobuf_TextFormatParseInfoTree_builder__).build();
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Prediction Service Client library
    const {
      // TODO(developer): Uncomment PredictionServiceClient before running the sample.
      // PredictionServiceClient,
      helpers,
    } = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    /**
     * TODO(developer): Update these variables before running the sample.
     */
    const projectId = 'your-project-id';
    const endpointRegion = 'your-vertex-endpoint-region';
    const endpointId = 'your-vertex-endpoint-id';
    
    // Prompt used in the prediction
    const prompt = 'Why is the sky blue?';
    
    // Encapsulate the prompt in a correct format for TPUs
    // Example format: [{prompt: 'Why is the sky blue?', temperature: 0.9}]
    const input = {
      prompt,
      // Parameters for default configuration
      maxOutputTokens: 1024,
      temperature: 0.9,
      topP: 1.0,
      topK: 1,
    };
    
    // Convert input message to a list of GAPIC instances for model input
    const instances = [[helpers](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html).toValue(input)];
    
    // TODO(developer): Uncomment apiEndpoint and predictionServiceClient before running the sample.
    // const apiEndpoint = `${endpointRegion}-aiplatform.googleapis.com`;
    
    // Create a client
    // predictionServiceClient = new PredictionServiceClient({apiEndpoint});
    
    // Call the Gemma2 endpoint
    const gemma2Endpoint = `projects/${projectId}/locations/${endpointRegion}/endpoints/${endpointId}`;
    
    const [response] = await predictionServiceClient.predict({
      endpoint: gemma2Endpoint,
      instances,
    });
    
    const predictions = response.predictions;
    const text = predictions[0].stringValue;
    
    console.log('Predictions:', text);

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    """
    Sample to run inference on a Gemma2 model deployed to a Vertex AI endpoint with TPU accellerators.
    """
    
    from google.cloud import aiplatform
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value
    
    # TODO(developer): Update & uncomment lines below
    # PROJECT_ID = "your-project-id"
    # ENDPOINT_REGION = "your-vertex-endpoint-region"
    # ENDPOINT_ID = "your-vertex-endpoint-id"
    
    # Default configuration
    config = {"max_tokens": 1024, "temperature": 0.9, "top_p": 1.0, "top_k": 1}
    
    # Prompt used in the prediction
    prompt = "Why is the sky blue?"
    
    # Encapsulate the prompt in a correct format for TPUs
    # Example format: [{'prompt': 'Why is the sky blue?', 'temperature': 0.9}]
    input = {"prompt": prompt}
    input.update(config)
    
    # Convert input message to a list of GAPIC instances for model input
    instances = [json_format.ParseDict(input, Value())]
    
    # Create a client
    api_endpoint = f"{ENDPOINT_REGION}-aiplatform.googleapis.com"
    client = aiplatform.gapic.[PredictionServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.prediction_service.PredictionServiceClient.html)(
        client_options={"api_endpoint": api_endpoint}
    )
    
    # Call the Gemma2 endpoint
    gemma2_end_point = (
        f"projects/{PROJECT_ID}/locations/{ENDPOINT_REGION}/endpoints/{ENDPOINT_ID}"
    )
    response = client.[predict](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.prediction_service.PredictionServiceClient.html)(
        endpoint=gemma2_end_point,
        instances=instances,
    )
    text_responses = response.predictions
    print(text_responses[0])
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
