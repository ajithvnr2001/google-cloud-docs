---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/rescoringmatchscorerclass/
title: class RescoringMatchScorer \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:53:39.259016+00:00
---

# class RescoringMatchScorer  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/rescoringmatchscorerclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  class RescoringMatchScorer Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `RescoringMatchScorer` allows you to sort documents based on the quality of query match. It is similar to a [MatchScorer](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/matchscorerclass) but uses a more complex scoring algorithm based on match term frequency and other factors like field type. Please be aware that this algorithm is continually refined and can change over time without notice. This means that the ordering of search results that use this scorer can also change without notice.

To use a `RescoringMatchScorer`, add it to the `SortOptions` as in the following code: 
    
    
      sort_opts = search.SortOptions(match_scorer=search.RescoringMatchScorer())

This sorts the documents in descending score order. The scores will be positive.

If you want to sort in ascending order, then use the following code:
    
    
      sort_opts = search.SortOptions(match_scorer=search.RescoringMatchScorer(),
          expressions=[search.SortExpression(
              expression='_score', direction=search.SortExpression.ASCENDING,
              default_value=0.0)])

The scores in this case will be negative.

`RescoringMatchScorer` is defined in the `google.appengine.api.search` module.

## Constructor

The constructor for class `RescoringMatchScorer` is defined as follows:

class RescoringMatchScorer()
    

Assigns a document score to search results representing how well they match the query, base on frequency of terms in the document and weighted by doc parts. 

Result value

    

A new instance of class `RescoringMatchScorer`.

Exceptions

TypeError
    

If any of the parameters have an invalid type, or an unknown attribute is passed.

ValueError
    

If any parameter has an invalid value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
