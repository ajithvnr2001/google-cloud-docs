---
url: https://docs.cloud.google.com/python/docs/reference/cloudprivatecatalog/latest/google.cloud.privatecatalog_v1beta1.types.SearchProductsRequest
title: Class SearchProductsRequest (0.12.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:23.193874+00:00
---

# Class SearchProductsRequest (0.12.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudprivatecatalog/latest/google.cloud.privatecatalog_v1beta1.types.SearchProductsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SearchProductsRequest (0.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.2 (latest)  0.12.1  0.11.0  0.10.0  0.9.18  0.8.0  0.7.2  0.6.2  0.5.2  0.4.1  0.3.0  0.2.4  0.1.1 
    
    
    SearchProductsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for PrivateCatalog.SearchProducts.

## Attributes  
  
---  
**Name** | **Description**  
`resource` |  `str`   
Required. The name of the resource context. See SearchCatalogsRequest.resource for details.   
`query` |  `str`   
The query to filter the products. The supported queries are: \- List products of all catalogs: empty \- List products under a catalog: `parent=catalogs/{catalog}` \- Get a product by name: `name=catalogs/{catalog}/products/{product}`  
`page_size` |  `int`   
The maximum number of entries that are requested.   
`page_token` |  `str`   
A pagination token returned from a previous call to SearchProducts that indicates where this listing should continue from.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
