---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules/
title: About serving controls \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:38.624533+00:00
---

# About serving controls  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  About serving controls Stay organized with collections  Save and categorize content based on your preferences. 

You can apply serving controls to [serving configs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs) to customize how search treats search queries and returns results. A serving control is a rule consisting of a condition-action pair, where the condition dictates when the serving control executes an action. The action specifies what behavior the serving control enacts.

You can create a serving control by using the API `Control.create` method.

If you don't want to use the API, you can choose [console](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#console-options) for creating serving controls in AI Commerce Search.

## Integration and configuration best practices

This section describes integration and configuration best practices using serving controls.

### Start with no controls

Start using AI Commerce Search with minimum to zero serving controls in place. Serving controls like boost and bury meddle with the ranking optimization that's originally done to improve the revenue and relevancy of the search result.

The serving controls should be added if there's a very strong business need to do so. For example, ABC.com is an online fashion marketplace. They have in-house brands **pqr** and **xyz** , along with other brands. Now, ABC.com could choose to boost in-house brands **pqr** and **xyz** , meaning, bringing them to the top of search results, for a few particular search queries, such as _women's tops._ The business use case for this could be that ABC.com has better margins with products of brand **pqr** and **xyz** , which provides the justification to interfere with the default ranking, meaning, to not use a boost.

Another reason to start out with minimal controls is because the backend AI model continuously learns and adapts based on user buying patterns and trends (as the backend trains on 30-90 days window worth of events). A good number of use cases around synonyms would be already taken care of.

In summary, the decision to add serving controls should be backed by some strong revenue indicator or business use case.

### Attribute configuration

See prerequisites on attribute configuration here. The purpose of attributes is to extend the product information structure and add user defined product attributes. The attributes are not to be used as a store of information. Additionally, set true/false flags for the attributes that make it searchable and indexable. Set at least one of the configuration flags to true for the attributes.

### Exact match attribute config

The exact match config flag is used for attributes like `model_name` or `part_number` which tend to be unique alphanumeric characters. For example, a washing machine model might have a model number like `"WA2300AH3000"`. In this case, set the attribute as `model_name` and set the config for exact match to `true` so that when the search query matches the `model_name` attribute string, only this product is returned in the search result.

A word of caution is to not use commonly-used words or brands in attributes and have exact match set to true. This highly restricts the search result when those commonly-used words are in the search query, resulting in low product recall for commonly-used search queries, as well as negatively impacting the CTR / CVR metrics.

### AI Commerce Search is a ranking service only

The value proposition of the AI Commerce Search service is that it is used to discover products from your catalog based on query relevance and rank them in a revenue optimized manner (along with auxiliary functionalities like Boost/Bury/Filter etc.).

Essentially, AI Commerce Search service returns a revenue- and relevance-optimized ranked list of products to be displayed to the end user. AI Commerce Search is not a replacement for the catalog database.

**Important:** Don't connect or integrate the search response from AI Commerce Search with the UI components directly. Instead, build an enrichment layer that enriches the search response with additional data that might not be returned as part of the search response, but is needed for the user interface and search experience.

If needed, the product's GET and LIST APIs can be used to get the complete product information as part of the enrichment layer.

## Available serving controls

The following serving controls are available:

  * **Boost/bury**: Affects result ranking and order in the returned result list. Available for search and recommendations.
  * **Filter**: Removes results that don't pass the filter from the returned result list. Available for search only.
  * **Redirect**: Redirects your users to a specific page depending on the search query. Available for search only.
  * **Pinning**: Exact position in the results is specified for a certain product.
  * **Linguistic**: Customizes search query linguistics. Available for search only. Several types of linguistic controls are available: 
    * **Synonym**: Expands considered synonyms for a search query.
    * **One-way synonym**: Expands considered synonyms unidirectionally for specific terms.
    * **Ignore**: Prevents a term from being used in searches.
    * **Do not associate**: Prevent terms from being used in searches when specific terms appear.
    * **Replacement**: Replaces terms in the search query.



## Control conditions

Control conditions dictate when a serving control executes an action.

Control condition fields can be query terms, time ranges, or both. Some control types allow multiple condition fields, or don't allow any.

