---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/logging/
title: View model architecture \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:46.295528+00:00
---

# View model architecture  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  View model architecture Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about how to use Cloud Logging to view details about a Gemini Enterprise Agent Platform model. Using Logging, you see:

  * The hyperparameters of the final model as key-value pairs.
  * The hyperparameters and object values used during model training and tuning, as well as an objective value.



By default, logs are deleted after 30 days.

The following topics are covered:

  1. Viewing training logs.
  2. Log fields.

**Note:** Model architecture logs are provided as part of the Cloud Logging service. For general information about Cloud Logging, see the [Cloud Logging](https://docs.cloud.google.com/logging/docs) documentation.

## Before you begin

Before you can view the hyperparameter logs for your model, you must [train it](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/train-model).

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions):

  * `logging.logServiceIndexes.list` on the project
  * `logging.logServices.list` on the project



## Viewing training logs

You can use the Google Cloud console to access the hyperparameter logs of the final model and the hyperparameter logs of the tuning trials.

  1. In the Google Cloud console, go to the Gemini Enterprise Agent Platform **Models** page.

[Go to Models page](https://console.cloud.google.com/agent-platform/models)

  2. In the **Region** drop-down, select the region where your model is located.

  3. From the list of models, select your model.

  4. Select your model's version number.

  5. Open the **Version Details** tab.

  6. To see the hyperparameter log of the final model, go to the **Model hyperparameters** row and click **Model**.

     1. There is just one log entry. Expand the payload as shown below. For details, see Log fields.

![Expanded Models logs](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/images/model-logs-expanded.png)

  7. To see the hyperparameter log of the tuning trials, go to the **Model hyperparameters** row and click **Trials**.

     1. There is one entry for each of the tuning trials. Expand the payload as shown below. For details, see Log fields.

![Expanded Trials logs](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/images/trials-logs-expanded.png)




## Log fields

Activity logs are structured as described in the [LogEntry](https://docs.cloud.google.com/logging/docs/exported_logs#the_logentry_type) type documentation.

Gemini Enterprise Agent Platform model logs have, among other fields:

  * `labels`: The `log_type` field is set to `automl_tables`.
  * `jsonPayload`: The specific details of the log entry, provided in JSON object format. For details, see Payload contents for the hyperparameter log of the final model or Payload contents for the hyperparameter log of a tuning trial.
  * `timestamp`: The date and time when the model was created or the trial was run.



### Payload contents for the hyperparameter log of the final model

The `jsonPayload` field for the hyperparameter log of the final model contains a `modelParameters` field. This field contains one entry for each model that contributes to the final ensemble model. Each entry has a `hyperparameters` field, whose contents depend on the model type. For details, see List of hyperparameters.

### Payload contents for the hyperparameter log of a tuning trial

The `jsonPayload` field for the hyperparameter log of a tuning trial contains the following fields:

Field | Type | Description  
---|---|---  
`modelStructure` | JSON |  A description of the Agent Platform model structure. This field contains a `modelParameters` field. The `modelParameters` field has a `hyperparameters` field, whose contents depend on the model type. For details, see List of hyperparameters.   
`trainingObjectivePoint` | JSON | The optimization objective used for model training. This entry includes a timestamp and an objective value at the time the log entry was recorded.  
  
### List of hyperparameters

The hyperparameter data provided in the logs differ for each type of model. The following sections describe the hyperparameters for each model type.

#### Gradient boosted decision tree models

  * Tree L1 regularization
  * Tree L2 regularization
  * Max tree depth
  * Model type: `GBDT`
  * Number of trees
  * Tree complexity



#### Feedforward neural network models

  * Dropout rate
  * Enable batchNorm (`True` or `False`)
  * Enable embedding L1 (`True` or `False`)
  * Enable embedding L2 (`True` or `False`)
  * Enable L1 (`True` or `False`)
  * Enable L2 (`True` or `False`)
  * Enable layerNorm (`True` or `False`)
  * Enable numerical embedding (`True` or `False`)
  * Hidden layer size
  * Model type: `nn`
  * Normalize numerical column (`True` or `False`)
  * Number of cross layers
  * Number of hidden layers
  * Skip connections type (`dense`, `disable`, `concat`, or `slice_or_padding`)



## What's next

Once you're ready to make predictions with your classification or regression model, you have two options:

  * [Make online (real-time) predictions using your model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/get-online-predictions).
  * [Get batch predictions directly from your model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/get-batch-predictions).



Additionally, you can:

  * [Evaluate your model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/evaluate-model).
  * [Review general information about Cloud Logging](https://docs.cloud.google.com/logging/docs).
  * You can export your logs to BigQuery, Cloud Storage, or Pub/Sub. Read [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) in the Logging documentation to learn how to export activity logs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
