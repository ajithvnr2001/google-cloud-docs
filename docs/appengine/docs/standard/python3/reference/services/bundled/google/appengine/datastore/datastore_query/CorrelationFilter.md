---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/CorrelationFilter/
title: google.appengine.datastore.datastore_query.CorrelationFilter \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:52.408489+00:00
---

# google.appengine.datastore.datastore_query.CorrelationFilter  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/CorrelationFilter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_query.CorrelationFilter Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L670-L767) A filter that isolates correlated values and applies a sub-filter on them. Inherits From: [`FilterPredicate`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_query/FilterPredicate), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_query.CorrelationFilter(
        subfilter
    )
    

This filter assumes that every property used by the sub-filter should be grouped before being passed to the sub-filter. The default grouping puts each value in its own group. Consider: e = {a: [1, 2], b: [2, 1, 3], c: 4} A correlation filter with a sub-filter that operates on (a, b) will be tested against the following 3 sets of values: {a: 1, b: 2} {a: 2, b: 1} {b: 3} In this case CorrelationFilter('a = 2 AND b = 2') won't match this entity but CorrelationFilter('a = 2 AND b = 1') will. To apply an uncorrelated filter on c, the filter must be applied in parallel to the correlation filter. For example: CompositeFilter(AND, [CorrelationFilter('a = 2 AND b = 1'), 'c = 3']) If 'c = 3' was included in the correlation filter, c would be grouped as well. This would result in the following values: {a: 1, b: 2, c: 3} {a: 2, b: 1} {b: 3} If any set of correlated values match the sub-filter then the entity matches the correlation filter. | 

## Args  
  
---  
  
`subfilter` |  A FilterPredicate to apply to the correlated values   
  
## Attributes  
  
---  
  
`subfilter` |   
  
## Methods

### `__call__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L168-L177)
    
    
    __call__(
        entity
    )
    

Applies the filter predicate to the given entity.

Args  
---  
  
`entity` |  the datastore_pb.EntityProto to test.   
  
Returns  
---  
True if the given entity matches the filter, False otherwise.   
  
### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L81-L84)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_query.py#L86-L90)
    
    
    __ne__(
        other
    )
    

Return self!=value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
