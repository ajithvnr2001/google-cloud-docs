---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/neural-architecture-search/pytorch-efficient-training/
title: Efficient PyTorch training with cloud data \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:45:26.971215+00:00
---

# Efficient PyTorch training with cloud data  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/neural-architecture-search/pytorch-efficient-training/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Efficient PyTorch training with cloud data Stay organized with collections  Save and categorize content based on your preferences. 

Agent Platform Neural Architecture Search has no requirements describing how to design your trainers. Therefore, choose any training frameworks to build the trainer.

For PyTorch training with large amounts of data, the best practice is to use the distributed training paradigm and to read data from Cloud Storage. Check out the blog post [Efficient PyTorch training with Agent Platform Neural Architecture Search](https://cloud.google.com/blog/products/ai-machine-learning/efficient-pytorch-training-with-vertex-ai) for methods to improve the training performance. You can see an overall 6x performance improvement with data on Cloud Storage using `WebDataset` and choosing `DistributedDataParallel` or `FullyShardedDataParallel` distributed training strategies. The training performance using data on Cloud Storage is similar to the training performance using data on a local disk.

The prebuilt [MNasNet classification example](https://github.com/google/vertex-ai-nas/blob/main/pytorch/classification/cloud_search_main.py) has incorporated these methods into its training pipeline.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
