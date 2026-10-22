---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/matchscorerclass/
title: class MatchScorer \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:49.308395+00:00
---

# class MatchScorer  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/matchscorerclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  class MatchScorer Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `MatchScorer` allows you to sort documents based on the quality of query match. The scorer assigns a score based on term frequency in a document. 

To use a `MatchScorer`, add it to the `SortOptions` as in the following code:
    
    
      sort_opts = search.SortOptions(match_scorer=search.MatchScorer())

This sorts the documents in descending score order. The scores will be positive.

If you want to sort in ascending order, then use the following code:
    
    
      sort_opts = search.SortOptions(match_scorer=search.MatchScorer(),
          expressions=[search.SortExpression(
              expression='_score', direction=search.SortExpression.ASCENDING,
              default_value=0.0)])

The scores in this case will be negative.

`MatchScorer` is defined in the `google.appengine.api.search` module.

## Constructor

The constructor for class `MatchScorer` is defined as follows:

class MatchScorer()
    

Assigns a document score to search results representing how well they match the query, base on frequency of terms in the document. 

Result value

    

A new instance of class `MatchScorer`.

Exceptions

TypeError
    

If any of the parameters have an invalid type, or an unknown attribute is passed.

ValueError
    

If any parameter has an invalid value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
