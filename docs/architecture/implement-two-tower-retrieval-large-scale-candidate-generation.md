---
url: https://docs.cloud.google.com/architecture/implement-two-tower-retrieval-large-scale-candidate-generation/
title: Implement two-tower retrieval for large-scale candidate generation \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:13.445860+00:00
---

# Implement two-tower retrieval for large-scale candidate generation  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/implement-two-tower-retrieval-large-scale-candidate-generation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Implement two-tower retrieval for large-scale candidate generation Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-16 UTC

This document provides a reference architecture that shows you how to implement an end-to-end two-tower [candidate generation](https://developers.google.com/machine-learning/recommendation/overview/types) workflow with [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview). The two-tower modeling framework is a powerful retrieval technique for personalization use cases because it learns the semantic similarity between two different entities, such as web queries and candidate items.

This document is for technical practitioners like data scientists and machine learning engineers who are developing large-scale recommendation applications with low-latency serving requirements. For more information about the modeling techniques, problem framing, and data preparation for building a two-tower model, see [Scaling deep retrieval with TensorFlow Recommenders and Vector Search](https://cloud.google.com/blog/products/ai-machine-learning/scaling-deep-retrieval-tensorflow-two-towers-architecture).

## Architecture

The following diagram shows an architecture to train a two-tower model and deploy each tower separately for different deployment and serving tasks:

![An architecture to train a two-tower model and deploy each tower separately.](https://docs.cloud.google.com/static/architecture/images/implement-two-tower-retrieval-large-scale-candidate-generation-architecture.svg)![](https://docs.cloud.google.com/static/architecture/images/implement-two-tower-retrieval-large-scale-candidate-generation-architecture.svg)

The architecture in the diagram includes the following components:

  * **Training data** : Training files are stored in Cloud Storage.
  * **Two-tower training** : The combined two-tower model is trained offline using the Gemini Enterprise Agent Platform Managed Training service; each tower is saved separately and used for different tasks.
  * **Registered query and candidate towers** : After the towers are trained, each tower is separately uploaded to Model Registry on Gemini Enterprise Agent Platform.
  * **Deployed query tower** : The registered query tower is deployed to a Agent Platform online endpoint.
  * **Batch predict embeddings** : The registered candidate tower is used in a batch prediction job to precompute the embedding representations of all available candidate items.
  * **Embeddings JSON** : The predicted embeddings are saved to a JSON file in Cloud Storage.
  * **ANN index** : Agent Platform Vector Search is used to create a serving index that's configured for approximate nearest neighbor (ANN) search.
  * **Deployed index** : The ANN index is deployed to a Agent Platform Vector Search index endpoint.



## Products used

This reference architecture uses the following Google Cloud products:

  * [ Gemini Enterprise Agent Platform Managed Training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview): A managed training service that lets you operationalize large-scale model training. 
  * [ Vector Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/overview): A vector similarity-matching service that lets you store, index, and search semantically similar or related data. 
  * [ Model Registry on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction): A central repository where you can manage the lifecycle of your ML models. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.



## Use case

To meet low-latency serving requirements, large-scale recommenders are often deployed to production as two-stage systems or sometimes as [multi-stage systems](https://medium.com/nvidia-merlin/recommender-systems-not-just-recommender-models-485c161c755e). The goal of the first stage, candidate generation, is to sift through a large collection of candidate items and retrieve a relevant subset of hundreds of items for downstream filtering and ranking tasks. To optimize this retrieval task, consider these two core objectives:

  1. During model training, learn the best representation of the problem or task to be solved, and compile this representation into `<query, candidate>` embeddings.
  2. During model serving, retrieve relevant items fast enough to meet latency requirements.



The following diagram shows the conceptual components of a two-stage recommender:

![The conceptual components of a two-stage recommender.](https://docs.cloud.google.com/static/architecture/images/implement-two-tower-retrieval-large-scale-candidate-generation-conceptual-components.svg)

In the diagram, candidate generation filters millions of candidate items. Ranking then filters the resulting hundreds of candidate items to return dozens of recommended items.

The reference architecture in this document trains a two-tower-based retrieval model. In the architecture, each tower is a neural network that processes either query or candidate item features, and then produces an embedding representation of those features. Each tower is deployed separately, because each tower will be used for different tasks in production:

  * **Candidate tower** : The candidate tower is used to precompute embeddings for all candidate items. The precomputed embeddings are deployed to a [Vector Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/overview) index endpoint that's optimized for low-latency retrieval.
  * **Deployed tower** : During online serving, the deployed query tower converts raw user queries to embedding representations. The embedding representations are then used to look up similar item embeddings in the deployed index.



Two-tower architectures are ideal for many retrieval tasks because a two-tower architecture captures the semantic relationship of query and candidate entities, and maps them to a shared [embedding space](https://developers.google.com/machine-learning/recommendation/overview/candidate-generation#embedding_space). When the entities are mapped to a shared embedding space, semantically similar entities are clustered closer together. Therefore, if you compute the [vector embeddings](https://cloud.google.com/blog/topics/developers-practitioners/meet-ais-multitool-vector-embeddings) of a given query, you can search the embedding space for the closest (most similar) candidate items. The primary benefit of such an architecture is the ability to decouple the inference of query and candidate representations. The advantages of this decoupling are mainly two-fold:

  * **You can serve new (fresh) items without retraining a new item vocabulary**. By feeding any set of item features to the candidate item tower, you can compute the item embeddings for any set of candidates, even those that aren't seen during training. Performing this computation helps to address the cold-start problem. 
    * The candidate tower can support an arbitrary set of candidate items, including items that haven't yet interacted with the recommendation system. This support is possible because two-tower architectures process rich content and metadata features about each `<query, candidate>` pair. This kind of processing lets the system describe an unknown item in terms of items that it knows.
  * **You can optimize the retrieval inference by precomputing all candidate item embeddings**. These precomputed embeddings can be indexed and deployed to a serving infrastructure that's optimized for low-latency retrieval. 
    * The co-learning of the towers lets you describe items in terms of queries and the other way around. If you have one half of a pair, like a query, and you need to look for the other corresponding item, you can precompute half of the equation ahead of time. The precomputation lets you make the rest of decision as quickly as possible.



## Design considerations

This section provides guidance to help you develop a candidate-generation architecture in Google Cloud that meets your security and performance needs. The guidance in this section isn't exhaustive. Depending on your specific requirements, you might choose to consider additional design factors and trade-offs.

### Security

Agent Platform Vector Search supports both public and Virtual Private Cloud (VPC) endpoint deployments. If you want to use a VPC network, get started by following [Set up a VPC Network Peering connection](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/vpc). If the Vector Search index is deployed within a VPC perimeter, users must access the associated resources from within the same VPC network. For example, if you're developing from Gemini Enterprise Agent Platform Workbench, you need to create the workbench instance within the same VPC network as the deployed index endpoint. Similarly, any pipeline that's expected to create an endpoint, or deploy an index to an endpoint, should run within the same VPC network.

### Performance optimization

This section describes the factors to consider when you use this reference architecture to design a topology in Google Cloud that meets the performance requirements of your workloads.

#### Profile training jobs

To optimize data input pipelines and the overall training graph, we recommend that you profile training performance with [Cloud Profiler](https://github.com/googleapis/python-aiplatform/tree/main/google/cloud/aiplatform/training_utils/cloud_profiler). Profiler is a managed implementation of the open source [TensorBoard Profiler](https://www.tensorflow.org/tensorboard/tensorboard_profiling_keras).

By passing the `–profiler` argument in the training job, you enable the TensorFlow callback to profile a set number of batches for each epoch. The profile captures traces from the host CPU and from the device GPU or TPU hardware. The traces provide information about the resource consumption of the training job. To avoid out-of-memory errors, we recommend that you start with a profile duration between 2 and 10 train steps, and increase as needed.

To learn how to use Profiler with Agent Platform Managed Training and Vertex AI TensorBoard, see [Profile model training performance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/tensorboard-profiler). For debugging best practices, see [Optimize GPU performance](https://www.tensorflow.org/guide/gpu_performance_analysis#1_debug_the_input_pipeline). For information about how to optimize performance, see [Optimize TensorFlow performance using the Profiler](https://www.tensorflow.org/guide/profiler).

#### Fully utilize accelerators

When you attach training accelerators such as NVIDIA GPUs or Cloud TPUs, it's important to keep them fully utilized. Full utilization of training accelerators is a best practice for cost management because accelerators are the most expensive component in the architecture. Full utilization of training accelerators is also a best practice for job efficiency because having no idle time results in less overall resource consumption.

To keep an accelerator fully utilized, you typically perform a few iterations of finding the bottleneck, optimizing the bottleneck, and then repeating these steps until the accelerator device utilization is acceptable. Because many of the datasets for this use case are too large to fit into memory, bottlenecks are typically found between storage, host VMs, and the accelerator.

The following diagram shows the conceptual stages of an ML training input pipeline:

![The conceptual stages of an ML training input pipeline.](https://docs.cloud.google.com/static/architecture/images/implement-two-tower-retrieval-large-scale-candidate-generation-conceptual-ml-training-input.svg)

In the diagram, data is read from storage and preprocessed. After the data is preprocessed, it's sent to the device. To optimize performance, start by determining if overall performance is bounded by the host CPU or by the accelerator device (GPU or TPU). The device is responsible for accelerating the training loop, while the host is responsible for feeding training data to the device and receiving results from the device. The following sections describe how to resolve bottlenecks by improving input pipeline performance and device performance.

##### Improve input pipeline performance

  * **Reading data from storage** : To improve data reads, try caching, [prefetching](https://www.tensorflow.org/guide/data_performance#prefetching), [sequential access patterns](https://en.wikipedia.org/wiki/Sequential_access), and parallel I/O.
  * **Preprocessing data** : To improve data preprocessing, configure [parallel processing](https://www.tensorflow.org/guide/data_performance#parallelizing_data_extraction) for data extraction and transformation, and tune the [`interleave` transformation](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave) in the data input pipeline.
  * **Sending data to device** : To reduce overall job time, transfer data from the host to multiple devices in parallel.



##### Improve device performance

  * **Increasing mini-batch size**. Mini-batches are the number of training samples that are used by each device in one iteration of a training loop. By increasing mini-batch size, you increase parallelism between operations and improve data reuse. However, the mini-batch must be able to fit into memory with the rest of the training program. If you increase mini-batch size too much, you can experience out-of-memory errors and model divergence.
  * [**Vectorize user-defined functions**](https://www.tensorflow.org/guide/data_performance#vectorizing_mapping). Typically, data transformations can be expressed as a user-defined function that describes how to transform each element of an input dataset. To vectorize this function, you apply the transform operation over a batch of inputs at once instead of transforming one element at a time. Any user-defined function has overhead that's related to scheduling and execution. When you transform a batch of inputs, you incur the overhead once per batch, instead of once per dataset element.



##### Scale up before scaling out

When you configure the compute resources for your training jobs, we recommend that you scale up before scaling out. This means that you should choose a larger, more powerful device before you use multiple less powerful devices. We recommend that you scale in the following way:

  1. Single worker + single device
  2. Single worker + more powerful device
  3. Single worker + multiple devices
  4. Distributed training



#### Evaluate recall against latency for ANN vector search

To evaluate the benefits of ANN search, you can measure the latency and recall of a given query. To help with index tuning, Agent Platform Vector Search provides the ability to create a brute-force index. Brute-force indexes will perform an exhaustive search, at the expense of higher latency, to find the true nearest neighbors for a given query vector. Use of brute-force indexes isn't intended for production use, but it provides a good baseline when you compute recall during index tuning.

To evaluate recall against latency, you deploy the precomputed candidate embeddings to one index that's configured for ANN search and to another index that's configured for brute-force search. The brute-force index will return the absolute nearest neighbors, but it will typically take longer than an ANN search. You might be willing to sacrifice some retrieval recall for gains in retrieval latency, but this tradeoff should be evaluated. Additional characteristics that impact recall and latency include the following:

  * **Modeling parameters** : Many modeling decisions impact the embedding space, which ultimately becomes the serving index. Compare the candidates that are retrieved for indexes that are built from both shallow and deep retrieval models.
  * **Dimensions** : Dimensions are another aspect that are ultimately determined by the model. The dimensions of the ANN index must match the dimensions of the query and candidate tower vectors.
  * **Crowding and filtering tags** : Tags can provide powerful capabilities to tailor results for different production use cases. It's a best practice to understand how tags influence the retrieved candidates and impact performance.
  * **ANN count** : Increasing this value increases recall and can proportionately increase latency.
  * **Percentage of leaf nodes to search** : The percentage of leaf nodes to search is the most critical option for evaluating recall against latency tradeoff. Increasing this value increases recall and can proportionately increase latency.



## What's next

For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 

## Contributors

Authors: 

  * [Jordan Totten](https://www.linkedin.com/in/jordantotten) | Customer Engineer
  * [Jeremy Wortz](https://www.linkedin.com/in/wortz) | Customer Engineer
  * [Lakshmanan Sethu](https://www.linkedin.com/in/lakshmanansethu) | Technical Account Manager



Other contributor: [Kaz Sato](https://www.linkedin.com/in/kazunori279) | Staff Developer Advocate

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-16 UTC."],[],[]] 
