---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImageClassificationModelMetadata
title: Class ImageClassificationModelMetadata (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:53.209032+00:00
---

# Class ImageClassificationModelMetadata (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImageClassificationModelMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ImageClassificationModelMetadata (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    ImageClassificationModelMetadata(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Model metadata for image classification.

## Attributes  
  
---  
**Name** | **Description**  
`base_model_id` |  `str`   
Optional. The ID of the `base` model. If it is specified, the new model will be created based on the `base` model. Otherwise, the new model will be created from scratch. The `base` model must be in the same `project` and `location` as the new model to create, and have the same `model_type`.   
`train_budget` |  `int`   
Required. The train budget of creating this model, expressed in hours. The actual `train_cost` will be equal or less than this value.   
`train_cost` |  `int`   
Output only. The actual train cost of creating this model, expressed in hours. If this model is created from a `base` model, the train cost used to create the `base` model are not included.   
`stop_reason` |  `str`   
Output only. The reason that this create model operation stopped, e.g. `BUDGET_REACHED`, `MODEL_CONVERGED`.   
`model_type` |  `str`   
Optional. Type of the model. The available values are: \- `cloud` \- Model to be used via prediction calls to AutoML API. This is the default value. \- `mobile-low-latency-1` \- A model that, in addition to providing prediction via AutoML API, can also be exported (see AutoMl.ExportModel) and used on a mobile or edge device with TensorFlow afterwards. Expected to have low latency, but may have lower prediction quality than other models. \- `mobile-versatile-1` \- A model that, in addition to providing prediction via AutoML API, can also be exported (see AutoMl.ExportModel) and used on a mobile or edge device with TensorFlow afterwards. \- `mobile-high-accuracy-1` \- A model that, in addition to providing prediction via AutoML API, can also be exported (see AutoMl.ExportModel) and used on a mobile or edge device with TensorFlow afterwards. Expected to have a higher latency, but should also have a higher prediction quality than other models. \- `mobile-core-ml-low-latency-1` \- A model that, in addition to providing prediction via AutoML API, can also be exported (see AutoMl.ExportModel) and used on a mobile device with Core ML afterwards. Expected to have low latency, but may have lower prediction quality than other models. \- `mobile-core-ml-versatile-1` \- A model that, in addition to providing prediction via AutoML API, can also be exported (see AutoMl.ExportModel) and used on a mobile device with Core ML afterwards. \- `mobile-core-ml-high-accuracy-1` \- A model that, in addition to providing prediction via AutoML API, can also be exported (see AutoMl.ExportModel) and used on a mobile device with Core ML afterwards. Expected to have a higher latency, but should also have a higher prediction quality than other models.   
`node_qps` |  `float`   
Output only. An approximate number of online prediction QPS that can be supported by this model per each node on which it is deployed.   
`node_count` |  `int`   
Output only. The number of nodes this model is deployed on. A node is an abstraction of a machine resource, which can handle online prediction QPS as given in the node_qps field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
