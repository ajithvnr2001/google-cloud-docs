---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/configure-engine/
title: Configure an engine \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:32:46.880888+00:00
---

# Configure an engine  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/configure-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Configure an engine Stay organized with collections  Save and categorize content based on your preferences. 

This page briefly covers concepts behind configuring an engine.

Before v004.009 v004.009 and later

This page is valid for the engine versions within the following major engine version groupings. To view the page for other engine versions, use the selector at the top of this page. 

  * [aml-retail.default.v004.009](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/private/engine-versions/aml-retail.default.v004#aml-retail.default.v004.009)
  * [aml-commercial.default.v004.009](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/private/engine-versions/aml-commercial.default.v004#aml-commercial.default.v004.009)



In summary, here are the changes from engine versions v003 to v004 (up to v004.008):

  * Added `partiesCount` and `identifiedPartiesCount` to the `ExpectedRecallPreTuning` and `ExpectedRecallPostTuning` metrics values.



## Supported sources for hyperparameters

When configuring an engine, you can select the source of the hyperparameters that are used to create a model. The following sources are supported:

  * Automatic tuning: AML AI tunes hyperparameters when you create an [EngineConfig resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs) (default behavior)
  * Inherit: Inherit hyperparameters from a previous engine config that was created with an earlier engine version within the same [tuning version](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/glossary#engine-version). This setting lets you avoid re-tuning each time you adopt a new model engine version.



## When to tune or inherit

The following sections outline when you should select automatic tuning and when you should inherit hyperparameters from a previous engine config.

### When to tune

You have the option to tune each new engine config and, when in doubt, you should always tune for best performance outcomes. See section How to tune an engine for more information.

For best performance, you should consider engine tuning when any of the following occur:

  * You make significant changes to dataset logic. For example, when any of the following change: 
    * The logic by which fields are populated
    * The selection of RECOMMENDED fields that are populated
    * The logic or selection of data provided in the [PartySupplementaryData](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#partysupplementarydata) table
  * You're about to have an engine train a model for a new [region](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations).

**Note:** Engine tuning is a billable operation requiring significant compute resources and may take days to complete. For more information, see the [Pricing page](https://cloud.google.com/financial-services/anti-money-laundering/pricing).

### When to inherit hyperparameters

To save time and costs when adopting a new engine version, you can inherit hyperparameters from a previous engine using the same tuning version. See section How to adopt an engine version without re-tuning.

**Note:** This inheritance requires an existing engine config, within the same tuning engine version, to use as a source for hyperparameters. This is supported on all engine versions with tuning version v004 and higher, and released from 2024-02-22. For more information, see the [engine version release notes](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/engine-versions).

Engine versions with tuning version v003, and engine versions released prior to 2024-02-22, don't support the inheriting of hyperparameters, but these versions may be used as a source of hyperparameters.

## How to tune an engine

To trigger tuning, see [Create and manage engine configs](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-engine-configs).

In particular, you need to select the following:

  * **The data to use for engine tuning:**

Specify a dataset and an end time within the date range of the dataset.

Engine tuning uses labels and features based on complete calendar months up to, but not including, the month of the selected end time. For more information, see [Dataset time ranges](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/overview-model-preparation#dataset-time-ranges).

  * **The engine version to use for engine tuning:**

[Select an engine version](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-engine-versions) that matches the line of business (retail or commercial) that you will use the associated models for.

  * **The volume of investigations you expect based on the models:**

Specify `partyInvestigationsPerPeriodHint`. This is used by engine tuning, training, and backtesting to ensure AML AI delivers performance at your monthly investigation volume. 




## Engine tuning output

Engine tuning generates an [EngineConfig resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs), which can be used to create a [Model resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models).

The [engine config metadata](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-engine-configs#export-metadata) contains the following metrics. In particular, these metrics show you the following:

  * Expected performance gain from engine tuning versus using the default hyperparameters

**Note** : Recall metrics only show the share of historical [`AML_EXIT`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/lifecycle-risk-case) events that would be alerted with a given model, and can be used to decide to proceed to live testing. Given that not all customers alerted by the model have previously been investigated, real-life performance is expected to be significantly better.

  * Measurements which can be used to assess dataset consistency (for example, by comparing the missingness values of feature families from different operations)


Metric name | Metric description | Example metric value  
---|---|---  
ExpectedRecallPreTuning  | Recall metric measured on a test set when using **default hyperparameters** of the engine version.  This recall measurement assumes the number of investigations per month specified in `partyInvestigationsPerPeriodHint`.  | 
    
    
    {
      "recallValues": [
        {
          "partyInvestigationsPerPeriod": 5000,
          "recallValue": 0.72,
          "partiesCount": 100,
          "identifiedPartiesCount": 72,
          "scoreThreshold": 0.42,
        },
      ],
    }
      
  
ExpectedRecallPostTuning  | Recall metric measured on a test set when using **tuned hyperparameters**.  This recall measurement assumes the number of investigations per month specified in `partyInvestigationsPerPeriodHint`.  | 
    
    
    {
      "recallValues": [
        {
          "partyInvestigationsPerPeriod": 5000,
          "recallValue": 0.80,
          "partiesCount": 100,
          "identifiedPartiesCount": 80,
          "scoreThreshold": 0.43,
        },
      ],
    }
      
  
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
      
  
## How to adopt an engine version without re-tuning

To re-use hyperparameters from a previous engine config, see section [Create an engine config that inherits hyperparameters](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-engine-configs#create-engine-config-inherit) (on the [Create and manage engine configs](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-engine-configs) page). In particular, you need to select the following:

  * **Hyperparameter source type:** Select `INHERITED` as the [`hyperparameterSourceType`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs#EngineConfig.FIELDS.hyperparameter_source_type). If you don't specify the source type, the hyperparameter source type is set to `TUNING` to allow for backwards compatibility.
  * **Hyperparameter source:** Specify the full resource name of the source engine config in the [`hyperparameterSource`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs#EngineConfig.FIELDS.hyperparameter_source) object. The outputs of the source engine config are used for the new engine config. The source engine config must have been created with an earlier engine version within the same [tuning engine version](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/glossary#engine-version) that you are now using.
  * **Engine version to use for the engine config:** [Select an engine version](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-engine-versions) that matches the line of business (retail or commercial) for the models you want to use. If inheriting hyperparameters, the line of business must match the line of business used for the hyperparameter source.



## Output and lineage when inheriting

Inheriting hyperparameters from another engine version creates an [EngineConfig resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs) which can be used to create a [Model resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models) using the hyperparameters from the source engine config.

For lineage, the following fields in the [EngineConfig resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs) are set as follows when inheriting hyperparameters from another engine config:

  * `hyperparameterSourceType`: `INHERITED`
  * `hyperparameterSource`: The engine config used as the hyperparameter source
  * `tuning`: Original [`tuning`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs#EngineConfig.FIELDS.tuning) object, including the reference to the dataset used for the original engine tuning (`primaryDataset`) and the latest time from which data was used to generate features for training (`endTime`)
  * `performanceTarget`: Original [`performanceTarget`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs#EngineConfig.FIELDS.performance_target) object, including the volume of investigations expected based on the specified models (`partyInvestigationsPerPeriodHint`)
  * [Engine config metadata](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-engine-configs#export-metadata) from the original engine tuning



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
