---
url: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization/
title: AI and ML perspective: Performance optimization \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:07.389513+00:00
---

# AI and ML perspective: Performance optimization  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  AI and ML perspective: Performance optimization Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-02-13 UTC

This document in the [Google Cloud Well-Architected Framework: AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) provides principles and recommendations to help you optimize the performance of your AI and ML workloads on Google Cloud. The recommendations in this document align with the [performance optimization pillar](https://docs.cloud.google.com/architecture/framework/performance-optimization) of the Well-Architected Framework.

AI and ML systems enable advanced automation and decision-making capabilities for your organization. The performance of these systems can directly affect important business drivers like revenue, costs, and customer satisfaction. To realize the full potential of AI and ML systems, you must optimize their performance based on your business goals and technical requirements. The performance optimization process often involves trade-offs. For example, a design choice that provides the required performance might lead to higher costs. The recommendations in this document prioritize performance over other considerations.

To optimize AI and ML performance, you need to make decisions regarding factors like the model architecture, parameters, and training strategy. When you make these decisions, consider the entire lifecycle of the AI and ML systems and their deployment environment. For example, very large LLMs can be highly performant on massive training infrastructure, but might not perform well in capacity-constrained environments like mobile devices.

The recommendations in this document are mapped to the following core principles:

  * Establish performance objectives and evaluation methods
  * Run and track frequent experiments
  * Build and automate training and serving infrastructure
  * Match design choices to performance requirements
  * Link performance metrics to design and configuration choices



## Establish performance objectives and evaluation methods

Your business strategy and goals are the foundation for leveraging AI and ML technologies. Translate your business goals into measurable key performance indicators (KPIs). Examples of KPIs include total revenue, costs, conversion rate, retention or churn rate, customer satisfaction, and employee satisfaction.

### Define realistic objectives

According to [site reliability engineering (SRE) best practices](https://sre.google/sre-book/service-level-objectives/#objectives-g0s1tdcz), the objectives of a service must reflect a performance level that satisfies the requirements of typical customers. This means that service objectives must be realistic in terms of scale and feature performance.

Unrealistic objectives can lead to wasted resources for minimal performance gains. Models that provide the highest performance might not lead to optimal business outcomes. Such models might require more time and cost to train and run.

When you define objectives, distinguish between and prioritize quality and performance objectives:

  * _Quality_ refers to inherent characteristics that determine the value of an entity. It helps you assess whether the entity meets your expectations and standards.
  * _Performance_ refers to how efficiently and effectively an entity functions or carries out its intended purpose.



ML engineers can improve the performance metrics of a model during the training process. Gemini Enterprise Agent Platform provides an [evaluation service](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction) that ML engineers can use to implement standardized and repeatable tracking of quality metrics. The _prediction efficiency_ of a model indicates how well a model performs in production or at inference time. To monitor performance, use [Cloud Monitoring](https://docs.cloud.google.com/monitoring#documentation) and [Model Monitoring on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview). To select appropriate models and decide how to train them, you must translate business goals into technical requirements that determine quality and performance metrics.

To understand how to set realistic objectives and identify appropriate performance metrics, consider the following example for an AI-powered fraud detection system:

  * **Business objective** : For a fraud detection system, an unrealistic business objective is to detect 100% of fraudulent transactions accurately within one nanosecond at a peak traffic of 100 billion transactions per second. A more realistic objective is to detect fraudulent transactions with 95% accuracy in 100 milliseconds for 90% of online predictions during US working hours at a peak volume of one million transactions per second.
  * **Performance metrics** : Detecting fraud is a classification problem. You can measure the quality of a fraud detection system by using metrics like [recall](https://developers.google.com/machine-learning/glossary#recall), [F1 score](https://developers.google.com/machine-learning/glossary#f1), and [accuracy](https://developers.google.com/machine-learning/glossary#accuracy). To track system performance or speed, you can measure inference latency. Detecting potentially fraudulent transactions might be more valuable than accuracy. Therefore, a realistic goal might be a high recall with a p90 latency that's less than 100 milliseconds.



### Monitor performance at all stages of the model lifecycle

During experimentation and training and after model deployment, monitor your KPIs and observe any deviations from the business objectives. A comprehensive monitoring strategy helps you make critical decisions about model quality and resource utilization, such as the following:

  * Decide when to stop a training job.
  * Determine whether a model's performance is degrading in production.
  * Improve the cost and time-to-market for new models.



#### Monitoring during experimentation and training

The objective of the experimentation stage is to find the optimal overall approach, model architecture, and hyperparameters for a specific task. Experimentation helps you iteratively determine the configuration that provides optimal performance and how to train the model. Monitoring helps you efficiently identify potential areas of improvement.

To monitor a model's quality and training efficiency, ML engineers must do the following:

  * Visualize model quality and performance metrics for each trial.
  * Visualize model graphs and metrics, such as histograms of weights and biases.
  * Visually represent training data.
  * Profile training algorithms on different hardware.



To monitor experimentation and training, consider the following recommendations:

Monitoring aspect | Recommendation  
---|---  
Model quality | To visualize and track experiment metrics like accuracy and to visualize model architecture or training data, use [TensorBoard](https://www.tensorflow.org/tensorboard/get_started). TensorBoard is an open-source suite of tools that's compatible with ML frameworks like the following:

  * [XGBoost](https://xgboost.readthedocs.io/en/stable/python/callbacks.html)
  * [JAX](https://docs.jax.dev/en/latest/profiling.html#tensorboard-profiling)
  * [Flax](https://github.com/google/flax/blob/main/flax/metrics/tensorboard.py)
  * [PyTorch](https://pytorch.org/docs/stable/tensorboard.html)
  * [PyTorch with accelerated linear algebra (XLA)](https://docs.cloud.google.com/tpu/docs/pytorch-xla-performance-profiling-tpu-vm#analysis_in_tensorboard) for TPU training
  * [TensorFlow](https://www.tensorflow.org/tensorboard/get_started)

  
Experiment tracking | [Experiments on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/intro-vertex-ai-experiments) integrates with managed enterprise-grade [Agent Platform TensorBoard](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/tensorboard-introduction) instances to support experiment tracking. This integration enables reliable storage and sharing of logs and metrics. To let multiple teams and individuals track experiments, we recommend that you use the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege).   
Training and experimentation efficiency | Agent Platform exports metrics to [Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) and collects telemetry data and logs by using an observability agent. You can visualize the metrics in the Google Cloud console. Alternatively, create dashboards or alerts based on these metrics by using Monitoring. For more information, see [Monitoring metrics for Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/monitoring-metrics).   
NVIDIA GPUs | The [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) enables GPU monitoring for Compute Engine and for [other products that Ops Agent supports](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_vms).  You can also use the [NVIDIA Data Center GPU Manager (DCGM)](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party-nvidia), which is a suite of tools for managing and monitoring NVIDIA GPUs in cluster environments. Monitoring NVIDIA GPUs is particularly useful for training and serving deep learning models.  
Deep debugging | To debug problems with the training code or the configuration of a Gemini Enterprise Agent Platform Managed Training job, you can inspect the training container by using an [interactive shell session](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/monitor-debug-interactive-shell).  
  
#### Monitoring during serving: Streaming prediction

After you train a model and export it to [Model Registry on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction), you can create a [Agent Platform endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/deployment). This endpoint provides an HTTP endpoint for the model.

[Model Monitoring on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) helps you identify large changes in the distribution of input or output features. You can also monitor [feature attributions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview#v2-objectives) in production when compared to a baseline distribution. The baseline distribution can be the training set or it can be based on past distributions of production traffic. A change in the serving distribution might imply a reduction in predictive performance compared to training.

  * **Choose a monitoring objective** : Depending on the sensitivity of a use case to changes in the data that's provided to the model, you can [monitor different types of objectives](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview#v2-objectives): input feature drift, output drift, and feature attribution. [Model Monitoring on Agent Platform v2](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview#v2) lets you monitor models that you deploy on a managed serving platform like Agent Platform and also on self-hosted services like Google Kubernetes Engine (GKE). In addition, for granular performance tracking, you can monitor parameters at the model level rather than for an endpoint.
  * **Monitor generative AI model serving** : To ensure stability and minimize latency, particularly for LLM endpoints, set up a robust monitoring stack. [Gemini](https://docs.cloud.google.com/gemini/docs/overview) models provide [built-in metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/use-provisioned-throughput#metrics), like time to first token (TTFT), which you can access directly in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). To monitor throughput, latency, and error rates across all Google Cloud models, use the [model observability dashboard](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-observability#view).



#### Monitoring during serving: Batch prediction

To monitor batch prediction, you can run standard evaluation jobs in the [Agent Platform evaluation service](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction). Model Monitoring on Agent Platform supports monitoring of [batch inferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/model-monitoring-batch-predictions). If you use Batch to run your serving workload, you can monitor resource consumption by using the [metrics in Metrics Explorer](https://docs.cloud.google.com/batch/docs/monitor-job-resources-using-metrics).

### Automate evaluation for reproducibility and standardization

To transition models from prototypes to reliable production systems, you need a standardized evaluation process. This process helps you track progress across iterations, compare different models, detect and mitigate bias, and ensure that you meet regulatory requirements. To ensure reproducibility and scalability, you must automate the evaluation process.

To standardize and automate the evaluation process for ML performance, complete the following steps:

  1. Define quantitative and qualitative indicators.
  2. Choose appropriate data sources and techniques.
  3. Standardize the evaluation pipeline.



These steps are described in the following sections.

#### 1\. Define quantitative and qualitative indicators

_Computation-based metrics_ are calculated by using numeric formulas. Remember that [training loss](https://developers.google.com/machine-learning/glossary#training-loss) metrics might differ from the evaluation metrics that are relevant to business goals. For example, a model that's used for supervised fraud detection might use [cross-entropy loss](https://developers.google.com/machine-learning/glossary#cross-entropy) for training. However, to evaluate inference performance, a more relevant metric might be [recall](https://developers.google.com/machine-learning/glossary#recall), which indicates the coverage of fraudulent transactions. Agent Platform provides an evaluation service for metrics like recall, precision, and area under the precision-recall curve (AuPRC). For more information, see [Model evaluation in Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction).

_Qualitative indicators_ , such as the fluency or entertainment value of generated content, can't be objectively computed. To evaluate these indicators, you can use the [LLM-as-a-judge](https://en.wikipedia.org/wiki/LLM-as-a-Judge) strategy or human labeling services like [Labelbox](https://docs.cloud.google.com/architecture/partners/model-development-data-labeling-labelbox-google-cloud).

#### 2\. Choose appropriate data sources and techniques

An evaluation is statistically significant when it runs on a certain minimum volume of varied examples. Choose the datasets and techniques that you use for evaluations by using approaches such as the following:

  * **Golden dataset** : Use trusted, consistent, and accurate data samples that reflect the probability distribution of a model in production.
  * **LLM-as-a-judge** : Evaluate the output of a generative model by using an LLM. This approach is relevant only to tasks where an LLM can evaluate a model.
  * **User feedback** : To guide future improvements, capture direct user feedback as a part of production traffic.



Depending on the evaluation technique, size and type of evaluation data, and frequency of evaluation, you can use BigQuery or Cloud Storage as data sources, including for the Agent Platform evaluation service.

  * BigQuery lets you use SQL commands to run inference tasks like natural language processing and machine translation. For more information, see [Task-specific solutions overview](https://docs.cloud.google.com/bigquery/docs/ai-application-overview).
  * Cloud Storage provides a [cost-efficient storage solution](https://docs.cloud.google.com/architecture/storage-advisor#object-storage) for large datasets.



#### 3\. Standardize the evaluation pipeline

To automate the evaluation process, consider the following services and tools:

  * [**Agent Platform evaluation service**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/using-model-evaluation): Provides ready-to-use primitives to track model performance as a part of the ML lifecycle on Agent Platform.
  * [**Gen AI evaluation service**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview): Lets you evaluate any generative model or application and benchmark the evaluation results against your own judgment and evaluation criteria. This service also helps you perform specialized tasks like prompt engineering, retrieval-augmented generation (RAG), and AI agent optimization.
  * [**Agent Platform automatic side-by-side (AutoSxS) tool**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/side-by-side-eval): Supports pairwise model-based evaluation.
  * [**Kubeflow**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/gcpc-list#modeleval_components): Provides special components to run model evaluations.



## Run and track frequent experiments

To effectively optimize ML performance, you need a dedicated, powerful, and interactive platform for experimentation. The platform must have the following capabilities:

  * Facilitate iterative development, so that teams can move from idea to validated results with speed, reliability, and scale.
  * Let teams efficiently discover optimal configurations that they can use to trigger training jobs.
  * Provide controlled access to relevant data, features, and tools to perform and track experiments.
  * Support reproducibility and data lineage tracking.



### Treat data as a service

Isolate experimental workloads from production systems and set up appropriate security controls for your data assets by using the following techniques:

Technique | Description | Benefits  
---|---|---  
Resource isolation | [Isolate the resources for different environments](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy#option1) in separate Google Cloud projects. For example, provision the resources for development, staging, and production environments in separate projects like `ml-dev`, `ml-staging`, and `ml-prod`. | Resource isolation helps to prevent experimental workloads from consuming resources that production systems need. For example, if you use a single project for experiments _and_ production, an experiment might consume all of the available NVIDIA A100 GPUs for Agent Platform Managed Training. This might cause interruptions in the retraining of a critical production model.  
Identity and access control | Apply the principles of [zero trust and least privilege](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust) and use workload-specific service accounts. Grant access by using predefined Identity and Access Management (IAM) roles like [Agent Platform User](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`). | This approach helps to prevent accidental or malicious actions that might corrupt experiments.  
Network security | Isolate network traffic by using [Virtual Private Cloud (VPC) networks](https://docs.cloud.google.com/vpc/docs/vpc) and enforce security perimeters by using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).  | This approach helps to protect sensitive data and prevents experimental traffic from affecting production services.  
Data isolation | Store experimental data in separate Cloud Storage buckets and BigQuery datasets. | Data isolation prevents accidental modification of production data. For example, without data isolation, an experiment might inadvertently alter the feature values in a shared BigQuery table, which might lead to a significant degradation in model accuracy in the production environment.  
  
### Equip teams with appropriate tools

To establish a curated set of tools to accelerate the entire experimentation lifecycle—from data exploration to model training and analysis—use the following techniques:

  * **Interactive prototyping** : For rapid data exploration, hypothesis testing, and code prototyping, use Colab Enterprise or managed JupyterLab instances on Gemini Enterprise Agent Platform Workbench. For more information, see [Choose a notebook solution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/notebook-solution).
  * **Scalable model training** : Run training jobs on a managed service that supports distributed training and scalable compute resources like GPUs and TPUs. This approach helps to reduce training time from days to hours and enables more parallel experimentation. For more information, see Use specialized components for training.
  * **In-database ML** : Train models directly in [BigQuery ML using SQL](https://docs.cloud.google.com/bigquery/docs/bqml-introduction). This technique helps to eliminate data movement and accelerates experimentation for analysts and SQL-centric users.
  * **Tracking experiments** : Create a searchable and comparable history of experiment data by logging parameters, metrics, and artifacts for every experiment run. For more information, see Build a data and model lineage system.
  * **Optimizing generative AI** : To optimize the performance of generative AI applications, you must experiment with prompts, model selection, and fine-tuning. For rapid prompt engineering, use [Agent Studio on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/quickstart). To experiment with foundation models (like Gemini) and find a model that's appropriate for your use case and business goals, use [Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models).



### Standardize for reproducibility and efficiency

To ensure that experiments consume resources efficiently and produce consistent and trustworthy results, standardize and automate experiments by using the following approaches:

  * **Ensure consistent environments by using containers** : Package your training code and dependencies as Docker containers. Manage and serve the containers by using [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker). This approach lets you reproduce issues on different machines by repeating experiments in identical environments. Agent Platform provides [prebuilt containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/pre-built-containers) for serverless training.
  * **Automate ML workflows as pipelines** : Orchestrate the end-to-end ML workflow as a codified pipeline by using [Gemini Enterprise Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction). This approach helps to enforce consistency, ensure reproducibility, and automatically track all of the artifacts and metadata in [Agent Platform ML Metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/introduction).
  * **Automate provisioning with infrastructure-as-code (IaC)** : Define and deploy standardized experimentation environments by using IaC tools like [Terraform](https://docs.cloud.google.com/docs/terraform/terraform-overview). To ensure that every project adheres to a standardized set of configurations for security, networking, and governance, use [Terraform modules](https://developer.hashicorp.com/terraform/language/modules).



## Build and automate training and serving infrastructure

To train and serve AI models, set up a robust platform that supports efficient and reliable development, deployment, and serving. This platform lets your teams efficiently improve the quality and performance of training and serving in the long run.

### Use specialized components for training

A reliable training platform helps to accelerate performance and provides a standardized approach to automate repeatable tasks in the ML lifecycle–from data preparation to model validation.

  * **Data collection and preparation** : For effective model training, you need to collect and prepare the data that's necessary for training, testing, and validation. The data might come from different sources and be of different data types. You also need to reuse relevant data across training runs and share features across teams. To improve the repeatability of the data collection and preparation phase, consider the following recommendations:

    * Improve data discoverability with [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview).
    * Centralize feature engineering in [Agent Platform Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview).
    * Preprocess data by using [Dataflow](https://docs.cloud.google.com/dataflow/docs).
  * **Training execution** : When you train a model, you use data to create a model object. To do this, you need to set up the necessary infrastructure and dependencies of the training code. You also need to decide how to persist the training models, track training progress, evaluate the model, and present the results. To improve training repeatability, consider the following recommendations:

    * Follow the guidelines in Automate evaluation for reproducibility and standardization.
    * To submit training jobs on one or more worker nodes without managing the underlying infrastructure provisioning or dependencies, use the [`CustomJob`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/create-custom-job#before) resource in Agent Platform Managed Training. You can also use the `CustomJob` resource for [hyperparameter tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/using-hyperparameter-tuning) jobs.
    * Optimize scheduling goodput by leveraging [Dynamic Workload Scheduler](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/schedule-jobs-dws#enable-dws) or [reservations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/use-reservations) for Agent Platform Managed Training.
    * Register your models to [Model Registry on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction).
  * **Training orchestration** : Deploy training workloads as stages of a pipeline by using [Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction). This service provides managed [Kubeflow](https://www.kubeflow.org/) and [TFX](https://www.tensorflow.org/tfx) services. Define each step of the pipeline as a [component](https://www.kubeflow.org/docs/components/) that runs in a container. Each component works like a function, with input parameters and output artifacts that become inputs to the subsequent components in the pipeline. To optimize the efficiency of your pipeline, consider the recommendations in the following table:

Goal | Recommendations  
---|---  
Implement core automation. | 
    * Use [Kubeflow Pipelines components](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/gcpc-list).
    * Use [Control Flows](https://www.kubeflow.org/docs/components/pipelines/user-guides/core-functions/control-flow/) for advanced pipeline designs, such as conditional gates.
    * Integrate the [pipeline compilation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/build-pipeline#compile_your_pipeline_into_a_yaml_file) as a part of your CI/CD flow.
    * Execute the pipeline with [Cloud Scheduler](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/schedule-pipeline-run).   
Increase speed and cost efficiency. | 
    * To increase the speed of iterations and reduce cost, use the [execution cache](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-caching) of Agent Platform Pipelines.
    * [Specify the machine configuration](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/machine-types) for each component based on the resource requirements of each step.   
Increase robustness. | 
    * To increase robustness against temporary issues without requiring manual intervention, configure [retries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-retries).
    * To [_fail fast_](https://en.wikipedia.org/wiki/Fail-fast_system) and iterate efficiently, configure a [failure policy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-failure-policy).
    * To handle failures, [configure email notifications](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications).   
Implement governance and tracking. | 
    * To experiment with different model configurations or training configurations, [add pipeline runs to experiments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction#experiments).
    * Monitor [logs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/logging) and [metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/metrics) for Agent Platform Pipelines.
    * Follow the recommendations in Monitor performance at all stages of the model lifecycle.   



### Use specialized infrastructure for prediction

To reduce the toil of managing infrastructure and model deployments, automate the repeatable task flows. A service-oriented approach lets you focus on speed and faster [time to value (TTV)](https://en.wikipedia.org/wiki/Time_to_value). Consider the following recommendations:

Recommendation | Techniques  
---|---  
Implement automatic deployment. | 

  * After a model is trained, use automation to deploy the model. Agent Platform Pipelines provides [specialized components](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/gcpc-list#endpoint_components) for deploying models to Agent Platform endpoints. You can manage automatic deployment by using [Kubeflow Control Flows](https://www.kubeflow.org/docs/components/pipelines/user-guides/core-functions/control-flow/). 
  * To decide whether to deploy a model based on an evaluation against a validation set, take advantage of the [evaluation components](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/model-evaluation-component) of the pipeline. You can automate deployment for batch inference by using specialized [batch prediction components](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/batchprediction-component) in Agent Platform.

  
Take advantage of managed scaling features. | 

  * [Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/get-predictions) provides batch and online inference capabilities that let you configure the [scaling behavior](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/deployment#scaling).
  * Cloud Run supports [autoscaling GPUs](https://docs.cloud.google.com/run/docs/configuring/services/gpu-best-practices#autoscaling-and-gpu). 

  
Optimize latency and throughput on Agent Platform endpoints.  | 

  * Choose an appropriate [machine type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/configure-compute).
  * Choose an appropriate [endpoint type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/choose-endpoint-type) for your models. [Dedicated private endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/private-service-connect) might help to reduce latency.
  * If you use Feature Store, choose an appropriate online serving type. Optimized online serving with Private Service Connect might provide low latency. For more information, see [Online service types](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/online-serving-types). 

  
Optimize resource utilization. | 

  * To optimize resource utilization, you can [share resources across model deployments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/model-co-hosting). Instead of using a separate VM for each model (default behavior), you can deploy several models on a single VM.
  * To assure or optimize resource availability, use [reservations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/use-reservations), [Dynamic Workload Scheduler](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/use-flex-start-vms), or [Spot VMs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/use-spot-vms).

  
Optimize model deployment. | 

  * To avoid breaking changes, you can perform gradual migration and implement A/B testing by automatically [deploying several models to the same endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/deployment#models-endpoint). Agent Platform decouples the endpoint layer from the models, which lets you split traffic between model versions.
  * To replace a deployed model, use a [rolling deployment strategy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/rolling-deployment). 

  
Monitor performance. | 

  * To improve serving performance in production, observe [logs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/online-prediction-logging) and [inference metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/view-endpoint-metrics) for Agent Platform endpoints. To understand the behavior of models in production, you need tools to monitor quality and performance. [Model Monitoring on Agent Platform v2](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/set-up-model-monitoring) lets you monitor several versions of a model and iterate rapidly. 

  
  
## Match design choices to performance requirements

When you make design choices to improve performance, assess whether the choices support your business requirements or are wasteful and counterproductive. To choose appropriate infrastructure, models, and configurations, identify performance bottlenecks and assess how they're linked to performance metrics. For example, even on very powerful GPU accelerators, training tasks can experience performance bottlenecks. These bottlenecks can be caused by data I/O issues in the storage layer or by performance limitations of the model.

### Focus on holistic performance of the ML flow

As training requirements grow in terms of model size and cluster size, the failure rate and infrastructure costs might increase. Therefore, the cost of failure might increase quadratically. You can't rely solely on conventional resource-efficiency metrics like [model FLOPs utilization (MFU)](https://arxiv.org/pdf/2204.02311#page=66.09). To understand why MFU might not be a sufficient indicator of overall training performance, examine the lifecycle of a typical training job. The lifecycle consists of the following cyclical flow:

  1. **Cluster creation** : Worker nodes are provisioned.
  2. **Initialization** : Training is initialized on the worker nodes.
  3. **Training execution** : Resources are used for forward or backward propagation.
  4. **Interruption** : The training process is interrupted during model checkpointing or due to worker-node preemptions.



After each interruption, the preceding flow is repeated.

The training execution step constitutes a fraction of the lifecycle of an ML job. Therefore, the utilization of worker nodes for the training execution step doesn't indicate the overall efficiency of the job. For example, even if the training execution step runs at 100% efficiency, the overall efficiency might be low if interruptions occur frequently or if it takes a long time to resume training after interruptions.

#### Adopt and track goodput metrics

To ensure holistic performance measurement and optimization, shift your focus from conventional resource-efficiency metrics like MFU to _goodput_. Goodput considers the availability and utilization of your clusters and compute resources, and it helps to measure resource efficiency across multiple layers.

The focus of goodput metrics is the _overall progress_ of a job rather than whether the job _appears to be busy_. Goodput metrics help you optimize training jobs for tangible overall gains in productivity and performance.

Goodput gives you a granular understanding of potential losses in efficiency through the following metrics:

  * _Scheduling goodput_ is the fraction of time when all of the resources that are required for training or serving are available for use.
  * _Runtime goodput_ represents the proportion of useful training steps that are completed during a given period.
  * _Program goodput_ is the peak hardware performance or MFU that a training job can extract from the accelerator. It depends on efficient utilization of the underlying compute resources during training.



#### Optimize scheduling goodput

To optimize scheduling goodput for a workload, you must identify the specific infrastructure requirements of the workload. For example, batch inference, streaming inference, and training have different requirements:

  * Batch inference workloads might accommodate some interruptions and delays in resource availability.
  * Streaming inference workloads require stateless infrastructure.
  * Training workloads require longer term infrastructure commitments.



##### Choose appropriate obtainability modes

In cloud computing, _obtainability_ is the ability to provision resources when they're required. Google Cloud provides the following obtainability modes:

  * **On-demand VMs** : You provision Compute Engine VMs when they're needed and run your workloads on the VMs. The provisioning request is subject to the availability of resources, such as GPUs. If a sufficient quantity of a requested resource type isn't available, the request fails.
  * [**Spot VMs**](https://docs.cloud.google.com/compute/docs/instances/spot): You create VMs by using unused compute capacity. Spot VMs are billed at a discounted price when compared to on-demand VMs, but Google Cloud might [_preempt_](https://docs.cloud.google.com/compute/docs/instances/spot#preemption) Spot VMs at any time. We recommend that you use Spot VMs for stateless workloads that can fail gracefully when the host VMs are preempted.
  * [**Reservations**](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type): You reserve capacity as a pool of VMs. Reservations are ideal for workloads that need capacity assurance. Use reservations to maximize scheduling goodput by ensuring that resources are available when required.
  * [**Dynamic Workload Scheduler**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest): This provisioning mechanism queues requests for GPU-powered VMs in a dedicated pool. Dynamic Workload Scheduler helps you avoid the constraints of the other obtainability modes:

    * Stock-out situations in the on-demand mode.
    * Statelessness constraint and preemption risk of Spot VMs.
    * Cost and availability implications of reservations.



The following table summarizes the obtainability modes for Google Cloud services and provides links to relevant documentation:

Product | On-demand VMs | Spot VMs | Reservations | Dynamic Workload Scheduler  
---|---|---|---|---  
Compute Engine | [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) | [About Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) | [About reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) | [Create a MIG with GPU VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms)  
GKE | [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools) | [About Spot VMs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#overview) | [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations) | [GPU, TPU, and H4D consumption with flex-start provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws)  
Cloud Batch | [Create and run a job](https://docs.cloud.google.com/batch/docs/create-run-example-job) | [Batch job with Spot VMs](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#provisioningmodel) | [Ensure resource availability using VM reservations](https://docs.cloud.google.com/batch/docs/create-run-job-reservation) | [Use GPUs and flex-start VMs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#use-gpu-vms-dws)  
Agent Platform Managed Training | [Create a serverless training job](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/create-custom-job) | [Use Spot VMs for training jobs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/use-spot-vms) | [Use reservations for training jobs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/use-reservations) | [Schedule training jobs based on resource availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/schedule-jobs-dws)  
Agent Platform | Get [batch inferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/get-batch-predictions) and [online inferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/get-online-predictions) from custom-trained models. | [Use Spot VMs for inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/use-spot-vms) | [Use reservations for online inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/use-reservations) | [Use flex-start VMs for inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/use-flex-start-vms)  
  
##### Plan for maintenance events

You can improve scheduling goodput by anticipating and planning for infrastructure maintenance and upgrades.

  * GKE lets you control when automatic cluster maintenance can be performed on your clusters. For more information, see [Maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).

  * Compute Engine provides the following capabilities:

    * To keep an instance running during a host event, such as planned maintenance for the underlying hardware, Compute Engine performs a _live migration_ of the instance to another host in the same zone. For more information, see [Live migration process during maintenance events](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).
    * To control how an instance responds when the underlying host requires maintenance or has an error, you can [set a host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options) for the instance.
  * For information about planning for host events that are related to large training clusters in AI Hypercomputer, see [Manage host events across compute instances](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events).




#### Optimize runtime goodput

The model training process is frequently interrupted by events like model checkpointing and resource preemption. To optimize runtime goodput, you must ensure that the system resumes training and inference efficiently after the required infrastructure is ready and after any interruption.

During model training, AI researchers use checkpointing to track progress and minimize the learning lost due to resource preemptions. Larger model sizes make checkpointing interruptions longer, which further affects overall efficiency. After interruptions, the training application must be restarted on every node in the cluster. These restarts can take some time because the necessary artifacts must be reloaded.

To optimize runtime goodput, use the following techniques:

Technique | Description  
---|---  
Implement automatic checkpointing. | Frequent checkpointing lets you track the progress of training at a granular level. However, the training process is interrupted for each checkpoint, which reduces runtime goodput. To minimize interruptions, you can set up automatic checkpointing, where the host's [SIGTERM](https://en.wikipedia.org/wiki/Signal_\(IPC\)#SIGTERM) signal triggers the creation of a checkpoint. This approach limits checkpointing interruptions to when the host needs maintenance. Remember that some hardware failures might not trigger SIGTERM signals; therefore, you must find a suitable balance between automatic checkpointing and SIGTERM events. You can set up automatic checkpointing by using the following techniques:

  * Preserve training progress on TPUs by using [autocheckpoint](https://docs.cloud.google.com/tpu/docs/autocheckpoint). 
  * Use the built-in automatic checkpointing in the [MaxText](https://github.com/AI-Hypercomputer/maxtext) framework.
  * Configure host maintenance notifications for [GPUs](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance) and [TPUs](https://docs.cloud.google.com/tpu/docs/view-maintenance-notifications).
  * Use [Orbax](https://github.com/google/orbax/blob/main/README.md) for ML using JAX.
  * Implement [multi-tier checkpointing in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/training/multi-tier-checkpointing). 

  
Use appropriate container-loading strategies. | In a GKE cluster, before nodes can resume training jobs, it might take some time to complete loading the required artifacts like data or model checkpoints. To reduce the time that's required to reload data and resume training, use the following techniques:

  * Preload data or container images by using [secondary boot disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading).
  * Pull container images by using [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming).
  * Use [larger persistent disks](https://docs.cloud.google.com/compute/docs/disks/performance#performance_limits) or provision ephemeral storage by using [Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local-ssd-perf-nvme).
  * Build and decompress images by using [Zstandard](https://github.com/facebook/zstd/blob/dev/README.md).
  * Preload container images by using [DaemonSets](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/automatically-bootstrapping-gke-nodes-with-daemonsets). 

  
Use the compilation cache. | If training requires a compilation-based stack, check whether you can use a compilation cache. When you use a compilation cache, the computation graph isn't recompiled after each training interruption. The resulting reductions in time and cost are particularly beneficial when you use TPUs. [JAX](https://docs.jax.dev/en/latest/persistent_compilation_cache.html#google-cloud) lets you store the compilation cache in a Cloud Storage bucket and then use the cached data in the case of interruptions.  
  
#### Optimize program goodput

Program goodput represents peak resource utilization during training, which is the conventional way to measure training and serving efficiency. To improve program goodput, you need an optimized distribution strategy, efficient compute-communication overlap, optimized memory access, and efficient pipelines.

To optimize program goodput, use the following strategies:

Strategy | Description  
---|---  
Use framework-level customization options. | Frameworks or compilers like [Accelerated Linear Algebra (XLA)](https://openxla.org/xla) provide many key components of program goodput. To further optimize performance, you can customize fundamental components of the computation graph. For example, [Pallas](https://docs.jax.dev/en/latest/pallas/tpu/) supports custom kernels for TPUs and GPUs.  
Offload memory to the host DRAM. | For large-scale training, which requires significantly high memory from accelerators, you can offload some memory usage to the host DRAM. For example, XLA lets you [offload model activations](https://github.com/pytorch/xla/tree/master/examples/host_offloading) from the forward pass to the host memory instead of using the accelerator's memory. With this strategy, you can improve training performance by increasing the model capacity or the batch size.  
Leverage [quantization](https://en.wikipedia.org/wiki/Large_language_model#Quantization) during training. | You can improve training efficiency and program goodput by leveraging model quantization during training. This strategy reduces the precision of the gradients or weights during certain steps of the training; therefore, program goodput improves. However, this strategy might require additional engineering effort during model development. For more information, see the following resources:

  * [Quantization-aware training on TensorFlow](https://www.tensorflow.org/model_optimization/guide/quantization/training_comprehensive_guide)
  * [Quantization-aware training on PyTorch](https://pytorch.org/blog/quantization-aware-training/)
  * [Qwix: a quantization library for JAX](https://github.com/google/qwix/blob/main/README.md)

  
Implement parallelism. | To increase the utilization of the available compute resources, you can use parallelism strategies at the model level during training and when loading data. For information about model parallelism, see the following:

  * [Pipeline parallelism on PyTorch](https://docs.pytorch.org/docs/stable/distributed.pipelining.html)
  * [Pipeline parallelism on GPUs with JAX](https://docs.jax.dev/en/latest/gpu_performance_tips.html#pipeline-parallelism-on-gpu)
  * [Pipeline parallelism in DeepSpeed](https://www.deepspeed.ai/tutorials/pipeline/)

To achieve data parallelism, you can use tools like the following:

  * [FSDP](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) on PyTorch
  * Distributed training on [TensorFlow](https://www.tensorflow.org/guide/distributed_training) or [Keras](https://keras.io/guides/distribution/)
  * [Distributed data loading](https://docs.jax.dev/en/latest/distributed_data_loading.html) with JAX

  
  
### Focus on workload-specific requirements

To ensure that your performance optimization efforts are effective and holistic, you must match optimization decisions to the specific requirements of your training and inference workloads. Choose appropriate AI models and use relevant prompt optimization strategies. Select appropriate frameworks and tools based on the requirements of your workloads.

#### Identify workload-specific requirements

Evaluate the requirements and constraints of your workloads across the following areas:

Area | Description  
---|---  
Task and quality requirements | Define the core task of the workload and the performance baseline. Answer questions like the following:

  * Does the task involve regression, classification, or generation?
  * What is the minimum acceptable quality: for example, accuracy, precision, or recall?

  
Serving context | Analyze the operational environment where you plan to deploy the model. The serving context often has a significant impact on design decisions. Consider the following factors:

  * **Latency** : Does the system need real-time, synchronous predictions, or is an asynchronous, batch process acceptable? 
  * **Connectivity** : Do you need to run the model offline or on an edge device?
  * **Volume** : What are the expected average and peak levels for prediction load? The load levels influence your decisions regarding scaling strategies and infrastructure.

  
Team skills and economics | Assess the business value of buying the solution against the cost and complexity of building and maintaining it. Determine whether your team has the specialized skills that are required for custom model development or whether a managed service might provide faster time to value.   
  
#### Choose an appropriate model

If an API or an open model can deliver the required performance and quality, use that API or model.

  * For modality-specific tasks like optical character recognition (OCR), labeling, and content moderation, choose ML APIs like the following:

    * [Cloud Natural Language API](https://docs.cloud.google.com/natural-language/docs/reference/rest)
    * [Cloud Vision API](https://docs.cloud.google.com/vision/docs/detect-labels-image-api)
    * [Video Intelligence API](https://docs.cloud.google.com/video-intelligence/docs/features)
    * [Speech-to-Text API](https://docs.cloud.google.com/speech-to-text/docs/overview)
    * [Text-to-Speech API](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)
    * [Cloud Translation API](https://docs.cloud.google.com/translate/docs/overview)
  * For generative AI applications, consider Google models like [Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models#gemini-models), [Imagen](https://deepmind.google/models/imagen/), and [Veo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models#veo-models).

Explore [Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models) and choose from a curated collection of foundation and task-specific Google models. Model Garden also provides open models like Gemma and third-party models, which you can run in Agent Platform or deploy on runtimes like GKE.

  * If a task can be completed by using either an ML API or a generative AI model, consider the complexity of the task. For complex tasks, large models like Gemini might provide higher performance than smaller models.




#### Improve quality through better prompting

To improve the quality of your prompts at scale, use the [Agent Platform prompt optimizer](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-optimizer). You don't need to manually rewrite system instructions and prompts. The prompt optimizer supports the following approaches:

  * **Zero-shot optimization** : A low-latency approach that improves a single prompt or system instruction in real time.
  * **Data-driven optimization** : An advanced approach that improves prompts by evaluating a model's responses to sample prompts against specific evaluation metrics.



For more prompt-optimization guidelines, see [Overview of prompting strategies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies).

#### Improve performance for ML and generative AI endpoints

To improve the latency or throughput (tokens per second) for ML and generative AI endpoints, consider the following recommendations:

  * Cache results by using [Memorystore](https://docs.cloud.google.com/memorystore/docs).
  * For generative AI APIs, use the following techniques: 
    * [Context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview): Achieve lower latency for requests that contain repeated content.
    * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput): Improve the throughput for Gemini endpoints by reserving throughput capacity.
  * For self-hosted models, consider the following optimized inference frameworks: Framework | Notebooks and guides  
---|---  
Optimized [vLLM](https://github.com/vllm-project/vllm/blob/main/README.md) containers in Model Garden | [Deploy open models with prebuilt containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-prebuilt-containers)  
GPU-based inference on GKE | 
    * [Serve an LLM with Ray](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/serve-llm-l4-ray)
    * [Serve Gemma open models with Hugging Face TGI](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-tgi)
    * [Serve Gemma open models with vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm)
    * [Serve Gemma open models with TensorRT-LLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-tensortllm)
    * [Serve scalable LLMs with TorchServe](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scalable-ml-models-torchserve)  
TPU-based inference | 
    * [Serve open models using TPUs on GKE with Optimum TPU](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/optimum-tpu)
    * [Serve open models using vLLM TPU on Cloud TPU](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/vllm/use-vllm-tpu)  



#### Use low-code solutions and tuning

If pre-trained models don't meet your requirements, you can improve their performance for specific domains by using the solutions:

  * [AutoML](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/beginner/beginners-guide) is a low-code solution to improve inference results with minimal technical effort for a wide range of tasks. AutoML lets you create models that are optimized on several dimensions: architecture, performance, and training stage (through checkpointing).
  * [Tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning) helps you achieve higher quality, more stable generation and lower latency with shorter prompts and without a lot of data. We recommend that you start tuning by using the [default values for hyperparameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning/use#tuning_hyperparameters). For more information, see [About supervised fine-tuning for Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning).



#### Optimize self-managed training

In some cases, you might decide to retrain a model or fully manage a fine-tuning job. This approach requires advanced skills and additional time depending on the model, framework, and resources that you use.

Take advantage of performance-optimized framework options, such as the following:

  * Use deep learning [images](https://docs.cloud.google.com/deep-learning-vm/docs/introduction) or [containers](https://docs.cloud.google.com/deep-learning-containers/docs/getting-started-local), which include the latest software dependencies and Google Cloud-specific libraries.

  * Run model training with Ray on Google Cloud:

    * [Ray on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/open-source/ray) lets you bring Ray's distributed training framework to Compute Engine or GKE and it simplifies the overhead of managing the framework.
    * You can self-manage Ray on GKE with KubeRay by deploying the [Ray operator](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/enable-ray-on-gke) on an existing cluster.
  * Deploy training workloads on a compute cluster that you provision by using the open-source [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview). To efficiently provision performance-optimized clusters, use YAML-based [blueprints](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog). Manage the clusters by using schedulers like [Slurm](https://slurm.schedmd.com/overview.html) and GKE.

  * Train standard model architectures by using [GPU-optimized recipes](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/README.md).




Build training architectures and strategies that optimize performance by using the following techniques:

  * Implement [distributed training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/distributed-training) on Agent Platform or on the frameworks described earlier. Distributed training enables model parallelism and data parallelism, which can help to increase the training dataset size and model size, and help to reduce training time.
  * For efficient model training and to explore different performance configurations, run checkpointing at appropriate intervals. For more information, see Optimize runtime goodput.



#### Optimize self-managed serving

For self-managed serving, you need efficient inference operations and a high throughput (number of inferences per unit of time).

To optimize your model for inference, consider the following approaches:

  * [Quantization](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization#quantization): Reduce the model size by representing its parameters in a lower precision format. This approach helps to reduce memory consumption and latency. However, quantization _after_ training might change model quality. For example, quantization after training might cause a reduction in accuracy.

    * Post-training quantization (PTQ) is a repeatable task. Major ML frameworks like [PyTorch](https://pytorch.org/docs/stable/quantization.html) and [TensorFlow](https://ai.google.dev/edge/litert/models/quantization_spec) support PTQ.
    * You can orchestrate PTQ by using a pipeline on [Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction).
    * To stabilize model performance and benefit from reductions in model size, you can use [Qwix](https://github.com/google/qwix/blob/main/README.md).
  * [Tensor parallelism](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization#tensor-parallelism): Improve inference throughput by distributing computational load across multiple GPUs.

  * [Memory optimization](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization#model-memory): Increase throughput and optimize attention caching, batch sizes, and input sizes.




Use inference-optimized frameworks, such as the following:

  * For generative models, use an open framework like [MaxText](https://github.com/AI-Hypercomputer/maxtext/blob/main/README.md), [MaxDiffusion](https://github.com/AI-Hypercomputer/maxdiffusion/blob/main/README.md#overview), or [vLLM](https://github.com/vllm-project/vllm/blob/main/README.md).
  * Run [prebuilt container images](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/pre-built-containers) on Agent Platform for predictions and explanations. If you choose TensorFlow, then use the [optimized TensorFlow runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/optimized-tensorflow-runtime). This runtime enables more efficient and lower cost inference than prebuilt containers that use open-source TensorFlow.
  * Run [multi-host inferencing using Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference).
  * Leverage the [NVIDIA Triton inference server](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/using-nvidia-triton) for Agent Platform.
  * Simplify the deployment of inference workloads on GKE by using LLM-optimized configurations. For more information, see [Analyze model serving performance and costs with GKE Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart).



### Optimize resource consumption based on performance goals

Resource optimization helps to accelerate training, iterate efficiently, improve model quality, and increase the serving capacity.

#### Choose appropriate processor types

Your choice of compute platform can have a significant impact on the training efficiency of a model.

  * Deep learning models perform well on GPUs and TPUs because such models require large amounts of memory and parallel matrix computation. For more information about workloads that are well suited to CPUs, GPUs, and TPUs, see [When to use TPUs](https://docs.cloud.google.com/tpu/docs/intro-to-tpu#when_to_use_tpus).
  * [Compute-optimized VMs](https://docs.cloud.google.com/compute/docs/compute-optimized-machines) are ideal for HPC workloads.



#### Optimize training and serving on GPUs

To optimize the performance of training and inference workloads that are deployed on GPUs, consider the following recommendations:

Recommendation | Description  
---|---  
**Select appropriate memory specifications.** | When you choose [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus), select memory specifications based on the following factors:

  * **Model capacity** : The total memory size (memory footprint) of the model's trainable parameters and gradients.
  * **Workload type** : Training requires more memory than serving.
  * **Training batch size** : For larger batches, more activations are stored and the memory requirement is higher.
  * **Data type** : Workloads that process high-quality images or that use high-precision arithmetics need machine types with larger memory specifications.

  
**Assess core and memory bandwidth requirements.** | In addition to memory size, consider other requirements like the number of Tensor cores and memory bandwidth. These factors influence the speed of data access and computations on the chip.  
**Choose appropriate GPU machine types.** | Training and serving might need different GPU machine types.

  * Training jobs need one or more GPUs, or even multiple nodes, with significantly large memory and bandwidth.
  * Inference workloads require relatively less memory and fewer high-performance GPUs.

We recommend that you use large machine types for training and smaller, cost-effective machine types for inference. To detect resource utilization issues, use monitoring tools like the NVIDIA DCGM agent and adjust resources appropriately.  
**Leverage GPU sharing on GKE.** | Dedicating a full GPU to a single container might be an inefficient approach in some cases. To help you overcome this inefficiency, GKE supports the following [GPU-sharing strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus):

  * [Multi-instance GPU](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi): Allocate a single GPU to multiple containers on a node.
  * [GPU time-sharing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/timesharing-gpus): Allocate GPU time across multiple containers. Each container gets a time slice.
  * [NVIDIA multi-process service (MPS)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nvidia-mps-gpus): Run multi-process workloads concurrently on a single GPU by using a binary-compatible [CUDA](https://developer.nvidia.com/cuda) implementation.

To maximize resource utilization, we recommend that you use an appropriate combination of these strategies. For example, when you virtualize a large H100 GPU by using the GPU time-sharing _and_ multi-instance GPU strategies, the serving platform can scale up and down based on traffic. GPU resources are repurposed in real time based on the load on the model containers.  
**Optimize routing and load balancing.** | When you deploy multiple models on a cluster, you can use [GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway) for optimized routing and load balancing. Inference Gateway extends the routing mechanisms of the [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io) by using the following capabilities:

  * [Request body routing logic](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway#create-httproute) and endpoint selection. These features enable optimization strategies like using the same base model for [multiple LoRA adapters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway#specify-model-objectives).
  * Generative AI-specific [security extensions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-gke-inference-gateway-configurations#ai-safety-checks) like Model Armor.

  
**Share resources for Agent Platform endpoints.** | You can configure multiple Agent Platform endpoints to use a common pool of resources. For more information about this feature and its limitations, see [Share resources across deployments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/model-co-hosting).   
  
#### Optimize training and serving on TPUs

TPUs are Google chips that help solve massive scale challenges for ML algorithms. These chips provide optimal performance for AI training and inference workloads. When compared to GPUs, TPUs provide higher efficiency for deep learning training and serving. For information about the use cases that are suitable for TPUs, see [When to use TPUs](https://docs.cloud.google.com/tpu/docs/intro-to-tpu#when_to_use_tpus). TPUs are compatible with ML frameworks like [TensorFlow](https://docs.cloud.google.com/tpu/docs/tensorflow-pods), [PyTorch](https://docs.cloud.google.com/tpu/docs/run-calculation-pytorch), and [JAX](https://docs.cloud.google.com/tpu/docs/run-calculation-jax).

To optimize TPU performance, use the following techniques, which are described in the [Cloud TPU performance guide](https://docs.cloud.google.com/tpu/docs/performance-guide):

  * Maximize the batch size for each TPU memory unit.
  * Ensure that TPUs aren't idle. For example, implement parallel data reads.
  * Optimize the XLA compiler. Adjust tensor dimensions as required and avoid padding. XLA automatically optimizes for graph execution performance by using tools like fusion and broadcasting.



#### Optimize training on TPUs and serving on GPUs

TPUs support efficient training. GPUs provide versatility and wider availability for inference workloads. To combine the strengths of TPUs and GPUs, you can train models on TPUs and serve them on GPUs. This approach can help to reduce overall costs and accelerate development, particularly for large models. For information about the locations where TPU and GPU machine types are available, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones) and [GPU locations](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

#### Optimize the storage layer

The storage layer of your training and serving infrastructure is critical to performance. Training jobs and inferencing workloads involve the following storage-related activities:

  * Loading and processing data.
  * Checkpointing the model during training.
  * Reloading binaries to resume training after node preemptions.
  * Loading the model efficiently to handle inferencing at scale.



The following factors determine your requirements for storage capacity, bandwidth, and latency:

  * Model size
  * Volume of the training dataset
  * Checkpointing frequency
  * Scaling patterns



If your training data is in Cloud Storage, you can reduce the data loading latency by using [file caching in Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching). Cloud Storage FUSE lets you mount a Cloud Storage bucket on compute nodes that have Local SSD disks. For information about improving the performance of Cloud Storage FUSE, see [Performance tuning best practices](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).

A [PyTorch connector](https://docs.cloud.google.com/storage/docs/pytorch-connector) to Cloud Storage provides high performance for data reads and writes. This connector is particularly beneficial for training with large datasets and for checkpointing large models.

Compute Engine supports various [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types) types. With [Google Cloud Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hyperdisks), you can provision the required throughput and IOPS based on training needs. To optimize disk performance, start by resizing the disks and then consider changing the machine type. For more information, see [Optimize Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance). To load test the read-write performance and latency at the storage layer, you can use tools like [Flexible I/O tester (FIO)](https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-linux).

For more information about choosing and optimizing storage services for your AI and ML workloads, see [Overview of storage services for AI and ML workloads in AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/storage).

#### Optimize the network layer

To optimize the performance of AI and ML workloads, configure your VPC networks to provide adequate bandwidth and maximum throughput with minimum latency. Consider the following recommendations:

Recommendation | Suggested techniques for implementation  
---|---  
Optimize VPC networks. | 

  * Configure a large [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) size.
  * Use [Premium Tier networking](https://docs.cloud.google.com/network-tiers/docs/overview#premium_tier).
  * For improved connectivity on VMs with NVIDIA ConnectX machine types (A3 Ultra and later), configure the VPC network with the [Remote Direct Memory Access (RDMA) network profile](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles). 

  
Place VMs closer to each other. | 

  * Define [compact placement policies in Compute Engine](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies). 
  * Use [Topology Aware Scheduling in GKE](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas). 

  
Configure VMs to support higher network speeds. | 

  * Use [Google Virtual NICs (gVNICs)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).
  * Configure [per VM Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration). For information about testing Tier_1 networking performance, see [Benchmark higher network bandwidth for VM instances](https://docs.cloud.google.com/compute/docs/networking/benchmarking-higher-bandwidth-vms). 
  * For multi-GPU training, optimize GPU-to-GPU network performance by using NVIDIA-specific [connectivity configurations](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth).
  * Install [NVIDIA GPUDirect](https://developer.nvidia.com/gpudirect) and configure the [NVIDIA collective communication library (NCCL)](https://developer.nvidia.com/nccl). For more information, see [Install the GPUDirect binary and configure NCCL](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx#install-gpudirect-tcpx-nccl). To test the performance of NCCL operations, you can use standard [NCCL tests](https://github.com/NVIDIA/nccl-tests). 

  
  
## Link performance metrics to design and configuration choices

To innovate, troubleshoot, and investigate performance issues, you must establish a clear link between design choices and performance outcomes. You need a reliable record of the lineage of ML assets, deployments, model outputs, and the corresponding configurations and inputs that produced the outputs.

### Build a data and model lineage system

To reliably improve performance, you need the ability to trace every model version back to the exact data, code, and configurations that were used to produce the model. As you scale a model, such tracing becomes difficult. You need a lineage system that automates the tracing process and creates a record that's clear and can be queried for every experiment. This system lets your teams efficiently identify and reproduce the choices that lead to the optimally performing models.

To view and analyze the lineage of pipeline artifacts for workloads in Agent Platform, you can use [Agent Platform ML Metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/introduction) or [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction). Both options let you register events or artifacts to meet governance requirements and to query the metadata and retrieve information when needed. This section provides an overview of the two options. For detailed information about the differences between Agent Platform ML Metadata and Knowledge Catalog, see [Track the lineage of pipeline artifacts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/lineage).

#### Default implementation: Agent Platform ML Metadata

Your first pipeline run or _experiment_ in Agent Platform creates a default Agent Platform ML Metadata service. The parameters and artifact metadata that the pipeline consumes and generates are automatically registered to a Agent Platform ML Metadata store. The [data model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/data-model) that's used to organize and connect the stored metadata contains the following elements:

  * **Context** : A group of artifacts and executions that represents an experimentation run.
  * **Execution** : A step in a workflow, like data validation or model training.
  * **Artifact** : An input or output entity, object, or piece of data that a workflow produces and consumes.
  * **Event** : A relationship between an artifact and an execution.



By default, Agent Platform ML Metadata captures and [tracks](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/tracking) all input and output artifacts of a pipeline run. It integrates these artifacts with [Experiments on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/intro-vertex-ai-experiments), [Model Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction), and [Agent Platform managed datasets](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/overview).

[Autologging](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/run-training-job-experiments) is a built-in feature in Agent Platform Managed Training to automatically log data to Experiments on Agent Platform. To efficiently track experiments for optimizing performance, use the built-in integrations between Experiments on Agent Platform and the associated Agent Platform ML Metadata service.

Agent Platform ML Metadata provides a filtering syntax and operators to run queries about artifacts, executions, and contexts. When required, your teams can efficiently retrieve information about a model's registry link and its dataset or evaluation for a specific experiment run. This metadata can help to accelerate the discovery of choices that optimize performance. For example, you can [compare pipeline runs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/user-journey/uj-compare-pipeline-runs), [compare models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/user-journey/uj-compare-models), and [compare experiment runs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/compare-analyze-runs). For more information, including example queries, see [Analyze metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/analyzing#inputs-and-outputs).

#### Alternative implementation: Knowledge Catalog

Knowledge Catalog discovers metadata from [Google Cloud resources](https://docs.cloud.google.com/dataplex/docs/catalog-overview#supported-sources), including Agent Platform artifacts. You can also integrate a [custom data source](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources).

Knowledge Catalog can read metadata across multiple regions and organization-wide stores, whereas Agent Platform ML Metadata is a project-specific resource. When compared to Agent Platform ML Metadata, Knowledge Catalog involves more setup effort. However, Knowledge Catalog might be appropriate when you need integration with your wider data portfolio in Google Cloud and with organization-wide stores.

Knowledge Catalog discovers and harvests metadata for projects where the Data Lineage API is enabled. The metadata in the catalog is organized by using a [data model](https://docs.cloud.google.com/dataplex/docs/catalog-overview#supported-sources) that consists of projects, entry groups, entries, and aspects. Knowledge Catalog provides a [specific syntax](https://docs.cloud.google.com/dataplex/docs/search-syntax) that you can use to discover artifacts. If required, you can [map metadata artifacts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/lineage#map_artifacts_to_fqn) to Knowledge Catalog.

### Use explainability tools

The behavior of an AI model is based on data that was used to train the model. This behavior is encoded as [parameters](https://developers.google.com/machine-learning/glossary#parameter) in mathematical functions. Understanding exactly _why_ a model performs in a certain way can be difficult. However, this knowledge is critical for performance optimization.

For example, consider an image classification model where the training data contains images of only red cars. The model might learn to identify the "car" label based on the color of the object rather than the object's spatial and shape attributes. When the model is tested with images that show cars of different colors, the performance of the model might degrade. The following sections describe tools that you can use to identify and diagnose such problems.

#### Detect data biases

In the exploratory data analysis (EDA) phase of an ML project, you identify issues with the data, such as [class-imbalanced datasets](https://developers.google.com/machine-learning/glossary/fundamentals#class_imbalanced_data_set) and [biases](https://developers.google.com/machine-learning/glossary/fundamentals#bias-ethicsfairness).

In production systems, you often retrain models and run experiments with different datasets. To standardize data and compare across experiments, we recommend a systematic approach to EDA that includes the following characteristics:

  * **Automation** : As a training set grows in size, the EDA process must run automatically in the background.
  * **Wide coverage** : When you add new features, the EDA must reveal insights about the new features.



Many EDA tasks are specific to the data type and the business context. To automate the EDA process, use BigQuery or a managed data processing service like Dataflow. For more information, see [Classification on imbalanced data](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data) and [Data bias metrics for Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/data-bias-metrics).

#### Understand model characteristics and behavior

In addition to understanding the distribution of data in the training and validation sets and their biases, you need to understand a model's characteristics and behavior at prediction time. To understand model behavior, use the following tools:

Tool | Description | Purposes  
---|---|---  
**Example-based explanations** | You can use example-based explanations or nearest-neighbor search to understand a prediction by finding the most similar examples from the training data. This approach is based on the principle that similar inputs yield similar outputs. | 

  * Identify and fix gaps in the training data by finding similar examples for an incorrect prediction.
  * Classify inputs that the model was not originally trained to recognize, by using [neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) from a reference set.
  * Identify anomalies by finding inputs that are significantly different from all of the known training examples.
  * Make data collection more efficient by identifying ambiguous cases, like when neighbors have mixed labels. Prioritize such cases for human review.

  
**Feature-based explanations** | For predictions that are based on tabular data or images, feature-based explanations show how much each [feature](https://developers.google.com/machine-learning/glossary/fundamentals#feature) affects a prediction when it's compared to a baseline. Explainability techniques and [tabular explanations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-explanations) provide feature attribution methods depending on the model type and task. The methods typically rely on sampling and sensitivity analysis to measure how much the output changes in response to changes in an input feature. | 

  * Identify biases that a validation step might miss.
  * Optimize performance by identifying the features that are most important for a prediction. To increase a model's quality and performance, ML engineers can intentionally add, remove, or engineer features. 

  
**[What-If Tool](https://pair-code.github.io/what-if-tool)** | The What-If Tool was developed by Google's [People + AI Research (PAIR) initiative](https://pair.withgoogle.com/) to help you understand and visualize the behavior of image and tabular models. For examples of using the tool, see [What-If Tool Web Demos](https://pair-code.github.io/what-if-tool/explore/). | 

  * Debug and find the root cause of incorrect predictions.
  * Investigate how a model performs across different subsets of data by identifying biases through a fairness analysis.
  * Understand a model's behavior, particularly the relationship between a model's predictions and input features.
  * Compare predictions by using a visual comparison tool that requires either two models or a ground truth baseline. 

  
  
## Contributors

Authors: 

  * [Benjamin Sadik](https://www.linkedin.com/in/benjaminhaimsadik) | AI and ML Specialist Customer Engineer
  * [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist



Other contributors: 

  * [Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer



[ Previous arrow_back  Cost optimization  ](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]] 
