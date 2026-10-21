---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Query/
title: google.appengine.api.search.Query \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:01:55.284847+00:00
---

# google.appengine.api.search.Query  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.Query Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3226-L3372) Represents a request on the search service to query the index. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.Query`
    
    
    google.appengine.api.search.Query(
        query_string,
        options=None,
        enable_facet_discovery=False,
        return_facets=None,
        facet_options=None,
        facet_refinements=None
    )
    

| 

## Args  
  
---  
  
`query_string` |  The query to match against documents in the index. A query is a boolean expression containing terms. For example, the query 'job tag:"very important" sent <= 2011-02-28' finds documents with the term job in any field, that contain the phrase "very important" in a tag field, and a sent date up to and including 28th February, 2011. You can use combinations of '(cat OR feline) food NOT dog' to find documents which contain the term cat or feline as well as food, but do not mention the term dog. A further example, 'category:televisions brand:sony price >= 300 price < 400' will return documents which have televisions in a category field, a sony brand and a price field which is 300 (inclusive) to 400 (exclusive). See https://developers.google.com/appengine/docs/python/search/overview#Expressions for a list of expressions that can be used in queries.   
`options` |  A QueryOptions describing post-processing of search results.   
`enable_facet_discovery` |  discovery top relevant facets to this search query and return them.   
`return_facets` |  An iterable of FacetRequest or basestring as facet name to return specific facet with the result.   
`facet_options` |  A FacetOption describing processing of facets.   
`facet_refinements` |  An iterable of FacetRefinement objects or refinement token strings used to filter out search results based on a facet value. refinements for different facets will be conjunction and refinements for the same facet will be disjunction.   
  
## Raises  
  
---  
  
`QueryError` |  If the query string is not parseable.   
  
## Attributes  
  
---  
  
`enable_facet_discovery` |  Returns true if facet disocery is on.   
`facet_options` |  Returns FacetOptions defining processing of facets.   
`facet_refinements` |  Returns list of facet refinements.   
`options` |  Returns QueryOptions defining post-processing on the search results.   
`query_string` |  Returns the query string to be applied to search service.   
`return_facets` |  Returns the list of specific facets to be included with the result.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
