---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-with-pdf/
title: Process a PDF file with Gemini \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:08.144209+00:00
---

# Process a PDF file with Gemini  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-with-pdf/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Process a PDF file with Gemini Stay organized with collections  Save and categorize content based on your preferences. 

This sample shows you how to process a PDF document using Gemini.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Document understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/document-understanding)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.GenAI;
    using Google.GenAI.Types;
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class TextGenWithPdf
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
    
            string prompt = @"
                You are a highly skilled document summarization specialist.
                Your task is to provide a concise executive summary of no more than 300 words.
                Please summarize the given document for a general audience.";
    
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
                                FileUri = "gs://cloud-samples-data/generative-ai/pdf/1706.03762v7.pdf",
                                MimeType = "application/pdf",
                            }
                        },
                        new Part { Text = prompt }
                    }
                }
            };
    
            GenerateContentResponse response = await client.Models.GenerateContentAsync(model: model, contents: contents);
    
            string responseText = response.Candidates[0].Content.Parts[0].Text;
            Console.WriteLine(responseText);
            // Example response:
            // This paper introduces the Transformer, a novel neural network architecture designed
            // for processing sequences, such as those found in language translation. Traditionally,
            // such tasks have relied on complex recurrent or convolutional neural networks...
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
    
    // generateTextWithPDF shows how to generate text using a PDF file input.
    func generateTextWithPDF(w io.Writer) error {
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
    			{Text: `You are a highly skilled document summarization specialist.
    	Your task is to provide a concise executive summary of no more than 300 words.
    	Please summarize the given document for a general audience.`},
    			{FileData: &genai.FileData{
    				FileURI:  "gs://cloud-samples-data/generative-ai/pdf/1706.03762v7.pdf",
    				MIMEType: "application/pdf",
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
    	// "Attention Is All You Need" introduces the Transformer,
    	// a groundbreaking neural network architecture designed for...
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
    
    public class TextGenerationWithPdf {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        generateContent(modelId);
      }
    
      // Generates text with PDF file input
      public static String generateContent(String modelId) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("global")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1").build())
                .build()) {
    
          String prompt =
              "You are a highly skilled document summarization specialist.\n"
                  + " Your task is to provide a concise executive summary of no more than 300 words.\n"
                  + " Please summarize the given document for a general audience";
    
          GenerateContentResponse response =
              client.models.generateContent(
                  modelId,
                  Content.fromParts(
                      Part.fromUri(
                          "gs://cloud-samples-data/generative-ai/pdf/1706.03762v7.pdf",
                          "application/pdf"),
                      Part.fromText(prompt)),
                  null);
    
          System.out.print(response.text());
          // Example response:
          // The document introduces the Transformer, a novel neural network architecture designed for
          // sequence transduction tasks, such as machine translation. Unlike previous dominant models
          // that rely on complex recurrent or convolutional neural networks, the Transformer proposes a
          // simpler, more parallelizable design based *solely* on attention mechanisms, entirely
          // dispensing with recurrence and convolutions...
    
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
    
      const prompt = `You are a highly skilled document summarization specialist.
        Your task is to provide a concise executive summary of no more than 300 words.
        Please summarize the given document for a general audience.`;
    
      const pdfFile = {
        fileData: {
          fileUri: 'gs://cloud-samples-data/generative-ai/pdf/1706.03762v7.pdf',
          mimeType: 'application/pdf',
        },
      };
    
      const response = await client.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: [pdfFile, prompt],
      });
    
      console.log(response.text);
    
      // Example response:
      //  Here is a summary of the document in 300 words.
      //  The paper introduces the Transformer, a novel neural network architecture for
      //  sequence transduction tasks like machine translation. Unlike existing models that rely on recurrent or
      //  convolutional layers, the Transformer is based entirely on attention mechanisms.
      //  ...
    
      return response.text;
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import HttpOptions, Part
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    model_id = "gemini-3.5-flash"
    
    prompt = """
    You are a highly skilled document summarization specialist.
    Your task is to provide a concise executive summary of no more than 300 words.
    Please summarize the given document for a general audience.
    """
    
    pdf_file = Part.from_uri(
        file_uri="gs://cloud-samples-data/generative-ai/pdf/1706.03762v7.pdf",
        mime_type="application/pdf",
    )
    
    response = client.models.generate_content(
        model=model_id,
        contents=[pdf_file, prompt],
    )
    
    print(response.text)
    # Example response:
    # Here is a summary of the document in 300 words.
    #
    # The paper introduces the Transformer, a novel neural network architecture for
    # sequence transduction tasks like machine translation. Unlike existing models that rely on recurrent or
    # convolutional layers, the Transformer is based entirely on attention mechanisms.
    # ...

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
