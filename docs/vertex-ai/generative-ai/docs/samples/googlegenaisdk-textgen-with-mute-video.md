---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-with-mute-video/
title: Generate text from a video \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:38.724872+00:00
---

# Generate text from a video  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-with-mute-video/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Generate text from a video Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to use the Gemini API to generate text from a video

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.GenAI;
    using Google.GenAI.Types;
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class TextGenWithMuteVideo
    {
        public async Task<string> GenerateContent(
            string projectId = "your-project-id",
            string location = "global",
            string model = "gemini-2.5-flash")
        {
            await using var client = new Client(
                project: projectId,
                location: location,
                vertexAI: true,
                httpOptions: new HttpOptions { ApiVersion = "v1" });
    
            var contents = new List<Content>
            {
                new Content
                {
                    Role = "user",
                    Parts = new List<Part>
                    {
                        new Part
                        {
                            FileData = new FileData
                            {
                                FileUri = "gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4",
                                MimeType = "video/mp4"
                            }
                        },
                        new Part { Text = "What is in this video?"}
                    }
                }
            };
    
            GenerateContentResponse response = await client.Models.GenerateContentAsync(
                model: model,
                contents: contents);
    
            string responseText = response.Candidates[0].Content.Parts[0].Text;
            Console.WriteLine(responseText);
            // Example response:
            // This video shows an aerial view of people surfing in the ocean on a misty
            // or hazy day, with a distant coastline and mountains in the background...
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
    
    	genai "google.golang.org/genai"
    )
    
    // generateWithMuteVideo shows how to generate text using a video with no sound as the input.
    func generateWithMuteVideo(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := genai.NewClient(ctx, &genai.ClientConfig{
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create genai client: %w", err)
    	}
    
    	modelName := "gemini-2.5-flash"
    	contents := []*genai.Content{
    		{Parts: []*genai.Part{
    			{Text: "What is in the video?"},
    			{FileData: &genai.FileData{
    				FileURI:  "gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4",
    				MIMEType: "video/mp4",
    			}},
    		},
    			Role: genai.RoleUser},
    	}
    
    	resp, err := client.Models.GenerateContent(ctx, modelName, contents, nil)
    	if err != nil {
    		return fmt.Errorf("failed to generate content: %w", err)
    	}
    
    	respText := resp.Text()
    
    	fmt.Fprintln(w, respText)
    
    	// Example response:
    	// The video shows several surfers riding waves in an ocean setting. The waves are ...
    
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
    
    public class TextGenerationWithMuteVideo {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        generateContent(modelId);
      }
    
      // Generates text with mute video input
      public static String generateContent(String modelId) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("global")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1").build())
                .build()) {
    
          GenerateContentResponse response =
              client.models.generateContent(
                  modelId,
                  Content.fromParts(
                      Part.fromUri(
                          "gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4",
                          "video/mp4"),
                      Part.fromText("What is in this video?")),
                  null);
    
          System.out.print(response.text());
          // Example response:
          // This video features **surfers in the ocean**.
          //
          // The main focus is on **one individual who catches and rides a wave**, executing various
          // turns and maneuvers as the wave breaks and dissipates into whitewater...
          return response.text();
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {GoogleGenAI} = require('@google/genai');
    
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
    
      const response = await client.models.generateContent({
        model: 'gemini-2.5-flash-lite',
        contents: [
          {
            role: 'user',
            parts: [
              {
                fileData: {
                  mimeType: 'video/mp4',
                  fileUri:
                    'gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4',
                },
              },
              {
                text: 'What is in the video?',
              },
            ],
          },
        ],
        config: {
          mediaResolution: 'MEDIA_RESOLUTION_LOW',
        },
      });
    
      console.log(response.text);
    
      // Example response:
      // The video shows several people surfing in an ocean with a coastline in the background. The camera ...
    
      return response.text;
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import HttpOptions, Part
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[
            Part.from_uri(
                file_uri="gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4",
                mime_type="video/mp4",
            ),
            "What is in the video?",
        ],
    )
    print(response.text)
    # Example response:
    # The video shows several people surfing in an ocean with a coastline in the background. The camera ...

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
