---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-contentcache-create-with-txt-gcs-pdf/
title: Create a context cache \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:55.618642+00:00
---

# Create a context cache  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-contentcache-create-with-txt-gcs-pdf/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Create a context cache Stay organized with collections  Save and categorize content based on your preferences. 

Create a context cache to reduce costs with repeated requests that contain the same token count input.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a context cache](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-create)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"io"
    	"time"
    
    	genai "google.golang.org/genai"
    )
    
    // createContentCache shows how to create a content cache with an expiration parameter.
    func createContentCache(w io.Writer) (string, error) {
    	ctx := context.Background()
    
    	client, err := genai.NewClient(ctx, &genai.ClientConfig{
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return "", fmt.Errorf("failed to create genai client: %w", err)
    	}
    
    	modelName := "gemini-2.5-flash"
    
    	systemInstruction := "You are an expert researcher. You always stick to the facts " +
    		"in the sources provided, and never make up new facts. " +
    		"Now look at these research papers, and answer the following questions."
    
    	cacheContents := []*genai.Content{
    		{
    			Parts: []*genai.Part{
    				{FileData: &genai.FileData{
    					FileURI:  "gs://cloud-samples-data/generative-ai/pdf/2312.11805v3.pdf",
    					MIMEType: "application/pdf",
    				}},
    				{FileData: &genai.FileData{
    					FileURI:  "gs://cloud-samples-data/generative-ai/pdf/2403.05530.pdf",
    					MIMEType: "application/pdf",
    				}},
    			},
    			Role: genai.RoleUser,
    		},
    	}
    	config := &genai.CreateCachedContentConfig{
    		Contents: cacheContents,
    		SystemInstruction: &genai.Content{
    			Parts: []*genai.Part{
    				{Text: systemInstruction},
    			},
    		},
    		DisplayName: "example-cache",
    		TTL:         time.Duration(time.Duration.Seconds(86400)),
    	}
    
    	res, err := client.Caches.Create(ctx, modelName, config)
    	if err != nil {
    		return "", fmt.Errorf("failed to create content cache: %w", err)
    	}
    
    	cachedContent, err := json.MarshalIndent(res, "", "  ")
    	if err != nil {
    		return "", fmt.Errorf("failed to marshal cache info: %w", err)
    	}
    
    	// See the documentation: https://pkg.go.dev/google.golang.org/genai#CachedContent
    	fmt.Fprintln(w, string(cachedContent))
    
    	// Example response:
    	// {
    	//   "name": "projects/111111111111/locations/us-central1/cachedContents/1111111111111111111",
    	//   "displayName": "example-cache",
    	//   "model": "projects/111111111111/locations/us-central1/publishers/google/models/gemini-2.5-flash",
    	//   "createTime": "2025-02-18T15:05:08.29468Z",
    	//   "updateTime": "2025-02-18T15:05:08.29468Z",
    	//   "expireTime": "2025-02-19T15:05:08.280828Z",
    	//   "usageMetadata": {
    	//     "imageCount": 167,
    	//     "textCount": 153,
    	//     "totalTokenCount": 43125
    	//   }
    	// }
    
    	return res.Name, nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.genai.Client;
    import com.google.genai.types.CachedContent;
    import com.google.genai.types.Content;
    import com.google.genai.types.CreateCachedContentConfig;
    import com.google.genai.types.HttpOptions;
    import com.google.genai.types.Part;
    import java.time.Duration;
    import java.util.Optional;
    
    public class ContentCacheCreateWithTextGcsPdf {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        contentCacheCreateWithTextGcsPdf(modelId);
      }
    
      // Creates a cached content using text and gcs pdfs files
      public static Optional<String> contentCacheCreateWithTextGcsPdf(String modelId) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("global")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1").build())
                .build()) {
    
          // Set the system instruction
          Content systemInstruction =
              Content.fromParts(
                  Part.fromText(
                      "You are an expert researcher. You always stick to the facts"
                          + " in the sources provided, and never make up new facts.\n"
                          + "Now look at these research papers, and answer the following questions."));
    
          // Set pdf files
          Content contents =
              Content.fromParts(
                  Part.fromUri(
                      "gs://cloud-samples-data/generative-ai/pdf/2312.11805v3.pdf", "application/pdf"),
                  Part.fromUri(
                      "gs://cloud-samples-data/generative-ai/pdf/2403.05530.pdf", "application/pdf"));
    
          // Configuration for cached content using pdfs files and text
          CreateCachedContentConfig config =
              CreateCachedContentConfig.builder()
                  .systemInstruction(systemInstruction)
                  .contents(contents)
                  .displayName("example-cache")
                  .ttl(Duration.ofSeconds(86400))
                  .build();
    
          CachedContent cachedContent = client.caches.create(modelId, config);
          cachedContent.name().ifPresent(System.out::println);
          cachedContent.usageMetadata().ifPresent(System.out::println);
          // Example response:
          // projects/111111111111/locations/global/cachedContents/1111111111111111111
          // CachedContentUsageMetadata{audioDurationSeconds=Optional.empty, imageCount=Optional[167],
          // textCount=Optional[153], totalTokenCount=Optional[43125],
          // videoDurationSeconds=Optional.empty}
          return cachedContent.name();
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {GoogleGenAI} = require('@google/genai');
    
    const GOOGLE_CLOUD_PROJECT = process.env.GOOGLE_CLOUD_PROJECT;
    const GOOGLE_CLOUD_LOCATION = process.env.GOOGLE_CLOUD_LOCATION || 'global';
    async function generateContentCache(
      projectId = GOOGLE_CLOUD_PROJECT,
      location = GOOGLE_CLOUD_LOCATION
    ) {
      const client = new GoogleGenAI({
        vertexai: true,
        project: projectId,
        location: location,
        httpOptions: {
          apiVersion: 'v1',
        },
      });
    
      const systemInstruction = `
      You are an expert researcher. You always stick to the facts in the sources provided, and never make up new facts.
      Now look at these research papers, and answer the following questions.
      `;
    
      const contents = [
        {
          role: 'user',
          parts: [
            {
              fileData: {
                fileUri:
                  'gs://cloud-samples-data/generative-ai/pdf/2312.11805v3.pdf',
                mimeType: 'application/pdf',
              },
            },
            {
              fileData: {
                fileUri: 'gs://cloud-samples-data/generative-ai/pdf/2403.05530.pdf',
                mimeType: 'application/pdf',
              },
            },
          ],
        },
      ];
    
      const contentCache = await client.caches.create({
        model: 'gemini-2.5-flash',
        config: {
          contents: contents,
          systemInstruction: systemInstruction,
          displayName: 'example-cache',
          ttl: '86400s',
        },
      });
    
      console.log(contentCache);
      console.log(contentCache.name);
    
      // Example response:
      //  projects/111111111111/locations/us-central1/cachedContents/1111111111111111111
      //  CachedContentUsageMetadata(audio_duration_seconds=None, image_count=167,
      //  text_count=153, total_token_count=43130, video_duration_seconds=None)
    
      return contentCache.name;
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import Content, CreateCachedContentConfig, HttpOptions, Part
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    
    system_instruction = """
    You are an expert researcher. You always stick to the facts in the sources provided, and never make up new facts.
    Now look at these research papers, and answer the following questions.
    """
    
    contents = [
        Content(
            role="user",
            parts=[
                Part.from_uri(
                    file_uri="gs://cloud-samples-data/generative-ai/pdf/2312.11805v3.pdf",
                    mime_type="application/pdf",
                ),
                Part.from_uri(
                    file_uri="gs://cloud-samples-data/generative-ai/pdf/2403.05530.pdf",
                    mime_type="application/pdf",
                ),
            ],
        )
    ]
    
    content_cache = client.caches.create(
        model="gemini-3.5-flash",
        config=CreateCachedContentConfig(
            contents=contents,
            system_instruction=system_instruction,
            # (Optional) For enhanced security, the content cache can be encrypted using a Cloud KMS key
            # kms_key_name = "projects/.../locations/.../keyRings/.../cryptoKeys/..."
            display_name="example-cache",
            ttl="86400s",
        ),
    )
    
    print(content_cache.name)
    print(content_cache.usage_metadata)
    # Example response:
    #   projects/111111111111/locations/.../cachedContents/1111111111111111111
    #   CachedContentUsageMetadata(audio_duration_seconds=None, image_count=167,
    #       text_count=153, total_token_count=43130, video_duration_seconds=None)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
