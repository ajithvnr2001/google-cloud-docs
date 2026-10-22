---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models/
title: About recommendation models \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:47.357844+00:00
---

# About recommendation models  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  About recommendation models Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the recommendation models with their default serving configs and optimization objectives, available customizations, and supported event types.

**Note:** Creating and configuring models is only available for recommendations.

## Introduction

When you sign up to use AI Commerce Search, you work with AI Commerce Search Support to determine the best recommendation models and customizations to use for your site. The models and customizations you use depend on your business needs, and where you plan to display the resulting recommendations.

When you request recommendations, you provide the serving config value to the `placement` resource. (See [About serving configurations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs) for details about using the `placement` resource for serving configs, and about support for placements, which were previously used to place models.) The serving config determines which model is used to return your recommendations. You can also [filter your results](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict#filters).

## Recommendation model types

These are the recommendation model types:

  * Others You May Like
  * Frequently Bought Together (shopping cart expansion)
  * Recommended for You
  * Buy it Again
  * On-sale
  * Recently Viewed
  * Page-Level Optimization
  * Similar Items



### Others You May Like

The Others You May Like recommendation predicts the next product that a user is most likely to engage or convert with. The prediction is based on the shopping and viewing history of the user and the candidate product's relevance to a current specified product.

**Default optimization objective** : click-through rate

**Default serving config** : N/A

**Available customizations** :

  * Change optimization objective to conversion rate or revenue per session.
  * Add [price reranking](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#price-reranking).
  * Add [Result diversification](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#diversification) (supported but not recommended).



**Supported pages for model deployment** :

  * Detail page. See [detail-page-view](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#detail-page-view) event.
  * Add-to-cart page. See [add-to-cart](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#add-to-cart) event.



### Frequently Bought Together (shopping cart expansion)

The Frequently Bought Together recommendation predicts items frequently bought together for a specific product within the same shopping session. If a list of products is being viewed, then it predicts items frequently bought with that product list.

This recommendation is useful when the user has indicated an intent to purchase a particular product (or list of products) already, and you are looking to recommend complements (as opposed to substitutes). This recommendation is commonly displayed on the `add-to-cart` page, or on the shopping cart or registry pages (for shopping cart expansion).

**Default optimization objective** : revenue per session

**Default serving config** : N/A

**Available customizations** :

  * Add [Result diversification](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#diversification) (supported but not recommended)
  * Choose the context product type

**Note:** Boost controls and diversity (rule-based or data-driven) are not compatible with each other. Only specify one of these settings at a time. 

**Supported pages for model deployment** :

  * Detail page. See [detail-page-view](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#detail-page-view) event.
  * Add-to-cart page. See [add-to-cart](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#add-to-cart) event.
  * Shopping cart page. See [shopping-cart-page-view](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#shopping-cart-page-view) event
  * Purchase-complete page. See [purchase-complete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#purchase-complete) event.



### Recommended for You

The Recommended for You recommendation predicts the next product that a user is most likely to engage with or purchase, based on the shopping or viewing history of that user and contextual information of requests, such as timestamps. This recommendation is typically used on the home page.

Recommended for You can also be useful on category pages. A category page is similar to a home page, except that you display only items from that category. You can achieve this using a standard Recommended for You model with filter tags. For example, you can add customized filter tags (corresponding to each category page) to the items in your catalog. When you send the prediction request, set the user event object as `category-page-view` and specify a specific category page's tag in the `filter` field. Only recommendation results matching the requested filter tag are returned. Diversity should be disabled in this use case, because diversity can conflict with category-based filter tags. 

**Default optimization objective** : click-through rate

**Default serving config** : N/A

**Available customizations** :

  * Change optimization objective to conversion rate or revenue per session.
  * Add [price reranking](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#price-reranking).
  * Add [Result diversification](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#diversification).



**Supported pages for model deployment** :

  * All



### Buy it Again

The Buy it Again model encourages purchasing items again based on previous recurring purchases. This personalized model predicts products that have been previously bought at least twice and that are typically bought regularly. The interval at which a product is suggested depends on the product and site visitor. Recommendations from this model can be used on any page type.

The following also apply to the Buy it Again model: \- Uses purchase-complete user events. \- Cannot be tuned. \- Only supports `visitor_id`, which, if it doesn't have personalized results, means the Buy it Again model suggests globally popular items. (This fallback behavior can't be controlled or disabled.)

Only create one Buy it Again model per project, because Buy it Again models are not customizable. Creating multiple Buy it Again models based on the same user events doesn't produce different recommendations and can incur unnecessary costs.

**Default optimization objective** : N/A

**Default serving config** : N/A

**Available customizations** : N/A

**Supported pages for model deployment** :

  * All



### On-sale

The On-sale model type is a personalized promotions-based model that can recommend on-sale products. You can use this model type to encourage users to purchase discounted items.

Typically used on the home page, add-to-cart page, shopping cart page, category page, and detail page.

**Default optimization objective** : Click-through rate

**Default serving config** : N/A

**Available customizations** :

  * Change optimization objective to conversion rate



**Supported pages for model deployment** :

  * Detail page. See [detail-page-view](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#detail-page-view) event.
  * Home page. See [home-page-view](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#home-page-view) event.
  * Add-to-cart page. See [add-to-cart](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#add-to-cart) event.
  * Shopping cart page. See [shopping-cart-page-view](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#shopping-cart-page-view) event.
  * Purchase-complete page. See [purchase-complete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#purchase-complete) event.
  * Category page. See [category-page-view](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#category-page-view) event.



### Recently Viewed

The Recently Viewed recommendation is not actually a recommendation. It provides the IDs of products the user or visitor has recently interacted with, with the most recent products first.

**Default optimization objective** : N/A

**Default serving config** : `recently_viewed_default`

**Available customizations** : N/A

**Supported pages for model deployment** :

  * All



### Page-Level Optimization

Page-Level Optimization extends recommendations from optimizing for a single recommendation panel at a time to optimizing for an entire page with multiple panels. The Page-Level Optimization model automatically selects the contents for each panel and determines the panel order on your page.

For example, home pages are typically structured with products organized into rows of related groups, such as categories, trending items, or recently viewed products. Using the Page-Level Optimization model on a home page can provide an end user with a personalized recommendation experience while automating the decision process for coordinating model combinations and layouts for that page.

To create a Page-Level Optimization model, you must first have existing recommendation serving configurations that have trained models. When creating a Page-Level Optimization model, you specify what type of page you'll use the model on, what restrictions you'll apply to limit serving similar serving configs, what business objective to optimize for (CTR or CVR), how many recommendation panels to display, and which serving configs to consider for each panel.

Just as with other models, to use the Page-Level Optimization model you make a prediction call using a serving config that contains the "Page-Level Optimization" model. Instead of recommendations, the prediction response contains a sorted list of serving config IDs representing the serving config to use for each panel. Then, make a new prediction call for each panel with the corresponding serving config ID that was returned from the Page-Level Optimization model. The prediction response for each panel contains the list of recommended items to display in that panel.

**Default optimization objective** : N/A

**Default serving config** : N/A

**Available customizations** : N/A

**Supported pages for model deployment** :

  * All



### Similar Items

This model predicts other products that share similar attributes to a specific context product. It is typically deployed on product detail pages or used as a fallback when a specific product is out of stock.

The Similar Items model requires only information from the product catalog; no user events are required.

Similar Items models can neither be tuned nor personalized. Therefore, Similar Items cannot be used to capture user behavior. Despite not being customizable, Similar Items models can be used to enable category matching in the [serving config](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#category-match) to ensure returned items share at least one category with the context product.

You should create only one Similar Items model per project. Because Similar Items models are not customizable, creating multiple Similar Items models based on the same user events does not produce different recommendations and can incur unnecessary costs.

**Default optimization objective** : Relevance

**Default serving config** : N/A

**Available customizations** : N/A

**Supported pages for model deployment** : Create recommendations models. See [Similar items](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models#import-reqs).

## When you enable this feature

  * Your description information should be explanatory for each product and contain unique information or words separate from the title.
  * this feature works best when there are at least 10 description words on average.
  * The percentage of events containing unknown item_ids should be under 10 percent. (The unjoined ratio can be [checked](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events#view-events). Read more about the [definition of unjoined ratio](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events#rejoin-event)).



## Optimization for business objectives

Machine learning models are created to optimize for a particular business objective, which determines how the model is built. Each model has a default optimization objective, but you can request a different optimization objective to support your business goals by contacting your support representative.

After you have trained a model, you cannot change the optimization objective. You must train a new model to use a different optimization objective.

AI Commerce Search supports the following optimization objectives.

### Click-through rate (CTR)

Optimizing for CTR emphasizes engagement; you should optimize for CTR when you want to maximize the likelihood that the user interacts with the recommendation.

CTR is the default optimization objective for the Others You May Like and Recommended for You recommendation model types.

### Revenue per session

The revenue per session optimization objective is available for "Others You May Like", "Recommended for You", and "Frequently Bought Together" recommendation model types. Although objective works differently for each model, the goal is the same, to increase revenue.

  * **For Others You May Like and Recommended for You.** The objective combines information from clicks, conversions, and item prices to help the model recommend items that have higher prices and a higher probability of being purchased.

  * **For Frequently Bought Together.** This objective optimizes for recommending items with a higher probability of being added to carts, benefiting revenue with by expanding cart sizes.




### Conversion rate (CVR)

Optimizing for conversion rate maximizes the likelihood that the user adds the recommended item to their cart; if you want to increase the number of items added to a cart per session, optimize for conversion rate.

## Advanced model configuration options

Depending on the model type, there are some other model configuration options you can use to change the behavior of your model.

### Tuning preference

Tuning keeps model training optimal as input data changes over time. Set your model to automatically tune every three months, or choose to only tune it manually. The model automatically tunes one time after creation. [Learn more](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-models).

For tuning cost details, see [Pricing](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/pricing).

## Available serving configs and models

Before you can request predictions from your model, you must create at least one serving config for it. For more information, see [Create serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs).

You can see your models listed on the [Models page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/models/). Click a model name to go to its details page, where you can see serving configs associated with that model.

## Context products

When generating a recommendation, models take into account the products that a user has previously interacted with in the context of the recommendation panel.

These contextual products are passed into the body of a `predict` request as part of a user event. For example, if there is a recommendation panel on a shopping cart page, any `shopping-cart-page-view` user event that triggers a `predict` request should include the products that are in the shopping cart at that time. These products are used as the context products for that recommendation.

When creating a Frequently Bought Together model, you specify whether that model will generate recommendations in the context of one or multiple items. Which option you choose depends on what type of page you plan to use the model.

  * **Multiple context products (default)** : The Frequently Bought Together model can use one or multiple products as context for its recommendations. This use case is typically for shopping cart pages that have a variety of contextual products that can inform the recommendation to be served on that page.
  * **Single context product** : The Frequently Bought Together model can use only one context product. This use case is typically for pages that have a single product that would be used as context for recommendations, such as add-to-cart pages and product detail pages.

Passing more than one product in a `predict` request from a single context product Frequently Bought Together model does not fail, although it is not recommended because it might not result in optimal recommendations.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
