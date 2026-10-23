---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-grounding-with-vais/
title: Ground Gemini to a Vertex AI Search data store \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:50.773218+00:00
---

# Ground Gemini to a Vertex AI Search data store  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-grounding-with-vais/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Ground Gemini to a Vertex AI Search data store Stay organized with collections  Save and categorize content based on your preferences. 

Use this to ground Gemini output to your own data stored in a Vertex AI Search data store

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.html);
    using System;
    using System.Threading.Tasks;
    
    public class GroundingVertexAiSearchSample
    {
        public async Task<string> GenerateTextWithVertexAiSearch(
            string projectId = "your-project-id",
            string location = "us-central1",
            string publisher = "google",
            string model = "gemini-2.5-flash",
            string dataStoreLocation = "global",
            string dataStoreId = "your-datastore-id")
        {
            var predictionServiceClient = new [PredictionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PredictionServiceClientBuilder.html)
            {
                Endpoint = $"{location}-aiplatform.googleapis.com"
            }.Build();
    
            var generateContentRequest = new [GenerateContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateContentRequest.html)
            {
                Model = $"projects/{projectId}/locations/{location}/publishers/{publisher}/models/{model}",
                GenerationConfig = new [GenerationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerationConfig.html)
                {
                    Temperature = 0.0f
                },
                Contents =
                {
                    new [Content](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Content.html)
                    {
                        Role = "USER",
                        Parts = { new [Part](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Part.html) { Text = "How do I make an appointment to renew my driver's license?" } }
                    }
                },
                Tools =
                {
                    new [Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Tool.html)
                    {
                        Retrieval = new [Retrieval](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Retrieval.html)
                        {
                            VertexAiSearch = new [VertexAISearch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VertexAISearch.html)
                            {
                                Datastore = $"projects/{projectId}/locations/{dataStoreLocation}/collections/default_collection/dataStores/{dataStoreId}"
                            }
                        }
                    }
                }
            };
    
            [GenerateContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateContentResponse.html) response = await predictionServiceClient.GenerateContentAsync(generateContentRequest);
    
            string responseText = response.[Candidates](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenerateContentResponse.html#Google_Cloud_AIPlatform_V1_GenerateContentResponse_Candidates)[0].[Content](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Content.html).Parts[0].Text;
            Console.WriteLine(responseText);
    
            return responseText;
        }
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
