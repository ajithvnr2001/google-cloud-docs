---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/FacetOptions/
title: google.appengine.api.search.FacetOptions \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:26.627762+00:00
---

# google.appengine.api.search.FacetOptions  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/FacetOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.FacetOptions Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2937-L3000) Options for processing facet reults of a query. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.FacetOptions`
    
    
    google.appengine.api.search.FacetOptions(
        discovery_limit=10, discovery_value_limit=None, depth=None
    )
    

| 

## Args  
  
---  
  
`discovery_limit` |  Number of facets to discover if facet discovery is turned on. If None, discover facets will be disabled.   
`discovery_value_limit` |  Number of values to be discovered for each of the top discovered facets.   
`depth` |  Number of documents in query results to evaluate to gather facet information.   
  
## Raises  
  
---  
  
`TypeError` |  If an unknown attribute is passed.   
`ValueError` |  If any of the parameters have invalid values (e.g., a negative depth).   
  
## Attributes  
  
---  
  
`depth` |  Returns the number of documents to analyze for facet discovery.   
`discovery_limit` |  Returns the number of facets to discover.   
`discovery_value_limit` |  Returns the number of values to discover for each facet.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
