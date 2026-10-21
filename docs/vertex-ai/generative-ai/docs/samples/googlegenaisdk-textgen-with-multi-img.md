---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-with-multi-img/
title: Generate text using images from a local and Google Cloud Storage \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:05.423343+00:00
---

# Generate text using images from a local and Google Cloud Storage  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-with-multi-img/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Generate text using images from a local and Google Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This example demonstrates how to generate text using a local image and an image in Google Cloud Storage

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Image understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/image-understanding)



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
    
    public class TextGenWithMultiImg
    {
        public async Task<string> GenerateContent(
            string projectId = "your-project-id",
            string location = "global",
            string model = "gemini-2.5-flash",
            string localImageFilePath = "path/to/img.jpg")
        {
            await using var client = new Client(
                project: projectId,
                location: location,
                vertexAI: true,
                httpOptions: new HttpOptions { ApiVersion = "v1" });
    
            // Read local image content.
            byte[] localImgBytes = File.ReadAllBytes(localImageFilePath);
    
            // Image from GCS
            string gcsImageFilePath = "gs://cloud-samples-data/generative-ai/image/scones.jpg";
    
            var contents = new List<Content>
            {
                new Content
                {
                    Role = "user",
                    Parts = new List<Part>
                    {
                        new Part { FileData = new FileData { FileUri = gcsImageFilePath, MimeType = "image/jpeg" } },
                        new Part { InlineData = new Blob { Data = localImgBytes, MimeType = "image/jpeg" } },
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
            // The objects contained in both images are:
            // *Coffee
            // * Cups(or mugs)
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
    
    // generateWithMultiImg shows how to generate text using multiple image inputs.
    func generateWithMultiImg(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := genai.NewClient(ctx, &genai.ClientConfig{
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create genai client: %w", err)
    	}
    
    	// TODO(Developer): Update the path to file (image source:
    	//   https://storage.googleapis.com/cloud-samples-data/generative-ai/image/latte.jpg )
    	imageBytes, err := os.ReadFile("./latte.jpg")
    	if err != nil {
    		return fmt.Errorf("failed to read image: %w", err)
    	}
    
    	contents := []*genai.Content{
    		{Parts: []*genai.Part{
    			{Text: "Write an advertising jingle based on the items in both images."},
    			{FileData: &genai.FileData{
    				// Image source: https://storage.googleapis.com/cloud-samples-data/generative-ai/image/scones.jpg
    				FileURI:  "gs://cloud-samples-data/generative-ai/image/scones.jpg",
    				MIMEType: "image/jpeg",
    			}},
    			{InlineData: &genai.Blob{
    				Data:     imageBytes,
    				MIMEType: "image/jpeg",
    			}},
    		}},
    	}
    	modelName := "gemini-2.5-flash"
    
    	resp, err := client.Models.GenerateContent(ctx, modelName, contents, nil)
    	if err != nil {
    		return fmt.Errorf("failed to generate content: %w", err)
    	}
    
    	respText := resp.Text()
    
    	fmt.Fprintln(w, respText)
    
    	// Example response:
    	// Okay, here's an advertising jingle inspired by the blueberry scones, coffee, flowers, chocolate cake, and latte:
    	//
    	// (Upbeat, jazzy music)
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
    
    public class TextGenerationWithMultiImage {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        // Content from Google Cloud Storage
        String gcsFileImagePath = "gs://cloud-samples-data/generative-ai/image/scones.jpg";
        String localImageFilePath = "resources/latte.jpg";
        generateContent(modelId, gcsFileImagePath, localImageFilePath);
      }
    
      // Generates text with multiple images
      public static String generateContent(
          String modelId, String gcsFileImagePath, String localImageFilePath) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("global")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1").build())
                .build()) {
    
          // Read content from a local file.
          byte[] localFileImgBytes = Files.readAllBytes(Paths.get(localImageFilePath));
    
          GenerateContentResponse response =
              client.models.generateContent(
                  modelId,
                  Content.fromParts(
                      Part.fromText("Generate a list of all the objects contained in both images"),
                      Part.fromBytes(localFileImgBytes, "image/jpeg"),
                      Part.fromUri(gcsFileImagePath, "image/jpeg")),
                  null);
    
          System.out.print(response.text());
          // Example response:
          // Okay, here's the list of objects present in both images:
          //
          // **Image 1 (Scones):**
          //
          // *   Scones
          // *   Plate
          // *   Jam/Preserve
          // *   Cream/Butter
          // *   Table/Surface
          // *   Napkin/Cloth (possibly)
          //
          // **Image 2 (Latte):**
          //
          // *   Latte/Coffee cup
          // *   Saucer
          // *   Spoon
          // *   Table/Surface
          // *   Foam/Latte art
          //
          // **Objects potentially in both (depending on interpretation and specific items):**
          //
          // *   Plate/Saucer (both are serving dishes)
          // *   Table/Surface
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
    
      const image1 = {
        fileData: {
          fileUri: 'gs://cloud-samples-data/generative-ai/image/scones.jpg',
          mimeType: 'image/jpeg',
        },
      };
    
      const image2 = {
        fileData: {
          fileUri: 'gs://cloud-samples-data/generative-ai/image/fruit.png',
          mimeType: 'image/png',
        },
      };
    
      const response = await client.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: [
          image1,
          image2,
          'Generate a list of all the objects contained in both images.',
        ],
      });
    
      console.log(response.text);
    
      return response.text;
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import HttpOptions, Part
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    
    # Read content from GCS
    gcs_file_img_path = "gs://cloud-samples-data/generative-ai/image/scones.jpg"
    
    # Read content from a local file
    with open("test_data/latte.jpg", "rb") as f:
        local_file_img_bytes = f.read()
    
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[
            "Generate a list of all the objects contained in both images.",
            Part.from_uri(file_uri=gcs_file_img_path, mime_type="image/jpeg"),
            Part.from_bytes(data=local_file_img_bytes, mime_type="image/jpeg"),
        ],
    )
    print(response.text)
    # Example response:
    # Okay, here's the list of objects present in both images:
    # ...

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
