---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-async-with-txt/
title: Async example to Generate content with Multimodal AI Model \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:25.961123+00:00
---

# Async example to Generate content with Multimodal AI Model  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-async-with-txt/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Async example to Generate content with Multimodal AI Model Stay organized with collections  Save and categorize content based on your preferences. 

The code sample demonstrates how to use Generative AI Models using async feature

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.GenAI;
    using Google.GenAI.Types;
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class TextGenAsyncWithTxt
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
    
            GenerateContentResponse response = await client.Models.GenerateContentAsync(
                model: model,
                contents: "Compose a song about the adventures of a time-traveling squirrel.",
                config: new GenerateContentConfig { ResponseModalities = new List<string> { "TEXT" } });
    
            string responseText = response.Candidates[0].Content.Parts[0].Text;
            Console.WriteLine(responseText);
            // Example response:
            // (Verse 1)
            // In an old oak tree, lived a squirrel named Scurry,
            // His life was quite normal, no reason to hurry.
            // Just burying nuts, and chattering loud...
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
    
    	"google.golang.org/genai"
    )
    
    // generateWithTextAsyncStream shows how to stream a text generation response.
    func generateWithTextAsyncStream(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := genai.NewClient(ctx, &genai.ClientConfig{
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create genai client: %w", err)
    	}
    
    	modelName := "gemini-2.5-flash"
    
    	contents := []*genai.Content{
    		{
    			Role: genai.RoleUser,
    			Parts: []*genai.Part{
    				{Text: "Compose a song about the adventures of a time-traveling squirrel."},
    			},
    		},
    	}
    
    	for resp, err := range client.Models.GenerateContentStream(ctx, modelName, contents, &genai.GenerateContentConfig{
    		ResponseModalities: []string{"TEXT"}}) {
    		if err != nil {
    			return fmt.Errorf("failed to generate content: %w", err)
    		}
    
    		chunk := resp.Text()
    
    		fmt.Fprintln(w, chunk)
    	}
    
    	// Example output (streamed piece by piece):
    	// (Verse 1)
    	// Pip was a squirrel, a regular chap,
    	//Burying acorns, enjoying a nap.
    	//One sunny morning, beneath the old pine,
    	//He dug up a thing, incredibly fine.
    	//A tiny contraption, with gears and a gleam,
    	//It pulsed with a power, a
    	// time-traveling dream.
    	//He nudged it with curiosity, twitching his nose,
    	//And *poof!* went the world, as everyone knows...
    	//
    	//(Chorus)
    	//Oh, Pip the squirrel, with his bushy brown tail,
    	//Through the time stream he'd often sail!
    	// ...
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.genai.Client;
    import com.google.genai.types.GenerateContentResponse;
    import com.google.genai.types.HttpOptions;
    import java.util.concurrent.CompletableFuture;
    
    public class TextGenerationAsyncWithText {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        generateContent(modelId);
      }
    
      // Generates text asynchronously with text input
      public static String generateContent(String modelId) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("global")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1").build())
                .build()) {
    
          CompletableFuture<GenerateContentResponse> asyncResponse =
              client.async.models.generateContent(
                  modelId, "Compose a song about the adventures of a time-traveling squirrel.", null);
    
          String response = asyncResponse.join().text();
          System.out.print(response);
          // Example response:
          // (Verse 1)
          // In an oak tree, so leafy and green,
          // Lived Squeaky the squirrel, a critter unseen.
          // Just burying nuts, a routine so grand,
          // ...
    
          return response;
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
        model: 'gemini-2.5-flash',
        contents:
          'Compose a song about the adventures of a time-traveling squirrel.',
        config: {
          responseMimeType: 'text/plain',
        },
      });
    
      console.log(response.text);
    
      // Example response:
      // (Verse 1)
      // Sammy the nugget, a furry little friend
      // Had a knack for adventure, beyond all comprehend
    
      return response.text;
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import GenerateContentConfig, HttpOptions
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    model_id = "gemini-3.5-flash"
    
    response = await client.aio.models.generate_content(
        model=model_id,
        contents="Compose a song about the adventures of a time-traveling squirrel.",
        config=GenerateContentConfig(
            response_modalities=["TEXT"],
        ),
    )
    
    print(response.text)
    # Example response:
    # (Verse 1)
    # Sammy the squirrel, a furry little friend
    # Had a knack for adventure, beyond all comprehend
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
