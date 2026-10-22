---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials/
title: Interactive tutorials \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:42.700386+00:00
---

# Interactive tutorials  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Interactive tutorials Stay organized with collections  Save and categorize content based on your preferences. 

This page lists a set of interactive tutorials for AI Commerce Search. These tutorials include actions that can be run in the Google Cloud Shell Editor. With this tool you can write, build, test, run, and debug cloud native applications directly from your browser.

## Overview

Try different tutorials depending on what you'd like to learn:

  * If you're starting a project, try the [Import catalog information](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#import_catalog_information) tutorials. Here, you learn how to import products into the catalog so you can try out, for example, different search functionalities. Next, see the [Import historical user events](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#import) tutorials. AI Commerce Search uses user events to generate initial recommendations and search results. Then try the [Record real-time user events](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#record) tutorials. Real-time user events provide high quality and relevant results.

  * If you're interested in how search works in general, try the [Search tutorials](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#search_tutorials).

  * If you want to learn how to configure search with serving configs and controls, try the following tutorials:

    * [Filtering](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#filtering_tutorial)
    * [Ordering](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#ordering_tutorial)
    * [Query expansion](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#query_expansion_tutorial)
    * [Pagination](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#pagination_tutorial)
    * [Boosting](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#boosting_tutorial)
    * [Redirect control](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#redirect_control_tutorial)
  * If you need to update your catalog information, see the [Manage catalog information](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#manage_catalog_information) tutorials.

  * If you want to learn how to update inventory, see the [Update inventory for search](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#update_inventory_for) tutorials.

  * If you want to learn how to record, view, or remove real-time user events, see the [Record real-time user events](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials#record) tutorials.

  * If you plan to use recommendations, see the tutorials for importing and managing catalogs and user events.




## Import catalog information

These tutorials describe how to import your catalog information and keep it up to date.

### Import catalog data from BigQuery

This tutorial shows you how to use a BigQuery table to import large amounts of catalog data with no limits.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_import_products_big_query_table_select_language&show=ide&environment_deployment=ide)

* * *

### Import catalog data from Cloud Storage

This tutorial shows you how to import a large number of items to a catalog.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_import_products_gcs_select_language&show=ide&environment_deployment=ide)

* * *

### Import catalog data inline

This tutorial shows how to import products into a catalog inline.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_import_products_inline_source_select_language&show=ide&environment_deployment=ide)

* * *

## Manage catalog information

These tutorials describe how to manage your product information after you have imported a catalog. You can read, write, and delete products in your catalog.

Learn how to call the API with your language of choice.

### Create/Get/Update/Delete product tutorial

This tutorial shows you how to use API methods, which perform the following actions:

  * Create a product
  * Get a product
  * Update a product
  * Delete a product



To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_crud_select_language&show=ide&environment_deployment=ide)

* * *

### Create product tutorial

This tutorial shows you how to create a single product.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_create_product_select_language&show=ide&environment_deployment=ide)

* * *

### Get product tutorial

This tutorial shows you how to retrieve a product item.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_get_product_select_language&show=ide&environment_deployment=ide)

* * *

### Update product tutorial

This tutorial shows you how to update a product in a catalog.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_update_product_select_language&show=ide&environment_deployment=ide)

* * *

### Delete product tutorial

This tutorial shows you how to delete a product from a catalog.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_delete_product_select_language&show=ide&environment_deployment=ide)

* * *

## Import historical user events

These tutorials describe how to import user event data from past events in bulk. Models require user event data for training.

### Import events from Cloud Storage tutorial

This tutorial shows how to import user events from Cloud Storage.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_import_user_events_gcs_select_language&show=ide&environment_deployment=ide)

* * *

### Import events from BigQuery tutorial

This tutorial shows how to import user events from BigQuery.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_import_user_events_big_query_table_select_language&show=ide&environment_deployment=ide)

* * *

### Import events inline tutorial

This tutorial shows how to import user events data inline.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_import_user_events_inline_source_select_language&show=ide&environment_deployment=ide)

* * *

## Record real-time user events

These tutorials describe how to record, view or remove real-time user events. AI Commerce Search uses real-time user events to generate recommendations and search results. Recording as many types of user events as possible with valid product information increases the quality of your results.

### Write user events tutorial

This tutorial shows how to record user events using the [`userEvents.write`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/write) method.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_write_user_events_select_language&show=ide&environment_deployment=ide)