The condition fields available:

  * **Query terms** : Triggered when the term appears in the search query. 
    * A full match requires the entire search query to match the query term.
    * Multiple query terms can be specified. Triggers as long as one of the query terms appears in the search query.
  * **Active time range** : Triggered when the date of the search query is in the time range. 
    * Multiple time ranges can be specified. Triggers as long as date of query is within the time range (inclusive).



The condition fields that you specify determine whether the control is applied.

  * **Multiple condition fields** are combined using AND. This means that if you specify both time range and query terms, both condition fields need to be triggered for the control to apply.
  * **Multiple condition sub-fields** are combined using OR. This means that if you have multiple query terms the query terms are triggered if any one query term matches. If you have multiple time ranges, any one time range that matches triggers the control.
  * **No condition fields** specified mean the control always applies. However, some controls require a field to be defined.



For more about condition settings, see the [`Controls.condition` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls#condition).

## Control actions

A control action specifies what behavior the serving control enacts if the conditions are met during a search.

What kind of action you can specify depends on the type of serving control you create. For example, the action for a boost/bury control is to apply a boost/bury value to products that the filter you specify, while the action for a one-way synonym control is to apply an associated term that you specify.

## Boost/bury controls

Boost/bury controls enable you to show certain search results as higher or lower in ranking.

You can create a boost/bury control for search or recommendations. Boost/bury for recommendations is in Public Preview.

When creating a boost/bury control, you can use filter expressions to specify the conditions based on `Product` fields.

  * For search filters, use the filter expression syntax documented in [Filter and order results](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order).
  * For recommendations filters, use the filter expression syntax documented in [Filter recommendations](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-recs).



You can then apply a `boost` value between -1.0 and 1.0 to indicate how much to boost or bury product results matching those conditions. A positive value boosts the results, and a negative value buries them.

Setting a high boost strength gives the item a large promotion, but doesn't necessarily mean that the boosted item is the top result at all times. Results that are significantly more relevant to the search query can still trump heavily favored but irrelevant items. Likewise, setting the boost strength to -1.0 would give the item a large demotion, but results that are deeply relevant might still be shown.

As an example of using boost/bury, you could prioritize cheaper products and deprioritize the expensive ones.

Control conditions differ between search and recommendations boost/bury controls:

  * Search: You can set query terms and applicable time ranges as the control conditions.
  * Recommendations: Control conditions aren't available. The control always applies.



As a control action, specify a filter for products to boost or bury, and set the boost/bury value.

To create a boost/bury control, see [Create a new serving control](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#create-serving-control).

For more about boost/bury control settings, see the [`Controls.BoostAction` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls#boostaction).

## Filter controls

With filter controls, you can dynamically add predefined filters based on a specific search request.

You can use filter expressions based on `Product` fields. See [Filter and order results](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order) for the filter expression syntax.

You can set query terms and applicable time ranges as the control conditions. As a control action, specify a filter to apply at query time.

For example, given the query _blue shoes_ , you can use a filter control to automatically filter search results on the color blue. You can also use filter controls to prevent certain results from being returned to shoppers.

To create a filter control, see [Create a new serving control](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#create-serving-control).

For more about filter control settings, see the [`Controls.FilterAction` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls#filteraction).

## Redirect controls

You can use a redirect control to redirect your shoppers to different pages based on their intent, instead of only showing them search results.

You can set query terms and applicable time ranges as the control conditions. As a control action, specify a redirect URI to redirect to if the conditions are matched.

For example, you could create a redirect control so that during a promotion for a the product _gShoe_ , queries with _running shoes_ or _sports_ shoes redirects to the gShoe product page. Another case for using redirect controls would be to redirect shoppers to a specific page if they search for a term that is not relevant to your site, such as a search for _FAQ_ redirecting the user to the actual Frequently Asked Questions page on your site instead of showing search results.

To create a redirect control, see [Create a new serving control](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#create-serving-control).

For more about redirect control settings, see the [`Controls.RedirectAction` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls#redirectaction).

## Pinning controls

Pinning controls let you specify an exact position in the results you want a certain product to appear. You can create a pinning control for search or browse. It is not supported for recommendations. When creating a pinning control, you can use filter expressions to specify the conditions based on `Product` fields.

As a control action, add a `Rule` to your search or browse `Condition` which will be the action field `pin_action.`

You can then apply a `pin` value between [1,120] to indicate the fixed position to pin the results to matching those conditions given.

  * **Rule Condition** : Must specify non-empty `[Condition.query_terms][]` (for search only) or `[Condition.page_categories][]` (for browse only), but not both.
  * **Action Input** : `[pin_position, product_id]` pairs are mapped (the input position can be a value from 1 to 120). The maximum size is the maximum request page size. 10 is the number of allowed pairs in the pin map.
  * **Action Result** : Pin products with matching IDs to the position specified in the final result order. To name an example, suppose the query is _shoes_ , the `[Condition.query_terms][]` is `"shoes"` and the `pin_map` has `{1`, `pid1}`. The product with `pid1` is pinned to the top position in the final results.

**Note:** A query with an active pin experiences 100ms of added latency.

The [pinning rule](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.controls#PinAction) accepts any product ID (primary, variant, or collection), but the pinning effect is muted for any item with a non-primary product ID.

That means, if you want an exact variant or a collection to be visibly pinned to the top of the user interface:

  1. Create the pinning rule based on the item's primary product ID.

  2. Then, you must do either of the following:

     * Add an additional boost rule and boost the variant IDs (using a boost condition, such as `id:ANY(123, 234)`).
     * Add an additional filter rule to filter out the exact variant products of interest.



### Enabling pins and applied rules

When a pinning control is enabled:

  * Products with product IDs which match a pin appear in the final response in the exact position specified by the control.
  * Pins to the second page or later (higher page number) are not allowed, that is, any pin that is set to a position higher than the request `page_size` is ignored.
  * A maximum of 10 products can be pinned with one control.
  * The `product_id` must be the ID of an existing product in the catalog.



The product is always recalled in every search and appears on the page unless:

  * Filters and sorting are applied. These prevent pins from appearing.
  * The sort order (such as having the search results sorted by price) is not the default.



### Pin behavior

  * If a product is pinned, it ignores any [boosts or buries](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/boosting) from the request or from other controls.
  * If a product is pinned to multiple positions, the most recently updated control takes precedence.
  * Two products cannot be pinned to the same position inside the same pinning control (pin map). 
    * If multiple controls match the same query and each of those have a different pin for the same product ID, the `[pin_pos, p_id]` pair from the most recently updated control takes precedence.

**Caution:** Adding pinning controls to many common queries can adversely impact your total latency. Use sparingly and only when necessary.

## Linguistic controls

You can create additions or overrides to how words are treated for certain queries.

### Synonym controls

Setting two words as synonyms is a linguistic control that associates two words.

Synonym controls add additional context to a search query. They don't force a result to be included in the search results, but they can help the system include additional products in the search results, making it more likely that a given result is included. In other words, synonym controls can encourage the search result to consider more options, but ultimately the search result is dependent on scoring.

For example, if you want search results for _running shoes_ to also include _sport shoes_ , create a linguistic synonym control. The condition is that _running shoes_ is entered as the search term. The action is to include the synonym _sport shoes_ with that search. So when a shopper on your site searches _running shoes_ , search finds that match in the linguistic control you created, expanding it to include _sport shoes_ when it returns search results to the shopper.

To create a synonym control, see [Create a new serving control](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#create-serving-control).

### Two-way synonym controls

Use two-way synonym controls to link several terms together so that search treats them the same during searches.

You can set query terms and applicable time ranges as the control conditions. You don't need to set a separate control action; if a term you specified is used as a query, the control action is to use other terms you specified as the synonyms.

For example, you could set a two-way synonym control that associates the terms _dish towel_ and _kitchen towel_ as synonyms. When a shopper on your site enters _kitchen towel_ as a query, search can then expand the query to include results for _dish towel_ and _kitchen towel_.

To create a synonym control, see [Create a new serving control](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#create-serving-control).

Synonyms don't change the original query. For example, if queries A and B are a two-way synonym, expect the following effect:

  * **Query A results returned** : Set A (with no synonym rule applied) and some of set B. However, the results might be less than the combination of A and B.

  * **Query B results returned** : Set B and some of A, but possibly less than the sum of result sets A and B.




For more about two-way synonym control settings, see the [`Controls.TwowaySynonymsAction`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls#twowaysynonymsaction) API reference.

#### One-way synonym controls

One-way synonym controls expand query terms to link terms together unidirectionally.

You can set query terms and applicable time ranges as the control conditions. As a control action, specify the terms to use as one-way synonyms.

For example, you could set a one-way synonym control that expands searches for the term _rose_ to include the term _pink_. Because it is a one-way synonym, searches for the term _pink_ don't expand to include the term _rose_.

To create a one-way synonym control, see [Create a new serving control](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#create-serving-control).

Note that just as with two-way synonyms, the original query is executed and the synonyms are provided as hints to that query. Synonyms for entirely different words might only result in small numbers of the synonym terms being included in the results. The preceding example returns pink items with an emphasis on pink roses, but a synonym rule expanding searches for the term _dog_ to include _cat_ returns mostly items with dogs, plus some with cats.

For more about one-way synonym control settings, see the [`Controls.OnewaySynonymsAction` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls#onewaysynonymsaction).

#### Synonyms don't provide identical results

Search results for two synonyms aren't always identical. 

For example, if you set _laptop bags_ and _luggage_ as two-way synonyms, the system might already associate _suitcase_ with _luggage_. So, when a user searches for _luggage_ , AI Commerce Search returns results about _luggage_ , _suitcase_ , and _laptop bags_. However, when you search for _laptop bags_ , AI Commerce Search only adds _luggage_ to the synonyms. So the results might not contain _suitcase_.

### Ignore controls

Ignore controls prevent search from using certain query terms during searches. They mark ignored terms in a query as not important, but does not exclude them from the query entirely. 

To completely remove a search term from a query, use a replacement control. While a filter control affects which results are shown, a replacement control is a more robust way to prevent AI Commerce Search from returning results for a specific term.

An ignore control doesn't guarantee that results for the ignored term won't be returned in a AI Commerce Search results. For example, an ignore control for the word _oil_ could still return oil paints for a query of _oil paints._ The query is passed as _paints,_ and there could be many matching oil paints, but the result set is larger as the search is for _paints._ This type of control might be useful if _oil paints_ were a popular query on your site and you sell many different types of paints, but not many oil-based paints.

You can set query terms and applicable time ranges as the control conditions. You don't need to set a separate control action; if a term you specified is used as a query, the control action is to ignore that term.

For example, you could create a control that ignores query terms that use offensive language.

To create an ignore control, see [Create a new serving control](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#create-serving-control).

For more about ignore control settings, see the [`Controls.IgnoreAction` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls#ignoreaction).

### Do-not-associate controls

Do-not-associate controls suppress certain search terms from being associated with other specified ones. This won't necessarily affect the search results, but it can.

Use a given query term and applicable time ranges for your control conditions. As a control action, specify which terms _shouldn't_ be associated with the query terms.

Example: You create a control that prevents a brand name (such as _gShoe_) from grouping with _cheap_ and _poor quality_ in a query. A shopper searches for _poor quality cheap gShoe_. Search removes the query terms _cheap_ and _poor quality_ from the initial query, with the resulting query term being _gShoe._ However, this does not guarantee that it is entirely removed from the search results.

If a relevant query term also contains a term specified as do-not-associate, that relevant result might still be returned. To prevent this from happening entirely, use a filter control.

To create a do-not-associate control, see [Create a new serving control](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#create-serving-control).

For more about do-not-associate control settings, see the [`Controls.DoNotAssociateAction` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls#donotassociateaction).

### Replacement controls

Replacement controls replace one or more given query terms with a different term that you specify. You can specify multiple terms that can be mapped to single term (but not vice versa).

You can set query terms and applicable time ranges as the control conditions. As a control action, specify the term that should be used as a replacement.

For example, you could create a control that replaces nicknames for a brand with the full brand name that is more commonly used in product descriptions.

To create a replacement control in the AI Commerce Search in Gemini Enterprise for Customer Experience console, see [Create a new serving control](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#create-serving-control).

For more about replacement control settings, see the [`Controls.ReplacementAction` API reference](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.controls#replacementaction).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
