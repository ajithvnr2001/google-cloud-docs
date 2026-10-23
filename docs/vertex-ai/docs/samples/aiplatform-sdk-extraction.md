---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-sdk-extraction/
title: Extract information from text (Generative AI) \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:32.152084+00:00
---

# Extract information from text (Generative AI)  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-sdk-extraction/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Extract information from text (Generative AI) Stay organized with collections  Save and categorize content based on your preferences. 

Extract information from text using a publisher text model.

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
    
    // Extractive Question Answering with a Large Language Model
    public class PredictTextExtractionSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Details about designing prompts that extract information from text:
        // https://cloud.google.com/vertex-ai/docs/generative-ai/text/extraction-prompts
        String instance =
            "{\"content\": \"Background: There is evidence that there have been significant changes \n"
                + "in Amazon rainforest vegetation over the last 21,000 years through the Last \n"
                + "Glacial Maximum (LGM) and subsequent deglaciation. Analyses of sediment \n"
                + "deposits from Amazon basin paleo lakes and from the Amazon Fan indicate that \n"
                + "rainfall in the basin during the LGM was lower than for the present, and this \n"
                + "was almost certainly associated with reduced moist tropical vegetation cover \n"
                + "in the basin. There is debate, however, over how extensive this reduction \n"
                + "was. Some scientists argue that the rainforest was reduced to small, isolated \n"
                + "refugia separated by open forest and grassland; other scientists argue that \n"
                + "the rainforest remained largely intact but extended less far to the north, \n"
                + "south, and east than is seen today. This debate has proved difficult to \n"
                + "resolve because the practical limitations of working in the rainforest mean \n"
                + "that data sampling is biased away from the center of the Amazon basin, and \n"
                + "both explanations are reasonably well supported by the available data.\n"
                + "\n"
                + "Q: What does LGM stands for?\n"
                + "A: Last Glacial Maximum.\n"
                + "\n"
                + "Q: What did the analysis from the sediment deposits indicate?\n"
                + "A: Rainfall in the basin during the LGM was lower than for the present.\n"
                + "\n"
                + "Q: What are some of scientists arguments?\n"
                + "A: The rainforest was reduced to small, isolated refugia separated by open forest"
                + " and grassland.\n"
                + "\n"
                + "Q: There have been major changes in Amazon rainforest vegetation over the last how"
                + " many years?\n"
                + "A: 21,000.\n"
                + "\n"
                + "Q: What caused changes in the Amazon rainforest vegetation?\n"
                + "A: The Last Glacial Maximum (LGM) and subsequent deglaciation\n"
                + "\n"
                + "Q: What has been analyzed to compare Amazon rainfall in the past and present?\n"
                + "A: Sediment deposits.\n"
                + "\n"
                + "Q: What has the lower rainfall in the Amazon during the LGM been attributed to?\n"
                + "A:\"}";
        String parameters =
            "{\n"
                + "  \"temperature\": 0,\n"
                + "  \"maxDecodeSteps\": 32,\n"
                + "  \"topP\": 0,\n"
                + "  \"topK\": 1\n"
                + "}";
        String project = "YOUR_PROJECT_ID";
        String location = "us-central1";
        String publisher = "google";
        String model = "text-bison@001";
    
        predictTextExtraction(instance, parameters, project, location, publisher, model);
      }
    
      static void predictTextExtraction(
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
    
          // Use Value.Builder to convert instance to a dynamically typed value that can be
          // processed by the service.
          [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).Builder instanceValue = [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder();
          [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(instance, instanceValue);
          [List<Value>](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html) instances = new ArrayList<>();
          instances.add(instanceValue.build());
    
          // Use Value.Builder to convert parameter to a dynamically typed value that can be
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
