---
url: https://docs.cloud.google.com/architecture/deploy-operate-generative-ai-applications/
title: Deploy and operate generative AI applications \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:33.477163+00:00
---

# Deploy and operate generative AI applications  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/deploy-operate-generative-ai-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Deploy and operate generative AI applications Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-11-19 UTC

Generative AI has introduced a new way to build and operate AI applications that is different from predictive AI. To build a generative AI application, you must choose from a diverse range of architectures and sizes, curate data, engineer optimal prompts, tune models for specific tasks, and ground model outputs in real-world data.

This document describes how you can adapt DevOps and MLOps processes to develop, deploy, and operate generative AI applications on existing foundation models. For information on deploying predictive AI, see [MLOps: Continuous delivery and automation pipelines in machine learning](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning).

## What are DevOps and MLOps?

DevOps is a software engineering methodology that connects development and operations. DevOps promotes collaboration, automation, and continuous improvement to streamline the software development lifecycle, using practices such as continuous integration and continuous delivery (CI/CD).

MLOps builds on DevOps principles to address the challenges of building and operating machine learning (ML) systems. Machine learning systems typically use predictive AI to identify patterns and make predictions. The MLOps workflow includes the following:

  * Data validation
  * Model training
  * Model evaluation and iteration
  * Model deployment and serving
  * Model monitoring



## What are foundation models?

Foundation models are the core component in a generative AI application. These models are large programs that use datasets to learn and make decisions without human intervention. Foundation models are trained on many types of data, including text, images, audio, and video. Foundation models include large language models (LLMs) such as Llama 3.1 and multimodal models such as Gemini.

