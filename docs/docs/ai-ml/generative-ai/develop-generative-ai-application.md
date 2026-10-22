---
url: https://docs.cloud.google.com/docs/ai-ml/generative-ai/develop-generative-ai-application/
title: Develop a generative AI application \u00a0|\u00a0 Generative AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:44.579193+00:00
---

# Develop a generative AI application  |  Generative AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/ai-ml/generative-ai/develop-generative-ai-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Generative AI ](https://docs.cloud.google.com/docs/generative-ai)
  * [ Guides ](https://docs.cloud.google.com/docs/ai-ml/generative-ai/generative-ai-or-traditional-ai)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Develop a generative AI application

This document helps you learn how to address the challenges in each stage of developing a generative AI application. It describes how to select a model, customize the model's output to meet your needs, evaluate your customizations, and deploy your model. This document assumes that you already have a use case in mind, and that the use case is suitable for generative AI. For information about how to develop a use case, see [Evaluate and define your generative AI business use case](https://docs.cloud.google.com/docs/ai-ml/generative-ai/evaluate-define-generative-ai-use-case).

Before you start developing a generative AI application, assess your organization's technical readiness (capabilities and infrastructure). For information about how to assess your AI capabilities and create a roadmap to harness its potential, see [AI Readiness Workshop](https://docs.cloud.google.com/consulting/ai-readiness-workshop). If you plan to develop workflows that are automated by generative AI, assess whether humans should be included in the loop for critical decision stages. Human review can help with decisions like ensuring responsible use, meeting specific quality control requirements, or monitoring generated content.

## Generative AI models

Generative AI [foundation models](https://www.youtube.com/watch?v=YCZ6nwGnL4o) are trained on multi-terabyte datasets of text, images, code or other multimedia. The data and the model architecture enable the models to identify complex patterns and gain a deep, contextual understanding and produce new content like text, images, music, or videos driven by the training data.

Foundation models form the core upon which numerous generative AI applications are built. The models' capabilities translate into emergent abilities: with a simple text prompt instruction, generative AI foundation models can learn to perform a variety of tasks—like translate languages, answer questions, write a poem, or write code—without explicit training for each task. Generative AI foundation models can also adapt to perform specific tasks with some [prompt techniques](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/learn/prompt-design-strategies) or they can be fine-tuned with minimal additional training data.

[Large language models (LLMs)](https://docs.cloud.google.com/ai/llms#features) are trained on text, and they're one example of foundation models that are typically based on deep-learning architectures, such as the Transformer developed by Google in 2017. LLMs can be trained on billions of text samples and other content, and an LLM can be customized for specific domains.

Other [multimodal](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/docs/learn/models) models extend the ability of a generative AI application to process information from multiple modalities including images, videos, audio, and text. [Multimodal prompts](https://developers.google.com/solutions/ai-images) combine multiple input formats such as text, images, and audio. For example, you can input an image and ask a generative AI application to list or describe the objects in the image. Google's [Gemini models](https://blog.google/technology/ai/google-gemini-ai) are built from the ground up for multimodality, and they can reason seamlessly across text, images, video, audio, and code. Google Cloud's [Model Garden](https://cloud.google.com/model-garden) and [Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/overview) can help you to find and customize a range of foundation models from Google, open source, and third party sources.

## Choose a model

When you choose a model, consider the model's modality, size, and cost. Choose the most affordable model that still meets your response quality and latency requirements.

  * **Modality** : As described in the preceding section, the modality of a model corresponds to high-level data categories that a model is trained for, like text, images, and video. Typically, your use case and the model's modality are closely associated. If your use case involves text-to-image generation, you need to find a model trained on text and image data. If you need the flexibility of multiple modalities, as in multimodal search, there are models that also support multimodal use cases, but cost and latency might be higher. 
    * [Vertex AI models](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/learn/models) offers a large list of generative AI models that you can use.
    * [Model Garden](https://docs.cloud.google.com/vertex-ai/docs/start/explore-models) provides a list of first party and open source ML model offerings on Google Cloud.
  * **Size** : The size of a model is typically measured by the number of parameters. In general, a larger model can learn more complex patterns and relationships within data, which can result in higher quality responses. Because larger models in the same family can have higher latency and costs, you might need to experiment and evaluate models to determine which model size works best for your use case.
  * **Cost** : The cost of a model is related to its capabilities, which usually relates to the model's parameter count. Models can also be metered and charged differently. For example, some models are charged based on the number of input and output tokens. Other models are charged based on the number of node hours that are used while the model is deployed.

    * For information about generative AI model pricing on Vertex AI, see [Vertex AI pricing](https://docs.cloud.google.com/vertex-ai/generative-ai/pricing).

    * For information about the cost to deploy models on Google Kubernetes Engine (GKE), see [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing).

  * **Features** : Not all models support features like tuning and distillation. If those capabilities are important to you, check the features that are supported by each model.




## Design prompts

Prompt design is the process of authoring prompt and response pairs to give language models additional context and instructions. After you author prompts, you feed them to the model as a prompt dataset for pretraining. When a model serves predictions, it responds with your instructions built in.

If you want to get a specific output, you can use prompt design strategies, such as instructing the model to complete partial input or giving the model examples of ideal responses. For more information, see [Introduction to prompt design](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/learn/introduction-prompt-design).

## Customize a model

After prompt design, you might find that a model's responses work well, so you don't need to customize it. If the model isn't performing well—for example if it's hallucinating—you can use additional customization techniques. The following sections introduce such techniques and can help you understand how these options influence your model's output.

### Function calling and extensions

[Function calling](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling) and [Vertex AI Extensions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/overview) expand the capabilities of your model. Consider the use cases for your application and where using a model alone might be insufficient. You can assist the model by adding function calling or extensions. For example, your model can extract calendar information from text and then use an extension to find and book a reservation.

Although you can use function calling and extensions interchangeably, there are some high-level differences. Function calling is an asynchronous operation and you don't need to include credentials in your code. Vertex AI Extensions provide prebuilt options that you can use for complex tasks so that you don't need to write your own functions. However, because Vertex AI Extensions returns and calls functions for you, extensions require you to include credentials in your code.

### Grounding

_Grounding_ refers to augmenting model responses by anchoring them to verifiable sources of information. To ground a model, you connect it to a data source. Grounding a model helps enhance the trustworthiness of the generated content by reducing hallucinations.

_Retrieval augmented generation_ (RAG) is a commonly used grounding technique. RAG uses search functionality to find relevant information and then it adds that information to a model prompt. When you use RAG, output is grounded in facts and the latest information. RAG search uses vector embeddings and vector databases, which store data as numerical representations of unstructured data like text and images. For more information, see [What is a vector database](https://docs.cloud.google.com/discover/what-is-a-vector-database).

To learn about grounding in Vertex AI, see [Grounding overview](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/grounding/overview). For information about how to set up an embedding workflow in AlloyDB for PostgreSQL, see the [example embedding workflow](https://docs.cloud.google.com/alloydb/docs/ai/example-embeddings).

### Model tuning

Specialized tasks, such as training a language model on specific terminology, might require more training than you can do with prompt design alone. In that scenario, you can use model tuning to improve performance and have the model adhere to specific output requirements.

To tune a model, you must build a training dataset and then select a tuning method, such as supervised tuning, reinforcement learning from human feedback (RLHF) tuning, or model distillation. The size of the dataset and the tuning methods depends on your model and what you're optimizing for. For example, specialized, niche tasks require a smaller dataset to get significant improvements. To learn more about model tuning, see [Tune language foundation models](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/models/tune-models).

## Evaluate a model

Model evaluation helps you assess how your prompts and customizations affect a model's performance. Each evaluation method has its own strengths and weaknesses to consider. For example, [metrics-based evaluations](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/models/evaluate-models) can be automated and scaled quickly with a quantifiable way to measure performance. However, metrics can oversimplify results and miss context and nuances of natural language. To mitigate these shortcomings, use a wide range of metrics in combination with human evaluations.

Generative AI on Vertex AI offers automatic [side-by-side evaluation](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/models/side-by-side-eval), which lets you compare the output of two models against the [ground truth](https://developers.google.com/machine-learning/glossary/#ground-truth). A third model helps you to select the higher quality responses. Automatic side-by-side evaluation is on par with human evaluators, but it's quicker and available on demand. However, to perform the comparisons, this method requires a model that's larger than the models that you're evaluating, which can exhibit inherent biases. You should therefore still perform some human evaluations.

For all evaluation methods, you need an evaluation dataset. An evaluation dataset includes prompt and ground truth (ideal response) pairs that you create. When you build your dataset, include a diverse set of examples that align with the task you're evaluating to get meaningful results.

## Deploy a model

Deploying a model associates an endpoint and physical machine resources with your model for serving online, low-latency predictions. Not all models require deployment. For example, Google's foundation models that are available in generative AI on Vertex AI already have endpoints. The endpoints are specific to your Google Cloud project and they're immediately available for your use. However, if you tune any of those models, you must deploy them to an endpoint.

When you deploy a model, decide if you prefer to deploy models in a fully managed environment or a self-managed environment. In a fully managed environment, you select the physical resources that you need, like the machine type and accelerator type, and then Vertex AI instantiates and manages the resources for you. For example, to enable online predictions where Vertex AI manages the deployment resources for you, see [Deploy a model to an endpoint](https://docs.cloud.google.com/vertex-ai/docs/general/deployment). In a self-managed environment, you have more fine-grained control over your resources, but you manage them on your own. With self-managed environments, you can [serve models on platforms like GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multiple-gpu).

After you decide what type of environment you want to deploy in, consider your anticipated traffic, latency requirements, and budget. You need to balance these factors with your physical resources. For example, if lower cost is a priority, you might be able to tolerate higher latency with lower-cost machines. Test environments are a good example of this tradeoff. For more information about how to choose a machine type, see the notebook [Determining the ideal machine type to use for Vertex AI endpoints](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/vertex_endpoints/find_ideal_machine_type/find_ideal_machine_type.ipynb).

## Responsible AI

Generative AI on Vertex AI is designed with Google's AI principles in mind. However, it's important that you test models to ensure that they're used safely and responsibly. Because of the incredible versatility of LLMs, it's difficult to predict unintended or unforeseen responses.

When you develop applications for your use case, consider the limitations of generative AI models so that you can properly mitigate potential misuse and unintended issues. One example of a model limitation is that a model is only as good as the data that you use. If you give the model suboptimal data—like inaccurate or incomplete data—you can't expect optimal performance. Verify that your input data and prompts are accurate. Otherwise, the model can have suboptimal performance or false model outputs. To learn more about generative AI model limitations, see [Responsible AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/responsible-ai#limitations).

## What's next

  * Try out the [Vertex AI notebook tutorials](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/tutorials).
  * Learn about [Machine Learning Operations (MLOps) for Generative AI](https://www.cloudskillsboost.google/course_templates/927?locale=es&qlcampaign=gc-dms).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
