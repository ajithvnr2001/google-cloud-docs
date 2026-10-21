---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-with-video/
title: Summarize a video file with audio with Gemini Multimodal \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:29:59.092550+00:00
---

# Summarize a video file with audio with Gemini Multimodal  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-with-video/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Summarize a video file with audio with Gemini Multimodal Stay organized with collections  Save and categorize content based on your preferences. 

This sample shows you how to summarize a video file with audio and return chapters with timestamps.

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.GenAI;
    using Google.GenAI.Types;
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class TextGenWithVideo
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
    
            string prompt = "Analyze the provided video file, including its audio. " +
                "Summarize the main points of the video concisely. " +
                "Create a chapter breakdown with timestamps for key sections or topics discussed.";
    
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
                                FileUri = "gs://cloud-samples-data/generative-ai/video/pixel8.mp4",
                                MimeType = "video/mp4"
                            }
                        },
                        new Part { Text = prompt }
                    }
                }
            };
    
            GenerateContentResponse response = await client.Models.GenerateContentAsync(
                model: model,
                contents: contents);
    
            string responseText = response.Candidates[0].Content.Parts[0].Text;
            Console.WriteLine(responseText);
            // Example response:
            // This video features Saeka Shimada, a Tokyo photographer, as she explores the city's vibrant nightlife
            // using the new Google Pixel. She highlights the phone's "Video Boost" feature, which leverages
            // "Night Sight" for superior low-light video quality...
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
    
    // generateWithVideo shows how to generate text using a video input.
    func generateWithVideo(w io.Writer) error {
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
    			{Text: `Analyze the provided video file, including its audio.
    Summarize the main points of the video concisely.
    Create a chapter breakdown with timestamps for key sections or topics discussed.`},
    			{FileData: &genai.FileData{
    				FileURI:  "gs://cloud-samples-data/generative-ai/video/pixel8.mp4",
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
    	// Here's an analysis of the provided video file:
    	//
    	// **Summary**
    	//
    	// The video features Saeka Shimada, a photographer in Tokyo, who uses the new Pixel phone ...
    	//
    	// **Chapter Breakdown**
    	//
    	// *   **0:00-0:05**: Introduction to Saeka Shimada and her work as a photographer in Tokyo.
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
    
    public class TextGenerationWithVideo {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        String prompt =
            " Analyze the provided video file, including its audio.\n"
                + " Summarize the main points of the video concisely.\n"
                + " Create a chapter breakdown with timestamps for key sections or topics discussed.";
        generateContent(modelId, prompt);
      }
    
      // Generates text with video input
      public static String generateContent(String modelId, String prompt) {
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
                      Part.fromText(prompt),
                      Part.fromUri(
                          "gs://cloud-samples-data/generative-ai/video/pixel8.mp4", "video/mp4")),
                  null);
    
          System.out.print(response.text());
          // Example response:
          // Here's a breakdown of the video:
          //
          // **Summary:**
          //
          // Saeka Shimada, a photographer in Tokyo, uses the Google Pixel 8 Pro's "Video Boost" feature
          // to ...
          //
          // **Chapter Breakdown with Timestamps:**
          //
          // * **[00:00-00:12] Introduction & Tokyo at Night:** Saeka Shimada introduces herself ...
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
    
    async function generateContent(
      projectId = GOOGLE_CLOUD_PROJECT,
      location = GOOGLE_CLOUD_LOCATION
    ) {
      const client = new GoogleGenAI({
        vertexai: true,
        project: projectId,
        location: location,
      });
    
      const prompt = `
      Analyze the provided video file, including its audio.
      Summarize the main points of the video concisely.
      Create a chapter breakdown with timestamps for key sections or topics discussed.
     `;
    
      const video = {
        fileData: {
          fileUri: 'gs://cloud-samples-data/generative-ai/video/pixel8.mp4',
          mimeType: 'video/mp4',
        },
      };
    
      const response = await client.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: [video, prompt],
        config: {
          mediaResolution: 'MEDIA_RESOLUTION_LOW',
        },
      });
    
      console.log(response.text);
    
      return response.text;
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import HttpOptions, Part
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    prompt = """
    Analyze the provided video file, including its audio.
    Summarize the main points of the video concisely.
    Create a chapter breakdown with timestamps for key sections or topics discussed.
    """
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[
            Part.from_uri(
                file_uri="gs://cloud-samples-data/generative-ai/video/pixel8.mp4",
                mime_type="video/mp4",
            ),
            prompt,
        ],
    )
    
    print(response.text)
    # Example response:
    # Here's a breakdown of the video:
    #
    # **Summary:**
    #
    # Saeka Shimada, a photographer in Tokyo, uses the Google Pixel 8 Pro's "Video Boost" feature to ...
    #
    # **Chapter Breakdown with Timestamps:**
    #
    # * **[00:00-00:12] Introduction & Tokyo at Night:** Saeka Shimada introduces herself ...
    # ...

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
