---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/lyria-music-generation/
title: Lyria API \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:15.282376+00:00
---

# Lyria API  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/lyria-music-generation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Lyria API Stay organized with collections  Save and categorize content based on your preferences. 

Lyria is a new foundation model for high-quality audio generation, capable of creating diverse soundscapes and musical pieces from text prompts. Lyria enables users to generate high-quality instrumental music from text prompts.

To explore this model in the console, see the Lyria model card in the Gemini Enterprise Agent Platform Model Garden (accessible using the Media Studio tab).

[ Try Lyria in the Agent Studio](https://console.cloud.google.com/agent-platform/studio/media/music)

[Try Lyria in a Colab](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/music/getting-started/lyria2_music_generation.ipynb)

## Supported Models

The Lyria API supports the following model:

  * `lyria-002`



## HTTP request
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      https://LOCATION[-aiplatform.googleapis.com/v1/projects/](https://-aiplatform.googleapis.com/v1/projects/)PROJECT_ID/locations/LOCATION/publishers/google/models/lyria-002:predict \
      -d '{
        "instances": [
          {
            "prompt": "string",
            "negative_prompt": "string", // Optional
            "seed": 0 // Optional. Cannot be used with sample_count.
          }
        ],
        "parameters": {
          "sample_count": 1 // Optional. Cannot be used with seed.
        }
      }'
    

Use the following parameters for the Lyria model. For more information, see the Lyria Model Garden card details.

Parameter  
---  
`prompt` (in `instances` object) |  `string` Required. The text description in US English (en-us) of the audio to generate.  Example: _"An energetic electronic dance track with a fast tempo."_  
`negative_prompt` (in `instances` object) |  `string` Optional. A description of what to exclude from the generated audio.  Example: _"vocals, slow tempo"_  
`seed` (in `instances` object) |  `integer` Optional. A seed for deterministic generation. If provided, the model will attempt to produce the same audio given the same prompt and other parameters.  Cannot be used with `sample_count` in the same request.  Example: `12345`  
`sample_count` (in `parameters` object) |  `integer` Optional. The number of audio samples to generate. Default is 1 if not specified and seed is not used.  Cannot be used with `seed` in the same request.  Example: `2`  
  
## Sample request

Use the following request to generate instrumental music from a text prompt:

### Text-to-music generation request

### curl
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/lyria-002:predict \
    -d '{
      "instances": [
        {
          "prompt": "A calm acoustic folk song with a gentle guitar melody and soft strings.",
          "negative_prompt": "drums, electric guitar",
          "seed": 98765
        }
      ],
      "parameters": {}
    }'
    

### JSON

This example uses `seed` for reproducible output.
    
    
    
    {
      "instances": [
        {
          "prompt": "A calm acoustic folk song with a gentle guitar melody and soft strings.",
          "negative_prompt": "drums, electric guitar",
          "seed": 98765
        }
      ],
      "parameters": {}
    }
    
    

### JSON with sample_count

This example uses `sample_count` to generate multiple samples.

To test a text prompt using the Lyria API, send a POST request to the publisher model endpoint. The following example omits `seed` from the `instances` object and uses `sample_count` in the `parameters` object to generate multiple samples. 
    
    
    
    {
      "instances": [
        {
          "prompt": "A calm acoustic folk song with a gentle guitar melody and soft strings.",
          "negative_prompt": "drums, electric guitar"
        }
      ],
      "parameters": {
        "sample_count": 2
      }
    }
    
    

## Response body

A successful request returns a JSON object containing the generated audio data. Each generated audio clip is 30 seconds long and provided as a WAV audio file at a 48kHz sample rate.
    
    
    {
      "predictions": [
        {
          "audioContent": "BASE64_ENCODED_WAV_STRING_SAMPLE_1",
          "mimeType": "audio/wav"
        }
        // Additional audio samples will be listed here if sample_count > 1
        // e.g.,
        //{"audioContent": "BASE64_ENCODED_WAV_STRING_SAMPLE_2",
        // "mimeType": "audio/wav"
        //}
      ],
      "deployedModelId": "xxxxxxxxxxxxxxx", // Actual ID may vary based on deployment
      "model": "projects/PROJECT_ID/locations/LOCATION/publishers/google/models/lyria-002",
      "modelDisplayName": "Lyria 2"
    }
    

Response element  
---  
`predictions` |  `array` An array of generated audio samples. Each object in the array represents one audio clip.  
`predictions[].audioContent` |  `string` Base64-encoded string of the generated WAV audio data.  
`predictions[].mimeType` |  `string` The MIME type of the audio data. For Lyria, this is `"audio/wav"`.  
`deployedModelId` |  `string` The ID of the deployed model that processed the request (if applicable for the endpoint type).  
`model` |  `string` The full resource name of the model that processed the request.  
`modelDisplayName` |  `string` The display name of the model.  
  
## Best practices and limitations

Refer to the Lyria Model Card for detailed best practices on prompting, language support (US English only for prompts), generation times, output format (WAV, 48 kHz, 30s instrumental clips), safety measures, and deployment information.

Key points:

  * **Detailed Prompts:** Generally lead to better audio.
  * **Specify:** Genre, mood, instrumentation, tempo.
  * **Negative Prompting:** Use `negative_prompt` to exclude elements.
  * **Output:** 30-second WAV audio clips, 48 kHz, instrumental only.
  * **Safety:** Content safety filters, recitation checking, artist intent checks, and SynthID watermarking are applied.



## Pricing

Lyria 2 usage is priced at $0.06 per 30 seconds of output music generated. For more details, see [generative AI pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing).

## More information

  * Learn more about [generative AI on Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/beginners-guide).
  * For an overview of Lyria, refer to its model card available in the Model Garden (Media Studio).



## What's next

  * Try out Lyria in the [Agent Studio](https://console.cloud.google.com/agent-platform/studio/media/music).
  * Review the [Google Cloud Terms of Service](https://cloud.google.com/terms).
  * Read the [Additional Terms for Generative AI Products](https://policies.google.com/terms/generative-ai).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
