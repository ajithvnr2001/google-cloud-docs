---
url: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule
title: Class Rule (2.14.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:54.968482+00:00
---

# Class Rule (2.14.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Rule (2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.14.0 (latest)  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.2  1.20.1  1.19.1  1.18.0  1.17.0  1.16.3  1.15.1  1.14.1  1.13.0  1.12.0  1.11.0  1.10.2  1.9.0  1.8.1  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.2  0.4.2  0.3.1  0.2.0  0.1.0 
    
    
    Rule(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A rule is a condition-action pair

  * A condition defines when a rule is to be triggered.
  * An action specifies what occurs on that trigger. Currently rules only work for controls with SOLUTION_TYPE_SEARCH.



This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`boost_action` |  `[google.cloud.retail_v2beta.types.Rule.BoostAction](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule.BoostAction)`   
A boost action. This field is a member of `oneof`_ `action`.   
`redirect_action` |  `[google.cloud.retail_v2beta.types.Rule.RedirectAction](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule.RedirectAction)`   
Redirects a shopper to a specific page. This field is a member of `oneof`_ `action`.   
`oneway_synonyms_action` |  `[google.cloud.retail_v2beta.types.Rule.OnewaySynonymsAction](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule.OnewaySynonymsAction)`   
Treats specific term as a synonym with a group of terms. Group of terms will not be treated as synonyms with the specific term. This field is a member of `oneof`_ `action`.   
`do_not_associate_action` |  `[google.cloud.retail_v2beta.types.Rule.DoNotAssociateAction](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule.DoNotAssociateAction)`   
Prevents term from being associated with other terms. This field is a member of `oneof`_ `action`.   
`replacement_action` |  `[google.cloud.retail_v2beta.types.Rule.ReplacementAction](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule.ReplacementAction)`   
Replaces specific terms in the query. This field is a member of `oneof`_ `action`.   
`ignore_action` |  `[google.cloud.retail_v2beta.types.Rule.IgnoreAction](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule.IgnoreAction)`   
Ignores specific terms from query during search. This field is a member of `oneof`_ `action`.   
`filter_action` |  `[google.cloud.retail_v2beta.types.Rule.FilterAction](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule.FilterAction)`   
Filters results. This field is a member of `oneof`_ `action`.   
`twoway_synonyms_action` |  `[google.cloud.retail_v2beta.types.Rule.TwowaySynonymsAction](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule.TwowaySynonymsAction)`   
Treats a set of terms as synonyms of one another. This field is a member of `oneof`_ `action`.   
`force_return_facet_action` |  `[google.cloud.retail_v2beta.types.Rule.ForceReturnFacetAction](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule.ForceReturnFacetAction)`   
Force returns an attribute as a facet in the request. This field is a member of `oneof`_ `action`.   
`remove_facet_action` |  `[google.cloud.retail_v2beta.types.Rule.RemoveFacetAction](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule.RemoveFacetAction)`   
Remove an attribute as a facet in the request (if present). This field is a member of `oneof`_ `action`.   
`pin_action` |  `[google.cloud.retail_v2beta.types.Rule.PinAction](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Rule.PinAction)`   
Pins one or more specified products to a specific position in the results. This field is a member of `oneof`_ `action`.   
`condition` |  `[google.cloud.retail_v2beta.types.Condition](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2beta.types.Condition)`   
Required. The condition that triggers the rule. If the condition is empty, the rule will always apply.   
  
## Classes 

### BoostAction
    
    
    BoostAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A boost action to apply to results matching condition specified above.

### DoNotAssociateAction
    
    
    DoNotAssociateAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Prevents `query_term` from being associated with specified terms during search. Example: Don't associate "gShoe" and "cheap".

### FilterAction
    
    
    FilterAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

  * Rule Condition:

    * No Condition.query_terms provided is a global match.
    * 1 or more Condition.query_terms provided are combined with OR operator.
  * Action Input: The request query and filter that are applied to the retrieved products, in addition to any filters already provided with the SearchRequest. The AND operator is used to combine the query's existing filters with the filter rule(s). NOTE: May result in 0 results when filters conflict.

  * Action Result: Filters the returned objects to be ONLY those that passed the filter.




### ForceReturnFacetAction
    
    
    ForceReturnFacetAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Force returns an attribute/facet in the request around a certain position or above.

  * Rule Condition: Must specify non-empty Condition.query_terms (for search only) or Condition.page_categories (for browse only), but can't specify both.

  * Action Inputs: attribute name, position

  * Action Result: Will force return a facet key around a certain position or above if the condition is satisfied.




Example: Suppose the query is "shoes", the Condition.query_terms is "shoes", the ForceReturnFacetAction.FacetPositionAdjustment.attribute_name is "size" and the ForceReturnFacetAction.FacetPositionAdjustment.position is 8.

Two cases: a) The facet key "size" is not already in the top 8 slots, then the facet "size" will appear at a position close to 8. b) The facet key "size" in among the top 8 positions in the request, then it will stay at its current rank.

### IgnoreAction
    
    
    IgnoreAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Prevents a term in the query from being used in search. Example: Don't search for "shoddy".

### OnewaySynonymsAction
    
    
    OnewaySynonymsAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Maps a set of terms to a set of synonyms. Set of synonyms will be treated as synonyms of each query term only. `query_terms` will not be treated as synonyms of each other. Example: "sneakers" will use a synonym of "shoes". "shoes" will not use a synonym of "sneakers".

### PinAction
    
    
    PinAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Pins one or more specified products to a specific position in the results.

  * Rule Condition: Must specify non-empty Condition.query_terms (for search only) or Condition.page_categories (for browse only), but can't specify both.

  * Action Input: mapping of `[pin_position, product_id]` pairs (pin position uses 1-based indexing).

  * Action Result: Will pin products with matching ids to the position specified in the final result order.




Example: Suppose the query is `shoes`, the Condition.query_terms is `shoes` and the pin_map has `{1, "pid1"}`, then product with `pid1` will be pinned to the top position in the final results.

If multiple PinActions are matched to a single request the actions will be processed from most to least recently updated.

Pins to positions larger than the max allowed page size of 120 are not allowed.

### RedirectAction
    
    
    RedirectAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Redirects a shopper to a specific page.

  * Rule Condition: Must specify Condition.query_terms.
  * Action Input: Request Query
  * Action Result: Redirects shopper to provided uri.



### RemoveFacetAction
    
    
    RemoveFacetAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Removes an attribute/facet in the request if is present.

  * Rule Condition: Must specify non-empty Condition.query_terms (for search only) or Condition.page_categories (for browse only), but can't specify both.

  * Action Input: attribute name

  * Action Result: Will remove the attribute (as a facet) from the request if it is present.




Example: Suppose the query is "shoes", the Condition.query_terms is "shoes" and the attribute name "size", then facet key "size" will be removed from the request (if it is present).

### ReplacementAction
    
    
    ReplacementAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Replaces a term in the query. Multiple replacement candidates can be specified. All `query_terms` will be replaced with the replacement term. Example: Replace "gShoe" with "google shoe".

### TwowaySynonymsAction
    
    
    TwowaySynonymsAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Creates a set of terms that will be treated as synonyms of each other. Example: synonyms of "sneakers" and "shoes":

  * "sneakers" will use a synonym of "shoes".
  * "shoes" will use a synonym of "sneakers".



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
