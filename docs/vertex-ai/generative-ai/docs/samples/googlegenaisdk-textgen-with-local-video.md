---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-with-local-video/
title: Use Gemini to summarize local video file \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:29:55.408768+00:00
---

# Use Gemini to summarize local video file  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-with-local-video/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Use Gemini to summarize local video file Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to use Gemini to summarize a local video file.

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.GenAI;
    using Google.GenAI.Types;
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Threading.Tasks;
    
    public class TextGenWithLocalVideo
    {
        public async Task<string> GenerateContent(
            string projectId = "your-project-id",
            string location = "global",
            string model = "gemini-2.5-flash",
            string localVideoFilePath = "path/to/local_video.mp4")
        {
            await using var client = new Client(
                project: projectId,
                location: location,
                vertexAI: true,
                httpOptions: new HttpOptions { ApiVersion = "v1" });
    
            // Read local video content.
            byte[] videoBytes = File.ReadAllBytes(localVideoFilePath);
    
            var contents = new List<Content>
            {
                new Content
                {
                    Role = "user",
                    Parts = new List<Part>
                    {
                        new Part { InlineData = new Blob { Data = videoBytes, MimeType = "video/mp4" } },
                        new Part { Text = "Write a short and engaging blog post based on this video." }
                    }
                }
            };
    
            GenerateContentResponse response = await client.Models.GenerateContentAsync(
                model: model,
                contents: contents);
    
            string responseText = response.Candidates[0].Content.Parts[0].Text;
            Console.WriteLine(responseText);
            // Example response:
            // The Art of the Ascent: A Masterclass in Indoor Climbing
            // There's a certain raw beauty in the art of rock climbing,
            // and this video captures it perfectly.
            // ...
            return responseText;
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	genai "google.golang.org/genai"
    )
    
    // generateWithLocalVideo shows how to generate text using a local video input.
    func generateWithLocalVideo(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := genai.NewClient(ctx, &genai.ClientConfig{
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create genai client: %w", err)
    	}
    
    	// Read local video file content
    	data, err := os.ReadFile("describe_video_content.mp4")
    	if err != nil {
    		return fmt.Errorf("failed to read local video: %w", err)
    	}
    
    	modelName := "gemini-2.5-flash"
    	contents := []*genai.Content{
    		{
    			Role: "user",
    			Parts: []*genai.Part{
    				{Text: `Write a short and engaging blog post based on this video.`},
    				{InlineData: &genai.Blob{
    					MIMEType: "video/mp4",
    					Data:     data,
    				}},
    			},
    		},
    	}
    
    	resp, err := client.Models.GenerateContent(ctx, modelName, contents, nil)
    	if err != nil {
    		return fmt.Errorf("failed to generate content: %w", err)
    	}
    
    	respText := resp.Text()
    	fmt.Fprintln(w, respText)
    
    	// Example response:
    	// Finding Your Flow: The Focused Ascent
    	//
    	// Ever watched someone scale an indoor climbing wall and been captivated by their precision and power? This video perfectly captures that intense focus and calculated movement.
    	//
    	// Our climber isn't just pulling himself up; he's engaging in a dynamic dance with gravity. Every reach, every foot placement, every clip of the rope is a deliberate part of solving the route's puzzle. You can almost feel the concentration as his eyes scan for the next optimal hold, his muscles working in unison to propel him upwards.
    	//
    	// Indoor climbing....
    	// ...
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.genai.Client;
    import com.google.genai.types.Content;
    import com.google.genai.types.GenerateContentResponse;
    import com.google.genai.types.HttpOptions;
    import com.google.genai.types.Part;
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    
    public class TextGenerationWithLocalVideo {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        generateContent(modelId);
      }
    
      // Generates text with local video input
      public static String generateContent(String modelId) throws IOException {
        // Client Initialization. Once created, it can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("global")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1").build())
                .build()) {
    
          // Read content from the local video.
          byte[] videoData = Files.readAllBytes(Paths.get("resources/describe_video_content.mp4"));
    
          GenerateContentResponse response =
              client.models.generateContent(
                  modelId,
                  Content.fromParts(
                      Part.fromBytes(videoData, "video/mp4"),
                      Part.fromText("Write a short and engaging blog post based on this video.")),
                  null);
    
          System.out.print(response.text());
          // Example response:
          // More Than Just a Climb: Finding Your Flow on the Wall
          // There's something captivating about watching a climber in their element. This short clip
          // offers a perfect glimpse into the focused world of indoor climbing, where precision meets
          // power...
          return response.text();
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {GoogleGenAI} = require('@google/genai');
    const fs = require('fs');
    
    const GOOGLE_CLOUD_PROJECT = process.env.GOOGLE_CLOUD_PROJECT;
    const GOOGLE_CLOUD_LOCATION = process.env.GOOGLE_CLOUD_LOCATION || 'global';
    
    async function generateText(
      projectId = GOOGLE_CLOUD_PROJECT,
      location = GOOGLE_CLOUD_LOCATION
    ) {
      const client = new GoogleGenAI({
        vertexai: true,
        project: projectId,
        location: location,
      });
    
      const videoContent = fs.readFileSync('test-data/describe_video_content.mp4');
    
      const response = await client.models.generateContent({
        model: 'gemini-2.5-flash-lite',
        contents: [
          {
            inlineData: {
              data: videoContent.toString('base64'),
              mimeType: 'video/mp4',
            },
          },
          {text: 'Write a short and engaging blog post based on this video.'},
        ],
        config: {
          mediaResolution: 'MEDIA_RESOLUTION_LOW',
        },
      });
    
      console.log(response.text);
    
      // Example response:
      // Okay, here's a short and engaging blog post based on the climbing video:
      // **Title: Conquering the Wall: A Glimpse into the World of Indoor Climbing**
      // ...
    
      return response.text;
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import HttpOptions, Part
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    model_id = "gemini-3.5-flash"
    
    # Read local video file content
    with open("test_data/describe_video_content.mp4", "rb") as fp:
        # Video source: https://storage.googleapis.com/cloud-samples-data/generative-ai/video/describe_video_content.mp4
        video_content = fp.read()
    
    response = client.models.generate_content(
        model=model_id,
        contents=[
            Part.from_text(text="hello-world"),
            Part.from_bytes(data=video_content, mime_type="video/mp4"),
            "Write a short and engaging blog post based on this video.",
        ],
    )
    
    print(response.text)
    # Example response:
    # Okay, here's a short and engaging blog post based on the climbing video:
    # **Title: Conquering the Wall: A Glimpse into the World of Indoor Climbing**
    # ...

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
