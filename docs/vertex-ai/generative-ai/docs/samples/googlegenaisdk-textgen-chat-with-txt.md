---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-chat-with-txt/
title: Create a chat session with a Generative Model \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:00.728341+00:00
---

# Create a chat session with a Generative Model  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-chat-with-txt/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Create a chat session with a Generative Model Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to use Generative Models to create a chat session.

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
    
    // generateChatWithText shows how to generate chat using a text prompt.
    func generateChatWithText(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := genai.NewClient(ctx, &genai.ClientConfig{
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create genai client: %w", err)
    	}
    	modelName := "gemini-2.5-flash"
    	history := []*genai.Content{
    		{
    			Role: genai.RoleUser,
    			Parts: []*genai.Part{
    				{Text: "Hello there"},
    			},
    		},
    		{
    			Role: "model",
    			Parts: []*genai.Part{
    				{Text: "Great to meet you. What would you like to know?"},
    			},
    		},
    	}
    	chatSession, err := client.Chats.Create(ctx, modelName, nil, history)
    	if err != nil {
    		return fmt.Errorf("failed to create genai chat session: %w", err)
    	}
    	contents := genai.Part{Text: "Tell me a story."}
    	resp, err := chatSession.SendMessage(ctx, contents)
    	if err != nil {
    		return fmt.Errorf("failed to send message: %w", err)
    	}
    
    	respText := resp.Text()
    
    	fmt.Fprintln(w, respText)
    	// Example response:
    	// Okay, settle in. Let me tell you a story about a quiet cartographer, but not of lands and seas.
    	// ...
    	// In the sleepy town of Oakhaven, nestled between the Whispering Hills and the Murmuring River, lived a woman named Elara.
    	// ...
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.genai.Chat;
    import com.google.genai.Client;
    import com.google.genai.types.Content;
    import com.google.genai.types.GenerateContentConfig;
    import com.google.genai.types.GenerateContentResponse;
    import com.google.genai.types.HttpOptions;
    import com.google.genai.types.Part;
    
    public class TextGenerationChatWithText {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        generateContent(modelId);
      }
    
      // Shows how to create a chat session
      public static String generateContent(String modelId) {
        // Client Initialization. Once created, it can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("global")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1").build())
                .build()) {
    
          // Create a new chat session
          Chat chatSession = client.chats.create(modelId);
    
          GenerateContentResponse response = chatSession.sendMessage("Tell me a story");
          System.out.print(response.text());
          // Example response:
          //
          // In the heart of the Whispering Peaks lay the Valley of Silent Echoes, a place perpetually
          // shrouded in a twilight mist. No birds sang there, no rivers flowed, and the few trees that
          // clung to its edges were gnarled and bare...
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
    
      const chatSession = client.chats.create({
        model: 'gemini-2.5-flash',
        history: [
          {
            role: 'user',
            parts: [{text: 'Hello'}],
          },
          {
            role: 'model',
            parts: [{text: 'Great to meet you. What would you like to know?'}],
          },
        ],
      });
    
      const response = await chatSession.sendMessage({message: 'Tell me a story.'});
      console.log(response.text);
    
      // Example response:
      // Okay, here's a story for you:
      // ...
    
      return response.text;
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import HttpOptions, ModelContent, Part, UserContent
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    chat_session = client.chats.create(
        model="gemini-3.5-flash",
        history=[
            UserContent(parts=[Part(text="Hello")]),
            ModelContent(
                parts=[Part(text="Great to meet you. What would you like to know?")],
            ),
        ],
    )
    response = chat_session.send_message("Tell me a story.")
    print(response.text)
    # Example response:
    # Okay, here's a story for you:
    # ...

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
