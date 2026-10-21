---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions.Builder
title: Class SortOptions.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:59:28.530009+00:00
---

# Class SortOptions.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class SortOptions.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class SortOptions.Builder

A builder that constructs [SortOptionss](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions). A SortOptions will evaluate each of the [SortExpressions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression) on each search result and apply a sort order with priority given to the sort expressions from left to right. The following code illustrates creating a SortOptions specification to sort documents based on decreasing product rating and then within rating showing cheapest products based on price plus tax, sorting at most 2000 documents. 
    
    
       SortOptions sortOptions = SortOptions.newBuilder()
           .addSortExpression(SortExpression.newBuilder()
               .setExpression("rating")
               .setDirection(SortExpression.SortDirection.DESCENDING)
               .setDefaultValueNumeric(0))
           .addSortExpression(SortExpression.newBuilder()
               .setExpression("price + tax")
               .setDirection(SortExpression.SortDirection.ASCENDING)
               .setDefaultValueNumeric(99999999.00))
           .setLimit(1000)
           .build();
     

The following code fragment shows how the score from a [MatchScorer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer) can be used in an expression that combines the score with one thousandth of an "importance" field. At most 1000 documents are scored and sorted.
    
    
       SortOptions sortOptions = SortOptions.newBuilder()
           .setMatchScorer(MatchScorer.newBuilder())
           .addSortExpression(SortExpression.newBuilder()
               .setExpression(String.format(
                   "%s + (importance * .001)", SortExpression.SCORE_FIELD_NAME))
               .setDirection(SortExpression.SortDirection.DESCENDING)
               .setDefaultValueNumeric(0))
           .setLimit(1000)
           .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SortOptions.Builder

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### addSortExpression(SortExpression sortExpression)
    
    
    public SortOptions.Builder addSortExpression(SortExpression sortExpression)

Adds a [SortExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression) to the list of sort expressions.

**Parameter**  
---  
**Name** | **Description**  
`sortExpression` | `[SortExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression)`  
an expression to sort documents by  
**Returns**  
---  
**Type** | **Description**  
`[SortOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions.Builder)` | this Builder  
  
### addSortExpression(SortExpression.Builder builder)
    
    
    public SortOptions.Builder addSortExpression(SortExpression.Builder builder)

Adds a [SortExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression) built from the builder to the list of sort expressions.

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[SortExpression.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder)`  
a builder of SortExpression to sort documents by  
**Returns**  
---  
**Type** | **Description**  
`[SortOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions.Builder)` | this Builder  
  
### build()
    
    
    public SortOptions build()

Builds a [SortOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions) from the set values.

**Returns**  
---  
**Type** | **Description**  
`[SortOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions)` | a [SortOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions) built from the set values  
  
### setLimit(int limit)
    
    
    public SortOptions.Builder setLimit(int limit)

Sets the limit on the number of documents to score or sort.

**Parameter**  
---  
**Name** | **Description**  
`limit` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the maximum number of documents to score or sort  
**Returns**  
---  
**Type** | **Description**  
`[SortOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions.Builder)` | this builder  
  
### setMatchScorer(MatchScorer matchScorer)
    
    
    public SortOptions.Builder setMatchScorer(MatchScorer matchScorer)

Sets a [MatchScorer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer) or [RescoringMatchScorer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RescoringMatchScorer) to base some [SortExpressions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression) on. The value of the matchScorer can be accessed by using the field name "_score".

**Parameter**  
---  
**Name** | **Description**  
`matchScorer` | `[MatchScorer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer)`  
the rescoring/match matchScorer to use in an expression built on "_score"  
**Returns**  
---  
**Type** | **Description**  
`[SortOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions.Builder)` | this builder  
  
### setMatchScorer(MatchScorer.Builder builder)
    
    
    public SortOptions.Builder setMatchScorer(MatchScorer.Builder builder)

Sets the matchScorer to the [MatchScorer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer) built from the builder. See Also: [#setMatchScorer(MatchScorer)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions.Builder#com_google_appengine_api_search_SortOptions_Builder_setMatchScorer_com_google_appengine_api_search_MatchScorer_)

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[MatchScorer.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer.Builder)`  
a builder of a MatchScorer  
**Returns**  
---  
**Type** | **Description**  
`[SortOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions.Builder)` | this builder  
  
### setMatchScorer(RescoringMatchScorer.Builder builder)
    
    
    public SortOptions.Builder setMatchScorer(RescoringMatchScorer.Builder builder)

Sets the matchScorer to the [RescoringMatchScorer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RescoringMatchScorer) built from the builder. See Also: [#setMatchScorer(MatchScorer)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions.Builder#com_google_appengine_api_search_SortOptions_Builder_setMatchScorer_com_google_appengine_api_search_MatchScorer_)

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[RescoringMatchScorer.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RescoringMatchScorer.Builder)`  
a builder of a RescoringMatchScorer  
**Returns**  
---  
**Type** | **Description**  
`[SortOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions.Builder)` | this builder  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
