---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/genai-training-overview/
title: Agent Platform training overview \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:27.538484+00:00
---

# Agent Platform training overview  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/genai-training-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Agent Platform training overview Stay organized with collections  Save and categorize content based on your preferences. 

Generative AI often relies on large-scale machine learning (ML) models that are pre-trained on vast amounts of data. These are referred to as foundation models and serve as a base for various tasks. There are numerous ways to customize foundation models using Agent Platform:

  * Tuning: Tuning involves providing a model with a training dataset of specific examples relevant to the chosen downstream task.

    * [Supervised tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tune-models#how-tuning-works): This technique uses labeled examples to fine-tune a model. Each example demonstrates the chosen output for a given input during inference. Supervised tuning is effective for tasks where the expected output isn't overly complex and can be clearly defined, such as classification, sentiment analysis, entity extraction, summarization of less complex content, and generating domain-specific queries. You can tune text, image, audio, and document data types using supervised learning.
    * Reinforcement Learning from Human Feedback (RLHF) tuning: This method is suitable when the selected model output is more complex. RLHF tuning works well for objectives that aren't easily differentiated through supervised tuning, such as question answering, summarization of complex content, and creative content generation.
  * Distillation: Distillation often involves training a smaller "student" model to mimic the behavior of a larger, more capable "teacher" model.

  * Adapter model training: This involves training smaller adapter models (or layers) that work in conjunction with a foundation model to improve performance on specialized tasks. The original foundation model's parameters are often kept frozen, and only the adapter's weights are updated during training.

  * Grounding: While not a training method, grounding is a critical aspect of ensuring the reliability of generative AI outputs. [Grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview) involves connecting the model's output to verifiable sources of information, reducing the likelihood of invented content. This often involves providing the model with access to specific data sources during inference.




## What's next

  * [Overview of Generative AI on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
