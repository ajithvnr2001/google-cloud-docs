---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-sdk-ideation/
title: Test text prompts (Generative AI) \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:32.590047+00:00
---

# Test text prompts (Generative AI)  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-sdk-ideation/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Test text prompts (Generative AI) Stay organized with collections  Save and categorize content based on your preferences. 

Test a test prompt to generate ideas using a publisher text model.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html);
    import com.google.cloud.aiplatform.v1.[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class PredictTextPromptSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Details of designing text prompts for supported large language models:
        // https://cloud.google.com/vertex-ai/docs/generative-ai/text/text-overview
        String instance =
            "{ \"prompt\": " + "\"Give me ten interview questions for the role of program manager.\"}";
        String parameters =
            "{\n"
                + "  \"temperature\": 0.2,\n"
                + "  \"maxOutputTokens\": 256,\n"
                + "  \"topP\": 0.95,\n"
                + "  \"topK\": 40\n"
                + "}";
        String project = "YOUR_PROJECT_ID";
        String location = "us-central1";
        String publisher = "google";
        String model = "text-bison@001";
    
        predictTextPrompt(instance, parameters, project, location, publisher, model);
      }
    
      // Get a text prompt from a supported text model
      public static void predictTextPrompt(
          String instance,
          String parameters,
          String project,
          String location,
          String publisher,
          String model)
          throws IOException {
        String endpoint = String.format("%s-aiplatform.googleapis.com:443", location);
        [PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html) predictionServiceSettings =
            [PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html) predictionServiceClient =
            [PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html).create(predictionServiceSettings)) {
          final [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html) endpointName =
              [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html).[ofProjectLocationPublisherModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html#com_google_cloud_aiplatform_v1_EndpointName_ofProjectLocationPublisherModelName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(project, location, publisher, model);
    
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).Builder instanceValue = [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder();
          [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(instance, instanceValue);
          [List<Value>](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html) instances = new ArrayList<>();
          instances.add(instanceValue.build());
    
          // Use Value.Builder to convert instance to a dynamically typed value that can be
          // processed by the service.
          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).Builder parameterValueBuilder = [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder();
          [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(parameters, parameterValueBuilder);
          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html) parameterValue = parameterValueBuilder.build();
    
          [PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html) predictResponse =
              predictionServiceClient.predict(endpointName, instances, parameterValue);
          System.out.println("Predict Response");
          System.out.println(predictResponse);
        }
      }
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/ai_platform/v1"
    
    ##
    # Vertex AI Predict Text Prompt
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param location_id [String] Your Processor Location (e.g. "us-central1")
    # @param publisher [String] The Model Publisher (e.g. "google")
    # @param model [String] The Model Identifier (e.g. "text-bison@001")
    #
    def predict_text_prompt project_id:, location_id:, publisher:, model:
      # Create the Vertex AI client.
      client = ::Google::Cloud::AIPlatform::V1::PredictionService::Client.new do |config|
        config.endpoint = "#{location_id}-aiplatform.googleapis.com"
      end
    
      # Build the resource name from the project.
      endpoint = client.endpoint_path(
        project: project_id,
        location: location_id,
        publisher: publisher,
        model: model
      )
    
      prompt = "Give me ten interview questions for the role of program manager."
    
      # Initialize the request arguments
      instance = Google::Protobuf::[Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Value.html).new(
        struct_value: Google::Protobuf::[Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Struct.html).new(
          fields: {
            "prompt" => Google::Protobuf::Value.new(
              string_value: prompt
            )
          }
        )
      )
    
      instances = [instance]
    
      parameters = Google::Protobuf::[Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Value.html).new(
        struct_value: Google::Protobuf::[Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Struct.html).new(
          fields: {
            "temperature" => Google::Protobuf::Value.new(number_value: 0.2),
            "maxOutputTokens" => Google::Protobuf::Value.new(number_value: 256),
            "topP" => Google::Protobuf::Value.new(number_value: 0.95),
            "topK" => Google::Protobuf::Value.new(number_value: 40)
          }
        )
      )
    
      # Make the prediction request
      response = client.predict endpoint: endpoint, instances: instances, parameters: parameters
    
      # Handle the prediction response
      puts "Predict Response"
      puts response
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
