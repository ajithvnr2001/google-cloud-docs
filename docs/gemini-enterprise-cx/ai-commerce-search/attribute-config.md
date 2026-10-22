---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config/
title: About product attributes \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:44.489681+00:00
---

# About product attributes  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  About product attributes Stay organized with collections  Save and categorize content based on your preferences. 

AI Commerce Search can use product attributes for indexing, dynamic faceting, searchability, filtering, and model quality. This page discusses setting product attribute configurations and how they are treated depending on the method and configuration you use.

## Attribute types

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/pants-attributes.png)

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/pants-attributes.png)

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/pants-attribute-values.png)

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/pants-attribute-values.png)

Product attributes can have different default settings and allowed options depending on their type.

  * **System attributes** : Predefined system attributes are existing `Product` fields that provide more information about the product. These include product attributes like brand, availability, color, and size. For all available system attributes for products, see the [`Product` reference documentation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product).

  * **Custom attributes** : Custom attributes are extra attributes that you define using the `Product.attributes` field. For example, this could include store names, vendors, or style. For examples and limits for custom attributes, see the [`Product.attributes` reference documentation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.attributes).

Some examples of top 20 custom attributes are:

    * Product line this product belongs to
    * Volume of in-store sales for this product
    * Occasion for clothing
    * Deals and coupons applicable to this product
    * Site-wide product popularity
**Note:** The top 20 selected custom attributes change monthly. The selected attributes appear on the [Controls](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/) page of the AI Commerce Search in Gemini Enterprise for Customer Experience console. Access it by clicking the **Attribute controls** tab on the **Controls** page.
  * **Inventory-level attributes** : System or custom attributes that provide store-level information about the product. You might use inventory-level attributes for products whose properties vary significantly between stores and regions, such as grocery items, or for products that have store-specific promotions.

`inventories.price` and `inventories.originalPrice` are numeric system attributes predefined by AI Commerce Search. You can create custom inventory-level attributes, which can be textual or numeric. Inventory-level attributes are indexable by default. Setting searchable and dynamic faceting is not supported for inventory-level attributes.


**Note:** Providing values for predefined system attributes in [`Product`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products) such as brand, color, and size is highly encouraged. You can also include custom attributes that you define with [`Product.attributes`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.attributes).

## Available attribute settings

Attribute configuration settings impact search and recommendations behavior across your site.

