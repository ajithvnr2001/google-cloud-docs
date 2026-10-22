---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs/
title: Create serving configs \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:22.240433+00:00
---

# Create serving configs  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Create serving configs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create serving configs. A serving configuration is a serving entity that associates a model or a set of controls that are used to generate your search or recommendation results. For more information about serving configs, see [About serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs).

## Before you begin

Recommendations and search serving configs have different requirements and options:

  * Recommendations serving configs require a model. If you plan to attach an existing model to a new serving config, get the ID of the model you plan to use (required when using the `ServingConfig.create` method).

If creating the serving config using the console, you can create a new model during the creation process instead of attaching an existing model.

You can switch models later, as long as it is of the same model type.

  * Search can use serving controls, but they are not required. If you plan to attach existing controls to a new serving config, get the IDs of the controls you plan to use.

If creating the serving config using the console, you can also create new controls during the creation process.

You can switch or add serving controls to your serving config after you create it.




## Create a serving config

You can create a serving config using:

  * The AI Commerce Search in Gemini Enterprise for Customer Experience console.
  * The `ServingConfig.create` API.



Up to 100 serving configs are allowed per catalog.

Search works with non-configured serving configs. Any `serving_config_id` can be placed as part of the search request, and this `default_search` will search the catalog with AI Commerce Search default search capability.

If you have existing placements, or create new placements, a serving config associated with each placement is automatically created. Creating a serving config does not create a corresponding placement. Deleting a serving config deletes its corresponding placement, and deleting a placement deletes its corresponding serving config.

### Create a serving config in the console

Add a new serving config on the [Serving Configs page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs/) in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

To create a new serving config:

  1. Go to the **Serving Configs** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Serving configs page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs/)

  2. Click _add_box_**Create serving config**.

###  Recommendations 

     1. Select **Recommendation** as the product the serving config will be used for.

     2. Provide a name for your serving config.

The name must be 1024 characters or less, and can contain only alphanumeric characters, underscores, hyphens, and spaces.

     3. Optional: If needed, update the ID.

The ID is generated from the name you provide, and must be unique across your project. It must be 50 characters or less, and cannot contain spaces.

     4. Choose or create a model you want this serving config to provide recommendations for.

[Learn more](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models) about creating new models.

     5. Select how much price reranking should affect recommendation results, if available for the model you selected.

Price reranking causes recommended products with a similar recommendation probability to be ordered by price, with the highest-priced items first. Relevance is still also used to order items, so enabling price reranking is not the same as sorting by price.

     6. Select whether to use rule-based or data-driven result diversification:

        * **Ruled-based:** Ruled-based result diversification affects whether results returned from a single prediction request are from different categories of your product catalog.

        * **Data-driven:** Data-driven result diversification uses machine learning to balance category diversity and relevance in your prediction results.

