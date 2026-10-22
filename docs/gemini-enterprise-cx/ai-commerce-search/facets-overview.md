---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/facets-overview/
title: Facets for search \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:26.987017+00:00
---

# Facets for search  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/facets-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Facets for search Stay organized with collections  Save and categorize content based on your preferences. 

This page introduces some of the facet features and how to use them.

## Definitions related to facets

This section provides some basic definitions and explanations for some terms related to facets:

  * **Facets** : The facet specifications to perform faceted search. They help users find what they want by filtering the results. For example, if a user searches for `shoes`, some facets that could be returned are: `price`, `attributes.department`, `attributes.colors`, and `attributes.size`.

  * **System attributes** : Predefined [system attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#attribute-types) are existing product fields that provide more information about the product. These include a few predefined product attributes like `brand`, `availability`, `color`, and `size`.

  * **Custom attributes** : [Custom attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#attribute-types) are extra attributes that you define using the Product.attributes field. For example, this could include `style`, `color` or `department`.

  * **Facet key** : This is the name of a facet. For example, it could be `attributes.department` or `sizes`. The facet keys correspond to the attribute names. For example, the (product) system attribute name `sizes` corresponds to the facet key `sizes`. Similarly, the (product) custom attribute name `department` corresponds to the facet key `attributes.department` (for custom attributes, the prefix `attributes.` is added to the custom attribute name to obtain the facet key). The terms attribute name, facet key, and facet name are interchangeable.

  * **Facet value** : For textual keys, this is one of the textual values of a facet. By example, the textual facet key `brands` could have such textual values as `Asics` and `Nike`. For numerical keys, a facet value is an interval. By example, the numerical facet key price could have an interval of the form [20, 30).

  * **Type of an attribute or facet** : They can be either textual or numerical.

  * **Pinned facets** : This is a facet that you pass in the request using the `FacetSpec` with the option [`enableDynamicPosition`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec)`=false`. The facets should appear in their original order before all the dynamic facets in the response.

  * **Dynamic facets** : These are facets that search ranks on its side. They are either passed in the request with the option [`enableDynamicPosition`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec)`=true` or fetched according to the search models. They are then ranked by the same trained models with the most relevant ones at the top.

  * **Facetable, dynamic faceting, or tilable** : When an attribute is enabled for [dynamic faceting](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#dynamic-faceting), search can automatically use this attribute as a dynamic facet based on past user behavior such as facet clicks and views. To enable dynamic faceting for an attribute, you must also enable [indexing](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#indexable) for that attribute.

  * **Filter** : The [filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec) syntax consists of an expression language for constructing a predicate from one or more fields of the products being filtered. For example, if a user engages the facet values `Asics` of the facet key `attributes.brands`, then part of the filter could be `(attributes.brands:ANY(\"Asics",\"Nike\"))`. Filter expression is case-sensitive. See more details about the filter in this [user guide](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order#filter).




![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/shoes-facet-keys.png)

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/shoes-facet-keys.png)

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/shoes-facet-values-returned.png)

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/shoes-facet-values-returned.png)

## About dynamic facets and tiles

When dynamic faceting is enabled for a [serving config](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#dynamic), search can automatically use attributes as dynamic facets and tiles in search results for this configuration, based on past user behavior such as facet clicks and views. Dynamic facets are either passed in the request with the option [`enableDynamicPosition`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec)`=true` or fetched according to the search models. They are then ranked by the same models with the most relevant ones at the top.

By default, most facet keys are facetable. Dynamic faceting settings in the API can be overwritten for some specific facet keys of your choice by site-wide attribute controls in the AI Commerce Search in Gemini Enterprise for Customer Experience console. In other words, if you want some facet keys to be non-facetable, you need to disable [dynamic faceting](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#dynamic-faceting) for each of these keys in the `Attribute controls` tab. For more information, see [Managing site-wide attribute controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-site-controls).

Note that dynamic facets and tiles can be created based just on accurate product catalog data. However, for the feature to work optimally for your site, the facet models need to learn from activity on your site. For this, you need to set query, category, and filter fields in your search event uploads accurately.

If none of your serving configs has dynamic facets and tiles enabled and you just enabled dynamic facets and tiles in a serving config, expect to wait three to four days before they work.

## How attribute configuration impacts facet appearance

To effectively control how and when facets appear to your shoppers, it's crucial to understand the relationship between your catalog's attribute configuration and the AI Commerce Search faceting behavior. Facet appearance is primarily governed by two attribute settings: indexable and dynamic faceting.

### Indexable option as prerequisite

For an attribute to appear as a facet—whether static or dynamic—it must first be configured as **Indexable**.

  * **System attributes** : Predefined system attributes (such as `brand`, `availability`, `color`, and `size`) are indexable by default, and this setting cannot be disabled.
  * **Custom attributes** : Custom attributes (such as `store_name` or `style`) are indexable by default, but you can choose to disable this setting.



### Static or dynamic facet appearance

When an attribute is indexable, its appearance in search results depends on whether it is requested statically or dynamically:

  * **Static facets** : These facets appear because you explicitly request them in the `SearchRequest` using the `facetSpecs` field. As long as the requested attribute is indexable, the facet will be returned with the search results.
  * **Dynamic facets** : These facets appear automatically based on past user behavior (such as facet clicks and views) and relevance to the specific search query. For an attribute to appear dynamically, the **Dynamic faceting and tiling** option must be enabled for that attribute, and the serving config must also have dynamic faceting enabled.



### Textual and numerical facet behavior

The data type of your attribute significantly changes how it can be surfaced as a facet:

  * **Textual attributes** : Dynamic faceting is natively supported only for textual attributes (such as `Color: Red`).
  * **Numerical attributes** : Dynamic faceting is not natively supported for numerical attributes. To facet on numerical attributes (such as `Price`), you must either: 
    * Pass them as static facets and explicitly define `intervals` (buckets) in the search request, such as `$0-$50` and `$50-$100`.
    * Convert the numerical attribute to a textual attribute in your data pipeline (e.g., storing the price bucket as a string) and ingest it as a custom attribute to use dynamic faceting.



## Limits for attribute configuration and facets

When designing your search and faceting experience, be aware of the following system limits and behavioral constraints.

### Configuration and catalog limits

  * **Maximum attributes** : You can configure a maximum of 1,000 catalog attributes in an `AttributesConfig` request.
  * **Time to effect (attributes)** : Changes to attribute settings like `Indexable` or `Searchable` take effect immediately after your next catalog import, or within 12-24 hours if updated in the API.
  * **Time to effect (dynamic facets)** : Changes to `Dynamic Faceting` toggles or adding dynamic faceting to a serving config for the first time can take between two to four days to take effect.



### Search request and response limits

  * **Maximum facets per request** : A maximum of 200 `FacetSpec` objects can be included in a single search request.
  * **Maximum values per facet** : A single facet can return a maximum of 300 values (the default is 50).
  * **Maximum intervals** : You can define a maximum of 40 intervals (buckets) for a single numerical facet.
  * **Prefixes and contains** : When filtering facet values using `prefixes` or `contains`, you are limited to a maximum of 10 strings.
  * **Restricted values** : When using `restrictedValues` to limit returned facets, you can specify a maximum of 20 values.



### Data volume requirements

For dynamic faceting to work optimally and surface the most relevant facets, at least 10% of your ingested search user events must contain supported filter statements.

## Facet controls

This section provides instructions for creating different types of facet controls, many of which govern [tile](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/tiles) behavior also:

  * Ignore facet and tile values controls
  * Replace facets and tile values controls
  * Merge facets controls
  * Set numerical intervals controls
  * Remove facets and tile controls
  * Force return facets controls
  * Rerank dynamic facets controls



AI Commerce Search performs case-sensitive matching for all these facet controls unless stated otherwise. 

**Note:** The last three dynamic facet control types, remove, force return, and rerank, do **not** impact tiles.

To control specific facet values and tile behavior, navigate to the **Facet controls** tab in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

Click **Create control** to modify facets returned from search. A **Create control** pane opens. Click the **Control type** field to open a drop-down menu, from which you can select the control type. Each one opens a dialog with options for controlling your facets. All facet control types require at least the attribute information, but each form requires slightly different information.

![Alt text](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/create-facet-control-flyout.png)

### Create an ignore facet and tile values control

Create an ignore facet and tile values control when you want to remove some unwanted facet and tile values for some specific facet and tile keys.

**Note:** You can only ignore textual attributes. This control does not apply to numerical attributes.

This control is useful to erase unwanted facet and tile values like `NA` and `Not_applicable`. But, it can also be used to erase seasonal trends like `Easter` if you are in October.

To create a control that ignores facet and tile values:

  1. Go to the Controls page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Facet controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. Select **Ignore facet and tile values**.

  4. Specify the attribute name.

For example, `brands` for a system attribute. For a custom attribute, the name starts with `attributes.`—for example, `attributes.department` and `attributes.colors`. 

  5. Optional: Specify **Start Time** and/or **End Time**.

  6. Specify one or more attribute values as **Ignore values**.

For example, `NA`, `Not_applicable` and `Easter`.

  7. Click **Submit**.




### Create a replace facet and tile values control

Create a replace facet and tile values control when you want to consolidate a number of similar facet and tile values into one single term.

Replacing facet and tile values is sometimes referred to as _merging facet and tile values_.

To avoid conflicts and useless mappings, if an attribute value `facet_value_1` is replaced by another attribute value `facet_value_2`, then the latter can't be replaced by another attribute value. For example, if you replace `ruby` with `dark red`, you can't subsequently replace `dark red` with `red`.

For each attribute name, an attribute value shouldn't appear more than once in the **Replace values** field.

**Note:** This feature works only for custom textual attributes. Numeric attribute values cannot be replaced. During indexing for each product, both the replaced values and the replacement values will be included as attribute values unless you exceed the maximum number of values allowed per custom attribute in a per product, in which case search will truncate the replacement values arbitrarily.

To create a control that replaces facet and values:

  1. Go to the Controls page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Facet controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. Select **Replace facet and tile values**.

  4. Specify the attribute name.

This feature works only for custom attributes, which start with the prefix with `attributes` —for example, `attributes.department` and `attributes.colors`.

  5. Specify one or more attribute values as **Replace values** \- for example, `RED`, `Red`, `dark red`, `bright red`, `ruby`, and `crimson`.

An attribute value can only appear once in the **Replace values** field.

  6. Specify a single attribute value as **Replacement term** \- for example, `red`.

  7. Click **Submit**.




Although the replaced values might disappear quickly, the replacement terms can take up to four days to appear.

When the replace facet values control takes effect, if the facet key (in this example `attributes.colors`) is returned in the response, the replaced facet values (such as `dark red` and `crimson`) won't be present as facet values. They are replaced by their replacement terms (for example, `red`).

### Create a merge facets control

It is better to set correctly the product custom attribute names and values on your side before the products are ingested into search's database. However, if you can't change custom attribute names, you can create merge facets controls. You create a merge facets control if you want to merge (replace) a facet with another facet. For example, you might have several custom facet keys for colors like `attributes.colors_jeans`, `attributes.colors_clothes` and `attributes.colors_hue` and you want to replace them with an existing custom facet key called `attributes.colors`.

**Note:** You can only merge a textual facet into another single textual facet. Similarly, you can only merge a numerical facet into another single numerical facet. You can merge a facet into at most one merged facet. You can merge several facets into the same merged facet. Both a key and its merged key should be valid custom attribute names (with the added prefix `attributes.`). In other words, these two keys should be the custom attribute names of some ingested products.

Preferably, merged keys should be:

  * Custom attribute names that are permanent and won't change type.
  * Attribute names of many ingested products.



If you delete a merged key, you lose its engagement data, which is used to train dynamic facet models.

During indexing for each product, both the keys and the merged keys are included as attribute names, unless you exceed the maximum number of attributes allowed per product. If the maximum number of attributes exceed the quota allowed per product, search arbitrarily truncates the merged keys that become attribute names.

For example, if you already have the maximum number of custom attribute names for a specific product and one of its custom attribute names is `colors_jeans`, suppose you use a merge facets control to merge `attributes.colors_jeans` into `attributes.colors`. In this case, the attribute name `colors` won't be added to this specific product as it already contains the maximum number of custom keys per product. The merged keys won't be deleted from the (custom) attribute names of products, but they won't be returned as dynamic facet keys either. Similarly, if you merge several keys with the same key and this results in the number of attribute values for the merged key exceeding the limit of attribute values allowed, search arbitrarily truncates the attribute values.

To create a control that merged a facet into another:

  1. Go to the Controls page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Facet controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. Select **Merge facets**.

  4. Specify a valid custom facet key that merges into another one.

This feature works only for custom attributes, which start with the prefix with `attributes` —for example, `attributes.colors_clothes` and `attributes.colors_jeans`.

  5. Specify a valid custom facet key as the merged key.

  6. Click **Submit**.




This control typically takes effect in 2-4 days.

### Create a set numerical intervals control

The set numerical intervals control lets you determine the intervals for a numeric facet or tile instead of having to accept calculated intervals.

For example, search might calculate the intervals [10,15), [15,20) [20,25), [25,30), [30,40) and [40,50) and [50,infinity) for the custom numerical facet key `attributes.monitor_size`. But, you might prefer the intervals [0,14), [14,17), [17,21), [21,24), [24,27), [27,32) and [32,infinity) instead.

#### About calculated intervals and set intervals

**Note:** Search calculates intervals only if you have at least one [`serving config`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#dynamic) with [`DynamicFacetSpec`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.servingConfigs#dynamicfacetspec) set to `Enabled`.

For all numerical custom attributes and the numerical system attributes `price`, `rating` and `ratingCount`, search calculates some intervals with round bounds based on the distribution of all the (numerical) attribute values for each of these attributes. You can also specify some intervals in the request. As a last option, you can set your own intervals for each numerical facet key using the following set numerical intervals controls.

Here is the priority order that determines which intervals are used:

  1. First, if some intervals are specified in the request for a numerical facet key, these intervals are kept.

  2. Otherwise, if a numerical facet key is dynamic or passed in the request without intervals, then the intervals that you include using the set numerical intervals controls are added to that numerical facet key if these intervals are non-empty.

  3. Otherwise, the previously mentioned calculated intervals with round bounds are be added.




#### Create the control

If you want to specify your own intervals for numeric facet and tile keys instead of using the ones that AI Commerce Search calculates for you, then create a set numerical intervals controls.

**Note:** You can only set intervals to numerical attributes.

To create a control for adding intervals:

  1. Go to the Controls page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Facet controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. Select **Set numerical facet and tile intervals**.

  4. Specify the name of a numerical attribute.

For example, `price` for a system attribute. For a custom attribute, the name starts with `attributes.`—for example, `attributes.number_of_pieces`.

  5. Specify at least one of **Minimum** or **Maximum**. If both are specified, the minimum can't be greater than the maximum. You can choose each bound to be **Inclusive** or **Exclusive**.

  6. To add more intervals, click _add_box_**Add intervals**. The maximum number of intervals is 40.

  7. Click **Submit**.




### Create a control for removing facets and tiles

The remove facets control lets you to remove a specific facet and tile key from the dynamic facets. Facet and tile keys are removed based on some given query terms or page categories.

This facet control type controls the attribute itself. No facets or tiles associated with this facet as members will be returned in the search if this facet control type is applied.

This control is useful if you want to remove some facet and tile keys for some query terms or browse. For example, you can use this control to remove the facet key `attributes.shoe_size` for the query `shoes`.

You can use the Merchandising console or the Google Cloud console to remove a facet or tile:

###  Merchandising console 

  1. Click the URL provided by the administrator. Sign in.

This takes you to the **Controls** page in the **Merchandising console**.

  2. Click _add_box_**Create control**.

  3. Define the goals for your end users and timing required. All questions are required to be answered. Click **Next**.

  4. **Select a control**. Enter the name for your control, select the **Search** product, then choose the control type **Remove facets**.

  5. Configure your **Remove facets** control:

     1. Under **Triggers** , define what catalog attribute triggers this control by giving criteria to a related search query, such as _contains_ or _not in range_. If no catalog attribute has been configured, this control will always apply.

     2. Define an **Applicable time range** by entering a **Date range**. If any of the specified time ranges are met, the catalog attribute will be matched with the query during any of the specified time ranges. Add a time range with _add_box_**Add time range**.

     3. Define the **Attribute to ignore** under the **Remove facets actions** section for attirbutes you don't want to appear in dynamic facets for the query terms specified under the previous **Triggers** section. 

     4. Click _class="material-icons" >add_box_**Add attribute** to add more attributes.

  6. Click **Submit** to submit your control request to an Approver. You will be able to see the status of submitted requests in the Merchandising Console. If you change your mind, you can delete your control request.




#### Approver steps

  1. Under **Serving configs,** assign your control to existing serving config.
  2. [Approve the request](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#approver-notes) for a **Remove facets** control.



###  Cloud console 

  1. Go to the Controls page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Facet controls** tab, click _add_box_**Create control**. The **Create control** pane opens.

  3. Select **Remove facets and tiles**.

  4. Each control is for search or browse, but it can't apply to both. Do one of the following:

     * For search queries, click **Search** and specify some partial query terms or some exact query terms to match. See detailed information in [query terms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.retail_v2.types.Condition.QueryTerm) and [conditions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.retail_v2.types.Condition). The query terms need to be lowercase for both cases. For example, you can specify the partial query terms `shirts`, `polo`, `jackets`, `t-shirt` and `fall coats` and the facet keys specified next won't appear as a dynamic facet if the lowercase query is one of these query terms or contains any of these query terms as a unigram.

     * For browse, click **Browse categories** and specify some page categories. You can specify a list (up to 10 entries) of categories or departments. The format should be the same as the user event [page categories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.UserEvent#_Google_Cloud_Retail_V2_UserEvent__getPageCategories__). For example, it could be `page_categories` : `Sales > 2023 Black Friday Deals`. If there is an exact match (case sensitive) between the latter and one of the page categories passed in the event (for browse), then the facet keys specified next won't appear as a dynamic facet.

  5. Specify at least one valid facet key in **Attributes to ignore**.

  6. Click **Submit**.




### Create a force return facets control

If you have dynamic facets enabled for your facet serving config already, the force return facets control affects the list position, or order, of a dynamic facet key for a specific query or browse event.

**Important:** To add this control, force dynamic facets to appear in your facets by adding [`facet_spec`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec) to your search request.

The force return facets control is useful if you want to force a specific facet key among the dynamic facets for some query terms or browse. For example, you can use this control to force the facet key `brands` to appear to position 10 or a smaller position for the query `handbags`. If the facet `brands` is already in the top 10 for the dynamic facets for this query, then it shouldn't move much. If it is not in the top 10 or not in the list of dynamic facets, then it should move to position 10 approximately.

You can create a control for force return facets in the Merchandising console or the Google Cloud console.

###  Merchandising console 

  1. Click the URL provided by the administrator. Sign in.

This takes you to the **Controls** page in the **Merchandising console**.

  2. Click _add_box_**Create control**.

  3. Define the goals for your end users and timing required. All questions are required to be answered. Click **Next**.

  4. **Select a control**. Enter the name for your control, select the **Search** or **Browse** product, then choose the control type **Force return facets**.

  5. Configure your **Force return facets** control:

     1. Under **Triggers** , define what catalog attribute triggers this control by giving criteria to a related search query, such as _contains_ or _not in range_. If no catalog attribute has been configured, this control will always apply.

     2. Define an **Applicable time range** by entering a **Date range**. If any of the specified time ranges are met, the catalog attribute will be matched with the query during any of the specified time ranges. Add a time range with _add_box_**Add time range**.

     3. Define the **Attribute position adjustment** under the **Force return facets actions** section. Here you can choose an attribute that you want included in the dynamic facets or tiles for the query or page category you set in the previous **Triggers** section. Choosing a position of 5, for example, sets the facet to appear at the fifth position from the bottom of the page or higher.

     4. Click _add_box_**Add adjustment** to add more attributes to be governed by this control.

  6. Click **Submit** to submit your control request to an Approver. You will be able to see the status of submitted requests in the Merchandising Console. If you change your mind, you can delete your control request.




#### Approver steps

  1. Under **Serving configs,** assign your control to existing serving config.
  2. [Approve the request](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#approver-notes) for a **Force return facets** control.



###  Cloud console 

  1. Go to the Controls page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Facet controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. Select **Force return facets**.

  4. Each control is for search or browse, but it can't apply to both. Do one of the following:

     * For search queries, click **Search** and specify some partial query terms or some exact query terms to match. See detailed information in [query terms](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.retail_v2.types.Condition.QueryTerm) and [conditions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.retail_v2.types.Condition). The query terms need to be lowercase for both cases. For example, you can specify the partial query terms `shirts`, `polo`, `jackets`, `t-shirt` and `fall coats` and the facet keys specified next should appear around their respective position or higher among the dynamic facets if the lowercase query is one of these query terms or contains any of these query terms as a unigram.

     * For browse, click **Browse categories** and specify some page categories. You can specify a list (up to 10 entries) of categories or departments. The format should be the same as the user event [page categories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.UserEvent#_Google_Cloud_Retail_V2_UserEvent__getPageCategories__). For example, it could be `page_categories` : `Sales > 2023 Black Friday Deals`. If there is an exact match (case sensitive) between the latter and one of the page categories passed in the event (for browse), then the facet keys specified next should appear around their respective position or higher among the dynamic facets.

  5. Specify a valid facet key and an integer position between 1 and 100 (inclusive).

  6. If you want to specify more than one facet key, click _add_box_**Add adjustment** and redo the previous step.

  7. Click **Submit**.




### Create a rerank dynamic facets control

The dynamic facet ranking depends on the query (search) or page categories (browse). The rerank dynamic facets control also allows the ranking to depend on some facet values engaged by the user.

For example, using this control, if the user engages the facet value `watches` of the facet key `attributes.department` following a search or browse, then the ranking will also depend on the facet value `watches`. You can specify the facet values that you want to rerank on by facet key, or specify only the facet key and rerank on all its facet values.

**Note:** You can use this control only for custom facetable textual keys. To use this control, you also need to pass all the facet keys engaged by the user in the request using the field [`FacetSpec`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec). In particular, if you don't pass the facet keys engaged that you want to rerank on, this control won't be effective. Moreover, to obtain better results, the facet values that you want to rerank on should be close to English (ideally made of words, underscores, and spaces).

To create a control for rerank dynamic facets:

  1. Go to the Controls page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

[Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. On the **Facet controls** tab, click _add_box_**Create control**.

The **Create control** pane opens.

  3. Select **Rerank dynamic facets**.

  4. Specify a valid custom textual facet key (all custom keys have the prefix `attributes.`).

  5. You can either specify some specific facet values or apply to all.

     * If you want to rerank on all its facet values, click _add_box_**Any value changes**.

     * If you want to rerank on specific facet values, click _add_box_**Selected values changes**. Then insert all the facet values that you would like to rerank on (case sensitive). For example, it could be `watches`, `luggages`, `bed`.

  6. Click **Submit**.




You need to pass all the facet keys engaged by the user in the request for the following reasons:

  * Suppose that a user browses for sales and gets a first list of facet keys presented.
  * Then, the user engages first the facet key `attributes.age_group`.
  * Next, they engage the facet key `attributes.department` with the facet values `watches`, for which you set up a control to rerank on.



At that point, search reranks the keys.

So, it is possible that the previously engaged facet key `attributes.age_group` won't be returned in the response. If you pass this key in the request (using a [`Facetspec`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec) with [`enableDynamicPosition`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec) field set to `true`), it will automatically be returned in the response.

However, search could return that key at position 27 and you might show only the first 20 keys to the user. Because of this, make sure that these keys previously engaged by the user will be shown to the user. If you don't want to show too many keys to the user, you might have to filter out some intermediate non-engaged keys in the response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
