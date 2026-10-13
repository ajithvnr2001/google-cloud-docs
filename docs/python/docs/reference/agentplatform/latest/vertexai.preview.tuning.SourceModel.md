---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.tuning.SourceModel
title: Class SourceModel (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:31.910117+00:00
---

# Class SourceModel (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.tuning.SourceModel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SourceModel (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    SourceModel(base_model: str, custom_base_model: str = "")

A model that is used in managed OSS supervised tuning.

Usage:
    
    
    model = SourceModel(
        base_model="meta/llama3.1-8b", # OSS model name <publisher>/<model_name>
        custom_base_model="gs://user-bucket/custom-weights",
    )
    sft_tuning_job = sft.train(
        source_model=model,
        train_dataset="gs://my-bucket/train.jsonl",
        validation_dataset="gs://my-bucket/validation.jsonl",
        epochs=4,
        tuned_model_display_name="my-tuned-model",
        output_uri="gs://user-bucket/tuned-model"
    )
    
    while not sft_tuning_job.has_ended:
        time.sleep(60)
        sft_tuning_job.refresh()
    
    tuned_model = aiplatform.Model(sft_tuning_job.tuned_model_name)
    ```
    

## Methods 

### SourceModel
    
    
    SourceModel(base_model: str, custom_base_model: str = "")

Initializes SourceModel.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
