---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/RescoringMatchScorer/
title: google.appengine.api.search.RescoringMatchScorer \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:15:54.495311+00:00
---

# google.appengine.api.search.RescoringMatchScorer  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/RescoringMatchScorer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.RescoringMatchScorer Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2286-L2313) Assigns a document score based on term frequency weighted by doc parts. Inherits From: [`MatchScorer`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/MatchScorer), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.RescoringMatchScorer`
    
    
    google.appengine.api.search.RescoringMatchScorer()
    

If you add a RescoringMatchScorer to a SortOptions as in the following code:
    
    
    sort_opts = search.SortOptions(match_scorer=search.RescoringMatchScorer())
    

then, this will sort the documents in descending score order. The scores will be positive. If you want to sort in ascending order, then use the following code:
    
    
    sort_opts = search.SortOptions(match_scorer=search.RescoringMatchScorer(),
        expressions=[search.SortExpression(
            expression='_score', direction=search.SortExpression.ASCENDING,
            default_value=0.0)])
    

The scores in this case will be negative. | 

## Raises  
  
---  
  
`TypeError` |  If any of the parameters has an invalid type, or an unknown attribute is passed.   
`ValueError` |  If any of the parameters has an invalid value.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
