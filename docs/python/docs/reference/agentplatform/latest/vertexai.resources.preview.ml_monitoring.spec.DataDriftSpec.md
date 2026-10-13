---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources.preview.ml_monitoring.spec.DataDriftSpec
title: Class DataDriftSpec (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:40.391323+00:00
---

# Class DataDriftSpec (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources.preview.ml_monitoring.spec.DataDriftSpec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataDriftSpec (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    DataDriftSpec(
        features: typing.Optional[typing.List[str]] = None,
        categorical_metric_type: typing.Optional[str] = "l_infinity",
        numeric_metric_type: typing.Optional[str] = "jensen_shannon_divergence",
        default_categorical_alert_threshold: typing.Optional[float] = None,
        default_numeric_alert_threshold: typing.Optional[float] = None,
        feature_alert_thresholds: typing.Optional[typing.Dict[str, float]] = None,
    )

Data drift monitoring spec.

Data drift measures the distribution distance between the current dataset and a baseline dataset. A typical use case is to detect data drift between the recent production serving dataset and the training dataset, or to compare the recent production dataset with a dataset from a previous period.

.. rubric:: Example

feature_drift_spec=DataDriftSpec( features=["feature1"] categorical_metric_type="l_infinity", numeric_metric_type="jensen_shannon_divergence", default_categorical_alert_threshold=0.01, default_numeric_alert_threshold=0.02, feature_alert_thresholds={"feature1":0.02, "feature2":0.01}, )

## Attributes  
  
---  
**Name** | **Description**  
`features` |  `List[str]`   
Optional. Feature names / Prediction output names interested in monitoring. These should be a subset of the input feature names or prediction output names specified in the monitoring schema. If not specified, all features / prediction outputs outlied in the monitoring schema will be used.   
`categorical_metric_type` |  `str`   
Optional. Supported metrics type: l_infinity, jensen_shannon_divergence   
`numeric_metric_type` |  `str`   
Optional. Supported metrics type: jensen_shannon_divergence   
`default_categorical_alert_threshold` |  `float`   
Optional. Default alert threshold for all the categorical features.   
`default_numeric_alert_threshold` |  `float`   
Optional. Default alert threshold for all the numeric features.   
`feature_alert_thresholds` |  `Dict[str, float]`   
Optional. Per feature alert threshold will override default alert threshold.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
