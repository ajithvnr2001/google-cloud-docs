---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3/
title: Lyria 3 \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:07.599080+00:00
---

# Lyria 3  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Lyria 3 Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is a Generative AI Preview offering, subject to the "Pre-GA Offerings Terms" of the [ Google Cloud Service Specific Terms](https://cloud.google.com/terms/service-terms). For this Generative AI Preview offering, Customers may elect to use it for production or commercial purposes, or disclose Generated Output to third-parties, and may process personal data as outlined in the [ Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. 

Lyria is a music generation model from Google. This page documents the capabilities and features of Lyria 3.

## 3 Pro Preview

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/media/music) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Model ID | `lyria-3-pro-preview`  
---|---  
Modalities |  description  Text   
Input only  photo  Image   
Input only  mic  Audio   
Output only  videocam_off  Video   
Not supported   
Capabilities | 

  * [Text to music](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Image to music](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Vocal generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Instrumental mode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Lyrics generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [User-provided lyrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Negative prompting](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/music-gen-prompt-guide#negative-prompts)   
Not supported
  * [Song generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Full song  
Supported
  * [Detailed structure controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/music-gen-prompt-guide#detailed-structure)   
Duration, BPM, Intensity  
Supported
  * [Audio watermarking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Filtering](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Input, output (recitation), output (vocal likeness)  
Supported
  * [Prompt rewriter](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Content Credentials (C2PA)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/content-credentials)   
Supported

  
Technical specifications |  **Audio** mic | 

  * Maximum audio clip length: 184 seconds
  * Maximum number of clips per prompt: 1
  * Supported sample rates: 44.1 kHz
  * Supported bitrate: 192 kbps
  * Supported languages: English, German, Spanish, French, Hindi, Japanese, Korean, and Portuguese
  * Supported MIME types: `audio/mp3`

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * Global: `global`

  
Quotas | 

  * **Regional online prediction requests per minute per base model** : 10 tokens per minute

  
Versions | 

  * `lyria-3-pro-preview`
    * Launch stage: Preview
    * Release date: 2026-03-25

  
  
## 3 Clip Preview

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/media/music) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Model ID | `lyria-3-clip-preview`  
---|---  
Modalities |  description  Text   
Input only  photo  Image   
Input only  mic  Audio   
Output only  videocam_off  Video   
Not supported   
Capabilities | 

  * [Text to music](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Image to music](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Vocal generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Instrumental mode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Lyrics generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [User-provided lyrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Negative prompting](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/music-gen-prompt-guide#negative-prompts)   
Not supported
  * [Song generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
30 second clips  
Supported
  * [Detailed structure controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/music-gen-prompt-guide#detailed-structure)   
BPM, Intensity  
Supported
  * [Audio watermarking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Filtering](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Input, output (recitation), output (vocal likeness)  
Supported
  * [Prompt rewriter](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/generate-music)   
Supported
  * [Content Credentials (C2PA)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/content-credentials)   
Supported

  
Technical specifications |  **Audio** mic | 

  * Maximum audio clip length: 30 seconds
  * Maximum number of clips per prompt: 1
  * Supported sample rates: 44.1 kHz
  * Supported bitrate: 192 kbps
  * Supported languages: English, German, Spanish, French, Hindi, Japanese, Korean, and Portuguese
  * Supported MIME types: `audio/mp3`

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * Global: `global`

  
Quotas | 

  * **Regional online prediction requests per minute per base model** : 10 tokens per minute

  
Versions | 

  * `lyria-3-clip-preview`
    * Launch stage: Preview
    * Release date: 2026-03-25

  
  
For Lyria pricing information, see the [Lyria](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#lyria) section of the [Cost of building and deploying AI models in Vertex AI](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#lyria-models) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
