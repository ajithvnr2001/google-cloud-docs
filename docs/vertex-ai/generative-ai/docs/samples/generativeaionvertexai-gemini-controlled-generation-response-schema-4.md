---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-controlled-generation-response-schema-4/
title: Controlled generation JSON output with enum \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:11.695901+00:00
---

# Controlled generation JSON output with enum  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-controlled-generation-response-schema-4/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Controlled generation JSON output with enum Stay organized with collections  Save and categorize content based on your preferences. 

Output JSON formatted object with an enum value, given a description of the object and a list of values to choose from.

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public async Task<string> GenerateContentWithResponseSchema4(
        string projectId = "your-project-id",
        string location = "us-central1",
        string publisher = "google",
        string model = "gemini-2.5-flash")
    {
    
        var predictionServiceClient = new PredictionServiceClientBuilder
        {
            Endpoint = $"{location}-aiplatform.googleapis.com"
        }.Build();
    
        var responseSchema = new OpenApiSchema
        {
            Type = Type.Array,
            Items = new()
            {
                Type = Type.Object,
                Properties =
                {
                    ["to_discard"] = new() { Type = Type.Integer },
                    ["subcategory"] = new() { Type = Type.String },
                    ["safe_handling"] = new() { Type = Type.Integer },
                    ["item_category"] = new()
                    {
                        Type = Type.String,
                        Enum =
                        {
                            "clothing",
                            "winter apparel",
                            "specialized apparel",
                            "furniture",
                            "decor",
                            "tableware",
                            "cookware",
                            "toys"
                        }
                    },
                    ["for_resale"] = new() { Type = Type.Integer },
                    ["condition"] = new()
                    {
                        Type = Type.String,
                        Enum =
                        {
                            "new in package",
                            "like new",
                            "gently used",
                            "used",
                            "damaged",
                            "soiled"
                        }
                    }
                }
            }
        };
    
        string prompt = @"
            Item description:
            The item is a long winter coat that has many tears all around the seams and is falling apart.
            It has large questionable stains on it.";
    
        var generateContentRequest = new GenerateContentRequest
        {
            Model = $"projects/{projectId}/locations/{location}/publishers/{publisher}/models/{model}",
            Contents =
            {
                new Content
                {
                    Role = "USER",
                    Parts =
                    {
                        new Part { Text = prompt }
                    }
                }
            },
            GenerationConfig = new GenerationConfig
            {
                ResponseMimeType = "application/json",
                ResponseSchema = responseSchema
            },
        };
    
        GenerateContentResponse response = await predictionServiceClient.GenerateContentAsync(generateContentRequest);
    
        string responseText = response.Candidates[0].Content.Parts[0].Text;
        Console.WriteLine(responseText);
    
        return responseText;
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
