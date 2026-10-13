---
url: https://docs.cloud.google.com/python/docs/reference/servicedirectory/latest/google.cloud.servicedirectory_v1beta1.types.ListNamespacesRequest
title: Class ListNamespacesRequest (1.19.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:57.983133+00:00
---

# Class ListNamespacesRequest (1.19.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/servicedirectory/latest/google.cloud.servicedirectory_v1beta1.types.ListNamespacesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListNamespacesRequest (1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.12.1  1.11.6  1.10.0  1.9.1  1.8.2  1.7.1  1.6.0  1.5.3  1.4.1  1.3.1  1.2.1  1.1.0  1.0.4  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 
    
    
    ListNamespacesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The request message for RegistrationService.ListNamespaces.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The resource name of the project and location whose namespaces you'd like to list.   
`page_size` |  `int`   
Optional. The maximum number of items to return. The default value is 100.   
`page_token` |  `str`   
Optional. The next_page_token value returned from a previous List request, if any.   
`filter` |  `str`   
Optional. The filter to list results by. General `filter` string syntax: `` \- `` can be `name`, `labels.` for map field, or `attributes.` for attributes field \- `` can be ``, `>`, `<>`, `>=`, `!=`, `=`, `:`. Of which `:` means `HAS`, and is roughly the same as `=` \- `` must be the same data type as field \- `` can be `AND`, `OR`, `NOT` Examples of valid filters: \- `labels.owner` returns namespaces that have a label with the key `owner`, this is the same as `labels:owner` \- `labels.owner=sd` returns namespaces that have key/value `owner=sd` \- `name>projects/my-project/locations/us-east1/namespaces/namespace-c` returns namespaces that have name that is alphabetically later than the string, so "namespace-e" is returned but "namespace-a" is not \- `labels.owner!=sd AND labels.foo=bar` returns namespaces that have `owner` in label key but value is not `sd` AND have key/value `foo=bar` \- `doesnotexist.foo=bar` returns an empty list. Note that namespace doesn't have a field called "doesnotexist". Since the filter does not match any namespaces, it returns no results \- `attributes.managed_registration=true` returns namespaces that are managed by a GCP product or service For more information about filtering, see `API Filtering   
`order_by` |  `str`   
Optional. The order to list results by. General `order_by` string syntax: `` \- `` allows value: `name` \- `` ascending or descending order by ``. If this is left blank, `asc` is used Note that an empty `order_by` string results in default order, which is order by `name` in ascending order.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
