---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-models/
title: Manage models \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:04.603528+00:00
---

# Manage models  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Manage models Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to tune, pause, resume, delete, and list recommendation models. For help with creating a new recommendation model, see [Create recommendation models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models).

**Note:** Model management is only available for recommendations.

## General recommendations for model quality

Events should generally be uploaded at least daily to maintain good data quality.

  * **Data age limits** : User events older than 2015 are not accepted. For auto-learning suggestions, the system uses user events from the past 180 days. Similarly, metrics for user events older than 180 days or generated more than 180 days ago are not exportable.

  * **Unique visitor IDs** : The total number of unique visitor IDs for each event type should be at least 100 to ensure enough data for quality results.




Most models perform best with at least three months of product page views, home page views, and `add-to-cart` events.

For the Frequently Bought Together model, one to two years of purchase history is recommended. This model specifically requires _one_ of the following:

  * On average, 10 occurrences per catalog item (with a one-year window of purchase-complete events). 

  * _Both_ 90 days of purchase-complete events in the last year _and_ 1,000 purchase-complete events in that same year.




One to two weeks of detail-page views can be sufficient to begin training **Others You May Like** and **Recommended for You** models.

## Tune a model

AI Commerce Search uses the input data you provide to your model to adjust hyperparameters for training.

Tuning takes 2-4 days, during which the model continues to work as usual. For tuning cost details, see [Pricing](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/pricing).

### Set a model's tuning frequency

We recommend you periodically tune your model. This keeps model training optimal as data changes and customer behavior differs throughout the year. In addition, some internal major model upgrades can only be applied after the model has been tuned.

When creating the model, you can set it to automatically tune every three months, or choose to only tune it manually. Regardless of the setting you choose, the model automatically tunes one time after creation.

You can change the tuning status setting at any time. Changing this setting doesn't affect running tuning processes.

To edit a model's tuning status setting:

###  Console 

  1. Go to the **Models** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Models page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/models/)

You can see the tuning status of every model under **Tuning status**.

  2. Click a model name to view its details page.

  3. Click **Edit** _edit_ next to **Tuning status**.

  4. From the drop-down list, select a setting:

     * **Every three months**. Automatically tunes when the last tune was 90 days ago.
     * **Manual tune only**. Tunes only when you manually tune.
  5. Click **Done** _done_ to save your setting.




###  curl 

Make a `Models.patch` request using the API. See the [`Models.patch`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/patch) API reference.

For details about all `Models` fields, see the [`Models` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models).
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d '{
      "name": "projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/models/MODEL_ID",
      "PeriodicTuningState": "NEW_TUNING_STATE_VALUE"
    }' \
    'https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/models/MODEL_ID?updateMask=PeriodicTuningState'

### Manually tune a model

Manual tune triggers a one-time tune of your model. You might manually tune your model when there is a significant change in your catalog (such as size increase or change in catalog hierarchy) or events (such as backfilling historical events or a change in data distribution after promoting certain groups of items).

To manually tune a model:

###  Console 

  1. Go to the **Models** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Models page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/models/)

  2. Click a model name to view its details page.

  3. Click **Manual Tune** in the button bar.

Tuning takes 2-4 days, during which the model continues to work as usual. 




###  curl 

Make a `Models.tune` request using the API. See the [`Models.tune`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/patch) API reference.
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    'https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/models/MODEL_ID:tune'

## Pause and resume training for a model

If your model is active (not paused), the model is retrained at least once a week, but no more often than once a day. For consistent retraining, make sure that you upload user event data no more than 24 hours after the event occurs.

You can pause your model to stop retraining. You might want to do this if you have imported bad data or to stay under the limit of 10 active models per project. If you have fewer than 10 active models, you can restart a paused model at any time.

For training cost details, see [Pricing](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/pricing).

You can start up to five model operations per minute. Limited model operations include creation, deletion, pause, and resume. 

To pause or restart a model:

###  Console 

  1. Go to the **Models** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Models page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/models/)

You can see the training status of every model under **Training status**.

  2. To pause an active model (**Training status** of **TRAINING**), click **Pause** _pause_.

  3. To start a paused model (**Training status** of **PAUSED**), click **Resume** _play_arrow_.




###  curl 

To pause an active model, make a `Models.pause` request using the API. See the [`Models.pause`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/delete) API reference.
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    'https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/models/MODEL_ID:pause'

To start a paused model, make a `Models.resume` request using the API.
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    'https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/models/MODEL_ID:resume'

## View model details

View a model's details in the console or using the `Models.get` API method.

To see the serving configs that are associated with a specific model, use this procedure. All other model details are available in the console and the API response.

###  Console 

  1. Go to the **Models** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Models page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/models/)

  2. The **Models** page lists all your models and their training and query statuses.

  3. Click a model name to view its **Details** page.




###  curl 

To get a single model's information, make a `Models.get` request using the API. See the [`Models.get`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/get) API reference.
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    'https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/models/MODEL_ID'

## List your models

View a list of your models in the console or using the `Models.list` API method.

###  Console 

  1. Go to the **Models** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Models page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/models/)

  2. The **Models** page lists all your models and their training and query statuses.




###  curl 

To list all models and their details inline, make a `Models.list` request using the API. See the [`Models.list`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/list) API reference.

Optionally, you can use the parameter `pageSize` to set a maximum number of results to return. If more results are available, the `list` response includes a page token. You can pass a page token in the `pageToken` parameter of a `list` request to retrieve the next page of results. This example uses both parameters.
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    'https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/models?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN'

## Delete a model

You can start up to five model operations per minute. Limited model operations include creation, deletion, pause, and resume. 

Delete a model in the console or using the `Models.delete` API method.

###  Console 

  1. Go to the **Models** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Models page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/models/)

  2. Click the name of the model you want to delete to open its details page.

  3. Click **Delete** _delete_ in the button bar.

  4. Reenter the model name and click **Confirm**.




###  curl 

Make a `Models.delete` request using the API. See the [`Models.delete`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models/delete) API reference.

For details about all `Models` fields, see the [`Models` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.models).
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    'https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/models/MODEL_ID'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
