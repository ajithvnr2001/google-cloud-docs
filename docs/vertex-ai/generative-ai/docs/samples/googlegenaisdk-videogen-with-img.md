---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-videogen-with-img/
title: Generate Videos from Images using Veo \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:53.670556+00:00
---

# Generate Videos from Images using Veo  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-videogen-with-img/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Generate Videos from Images using Veo Stay organized with collections  Save and categorize content based on your preferences. 

Create videos from images, using Veo , a generative AI model for video generation.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Generate videos from an image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-an-image)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"google.golang.org/genai"
    )
    
    // generateVideoFromImage shows how to gen video from img.
    func generateVideoFromImage(w io.Writer, outputGCSURI string) error {
    	//outputGCSURI = "gs://your-bucket/your-prefix"
    	ctx := context.Background()
    
    	client, err := genai.NewClient(ctx, &genai.ClientConfig{
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create genai client: %w", err)
    	}
    
    	image := &genai.Image{
    		GCSURI:   "gs://cloud-samples-data/generative-ai/image/flowers.png",
    		MIMEType: "image/png",
    	}
    
    	config := &genai.GenerateVideosConfig{
    		AspectRatio:  "16:9",
    		OutputGCSURI: outputGCSURI,
    	}
    
    	modelName := "veo-3.0-generate-preview"
    	prompt := "Extreme close-up of a cluster of vibrant wildflowers swaying gently in a sun-drenched meadow."
    	operation, err := client.Models.GenerateVideos(ctx, modelName, prompt, image, config)
    	if err != nil {
    		return fmt.Errorf("failed to start video generation: %w", err)
    	}
    
    	// Polling until the operation is done
    	for !operation.Done {
    		time.Sleep(15 * time.Second)
    		operation, err = client.Operations.GetVideosOperation(ctx, operation, nil)
    		if err != nil {
    			return fmt.Errorf("failed to get operation status: %w", err)
    		}
    	}
    
    	if operation.Response != nil && len(operation.Response.GeneratedVideos) > 0 {
    		videoURI := operation.Response.GeneratedVideos[0].Video.URI
    		fmt.Fprintln(w, videoURI)
    		return nil
    	}
    
    	// Example response:
    	// gs://your-bucket/your-prefix/videoURI
    
    	return fmt.Errorf("video generation failed or returned no results")
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.genai.Client;
    import com.google.genai.types.GenerateVideosConfig;
    import com.google.genai.types.GenerateVideosOperation;
    import com.google.genai.types.GenerateVideosResponse;
    import com.google.genai.types.GeneratedVideo;
    import com.google.genai.types.GetOperationConfig;
    import com.google.genai.types.Image;
    import com.google.genai.types.Video;
    import java.util.concurrent.TimeUnit;
    
    public class VideoGenWithImg {
    
      public static void main(String[] args) throws InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "veo-3.1-generate-001";
        String outputGcsUri = "gs://your-bucket/your-prefix";
        generateContent(modelId, outputGcsUri);
      }
    
      // Generates a video with an image and a text prompt.
      public static String generateContent(String modelId, String outputGcsUri)
          throws InterruptedException {
        // Client Initialization. Once created, it can be reused for multiple requests.
        try (Client client = Client.builder().location("global").vertexAI(true).build()) {
    
          GenerateVideosOperation operation =
              client.models.generateVideos(
                  modelId,
                  "Extreme close-up of a cluster of vibrant wildflowers"
                      + " swaying gently in a sun-drenched meadow.",
                  Image.builder()
                      .gcsUri("gs://cloud-samples-data/generative-ai/image/flowers.png")
                      .mimeType("image/png")
                      .build(),
                  GenerateVideosConfig.builder()
                      .aspectRatio("16:9")
                      .outputGcsUri(outputGcsUri)
                      .build());
    
          while (!operation.done().orElse(false)) {
            TimeUnit.SECONDS.sleep(15);
            operation =
                client.operations.getVideosOperation(operation, GetOperationConfig.builder().build());
          }
    
          String generatedVideoUri =
              operation
                  .response()
                  .flatMap(GenerateVideosResponse::generatedVideos)
                  .flatMap(videos -> videos.stream().findFirst())
                  .flatMap(GeneratedVideo::video)
                  .flatMap(Video::uri)
                  .orElseThrow(
                      () ->
                          new IllegalStateException(
                              "Could not get the URI from the generated video"));
    
          System.out.println("Generated video URI: " + generatedVideoUri);
          // Example response:
          // Generated video URI: gs://your-bucket/your-prefix/generated-video-123.mp4
          return generatedVideoUri;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {GoogleGenAI} = require('@google/genai');
    
    const GOOGLE_CLOUD_PROJECT = process.env.GOOGLE_CLOUD_PROJECT;
    const GOOGLE_CLOUD_LOCATION = process.env.GOOGLE_CLOUD_LOCATION || 'global';
    
    async function generateVideo(
      outputGcsUri,
      projectId = GOOGLE_CLOUD_PROJECT,
      location = GOOGLE_CLOUD_LOCATION
    ) {
      const client = new GoogleGenAI({
        vertexai: true,
        project: projectId,
        location: location,
      });
    
      let operation = await client.models.generateVideos({
        model: 'veo-3.1-fast-generate-001',
        prompt:
          'Extreme close-up of a cluster of vibrant wildflowers swaying gently in a sun-drenched meadow',
        image: {
          gcsUri: 'gs://cloud-samples-data/generative-ai/image/flowers.png',
          mimeType: 'image/png',
        },
        config: {
          aspectRatio: '16:9',
          outputGcsUri: outputGcsUri,
        },
      });
    
      while (!operation.done) {
        await new Promise(resolve => setTimeout(resolve, 15000));
        operation = await client.operations.get({operation: operation});
        console.log(operation);
      }
    
      if (operation.response) {
        console.log(operation.response.generatedVideos[0].video.uri);
      }
      return operation;
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    from google import genai
    from google.genai.types import GenerateVideosConfig, Image
    
    client = genai.Client()
    
    # TODO(developer): Update and un-comment below line
    # output_gcs_uri = "gs://your-bucket/your-prefix"
    
    operation = client.models.generate_videos(
        model="veo-3.1-generate-001",
        prompt="Extreme close-up of a cluster of vibrant wildflowers swaying gently in a sun-drenched meadow.",
        image=Image(
            gcs_uri="gs://cloud-samples-data/generative-ai/image/flowers.png",
            mime_type="image/png",
        ),
        config=GenerateVideosConfig(
            aspect_ratio="16:9",
            output_gcs_uri=output_gcs_uri,
        ),
    )
    
    while not operation.done:
        time.sleep(15)
        operation = client.operations.get(operation)
        print(operation)
    
    if operation.response:
        print(operation.result.generated_videos[0].video.uri)
    
    # Example response:
    # gs://your-bucket/your-prefix

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
