---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources.preview.ml_monitoring.spec.ModelMonitoringSchema
title: Class ModelMonitoringSchema (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:40.711087+00:00
---

# Class ModelMonitoringSchema (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources.preview.ml_monitoring.spec.ModelMonitoringSchema

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ModelMonitoringSchema (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    ModelMonitoringSchema(
        feature_fields: typing.MutableSequence[
            vertexai.resources.preview.ml_monitoring.spec.schema.FieldSchema
        ],
        ground_truth_fields: typing.Optional[
            typing.MutableSequence[
                vertexai.resources.preview.ml_monitoring.spec.schema.FieldSchema
            ]
        ] = None,
        prediction_fields: typing.Optional[
            typing.MutableSequence[
                vertexai.resources.preview.ml_monitoring.spec.schema.FieldSchema
            ]
        ] = None,
    )

Initializer for ModelMonitoringSchema.

## Parameters  
  
---  
**Name** | **Description**  
`feature_fields` |  `MutableSequence[FieldSchema]`   
Required. Feature names of the model. Vertex AI will try to match the features from your dataset as follows: * For 'csv' files, the header names are required, and we will extract thecorresponding feature values when the header names align with the feature names. * For 'jsonl' files, we will extract the corresponding feature values if the key names match the feature names. Note: Nested features are not supported, so please ensure your features are flattened. Ensure the feature values are scalar or an array of scalars. * For 'bigquery' dataset, we will extract the corresponding feature values if the column names match the feature names. Note: The column type can be a scalar or an array of scalars. STRUCT or JSON types are not supported. You may use SQL queries to select or aggregate the relevant features from your original table. However, ensure that the 'schema' of the query results meets our requirements. * For the Vertex AI Endpoint Request Response Logging table or Vertex AI Batch Prediction Job results. If the prediction instance format is an array, ensure that the sequence in `feature_fields` matches the order of features in the prediction instance. We will match the feature with the array in the order specified in `feature_fields`.  
`prediction_fields` |  `MutableSequence[FieldSchema]`   
Optional. Prediction output names of the model. The requirements are the same as the `feature_fields`. For AutoML Tables, the prediction output name presented in schema will be: `predicted_{target_column}`, the `target_column` is the one you specified when you train the model. For Prediction output drift analysis: * AutoML Classification, the distribution of the argmax label will be analyzed. * AutoML Regression, the distribution of the value will be analyzed.  
`ground_truth_fields` |  `MutableSequence[FieldSchema]`   
Optional. Target /ground truth names of the model.  
  
## Methods 

### to_json
    
    
    to_json(output_dir: typing.Optional[str] = None) -> str

Transform ModelMonitoringSchema to json format.

**Parameter**  
---  
**Name** | **Description**  
`output_dir` |  `str`   
Optional. The output directory that the transformed json file would be put into.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
