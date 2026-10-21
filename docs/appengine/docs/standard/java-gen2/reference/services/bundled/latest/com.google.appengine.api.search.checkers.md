---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers
title: Package com.google.appengine.api.search.checkers (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:31:36.574301+00:00
---

# Package com.google.appengine.api.search.checkers (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.search.checkers (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

## Classes 

### [CursorChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.CursorChecker)

Checks values of [com.google.appengine.api.search.Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor).

### [DocumentChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.DocumentChecker)

Checks values of a [com.google.appengine.api.search.Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document).

### [FacetChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.FacetChecker)

Provides checks for Facet names and values: atom or number.

### [FacetQueryChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.FacetQueryChecker)

Provides checks for faceted search related query options.

### [FieldChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.FieldChecker)

Provides checks for Field names, language code, and values: text, HTML, atom or date.

### [GeoPointChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.GeoPointChecker)

Provides checks for [com.google.appengine.api.search.GeoPoint](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GeoPoint).

### [GetIndexesRequestChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.GetIndexesRequestChecker)

Checks values of [com.google.appengine.api.search.GetIndexesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest).

### [GetRequestChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.GetRequestChecker)

Checks values of [com.google.appengine.api.search.GetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest).

### [IndexChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.IndexChecker)

Checks values of [Indexes](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index).

### [Preconditions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.Preconditions)

Simple static methods to be called at the start of your own methods to verify correct arguments and state. This allows constructs such as
    
    
     if (count <= 0)="" {="" throw="" new="" illegalargumentexception("must="" be="" positive:="" "="" +="" count);="" }="">

to be replaced with the more compact
    
    
         checkArgument(count > 0, "must be positive: %s", count);

Note that the sense of the expression is inverted; with `Preconditions` you declare what you expect to be _true_ , just as you do with an [`assert`](http://java.sun.com/j2se/1.5.0/docs/guide/language/assert.html) or a JUnit `assertTrue` call.

**Note:** This class is a copy of a very old version of Guava's Preconditions. Please use the current Guava version instead. See Also: "<https://google.github.io/guava/releases/21.0/api/docs/com/google/common/base/Preconditions.html>"

### [QueryChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.QueryChecker)

Checks values of [com.google.appengine.api.search.Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)).

### [QueryOnlyCustomerDocumentChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.QueryOnlyCustomerDocumentChecker)

This class performs DocumentPb.Document validity checks for search customers that only use the query API.

### [QueryOptionsChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.QueryOptionsChecker)

Checks values of [com.google.appengine.api.search.QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions).

### [SearchApiLimits](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits)

Contains limits on field values, document sizes, and other properties of objects in the Search API.

### [SortExpressionChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SortExpressionChecker)

Checks the values of a [com.google.appengine.api.search.SortExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression).

### [SortOptionsChecker](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SortOptionsChecker)

Checks the values of a [com.google.appengine.api.search.SortOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
