---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models
title: REST Resource: projects.locations.catalogs.models \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:59:02.319802+00:00
---

# REST Resource: projects.locations.catalogs.models  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  REST Resource: projects.locations.catalogs.models Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Model
    * JSON representation
  * TrainingState
  * ServingState
  * PeriodicTuningState
  * DataState
  * ServingConfigList
    * JSON representation
  * ModelFeaturesConfig
    * JSON representation
  * FrequentlyBoughtTogetherFeaturesConfig
    * JSON representation
  * ContextProductsType
  * Methods



## Resource: Model

Metadata that describes the training and serving parameters of a `[Model](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#Model)`. A `[Model](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#Model)` can be associated with a `[ServingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs#ServingConfig)` and then queried through the Predict API.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "trainingState": enum ([TrainingState](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#TrainingState)),
      "servingState": enum ([ServingState](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#ServingState)),
      "createTime": string,
      "updateTime": string,
      "type": string,
      "optimizationObjective": string,
      "periodicTuningState": enum ([PeriodicTuningState](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#PeriodicTuningState)),
      "lastTuneTime": string,
      "tuningOperation": string,
      "dataState": enum ([DataState](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#DataState)),
      "filteringOption": enum ([RecommendationsFilteringOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/RecommendationsFilteringOption)),
      "servingConfigLists": [
        {
          object ([ServingConfigList](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#ServingConfigList))
        }
      ],
      "modelFeaturesConfig": {
        object ([ModelFeaturesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#ModelFeaturesConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The fully qualified resource name of the model.Format: `projects/{projectNumber}/locations/{locationId}/catalogs/{catalogId}/models/{modelId}` catalogId has char limit of 50. recommendation_model_id has char limit of 40.  
`displayName` |  `string` Required. The display name of the model.Should be human readable, used to display Recommendation Models in the Retail Cloud Console Dashboard. UTF-8 encoded string with limit of 1024 characters.  
`trainingState` |  `enum (`[TrainingState](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#TrainingState)`)` Optional. The training state that the model is in (e.g. `TRAINING` or `PAUSED`).Since part of the cost of running the service is frequency of training - this can be used to determine when to train model in order to control cost. If not specified: the default value for `models.create` method is `TRAINING`. The default value for `models.patch` method is to keep the state the same as before.  
`servingState` |  `enum (`[ServingState](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#ServingState)`)` Output only. The serving state of the model: `ACTIVE`, `NOT_ACTIVE`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp the Recommendation Model was created at.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp the Recommendation Model was last updated. E.g. if a Recommendation Model was paused - this would be the time the pause was initiated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`type` |  `string` Required. The type of model e.g. `home-page`.Currently supported values: `recommended-for-you`, `others-you-may-like`, `frequently-bought-together`, `page-optimization`, `similar-items`, `buy-it-again`, `on-sale-items`, and `recently-viewed`(readonly value).This field together with `[optimizationObjective](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#Model.FIELDS.optimization_objective)` describe model metadata to use to control model training and serving. See <https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models> for more details on what the model metadata control and which combination of parameters are valid. For invalid combinations of parameters (e.g. type = `frequently-bought-together` and optimizationObjective = `ctr`), you receive an error 400 if you try to create/update a recommendation with this set of knobs.  
`optimizationObjective` |  `string` Optional. The optimization objective e.g. `cvr`.Currently supported values: `ctr`, `cvr`, `revenue-per-order`.If not specified, we choose default based on model type. Default depends on type of recommendation:`recommended-for-you` => `ctr``others-you-may-like` => `ctr``frequently-bought-together` => `revenue_per_order`This field together with `[optimizationObjective](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#Model.FIELDS.type)` describe model metadata to use to control model training and serving. See <https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models> for more details on what the model metadata control and which combination of parameters are valid. For invalid combinations of parameters (e.g. type = `frequently-bought-together` and optimizationObjective = `ctr`), you receive an error 400 if you try to create/update a recommendation with this set of knobs.  
`periodicTuningState` |  `enum (`[PeriodicTuningState](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#PeriodicTuningState)`)` Optional. The state of periodic tuning.The period we use is 3 months - to do a one-off tune earlier use the `models.tune` method. Default value is `PERIODIC_TUNING_ENABLED`.  
`lastTuneTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the latest successful tune finished.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`tuningOperation` |  `string` Output only. The tune operation associated with the model.Can be used to determine if there is an ongoing tune for this recommendation. Empty field implies no tune is goig on.  
`dataState` |  `enum (`[DataState](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#DataState)`)` Output only. The state of data requirements for this model: `DATA_OK` and `DATA_ERROR`.Recommendation model cannot be trained if the data is in `DATA_ERROR` state. Recommendation model can have `DATA_ERROR` state even if serving state is `ACTIVE`: models were trained successfully before, but cannot be refreshed because model no longer has sufficient data for training.  
`filteringOption` |  `enum (`[RecommendationsFilteringOption](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/RecommendationsFilteringOption)`)` Optional. If `RECOMMENDATIONS_FILTERING_ENABLED`, recommendation filtering by attributes is enabled for the model.  
`servingConfigLists[]` |  `object (`[ServingConfigList](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#ServingConfigList)`)` Output only. The list of valid serving configs associated with the PageOptimizationConfig.  
`modelFeaturesConfig` |  `object (`[ModelFeaturesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#ModelFeaturesConfig)`)` Optional. Additional model features config.  
  
## TrainingState

The training state of the model.

Enums  
---  
`TRAINING_STATE_UNSPECIFIED` | Unspecified training state.  
`PAUSED` | The model training is paused.  
`TRAINING` | The model is training.  
  
## ServingState

The serving state of the model.

Enums  
---  
`SERVING_STATE_UNSPECIFIED` | Unspecified serving state.  
`INACTIVE` | The model is not serving.  
`ACTIVE` | The model is serving and can be queried.  
`TUNED` | The model is trained on tuned hyperparameters and can be queried.  
  
## PeriodicTuningState

Describes whether periodic tuning is enabled for this model or not. Periodic tuning is scheduled at most every three months. You can start a tuning process manually by using the `models.tune` method, which starts a tuning process immediately and resets the quarterly schedule. Enabling or disabling periodic tuning does not affect any current tuning processes.

Enums  
---  
`PERIODIC_TUNING_STATE_UNSPECIFIED` | Unspecified default value, should never be explicitly set.  
`PERIODIC_TUNING_DISABLED` | The model has periodic tuning disabled. Tuning can be reenabled by calling the `EnableModelPeriodicTuning` method or by calling the `models.tune` method.  
`ALL_TUNING_DISABLED` | The model cannot be tuned with periodic tuning OR the `models.tune` method. Hide the options in customer UI and reject any requests through the backend self serve API.  
`PERIODIC_TUNING_ENABLED` | The model has periodic tuning enabled. Tuning can be disabled by calling the `DisableModelPeriodicTuning` method.  
  
## DataState

Describes whether this model have sufficient training data to be continuously trained.

Enums  
---  
`DATA_STATE_UNSPECIFIED` | Unspecified default value, should never be explicitly set.  
`DATA_OK` | The model has sufficient training data.  
`DATA_ERROR` | The model does not have sufficient training data. Error messages can be queried via Stackdriver.  
  
## ServingConfigList

Represents an ordered combination of valid serving configs, which can be used for `PAGE_OPTIMIZATION` recommendations.

JSON representation  
---  
      
    
    {
      "servingConfigIds": [
        string
      ]
    }  
  
Fields  
---  
`servingConfigIds[]` |  `string` Optional. A set of valid serving configs that may be used for `PAGE_OPTIMIZATION`.  
  
## ModelFeaturesConfig

Additional model features config.

JSON representation  
---  
      
    
    {
    
      // Union field type_dedicated_config can be only one of the following:
      "frequentlyBoughtTogetherConfig": {
        object ([FrequentlyBoughtTogetherFeaturesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#FrequentlyBoughtTogetherFeaturesConfig))
      }
      // End of list of possible types for union field type_dedicated_config.
    }  
  
Fields  
---  
Union field `type_dedicated_config`.`type_dedicated_config` can be only one of the following:  
`frequentlyBoughtTogetherConfig` |  `object (`[FrequentlyBoughtTogetherFeaturesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#FrequentlyBoughtTogetherFeaturesConfig)`)` Additional configs for frequently-bought-together models.  
  
## FrequentlyBoughtTogetherFeaturesConfig

Additional configs for the frequently-bought-together model type.

JSON representation  
---  
      
    
    {
      "contextProductsType": enum ([ContextProductsType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#ContextProductsType))
    }  
  
Fields  
---  
`contextProductsType` |  `enum (`[ContextProductsType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#ContextProductsType)`)` Optional. Specifies the context of the model when it is used in predict requests. Can only be set for the `frequently-bought-together` type. If it isn't specified, it defaults to `[MULTIPLE_CONTEXT_PRODUCTS](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#ContextProductsType.ENUM_VALUES.MULTIPLE_CONTEXT_PRODUCTS)`.  
  
## ContextProductsType

Use single or multiple context products for recommendations.

Enums  
---  
`CONTEXT_PRODUCTS_TYPE_UNSPECIFIED` | Unspecified default value, should never be explicitly set. Defaults to `[MULTIPLE_CONTEXT_PRODUCTS](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models#ContextProductsType.ENUM_VALUES.MULTIPLE_CONTEXT_PRODUCTS)`.  
`SINGLE_CONTEXT_PRODUCT` | Use only a single product as context for the recommendation. Typically used on pages like add-to-cart or product details.  
`MULTIPLE_CONTEXT_PRODUCTS` | Use one or multiple products as context for the recommendation. Typically used on shopping cart pages.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/create)`

|  Creates a new model.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/delete)`

|  Deletes an existing model.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/get)`

|  Gets a model.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/list)`

|  Lists all the models linked to this event store.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/patch)`

|  Update of model metadata.  
  
### `[pause](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/pause)`

|  Pauses the training of an existing model.  
  
### `[resume](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/resume)`

|  Resumes the training of an existing model.  
  
### `[tune](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.models/tune)`

|  Tunes an existing model.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
