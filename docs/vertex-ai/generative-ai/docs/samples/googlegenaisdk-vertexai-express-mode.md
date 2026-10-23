---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-vertexai-express-mode/
title: Generate content using Vertex AI Express Mode \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:07.087135+00:00
---

# Generate content using Vertex AI Express Mode  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-vertexai-express-mode/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Generate content using Vertex AI Express Mode Stay organized with collections  Save and categorize content based on your preferences. 

This sample utilizes Vertex AI Express Mode to generate text content.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Gemini Enterprise Agent Platform in express mode overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/express-mode/overview)
  * [Google Gen AI SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/sdks/overview)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"google.golang.org/genai"
    )
    
    var newClient = genai.NewClient
    
    // generateContent shows how to use Vertex AI Express mode with an API key.
    func generateContentWithApiKey(w io.Writer) error {
    	ctx := context.Background()
    
    	// TODO(developer): Replace with your actual API key
    	apiKey := "YOUR_API_KEY"
    
    	client, err := newClient(ctx, &genai.ClientConfig{
    		APIKey:      apiKey,
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create genai client: %w", err)
    	}
    
    	modelName := "gemini-2.5-flash"
    	resp, err := client.Models.GenerateContent(ctx, modelName,
    		[]*genai.Content{
    			{Parts: []*genai.Part{
    				{Text: "Explain bubble sort to me."},
    			}, Role: genai.RoleUser},
    		},
    		nil,
    	)
    	if err != nil {
    		return fmt.Errorf("failed to generate content: %w", err)
    	}
    
    	fmt.Fprintln(w, resp.Text())
    
    	// Example response:
    	// Bubble Sort is a simple sorting algorithm that repeatedly steps through the list
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.genai.Client;
    import com.google.genai.types.GenerateContentConfig;
    import com.google.genai.types.GenerateContentResponse;
    
    public class ExpressModeWithApiKey {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        String apiKey = "YOUR_API_KEY";
        generateContent(modelId, apiKey);
      }
    
      // Generates content with Vertex AI Api key.
      public static String generateContent(String modelId, String apiKey) {
        // Client Initialization. Once created, it can be reused for multiple requests.
        try (Client client = Client.builder().apiKey(apiKey).vertexAI(true).build()) {
    
          GenerateContentResponse response =
              client.models.generateContent(
                  modelId, "Explain bubble sort to me.", GenerateContentConfig.builder().build());
    
          System.out.print(response.text());
          // Example response:
          // Bubble sort is one of the simplest sorting algorithms. It's often used to introduce the
          // concept of sorting because its logic is very straightforward.
          //
          // Imagine you have a list of numbers that you want to put in order, like `[5, 1, 4, 2, 8]`.
          // ...
          return response.text();
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {GoogleGenAI} = require('@google/genai');
    const API_KEY = 'YOUR_EXPRESS_MODE_API_KEY';
    
    async function generateWithApiKey(apiKey = API_KEY) {
      const client = new GoogleGenAI({
        vertexai: true,
        apiKey: apiKey,
      });
    
      const response = await client.models.generateContentStream({
        model: 'gemini-2.5-flash',
        contents: 'Explain bubble sort to me.',
      });
    
      console.log(response.text);
    
      // Example response:
      //  Bubble Sort is a simple sorting algorithm that repeatedly steps through the list
    
      return response;
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    
    # TODO(developer): Update below line
    API_KEY = "YOUR_API_KEY"
    
    client = genai.Client(vertexai=True, api_key=API_KEY)
    
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Explain bubble sort to me.",
    )
    
    print(response.text)
    # Example response:
    # Bubble Sort is a simple sorting algorithm that repeatedly steps through the list

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
