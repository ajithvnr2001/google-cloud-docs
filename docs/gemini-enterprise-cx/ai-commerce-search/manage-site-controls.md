---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-site-controls/
title: Manage site-wide attribute controls \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:16.300169+00:00
---

# Manage site-wide attribute controls  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-site-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Manage site-wide attribute controls Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage site-wide attribute controls.

Site-wide controls apply to all search results or all recommendation results, depending on what type of site-wide attribute control you apply.

## About site-wide attribute controls

Side-wide attribute controls enable you to manage settings globally across all serving configurations.

Site-wide attribute controls are available in the AI Commerce Search in Gemini Enterprise for Customer Experience console for your catalog's product attributes.

Search uses the following attribute settings: 

  * **Indexable** : Search can filter and facet using this attribute. 
  * **Dynamic faceting** : Search can automatically use this attribute as a dynamic facet based on past user behavior such as facet clicks and views. To enable dynamic faceting for an attribute, _Indexable_ must be set to true for that attribute. 
  * **Searchable** : This attribute is searchable by search queries, which increases recall for that attribute. This control is applicable only for text attributes. 
  * **Retrievable** : If set to true, search returns this attribute in responses to search queries. If all attributes have Retrievable set to false, the search results contain only the product name or (for variants) the product name and color information. The REST field RetrievableFields is deprecated for products. Use the retrievable site-wide control instead. 



Recommendations uses the following attribute settings: 

  * **Filterable** (Public Preview): This attribute can be used in recommendations filter expressions. This control is applicable only for text attributes. 



You can enable or disable side-wide attribute controls for individual attributes.

Dynamic faceting is available as a site-wide attribute control. By default, dynamic faceting is enabled for all custom attributes.

In [catalog-level configuration mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#config-modes), site-wide attribute controls are available for indexable and searchable.

For details about attribute configurations and what their default and allowed settings are, see the topic [About product attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config).

## Modify site-wide attribute controls

Change a site-wide attribute control on the [Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs/) in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

**Note:** Setting site-wide attribute controls globally is available in the default [catalog-level configuration mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#config-modes). Previously, product-level configuration was the default mode. If you are still on product-level configuration mode and need to switch modes, contact AI Commerce Search support.

  1. Go to the **Controls** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. Go to the **Site-wide controls** tab.

This tab displays a table of all product attributes you can set site-wide attribute controls for.

  3. Click _edit_**Modify Controls**.

  4. Enable or disable a control.

     * **True** : Enable a control for that attribute. This overrides any product-level attributes configuration.
     * **False** : Disable a control for that attribute. This overrides any product-level attribute configuration.

Note that you can only set dynamic faceting to true for attributes that are also set to indexable.

  5. Click **Save Controls**.

Changes to attribute configuration settings for indexable and searchable take effect within 12 hours, or immediately on your next catalog ingestion. Dynamic faceting configuration changes take up to two days. You can test if your changes have been applied on the [**Evaluate** page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/), which will reflect your changes immediately.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
