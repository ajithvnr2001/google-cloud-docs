---
url: https://docs.cloud.google.com/architecture/genai-podcasts-from-commentary/
title: Generative AI use case: Generate podcasts from audio files \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:05.096455+00:00
---

# Generative AI use case: Generate podcasts from audio files  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/genai-podcasts-from-commentary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Generative AI use case: Generate podcasts from audio files Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-12-12 UTC

This document provides a high-level architecture for an application that uses AI to generate podcasts based on audio input.

The intended audience for this document includes architects, developers, and administrators who build and manage generative AI applications in the cloud for the media and marketing industries. The document assumes that you have a foundational understanding of [generative AI](https://docs.cloud.google.com/docs/generative-ai/glossary#generative-ai).

The Deployment section of this document provides code samples for generative AI workloads that involve multi-modal input and output formats.

## Architecture

The following diagram shows an architecture for a podcast producer application in Google Cloud. The application uses AI to generate podcasts from audio files, such as live commentary for a sports event.

![Architecture for a generative AI application that generates podcasts from audio files.](https://docs.cloud.google.com/static/architecture/images/genai-podcasts-from-commentary-architecture.png)![Architecture for a generative AI application that generates podcasts from audio files.](https://docs.cloud.google.com/static/architecture/images/genai-podcasts-from-commentary-architecture.png)

The architecture shows the following flow:

  1. A user uploads audio files to a Cloud Storage bucket.
  2. Eventarc triggers a Cloud Run service.
  3. The Cloud Run service sends the audio files to Speech-to-Text.
  4. Speech-to-Text produces time-stamped transcripts of the audio files.
  5. The Cloud Run service sends the transcripts to Gemini API, with a prompt to generate a script for a podcast.

For example, the prompt could be to generate a script for a 15-minute podcast about the highlights of a sports event based on certain keywords in the commentary.

  6. Gemini generates a draft of a podcast script.

  7. The Cloud Run service sends the draft script to the user.

  8. The user reviews and edits the draft script and then sends the final script to Text-to-Speech.

  9. Text-to-Speech produces a podcast audio file.




## Products used

This example architecture uses the following Google Cloud products:

  * [ Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs/overview): An API that uses Google's speech recognition technologies to transcribe audio to text.
  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
  * [ Text-to-Speech](https://docs.cloud.google.com/text-to-speech/docs/basics): An API to create natural-sounding, synthetic human speech from text. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.
  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [ Eventarc](https://docs.cloud.google.com/eventarc/docs/overview): A serverless solution to asynchronously route messages triggered by events. 



## Deployment

To experiment with using Google Cloud products for workloads that involve multi-modal input and output formats such as audio and text, try the following code samples:

  * [Generate a transcript of an audio interview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/audio-understanding#audio_transcription).
  * [Generate a multi-speaker podcast by using Gemini and Text-to-Speech API](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/speech/use-cases/podcast/multi-speaker-podcast.ipynb).
  * [Record audio and generate a translation](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/audio/speech/sample-apps/live-translator).



## What's next

  * Explore more [generative AI architecture guides](https://docs.cloud.google.com/architecture/ai-ml#generative_ai).
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer

Other contributors: 

  * [Amina Mansour](https://www.linkedin.com/in/aminamansour/) | Tech Lead, Global Developer Relations & Strategic Content
  * [Megan O'Keefe](https://www.linkedin.com/in/askmeegs) | Developer Advocate
  * [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer
  * [Shir Meir Lador](https://www.linkedin.com/in/shirmeirlador) | Developer Relations Engineering Manager



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
