---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageObjectDetectionModelMetadata
title: Class ImageObjectDetectionModelMetadata (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:28.987409+00:00
---

# Class ImageObjectDetectionModelMetadata (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageObjectDetectionModelMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ImageObjectDetectionModelMetadata (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    ImageObjectDetectionModelMetadata(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Model metadata specific to image object detection.

## Attributes  
  
---  
**Name** | **Description**  
`model_type` |  `str`   
Optional. Type of the model. The available values are: \- `cloud-high-accuracy-1` \- (default) A model to be used via prediction calls to AutoML API. Expected to have a higher latency, but should also have a higher prediction quality than other models. \- `cloud-low-latency-1` \- A model to be used via prediction calls to AutoML API. Expected to have low latency, but may have lower prediction quality than other models. \- `mobile-low-latency-1` \- A model that, in addition to providing prediction via AutoML API, can also be exported (see AutoMl.ExportModel) and used on a mobile or edge device with TensorFlow afterwards. Expected to have low latency, but may have lower prediction quality than other models. \- `mobile-versatile-1` \- A model that, in addition to providing prediction via AutoML API, can also be exported (see AutoMl.ExportModel) and used on a mobile or edge device with TensorFlow afterwards. \- `mobile-high-accuracy-1` \- A model that, in addition to providing prediction via AutoML API, can also be exported (see AutoMl.ExportModel) and used on a mobile or edge device with TensorFlow afterwards. Expected to have a higher latency, but should also have a higher prediction quality than other models.   
`node_count` |  `int`   
Output only. The number of nodes this model is deployed on. A node is an abstraction of a machine resource, which can handle online prediction QPS as given in the qps_per_node field.   
`node_qps` |  `float`   
Output only. An approximate number of online prediction QPS that can be supported by this model per each node on which it is deployed.   
`stop_reason` |  `str`   
Output only. The reason that this create model operation stopped, e.g. `BUDGET_REACHED`, `MODEL_CONVERGED`.   
`train_budget_milli_node_hours` |  `int`   
Optional. The train budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The actual `train_cost` will be equal or less than this value. If further model training ceases to provide any improvements, it will stop without using full budget and the stop_reason will be `MODEL_CONVERGED`. Note, node_hour = actual_hour \\* number_of_nodes_invovled. For model type `cloud-high-accuracy-1`\ (default) and `cloud-low-latency-1`, the train budget must be between 20,000 and 900,000 milli node hours, inclusive. The default value is 216, 000 which represents one day in wall time. For model type `mobile-low-latency-1`, `mobile-versatile-1`, `mobile-high-accuracy-1`, `mobile-core-ml-low-latency-1`, `mobile-core-ml-versatile-1`, `mobile-core-ml-high-accuracy-1`, the train budget must be between 1,000 and 100,000 milli node hours, inclusive. The default value is 24, 000 which represents one day in wall time.   
`train_cost_milli_node_hours` |  `int`   
Output only. The actual train cost of creating this model, expressed in milli node hours, i.e. 1,000 value in this field means 1 node hour. Guaranteed to not exceed the train budget.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
