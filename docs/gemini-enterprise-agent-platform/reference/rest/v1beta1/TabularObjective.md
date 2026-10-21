---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective/
title: TabularObjective \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:30:37.970261+00:00
---

# TabularObjective  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  TabularObjective Stay organized with collections  Save and categorize content based on your preferences. 

Tabular monitoring objective.

Fields  
  
`featureDriftSpec` `object (`[DataDriftSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#DataDriftSpec)`)` Input feature distribution drift monitoring spec. | `predictionOutputDriftSpec` `object (`[DataDriftSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#DataDriftSpec)`)` Prediction output distribution drift monitoring spec. | `featureAttributionSpec` `object (`[FeatureAttributionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#FeatureAttributionSpec)`)` feature attribution monitoring spec. | JSON representation  
---  
      
    
    {
      "featureDriftSpec": {
        object ([DataDriftSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#DataDriftSpec))
      },
      "predictionOutputDriftSpec": {
        object ([DataDriftSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#DataDriftSpec))
      },
      "featureAttributionSpec": {
        object ([FeatureAttributionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#FeatureAttributionSpec))
      }
    }  
  
## DataDriftSpec

data drift monitoring spec. data drift measures the distribution distance between the current dataset and a baseline dataset. A typical use case is to detect data drift between the recent production serving dataset and the training dataset, or to compare the recent production dataset with a dataset from a previous period.

Fields  
  
`features[]` `string` feature names / Prediction output names interested in monitoring. These should be a subset of the input feature names or prediction output names specified in the monitoring schema. If the field is not specified all features / prediction outputs outlied in the monitoring schema will be used. | `categoricalMetricType` `string` Supported metrics type: * l_infinity * jensen_shannon_divergence | `numericMetricType` `string` Supported metrics type: * jensen_shannon_divergence | `defaultCategoricalAlertCondition` `object (`[ModelMonitoringAlertCondition](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#ModelMonitoringAlertCondition)`)` Default alert condition for all the categorical features. | `defaultNumericAlertCondition` `object (`[ModelMonitoringAlertCondition](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#ModelMonitoringAlertCondition)`)` Default alert condition for all the numeric features. | `featureAlertConditions` `map (key: string, value: object (`[ModelMonitoringAlertCondition](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#ModelMonitoringAlertCondition)`))` Per feature alert condition will override default alert condition. | JSON representation  
---  
      
    
    {
      "features": [
        string
      ],
      "categoricalMetricType": string,
      "numericMetricType": string,
      "defaultCategoricalAlertCondition": {
        object ([ModelMonitoringAlertCondition](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#ModelMonitoringAlertCondition))
      },
      "defaultNumericAlertCondition": {
        object ([ModelMonitoringAlertCondition](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#ModelMonitoringAlertCondition))
      },
      "featureAlertConditions": {
        string: {
          object ([ModelMonitoringAlertCondition](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#ModelMonitoringAlertCondition))
        },
        ...
      }
    }  
  
## ModelMonitoringAlertCondition

Monitoring alert triggered condition.

Fields  
  
`condition` `Union type`  
  
Alert triggered condition. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`threshold` `number` A condition that compares a stats value against a threshold. Alert will be triggered if value above the threshold. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // condition
      "threshold": number
      // Union type
    }  
  
## FeatureAttributionSpec

feature attribution monitoring spec.

Fields  
  
`features[]` `string` feature names interested in monitoring. These should be a subset of the input feature names specified in the monitoring schema. If the field is not specified all features outlied in the monitoring schema will be used. | `defaultAlertCondition` `object (`[ModelMonitoringAlertCondition](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#ModelMonitoringAlertCondition)`)` Default alert condition for all the features. | `featureAlertConditions` `map (key: string, value: object (`[ModelMonitoringAlertCondition](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#ModelMonitoringAlertCondition)`))` Per feature alert condition will override default alert condition. | `batchExplanationDedicatedResources` `object (`[BatchDedicatedResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchDedicatedResources)`)` The config of resources used by the Model Monitoring during the batch explanation for non-AutoML models. If not set, `n1-standard-2` machine type will be used by default. | JSON representation  
---  
      
    
    {
      "features": [
        string
      ],
      "defaultAlertCondition": {
        object ([ModelMonitoringAlertCondition](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#ModelMonitoringAlertCondition))
      },
      "featureAlertConditions": {
        string: {
          object ([ModelMonitoringAlertCondition](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/TabularObjective#ModelMonitoringAlertCondition))
        },
        ...
      },
      "batchExplanationDedicatedResources": {
        object ([BatchDedicatedResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchDedicatedResources))
      }
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
