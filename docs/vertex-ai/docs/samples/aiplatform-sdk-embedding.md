---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-sdk-embedding/
title: Get text embeddings (Generative AI) \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:29.986698+00:00
---

# Get text embeddings (Generative AI)  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-sdk-embedding/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Get text embeddings (Generative AI) Stay organized with collections  Save and categorize content based on your preferences. 

Get text embeddings for a snippet of text using an embedding model.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import static java.util.stream.Collectors.toList;
    
    import com.google.cloud.aiplatform.v1.[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html);
    import com.google.cloud.aiplatform.v1.[PredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequest.html);
    import com.google.cloud.aiplatform.v1.[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html);
    import com.google.protobuf.[Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.OptionalInt;
    import java.util.regex.Matcher;
    import java.util.regex.Pattern;
    
    public class PredictTextEmbeddingsSample {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Details about text embedding request structure and supported models are available in:
        // https://cloud.google.com/vertex-ai/docs/generative-ai/embeddings/get-text-embeddings
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        String project = "YOUR_PROJECT_ID";
        String model = "gemini-embedding-001";
        predictTextEmbeddings(
            endpoint,
            project,
            model,
            List.of("banana bread?", "banana muffins?"),
            "QUESTION_ANSWERING",
            OptionalInt.of(3072));
      }
    
      // Gets text embeddings from a pretrained, foundational model.
      public static List<List<Float>> predictTextEmbeddings(
          String endpoint,
          String project,
          String model,
          List<String> texts,
          String task,
          OptionalInt outputDimensionality)
          throws IOException {
        [PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html) settings =
            [PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
        Matcher matcher = Pattern.compile("^(?<Location>\\w+-\\w+)").matcher(endpoint);
        String location = matcher.matches() ? matcher.group("Location") : "us-central1";
        [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html) endpointName =
            [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html).[ofProjectLocationPublisherModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html#com_google_cloud_aiplatform_v1_EndpointName_ofProjectLocationPublisherModelName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(project, location, "google", model);
    
        List<List<Float>> floats = new ArrayList<>();
        // You can use this prediction service client for multiple requests.
        try ([PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html) client = [PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictionServiceClient.html).create(settings)) {
          // gemini-embedding-001 takes one input at a time.
          for (int i = 0; i < texts.size(); i++) {
            [PredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequest.html).Builder request = 
                [PredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictRequest.html).newBuilder().setEndpoint(endpointName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointName.html#com_google_cloud_aiplatform_v1_EndpointName_toString__)());
            if (outputDimensionality.isPresent()) {
              request.setParameters(
                  [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html).newBuilder()
                      .setStructValue(
                          [Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html).newBuilder()
                              .putFields(
                                  "outputDimensionality", valueOf(outputDimensionality.getAsInt()))
                              .build()));
            }
            request.addInstances(
                [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html).newBuilder()
                    .setStructValue(
                        [Struct](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html).newBuilder()
                            .putFields("content", valueOf(texts.get(i)))
                            .putFields("task_type", valueOf(task))
                            .build()));
            [PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html) response = client.predict(request.build());
    
            for ([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html) prediction : response.[getPredictionsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictResponse.html#com_google_cloud_aiplatform_v1_PredictResponse_getPredictionsList__)()) {
              [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html) embeddings = prediction.getStructValue().getFieldsOrThrow("embeddings");
              [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html) values = embeddings.[getStructValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html#com_google_protobuf_Value_getStructValue__)().getFieldsOrThrow("values");
              floats.add(
                  values.[getListValue](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html#com_google_protobuf_Value_getListValue__)().getValuesList().stream()
                      .map(Value::getNumberValue)
                      .map(Double::floatValue)
                      .collect(toList()));
            }
          }
          return floats;
        }
      }
    
      private static [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html) valueOf(String s) {
        return [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html).newBuilder().setStringValue(s).build();
      }
    
      private static [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html) valueOf(int n) {
        return [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html).newBuilder().setNumberValue(n).build();
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function main(
      project,
      model = 'gemini-embedding-001',
      texts = 'banana bread?;banana muffins?',
      task = 'QUESTION_ANSWERING',
      dimensionality = 0,
      apiEndpoint = 'us-central1-aiplatform.googleapis.com'
    ) {
      const aiplatform = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
      const {PredictionServiceClient} = aiplatform.v1;
      const {helpers} = aiplatform; // helps construct protobuf.Value objects.
      const clientOptions = {apiEndpoint: apiEndpoint};
      const location = 'us-central1';
      const endpoint = `projects/${project}/locations/${location}/publishers/google/models/${model}`;
    
      async function callPredict() {
        const instances = texts
          .split(';')
          .map(e => [helpers](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html).toValue({content: e, task_type: task}));
    
        const client = new [PredictionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
        const parameters = [helpers](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html).toValue(
          dimensionality > 0 ? {outputDimensionality: parseInt(dimensionality)} : {}
        );
        const allEmbeddings = []
        // gemini-embedding-001 takes one input at a time.
        for (const instance of instances) {
          const request = {endpoint, instances: [instance], parameters};
          const [response] = await client.predict(request);
          const predictions = response.predictions;
    
          const embeddings = predictions.map(p => {
            const embeddingsProto = p.structValue.fields.embeddings;
            const valuesProto = embeddingsProto.structValue.fields.values;
            return valuesProto.listValue.values.map(v => v.numberValue);
          });
    
          allEmbeddings.push(embeddings[0])
        }
    
    
        console.log('Got embeddings: \n' + JSON.stringify(allEmbeddings));
      }
    
      callPredict();
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
