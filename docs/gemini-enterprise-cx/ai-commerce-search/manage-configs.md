---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-configs/
title: Manage serving configs \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:03.303360+00:00
---

# Manage serving configs  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Manage serving configs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete, edit, and list serving configs, as well as review statistics about each configuration.

For help with creating a new serving config, see [Create serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs).

It is not necessary to configure a serving config for search to work. Any `serving_config_id` can be placed as part of the search request, in which case, it defaults to an empty or non-configured serving control. The catalog is then searched with AI Commerce Search default search capability.

If you have existing placements, or create new placements, AI Commerce Search automatically creates a serving config associated with each placement. Creating a serving config does not create a corresponding placement. Deleting a serving config deletes its corresponding placement, and deleting a placement deletes its corresponding serving config.

## Edit serving configs

You can edit serving configs using the AI Commerce Search in Gemini Enterprise for Customer Experience console or the API.

**Note:** If you are making significant changes to a a serving config that contains a Page-Level Optimization model, the Page-Level Optimization model might return suboptimal results while it is retraining. Because it can take a long time to retrain the Page-Level Optimization model, consider recreating the Page-Level Optimization model and its associated serving config.

### Edit serving configs in the console

You can see and edit the controls for each serving config on the [Serving Configs page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs/). Click a serving config to see its **Details** page, which lists all serving and site-wide controls for that configuration.

On this page, you can edit controls, create new controls, or apply existing controls to the configuration.

It takes a few minutes for newly created or updated serving configs to be ready to serve live traffic. You can test changes right away on the [**Evaluate** page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/).

### Edit serving configs inline

You can update serving config fields, add serving controls, and remove serving controls inline using API methods.

#### Patch serving configs inline

To update fields in a serving config, use `ServingConfig.patch` and include an instance of `ServingConfig` in the request body. Specify the fields to update with the `updateMask` parameter, or leave it unset to update all supported fields.

For more about this method, see the [`ServingConfig.patch` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/patch).
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d '{
          "name": "projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/servingConfigs/SERVING_CONFIG_ID",
          "FIELD_NAME_1": "NEW_FIELD_VALUE_1"
          "FIELD_NAME_2": "NEW_FIELD_VALUE_2"
        }' \
    'https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/servingConfigs/SERVING_CONFIG_ID?updateMask=FIELD_NAME_1,FIELD_NAME_2'

#### Add controls to serving configs inline

To add a control to a serving config, use `ServingConfig.addControl`. The control is added in the last position of the list of controls it belongs to. For example, a `facetSpec` control is applied in the last position of `servingConfig.facetSpecIds`.

For more about this method, see the [`ServingConfig.addControl` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/addControl).
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d '{
          "controlID": "CONTROL_ID"
        }' \
    'https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/servingConfigs/SERVING_CONFIG_ID:addControl'

#### Remove controls from serving configs inline

To remove a control from a serving config, use `ServingConfig.removeControl`.

For more about this method, see the [`ServingConfig.removeControl` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/removeControl).
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d '{
          "controlID": "CONTROL_ID"
        }' \
    'https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/servingConfigs/SERVING_CONFIG_ID:removeControl'

## View serving configs

You can view serving configs using the AI Commerce Search in Gemini Enterprise for Customer Experience console or the API.

### View serving configs in the console

You can see all of your serving configs on the [Serving Configs page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs/).

### View serving configs inline

To see a single serving config inline, use `ServingConfig.get`.

For more about this method, see the [`ServingConfig.get` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/get).
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    'https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/servingConfigs/SERVING_CONFIG_ID'

To list all serving configs inline, use `ServingConfig.list`.

Optionally, you can use the parameter `pageSize` to set a maximum number of results to return. If more results are available, the `list` response includes a page token. You can pass a page token in the `pageToken` parameter of a `list` request to retrieve the next page of results.

For more about this method, see the [`ServingConfig.list` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/list).
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    'https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/servingConfigs?pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN'

## Delete a serving config

You can delete serving configs using the AI Commerce Search in Gemini Enterprise for Customer Experience console or the API.

**Note:** If you delete a serving config that is being used by a Page-Level Optimization model, also delete and re-create the Page-Level Optimization model. Otherwise the Page-Level Optimization model will return the deleted serving config.

### Delete serving configs in the console

To delete a serving config in the console:

  1. Go to the **Serving Configs** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Serving configs page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs/)

  2. Click the serving config you want to delete to open its details page.

  3. Click _delete_**Delete** in the button bar at the top of the page.

  4. If the serving config is considered active, you must retype its ID and click **Confirm** to complete the deletion.




### Delete a serving config inline

To delete a single serving config inline, use `ServingConfig.delete`.

For more about this method, see the [`ServingConfig.delete` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/delete).
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    'https://retail.googleapis.com/v2beta/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/servingConfigs/SERVING_CONFIG_ID'

## Reviewing serving config statistics

You can see details for each serving config on the [Serving Configs page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs/). For any configuration in the table, click **View analytics** to see its statistics.

**Click-through-rate** shows the clicks per search for the serving config. **Conversion rate** indicates the purchases per search for the configuration.

**Note:** The time periods for statistics are in the Pacific time zone. For example, daily statistics represent the data from yesterday at midnight Pacific time to today at midnight Pacific time.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
