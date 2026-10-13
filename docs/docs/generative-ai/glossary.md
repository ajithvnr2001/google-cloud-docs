---
url: https://docs.cloud.google.com/docs/generative-ai/glossary/
title: Generative AI glossary \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:04.901120+00:00
---

# Generative AI glossary  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/generative-ai/glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Generative AI ](https://docs.cloud.google.com/docs/generative-ai)
  * [ Guides ](https://docs.cloud.google.com/docs/ai-ml/generative-ai/generative-ai-or-traditional-ai)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Generative AI glossary

This glossary defines generative artificial intelligence (AI) terms.

## AI agents

An _AI agent_ is an application that achieves a goal by processing input, performing reasoning with available tools, and taking actions based on its decisions. AI agents use function calling to format the input and ensure precise interactions with external tools. The following diagram shows the components of an AI agent:

![An AI agent consists of an orchestration layer, a model, and tools.](https://docs.cloud.google.com/static/docs/generative-ai/images/glossary-ai-agents.svg)

As shown in the preceding diagram, AI agents consist of the following components:

  * **Orchestration** : the orchestration layer of an agent manages memory, state, and decision-making by controlling the plan, tool usage, and data flow. Orchestration includes the following components: 
    * **Profile and instructions** : the agent takes on a specific role or persona to direct its actions and decision-making.
    * **Memory** : to maintain context and state, the agent retains short-term memory and long-term memory. Short-term memory holds the immediate context and information that's necessary for the current task. Long-term memory retains the complete conversation history.
    * **Reasoning and planning** : the agent uses the model to perform task decomposition and reflection, and then it creates a plan. First, the agent separates the user prompt into sub-components to handle complex tasks by calling one or more functions. Next, the agent reflects on the function outputs by using reasoning and feedback to improve the response.
  * **Model** : any generative language model that processes goals, creates plans, and generates responses. For optimal performance, a model should support function calling and it should be trained with data signatures from tools or reasoning steps.
  * **Tools** : a collection of tools including APIs, services, or functions that fetch data and perform actions or transactions. Tools let agents interact with external data and services.



For applications that require autonomous decision-making, complex multi-step workflow management, or adaptive experiences, AI agents perform better than standard foundational models. Agents excel at solving problems in real-time by using external data and at automating knowledge-intensive tasks. These capabilities enable an agent to provide more robust results than the passive text-generation capabilities of foundational models.

For more information about AI agents, see [What is an AI Agent](https://cloud.google.com/discover/what-are-ai-agents).

* * *

## context window

A _context window_ is the number of tokens that a foundational model can process in a given prompt. A larger context window lets the model access and process more information, which leads to more coherent, relevant, and comprehensive responses.

[Gemini models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/models) are purpose-built with long context windows to handle these larger amounts of information. To give a sense of scale, a model with a context window of 1 million tokens can process any one of the following inputs:

  * 50,000 lines of code (with the standard 80 characters per line)
  * All of the text messages that you've sent in the last 5 years
  * 8 average-length English-language novels
  * Transcripts of over 200 average-length podcast episodes
  * 1 hour of video without audio
  * Approximately 45 minutes of video with audio
  * 9.5 hours of audio



For more information about best practices for long context prompting, see [Long context](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/long-context).

* * *

## embedding

An _embedding_ is a numerical representation of data, such as text, images, or videos, that captures relationships between different inputs. Embeddings are generated during the training phase of a model by converting text, image, and video into arrays of floating point numbers that are called _vectors_. Embeddings often [reduce the dimensionality](https://en.wikipedia.org/wiki/Dimensionality_reduction) of data, which helps to enhance computational efficiency and to enable the processing of large datasets. This reduction in dimensionality is crucial for training and deploying complex models.

Machine learning (ML) models require data to be expressed in a format that they can process. Embeddings meet that requirement by mapping data into a continuous vector space where closer proximity reflects data points that have similar meanings. Embeddings enable models to discern nuanced patterns and relationships that would be obscured in raw data.

For example, large language models (LLMs) rely on embeddings in order to understand the context and meaning of text. That understanding lets the LLM generate coherent and relevant responses. In image generation, embeddings capture the visual features of images, which enables models to create realistic and diverse outputs.

Systems that use retrieval-augmented generation (RAG) rely on embeddings to match user queries with relevant knowledge. When a query is posed, it's converted into an embedding, which is then compared to the embeddings of documents that are within the knowledge base. This comparison, which is facilitated by similarity searches in the vector space, lets the system retrieve the most semantically relevant information.

For more information about embedding models and use cases, see [Embedding APIs overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings).

* * *

## foundation model

_Foundation models_ are large, powerful models that are trained on vast amounts of data, which often spans multiple modalities like text, images, video, and audio. These models use statistical modeling to predict likely responses to prompts and to generate new content. They learn patterns from their training data, such as language patterns for text generation and diffusion techniques for image generation.

Google offers a variety of [generative AI foundation models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/models) that are accessible through a managed API. To access the foundation models that are available in Google Cloud, use the Vertex AI [model garden](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models).

* * *

## function calling

_Function calling_ is a feature that connects large language models (LLMs) to external tools like APIs and functions to enhance the LLM's responses. This feature lets LLMs go beyond static knowledge and enhance responses with real-time information and services like databases, customer relationship management systems, and document repositories.

To use function calling, you provide the model with a set of functions. Then, when you prompt the model, the model can select and call the functions based on your request. The model analyzes the prompt and then it generates structured data that specifies which function to call and the parameter values. The structured data output calls the function and then it returns the results to the model. The model incorporates the results into its reasoning to generate a response. This process lets the model access and utilize information that's beyond its internal knowledge, which lets the model perform tasks that require external data or processing.

Function calling is a critical component in the architecture of AI agents. Function calling provides a structured way for the model to specify which tool to use and how to format the input, which helps to ensure precise interactions with external systems.

For more information about function calling in Gemini, see [Introduction to function calling](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling).

* * *

## generative AI

_Generative AI_ is a type of AI that goes beyond the traditional AI focus on [classification](https://developers.google.com/machine-learning/glossary#classification-model) and [prediction](https://developers.google.com/machine-learning/glossary#prediction). Traditional AI models learn from existing data to classify information or to predict future outcomes based on historical patterns. Generative AI uses foundation models to generate new content like text, images, audio, or videos. This new content is generated by learning the underlying patterns and style of the training data, which effectively lets the model create outputs that resemble the data that it was trained on.

Learn more about [when to use generative AI](https://docs.cloud.google.com/docs/ai-ml/generative-ai/generative-ai-or-traditional-ai) and [generative AI business use cases](https://docs.cloud.google.com/docs/ai-ml/generative-ai/evaluate-define-generative-ai-use-case).

* * *

## grounding

_Grounding_ is the process of connecting a model's output to verifiable sources of information. These sources might provide practical, context-specific information, such as internal company documentation, project-specific data, or communication records. Grounding helps to improve the accuracy, reliability, and usefulness of AI outputs by providing the model with access to specific data sources. Grounding reduces the likelihood of _hallucinations_ —instances where the model generates content that isn't factual. A common type of grounding is retrieval-augmented generation (RAG), which involves retrieving relevant external information to enhance the model's responses.

For more information about grounding with Google Search, see [Grounding overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview).

* * *

## large language model (LLM)

A _large language model (LLM)_ is a text-driven foundational model that's trained on a vast amount of data. LLMs are used to perform natural language processing (NLP) tasks, such as text generation, machine translation, text summarization, and question answering. The term _LLM_ is sometimes used interchangeably with foundation models. However, LLMs are text-based, whereas foundation models can be trained with and receive input from multiple modalities, including text, images, audio, and video.

To learn the patterns and relationships within language, LLMs use techniques such as [reinforcement learning](https://developers.google.com/machine-learning/glossary#reinforcement_learning) and instruction fine-tuning. When you design prompts, it's important to consider the various factors that can influence the model's responses.

* * *

## latency

_Latency_ is the time that it takes for a model to process an input prompt and generate a response. When you examine the latency of a model, consider the following:

  * **Time to First Token (TTFT)** : the time that it takes for the model to produce the first token of the response after it receives the prompt. TTFT is important for streaming applications where you want immediate feedback.
  * **Time to Last Token (TTLT)** : the total time that the model takes to process the prompt and generate the complete response.



For information about reducing latency, see [Best practices with large language models (LLMs)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompt-best-practices).

* * *

## prompt engineering

_Prompt engineering_ is the iterative process of creating a prompt and accessing the model's response to get the response that you want. Writing well-structured prompts can be an essential part of ensuring accurate, high quality responses from a language model.

The following are common techniques that you can use to improve responses:

  * **Zero-shot prompting** : provide a prompt without any examples and rely on the model's pre-existing knowledge.
  * **One-shot prompting** : provide a single example in the prompt to guide the model's response.
  * **Few-shot prompting** : provide multiple examples in the prompt to demonstrate the pattern or task that you want.



When you provide a model with examples, you help to control aspects of the model's response, such as formatting, phrasing, scope, and overall patterns. Effective few-shot prompts combine clear instructions with specific and varied examples. It's important to experiment to determine the optimal number of examples; too few examples might not provide enough guidance, but too many examples can cause the model to overfit to the examples and fail to generalize well.

For more information about best practices for prompting, see [Overview of prompting strategies](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies).

* * *

## prompting

A _prompt_ is a natural language request that's sent to a generative AI model to elicit a response. Depending on the model, a prompt can contain text, images, videos, audio, documents, and other modalities or even multiple modalities (multimodal).

An effective prompt consists of content and structure. Content provides all relevant task information, such as instructions, examples, and context. Structure ensures efficient parsing through organization, including ordering, labeling, and delimiters. Depending on the output that you want, you might consider additional [components](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies#components-of-a-prompt).

* * *

## model parameters

_Model parameters_ are internal variables that a model uses to determine how the model processes input data and how it generates outputs. During training, you can adjust model parameters, such as weight and bias, to optimize the model's performance. During inference, you can influence the model's output through various prompting parameters, which doesn't directly change the learned model parameters.

The following are some of the prompting parameters that affect content generation in the Gemini API in Vertex AI:

  * [`temperature`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#temperature): temperature changes the randomness of token selection during response generation, which influences the creativity and predictability of the output. The value of `temperature` ranges from `0` to `1`. Lower temperatures (closer to `0`) produce more deterministic and predictable results. Higher temperatures (closer to `1`) generate more diverse and creative text, but the results are potentially less coherent.
  * [`topP`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#top-p): Top-P changes how the model samples and selects tokens for output. Top-P selects the smallest set of tokens whose cumulative probability exceeds a threshold, or `p`, and then samples from that distribution. The value of `topP` ranges from `0` to `1`. For example, if tokens A, B, and C have a probability of 0.3, 0.2, and 0.1, and the `topP` value is `0.5`, then the model will select either A or B as the next token by using temperature, and it will exclude C as a candidate.
  * [`topK`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#topK): Top-K changes how the model samples and selects tokens for output. Top-K selects the most statistically likely tokens to generate a response. The value of `topK` represents a number of tokens from `1` to `40`, which the model will choose from before it generates a response. For example, if tokens A, B, C, and D have a probability of 0.6, 0.5, 0.2, and 0.1 and the top-K value is `3`, then the model will select either A, B, or C as the next token by using temperature, and it will exclude D as a candidate.
  * [`maxOutputTokens`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#maxOutputTokens): the `maxOutputTokens` setting changes the maximum number of tokens that can be generated in the response. A lower value will generate shorter responses and a higher value will generate potentially longer responses.



For more information about sampling parameters in the Gemini API in Vertex AI, see [Content generation parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters).

* * *

## retrieval-augmented generation (RAG)

_Retrieval-augmented generation (RAG)_ is a technique to improve the quality and accuracy of large language model (LLM) output by grounding it with sources of knowledge that are retrieved after the model was trained. RAG addresses LLM limitations, such as factual inaccuracies, lack of access to current or specialized information, and inability to cite sources. By providing access to information that's retrieved from trusted knowledge bases or documents—including data that the model wasn't trained on, proprietary data, or sensitive user-specific data—RAG enables LLMs to generate more reliable and contextually relevant responses.

When a model that uses RAG receives your prompt, the RAG process completes these stages:

  1. **Retrieve** : search for data that's relevant to the prompt.
  2. **Augment** : append the data that's retrieved to the prompt.
  3. **Generate** : 
     1. Instruct the LLM to create a summary or response that's based on the augmented prompt.
     2. Serve the response back.



For more information about Vertex AI and RAG, see [Vertex AI RAG Engine overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-overview).

* * *

## tokens

A _token_ is a basic unit of data that a foundation model processes. Models separate data in a prompt into tokens for processing. The set of all of the tokens that are used by a model is called the _vocabulary_. Tokens can be single characters like `z`, whole words like `cat`, or parts from longer words.

_Tokenizers_ separate long words—such as complex or technical terms, compound words, or words with punctuation and special characters—into several tokens. The process of splitting text into tokens is called _tokenization_. The goal of tokenization is to create tokens with semantic meaning that can be recombined to understand the original word. For example, the word "predefined" can be split into the following tokens: "pre", "define", "ed".

Tokens can represent multimodal input like images, videos, and audio. Embedding techniques transform multimodal input into numerical representations that the model can process as tokens. The following are the approximate token calculations for an example multimodal input, regardless of display or file size:

  * Images: 258 total tokens
  * Video: 263 tokens per second
  * Audio: 32 tokens per second



Each model has a limit on the number of tokens that it can handle in a prompt and response. Additionally, model usage costs are calculated based on the number of input and output tokens. For information about how to get the token count of a prompt that was sent to a Gemini model, see [List and count tokens](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/list-token). For information about the cost of generative AI models on Vertex AI, see [Vertex AI pricing](https://docs.cloud.google.com/vertex-ai/generative-ai/pricing).

* * *

## tuning

_Tuning_ is the process of adapting a foundation model to perform specific tasks with greater precision and accuracy. Tuning is achieved by adjusting some or all of the model's parameters or training a model on a dataset that contains examples that replicate the tasks and results that you want. Tuning is an iterative process, which can be complex and costly, but it has the potential to yield significant performance improvements. Tuning is most effective when you have a labeled dataset that has more than 100 examples, and you want to perform complex or unique tasks where prompting techniques aren't sufficient.

The following are tuning techniques that are supported by [Vertex AI](https://cloud.google.com/vertex-ai):

  * **Full fine-tuning** : a technique that updates all of the model's parameters during the tuning process. Full fine-tuning can be computationally expensive and it can require a lot of data, but it also has the potential to achieve the highest levels of performance, especially for complex tasks.
  * **Parameter-efficient tuning** : a technique that's also known as _adapter tuning_ ; parameter-efficient tuning updates some of the model's parameters during the tuning process. Parameter-efficient tuning is more resource efficient and more cost effective compared to full fine-tuning.
  * **Supervised fine-tuning** : a technique that trains the model on labeled input-output pairs. Supervised fine-tuning is commonly used for tasks that involve classification, translation, and summarization.



For more information about tuning, see [Introduction to tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
