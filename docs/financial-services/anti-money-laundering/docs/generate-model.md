---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/generate-model/
title: Generate a model \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:32.147241+00:00
---

# Generate a model  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/generate-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Generate a model Stay organized with collections  Save and categorize content based on your preferences. 

This page briefly covers concepts behind model training. An AML AI model resource represents a trained model that can be used to generate risk scores and explainability.

## When to train or re-train

AML AI trains a model as part of creating a [Model resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models). The model must be trained before it can be evaluated (that is, backtested) or used to generate prediction results.

For best performance and to maintain the most up-to-date models, consider monthly re-training. However, a given engine version supports generating prediction results for 12 months from the release of a newer minor engine version.

**Note:** Training is a billable operation requiring significant compute resources and may take days to complete. For more information, see the [Pricing page](https://cloud.google.com/financial-services/anti-money-laundering/pricing).

## How to train

To train a model (that is, create a model), see [Create and manage models](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-models).

In particular, you need to select the following:

  * **The data to use for training:**

Specify a dataset and an end time within the date range of the dataset.

Training uses labels and features based on complete calendar months up to, but not including, the month of the selected end time. For more information, see [Dataset time ranges](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/overview-model-preparation#dataset-time-ranges).

  * **An engine config created using a[consistent dataset](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/overview-model-preparation#dataset-consistency):**

See [Configure an engine](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/configure-engine).




## Training output

Training generates a [Model resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models), which can be used to do the following:

  * Create backtest results, which are used to evaluate model performance using currently-known true positives
  * Create prediction results, which are used once you are ready to start reviewing new cases for potential money laundering



The [model metadata](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-models#export-metadata) contains the `missingness` metric, which can be used to assess [dataset consistency](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/overview-model-preparation#dataset-consistency) (for example, by comparing the missingness values of feature families from different operations)

Metric name | Metric description | Example metric value  
---|---|---  
Missingness  |  Share of missing values across all features in each feature family.  Ideally, all AML AI feature families should have a Missingness near to 0. Exceptions may occur where the data underlying those feature families is unavailable for integration.  A significant change in this value for any feature family between tuning, training, evaluation, and prediction can indicate inconsistency in the datasets used.  | 
    
    
    {
      "featureFamilies": [
        {
          "featureFamily": "unusual_wire_credit_activity",
          "missingnessValue": 0.00,
        },
        ...
        ...
        {
          "featureFamily": "party_supplementary_data_id_3",
          "missingnessValue": 0.45,
        },
      ],
    }
      
  
Importance  |  A metric that shows the importance of a feature family to the model. Higher values indicate more significant use of the feature family in the model. A feature family that is not used in the model has zero importance.  Importance values can be used when prioritizing acting on family skew results. For example, the same skew value for a family with higher importance to the model is more urgent to resolve.  | 
    
    
    {
      "featureFamilies": [
        {
          "featureFamily": "unusual_wire_credit_activity",
          "importanceValue": 459761000000,
        },
        ...
        ...
        {
          "featureFamily": "party_supplementary_data_id_3",
          "importanceValue": 27492,
        },
      ],
    }
      
  
Model metadata does not contain recall metrics from a test set. To generate recall measurements for a specific time period (for example, the test set), see [Evaluate a model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/evaluate-model).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
