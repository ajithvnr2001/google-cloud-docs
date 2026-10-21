---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-sdk-sentiment-analysis/
title: Classify sentiment in text (Generative AI) \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:54.942338+00:00
---

# Classify sentiment in text (Generative AI)  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-sdk-sentiment-analysis/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Classify sentiment in text (Generative AI) Stay organized with collections  Save and categorize content based on your preferences. 

Classify the sentiment conveyed in text as positive or negative.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1beta1.EndpointName;
    import com.google.cloud.aiplatform.v1beta1.PredictResponse;
    import com.google.cloud.aiplatform.v1beta1.PredictionServiceClient;
    import com.google.cloud.aiplatform.v1beta1.PredictionServiceSettings;
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    // Text sentiment analysis with a Large Language Model
    public class PredictTextSentimentSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // The details of designing text prompts for supported large language models:
        // https://cloud.google.com/vertex-ai/docs/generative-ai/text/text-overview
        String instance =
            "{ \"content\": \"I had to compare two versions of Hamlet for my Shakespeare \n"
                + "class and unfortunately I picked this version. Everything from the acting \n"
                + "(the actors deliver most of their lines directly to the camera) to the camera \n"
                + "shots (all medium or close up shots...no scenery shots and very little back \n"
                + "ground in the shots) were absolutely terrible. I watched this over my spring \n"
                + "break and it is very safe to say that I feel that I was gypped out of 114 \n"
                + "minutes of my vacation. Not recommended by any stretch of the imagination.\n"
                + "Classify the sentiment of the message: negative\n"
                + "\n"
                + "Something surprised me about this movie - it was actually original. It was \n"
                + "not the same old recycled crap that comes out of Hollywood every month. I saw \n"
                + "this movie on video because I did not even know about it before I saw it at my \n"
                + "local video store. If you see this movie available - rent it - you will not \n"
                + "regret it.\n"
                + "Classify the sentiment of the message: positive\n"
                + "\n"
                + "My family has watched Arthur Bach stumble and stammer since the movie first \n"
                + "came out. We have most lines memorized. I watched it two weeks ago and still \n"
                + "get tickled at the simple humor and view-at-life that Dudley Moore portrays. \n"
                + "Liza Minelli did a wonderful job as the side kick - though I'm not her \n"
                + "biggest fan. This movie makes me just enjoy watching movies. My favorite scene \n"
                + "is when Arthur is visiting his fiancée's house. His conversation with the \n"
                + "butler and Susan's father is side-spitting. The line from the butler, \n"
                + "\\\"Would you care to wait in the Library\\\" followed by Arthur's reply, \n"
                + "\\\"Yes I would, the bathroom is out of the question\\\", is my NEWMAIL \n"
                + "notification on my computer.\n"
                + "Classify the sentiment of the message: positive\n"
                + "\n"
                + "This Charles outing is decent but this is a pretty low-key performance. Marlon \n"
                + "Brando stands out. There's a subplot with Mira Sorvino and Donald Sutherland \n"
                + "that forgets to develop and it hurts the film a little. I'm still trying to \n"
                + "figure out why Charlie want to change his name.\n"
                + "Classify the sentiment of the message: negative\n"
                + "\n"
                + "Tweet: The Pixel 7 Pro, is too big to fit in my jeans pocket, so I bought new \n"
                + "jeans.\n"
                + "Classify the sentiment of the message: \"}";
        String parameters =
            "{\n"
                + "  \"temperature\": 0,\n"
                + "  \"maxDecodeSteps\": 5,\n"
                + "  \"topP\": 0,\n"
                + "  \"topK\": 1\n"
                + "}";
        String project = "YOUR_PROJECT_ID";
        String location = "us-central1";
        String publisher = "google";
        String model = "text-bison@001";
    
        predictTextSentiment(instance, parameters, project, location, publisher, model);
      }
    
      static void predictTextSentiment(
          String instance,
          String parameters,
          String project,
          String location,
          String publisher,
          String model)
          throws IOException {
        String endpoint = String.format("%s-aiplatform.googleapis.com:443", location);
        PredictionServiceSettings predictionServiceSettings =
            PredictionServiceSettings.newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (PredictionServiceClient predictionServiceClient =
            PredictionServiceClient.create(predictionServiceSettings)) {
          final EndpointName endpointName =
              EndpointName.ofProjectLocationPublisherModelName(project, location, publisher, model);
    
          // Use Value.Builder to convert instance to a dynamically typed value that can be
          // processed by the service.
          V[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)Builder instanceValue = V[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)newBuilder();
          J[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html)parser().merge(instance, instanceValue);
          L[Lis<tValu>e](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ListValue.html)instances = new ArrayList>();
          instances.add(instanceValue.build());
    
          // Use Value.Builder to convert parameter to a dynamically typed value that can be
          // processed by the service.
          V[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)Builder parameterValueBuilder = V[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)newBuilder();
          J[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html)parser().merge(parameters, parameterValueBuilder);
          V[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)parameterValue = parameterValueBuilder.build();
    
          PredictResponse predictResponse =
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
