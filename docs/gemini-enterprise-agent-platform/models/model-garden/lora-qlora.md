---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/lora-qlora/
title: LoRA and QLoRA recommendations for LLMs \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:11.587471+00:00
---

# LoRA and QLoRA recommendations for LLMs  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/lora-qlora/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  LoRA and QLoRA recommendations for LLMs Stay organized with collections  Save and categorize content based on your preferences. 

This page gives you configuration recommendations for tuning large language models (LLM) on Gemini Enterprise Agent Platform by using [Low-Rank Adaptation of Large Language Models (LoRA)](https://arxiv.org/abs/2106.09685) and its more memory-efficient version, [QLoRA](https://arxiv.org/abs/2305.14314).

## Tuning recommendations

The following table summarizes our recommendations for tuning LLMs by using LoRA or QLoRA: 

Specification | Recommended | Details  
---|---|---  
GPU memory efficiency | QLoRA | QLoRA has about 75% smaller peak GPU memory usage compared to LoRA.  
Speed | LoRA | LoRA is about 66% faster than QLoRA in terms of tuning speed.  
Cost efficiency | LoRA | While both methods are relatively inexpensive, LoRA is up to 40% less expensive than QLoRA.  
Higher max sequence length | QLoRA | Higher max sequence length increases GPU memory consumption. QLoRA uses less GPU memory so it can support higher max sequence lengths.  
Accuracy improvement | Same | Both methods offer similar accuracy improvements.  
Higher batch size | QLoRA | QLoRA supports much higher batch sizes. For example, the following are batch size recommendations for tuning openLLaMA-7B on the following GPUs:  


  * 1 x A100 40G: 
    * LoRA: Batch size of 2 is recommended.
    * QLoRA: Batch size of 24 is recommended.
  * 1 x L4: 
    * LoRA: Batch size of 1 fails with an out of memory error (OOM).
    * QLoRA: Batch size of 12 is recommended.
  * 1 x V100: 
    * LoRA: Batch size of 1 fails with an out of memory error (OOM).
    * QLoRA: Batch size of 8 is recommended.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
