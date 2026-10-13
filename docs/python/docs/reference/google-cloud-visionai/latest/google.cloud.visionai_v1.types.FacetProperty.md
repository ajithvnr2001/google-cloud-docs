---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.FacetProperty
title: Class FacetProperty (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:50.363894+00:00
---

# Class FacetProperty (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.FacetProperty

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FacetProperty (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    FacetProperty(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Central configuration for a facet.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`fixed_range_bucket_spec` |  `[google.cloud.visionai_v1.types.FacetProperty.FixedRangeBucketSpec](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.FacetProperty.FixedRangeBucketSpec)`   
Fixed range facet bucket config. This field is a member of `oneof`_ `range_facet_config`.   
`custom_range_bucket_spec` |  `[google.cloud.visionai_v1.types.FacetProperty.CustomRangeBucketSpec](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.FacetProperty.CustomRangeBucketSpec)`   
Custom range facet bucket config. This field is a member of `oneof`_ `range_facet_config`.   
`datetime_bucket_spec` |  `[google.cloud.visionai_v1.types.FacetProperty.DateTimeBucketSpec](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.FacetProperty.DateTimeBucketSpec)`   
Datetime range facet bucket config. This field is a member of `oneof`_ `range_facet_config`.   
`mapped_fields` |  `MutableSequence[str]`   
Name of the facets, which are the dimensions users want to use to refine search results. `mapped_fields` will match UserSpecifiedDataSchema keys. For example, user can add a bunch of UGAs with the same key, such as player:adam, player:bob, player:charles. When multiple mapped_fields are specified, will merge their value together as final facet value. E.g. home_team: a, home_team:b, away_team:a, away_team:c, when facet_field = [home_team, away_team], facet_value will be [a, b, c]. UNLESS this is a 1:1 facet dimension (mapped_fields.size() == 1) AND the mapped_field equals the parent SearchConfig.name, the parent must also contain a SearchCriteriaProperty that maps to the same fields. mapped_fields must not be empty.   
`display_name` |  `str`   
Display name of the facet. To be used by UI for facet rendering.   
`result_size` |  `int`   
Maximum number of unique bucket to return for one facet. Bucket number can be large for high-cardinality facet such as "player". We only return top-n most related ones to user. If it's <= 0,="" the="" server="" will="" decide="" the="" appropriate="" result_size.="">  
`bucket_type` |  `[google.cloud.visionai_v1.types.FacetBucketType](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.FacetBucketType)`   
Facet bucket type e.g. value, range.   
  
## Classes 

### CustomRangeBucketSpec
    
    
    CustomRangeBucketSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

If bucket type is CUSTOM_RANGE, specify how values are bucketized. Use integer bucket value as an example, when the endpoints are 0, 10, 100, and 1000, we will generate the following facets: [-inf, 0), [0, 10), [10, 100), [100, 1000), [1000, inf). Notably:

  * endpoints must be listed in ascending order. Otherwise, the SearchConfig API will reject the facet config.
  * < 1 endpoints is an invalid spec.



### DateTimeBucketSpec
    
    
    DateTimeBucketSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

If bucket type is DATE, specify how date values are bucketized.

### FixedRangeBucketSpec
    
    
    FixedRangeBucketSpec(mapping=None, *, ignore_unknown_fields=False, **kwargs)

If bucket type is FIXED_RANGE, specify how values are bucketized. Use FixedRangeBucketSpec when you want to create multiple buckets with equal granularities. Using integer bucket value as an example, when bucket_start = 0, bucket_granularity = 10, bucket_count = 5, this facet will be aggregated via the following buckets: [-inf, 0), [0, 10), [10, 20), [20, 30), [30, inf). Notably, bucket_count <= 1 is an invalid spec.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