For more information, see [Result diversification](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#diversification).

     7. Select how much to diversify recommendation results.

     8. If you selected a Similar Items model for this serving config, select whether to enable category matching.

When category matching is enabled, the only product results returned are ones that share at least one category with the context product. Category matching can be used in combination with other filtering options, such as price, availability, and filter tags.

###  Search 

     1. On the **Create Serving Config** page, choose **Search** as the product the serving configuration will be used for.
     2. Provide a name for your serving configuration.  
  
The name must be 1024 characters or less, and can contain only alphanumeric characters, underscores, hyphens, and spaces.
     3. Optional: If needed, update the ID.  
  
The ID is generated from the name you provide, and must be unique across your project. It must be 50 characters or less, and cannot contain spaces.
     4. Click **Continue**.
     5. Choose whether to enable dynamic faceting for this serving configuration.
     6. Choose or create serving controls to optimize your searches with.  
  
For more information on controls, see [Creating and managing controls.](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-controls)

  3. Click **Create** to create the new configuration.

The new configuration appears in your [Serving Configs page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs/).

It might take a few minutes for the configuration to become available for use in search requests. It is immediately available for recommendations.

  4. Optional: On the Serving Configs page, click a serving config name and go to its **Evaluate** tab to preview the products that would be returned for this configuration.

Evaluation preview can help you to confirm that your configuration is performing as you expect.




### Create a serving config with `ServingConfig.create`

You can create a serving config with the `ServingConfig.create` API method. For API reference documentation for this method, see [`ServingConfig.create`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs/create).

Which fields you use depend on if you're creating a serving config for recommendations or search.

For more details about the `ServingConfig` fields, see the [`ServingConfigs` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.servingConfigs).

###  Recommendations 

Make a `ServingConfig.create` request with a serving config ID and an instance of `ServingConfig` contained in the request body.

  * `servingConfigId`: Required. Creates an ID for your `ServingConfig`. This value should be 4-63 characters. Valid characters are `/[a-z][0-9]-_/`.
  * `displayName`: Required. The human readable `ServingConfig` name displayed in the AI Commerce Search in Gemini Enterprise for Customer Experience console.
  * `modelID`: Required. The ID of the model to use at serving time.
  * `priceRerankingLevel`: Optional. Sets how much price reranking should affect recommendation results. Allowed values are `no-price-reranking` (default value if unset), `low-price-raranking`, `medium-price-reranking`, and `high-price-reranking`.
  * `diversityLevel`: Optional. Sets how much to diversify recommendations results. Allowed values are `no-diversity` (default), `low-diversity`, `medium-diversity`, `high-diversity`, and `auto-diversity`. If `diversityLevel` is not set, then diversity is disabled.
  * `diversityType`: Optional. Set to `RULE_BASED_DIVERSITY` to diversify recommendation results based on product category. Set to `DATA_DRIVEN_DIVERSITY` to diversify recommendations based on learning from product metadata to balances relevance and category diversity. If `diversityLevel` is set but `diversityType` is not set, then `diversityType` defaults to rule-based. For more information, see [result diversification](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#diversification).
  * `enableCategoryFilterLevel`: Optional. Sets whether to add additional category filters on the Similar Items model. Allowed values are `relaxed-category-match` (default value if unset) and `no-category-match`.
  * `solutionTypes`: Required. Set to `SOLUTION_TYPE_RECOMMENDATION` for recommendations serving configs.


    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": "DISPLAY_NAME",
                  "modelId": "MODEL_ID",
                  "priceRerankingLevel": "PRICE_RERANKING_LEVEL",
                  "diversityType": "DIVERSITY_TYPE",
                  "diversityLevel": "DIVERSITY_LEVEL",
                  "enableCategoryFilterLevel": "CATEGORY_FILTER_LEVEL",
                  "solutionTypes": [ "SOLUTION_TYPE_RECOMMENDATION" ]
                }' \
        "https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/servingConfigs?servingConfigId=SERVING_CONFIG_ID"
      

###  Search 

Make a `ServingConfig.create` request with a serving config ID and an instance of `ServingConfig` contained in the request body.

  * `servingConfigId`: Required. Creates an ID for your `ServingConfig`. This value should be 4-63 characters. Valid characters are `/[a-z][0-9]-_/`.
  * `displayName`: Required. The human readable `ServingConfig` name displayed in the AI Commerce Search in Gemini Enterprise for Customer Experience console.
  * `facetControlIds`: Optional. IDs of controls that have only `FacetSpec` set.
  * `dynamicFacetSpec.mode`: Optional. Mode of the `DynamicFacet` feature. Allowed values are `DISABLED` (default if unset) and `ENABLED`.
  * `boostControlIds`: Optional. IDs of boost serving controls.
  * `filterControlIds`: Optional. IDs of filter serving controls.
  * `redirectControlIds`: Optional. IDs of redirect serving controls.
  * `twowaySynonymsControlIds`: Optional. IDs of two-way synonym serving controls.
  * `onewaySynonymsControlIds`: Optional. IDs of one-way synonym serving controls.
  * `doNotAssociateControlIds`: Optional. IDs of do-not-associate serving controls.
  * `replacementControlIds`: Optional. IDs of replacement serving controls.
  * `ignoreControlIds`: Optional. IDs of ignore serving controls.
  * `solutionTypes`: Required. Set to `SOLUTION_TYPE_SEARCH` for search serving configs.


    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
                  "displayName": DISPLAY_NAME,
                  "facetControlIds": [
                    "FACET_CONTROL_ID_1",
                    "FACET_CONTROL_ID_2"
                  ],
                  "dynamicFacetSpec": {
                    "mode": "DYNAMIC_FACET_MODE"
                  },
                  "boostControlIds": [
                    "BOOST_CONTROL_ID_1",
                    "BOOST_CONTROL_ID_2"
                  ],
                  "filterControlIds": [
                    "FILTER_CONTROL_ID_1",
                    "FILTER_CONTROL_ID_2"
                  ],
                  "redirectControlIds": [
                    "REDIRECT_CONTROL_ID_1",
                    "REDIRECT_CONTROL_ID_2"
                  ],
                  "twowaySynonymsControlIds": [
                    "TWO_WAY_SYNONYM_CONTROL_ID_1",
                    "TWO_WAY_SYNONYM_CONTROL_ID_2"
                  ],
                  "onewaySynonymsControlIds": [
                    "ONE_WAY_SYNONYM_CONTROL_ID_1",
                    "ONE_WAY_SYNONYM_CONTROL_ID_2"
                  ],
                  "doNotAssociateControlIds": [
                    "DO_NOT_ASSOCIATE_CONTROL_ID_1",
                    "DO_NOT_ASSOCIATE_CONTROL_ID_2"
                  ],
                  "replacementControlIds": [
                    "REPLACEMENT_CONTROL_ID_1",
                    "REPLACEMENT_CONTROL_ID_2"
                  ],
                  "ignoreControlIds": [
                    "IGNORE_CONTROL_ID_1",
                    "IGNORE_CONTROL_ID_2"
                  ],
                  "solutionTypes": [ "SOLUTION_TYPE_SEARCH" ]
        }' \
        "https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/servingConfigs?servingConfigId=SERVING_CONFIG_ID"
      

## Next steps

  * [Request predictions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict) from your new placement.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
