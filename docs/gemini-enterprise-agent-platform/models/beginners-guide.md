---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/beginners-guide/
title: Generative AI beginner's guide \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:38:43.690359+00:00
---

# Generative AI beginner's guide  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/beginners-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Generative AI beginner's guide Stay organized with collections  Save and categorize content based on your preferences. 

This beginner's guide introduces you to the core technologies of generative AI and explains how they fit together to power chatbots and applications. Generative AI (also known as _genAI_ or _gen AI_) is a field of machine learning (ML) that develops and uses ML models for generating new content.

Generative AI models are often called large language models (LLMs) because of their large size and ability to understand and generate natural language. However, depending on the data that the models are trained on, these models can understand and generate content from multiple modalities, including text, images, videos, and audio. Models that work with multiple modalities of data are called _multimodal_ models.

Google provides the [Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models) family of generative AI models designed for _multimodal_ use cases; capable of processing information from multiple modalities, including images, videos, and text.

## Content generation

In order for generative AI models to generate content that's useful in real-world applications, they need to have the following capabilities:

  * **Learn how to perform new tasks:**

Generative AI models are designed to perform general tasks. If you want a model to perform tasks that are unique to your use case, then you need to be able to customize the model. On Gemini Enterprise Agent Platform, you can customize your model through model tuning.

  * **Access external information:**

Generative AI models are trained on vast amounts of data. However, in order for these models to be useful, they need to be able to access information outside of their training data. For example, if you want to create a customer service chatbot that's powered by a generative AI model, the model needs to have access to information about the products and services that you offer. In Gemini Enterprise Agent Platform, you use the grounding and function calling features to help the model access external information.

  * **Block harmful content:**

Generative AI models might generate output that you don't expect, including text that's offensive or insensitive. To maintain safety and prevent misuse, the models need safety filters to block prompts and responses that are determined to be potentially harmful. Gemini Enterprise Agent Platform has built-in safety features that promote the responsible use of our generative AI services.




### Prompt

![Prompt](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/models/images/icons/prompt.svg) |  The generative AI workflow typically starts with prompting. A prompt is a natural language request sent to a generative AI model to elicit a response back. Depending on the model, a prompt can contain _text_ , _images_ , _videos_ , _audio_ , _documents_ , and other modalities or even multiple modalities (multimodal).  Creating a prompt to get the desired response from the model is a practice called [prompt design](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/introduction-prompt-design). While prompt design is a process of trial and error, there are prompt design principles and strategies that you can use to nudge the model to behave in the desired way. [ Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/quickstart) offers a prompt management tool to help you manage your prompts. 

### Foundation models

|  ![Foundation models](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/models/images/icons/model.svg) |  Prompts are sent to a generative AI model for response generation. Gemini Enterprise Agent Platform has a variety of [generative AI foundation models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models) that are accessible through a managed API, including the following: 

  * **Gemini API:** Advanced reasoning, multiturn chat, code generation, and multimodal prompts.

The models differ in size, modality, and cost. You can explore Google models, as well as open models and models from Google partners, in [Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models). 

### Model customization

|  ![Model customization](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/models/images/icons/tune.svg) |  You can customize the default behavior of Google's foundation models so that they consistently generate the desired results without using complex prompts. This customization process is called [model tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tune-models). Model tuning helps you reduce the cost and latency of your requests by allowing you to simplify your prompts.  Gemini Enterprise Agent Platform also offers [model evaluation tools](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview) to help you evaluate the performance of your tuned model. After your tuned model is production-ready, you can [deploy it to an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/overview) and monitor performance like in standard MLOps workflows. 

### Access external information

|  ![Augmentation](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/models/images/icons/ground.svg) |  Gemini Enterprise Agent Platform offers multiple ways to give the model access to external APIs and real-time information. 

  * **[Grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview):** Connects model responses to a source of truth, such as your own data or web search, helping to reduce hallucinations.
  * **[RAG](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview):** Connects models to external knowledge sources, such as documents and databases, to generate more accurate and informative responses.
  * **[Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/function-calling):** Lets the model interact with external APIs to get real-time information and perform real-world tasks. 



### Citation check

|  ![Citation check](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/models/images/icons/cite.svg) |  After the response is generated, Gemini Enterprise Agent Platform checks whether [citations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters#citation-filter) need to be included with the response. If a significant amount of the text in the response comes from a particular source, that source is added to the citation metadata in the response. 

### Responsible AI and safety

|  ![Responsible AI and safety](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/models/images/icons/safe.svg) |  The last layer of checks that the prompt and response go through before being returned is the [safety filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters#configurable-filters). Gemini Enterprise Agent Platform checks both the prompt and response for how much the prompt or response belongs to a [safety category](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters#harm-categories). If the threshold is exceeded for one or more categories, the response is blocked and Gemini Enterprise Agent Platform returns a [fallback response](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/process-blocked-responses#when-blocked). 

### Response

|  ![Response](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/models/images/icons/spark.svg) |  If the prompt and response passes the safety filter checks, the response is returned. Typically, the response is returned all at once. However, with Agent Platform you can also receive responses progressively as it generates by enabling [streaming](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/send-chat-prompts-gemini#streaming-and-non-streaming-responses). 

## Get started

Try one of these quickstarts to get started with generative AI on Agent Platform:

  * **[Generate text using the Agent Platform Gemini API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start):** Use the SDK to send requests to the Gemini API
  * **[Generate an image by using Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-image):** Generate images from a text prompt

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-20 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
