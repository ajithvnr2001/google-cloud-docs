---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-transcript-with-gcs-audio/
title: Transcript an audio file with Multimodal AI Model \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:29:59.420981+00:00
---

# Transcript an audio file with Multimodal AI Model  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-textgen-transcript-with-gcs-audio/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Transcript an audio file with Multimodal AI Model Stay organized with collections  Save and categorize content based on your preferences. 

This sample shows you how to use an audio file to generate a podcast transcript with timestamps.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Audio understanding (speech only)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/audio-understanding)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.GenAI;
    using Google.GenAI.Types;
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class TextGenTranscriptWithGcsAudio
    {
        public async Task<string> GenerateContent(
            string projectId = "your-project-id",
            string location = "global",
            string model = "gemini-2.5-flash")
        {
            await using var client = new Client(
                project: projectId,
                location: location,
                vertexAI: true);
    
            var prompt = @"
                Transcribe the interview, in the format of timecode, speaker, caption.
                Use speaker A, speaker B, etc. to identify speakers.";
    
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
                                FileUri = "gs://cloud-samples-data/generative-ai/audio/pixel.mp3",
                                MimeType = "audio/mpeg"
                            }
                        },
                        new Part { Text = prompt }
                    }
                }
            };
    
            GenerateContentResponse response = await client.Models.GenerateContentAsync(
                model: model,
                contents: contents,
                // Required to enable timestamp understanding for audio-only files
                config: new GenerateContentConfig { AudioTimestamp = true });
    
            string responseText = response.Candidates[0].Content.Parts[0].Text;
            Console.WriteLine(responseText);
            // Example response:
            // [00:00:00] Speaker A: your devices are getting better over time...
            // [00:00:14] Speaker B: Welcome to the Made by Google podcast...
            // ...
            // [10:18:24] Speaker B: Thank you for listening to the Made by Google podcast...
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
    
    // generateAudioTranscript shows how to generate an audio transcript.
    func generateAudioTranscript(w io.Writer) error {
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
    			{Text: `Transcribe the interview, in the format of timecode, speaker, caption.
    Use speaker A, speaker B, etc. to identify speakers.`},
    			{FileData: &genai.FileData{
    				FileURI:  "gs://cloud-samples-data/generative-ai/audio/pixel.mp3",
    				MIMEType: "audio/mpeg",
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
    	// 00:00:00, A: your devices are getting better over time.
    	// 00:01:13, A: And so we think about it across the entire portfolio from phones to watch, ...
    	// ...
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.genai.Client;
    import com.google.genai.types.Content;
    import com.google.genai.types.GenerateContentConfig;
    import com.google.genai.types.GenerateContentResponse;
    import com.google.genai.types.HttpOptions;
    import com.google.genai.types.Part;
    
    public class TextGenerationTranscriptWithGcsAudio {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        generateContent(modelId);
      }
    
      // Generates transcript with audio input
      public static String generateContent(String modelId) {
        // Client Initialization. Once created, it can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("global")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1").build())
                .build()) {
    
          String prompt =
              "Transcribe the interview, in the format of timecode, speaker, caption.\n"
                  + "Use speaker A, speaker B, etc. to identify speakers.";
    
          // Enable audioTimestamp to generate timestamps for audio-only files.
          GenerateContentConfig contentConfig =
              GenerateContentConfig.builder().audioTimestamp(true).build();
    
          GenerateContentResponse response =
              client.models.generateContent(
                  modelId,
                  Content.fromParts(
                      Part.fromUri(
                          "gs://cloud-samples-data/generative-ai/audio/pixel.mp3", "audio/mpeg"),
                      Part.fromText(prompt)),
                  contentConfig);
    
          System.out.print(response.text());
          // Example response:
          // 00:00 - Speaker A: your devices are getting better over time. And so we think about it...
          // 00:14 - Speaker B: Welcome to the Made by Google Podcast, where we meet the people who...
          // 00:41 - Speaker A: So many features. I am a singer, so I actually think recorder...
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
    
      const prompt = `Transcribe the interview, in the format of timecode, speaker, caption.
        Use speaker A, speaker B, etc. to identify speakers.`;
    
      const response = await client.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: [
          {text: prompt},
          {
            fileData: {
              fileUri: 'gs://cloud-samples-data/generative-ai/audio/pixel.mp3',
              mimeType: 'audio/mpeg',
            },
          },
        ],
        // Required to enable timestamp understanding for audio-only files
        config: {
          audioTimestamp: true,
        },
      });
    
      console.log(response.text);
    
      // Example response:
      // [00:00:00] **Speaker A:** your devices are getting better over time. And so ...
      // [00:00:14] **Speaker B:** Welcome to the Made by Google podcast where we meet ...
      // [00:00:20] **Speaker B:** Here's your host, Rasheed Finch.
      // [00:00:23] **Speaker C:** Today we're talking to Aisha Sharif and DeCarlos Love. ...
      // ...
    
      return response.text;
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import GenerateContentConfig, HttpOptions, Part
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    prompt = """
    Transcribe the interview, in the format of timecode, speaker, caption.
    Use speaker A, speaker B, etc. to identify speakers.
    """
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[
            prompt,
            Part.from_uri(
                file_uri="gs://cloud-samples-data/generative-ai/audio/pixel.mp3",
                mime_type="audio/mpeg",
            ),
        ],
        # Required to enable timestamp understanding for audio-only files
        config=GenerateContentConfig(audio_timestamp=True),
    )
    print(response.text)
    # Example response:
    # [00:00:00] **Speaker A:** your devices are getting better over time. And so ...
    # [00:00:14] **Speaker B:** Welcome to the Made by Google podcast where we meet ...
    # [00:00:20] **Speaker B:** Here's your host, Rasheed Finch.
    # [00:00:23] **Speaker C:** Today we're talking to Aisha Sharif and DeCarlos Love. ...
    # ...

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