Unlike predictive AI models, which are trained for specific tasks on focused datasets, foundation models are trained on massive and diverse datasets. This training lets you use foundation models to develop applications for many different use cases. Foundation models have [_emergent properties_ (PDF)](https://arxiv.org/pdf/2206.07682.pdf), which let them provide responses to specific inputs without explicit training. Because of these emergent properties, foundation models are challenging to create and operate and require you to adapt your DevOps and MLOps processes.

Developing a foundation model requires significant data resources, specialized hardware, significant investment, and specialized expertise. Therefore, many businesses prefer to use existing foundation models to simplify the development and deployment of their generative AI applications.

## Lifecycle of a generative AI application

The lifecycle for a generative AI application includes the following phases:

  * **Discovery:** Developers and AI engineers identify which foundation model is most suitable for their use case. They consider each model's strengths, weaknesses, and costs to make an informed decision.
  * **Development and experimentation:** Developers use prompt engineering to create and refine input prompts to get the required output. When available, [few-shot learning](https://en.wikipedia.org/wiki/Few-shot_learning), parameter-efficient [fine-tuning](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)) (PEFT), and model chaining help guide model behavior. _Model chaining_ refers to orchestrating calls to multiple models in a specific sequence to create a workflow.
  * **Deployment:** Developers must manage many artifacts in the deployment process, including prompt templates, chain definitions, embedded models, retrieval data stores, and fine-tuned model adapters. These artifacts have their own governance requirements and require careful management throughout development and deployment. Generative AI application deployment also must account for the technical capabilities of the target infrastructure, ensuring that application hardware requirements are met.
  * **Continuous monitoring in production:** Administrators improve application performance and maintain safety standards through responsible AI techniques, such as ensuring fairness, transparency, and accountability in the model's outputs.
  * **Continuous improvement:** Developers constantly adjust foundation models through prompting techniques, swapping the models out for newer versions, or even combining multiple models for enhanced performance, cost efficiency, or reduced latency. Conventional continuous training still holds relevance for scenarios when recurrent fine-tuning or incorporating human feedback loops are needed.



Data engineering practices have a critical role across all development stages. To create reliable outputs, you must have factual grounding (which ensures that the model's outputs are based on accurate and up-to-date information) and recent data from internal and enterprise systems. Tuning data helps adapt models to specific tasks and styles, and rectifies persistent errors.

## Find the foundation model for your use case

Because building foundation models is resource-intensive, most businesses prefer to use an existing foundation model that is optimal for their use case. Finding the right foundation model is difficult because there are many foundation models. Each model has different architectures, sizes, training datasets, and licenses. In addition, each use case presents unique requirements, demanding that you analyze available models across multiple dimensions.

Consider the following factors when you assess models:

  * **Quality:** Run test prompts to gauge output quality.
  * **Latency and throughput:** Determine the correct latency and throughput that your use case requires, as these factors directly impact user experience. For example, a chatbot requires lower latency than batch-processed summarization tasks.
  * **Development and maintenance time:** Consider the time investment for initial development and ongoing maintenance. Managed models often require less effort than openly available models that you deploy yourself.
  * **Usage cost:** Consider the infrastructure and consumption costs that are associated with the model.
  * **Compliance:** Assess the model's ability to adhere to relevant regulations and licensing terms.



## Develop and experiment

When building generative AI applications, development and experimentation are iterative and orchestrated. Each experimental iteration involves refining data, adapting the foundation model, and evaluating results. Evaluation provides feedback that guides subsequent iterations in a continuous feedback loop. If performance doesn't match expectations, you can gather more data, augment the data, or further curate the data. In addition, you might need to optimize prompts, apply fine-turning techniques, or change to another foundation model. This iterative refinement cycle, driven by evaluation insights, is just as important for optimizing generative AI applications as it is for machine learning and predictive AI.

### The foundation model paradigm

Foundation models differ from predictive models because they are multi-purpose models. Instead of being trained for a single purpose on data specific to that task, foundation models are trained on broad datasets, which lets you apply a foundation model to many different use cases.

Foundation models are also highly sensitive to changes in their input. The output of the model and the task that it performs are determined by the input to the model. A foundation model can translate text, generate videos, or classify data simply by changing the input. Even insignificant changes to the input can affect the model's ability to correctly perform that task.

These properties of foundation models require different development and operational practices. Although models in the predictive AI context are self-sufficient and task-specific, foundation models are multi-purpose and need an additional element beyond the user input. Generative AI models require a prompt, and more specifically, a _prompt template_. A prompt template is a set of instructions and examples along with placeholders to accommodate user input. The application can combine the prompt template and the dynamic data (such as the user input) to create a complete prompt, which is the text that is passed as input to the foundation model.

### The prompted model component

The presence of the prompt is a distinguishing feature of generative AI applications. The model and the prompt aren't sufficient for the generation of content; generative AI needs both. The combination of the model and the prompt is known as the _prompted model component_. The prompted model component is the smallest independent component that is sufficient to create a generative AI application. The prompt doesn't need to be complicated. For example, it can be a simple instruction, such as "translate the following sentence from English to French", followed by the sentence to be translated. However, without that preliminary instruction, a foundation model won't perform the required translation task. So a prompt, even just a basic instruction, is necessary along with the input to get the foundation model to do the task required by the application.

The prompted model component creates an important distinction for MLOps practices when developing generative AI applications. In the development of a generative AI application, experimentation and iteration must be done in the context of a prompted model component. The generative AI experimentation cycle typically begins with testing variations of the prompt — changing the wording of the instructions, providing additional context, or including relevant examples — and evaluating the impact of those changes. This practice is commonly referred to as _prompt engineering_.

Prompt engineering involves the following iterative steps:

  * **Prompting:** Craft and refine prompts to elicit desired behaviors from a foundation model for a specific use case.
  * **Evaluation:** Assess the model's outputs, ideally programmatically, to gauge its understanding and success in fulfilling the prompt's instructions.



To track evaluation results, you can optionally register the results of an experiment. Because the prompt itself is a core element of the prompt engineering process, it becomes the most important artifact within the artifacts that are part of the experiment.

However, to experiment with a generative AI application, you must identify the artifact types. In predictive AI, data, pipelines, and code are different. But with the prompt paradigm in generative AI, prompts can include context, instructions, examples, guardrails, and actual internal or external data pulled from somewhere else.

To determine the artifact type, you must recognize that a prompt has different components and requires different management strategies. Consider the following:

  * **Prompt as data:** Some parts of the prompt act just like data. Elements like few-shot examples, knowledge bases, and user queries are essentially data points. These components require data-centric MLOps practices such as data validation, drift detection, and lifecycle management.
  * **Prompt as code:** Other components such as context, prompt templates, and guardrails are similar to code. These components define the structure and rules of the prompt itself and require more code-centric practices such as approval processes, code versioning, and testing.



As a result, when you apply MLOps practices to generative AI, you must have processes that give developers an easy way to store, retrieve, track, and modify prompts. These processes allow for fast iteration and principled experimentation. Often one version of a prompt can work well with a specific version of the model and not as well with a different version. When you track the results of an experiment, you must record the prompt, the components' versions, the model version, metrics, and output data.

### Model chaining and augmentation

Generative AI models, particularly large language models (LLMs), face inherent challenges in maintaining recency and avoiding hallucinations. Encoding new information into LLMs requires expensive and data-intensive pre-training before they can be deployed. Depending on the use case, using only one prompted model to perform a particular generation might not be sufficient. To solve this issue, you can connect several prompted models together, along with calls to external APIs and logic expressed as code. A sequence of prompted model components connected together in this way is commonly known as a _chain_.

The following diagram shows the components of a chain and the relative development process.

![Model chains in the development process.](https://docs.cloud.google.com/static/architecture/images/gen-ai-chain.svg)

#### Mitigation for recency and hallucination

Two common chain-based patterns that can mitigate recency and hallucinations are [retrieval-augmented generation (RAG) (PDF)](https://arxiv.org/pdf/2005.11401.pdf) and agents.

  * RAG augments pre-trained models with knowledge retrieved from databases, which bypasses the need for pre-training. RAG enables grounding and reduces hallucinations by incorporating up-to-date factual information directly into the generation process.
  * Agents, popularized by the [ReAct prompting technique (PDF)](https://arxiv.org/pdf/2210.03629.pdf), use LLMs as mediators that interact with various tools, including RAG systems, internal or external APIs, custom extensions, or even other agents. Agents enable complex queries and real-time actions by dynamically selecting and using relevant information sources. The LLM, acting as an agent, interprets the user's query, decides which tool to use, and formulates the response based on the retrieved information.



You can use RAG and agents to create multi-agent systems that are connected to large information networks, enabling sophisticated query handling and real-time decision making.

The orchestration of different models, logic, and APIs is not new to generative AI applications. For example, recommendation engines combine collaborative filtering models, content-based models, and business rules to generate personalized product recommendations for users. Similarly, in fraud detection, machine learning models are integrated with rule-based systems and external data sources to identify suspicious activities.

What makes these chains of generative AI components different is that you can't characterize the distribution of component inputs beforehand, which makes the individual components much harder to evaluate and maintain in isolation. Orchestration causes a paradigm shift in how you develop AI applications for generative AI.

In predictive AI, you can iterate on the separate models and components in isolation and then chain them in the AI application. In generative AI, you develop a chain during integration, perform experimentation on the chain end-to-end, and iterate chaining strategies, prompts, foundation models, and other APIs in a coordinated manner to achieve a specific goal. You often don't need feature engineering, data collection, or further model training cycles; just changes to the wording of the prompt template.

The shift towards MLOps for generative AI, in contrast to MLOps for predictive AI, results in the following differences:

  * **Evaluation:** Because of the tight coupling of chains, chains require end-to-end evaluation, not just for each component, to gauge their overall performance and the quality of their output. In terms of evaluation techniques and metrics, evaluating chains is similar to evaluating prompted models.
  * **Versioning:** You must manage a chain as a complete artifact in its entirety. You must track the chain configuration with its own revision history for analysis, for reproducibility, and to understand the effects of changes on output. Your logs must include the inputs, outputs, intermediate states of the chain, and any chain configurations that were used during each execution.
  * **Continuous monitoring:** To detect performance degradation, data drift, or unexpected behavior in the chain, you must configure proactive monitoring systems. Continuous monitoring helps to ensure early identification of potential issues to maintain the quality of the generated output.
  * **Introspection:** You must inspect the internal data flows of a chain (that is, the inputs and outputs from each component) as well as the inputs and outputs of the entire chain. By providing visibility into the data that flows through the chain and the resulting content, developers can pinpoint the sources of errors, biases, or undesirable behavior.



The following diagram shows how chains, prompted model components, and model tuning work together in a generative AI application to reduce recency and hallucinations. Data is curated, models are tuned, and chains are added to further refine responses. After the results are evaluated, developers can log the experiment and continue to iterate.

![Chains, prompted model, and model tuning in generative AI applications.](https://docs.cloud.google.com/static/architecture/images/gen-ai-chain-tuning.svg)

### Fine-tuning

When you are developing a generative AI use case that involves foundation models, it can be difficult, especially for complex tasks, to rely on only prompt engineering and chaining to solve the use case. To improve task performance, developers often need to fine-tune the model directly. Fine-tuning lets you actively change all the layers or a subset of layers (parameter efficient fine-tuning) of the model to optimize its ability to perform a certain task. The most common ways of tuning a model are the following:

  * **Supervised fine-tuning:** You train the model in a supervised manner, teaching it to predict the right output sequence for a given input.
  * **Reinforcement learning from human feedback (RLHF):** You train a reward model to predict what humans would prefer as a response. Then, you use this reward model to nudge the LLM in the right direction during the tuning process. This process is similar to having a panel of human judges guide the model's learning.



The following diagram shows how tuning helps refine the model during the experimentation cycle.

![Fine-turning models.](https://docs.cloud.google.com/static/architecture/images/gen-ai-tune-train.svg)

In MLOps, fine-tuning shares the following capabilities with model training:

  * The ability to track the artifacts that are part of the tuning job. For example, artifacts include the input data or the parameters being used to tune the model.
  * The ability to measure the impact of the tuning. This capability lets you evaluate the tuned model for the specific tasks that it was trained on and to compare results with previously tuned models or frozen models for the same task.



#### Continuous training and tuning

In MLOps, continuous training is the practice of repeatedly retraining machine learning models in a production environment. Continuous training helps to ensure that the model remains up-to-date and performs well as real-world data patterns change over time. For generative AI models, continuous tuning of the models is often more practical than a retraining process because of the high data and computational costs involved.

The approach to continuous tuning depends on your specific use case and goals. For relatively static tasks like text summarization, the continuous tuning requirements might be lower. But for dynamic applications like chatbots that need constant human alignment, more frequent tuning using techniques like RLHF that are based on human feedback is necessary.

To determine the right continuous tuning strategy, you must evaluate the nature of your use case and how the input data evolves over time. Cost is also a major consideration, as compute infrastructure greatly affects the speed and expense of tuning. Graphics processing units (GPUs) and tensor processing units (TPUs) are hardware that is required for fine-tuning. GPUs, known for their parallel processing power, are highly effective in handling the computationally intensive workloads and are often associated with training and running complex machine learning models. TPUs, on the other hand, are specifically designed by Google for accelerating machine learning tasks. TPUs excel in handling large-matrix operations that are common in deep learning neural networks.

### Data practices

Previously, ML model behavior was dictated solely by its training data. While this still holds true for foundation models, the model behavior for generative AI applications that are built on top of foundation models is determined by how you adapt the model with different types of input data.

Foundation models are trained on data such as the following:

  * Pretraining datasets (for example, C4, [The Pile](https://pile.eleuther.ai/), or proprietary data)
  * Instruction tuning datasets
  * Safety tuning datasets
  * Human preference data



Generative AI applications are adapted on data such as the following:

  * Prompts
  * Augmented or grounded data (for example, websites, documents, PDFs, databases, or APIs)
  * Task-specific data for PEFT
  * Task-specific evaluations
  * Human preference data



The main difference for data practices between predictive ML and generative AI is at the beginning of the lifecycle process. In predictive ML, you spend a lot of time on data engineering, and if you don't have the right data, you cannot build an application. In generative AI, you start with a foundation model, some instructions, and maybe a few example inputs (such as in-context learning). You can prototype and launch an application with very little data.

The ease of prototyping, however, comes with the additional challenge of managing diverse data. Predictive AI relies on well-defined datasets. In generative AI, a single application can use various data types, from completely different data sources, all working together.

Consider the following data types:

  * **Conditioning prompts:** Instructions given to the foundation model to guide its output and set boundaries of what it can generate.
  * **Few-shot examples:** A way to show the model what you want to achieve through input-output pairs. These examples help the model understand the specific tasks, and in many cases, these examples can boost performance.
  * **Grounding or augmentation data:** The data that permits the foundation model to produce answers for a specific context and keep responses current and relevant without retraining the entire foundation model. This data can come from external APIs (like Google Search) or internal APIs and data sources.
  * **Task-specific datasets:** The datasets that help fine-tune an existing foundation model for a particular task, improving its performance in that specific area.
  * **Full pre-training datasets:** The massive datasets that are used to initially train foundation models. Although application developers might not have access to them or the tokenizers, the information encoded in the model itself influences the application's output and performance.



This diverse range of data types adds a complexity layer in terms of data organization, tracking, and lifecycle management. For example, a RAG-based application can rewrite user queries, dynamically gather relevant examples using a curated set of examples, query a vector database, and combine the information with a prompt template. A RAG-based application requires you to manage multiple data types, including user queries, vector databases with curated few-shot examples and company information, and prompt templates.

Each data type needs careful organization and maintenance. For example, a vector database requires processing data into embeddings, optimizing chunking strategies, and ensuring only relevant information is available. A prompt template needs versioning and tracking, and user queries need rewriting. MLOps and DevOps best practices can help with these tasks. In predictive AI, you create data pipelines for extraction, transformation, and loading. In generative AI, you build pipelines to manage, evolve, adapt, and integrate different data types in a versionable, trackable, and reproducible way.

Fine-tuning foundation models can boost generative AI application performance, but the models need data. You can get this data by launching your application and gathering real-world data, generating synthetic data, or a mix of both. Using large models to generate synthetic data is becoming popular because this method speeds up the deployment process, but it's still important to have humans check the results for quality assurance. The following are examples of how you can use large models for data engineering purposes:

  * **Synthetic data generation:** This process involves creating artificial data that closely resembles real-world data in terms of its characteristics and statistical properties. Large and capable models often complete this task. Synthetic data serves as additional training data for generative AI, enabling it to learn patterns and relationships even when labeled real-world data is scarce.
  * **Synthetic data correction:** This technique focuses on identifying and correcting errors and inconsistencies within existing labeled datasets. By using the power of larger models, generative AI can flag potential labeling mistakes and propose corrections to improve the quality and reliability of the training data.
  * **Synthetic data augmentation:** This approach goes beyond generating new data. Synthetic data augmentation involves intelligently manipulating existing data to create diverse variations while preserving essential features and relationships. Generative AI can encounter a broader range of scenarios than predictive AI during training, which leads to improved generalization and the ability to generate nuanced and relevant outputs.



Unlike predictive AI, it is difficult to evaluate generative AI. For example, you might not know the training data distribution of the foundation models. You must build a custom evaluation dataset that reflects all your use cases, including the essential, average, and edge cases. Similar to fine-tuning data, you can use powerful LLMs to generate, curate, and augment data for building robust evaluation datasets.

### Evaluation

The evaluation process is a core activity of the development of generative AI applications. Evaluation might have different degrees of automation: from entirely driven by humans to entirely automated by a process.

When you're prototyping a project, evaluation is often a manual process. Developers review the model's outputs, getting a qualitative sense of how it's performing. But as the project matures and the number of test cases increases, manual evaluation becomes a bottleneck.

Automating evaluation has two big benefits: it lets you move faster and makes evaluations more reliable. It also takes human subjectivity out of the equation, which helps ensure that the results are reproducible.

But automating evaluation for generative AI applications comes with its own set of challenges. For example, consider the following:

  * Both the inputs (prompts) and outputs can be incredibly complex. A single prompt might include multiple instructions and constraints that the model must manage. The outputs themselves are often high-dimensional such as a generated image or a block of text. Capturing the quality of these outputs in a simple metric is difficult. Some established metrics, like [BLEU](https://en.wikipedia.org/wiki/BLEU) for translations and [ROUGE](https://en.wikipedia.org/wiki/ROUGE_\(metric\)) for summaries, aren't always sufficient. Therefore, you can use custom evaluation methods or another foundation model to evaluate your system. For example, you could prompt a large language model (such as [AutoSxS](https://ai.google.dev/gemma/docs/paligemma/model-card)) to score the quality of generated texts across various dimensions.
  * Many evaluation metrics for generative AI are subjective. What makes one output better than another can be a matter of opinion. You must make sure that your automated evaluation aligns with human judgment because you want your metrics to be a reliable proxy of what people would think. To ensure comparability between experiments, you must determine your evaluation approach and metrics early in the development process.
  * Lack of ground truth data, especially in the early stages of a project. One workaround is to generate synthetic data to serve as a temporary ground truth that you can refine over time with human feedback.
  * Comprehensive evaluation is essential for safeguarding generative AI applications against adversarial attacks. Malicious actors can craft prompts to try to extract sensitive information or manipulate the model's outputs. Evaluation sets need to specifically address these attack vectors, through techniques like prompt fuzzing (feeding the model random variations on prompts) and testing for information leakage.



To evaluate generative AI applications, implement the following:

  * Automate the evaluation process to help ensure speed, scalability, and reproducibility. You can consider automation as a proxy for human judgment.
  * Customize the evaluation process as required for your use cases.
  * To ensure comparability, stabilize the evaluation approach, metrics, and ground truth data as early as possible in the development phase.
  * Generate synthetic ground truth data to accommodate for the lack of real ground truth data.
  * Include test cases of adversarial prompting as part of the evaluation set to test the reliability of the system itself against these attacks.



## Deploy

Production-level generative AI applications are complex systems with many interacting components. To deploy a generative AI application to production, you must manage and coordinate these components with the previous stages of generative AI application development. For example, a single application might use several LLMs alongside a database, all fed by a dynamic data pipeline. Each of these components can require its own deployment process.

Deploying generative AI applications is similar to deploying other complex software systems because you must deploy system components such as databases and Python applications. We recommend that you use standard software engineering practices such as [version control](https://en.wikipedia.org/wiki/Version_control) and CI/CD.

### Version control

Generative AI experimentation is an iterative process that involves repeated cycles of development, evaluation, and modification. To ensure a structured and manageable approach, you must implement strict versioning for all modifiable components. These components include the following:

  * **Prompt templates:** Unless you use specific prompt management solutions, use version control tools to track versions.
  * **Chain definitions:** Use version control tools to track versions of the code that defines the chain (including API integrations, database calls, and functions).
  * **External datasets:** In RAG systems, external datasets play an important role. Use existing data analytics solutions such as BigQuery, AlloyDB for PostgreSQL, and Agent Platform Feature Store to track these changes and versions of these datasets.
  * **Adapter models:** Techniques like LoRA tuning for adapter models are constantly evolving. Use established data storage solutions (for example, Cloud Storage) to manage and version these assets effectively.



### Continuous integration

In a continuous integration framework, every code change goes through automatic testing before merging to catch issues early. Unit and integration testing are important for quality and reliability. Unit tests focus on individual code pieces, while integration testing verifies that different components work together.

Implementing a continuous integration system helps to do the following:

  * **Ensure reliable, high-quality outputs:** Rigorous testing increases confidence in the system's performance and consistency.
  * **Catch bugs early:** Identifying issues through testing prevents them from causing bigger problems downstream. Catching bugs early makes the system more robust and resilient to edge cases and unexpected inputs.
  * **Lower maintenance costs:** Well-documented test cases simplify troubleshooting and enable smoother modifications in the future, reducing overall maintenance efforts.



These benefits are applicable to generative AI applications. Apply continuous integration to all elements of the system, including the prompt templates, chain, chaining logic, any embedded models, and retrieval systems.

However, applying continuous integration to generative AI comes with the following challenges:

  * **Difficulty generating comprehensive test cases:** The complex and open-ended nature of generative AI outputs makes it hard to define and create an exhaustive set of test cases that cover all possibilities.
  * **Reproducibility issues:** Achieving deterministic, reproducible results is tricky because generative models often have intrinsic randomness and variability in their outputs, even for identical inputs. This randomness makes it harder to consistently test for expected behaviors.



These challenges are closely related to the broader question of how to evaluate generative AI applications. You can apply many of the same evaluation techniques to the development of CI systems for generative AI.

### Continuous delivery

After the code is merged, a continuous delivery process begins to move the built and tested code through environments that closely resemble production for further testing before the final deployment.

As described in Develop and experiment, chain elements become one of the main components to deploy because they fundamentally constitute the generative AI application. The delivery process for the generative AI application that contains the chain might vary depending on the latency requirements and whether the use case is batch or online.

Batch use cases require that you deploy a batch process that is executed on a schedule in production. The delivery process focuses on testing the entire pipeline in integration in an environment that is similar to production before deployment. As part of the testing process, developers can assert specific requirements around the throughput of the batch process itself and check that all components of the application are functioning correctly. (For example, developers can check permissions, infrastructure, and code dependencies.)

Online use cases require that you deploy an API, which is the application that contains the chain and is capable of responding to users at low latency. Your delivery process involves testing the API in integration in an environment that is similar to production. These tests verify that all components of the application are functioning correctly. You can verify non-functional requirements (for example, scalability, reliability, and performance) through a series of tests, including load tests.

### Deployment checklist

The following list describes the steps to take when you deploy a generative AI application using a managed service such as Gemini Enterprise Agent Platform:

  * **Configure version control:** Implement version control practices for model deployments. Version control lets you roll back to previous versions if necessary and track changes made to the model or deployment configuration.
  * **Optimize the model:** Perform model optimization tasks (distillation, quantization, and pruning) before packaging or deploying the model.
  * **Containerize the model:** Package the trained model into a container.
  * **Define the target hardware requirements:** Ensure the target deployment environment meets the requirements for optimal performance of the model, such as GPUs, TPUs, and other specialized hardware accelerators.
  * **Define the model endpoint:** Specify the model container, input format, output format, and any additional configuration parameters.
  * **Allocate resources:** Allocate the appropriate compute resources for the endpoint based on the expected traffic and performance requirements.
  * **Configure access control:** Set up access control mechanisms to restrict access to the endpoint based on authentication and authorization policies. Access control helps ensure that only authorized users or services can interact with the deployed model.
  * **Create model endpoint:** [Create an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/using-private-endpoints) to deploy the model as a REST API service. The endpoint lets clients send requests to the endpoint and receive responses from the model.
  * **Configure monitoring and logging:** Set up monitoring and logging systems to track the endpoint's performance, resource utilization, and error logs.
  * **Deploy custom integrations:** Integrate the model into custom applications or services using the model's SDK or APIs.
  * **Deploy real-time applications:** Create a streaming pipeline that processes data and generates responses in real time.



## Log and monitor

Monitoring generative AI applications and their components requires techniques that you can add to the monitoring techniques that you use for conventional MLOps. You must log and monitor your application end-to-end, which includes logging and monitoring the overall input and output of your application and every component.

Inputs to the application trigger multiple components to produce the outputs. If the output to a given input is factually inaccurate, you must determine which of the components didn't perform well. You require lineage in your logging for all components that were executed. You must also map the inputs and components with any additional artifacts and parameters that they depend on so that you can analyze the inputs and outputs.

When applying monitoring, prioritize monitoring at the application level. If application-level monitoring proves that the application is performing well, it implies that all components are also performing well. Afterwards, apply monitoring to the prompted model components to get more granular results and a better understanding of your application.

As with conventional monitoring in MLOps, you must deploy an alerting process to notify application owners when drift, skew, or performance decay is detected. To set up alerts, you must integrate alerting and notification tools into your monitoring process.

The following sections describe monitoring skew and drift and continuous evaluation tasks. In addition, monitoring in MLOps includes monitoring the metrics for overall system health like resources utilization and latency. These [efficiency metrics](https://dora.dev/capabilities/monitoring-and-observability/) also apply to generative AI applications.

### Skew detection

Skew detection in conventional ML systems refers to training-serving skew that occurs when the feature data distribution in production deviates from the feature data distribution that was observed during model training. For generative AI applications that use pretrained models in components that are chained together to produce the output, you must also measure skew. You can measure skew by comparing the distribution of the input data that you used to evaluate your application and the distribution of the inputs to your application in production. If the two distributions drift apart, you must investigate further. You can apply the same process to the output data as well.

### Drift detection

Like skew detection, drift detection checks for statistical differences between two datasets. However, instead of comparing evaluations and serving inputs, drift looks for changes in input data. Drift lets you evaluate the inputs and therefore how the behavior of your users changes over time.

Given that the input to the application is typically text, you can use different methods to measure skew and drift. In general, these methods are trying to identify significant changes in production data, both textual (such as size of input) and conceptual (such as topics in input), when compared to the evaluation dataset. All these methods are looking for changes that could indicate the application might not be prepared to successfully handle the nature of the new data that are now coming in. Some common methods including the following:

  * Calculating embeddings and distances
  * Counting text length and number of tokens
  * Tracking vocabulary changes, new concepts and intents, prompts and topics in datasets
  * Using statistical approaches such as [least-squares density difference (PDF)](https://www.ms.k.u-tokyo.ac.jp/sugi/2014/CLSDD.pdf), [maximum mean discrepancy (MMD)](https://jmlr.csail.mit.edu/papers/v13/gretton12a.html), [learned kernel MMD (PDF)](https://arxiv.org/pdf/2203.08644.pdf), or context-aware MMD.



Because generative AI use cases are so diverse, you might require additional custom metrics that better capture unexpected changes in your data.

### Continuous evaluation

Continuous evaluation is another common approach to generative AI application monitoring. In a continuous evaluation system, you capture the model's production output and run an evaluation task using that output to keep track of the model's performance over time. You can collect direct user feedback, such as ratings, which provide immediate insight into the perceived quality of outputs. In parallel, comparing model-generated responses against established ground truth allows for deeper analysis of performance. You can collect ground truth through human assessment or as a result of an ensemble AI model approach to generate evaluation metrics. This process provides a view on how your evaluation metrics changed from when you developed your model to what you have in production today.

## Govern

In the context of MLOps, governance encompasses all the practices and policies that establish control, accountability, and transparency over the development, deployment, and ongoing management of machine learning models, including all the activities related to the code, data, and model lifecycles.

In predictive AI applications, lineage focuses on tracking and understanding the complete journey of a machine learning model. In generative AI, lineage goes beyond the model artifact to extend to all the components in the chain. Tracking includes the data, models, model lineage, code, and the relative evaluation data and metrics. Lineage tracking can help you audit, debug, and improve your models.

Along with these new practices, you can govern the data lifecycle and the generative AI component lifecycles using standard MLOps and DevOps practices.

## What's next

[Deploy a generative AI application using Agent Platform](https://docs.cloud.google.com/architecture/blueprints/genai-mlops-blueprint)

_Authors: Anant Nawalgaria, Christos Aniftos, Elia Secchi, Gabriela Hernandez Larios, Mike Styer, and Onofrio Petragallo_

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-11-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-11-19 UTC."],[],[]] 
