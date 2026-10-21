---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/FacetRefinement/
title: google.appengine.api.search.FacetRefinement \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:56:02.177969+00:00
---

# google.appengine.api.search.FacetRefinement  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/FacetRefinement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.FacetRefinement Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L1349-L1457) A Facet Refinement to filter out search results based on a facet value. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.FacetRefinement`
    
    
    google.appengine.api.search.FacetRefinement(
        name, value=None, facet_range=None
    )
    

NOTE: The recommended way to use facet refinement is to use the token string. Each FacetResult will have a token that is acceptable instead of this class. To provide manual FacetRefinement, an instance of this class can be passed to SearchOptions. NOTE: that either value or facet_range should be set but not both. Example: Request for a range refinement for a numeric facet: FacetRefinement(name='rating', facet_range=FacetRange(start=1.0,end=2.5)) | 

## Args  
  
---  
  
`name` |  The name of the facet.   
`value` |  Value of the facet.   
`facet_range` |  A FacetRange to refine facet based on a range.   
  
## Raises  
  
---  
  
`TypeError` |  If any of the parameters have invalid types, or an unknown attribute is passed.   
`ValueError` |  If any of the parameters have invalid values.   
  
## Attributes  
  
---  
  
`facet_range` |  Returns range of the facet refinement.   
`name` |  Returns name of the facet refinement.   
`value` |  Returns value of the facet refinement.   
  
## Methods

### `FromTokenString`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L1409-L1443)
    
    
    @staticmethod
    FromTokenString(
        token_string
    )
    

Converts a token string to a FacetRefinement object.

Do not store token strings between different versions of API as key could be incompatible.

Args  
---  
  
`token_string` |  A token string created by ToTokenString method or returned by a search result.   
  
Returns  
---  
A FacetRefinement object.   
  
Raises  
---  
  
`ValueError` |  If the token_string is invalid.   
  
### `ToTokenString`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L1397-L1407)
    
    
    ToTokenString()
    

Converts this refinement to a token string safe to be used in HTML.

The format of this string may change.

Returns  
---  
A token string safe to be used in HTML for this facet refinement.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