* * *

### Rejoin user events tutorial

This tutorial shows how to rejoin user events by making a `POST` request to the [`userEvents:rejoin`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/rejoin) endpoint.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_rejoin_user_events_select_language&show=ide&environment_deployment=ide)

* * *

### Remove user events tutorial

This tutorial shows how to purge user events.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_purge_user_events_select_language&show=ide&environment_deployment=ide)

* * *

## Search Tutorials

The `search()` method is used to search over the catalog according to the search query and other parameters, such as filter, facet, or order_by.

By default, the search response contains a reasonable number of results ordered by relevance.

### Querying tutorial

This tutorial shows you how to send a simple search query and analyze the response.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_querying_select_language&show=ide&environment_deployment=ide)

* * *

### Pagination tutorial

This tutorial shows how to control pagination in the search request. When a shopper looks for products in a shop, they can improve their navigation through search results. For example, they can limit the number of items in the search response by using the page size feature or jump to their preferred page by using the offset feature.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_pagination_select_language.neos.md&show=ide&environment_deployment=ide)

* * *

### Query expansion tutorial

This tutorial shows you how to enable the query expansion feature. When a shopper uses an ambiguous or a multi-word search phrase, they can get an empty response. After turning on query expansion, the request is analyzed and what's returned is the expanded list of products based on the parsed search query.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_query_expansion_select_language&show=ide&environment_deployment=ide)

* * *

### Filtering tutorial

This tutorial demonstrates the filtering feature. It lets you fine-tune search requests according to your or your customer's needs. You can filter by single or multiple fields, filter by text or numeric fields, or both. You can use an expression language to construct a predicate for each field or combine different expressions using logical operators. For example, a shopper looking for shoes can use filters to narrow their search to their preferred brand and color.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_filtering_select_language&show=ide&environment_deployment=ide)

* * *

### Ordering tutorial

This tutorial shows how to order items in a search response. When a shopper looks for a product on your site, you can show results ordered by multiple fields. For example, a shopper is searching for a dress with the best price and discount. Price and discount are multiple fields here. The shopper is shown dresses ordered by price, and for the dresses with the same price, ordered by discount.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_ordering_select_language&show=ide&environment_deployment=ide)

* * *

### Boosting tutorial

This tutorial shows some examples of product boosting in search results. With boosting, you can apply a boost to a product to prioritize or deprioritize it in the search results.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_boosting_select_language&show=ide&environment_deployment=ide)

* * *

### Redirect control tutorial

This tutorial shows you how to use the redirect control. The redirect control lets you specify a URL to which you can redirect users when they use a specific search query. For example, if a user requests "sustainable manufacturing products", you can redirect them to a page containing the environmental brands that you are working with.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_redirect_control_select_language&show=ide&environment_deployment=ide)

* * *

## Update inventory for search

While the `Product` create, read, update, and delete (CRUD) methods are used to broadly modify a `Product`'s attributes, there is a set of `Product` methods that can be used for updating inventory-specific fields with varying levels of granularity. The following `Product` fields are considered inventory fields:

  * `Product.price_info`
  * `Product.availability`
  * `Product.available_quantity`
  * `Product.fulfillment_info`



### Add fulfillment tutorial

This tutorial shows how to update product fulfillment information using the [`AddFulfillmentPlaces`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AddFulfillmentPlacesRequest) method. In this way, search can show updates where products are available and orders can be fulfilled. For example, a shopper is looking for blue jeans in a shop but they're out of stock. The moment the jeans are in stock again at this shop or any other shop, the shopper sees the updates and can proceed with their order.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_add_fulfillment_places_select_language&show=ide&environment_deployment=ide)

* * *

### Remove fulfillment tutorial

This tutorial shows how to update product fulfillment information using the [`RemoveFulfillmentPlaces`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.RemoveFulfillmentPlacesRequest) method. In this way, search can show updates where products aren't available and orders can't be fulfilled. For example, a shopper is looking for blue jeans in a shop. If the jeans become out of stock in this shop, the shopper sees this and can't proceed with their order.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_remove_fulfillment_places_select_language&show=ide&environment_deployment=ide)

* * *

### Set inventory tutorial

This tutorial shows how to push inventory updates using the [`SetInventory`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.SetInventoryRequest) method instead of updating the entire product.

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_set_inventory_select_language&show=ide&environment_deployment=ide)

* * *

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
