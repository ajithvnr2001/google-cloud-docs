---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.TuningEvaluationSpec
title: Class TuningEvaluationSpec (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:28.733490+00:00
---

# Class TuningEvaluationSpec (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.TuningEvaluationSpec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TuningEvaluationSpec (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    TuningEvaluationSpec(
        evaluation_data: typing.Optional[str] = None,
        evaluation_interval: typing.Optional[int] = None,
        enable_early_stopping: typing.Optional[bool] = None,
        enable_checkpoint_selection: typing.Optional[bool] = None,
        tensorboard: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.tensorboard.tensorboard_resource.Tensorboard, str
            ]
        ] = None,
    )

Specification for model evaluation to perform during tuning.

## Attributes  
  
---  
**Name** | **Description**  
`evaluation_data` |  `Optional[str]`   
GCS URI of the evaluation dataset. This will run model evaluation as part of the tuning job.   
`evaluation_interval` |  `Optional[int]`   
The evaluation will run at every evaluation_interval tuning steps. Default: 20.   
`enable_early_stopping` |  `Optional[bool]`   
If True, the tuning may stop early before completing all the tuning steps. Requires evaluation_data.   
`enable_checkpoint_selection` |  `Optional[bool]`   
If set to True, the tuning process returns the best model checkpoint (based on model evaluation). If set to False, the latest model checkpoint is returned. If unset, the selection is only enabled for `*-bison@001` models.   
`tensorboard` |  `Optional[Union[google.cloud.aiplatform.tensorboard.tensorboard_resource.Tensorboard, str]]`   
Vertex Tensorboard where to write the evaluation metrics. The Tensorboard must be in the same location as the tuning job.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
