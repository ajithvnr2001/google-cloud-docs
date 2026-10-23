---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/arc/
title: AI Co-Builder: Arc \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:18.439550+00:00
---

# AI Co-Builder: Arc  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/arc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  AI Co-Builder: Arc Stay organized with collections  Save and categorize content based on your preferences. 

_AI Co-Builder: Arc_ (or just Arc) is a coding agent built directly in CX Agent Studio. It is equipped with all of the skills necessary to build agent applications:

  * Multi-agent architectures
  * Instructions
  * Tool implementations (for instance: OpenAPI tools and Python tools)
  * Callback implementations
  * Guardrails
  * Versions



To use Arc, click the **Arc** icon at the top of the agent builder, then provide your prompt to the agent.

## Uploading files

You can attach files to a message to give Arc more context: a product requirements document, a sample data file, details of external services that need to be called, or an archive of existing configuration.

Arc handles files in three ways, depending on the format:

How it is used | Formats | What happens  
---|---|---  
Read directly | PDF, PNG, JPG, JPEG, WAV, OGG | The file is provided to the model as-is.  
Read as text | TXT, MD, JSON, CSV, HTML, JS, XML, RTF, CSS | The file's text is added to your message. Only the first 262,144 characters are included; ask Arc to read further if the file is longer.  
Unpacked | ZIP | The archive is extracted and its text files become searchable. The archive itself is not sent to the model, and non-text entries inside it are listed but not read. To let Arc read a non-text file that is inside a ZIP archive (a PDF or an image, for example) upload that file directly instead.  
  
The following file limitations apply:

  * Up to 5 files per message
  * Maximum file size of 20 MB
  * Maximum ZIP archive size of 500 MB



Uploads go to a Cloud Storage bucket in your own project, named `PROJECT_ID-agent-assist-artifacts`, under the `agent-assist-uploads/` prefix. If the bucket does not exist, the console creates it the first time you upload a file, which requires the `storage.buckets.create permission`. Uploading requires `storage.objects.create`.

Uploaded files are deleted automatically 75 days after upload, under a lifecycle rule applied when the console creates the bucket. If the bucket already existed, its own lifecycle policy applies instead.

## Chain of thought

While processing, Arc provides its chain of thought in sections. You can expand any of these sections to get detail on the agent reasoning.

## Select context

Within the prompt dialog, you can click the **Select context** button, then add select items that Arc should use for additional context in your prompt. For example, you can click this button, followed by a particular agent in the agent builder, then ask Arc to explain the agent to you.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
