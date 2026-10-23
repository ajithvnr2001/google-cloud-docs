---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-config-with-txt/
title: Configurations to generate content with Multimodal AI Model \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:25.349564+00:00
---

# Configurations to generate content with Multimodal AI Model  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-config-with-txt/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Configurations to generate content with Multimodal AI Model Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to provide user configurations to a Multimodal AI Model

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Content generation parameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/content-generation-parameters)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.GenAI;
    using Google.GenAI.Types;
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class TextGenConfigWithTxt
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
                contents: "Why is the sky blue?",
                // See the SDK documentation at
                // https://googleapis.github.io/dotnet-genai/api/Google.GenAI.Types.GenerateContentConfig.html
                config: new GenerateContentConfig
                {
                    Temperature = 0,
                    CandidateCount = 1,
                    ResponseMimeType = "application/json",
                    TopP = 0.95,
                    TopK = 20,
                    Seed = 5,
                    MaxOutputTokens = 500,
                    StopSequences = new List<string> { "STOP!" },
                    PresencePenalty = 0,
                    FrequencyPenalty = 0
                });
    
            string responseText = response.Candidates[0].Content.Parts[0].Text;
            Console.WriteLine(responseText);
            // Example response:
            // {
            //  "explanation": "The sky appears blue due to a phenomenon called Rayleigh scattering...
            // }
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
    
    // generateWithConfig shows how to generate text using a text prompt and custom configuration.
    func generateWithConfig(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := genai.NewClient(ctx, &genai.ClientConfig{
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create genai client: %w", err)
    	}
    
    	modelName := "gemini-2.5-flash"
    	contents := genai.Text("Why is the sky blue?")
    	// See the documentation: https://pkg.go.dev/google.golang.org/genai#GenerateContentConfig
    	config := &genai.GenerateContentConfig{
    		Temperature:      genai.Ptr(float32(0.0)),
    		CandidateCount:   int32(1),
    		ResponseMIMEType: "application/json",
    	}
    
    	resp, err := client.Models.GenerateContent(ctx, modelName, contents, config)
    	if err != nil {
    		return fmt.Errorf("failed to generate content: %w", err)
    	}
    
    	respText := resp.Text()
    
    	fmt.Fprintln(w, respText)
    	// Example response:
    	// {
    	//   "explanation": "The sky is blue due to a phenomenon called Rayleigh scattering ...
    	// }
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.genai.Client;
    import com.google.genai.types.GenerateContentConfig;
    import com.google.genai.types.GenerateContentResponse;
    import com.google.genai.types.HttpOptions;
    
    public class TextGenerationConfigWithText {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        generateContent(modelId);
      }
    
      // Generates text with text input and optional configurations
      public static String generateContent(String modelId) {
        // Client Initialization. Once created, it can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("global")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1").build())
                .build()) {
    
          // Set optional configuration parameters
          GenerateContentConfig contentConfig =
              GenerateContentConfig.builder()
                  .temperature(0.0F)
                  .candidateCount(1)
                  .responseMimeType("application/json")
                  .topP(0.95F)
                  .topK(20F)
                  .seed(5)
                  .maxOutputTokens(500)
                  .stopSequences("STOP!")
                  .presencePenalty(0.0F)
                  .frequencyPenalty(0.0F)
                  .build();
    
          // Generate content using optional configuration
          GenerateContentResponse response =
              client.models.generateContent(modelId, "Why is the sky blue?", contentConfig);
    
          System.out.print(response.text());
          // Example response:
          // {
          //  "explanation": "The sky appears blue due to a phenomenon called Rayleigh scattering.
          // Sunlight, which appears white, is actually composed of all the colors of the rainbow...
          // }
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
    
      const config = {
        temperature: 0,
        candidateCount: 1,
        responseMimeType: 'application/json',
        topP: 0.95,
        topK: 20,
        seed: 5,
        maxOutputTokens: 500,
        stopSequences: ['STOP!'],
        presencePenalty: 0.0,
        frequencyPenalty: 0.0,
      };
    
      const response = await client.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: 'Why is the sky blue?',
        config: config,
      });
    
      console.log(response.text);
    
      // Example response:
      // {
      //   "explanation": "The sky appears blue due to a phenomenon called Rayleigh scattering. When ...
      // }
    
      return response.text;
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import GenerateContentConfig, HttpOptions
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Why is the sky blue?",
        # See the SDK documentation at
        # https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentConfig
        config=GenerateContentConfig(
            temperature=0,
            candidate_count=1,
            response_mime_type="application/json",
            top_p=0.95,
            top_k=20,
            seed=5,
            max_output_tokens=500,
            stop_sequences=["STOP!"],
            presence_penalty=0.0,
            frequency_penalty=0.0,
        ),
    )
    print(response.text)
    # Example response:
    # {
    #   "explanation": "The sky appears blue due to a phenomenon called Rayleigh scattering. When ...
    # }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
