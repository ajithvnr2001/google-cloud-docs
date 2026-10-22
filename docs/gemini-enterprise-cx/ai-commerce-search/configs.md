---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs/
title: About serving configs \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:29.550892+00:00
---

# About serving configs  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  About serving configs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes serving configs. A serving config is a serving entity that associates a model or a set of controls that are used to generate your recommendation or search results.

## Relationship with models and controls

When you [create a serving config](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs), you select a model (for recommendations) or controls (for search) to attach. Serving configs are invoked by your site when surfacing recommendations or search results. At serving time, the serving config's associated model or controls are referenced to determine what the recommendations or search results generate.

### Models

A recommendations serving config can have a single model associated with it. However, any model can be associated with multiple serving configurations, enabling you to deploy the same model on different pages using different serving configs.

### Serving controls

Search serving configs have a multi-to-multi relationship with serving controls. You can add multiple serving controls to a serving config, and a single serving control can be associated with multiple serving configs.

You can create serving controls and then add or swap them into a live search serving config.

## API resource and permissions

A serving config is passed into the API using the `placements` resource:

  * Recommendations uses the URL `projects/PROJECT_ID/locations/global/catalogs/default_catalog/placements/SERVING_CONFIG_ID:predict`.
  * Search uses the URL `projects/PROJECT_ID/locations/global/catalogs/default_catalog/placements/SERVING_CONFIG_ID:search`.



The permissions used on these resources are the `placements.search` and `placements.predict` permissions.

## Support for placements in AI Commerce Search

The [`placement`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search) identifies the serving config name and the set of models to use for the search.

Serving configurations are available as of Recommendations AI v2 and Retail Search v2alpha. 

The `servingConfig` resource is available in the API versions v2beta and v2alpha. You can use this resource to create, view, edit, and remove serving configurations. 

If you have existing placements, or create new placements, serving configurations associated with each placement are automatically created. Creating a serving configuration does not create a corresponding placement. 

Deleting a serving configuration deletes its corresponding placement, and deleting a placement deletes its corresponding serving configuration. 

Serving configurations allow you to edit diversity and price reranking options and have them take effect in near real-time. With placements, diversity and pricing settings can only be changed from the recommendation model that the placement points to. 

Placements are still supported, but using serving configurations instead is recommended. If a random `serving_config_id` is placed as part of the search request, search will default to essentially an empty or non-configured serving control, allowing AI Commerce Search to still work with default search capability. 

## Recommendations options for serving configs

The following options allow you to change the behavior of a recommendations serving config.

These options were previously available when creating models; they are now associated with serving configs instead.

### Price reranking

Price reranking causes recommended catalog items with a similar recommendation probability to be ordered by price, with the highest-priced items first. Price reranking is disabled by default.

Enabling price reranking helps balance conversion rates and average order values. Because relevance is also used to order the items returned, enabling price reranking is not the same as sorting by price.

This option can be edited after creating a serving config.

### Result diversification

If you want to ensure that results returned from a single prediction request are more diversified rather than looking similar, you can enable diversification. Generally, diversification reduces the likelihood that similar products are shown in a recommendation panel, at the risk of removing some good recommendations. Diversification settings can be edited after creating a serving configuration. It is disabled by default.

Two types of diversification are available: rule-based diversity and data-driven diversity.

**Note:** Boost controls and diversity (rule-based or data-driven) are not compatible with each other. Only specify one of these settings at a time. 

#### Rule-based diversity

Rule-based diversity relies on categories of your product catalog. Use rule-based diversity to recommend products from a variety of categories. Diversification is configured by level, with higher levels of diversification causing fewer items to be displayed per category. This diversification type works best if your catalog provides high-quality product categories.

Diversification level | Max items per category  
---|---  
None | Unlimited  
Low | 3  
Medium | 2  
High | 1  
Auto | Depends on catalog  
  
#### Data-driven diversity

Use data-driven diversity to produce recommendations results that balance relevance and diversity. Data-driven diversity learns from product catalog metadata, such as titles or categories. Instead of relying on the title or category words, data-driven diversity captures semantic similarity to produce better-performing diversification.

Diversification level | Max similar items  
---|---  
None | Unlimited  
Low | 3  
Medium | 2  
High | 1  
Auto | Depends on catalog  
  
### Category matching

If the serving config includes a Similar Items model for recommendations, you can enable category matching. When category matching is used, the only product results returned are those that share at least one category with the context product.

If your categories have deeply nested hierarchies, they are truncated using heuristics to improve the possibility of a match. For example, if the context product's categories are `a > b > c > d > e > f`, the returned results are those whose categories are `a > b > c`.

Category matching can be used in combination with other filtering options, such as price, availability, and filter tags. For example, if you use the filter tag `fall_Sale` and have category match enabled, the returned results are those that have both the required tag and a category match.

This option can be edited after creating a serving config. By default, category matching is disabled.

## Dynamic faceting search option for serving configs

You can turn on dynamic faceting when you create or edit a serving configuration.

When dynamic faceting is enabled for a serving config, search can automatically use attributes as dynamic facets in search results for this configuration, based on past user behavior such as facet clicks and views. Whether a given attribute can be used as a facet is by default defined by the product-level [attribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.attributes) configuration. Dynamic faceting settings in the API can be overwritten by site-wide attribute controls in the AI Commerce Search in Gemini Enterprise for Customer Experience console. See [Managing site-wide controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-site-controls).

Note that dynamic facets can be created based just on accurate product catalog data. However, for the feature to work optimally for your site, the facet models need to learn from activity on your site. For this, you need to set query, category and filter fields in your `search` [event](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents) uploads accurately.

## Next steps

  * [Request predictions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict) from your new placement.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
