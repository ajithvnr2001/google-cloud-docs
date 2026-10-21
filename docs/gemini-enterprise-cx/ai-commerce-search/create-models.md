---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models/
title: Create recommendation models \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:39.656085+00:00
---

# Create recommendation models  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Create recommendation models Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a new recommendations model.

**Note:** You don't need to manually configure or create models for search.

If you already have a recommendation model of the correct [type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#model-types) and you want to get predictions from it from a different location in your site, you can create a new serving config for it rather than creating a new model. [Learn more](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs).

## Introduction

When you want to use a new recommendation type for getting predictions, you must create a new recommendation model and provide sufficient user event data for it to be trained. You create serving configs for your new model, and when the model has finished training, request predictions from those serving configurations.

For an overview of the process of working with AI Commerce Search, see [Implement AI Commerce Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/overview).

## Create a recommendation model

Add a new recommendation model by using the [AI Commerce Search in Gemini Enterprise for Customer Experience console](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/dashboard/) or the [`models.Create` API method](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/create).

You can have up to 20 models per project, and up to 10 of them can be active (not paused) at any time. Learn more about [pausing a model](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-models#pause).

You can start up to five model operations per minute. Limited model operations include creation, deletion, pause, and resume. 

Before you create a new model:

  * Review and choose from the available [recommendation model types](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#model-types) and [model business objectives](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#opt-obj). These determine what kind of recommendations this model should be trained to provide.
  * Decide how often to [tune the model](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-models#tune). For tuning and training cost details, see [Pricing](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/pricing).
  * Make sure you have enough data uploaded to meet requirements for creating a new model. Some requirements depend on the model type you choose.
  * If you plan to create a Page-Level Optimization model:

    * Check that you already have recommendation serving configs that have trained models attached to them. You must provide a selection of recommendation serving configs that Page-Level Optimization can choose from when optimizing a page's recommendations.

    * Set up event recording for `detail-page-view` events and events that match the page type you will deploy the Page-Level Optimization model on (for example, if you deploy the model on a home page, make sure you set up recording for `home-page-view` events). To improve personalized recommendations, event recording for `purchase` and `add-to-cart` events is also recommended.

    * If you choose the conversion rate (CVR) business objective, event recording for `add-to-cart` events is required.

    * Make sure that after creating the Page-Level Optimization model, you continue to query the model to create recommendations impressions. These impressions are used to train the Page-Level Optimization model and improve the recommendations it serves.




To create a new model:

###  Google Cloud console 

  1. Go to the **Models** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Models page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/models/)

  2. Click **Create model**.

  3. Enter a name for your model.

The name must be 1024 characters or less, and can contain only alphanumeric characters, underscores, hyphens, and spaces.

  4. Choose the recommendation type.

  5. If you selected the [Page-Level Optimization model type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#plo):

     1. Choose the type of page the "Page-Level Optimization" model will optimize for you.

     2. Choose how much to restrict the serving of similar serving configs across panels:

        * **Unique model type:** Do not allow multiple serving configs with the same model type to be shown on different panels.

        * **Unique model:** Do not allow multiple serving configs with the same model to be shown on different panels.

        * **Unique serving config:** Do not allow the same serving config to be shown on multiple panels.

        * **No restriction:** Allow any serving configs to be shown on any number of panels.

     3. For each recommendation panel you plan to show with this model:

        1. Enter a panel ID.

        2. Select which serving configs the Page-Level Optimization model can consider as options for that panel.

For example, an add-to-cart page might have a recommendation panel where you want to display either Frequently Bought Together or Others You May Like recommendations. In this case, select a serving config that uses the Frequently Bought Together model and another that uses the Others You May Like model for consideration on this panel. When you make a prediction call to the Page-Level Optimization model, it chooses which type of recommendations you should display in that panel based on the end user's event history.

        3. Select a default serving config.

If a Google server outage occurs, the Page-Level Optimization model can still serve results from the default serving config.

     4. If you need to create additional panels, for each new panel click **Add a panel** and enter the new panel details.

  6. Choose the business objective, if available for the model type you selected.

  7. If you chose the Frequently Bought Together model type, select the **Context products type** :

     * **Multiple context products** : Use one or multiple items as context for recommendations from this model.
     * **Single context product** : Use one item as context for recommendations from this model.
  8. Review the **Data requirements met?** list to confirm that you have uploaded sufficient data for the model type you selected.

If an unmet data requirement prevents you from creating the model, an **X** _cancel_ icon appears next to the requirement and the **Create** button at the bottom of the **Create recommendation model** pane is disabled.

If you need to upload more data, carefully review the data requirements listed to make sure whether some or all of them need to be fulfilled for that model, then import the user events or products required to create the model

For how to import, see [Import historical user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events) and [Import catalog information](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog).

  9. Choose how often to tune the model. For tuning cost details, see [Pricing](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/pricing).

     * **Every three months** : The model automatically tunes every three months.
     * **Manual tune only** : The model is tuned only when you tune it manually.
  10. (**Public Preview feature**) Choose whether to automatically generate tags for filtering.

     * **Auto generate tags** : Turning on this option lets you filter recommendations results from this model. Having this option turned on can increase training time. For training cost details, see [Pricing](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/pricing).
     * **Do not generate tags** : If this option is turned off, you cannot get filtered recommendations from this model.
  11. Click **Create** to create the new recommendation model.

If you have uploaded sufficient user event data of the required type, the initial model training and tuning begins. Initial model training and tuning takes 2-5 days to complete, but can take longer for large datasets. 

You can [create serving configurations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs) for your new model before training completes, but they will serve only ["dry run" predictions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict) until the initial training and tuning completes and the model becomes active.




###  curl 

Make a `Models.create` request to the v2 API with an instance of `Model` in the request body. See the [`Models.create`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/create) API reference.

For details about all `Models` fields, see the [`Models` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models).
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data '{
                "name": "FULL_MODEL_NAME",
                "displayName": "DISPLAY_NAME",
                "trainingState": "TRAINING_STATE",
                "type": "MODEL_TYPE",
                "optimizationObjective": "OPTIMIZATION_OBJECTIVE",
                "periodicTuningState": "TUNING_STATE",
                "filteringOption": "FILTERING_STATE",
                "modelTypeConfig" {
                  "contextProductsType": "CONTEXT_PRODUCTS_TYPE"
                }
              }' \
      "https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/models"

If you have uploaded sufficient user event data of the required type, the initial model training and tuning begins. Initial model training and tuning takes 2-5 days to complete, but can take longer for large datasets. 

You can [create serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs) for your new model before training completes, but they will serve only ["dry run" predictions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict) until the initial training and tuning completes and the model becomes active.

### Requirements for creating a new recommendation model

The first time you use a specific recommendation type for your site, you are training a new machine learning model, which requires sufficient training data, as well as time to train and tune the model. The following steps are required to start using a new recommendation type:

  1. [Import your catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog) to AI Commerce Search, if you haven't already, and implement processes to keep the uploaded catalog up to date.
  2. Start [recording user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events) to AI Commerce Search, if you haven't already, making sure to follow the [best practices for recording user event data](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events#bps).
  3. Identify the [recommendation type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#model-types) and [optimization objective](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#opt-obj) you want to use.
  4. Determine the user event data requirement for your selected recommendation type and objective.
  5. [Import historical user event data](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events) to meet the minimum event data requirements, or wait until the user event data collection meets the minimum requirements.
  6. Create your model and your [serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs).

At this point, AI Commerce Search initiates model training and tuning. Initial model training and tuning takes 2-5 days to complete, but can take longer for large datasets. 

  7. Confirm that your model is working correctly using [prediction preview](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict#preview).

  8. Create your [A/B experiment](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/a-b-testing).




### Model type minimum data requirements

The type of user events you import, and the amount of data you need, depends on your [recommendation (model) type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#model-types) and your [optimization objective](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#opt-obj). When you reach the minimum data requirement, you can begin model training.

The data collection window represents the period for user events; importing more historical data has no effect on model quality.

Make sure to use real user events and real catalog data. Good quality models can't be built on synthetic data.

Model type | Optimization objective | Supported user event types | Minimum data requirement | Data collection window  
---|---|---|---|---  
Recommended for You | Click-through rate |  `detail-page-view`  
  
`home-page-view` |  7 days of `detail-page-view` events in the last 90 days AND 10 occurrences per catalog item on average (with a 90 days window) of `detail-page-view` events OR 60 days of `detail-page-view` events in the last 90 days  100 unique catalog items for the `detail-page-view` event in the last 90 days  10,000 `detail-page-view` events in the last 90 days  AND 7 days of `home-page-view` events in the last 90 days  10,000 `home-page-view` events in the last 90 days  | 3 months  
Recommended for You | Conversion rate |  `add-to-cart`  
  
`detail-page-view`  
  
`home-page-view` |  7 days of ` add-to-cart` events in the last 90 days AND 10 occurrences per catalog item on average (with a 90 days window) of `add-to-cart` events OR 60 days of ` add-to-cart` events in the last 90 days  100 unique catalog items for the `add-to-cart` event in the last 90 days  10,000 `add-to-cart` events in the last 90 days  AND 7 days of `detail-page-view ` events in the last 90 days AND 10 occurrences per catalog item on average (with a 90 days window) of `detail-page-view ` events OR 60 days of `detail-page-view ` events in the last 90 days  100 unique catalog items for the `detail-page-view ` event in the last 90 days  10,000 `detail-page-view ` events in the last 90 days  AND 7 days of `home-page-view` events in the last 90 days  10,000 `home-page-view` events in the last 90 days  | 3 months  
Recommended for You | Revenue per session |  `add-to-cart`  
  
`detail-page-view`  
  
`home-page-view` |  7 days of ` add-to-cart` events in the last 90 days AND 10 occurrences per catalog item on average (with a 90 days window) of ` add-to-cart` events OR 60 days of ` add-to-cart` events in the last 90 days  100 unique catalog items for the ` add-to-cart` event in the last 90 days  10,000 ` add-to-cart` events in the last 90 days  AND 7 days of `home-page-view` events in the last 90 days  10,000 ` home-page-view ` events in the last 90 days  | 3 months  
Others You May Like | Click-through rate |  `detail-page-view` |  7 days of `detail-page-view` events in the last 90 days AND 10 occurrences per catalog item on average (with a 90 days window) of `detail-page-view` events OR 60 days of `detail-page-view`events in the last 90 days  100 unique catalog items for the `detail-page-view` event in the last 90 days  10,000 `detail-page-view` events in the last 90 days  | 3 months  
Others You May Like | Conversion rate |  `add-to-cart`  
  
`detail-page-view` |  7 days of `add-to-cart` events in the last 90 days AND 10 occurrences per catalog item on average (with a 90 days window) of `add-to-cart`events OR 60 days of `add-to-cart` events in the last 90 days  100 unique catalog items for the `add-to-cart` event in the last 90 days  10,000 `add-to-cart` events in the last 90 days  AND 7 days of `detail-page-view` events in the last 90 days AND 10 occurrences per catalog item on average (with a 90 days window) of `detail-page-view` events OR 60 days of `detail-page-view` events in the last 90 days  100 unique catalog items for the `detail-page-view` event in the last 90 days  10,000 `detail-page-view` events in the last 90 days  | 3 months  
Others You May Like | Revenue per session |  `add-to-cart`  
  
`detail-page-view` |  7 days of `add-to-cart` events in the last 90 days AND 10 occurrences per catalog item on average (with a 90 days window) of `add-to-cart`events OR 60 days of `add-to-cart` events in the last 90 days  100 unique catalog items for the `add-to-cart` event in the last 90 days  10,000 `add-to-cart` events in the last 90 days  AND 7 days of `detail-page-view` events in the last 90 days AND 10 occurrences per catalog item on average (with a 90 days window) of `detail-page-view` events OR 60 days of `detail-page-view` events in the last 90 days  100 unique catalog items for the `detail-page-view` event in the last 90 days  10,000 `detail-page-view` events in the last 90 days  | 3 months  
Frequently Bought Together | Revenue per session |  `purchase-complete` |  10 occurrences per catalog item on average (with a 1 year window of `purchase-complete` events) OR 90 days of `purchase-complete` events in the last 1 year  100 unique catalog items for the `purchase-complete` event in the last 1 year  1,000 `purchase-complete` events in the last 1 year  |  3 months We recommend uploading events at least daily to maintain good data quality. During historical event imports, make sure that data distribution skews toward the most recent timestamp. The number of events on the last timestamp day should be equal to or more than the average daily event count.   
On-sale | Click-through rate |  `detail-page-view`  
  
`home-page-view` |  7 days of `detail-page-view` events in the last 90 days AND 10 occurrences per catalog item on average (with a 90 days window) of `detail-page-view` events OR 60 days of `detail-page-view` events in the last 90 days  100 unique catalog items for the `detail-page-view` event in the last 90 days  10,000 `detail-page-view` events in the last 90 days  AND 7 days of `home-page-view` events in the last 90 days  10,000 `home-page-view` events in the last 90 days  | 3 months  
On-sale | Conversion rate |  `add-to-cart`  
  
`detail-page-view`  
  
`home-page-view` |  7 days of `add-to-cart` events in the last 90 days AND 10 occurrences per catalog item on average (with a 90 days window) of `add-to-cart` events OR 60 days of `add-to-cart` events in the last 90 days  100 unique catalog items for the `add-to-cart` event in the last 90 days  10,000 `add-to-cart` events in the last 90 days  AND 7 days of `detail-page-view` events in the last 90 days AND 10 occurrences per catalog item on average (with a 90 days window) of `detail-page-view` events OR 60 days of `detail-page-view` events in the last 90 days  100 unique catalog items for the `detail-page-view` event in the last 90 days  10,000 `detail-page-view` events in the last 90 days  AND 7 days of `home-page-view` events in the last 90 days  10,000 `home-page-view` events in the last 90 days  | 3 months  
Similar Items | N/A |  None required.  |  100 product SKUs must be in some branch  | N/A  
Page-Level Optimization | Any |  `detail-page-view`  
  
`add-to-cart`  
  
`purchase-complete`  
  
`home-page-view` |  Page-Level Optimization optimizes recommendation panels by choosing between several possible models. Refer to the data requirements for the models you select as options for Page-Level Optimization.  | N/A  
Buy it Again | N/A |  `purchase-complete` |  10 occurrences per catalog item on average (with a 90 days window of `purchase-complete` events) OR 60 days of `purchase-complete` events in the last 90 days  100 unique catalog items for the `purchase-complete` event in the last 90 days  1,000 `purchase-complete` events in the last 90 days  100 product SKUs must be in some branch  |  N/A  We recommend uploading events at least daily to maintain good data quality. During historical event imports, make sure that data distribution skews toward the most recent timestamp. The number of events on the last timestamp day should be equal to or more than the average daily event count.   
  
## What's next

  * [Create a serving config](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs) for your model.
  * Learn how to [pause and resume training](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-models#pause) for your model.
  * When the model finishes training, [start requesting recommendations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
