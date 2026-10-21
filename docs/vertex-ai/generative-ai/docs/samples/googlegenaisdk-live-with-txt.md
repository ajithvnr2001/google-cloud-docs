---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-live-with-txt/
title: Generate text with Gemini Live API \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:04.662215+00:00
---

# Generate text with Gemini Live API  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-live-with-txt/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Generate text with Gemini Live API Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to generate text using Gemini Live API

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Gemini Live API reference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/multimodal-live)



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
    
    // generateLiveWithText demonstrates using a live Gemini model
    // that performs live with text and handles responses.
    func generateLiveWithText(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := genai.NewClient(ctx, &genai.ClientConfig{
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create genai client: %w", err)
    	}
    
    	modelName := "gemini-2.0-flash-001"
    
    	config := &genai.LiveConnectConfig{
    		ResponseModalities: []genai.Modality{genai.ModalityText},
    	}
    
    	// Open a live session
    	session, err := client.Live.Connect(ctx, modelName, config)
    	if err != nil {
    		return fmt.Errorf("failed to connect live: %w", err)
    	}
    	defer session.Close()
    
    	// Prepare the input message
    	inputText := "Hello? Gemini, are you there?"
    	fmt.Fprintf(w, "> %s\n\n", inputText)
    
    	// Send text content to the model
    	err = session.SendClientContent(genai.LiveClientContentInput{
    		Turns: []*genai.Content{
    			{
    				Role: genai.RoleUser,
    				Parts: []*genai.Part{
    					{Text: inputText},
    				},
    			},
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to send content: %w", err)
    	}
    
    	// Stream the response
    	var response string
    	for {
    		chunk, err := session.Receive()
    		if err != nil {
    			if err == io.EOF {
    				break
    			}
    			return fmt.Errorf("error receiving response: %w", err)
    		}
    
    		if chunk.ServerContent != nil && chunk.ServerContent.ModelTurn != nil {
    			for _, part := range chunk.ServerContent.ModelTurn.Parts {
    				if part.Text != "" {
    					response += part.Text
    				}
    			}
    		}
    	}
    
    	// Example output:
    	//  >  Hello? Gemini are you there?
    	//  Yes, I'm here. What would you like to talk about?
    	fmt.Fprintln(w, response)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import static com.google.genai.types.Modality.Known.TEXT;
    
    import com.google.genai.AsyncSession;
    import com.google.genai.Client;
    import com.google.genai.types.Content;
    import com.google.genai.types.HttpOptions;
    import com.google.genai.types.LiveConnectConfig;
    import com.google.genai.types.LiveSendClientContentParameters;
    import com.google.genai.types.LiveServerContent;
    import com.google.genai.types.LiveServerMessage;
    import com.google.genai.types.Part;
    import java.util.concurrent.CompletableFuture;
    
    public class LiveWithTxt {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.0-flash-live-preview-04-09";
        generateContent(modelId);
      }
    
      // Shows how to send a text prompt and receive messages from the live session.
      public static String generateContent(String modelId) {
        // Client Initialization. Once created, it can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("us-central1")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1beta1").build())
                .build()) {
    
          // Connects to the live server.
          CompletableFuture<AsyncSession> sessionFuture =
              client.async.live.connect(
                  modelId, LiveConnectConfig.builder().responseModalities(TEXT).build());
    
          // Sends and receives messages from the live session.
          CompletableFuture<String> responseFuture =
              sessionFuture.thenCompose(
                  session -> {
                    // A future that completes when the model signals the end of its turn.
                    CompletableFuture<Void> turnComplete = new CompletableFuture<>();
                    // A variable to concatenate the text response from the model.
                    StringBuilder modelResponse = new StringBuilder();
                    // Starts receiving messages from the live session.
                    session.receive(
                        message -> handleLiveServerMessage(message, turnComplete, modelResponse));
                    // Sends content to the live session and waits for the turn to complete.
                    return sendContent(session)
                        .thenCompose(unused -> turnComplete)
                        .thenCompose(
                            unused -> session.close().thenApply(result -> modelResponse.toString()));
                  });
    
          String response = responseFuture.join();
          System.out.println(response);
          // Example output:
          // > Hello? Gemini, are you there?
          //
          // Yes, I am here. How can I help you today?
          return response;
        }
      }
    
      // Sends content to the live session.
      private static CompletableFuture<Void> sendContent(AsyncSession session) {
        String textInput = "Hello? Gemini, are you there?";
        System.out.printf("> %s\n", textInput);
        return session.sendClientContent(
            LiveSendClientContentParameters.builder()
                .turns(Content.builder().role("user").parts(Part.fromText(textInput)).build())
                .turnComplete(true)
                .build());
      }
    
      // Concatenates the output transcription from the model and signals
      // `turnComplete` when the model is done generating the response.
      private static void handleLiveServerMessage(
          LiveServerMessage message, CompletableFuture<Void> turnComplete, StringBuilder response) {
        message
            .serverContent()
            .flatMap(LiveServerContent::modelTurn)
            .flatMap(Content::parts)
            .ifPresent(parts -> parts.forEach(part -> part.text().ifPresent(response::append)));
        // Checks if the model's turn is over.
        if (message.serverContent().flatMap(LiveServerContent::turnComplete).orElse(false)) {
          turnComplete.complete(null);
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    'use strict';
    
    const {GoogleGenAI, Modality} = require('@google/genai');
    
    const GOOGLE_CLOUD_PROJECT = process.env.GOOGLE_CLOUD_PROJECT;
    const GOOGLE_CLOUD_LOCATION = process.env.GOOGLE_CLOUD_LOCATION || 'global';
    
    async function generateLiveConversation(
      projectId = GOOGLE_CLOUD_PROJECT,
      location = GOOGLE_CLOUD_LOCATION
    ) {
      const client = new GoogleGenAI({
        vertexai: true,
        project: projectId,
        location: location,
      });
    
      const modelId = 'gemini-2.0-flash-live-preview-04-09';
      const config = {responseModalities: [Modality.TEXT]};
    
      const responseQueue = [];
    
      async function waitMessage() {
        while (responseQueue.length === 0) {
          await new Promise(resolve => setTimeout(resolve, 100));
        }
        return responseQueue.shift();
      }
    
      async function handleTurn() {
        const turns = [];
        let done = false;
        while (!done) {
          const message = await waitMessage();
          turns.push(message);
          if (message.serverContent && message.serverContent.turnComplete) {
            done = true;
          }
        }
        return turns;
      }
    
      const session = await client.live.connect({
        model: modelId,
        config: config,
        callbacks: {
          onmessage: msg => responseQueue.push(msg),
          onerror: e => console.error('Error:', e.message),
        },
      });
    
      const textInput = 'Hello? Gemini, are you there?';
      console.log('> ', textInput, '\n');
    
      await session.sendClientContent({
        turns: [{role: 'user', parts: [{text: textInput}]}],
      });
    
      const turns = await handleTurn();
      for (const turn of turns) {
        if (turn.text) {
          console.log('Received text:', turn.text);
        }
      }
      // Example output:
      //> Hello? Gemini, are you there?
      // Received text: Yes
      // Received text: I'm here. How can I help you today?
      session.close();
      return turns;
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import (
        Content,
        HttpOptions,
        LiveConnectConfig,
        Modality,
        Part,
    )
    
    client = genai.Client(http_options=HttpOptions(api_version="v1beta1"))
    model_id = "gemini-live-2.5-flash-native-audio"
    
    async with client.aio.live.connect(
        model=model_id,
        config=LiveConnectConfig(response_modalities=[Modality.TEXT]),
    ) as session:
        text_input = "Hello? Gemini, are you there?"
        print("> ", text_input, "\n")
        await session.send_client_content(
            turns=Content(role="user", parts=[Part(text=text_input)])
        )
    
        response = []
    
        async for message in session.receive():
            if message.text:
                response.append(message.text)
    
        print("".join(response))
    # Example output:
    # >  Hello? Gemini, are you there?
    # Yes, I'm here. What would you like to talk about?

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
