---
url: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence/
title: AI and ML perspective: Operational excellence \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:43.132100+00:00
---

# AI and ML perspective: Operational excellence  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  AI and ML perspective: Operational excellence Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-04-28 UTC

This document in the [Well-Architected Framework: AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) provides an overview of the principles and recommendations to build and operate robust AI and ML systems on Google Cloud. These recommendations help you set up foundational elements like observability, automation, and scalability. The recommendations in this document align with the [operational excellence pillar](https://docs.cloud.google.com/architecture/framework/operational-excellence) of the Google Cloud Well-Architected Framework.

Operational excellence within the AI and ML domain is the ability to seamlessly deploy, manage, and govern the AI and ML systems and pipelines that help drive your organization's strategic objectives. Operational excellence lets you respond efficiently to changes, reduce operational complexity, and ensure that your operations remain aligned with business goals.

The recommendations in this document are mapped to the following core principles:

  * Build a robust foundation for model development
  * Automate the model development lifecycle
  * Implement observability
  * Build a culture of operational excellence
  * Design for scalability



## Build a robust foundation for model development

To develop and deploy scalable, reliable AI systems that help you achieve your business goals, a robust model-development foundation is essential. Such a foundation enables consistent workflows, automates critical steps in order to reduce errors, and ensures that the models can scale with demand. A strong model-development foundation ensures that your ML systems can be updated, improved, and retrained seamlessly. The foundation also helps you to align your models' performance with business needs, deploy impactful AI solutions quickly, and adapt to changing requirements.

To build a robust foundation to develop your AI models, consider the following recommendations.

### Define the problems and the required outcomes

Before you start any AI or ML project, you must have a clear understanding of the business problems to be solved and the required outcomes. Start with an outline of the business objectives and break the objectives down into measurable key performance indicators (KPIs). To organize and document your problem definitions and hypotheses in a Jupyter notebook environment, use tools like [Gemini Enterprise Agent Platform Workbench](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/introduction). To implement versioning for code and documents and to document your projects, goals, and assumptions, use tools like Git. To develop and manage prompts for generative AI applications, you can use [Agent Studio on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/quickstart).

### Collect and preprocess the necessary data

To implement data preprocessing and transformation, you can use [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) (for Apache Beam), [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc-serverless/docs/overview) (for Apache Spark), or [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) if an SQL-based process is appropriate. To validate schemas and detect anomalies, use [TensorFlow Data Validation (TFDV)](https://www.tensorflow.org/tfx/data_validation/get_started) and take advantage of [automated data quality scans](https://docs.cloud.google.com/bigquery/docs/data-quality-scan) in BigQuery where applicable.

For generative AI, data quality includes accuracy, relevance, diversity, and alignment with the required output characteristics. In cases where real-world data is insufficient or imbalanced, you can generate synthetic data to help improve model robustness and generalization. To create synthetic datasets based on existing patterns or to augment training data for better model performance, use [BigQuery DataFrames](https://docs.cloud.google.com/bigquery/docs/bigquery-dataframes-introduction). Synthetic data is particularly valuable for generative AI because it can help improve prompt diversity and overall model robustness. When you build datasets for fine-tuning generative AI models, consider using the synthetic data generation capabilities in Gemini Enterprise Agent Platform.

For generative AI tasks like fine-tuning or reinforcement learning from human feedback (RLHF), ensure that labels accurately reflect the quality, relevance, and safety of the generated outputs.

### Select an appropriate ML approach

When you design your model and parameters, consider the model's complexity and computational needs. Depending on the task (such as classification, regression, or generation), consider using [Agent Platform custom training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview) for custom model building or AutoML for simpler ML tasks. For common applications, you can also access pretrained models through [Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models). You can experiment with a variety of state-of-the-art foundation models for various use cases, such as generating text, images, and code.

You might want to fine-tune a pretrained foundation model to achieve optimal performance for your specific use case. For high-performance requirements in custom training, configure [Cloud Tensor Processing Units (TPUs)](https://docs.cloud.google.com/tpu) or [GPU resources](https://docs.cloud.google.com/compute/docs/gpus) to accelerate the training and inference of deep-learning models, like large language models (LLMs) and diffusion models.

### Set up version control for code, models, and data

To manage and deploy code versions effectively, use tools like GitHub or GitLab. These tools provide robust collaboration features, branching strategies, and integration with CI/CD pipelines to ensure a streamlined development process.

Use appropriate solutions to manage each artifact of your ML system, like the following examples:

  * For code artifacts like container images and pipeline components, [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) provides a scalable storage solution that can help improve security. Artifact Registry also includes versioning and can integrate with [Cloud Build](https://docs.cloud.google.com/build/docs/overview) and [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview).
  * To manage data artifacts, like datasets used for training and evaluation, use solutions like BigQuery or [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) for storage and versioning.
  * To store metadata and pointers to data locations, use your version control system or a separate data catalog.



To maintain the consistency and versioning of your feature data, use [Agent Platform Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview). To track and manage model artifacts, including binaries and metadata, use [Model Registry on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction), which lets you store, organize, and deploy model versions seamlessly.

To ensure model reliability, implement [Model Monitoring on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview). Detect data drift, track performance, and identify anomalies in production. For generative AI systems, monitor shifts in output quality and safety compliance.

## Automate the model-development lifecycle

Automation helps you to streamline every stage of the AI and ML lifecycle. Automation reduces manual effort and standardizes processes, which leads to enhanced operational efficiency and a lower risk of errors. Automated workflows enable faster iteration, consistent deployment across environments, and more reliable outcomes, so your systems can scale and adapt seamlessly.

To automate the development lifecycle of your AI and ML systems, consider the following recommendations.

### Use a managed pipeline orchestration system

Use [Gemini Enterprise Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction) to automate every step of the ML lifecycle—from data preparation to model training, evaluation, and deployment. To accelerate deployment and promote consistency across projects, automate recurring tasks with [scheduled pipeline runs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/schedule-pipeline-run), monitor workflows with [execution metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/metrics), and develop [reusable pipeline templates](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/create-pipeline-template) for standardized workflows. These capabilities extend to generative AI models, which often require specialized steps like [prompt engineering](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies), response filtering, and [human-in-the-loop](https://cloud.google.com/discover/human-in-the-loop) evaluation. For generative AI, Agent Platform Pipelines can automate these steps, including the evaluation of generated outputs against quality metrics and safety guidelines. To improve prompt diversity and model robustness, automated workflows can also include data augmentation techniques.

### Implement CI/CD pipelines

To automate the building, testing, and deployment of ML models, use Cloud Build. This service is particularly effective when you run test suites for application code, which ensures that the infrastructure, dependencies, and model packaging meet your deployment requirements.

ML systems often need additional steps beyond code testing. For example, you need to stress test the models under varying loads, perform bulk evaluations to assess model performance across diverse datasets, and validate data integrity before retraining. To simulate realistic workloads for stress tests, you can use tools like [Locust](https://locust.io/), [Grafana k6](https://grafana.com/docs/k6/latest/), or [Apache JMeter](https://jmeter.apache.org/). To identify bottlenecks, monitor key metrics like latency, error rate, and resource utilization through [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). For generative AI, the testing must also include evaluations that are specific to the type of generated content, such as text quality, image fidelity, or code functionality. These evaluations can involve automated metrics like [perplexity](https://developers.google.com/machine-learning/glossary#perplexity) for language models or human-in-the-loop evaluation for more nuanced aspects like creativity and safety.

To implement testing and evaluation tasks, you can integrate Cloud Build with other Google Cloud services. For example, you can use Agent Platform Pipelines for automated model evaluation, [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) for large-scale data analysis, and Dataflow pipeline validation for feature validation.

You can further enhance your CI/CD pipeline by using [Agent Platform for continuous training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/continuous-training-tutorial) to enable automated retraining of models on new data. Specifically for generative AI, to keep the generated outputs relevant and diverse, the retraining might involve automatically updating the models with new training data or prompts. You can use [Agent Platform Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models) to select the latest base models that are available for tuning. This practice ensures that the models remain current and optimized for your evolving business needs.

### Implement safe and controlled model releases

To minimize risks and ensure reliable deployments, implement a model release approach that lets you detect issues early, validate performance, and roll back quickly when required.

To package your ML models and applications into container images and deploy them, use [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview). You can deploy your models to [Agent Platform endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/deployment).

Implement controlled releases for your AI applications and systems by using strategies like [canary releases](https://en.wikipedia.org/wiki/Canary_release). For applications that use managed models like Gemini, we recommend that you gradually release new application versions to a subset of users before the full deployment. This approach lets you detect potential issues early, especially when you use generative AI models where outputs can vary.

To release fine-tuned models, you can use Cloud Deploy to manage the deployment of the model versions, and use the canary release strategy to minimize risk. With managed models and fine-tuned models, the goal of controlled releases is to test changes with a limited audience before you release the applications and models to all users.

For robust validation, use [Experiments on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/intro-vertex-ai-experiments) to compare new models against existing ones, and use [Agent Platform model evaluation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction) to assess model performance. Specifically for generative AI, define evaluation metrics that align with the intended use case and the potential risks. You can use the Gen AI evaluation service in Agent Platform to assess metrics like toxicity, coherence, factual accuracy, and adherence to safety guidelines.

To ensure deployment reliability, you need a robust rollback plan. For traditional ML systems, use [Model Monitoring on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) to detect data drift and performance degradation. For generative AI models, you can track relevant metrics and set up alerts for shifts in output quality or the emergence of harmful content by using Agent Platform model evaluation along with Cloud Logging and Cloud Monitoring. Configure alerts based on generative AI-specific metrics to trigger rollback procedures when necessary. To track model lineage and revert to the most recent stable version, use insights from [Model Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction).

## Implement observability

The behavior of AI and ML systems can change over time due to changes in the data or environment and updates to the models. This dynamic nature makes observability crucial to detect performance issues, biases, or unexpected behavior. This is especially true for generative AI models because the outputs can be highly variable and subjective. Observability lets you proactively address unexpected behavior and ensure that your AI and ML systems remain reliable, accurate, and fair.

To implement observability for your AI and ML systems, consider the following recommendations.

### Monitor performance continuously

Use metrics and success criteria for ongoing evaluation of models after deployment.

You can use [Model Monitoring on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) to proactively track model performance, identify training-serving skew and prediction drift, and receive alerts to trigger necessary model retraining or other interventions. To effectively monitor for training-serving skew, construct a [golden dataset](https://developers.google.com/machine-learning/glossary#golden-dataset) that represents the ideal data distribution, and use [TFDV](https://www.tensorflow.org/tfx/data_validation/get_started) to analyze your training data and establish a baseline schema.

Configure Model Monitoring on Agent Platform to compare the distribution of input data against the golden dataset for automatic skew detection. For traditional ML models, focus on [metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) like accuracy, precision, recall, F1-score, AUC-ROC, and log loss. Define custom thresholds for alerts in Model Monitoring on Agent Platform. For generative AI, use the [Gen AI evaluation service](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview) to continuously monitor model output in production. You can also enable automatic evaluation metrics for response quality, safety, instruction adherence, grounding, writing style, and verbosity. To assess the generated outputs for quality, relevance, safety, and adherence to guidelines, you can incorporate [human-in-the-loop](https://cloud.google.com/discover/human-in-the-loop) evaluation.

Create feedback loops to automatically retrain models with Agent Platform Pipelines when Model Monitoring on Agent Platform triggers an alert. Use these insights to improve your models continuously.

### Evaluate models during development

Before you deploy your LLMs and other generative AI models, thoroughly evaluate them during the development phase. Use Agent Platform model evaluation to achieve optimal performance and to mitigate risk. Use [Agent Platform rapid evaluation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/run-evaluation) to let Google Cloud automatically run evaluations based on the dataset and prompts that you provide.

You can also define and integrate custom metrics that are specific to your use case. For feedback on generated content, integrate human-in-the-loop workflows by using Agent Platform Model Evaluation.

Use [adversarial testing](https://developers.google.com/machine-learning/guides/adv-testing) to identify vulnerabilities and potential failure modes. To identify and mitigate potential biases, use techniques like subgroup analysis and counterfactual generation. Use the insights gathered from the evaluations that were completed during the development phase to define your model monitoring strategy in production. Prepare your solution for continuous monitoring as described in the Monitor performance continuously section of this document.

### Monitor for availability

To gain visibility into the health and performance of your deployed endpoints and infrastructure, use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). For your Agent Platform endpoints, track key metrics like request rate, error rate, latency, and resource utilization, and set up alerts for anomalies. For more information, see [Cloud Monitoring metrics for Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/monitoring-metrics).

Monitor the health of the underlying infrastructure, which can include Compute Engine instances, Google Kubernetes Engine (GKE) clusters, and TPUs and GPUs. Get automated optimization recommendations from [Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist). If you use autoscaling, monitor the scaling behavior to ensure that autoscaling responds appropriately to changes in traffic patterns.

Track the status of model deployments, including canary releases and rollbacks, by integrating Cloud Deploy with Cloud Monitoring. In addition, monitor for potential security threats and vulnerabilities by using [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview).

### Set up custom alerts for business-specific thresholds

For timely identification and rectification of anomalies and issues, set up custom alerting based on thresholds that are specific to your business objectives. Examples of Google Cloud products that you can use to implement a custom alerting system include the following:

  * [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview): Collect, store, and analyze logs from all components of your AI and ML system.
  * Cloud Monitoring: Create custom dashboards to visualize key metrics and trends, and define custom metrics based on your needs. Configure alerts to get notifications about critical issues, and integrate the alerts with your incident management tools like PagerDuty or Slack.
  * [Error Reporting](https://docs.cloud.google.com/error-reporting/docs/grouping-errors): Automatically capture and analyze errors and exceptions.
  * [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview): Analyze the performance of distributed systems and identify bottlenecks. Tracing is particularly useful for understanding latency between different components of your AI and ML pipeline.
  * [Cloud Profiler](https://docs.cloud.google.com/profiler/docs/about-profiler): Continuously analyze the performance of your code in production and identify performance bottlenecks in CPU or memory usage.



## Build a culture of operational excellence

Shift the focus from just building models to building sustainable, reliable, and impactful AI solutions. Empower teams to continuously learn, innovate, and improve, which leads to faster development cycles, reduced errors, and increased efficiency. By prioritizing automation, standardization, and ethical considerations, you can ensure that your AI and ML initiatives consistently deliver value, mitigate risks, and promote responsible AI development.

To build a culture of operational excellence for your AI and ML systems, consider the following recommendations.

### Champion automation and standardization

To emphasize efficiency and consistency, embed automation and standardized practices into every stage of the AI and ML lifecycle. Automation reduces manual errors and frees teams to focus on innovation. Standardization ensures that processes are repeatable and scalable across teams and projects.

### Prioritize continuous learning and improvement

Foster an environment where ongoing education and experimentation are core principles. Encourage teams to stay up-to-date with AI and ML advancements, and provide opportunities to learn from past projects. A culture of curiosity and adaptation drives innovation and ensures that teams are equipped to meet new challenges.

### Cultivate accountability and ownership

Build trust and alignment with clearly defined roles, responsibilities, and metrics for success. Empower teams to make informed decisions within these boundaries, and establish transparent ways to measure progress. A sense of ownership motivates teams and ensures collective responsibility for outcomes.

### Embed AI ethics and safety considerations

Prioritize considerations for ethics in every stage of development. Encourage teams to think critically about the impact of their AI solutions, and foster discussions on fairness, bias, and societal impact. Clear principles and accountability mechanisms ensure that your AI systems align with organizational values and promote trust.

## Design for scalability

To accommodate growing data volumes and user demands and to maximize the value of AI investments, your AI and ML systems need to be scalable. The systems must adapt and perform optimally to avoid performance bottlenecks that hinder effectiveness. When you design for scalability, you ensure that the AI infrastructure can handle growth and maintain responsiveness. Use scalable infrastructure, plan for capacity, and employ strategies like horizontal scaling and managed services.

To design your AI and ML systems for scalability, consider the following recommendations.

### Plan for capacity and quotas

Assess future growth, and plan your infrastructure capacity and resource quotas accordingly. Work with business stakeholders to understand the projected growth and then define the infrastructure requirements accordingly.

Use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) to analyze historical resource utilization, identify trends, and project future needs. Conduct regular load testing to simulate workloads and identify bottlenecks.

Familiarize yourself with [Google Cloud quotas](https://docs.cloud.google.com/docs/quotas/view-manage) for the services that you use, such as Compute Engine, Agent Platform, and Cloud Storage. Proactively request quota increases through the Google Cloud console, and justify the increases with data from forecasting and load testing. [Monitor quota usage](https://docs.cloud.google.com/monitoring/alerts/using-quota-metrics) and set up alerts to get notifications when the usage approaches the quota limits.

To optimize resource usage based on demand, rightsize your resources, use [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms) for fault-tolerant batch workloads, and implement autoscaling.

### Prepare for peak events

Ensure that your system can handle sudden spikes in traffic or workload during peak events. Document your peak event strategy and conduct regular drills to test your system's ability to handle increased load.

To aggressively scale up resources when the demand spikes, configure autoscaling policies in [Compute Engine](https://docs.cloud.google.com/compute/docs/autoscaler) and [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler). For predictable peak patterns, consider using [predictive autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling). To trigger autoscaling based on application-specific signals, use custom metrics in Cloud Monitoring.

Distribute traffic across multiple application instances by using [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). Choose an appropriate load balancer type based on your application's needs. For geographically distributed users, you can use global load balancing to route traffic to the nearest available instance. For complex microservices-based architectures, consider using [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview).

Cache static content at the edge of Google's network by using [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview).

To cache frequently accessed data, use one of the following fully managed in-memory datastore services:

  * [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)
  * [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview)
  * [Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Decouple the components of your system by using [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) for real-time messaging and Cloud Tasks for asynchronous task execution

### Scale applications for production

To ensure scalable serving in production, you can use managed services like [Agent Platform distributed training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/distributed-training) and [Gemini Enterprise Agent Platform Inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/overview). Agent Platform Inference lets you configure the [machine types](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/configure-compute#machine-types) for your prediction nodes when you deploy a model to an endpoint or request batch predictions. For some configurations, you can add GPUs. Choose the appropriate machine type and accelerators to optimize latency, throughput, and cost.

To scale complex AI and Python applications and custom workloads across distributed computing resources, you can use [Ray on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/open-source/ray). This feature can help optimize performance and enables seamless integration with Google Cloud services. Ray on Gemini Enterprise Agent Platform simplifies distributed computing by handling cluster management, task scheduling, and data transfer. It integrates with other Agent Platform services like training, prediction, and pipelines. Ray provides fault tolerance and autoscaling, and helps you adapt the infrastructure to changing workloads. It offers a unified framework for distributed training, hyperparameter tuning, reinforcement learning, and model serving. Use Ray for distributed data preprocessing with [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) or [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview), accelerated model training, scalable hyperparameter tuning, reinforcement learning, and parallelized batch prediction.

## Contributors

Authors: 

  * [Charlotte Gistelinck, PhD](https://www.linkedin.com/in/charlottegistelinck) | Partner Engineer
  * [Sannya Dang](https://www.linkedin.com/in/thugiangdang) | AI Solution Architect
  * [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist



Other contributors: 

  * [Gary Harmson](https://www.linkedin.com/in/garyharmson) | Principal Architect
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer
  * [Ryan Cox](https://www.linkedin.com/in/ryanlcox) | Principal Architect
  * [Stef Ruinard](https://www.linkedin.com/in/stefruinard) | Generative AI Field Solutions Architect



[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml)

[ Next Security  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-28 UTC."],[],[]] 
