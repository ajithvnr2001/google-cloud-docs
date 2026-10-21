---
url: https://docs.cloud.google.com/architecture/framework/sustainability/ai-ml-energy-efficiency/
title: Optimize AI and ML workloads for energy efficiency \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:22.056714+00:00
---

# Optimize AI and ML workloads for energy efficiency  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/sustainability/ai-ml-energy-efficiency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Optimize AI and ML workloads for energy efficiency Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-28 UTC

This principle in the sustainability pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability) provides recommendations for optimizing AI and ML workloads to reduce their energy usage and carbon footprint.

## Principle overview

To optimize AI and ML workloads for sustainability, you need to adopt a holistic approach to designing, deploying, and operating the workloads. Select appropriate models and specialized hardware like Tensor Processing Units (TPUs), run the workloads in low-carbon regions, optimize to reduce resource usage, and apply operational best practices.

Architectural and operational practices that optimize the cost and performance of AI and ML workloads inherently lead to reduced energy consumption and lower carbon footprint. The [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework describes principles and recommendations to design, build, and manage AI and ML workloads that meet your operational, security, reliability, cost, and performance goals. In addition, the [Cloud Architecture Center](https://docs.cloud.google.com/architecture/ai-ml) provides detailed reference architectures and design guides for AI and ML workloads in Google Cloud.

## Recommendations

To optimize AI and ML workloads for energy efficiency, consider the recommendations in the following sections.

### Architect for energy efficiency by using TPUs

AI and ML workloads can be compute-intensive. The energy consumption by AI and ML workloads is a key consideration for sustainability. [TPUs](https://docs.cloud.google.com/tpu) let you significantly improve the energy efficiency and sustainability of your AI and ML workloads.

TPUs are custom-designed accelerators that are purpose-built for AI and ML workloads. The specialized architecture of TPUs make them highly effective for large-scale matrix multiplication, which is the foundation of deep learning. TPUs can perform complex tasks at scale with greater efficiency than general-purpose processors like CPUs or GPUs.

TPUs provide the following direct benefits for sustainability:

  * **Lower energy consumption** : TPUs are engineered for optimal energy efficiency. They deliver higher computations per watt of energy consumed. Their specialized architecture significantly reduces the power demands of large-scale training and inference tasks, which leads to reduced operational costs _and_ lower energy consumption.
  * **Faster training and inference** : The exceptional performance of TPUs lets you train complex AI models in hours rather than days. This significant reduction in the total compute time contributes directly to a smaller environmental footprint.
  * **Reduced cooling needs** : TPUs incorporate advanced liquid cooling, which provides efficient thermal management and significantly reduces the energy that's used for cooling the data center.
  * **Optimization of the AI lifecycle** : By integrating hardware and software, TPUs provide an optimized solution across the entire AI lifecycle, from data processing to model serving.



### Follow the 4Ms best practices for resource selection

Google recommends a set of best practices to reduce energy usage and carbon emissions significantly for AI and ML workloads. We call these best practices [_4Ms_](https://cloud.google.com/transform/betting-on-efficient-ai-the-4-ms):

  * **Model** : Select efficient ML model architectures. For example, [sparse models](https://ai.googleblog.com/2021/03/constructing-transformers-for-longer.html) improve ML quality and reduce computation by 3-10 times when compared to dense models.
  * **Machine** : Choose processors and systems that are optimized for ML training. These processors improve performance and energy efficiency by 2-5 times when compared to general-purpose processors.
  * **Mechanization** : Deploy your compute-intensive workloads in the cloud. Your workloads use less energy and cause lower emissions by 1.4 to 2 times when compared to on-premises deployments. Cloud data centers use newer, custom-designed warehouses that are built for energy efficiency and have a high [power usage effectiveness (PUE)](https://en.wikipedia.org/wiki/Power_usage_effectiveness) ratio. On-premises data centers are often older and smaller, therefore investments in energy-efficient cooling and power distribution systems might not be economical.
  * **Map** : Select Google Cloud locations that use the cleanest energy. This approach helps to reduce the gross carbon footprint of your workloads by 5-10 times. For more information, see [Carbon-free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon).



For more information about the 4Ms best practices and efficiency metrics, see the following research papers:

  * [The carbon footprint of machine learning training will plateau, then shrink](https://www.techrxiv.org/doi/full/10.36227/techrxiv.19139645.v1)
  * [The data center as a computer: An introduction to the design of warehouse-scale machines, second edition](https://research.google/pubs/the-datacenter-as-a-computer-an-introduction-to-the-design-of-warehouse-scale-machines-second-edition/)



### Optimize AI models and algorithms for training and inference

The architecture of an AI model and the algorithms that are used for training and inference have a significant impact on energy consumption. Consider the following recommendations.

#### Select efficient AI models

Choose smaller, more efficient AI models that meet your performance requirements. Don't select the largest available model as a default choice. For example, a smaller, distilled model version like [DistilBERT](https://huggingface.co/papers/1910.01108) can deliver similar performance with significantly less computational overhead and faster inference than a larger model like BERT.

#### Use domain-specific, hyper-efficient solutions

Choose specialized ML solutions that provide better performance and require significantly less compute power than a large foundation model. These specialized solutions are often pre-trained and hyper-optimized. They can provide significant reductions in energy consumption and research effort for both training and inference workloads. The following are examples of domain-specific specialized solutions:

  * [Earth AI](https://ai.google/earth-ai/) is an energy-efficient solution that synthesizes large amounts of global geospatial data to provide timely, accurate, and actionable insights.
  * [WeatherNext](https://deepmind.google/science/weathernext/) produces faster, more efficient, and highly accurate global weather forecasts when compared to conventional physics-based methods.



#### Apply appropriate model compression techniques

The following are examples of techniques that you can use for model compression:

  * **Pruning** : Remove unnecessary parameters from a neural network. These are parameters that don't contribute significantly to a model's performance. This technique reduces the size of the model and the computational resources that are required for inference.
  * **Quantization** : Reduce the precision of model parameters. For example, reduce the precision from 32-bit floating-point to 8-bit integers. This technique can help to significantly decrease the memory footprint and power consumption without a noticeable reduction in accuracy.
  * **Knowledge distillation** : Train a smaller _student_ model to mimic the behavior of a larger, more complex _teacher_ model. The student model can achieve a high level of performance with fewer parameters and by using less energy.



#### Use specialized hardware

As mentioned in Follow the 4Ms best practices for resource selection, choose processors and systems that are optimized for ML training. These processors improve performance and energy efficiency by 2-5 times when compared to general-purpose processors.

#### Use parameter-efficient fine-tuning

Instead of adjusting all of a model's billions of parameters (full fine-tuning), use parameter-efficient fine-tuning (PEFT) methods like low-rank adaptation (LoRA). With this technique, you freeze the original model's weights and train only a small number of new, lightweight layers. This approach helps to reduce cost and energy consumption.

### Follow best practices for AI and ML operations

Operational practices significantly affect the sustainability of your AI and ML workloads. Consider the following recommendations.

#### Optimize model training processes

Use the following techniques to optimize your model training processes:

  * **Early stopping** : Monitor the training process and stop it when you don't observe further improvement in model performance against the validation set. This technique helps you prevent unnecessary computations and energy use.
  * **Efficient data loading** : Use efficient data pipelines to ensure that the GPUs and TPUs are always utilized and don't wait for data. This technique helps to maximize resource utilization and reduce wasted energy.
  * **Optimized hyperparameter tuning** : To find optimal hyperparameters more efficiently, use techniques like Bayesian optimization or reinforcement learning. Avoid exhaustive grid searches, which can be resource-intensive operations.



#### Improve inference efficiency

To improve the efficiency of AI inference tasks, use the following techniques:

  * **Batching** : Group multiple inference requests in batches and take advantage of parallel processing on GPUs and TPUs. This technique helps to reduce the energy cost per prediction.
  * **Advanced caching** : Implement a multi-layered caching strategy, which includes key-value (KV) caching for autoregressive generation and semantic-prompt caching for application responses. This technique helps to bypass redundant model computations and can yield significant reductions in energy usage and carbon emissions.



#### Measure and monitor

Monitor and measure the following parameters:

  * **Usage and cost** : Use appropriate tools to track the token usage, energy consumption, and carbon footprint of your AI workloads. This data helps you identify opportunities for optimization and report progress toward sustainability goals.
  * **Performance** : Continuously monitor model performance in production. Identify issues like data drift, which can indicate that the model needs to be fine-tuned again. If you need to re-train the model, you can use the original fine-tuned model as a starting point and save significant time, money, and energy on updates. 
    * To track performance metrics, use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).
    * To correlate model changes with improvements in performance metrics, use [event annotations](https://docs.cloud.google.com/monitoring/dashboards/show-events).



For more information about operationalizing continuous improvement, see [Continuously measure and improve sustainability](https://docs.cloud.google.com/architecture/framework/sustainability/continuously-measure-improve).

#### Implement carbon-aware scheduling

Architect your ML pipeline jobs to run in regions with the cleanest energy mix. Use the Carbon Footprint report to identify the least carbon-intensive regions. Schedule resource-intensive tasks as batch jobs during periods when the local electrical grid has a higher percentage of carbon-free energy (CFE).

#### Optimize data pipelines

ML operations and fine-tuning require a clean, high-quality dataset. Before you start ML jobs, use managed data processing services to prepare the data efficiently. For example, use [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) for streaming and batch processing and use [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview) for managed Spark and Hadoop pipelines. An optimized data pipeline helps to ensure that your fine-tuning workload doesn't wait for data, so you can maximize resource utilization and help reduce wasted energy.

#### Embrace MLOps

To automate and manage the entire ML lifecycle, implement [ML Operations (MLOps) practices](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning). These practices help to ensure that models are continuously monitored, validated, and redeployed efficiently, which helps to prevent unnecessary training or resource allocation.

#### Use managed services

Instead of managing your own infrastructure, use managed cloud services like [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform). The cloud platform handles the underlying resource management, which lets you focus on the fine-tuning process. Use services that include built-in tools for hyperparameter tuning, model monitoring, and resource management.

## What's next

  * [How much energy does Google's AI use? We did the math](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference/)
  * [Ironwood: The first Google TPU for the age of inference](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/)
  * [Google Sustainability 2025 Environmental Report](https://sustainability.google/google-2025-environmental-report/)
  * [More Efficient In-Context Learning with GLaM](https://research.google/blog/more-efficient-in-context-learning-with-glam/)
  * [Context caching overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)



[ Previous arrow_back  Use low-carbon regions  ](https://docs.cloud.google.com/architecture/framework/sustainability/low-carbon-regions)

[ Next Optimize resource usage  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/sustainability/optimize-resource-usage)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-28 UTC."],[],[]] 