Configuration | Description | System attributes | Custom attributes | Inventory-level attributes  
---|---|---|---|---  
Searchability | This attribute is searchable by search queries, which increases recall for that attribute (text attributes only). | Always on (text only) | Disabled by default (Can be enabled; text only.) | Not supported  
Indexability | Search can filter and facet using this attribute. | Always on | Enabled by default (Can be disabled.) | System: always on  
Custom: default on (Can be disabled.)  
Dynamic faceting | Search can automatically use this attribute as a dynamic facet, based on past user behavior such as facet clicks and views (text attributes only). | Enabled by default (if `indexability = True`) (Can be disabled.) | Enabled by default (if `indexability = True`) (Can be disabled.) | Not supported  
Filterable  
[(Preview)](https://docs.cloud.google.com/guides/components/launch-stages#features) | This attribute can be used in Recommendations AI filter expressions. This control is applicable only for text attributes. | Disabled by default (Can enabled for text; except `FulfillmentInfo` and `Title`.) | Disabled by default (Can be enabled for text.) | Supported only for `availability=IN_STOCK`  
Exact match | This property only applies to textual custom attributes. To enable exact-searchable, requires indexable set to enabled. | Not supported | Disabled by default (Can be enabled.) | Not supported  
  
Search uses the following attribute settings: 

  * **Indexable** : Search can filter and facet using this attribute. 
  * **Dynamic faceting** : Search can automatically use this attribute as a dynamic facet based on past user behavior such as facet clicks and views. To enable dynamic faceting for an attribute, _Indexable_ must be set to true for that attribute. 
  * **Searchable** : This attribute is searchable by search queries, which increases recall for that attribute. This control is applicable only for text attributes. 
  * **Retrievable** : If set to true, search returns this attribute in responses to search queries. If all attributes have Retrievable set to false, the search results contain only the product name or (for variants) the product name and color information. The REST field RetrievableFields is deprecated for products. Use the retrievable site-wide control instead. 



Recommendations uses the following attribute settings: 

  * **Filterable** (Public Preview): This attribute can be used in recommendations filter expressions. This control is applicable only for text attributes. 



### Indexable

If an attribute is set to indexable, search can filter and facet using the attribute.

  * **System attributes** : Indexability is always enabled for predefined system attributes. This setting can't be disabled for system attributes.
  * **Custom attributes** : Enabled by default. You can disable indexability for any custom attribute. If you plan to make a custom attributes indexable, it must follow the regular expression pattern `[a-zA-Z0-9][a-zA-Z0-9_]*`. For example, `key0LikeThis` or `KEY_1_LIKE_THIS`.
  * **Inventory-level attributes** : Always enabled for system inventory-level attributes; this setting can't be changed. Enabled by default for custom inventory-level attributes; this setting can be turned off.
  * **Dependencies** : N/A



Your index configuration changes go into effect immediately after you import catalog data. Otherwise it can take up to 12 hours or more for your changes to take effect. You can test if your changes have been applied on the [**Evaluate**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page.

### Dynamic faceting

When dynamic faceting is enabled for an attribute, search can use the attribute as a dynamic facet. Dynamic facets can be automatically added to a search based on past user behavior such as facet clicks and views.

  * **System attributes** : Enabled by default if indexability is set to true. You can disable dynamic faceting for any system attribute.
  * **Custom attributes** : Enabled by default if indexability is set to true. You can disable dynamic faceting for any custom attribute.
  * **Inventory-level attributes** : Not supported.
  * **Dependencies** : To enable dynamic faceting for an attribute, you must first enable indexability for that attribute.



Setting dynamic faceting for an attribute is always global. The dynamic faceting configuration you apply to that attribute is used by products across the catalog that use that attribute.

Dynamic faceting configuration changes take up to two days. You can test if your changes have been applied on the [**Evaluate**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page.

For numerical custom attributes, buckets need to be specified in the request. Numerical values are not bucketed automatically.

### Searchable

If an attribute is set to searchable, recall for that attribute in search queries is improved.

Only textual attributes values can have searchability enabled. It is not applicable to numerical attributes.

  * **System attributes** : Predefined textual system attributes for `Product` have their searchability settings configured by AI Commerce Search. These setting can't be changed.
  * **Custom attributes** : Disabled by default. You can enable this configuration for any textual custom attribute.
  * **Inventory-level attributes** : Not supported.
  * **Dependencies** : N/A
  * **Exact-searchable** : Targeted search returns for search queries that match any given product in your catalog. This option works well for serial numbers. See more information about the [exact-searchable option](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#exactsearchableoption).



Although products with a searchable attribute are more likely to appear in search results for that attribute, they are not guaranteed to appear.

### Recommendations filtering

**Preview:** This feature is in public preview.

While there is a limit of 10 filterable attributes that can be aggregated from variants into primary products for recommendations, if an attribute has recommendations filtering turned on, it can be used in recommendations filter expressions to filter products in predictions.

  * **System attributes** : Off by default. You can turn on this setting for any predefined system textual attributes for `Product`, except for `FulfillmentInfo` and `title`. Not supported for numeric attributes.
  * **Custom attributes** : Off by default. You can turn on this setting for any custom textual attributes for `Product`. Not supported for numeric attributes.
  * **Inventory-level attributes** : Supported only for the `availability` value `IN_STOCK`.
  * **Dependencies** : N/A



### Exact-searchable option

You can give a certain value for specific string queries to the `exact-searchable` option, a catalog attribute field. If a query matches any product in your catalog where the value for that field is the string given in the query, it returns exactly that product in the search query. This option works well for serial numbers, where customers expect a targeted search experience.

Usually for custom attributes, the [`ExactSearchableOption`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#exactsearchableoption) field is useful for product attributes with an exact value (like `ModelId` or `ManufacturerId`). Attributes like `product_id` are primary index fields—exact-searchable by default. The `item_id` field is always on for exact match and can't be disabled.

  * To avoid returning unrelated items in searches, never set the searchable option to a generic value such as `battery`.
  * To avoid under-serving search queries, don't set special fields like `tag` — which could have as one of its string values "iphone" — to exact-searchable. Doing so could cause those queries to limit results for all iphones in the product catalog.



For more information, see [About product attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config).

### Attribute configuration best practices

These best practices are important for understanding how to index your custom attributes properly, keeping in mind certain language parsing mechanisms that could affect their searchability.

  * **Handling alphanumerics (part numbers or SKUs)** : Because the default linguistic analysis optimizes for natural language, it may strip special characters like hyphens (`-`) from part numbers (such as converting `part-123` to `part` and `123`). To make these searchable, you must use the `exact-searchable` attribute flag.
  * **The n-gram workaround** : For highly complex model numbers containing special characters, best practice dictates breaking the string into n-grams in your own data pipeline prior to ingestion, and storing the original string in a custom attribute marked as `exact searchable: true`. This forces rigid matching against your n-gram fragments.
  * **Custom attribute key restrictions** : Custom attribute keys can't contain hyphens or special characters. To be indexable, the key must strictly match the regular expression pattern `[a-zA-Z0-9][a-zA-Z0-9_]*`. For more information, refer to the [About product attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config) page.
  * **UTF-8 requirement** : All string attributes and values must be valid UTF-8 encoded strings.



## Attribute behavior

When structuring your product catalog using primary and variant product designations, know how product attributes are handled for filtering. Their behavior depends on whether you're using search or recommendations and on how you configure your catalog taxonomy. 

To ensure predictable and accurate filtering behavior, maintain consistency and completeness in your filterable attribute definitions across primary and variant products. This approach aids in precise filtering, which improves product discovery and search relevance.

### Primary-variant behavior in search versus recommendations

While only primary items are returned in search and recommendation results, AI Commerce Search optimizes search and recommendation quality.

  * For search models, variant attributes are used for the primary product in the search index. Search results display diverse options for the primary product based on its variants' attributes.

  * For recommendation models, product details and attributes are not inherited from primary to variant. For optimal recommendation quality, it's crucial that primary and variant products have complete and accurate details for key attributes such as `product.categories`, `product.title`, `product.attributes`, and `product.prices`.




### Handle attributes during indexing and filtering

If the same attribute is defined in **Primary** and **Variant** , the attribute in the variant is part of filtering. For example, say an attribute is defined for a primary product and its variants (color or size). Variant attribute values are mainly for filtering, during which the system checks if any of the primary's variants match the attribute value. Take product availability: A primary product can be marked `out-of-stock`, but if at least one of its variants is `in-stock`, the primary is available for search results if an `in-stock` filter is applied.

  * Variant attributes take precedence for filtering. If an attribute is defined on a primary product and its variants, the attribute from the variant is used in filtering. For example, if a primary product has a placeholder color, but its variants have actual colors, the variant's color should be populated and is used for filtering.

  * For inventory-related attributes like availability, if a primary product has variants, the primary product's availability should be set to `OUT_OF_STOCK`, while the true availability (such as `IN_STOCK`) should be set at the variant level. This way, the primary product is considered in stock as long as at least one variant is in stock. If so, filters such as `availability: ANY("IN_STOCK")` correctly return the primary product.

  * When a filter expression is used, the prediction response will return primary products that have at least one primary or variant product matching the filter's attribute value.




#### Optional attributes for filtering

Keep the `categories` field clean and optimized for taxonomy. If more filtering is needed, implement it based on broad categories using separate custom attributes, not in the `categories` field. This also avoids negatively impacting autocompletion training for category suggestions.

For example, say you typically set categories like `[lvl1, lvl1>lvl2, lvl1>lvl2>lvl3]` for filtering. Autocomplete counts the most frequent categories for a given query, so you end up with `lvl1` and `lvl2` (all your products) as suggested categories.

### Attribute behavior best practices

If your catalog consists of primary and variant products _and_ the same attribute is defined in both, the attribute in variant will be considered during filtering.

  * **Populate attributes accurately** : Ensure that both primary and variant products have complete and accurate details for their attributes, especially those used for filtering, to maximize effectiveness.

  * **Use built-in fields** : Do not rely solely on custom attributes. Map your product information to the built-in `Product` fields (`brands`, `colors`, `sizes`, and the [required fields](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#required-fields)). Built-in fields have a greater impact on searchability, indexability, and relevance optimizations. Custom attributes (`Product.attributes`) are for product data that doesn't fit into predefined system attributes.

  * **Set site-wide retrievable fields control** : The API supports `variantRollupKeys` for variants, allowing you to retrieve details in search responses.

**Caution:** If you're using search, [`Product.retrievableFields`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.retrievable_fields), where attributes were included with a product in the search response, is deprecated. Use the retrievable site-wide control.
  * **Consistent catalog language** : The product catalog should be in one language only, and search queries should be sent in the same language. Having multiple languages in the catalog can degrade model performance. Not setting the language code can affect features like spell correction.

  * **Price information** : Accurately populate price information for both primary and variant products to ensure accurate recommendations and filtering. If a product lacks product-level pricing and relies solely on local inventory pricing, fill the primary product's pricing with the median from inventory-level pricing.




## Configuration modes

The configuration mode determines how attribute configurations are treated and which attribute configurations you can set.

  * **Catalog-level configuration mode (default)** : In this mode, attribute configurations on the catalog level on the catalog level are used as the source of truth.
  * **Product-level configuration mode (deprecated)** : In this mode, attribute configurations on the product-level are used as the source of truth.



Previously, product-level configuration was the default mode. If you are still on product-level configuration mode and need to switch to catalog-level configuration mode, contact Support. Search doesn't support returning to product-level configuration mode after you have switched.

To check the configuration mode, go to the AI Commerce Search in Gemini Enterprise for Customer Experience console [**Controls** page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/). If the **Indexable** option is available as a column on the **Site-wide controls** tab, then the configuration model is catalog level. If the **Indexable** column is not available on the **Site-wide controls** tab, then the configuration model is product-level.

## Configuration methods

You can set attribute configurations in the following ways:

  * **The AI Commerce Search in Gemini Enterprise for Customer Experience console** : Set attribute configurations on the catalog level using the AI Commerce Search in Gemini Enterprise for Customer Experience console. This configures attributes globally across all products. Which of these settings are available in the console depends on the configuration mode. See the next section for more details on how to configure attributes in the console.

  * **The`AttributeConfig` API method**: Set attribute configurations on the catalog level using the API. This configures attributes across all products.

  * **The`Product` API method (deprecated)**: Set custom attributes on the product-level using the `Product` API method. Setting attributes with this method is not available to new users and is not recommended.




### Configure attributes in the console

You can globally set attribute options across all products from the AI Commerce Search in Gemini Enterprise for Customer Experience console [**Controls** page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/), on the **Site-wide controls** tab. For more details on how to set this in the console, see [Manage site-wide attribute controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-site-controls).

To use this feature the configuration mode must be catalog level.

Changes to attribute configuration settings for indexable and searchable take effect immediately upon catalog ingestion. Otherwise, it can take up to 12 hours or more for changes to take effect. You can test if your changes have been applied on the [**Evaluate**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/evaluate/) page.

### Configure attributes with `AttributesConfig`

The `AttributesConfig` API resource lets you manage attribute configurations on the catalog level.

The following fields set attribute options at the catalog level:

  * [**`CatalogAttribute.indexableOption`**](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute.FIELDS.indexable_option): Sets the indexable option for an attribute.
  * [**`CatalogAttribute.dynamicFacetableOption`**](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute.FIELDS.dynamic_facetable_option): Sets the dynamic faceting option for an attribute.
  * [**`CatalogAttribute.searchableOption`**](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute.FIELDS.searchable_option): Sets the searchable option for an attribute.
  * [**`CatalogAttribute.recommendationsFilteringOption`**](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute.FIELDS.recommendations_filtering_option) (Public Preview): Sets the recommendations filtering option for an attribute.



To retrieve all attribute configurations, use the [`GetAttributesConfig`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/getAttributesConfig) method.

#### Update multiple attributes

Use the [`updateAttributesConfig`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/updateAttributesConfig) method to update multiple attributes at the catalog level.

The catalog attributes you include in the request are updated in the catalog, or inserted if they don't exist. If there is no value for a catalog attribute field, it is assigned a default value.

The maximum number of catalog attributes allowed in a request is 1000.

#### Update an individual attribute

The following [methods](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#methods) are used to update individual catalog attributes:

  * **`AddCatalogAttribute`** : Adds an individual attribute configuration to a catalog attribute.

See the API reference documentation for [`AddCatalogAttribute`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#catalogattribute).

  * **`ReplaceCatalogAttribute`** : Modifies an individual attribute configuration. This replaces the specified `CatalogAttribute` in the `AttributesConfig` by updating the catalog attribute with the same `CatalogAttribute.key`.

See the API reference documentation for [`ReplaceCatalogAttribute`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig/replaceCatalogAttribute).

  * **`RemoveCatalogAttribute`** : Removes an individual attribute configuration from `AttributesConfig`.

Only `CatalogAttributes` that are not in use by products can be deleted. If a `CatalogAttribute` is in use, `RemoveCatalogAttribute` doesn't delete it, but resets its configuration properties to default values. `CatalogAttribute.inUse` is set to `True` if the attribute is in use by any products.

See the API reference documentation for [`RemoveCatalogAttribute`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig/removeCatalogAttribute).


**Deprecated**

### Configure attributes with the `Product` method

Setting attributes with this method is not available to new users and is not recommended.

The following fields set indexable and searchable settings for a specific product using the `Product` API method:

  * [`Product.attributes.indexable`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.inlinedField_1).
  * [`Product.attributes.searchable`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.inlinedField_2). Only available for custom attributes.



## Best practices for naming and structuring custom attributes

When extending your product data beyond the predefined schema, how you name and format your custom attributes directly impacts AI Commerce Search's ability to index, retrieve, and facet your products.

Follow these best practices to ensure optimal search performance and avoid validation errors:

  1. **Prioritize native system attributes first**. Before creating a custom attribute, verify whether a default system attribute (such as `brands`, `colorInfo`, `sizes`, or `materials`) already exists for your data. The backend AI models understand default fields much better than custom attributes, and heavily factor them into relevance and recall optimizations.

     * **Example** : Do not pass brand information as `Product.attributes.brand`. Instead, map it directly to the default `Product.brands` field. Save custom attributes for uniquely specific data, such as `Product.attributes.sleeve_length`.
  2. **Follow strict naming conventions for indexability**. If you intend to use a custom attribute for filtering, faceting, or boosting, it must be marked as `Indexable`. To be indexable, your custom attribute key must adhere to the regular expression pattern `[a-zA-Z0-9][a-zA-Z0-9_]*`.

     * **Valid naming** : `sleeve_length` or `KEY_1_LIKE_THIS`.
     * **Invalid naming** : `sleeve-length` (hyphens are not allowed and will prevent indexing).
     * **Limits** : The attribute key must be a UTF-8 encoded string with a maximum length of 128 characters. A single product can have a maximum of 200 custom attributes.
  3. **Define clear value types (text or numbers)**. AI Commerce Search strictly requires that custom attribute values be defined as either textual (`text`) or numerical (`numbers`). You must set exactly one of these types for a given key; attempting to populate both `text` and `numbers` for the same attribute will return an `INVALID_ARGUMENT` error.

     * **Textual attributes** : Allowed up to 400 values per attribute. Empty strings (`""`) are not permitted. Each value must be a non-empty UTF-8 string with a maximum length of 256 characters.
     * **Numerical attributes** : Allowed up to 400 values per attribute.
     * **Faceting consideration:** If you want to use a numerical attribute as a `dynamicFacet`, you must cast the numerical data type to a `Text` string in your data pipeline before ingestion (such as passing `10.99` as `"10.99"`). Otherwise, numerical attributes can only be used as static facets where you must manually explicitly define interval buckets in the search request.
  4. **Use exact matches strategically.** The exact-searchable configuration is designed for highly specific, alphanumeric strings that lack linguistic meaning, such as `model_name` (such as `"WA2300AH3000"`) or `part_number`.

     * **Example** : Do _not_ apply exact match to custom attributes containing common English nouns or popular brands. Doing so restricts the search results when those common words appear in a search query, resulting in low product recall and negatively affecting click-through rates (CTR).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
