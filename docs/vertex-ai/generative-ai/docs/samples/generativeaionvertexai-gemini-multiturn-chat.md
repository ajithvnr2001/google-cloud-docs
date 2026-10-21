---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-multiturn-chat/
title: Interactive text generation with a chatbot \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:17.562223+00:00
---

# Interactive text generation with a chatbot  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-multiturn-chat/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Interactive text generation with a chatbot Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to use the Gemini model to generate text interactively.

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class MultiTurnChatSample
    {
        public async Task<string> GenerateContent(
            string projectId = "your-project-id",
            string location = "us-central1",
            string publisher = "google",
            string model = "gemini-2.5-flash"
        )
        {
            // Create a chat session to keep track of the context
            ChatSession chatSession = new ChatSession($"projects/{projectId}/locations/{location}/publishers/{publisher}/models/{model}", location);
    
            string prompt = "Hello.";
            Console.WriteLine($"\nUser: {prompt}");
    
            string response = await chatSession.SendMessageAsync(prompt);
            Console.WriteLine($"Response: {response}");
    
            prompt = "What are all the colors in a rainbow?";
            Console.WriteLine($"\nUser: {prompt}");
    
            response = await chatSession.SendMessageAsync(prompt);
            Console.WriteLine($"Response: {response}");
    
            prompt = "Why does it appear when it rains?";
            Console.WriteLine($"\nUser: {prompt}");
    
            response = await chatSession.SendMessageAsync(prompt);
            Console.WriteLine($"Response: {response}");
    
            return response;
        }
    
        private class ChatSession
        {
            private readonly string _modelPath;
            private readonly [PredictionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PredictionServiceClient.html) _predictionServiceClient;
    
            private readonly List<Content> _contents;
    
            public ChatSession(string modelPath, string location)
            {
                _modelPath = modelPath;
    
                _predictionServiceClient = new [PredictionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PredictionServiceClientBuilder.html)
                {
                    Endpoint = $"{location}-aiplatform.googleapis.com"
                }.Build();
    
                // Initialize contents to send over in every request.
                _contents = new List<Content>();
            }
    
            public async Task<string> SendMessageAsync(string prompt)
            {
                var content = new [Content](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Content.html)
                {
                    Role = "USER",
                    Parts =
                    {
                        new [Part](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Part.html) { Text = prompt }
                    }
                };
                _contents.Add(content);
    
                var generateContentRequest = new [GenerateContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateContentRequest.html)
                {
                    Model = _modelPath,
                    GenerationConfig = new [GenerationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerationConfig.html)
                    {
                        Temperature = 0.9f,
                        TopP = 1,
                        TopK = 32,
                        CandidateCount = 1,
                        MaxOutputTokens = 2048
                    }
                };
                generateContentRequest.Contents.AddRange(_contents);
    
                [GenerateContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateContentResponse.html) response = await _predictionServiceClient.[GenerateContentAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PredictionServiceClient.html#Google_Cloud_AIPlatform_V1_PredictionServiceClient_GenerateContentAsync_Google_Cloud_AIPlatform_V1_GenerateContentRequest_Google_Api_Gax_Grpc_CallSettings_)(generateContentRequest);
    
                _contents.Add(response.[Candidates](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateContentResponse.html#Google_Cloud_AIPlatform_V1_GenerateContentResponse_Candidates)[0].[Content](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Content.html));
    
                return response.[Candidates](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateContentResponse.html#Google_Cloud_AIPlatform_V1_GenerateContentResponse_Candidates)[0].[Content](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Content.html).Parts[0].Text;
            }
        }
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
