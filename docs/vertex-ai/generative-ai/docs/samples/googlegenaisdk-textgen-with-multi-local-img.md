---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-with-multi-local-img/
title: Generate text from multimodal prompt \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:06.169187+00:00
---

# Generate text from multimodal prompt  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-with-multi-local-img/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Generate text from multimodal prompt Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to generate text from a multimodal prompt using the Gemini model. The prompt consists of three images and two text prompts. The model generates a text response that describes the images and the text prompts.

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.GenAI;
    using Google.GenAI.Types;
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Threading.Tasks;
    
    public class TextGenWithMultiLocalImg
    {
        public async Task<string> GenerateContent(
            string projectId = "your-project-id",
            string location = "global",
            string model = "gemini-2.5-flash",
            string localImgFilePath1 = "path/to/img1.jpg",
            string localImgFilePath2 = "path/to/img2.jpg")
        {
            await using var client = new Client(
                project: projectId,
                location: location,
                vertexAI: true,
                httpOptions: new HttpOptions { ApiVersion = "v1" });
    
            // Read local images content.
            byte[] localImg1Bytes = File.ReadAllBytes(localImgFilePath1);
            byte[] localImg2Bytes = File.ReadAllBytes(localImgFilePath2);
    
            var contents = new List<Content>
            {
                new Content
                {
                    Role = "user",
                    Parts = new List<Part>
                    {
                        new Part { InlineData = new Blob { Data = localImg1Bytes, MimeType = "image/jpeg" } },
                        new Part { InlineData = new Blob { Data = localImg2Bytes, MimeType = "image/jpeg" } },
                        new Part { Text = "Generate a list of all the objects contained in both images." }
                    }
                }
            };
    
            GenerateContentResponse response = await client.Models.GenerateContentAsync(
                model: model,
                contents: contents);
    
            string responseText = response.Candidates[0].Content.Parts[0].Text;
            Console.WriteLine(responseText);
            // Example response:
            // Here are the objects contained in both images:
            // 1. **Coffee cup **: Both images feature coffee cups.
            // 2. **Baked goods **: Image 1 contains a slice of cake,
            // and Image 2 contains scones. Both fall under the category of baked goods.
            // ...
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
    	"os"
    
    	genai "google.golang.org/genai"
    )
    
    // generateWithMultiLocalImages shows how to generate text using multiple local image inputs.
    func generateWithMultiLocalImages(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := genai.NewClient(ctx, &genai.ClientConfig{
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create genai client: %w", err)
    	}
    
    	// Read local image files
    	image1, err := os.ReadFile("latte.jpg")
    	if err != nil {
    		return fmt.Errorf("failed to read image1: %w", err)
    	}
    	image2, err := os.ReadFile("scones.jpg")
    	if err != nil {
    		return fmt.Errorf("failed to read image2: %w", err)
    	}
    
    	modelName := "gemini-2.5-flash"
    	contents := []*genai.Content{
    		{
    			Role: "user",
    			Parts: []*genai.Part{
    				{Text: "Generate a list of all the objects contained in both images."},
    				{InlineData: &genai.Blob{
    					MIMEType: "image/jpeg",
    					Data:     image1,
    				}},
    				{InlineData: &genai.Blob{
    					MIMEType: "image/jpeg",
    					Data:     image2,
    				}},
    			},
    		},
    	}
    
    	// Call the model
    	resp, err := client.Models.GenerateContent(ctx, modelName, contents, nil)
    	if err != nil {
    		return fmt.Errorf("failed to generate content: %w", err)
    	}
    
    	fmt.Fprintln(w, resp.Text())
    
    	// Example response:
    	// Here is a list of all the distinct objects found in both images:
    	// 1.  **Coffee** (in mugs/cups; one is clearly a latte with heart art, others are also coffee/latte)
    	// 2.  **Mug(s)/Cup(s)** (yellow in the top image, white in the bottom image)
    	// 3.  **Cake** (sliced, in the top image)
    	// 4.  **Plate** (white, under the cake slice in the top image)
    	// 5.  **Fork** (partially visible on the plate in the top image)
    	// 6.  **Scones/Biscuits** (blueberry, in the bottom image)
    	// 7.  **Blueberries** (scattered and in a bowl in the bottom image)
    	// 8.  **Bowl** (small, dark, holding blueberries in the bottom image)
    	// 9.  **Spoon** (silver, with "LET'S JAM" inscription, in the bottom image)
    	// 10. **Flowers** (peonies, in the bottom image)
    	// 11. **Leaves** (green, possibly mint, in the bottom image)
    	// 12. **Paper** (parchment or wax paper, in the bottom image)
    	// 13. **Table/Surface** (wooden in the top image, textured/painted in the bottom image)
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
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    
    public class TextGenerationWithMultiLocalImage {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        String localImageFilePath1 = "your/local/img1.jpg";
        String localImageFilePath2 = "your/local/img2.jpg";
        generateContent(modelId, localImageFilePath1, localImageFilePath2);
      }
    
      // Generates text using multiple local images
      public static String generateContent(
          String modelId, String localImageFilePath1, String localImageFilePath2) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("global")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1").build())
                .build()) {
    
          // Read content from local files.
          byte[] localFileImg1Bytes = Files.readAllBytes(Paths.get(localImageFilePath1));
          byte[] localFileImg2Bytes = Files.readAllBytes(Paths.get(localImageFilePath2));
    
          GenerateContentResponse response =
              client.models.generateContent(
                  modelId,
                  Content.fromParts(
                      Part.fromBytes(localFileImg1Bytes, "image/jpeg"),
                      Part.fromBytes(localFileImg2Bytes, "image/jpeg"),
                      Part.fromText("Generate a list of all the objects contained in both images")),
                  null);
    
          System.out.print(response.text());
          // Example response:
          // Based on both images, here are the objects contained in both:
          //
          // 1.  **Coffee cups (or mugs)**: Both images feature one or more cups containing a beverage.
          // 2.  **Coffee (or a similar beverage)**: Both images contain a liquid beverage in the cups,
          // appearing to be coffee or a coffee-like drink.
          // 3.  **Table (or a flat surface)**: Both compositions are set on a flat surface, likely a
          // table or countertop.
          return response.text();
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {GoogleGenAI} = require('@google/genai');
    const fs = require('fs');
    
    const GOOGLE_CLOUD_PROJECT = process.env.GOOGLE_CLOUD_PROJECT;
    const GOOGLE_CLOUD_LOCATION = process.env.GOOGLE_CLOUD_LOCATION || 'global';
    
    function loadImageAsBase64(path) {
      const bytes = fs.readFileSync(path);
      return bytes.toString('base64');
    }
    
    async function generateContent(
      projectId = GOOGLE_CLOUD_PROJECT,
      location = GOOGLE_CLOUD_LOCATION,
      imagePath1,
      imagePath2
    ) {
      const client = new GoogleGenAI({
        vertexai: true,
        project: projectId,
        location: location,
      });
    
      // TODO(Developer): Update the below file paths to your images
      const image1 = loadImageAsBase64(imagePath1);
      const image2 = loadImageAsBase64(imagePath2);
    
      const response = await client.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: [
          {
            role: 'user',
            parts: [
              {
                text: 'Generate a list of all the objects contained in both images.',
              },
              {
                inlineData: {
                  data: image1,
                  mimeType: 'image/jpeg',
                },
              },
              {
                inlineData: {
                  data: image2,
                  mimeType: 'image/jpeg',
                },
              },
            ],
          },
        ],
      });
    
      console.log(response.text);
    
      // Example response:
      //  Okay, here's a jingle combining the elements of both sets of images, focusing on ...
      //  ...
    
      return response.text;
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import HttpOptions, Part
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    # TODO(Developer): Update the below file paths to your images
    # image_path_1 = "path/to/your/image1.jpg"
    # image_path_2 = "path/to/your/image2.jpg"
    with open(image_path_1, "rb") as f:
        image_1_bytes = f.read()
    with open(image_path_2, "rb") as f:
        image_2_bytes = f.read()
    
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[
            "Generate a list of all the objects contained in both images.",
            Part.from_bytes(data=image_1_bytes, mime_type="image/jpeg"),
            Part.from_bytes(data=image_2_bytes, mime_type="image/jpeg"),
        ],
    )
    print(response.text)
    # Example response:
    # Okay, here's a jingle combining the elements of both sets of images, focusing on ...
    # ...

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
