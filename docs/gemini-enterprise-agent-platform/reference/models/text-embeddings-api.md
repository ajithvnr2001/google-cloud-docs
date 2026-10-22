---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/text-embeddings-api/
title: Text embeddings API \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:08.471228+00:00
---

# Text embeddings API  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/text-embeddings-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Text embeddings API Stay organized with collections  Save and categorize content based on your preferences. 

The Text embeddings API converts textual data into numerical vectors. These vector representations are designed to capture the semantic meaning and context of the words they represent.

## Supported models

You can get text embeddings by using the following models:

Model name | Description | Output Dimensions | Max sequence length | Supported text languages  
---|---|---|---|---  
`gemini-embedding-001` | State-of-the-art performance across English, multilingual and code tasks. It unifies the previously specialized models like `text-embedding-005` and `text-multilingual-embedding-002` and achieves better performance in their respective domains. Read our [Tech Report](https://deepmind.google/research/publications/157741/) for more detail. | up to 3072 | 2048 tokens | [Supported text languages](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/text-embeddings-api#supported_text_languages)  
`gemini-embedding-2` | Best for embedding long strings, including multilingual and unstructured data. Supports a mix of text, images, audio, video, and PDF files. | up to 3072 | 8192 tokens | [Supported text languages](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/text-embeddings-api#supported_text_languages)  
`text-embedding-005` | Specialized in English and code tasks. | up to 768 | 2048 tokens | English  
`text-multilingual-embedding-002` | Specialized in multilingual tasks. | up to 768 | 2048 tokens | [Supported text languages](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/text-embeddings-api#supported_text_languages)  
  
For superior embedding quality, `gemini-embedding-001` is our large model designed to provide the highest performance.

## Syntax

### curl
    
    
    PROJECT_ID = PROJECT_ID
    REGION = us-central1
    MODEL_ID = MODEL_ID
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      https://${REGION}-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${REGION}/publishers/google/models/${MODEL_ID}:predict -d \
      '{
        "instances": [
          ...
        ],
        "parameters": {
          ...
        }
      }'

### Python
    
    
    PROJECT_ID = PROJECT_ID
    REGION = us-central1
    MODEL_ID = MODEL_ID
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai.language_models import TextEmbeddingModel
    
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(project=PROJECT_ID, location=REGION)
    
    model = TextEmbeddingModel.from_pretrained(MODEL_ID)
    embeddings = model.[get_embeddings](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.MultiModalEmbeddingModel.html#vertexai_preview_vision_models_MultiModalEmbeddingModel_get_embeddings)(...)

## Parameter list

Top-level fields  
---  
`instances` | A list of objects containing the following fields:

  * **`content`**
  * **`title`** (optional)
  * **`task_type`** (optional)

  
`parameters` | An object containing the following fields:

  * **`autoTruncate`** (optional)
  * **`outputDimensionality`** (optional)

  
`instance` fields  
---  
`content` | `string`The text that you want to generate embeddings for.  
`task_type` | Optional: `string`Used to convey intended downstream application to help the model produce better embeddings. If left blank, the default used is `RETRIEVAL_QUERY`.

  * `RETRIEVAL_QUERY`
  * `RETRIEVAL_DOCUMENT`
  * `SEMANTIC_SIMILARITY`
  * `CLASSIFICATION`
  * `CLUSTERING`
  * `QUESTION_ANSWERING`
  * `FACT_VERIFICATION`
  * `CODE_RETRIEVAL_QUERY`

For more information about task types, see [Choose an embeddings task type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/task-types).  
`title` | Optional: `string`Used to help the model produce better embeddings. Only valid with `task_type=RETRIEVAL_DOCUMENT`.  
  
#### `task_type`

The following table describes the `task_type` parameter values and their use cases:

`task_type` | Description  
---|---  
`RETRIEVAL_QUERY` | Specifies the given text is a query in a search or retrieval setting. Use RETRIEVAL_DOCUMENT for the document side.  
`RETRIEVAL_DOCUMENT` | Specifies the given text is a document in a search or retrieval setting.  
`SEMANTIC_SIMILARITY` | Specifies the given text is used for Semantic Textual Similarity (STS).  
`CLASSIFICATION` | Specifies that the embedding is used for classification.  
`CLUSTERING` | Specifies that the embedding is used for clustering.  
`QUESTION_ANSWERING` | Specifies that the query embedding is used for answering questions. Use RETRIEVAL_DOCUMENT for the document side.  
`FACT_VERIFICATION` | Specifies that the query embedding is used for fact verification. Use RETRIEVAL_DOCUMENT for the document side.  
`CODE_RETRIEVAL_QUERY` | Specifies that the query embedding is used for code retrieval for Java and Python. Use RETRIEVAL_DOCUMENT for the document side.  
  
**Retrieval Tasks** :

Query: Use task_type=`RETRIEVAL_QUERY` to indicate that the input text is a search query. Corpus: Use task_type=`RETRIEVAL_DOCUMENT` to indicate that the input text is part of the document collection being searched.

**Similarity Tasks** :

Semantic similarity: Use task_type= `SEMANTIC_SIMILARITY` for both input texts to assess their overall meaning similarity.

**Note:** `SEMANTIC_SIMILARITY` is not intended for retrieval use cases, such as document search and information retrieval. For these use cases, use `RETRIEVAL_DOCUMENT`, `RETRIEVAL_QUERY`, `QUESTION_ANSWERING`, and `FACT_VERIFICATION`.`parameters` fields  
---  
`autoTruncate` | Optional: `bool`When set to true, input text will be truncated. When set to false, an error is returned if the input text is longer than the maximum length supported by the model. Defaults to true.  
`outputDimensionality` | Optional: `int`Used to specify output embedding size. If set, output embeddings will be truncated to the size specified.  
  
### Request body
    
    
    {
      "instances": [
        {
          "task_type": "RETRIEVAL_DOCUMENT",
          "title": "document title",
          "content": "I would like embeddings for this text!"
        },
      ]
    }
    

### Response body
    
    
    {
      "predictions": [
        {
          "embeddings": {
            "statistics": {
              "truncated": boolean,
              "token_count": integer
            },
            "values": [ number ]
          }
        }
      ]
    }
    

Response elements  
---  
`predictions` | A list of objects with the following fields:

  * **`embeddings`** : The result generated from input text. Contains the following fields:
    * **`values`**
    * **`statistics`**

  
`embeddings` fields  
---  
`values` | A list of `float`s. The `values` field contains a numerical encoding (embedding vector) of the semantic content present in the given input text.  
`statistics` | The statistics computed from the input text. Contains:

  * **`truncated`** : Indicates whether the input text was truncated due to being longer than the maximum number of tokens allowed by the model.
  * **`token_count`** : Number of tokens of the input text.

  
  
#### Sample response
    
    
    {
      "predictions": [
        {
          "embeddings": {
            "values": [
              0.0058424929156899452,
              0.011848051100969315,
              0.032247550785541534,
              -0.031829461455345154,
              -0.055369812995195389,
              ...
            ],
            "statistics": {
              "token_count": 4,
              "truncated": false
            }
          }
        }
      ]
    }
    

## Examples

### Embed a text string

The following example shows how to obtain the embedding of a text string.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers). .
  * TEXT: The text that you want to generate embeddings for. **Limit:** five texts of up to 2,048 tokens per text for all models except `textembedding-gecko@001`. The max input token length for `textembedding-gecko@001` is 3072. For `gemini-embedding-001`, each request can only include a single input text. For more information, see [Text embedding limits](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas#text-embedding-limits). 
  * AUTO_TRUNCATE: If set to `false`, text that exceeds the token limit causes the request to fail. The default value is `true`.



HTTP method and URL: 
    
    
    POST https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/gemini-embedding-001:predict

Request JSON body: 
    
    
    {
      "instances": [
        { "content": "TEXT"}
      ],
      "parameters": { 
        "autoTruncate": AUTO_TRUNCATE 
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
         "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/gemini-embedding-001:predict"

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
        -Uri "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/gemini-embedding-001:predict" | Select-Object -Expand Content

You should receive a JSON response similar to the following. Note that `values` has been truncated to save space. 

#### Response
    
    
    {
      "predictions": [
        {
          "embeddings": {
            "statistics": {
              "truncated": false,
              "token_count": 6
            },
            "values": [ ... ]
          }
        }
      ]
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import EmbedContentConfig
    
    client = genai.Client()
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=[
            "How do I get a driver's license/learner's permit?",
            "How long is my driver's license valid for?",
            "Driver's knowledge test study guide",
        ],
        config=EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",  # Optional
            output_dimensionality=3072,  # Optional
            title="Driver's License",  # Optional
        ),
    )
    print(response)
    # Example response:
    # embeddings=[ContentEmbedding(values=[-0.06302902102470398, 0.00928034819662571, 0.014716853387653828, -0.028747491538524628, ... ],
    # statistics=ContentEmbeddingStatistics(truncated=False, token_count=13.0))]
    # metadata=EmbedContentMetadata(billable_character_count=112)

### Go

Before trying this sample, follow the Go setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	aiplatform "cloud.google.com/go/aiplatform/apiv1"
    	"cloud.google.com/go/aiplatform/apiv1/aiplatformpb"
    
    	"google.golang.org/api/option"
    	"google.golang.org/protobuf/types/known/structpb"
    )
    
    // embedTexts shows how embeddings are set for gemini-embedding-001 model
    func embedTexts(w io.Writer, project, location string) error {
    	// location := "us-central1"
    	ctx := context.Background()
    
    	apiEndpoint := fmt.Sprintf("%s-aiplatform.googleapis.com:443", location)
    	dimensionality := 3072
    	model := "gemini-embedding-001"
    	texts := []string{"banana muffins? ", "banana bread? banana muffins?"}
    
    	client, err := aiplatform.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1.html#cloud_google_com_go_aiplatform_apiv1_PredictionClient_NewPredictionClient)(ctx, option.WithEndpoint(apiEndpoint))
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	endpoint := fmt.Sprintf("projects/%s/locations/%s/publishers/google/models/%s", project, location, model)
    	allEmbeddings := make([][]float32, 0, len(texts))
    	// gemini-embedding-001 takes 1 input at a time
    	for _, text := range texts {
    		instances := make([]*structpb.Value, 1)
    		instances[0] = structpb.NewStructValue(&structpb.Struct{
    			Fields: map[string]*structpb.Value{
    				"content":   structpb.NewStringValue(text),
    				"task_type": structpb.NewStringValue("QUESTION_ANSWERING"),
    			},
    		})
    
    		params := structpb.NewStructValue(&structpb.Struct{
    			Fields: map[string]*structpb.Value{
    				"outputDimensionality": structpb.NewNumberValue(float64(dimensionality)),
    			},
    		})
    
    		req := &aiplatformpb.PredictRequest{
    			Endpoint:   endpoint,
    			Instances:  instances,
    			Parameters: params,
    		}
    		resp, err := client.Predict(ctx, req)
    		if err != nil {
    			return err
    		}
    
    		// Process the prediction for the single text
    		// The response will contain one prediction because we sent one instance.
    		if len(resp.Predictions) == 0 {
    			return fmt.Errorf("no predictions returned for text \"%s\"", text)
    		}
    
    		prediction := resp.Predictions[0]
    		embeddingValues := prediction.GetStructValue().Fields["embeddings"].GetStructValue().Fields["values"].[GetListValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1beta1/aiplatformpb.html#cloud_google_com_go_aiplatform_apiv1beta1_aiplatformpb_MetadataValue_GetListValue)().Values
    
    		currentEmbedding := make([]float32, len(embeddingValues))
    		for j, value := range embeddingValues {
    			currentEmbedding[j] = float32(value.GetNumberValue())
    		}
    		allEmbeddings = append(allEmbeddings, currentEmbedding)
    	}
    
    	if len(allEmbeddings) > 0 {
    		fmt.Fprintf(w, "Dimensionality: %d. Embeddings length: %d", len(allEmbeddings[0]), len(allEmbeddings))
    	} else {
    		fmt.Fprintln(w, "No texts were processed.")
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Node.js setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## Supported text languages

All text embedding models support and have been evaluated on English-language text. The `text-multilingual-embedding-002` model additionally supports and has been evaluated on the following languages:

  * **Evaluated languages:** `Arabic (ar)`, `Bengali (bn)`, `English (en)`, `Spanish (es)`, `German (de)`, `Persian (fa)`, `Finnish (fi)`, `French (fr)`, `Hindi (hi)`, `Indonesian (id)`, `Japanese (ja)`, `Korean (ko)`, `Russian (ru)`, `Swahili (sw)`, `Telugu (te)`, `Thai (th)`, `Yoruba (yo)`, `Chinese (zh)`
  * **Supported languages** : `Afrikaans`, `Albanian`, `Amharic`, `Arabic`, `Armenian`, `Azerbaijani`, `Basque`, `Belarusiasn`, `Bengali`, `Bulgarian`, `Burmese`, `Catalan`, `Cebuano`, `Chichewa`, `Chinese`, `Corsican`, `Czech`, `Danish`, `Dutch`, `English`, `Esperanto`, `Estonian`, `Filipino`, `Finnish`, `French`, `Galician`, `Georgian`, `German`, `Greek`, `Gujarati`, `Haitian Creole`, `Hausa`, `Hawaiian`, `Hebrew`, `Hindi`, `Hmong`, `Hungarian`, `Icelandic`, `Igbo`, `Indonesian`, `Irish`, `Italian`, `Japanese`, `Javanese`, `Kannada`, `Kazakh`, `Khmer`, `Korean`, `Kurdish`, `Kyrgyz`, `Lao`, `Latin`, `Latvian`, `Lithuanian`, `Luxembourgish`, `Macedonian`, `Malagasy`, `Malay`, `Malayalam`, `Maltese`, `Maori`, `Marathi`, `Mongolian`, `Nepali`, `Norwegian`, `Pashto`, `Persian`, `Polish`, `Portuguese`, `Punjabi`, `Romanian`, `Russian`, `Samoan`, `Scottish Gaelic`, `Serbian`, `Shona`, `Sindhi`, `Sinhala`, `Slovak`, `Slovenian`, `Somali`, `Sotho`, `Spanish`, `Sundanese`, `Swahili`, `Swedish`, `Tajik`, `Tamil`, `Telugu`, `Thai`, `Turkish`, `Ukrainian`, `Urdu`, `Uzbek`, `Vietnamese`, `Welsh`, `West Frisian`, `Xhosa`, `Yiddish`, `Yoruba`, `Zulu`.



The `gemini-embedding-001` model supports the following languages:

`Arabic`, `Bengali`, `Bulgarian`, `Chinese (Simplified and Traditional)`, `Croatian`, `Czech`, `Danish`, `Dutch`, `English`, `Estonian`, `Finnish`, `French`, `German`, `Greek`, `Hebrew`, `Hindi`, `Hungarian`, `Indonesian`, `Italian`, `Japanese`, `Korean`, `Latvian`, `Lithuanian`, `Norwegian`, `Polish`, `Portuguese`, `Romanian`, `Russian`, `Serbian`, `Slovak`, `Slovenian`, `Spanish`, `Swahili`, `Swedish`, `Thai`, `Turkish`, `Ukrainian`, `Vietnamese`, `Afrikaans`, `Amharic`, `Assamese`, `Azerbaijani`, `Belarusian`, `Bosnian`, `Catalan`, `Cebuano`, `Corsican`, `Welsh`, `Dhivehi`, `Esperanto`, `Basque`, `Persian`, `Filipino (Tagalog)`, `Frisian`, `Irish`, `Scots Gaelic`, `Galician`, `Gujarati`, `Hausa`, `Hawaiian`, `Hmong`, `Haitian Creole`, `Armenian`, `Igbo`, `Icelandic`, `Javanese`, `Georgian`, `Kazakh`, `Khmer`, `Kannada`, `Krio`, `Kurdish`, `Kyrgyz`, `Latin`, `Luxembourgish`, `Lao`, `Malagasy`, `Maori`, `Macedonian`, `Malayalam`, `Mongolian`, `Meiteilon (Manipuri)`, `Marathi`, `Malay`, `Maltese`, `Myanmar (Burmese)`, `Nepali`, `Nyanja (Chichewa)`, `Odia (Oriya)`, `Punjabi`, `Pashto`, `Sindhi`, `Sinhala (Sinhalese)`, `Samoan`, `Shona`, `Somali`, `Albanian`, `Sesotho`, `Sundanese`, `Tamil`, `Telugu`, `Tajik`, `Uyghur`, `Urdu`, `Uzbek`, `Xhosa`, `Yiddish`, `Yoruba`, `Zulu`.

## Model versions

To use a current stable model, specify the model version number, for example `gemini-embedding-001`. Specifying a model without a version number, isn't recommended, as it is merely a legacy pointer to another model and isn't stable.

For more information, see [Model versions and lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions).

## What's next

For detailed documentation, see the following:

  * [Text Embeddings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-text-embeddings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
