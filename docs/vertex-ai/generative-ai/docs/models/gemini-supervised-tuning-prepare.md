---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning-prepare/
title: Prepare supervised fine-tuning data for Gemini models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:11:23.166677+00:00
---

# Prepare supervised fine-tuning data for Gemini models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning-prepare/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Prepare supervised fine-tuning data for Gemini models Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to define a supervised fine-tuning dataset for a Gemini model. You can tune [text](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/text), [image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/image), [audio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/audio), [video](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/video), and [document](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/document) data types.

## About supervised fine-tuning datasets

A supervised fine-tuning dataset is used to fine-tune a pre-trained model to a specific task or domain. The input data should be similar to what you expect the model to encounter in real-world use. The output labels should represent the correct answers or outcomes for each input.

**Training dataset**

To tune a model, you provide a _training dataset_. For best results, we recommend that you start with 100 examples. You can scale up to thousands of examples if needed. The quality of the dataset is far more important than the quantity.

**Validation dataset**

We strongly recommend that you provide a validation dataset. A validation dataset helps you measure the effectiveness of a tuning job.

**Limitations**

For limitations on datasets, such as maximum input and output tokens, maximum validation dataset size, and maximum training dataset file size, see [About supervised fine-tuning for Gemini models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning#limitations).

### Dataset format

We support the following data formats:

  * [Multimodal dataset on Gemini Enterprise Agent Platform (preview)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/datasets).

  * [JSON Lines](https://jsonlines.org/) (JSONL) format, where each line contains a single tuning example. Before tuning your model, you must upload your dataset to a Cloud Storage bucket.




## Dataset example for Gemini
    
    
    {
      "systemInstruction": {
        "role": string,
        "parts": [
          {
            "text": string
          }
        ]
      },
      "contents": [
        {
          "role": string,
          "parts": [
            {
              // Union field data can be only one of the following:
              "text": string,
              "fileData": {
                "mimeType": string,
                "fileUri": string
              }
            }
          ]
        }
      ]
    }
    

### Parameters

The example contains data with the following parameters:

Parameters  
---  
`contents` | Required: `Content` The content of the current conversation with the model.For single-turn queries, this is a single instance. For multi-turn queries, this is a repeated field that contains conversation history and the latest request.  
`systemInstruction` | Optional: `Content`See [Supported models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning/use#supported_models).Instructions for the model to steer it toward better performance. For example, "Answer as concisely as possible" or "Don't use technical terms in your response".The `text` strings count toward the token limit.The `role` field of `systemInstruction` is ignored and doesn't affect the performance of the model.**Note:** Only `text` should be used in `parts` and content in each `part` should be in a separate paragraph.  
`tools` | Optional. A piece of code that enables the system to interact with external systems to perform an action, or set of actions, outside of knowledge and scope of the model. See [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/function-calling).  
  
### Contents

The base structured data type containing multi-part content of a message.

This class consists of two main properties: `role` and `parts`. The `role` property denotes the individual producing the content, while the `parts` property contains multiple elements, each representing a segment of data within a message.

Parameters  
---  
`role` | Optional: `string`The identity of the entity that creates the message. The following values are supported:

  * `user`: This indicates that the message is sent by a real person, typically a user-generated message.
  * `model`: This indicates that the message is generated by the model.

The `model` value is used to insert messages from the model into the conversation during multi-turn conversations.For non-multi-turn conversations, this field can be left blank or unset.  
`parts` | `part`A list of ordered parts that make up a single message. Different parts may have different [IANA MIME types](https://www.iana.org/assignments/media-types/media-types.xml).For limits on the inputs, such as the maximum number of tokens or the number of images, see the model specifications on the [Google models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models) page.To compute the number of tokens in your request, see [Get token count](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/get-token-count).  
  
### Parts

A data type containing media that is part of a multi-part `Content` message.

Parameters  
---  
`text` | Optional: `string` A text prompt or code snippet.  
`fileData` | Optional: `fileData`Data stored in a file.  
`functionCall` | Optional: `FunctionCall`.It contains a string representing the `FunctionDeclaration.name` field and a structured JSON object containing any parameters for the function call predicted by the model.See [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/function-calling).  
`functionResponse` | Optional: `FunctionResponse`.The result output of a `FunctionCall` that contains a string representing the `FunctionDeclaration.name` field and a structured JSON object containing any output from the function call. It is used as context to the model.See [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/function-calling).  
  
## Best practices

These sections outline best practices for preparing your supervised fine-tuning data.

### Maintain consistency with production data

The examples in your datasets should match your expected production traffic. If your dataset contains specific formatting, keywords, instructions, or information, the production data should be formatted in the same way and contain the same instructions.

For example, if the examples in your dataset include a `"question:"` and a `"context:"`, production traffic should also be formatted to include a `"question:"` and a `"context:"` in the same order as it appears in the dataset examples. If you exclude the context, the model won't recognize the pattern, even if the exact question was in an example in the dataset.

### Upload tuning datasets to Cloud Storage

To run a tuning job, you need to upload one or more datasets to a Cloud Storage bucket. You can either [create a new Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets#create_a_new_bucket) or use an existing one to store dataset files. The region of the bucket doesn't matter, but we recommend that you use a bucket that's in the same Google Cloud project where you plan to tune your model.

After your bucket is ready, [upload](https://docs.cloud.google.com/storage/docs/uploading-objects#uploading-an-object) your dataset file to the bucket.

### Follow the best practice of prompt design

Once you have your training dataset and you've trained the model, it's time to design prompts. It's important to follow the [best practice of prompt design](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies) in your training dataset to give detailed description of the task to be performed and how the output should look like.

## What's next

  * Choose a region to [tune a model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations).
  * To learn how supervised fine-tuning can be used in a solution that builds a generative AI knowledge base, see [Jump Start Solution: Generative AI knowledge base](https://docs.cloud.google.com/architecture/ai-ml/generative-ai-knowledge-base).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
