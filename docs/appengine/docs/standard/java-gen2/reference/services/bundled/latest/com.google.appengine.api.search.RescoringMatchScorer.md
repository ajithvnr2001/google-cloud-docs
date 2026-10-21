---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RescoringMatchScorer
title: Class RescoringMatchScorer (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:29:49.382605+00:00
---

# Class RescoringMatchScorer (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RescoringMatchScorer

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class RescoringMatchScorer (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class RescoringMatchScorer extends MatchScorer

Assigns a document score based on term frequency weighted on document parts.

If you add a MatchScorer to a SortOptions as in the following code:
    
    
      SortOptions sortOptions = SortOptions.newBuilder()
          .setMatchScorer(RescoringMatchScorer.newBuilder())
          .build();
     

then this will sort the documents in descending score order. The scores will be positive. If you want to sort in ascending order, then use the following code:
    
    
       SortOptions sortOptions = SortOptions.newBuilder()
           .setMatchScorer(RescoringMatchScorer.newBuilder())
           .addSortExpression(
               SortExpression.newBuilder()
                   .setExpression(SortExpression.SCORE_FIELD_NAME)
                   .setDirection(SortExpression.SortDirection.ASCENDING)
                   .setDefaultValueNumeric(0.0))
           .build();
     

The scores in this case will be negative.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [MatchScorer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer) > RescoringMatchScorer

## Inherited Members

[MatchScorer.newBuilder()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer#com_google_appengine_api_search_MatchScorer_newBuilder__)

[MatchScorer.toString()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer#com_google_appengine_api_search_MatchScorer_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### newBuilder()
    
    
    public static RescoringMatchScorer.Builder newBuilder()

Creates and returns a RescoringMatchScorer Builder.

**Returns**  
---  
**Type** | **Description**  
`[RescoringMatchScorer.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RescoringMatchScorer.Builder)` | a new [RescoringMatchScorer.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RescoringMatchScorer.Builder). Set the parameters for scorer on the Builder, and use the Builder#build() method to create a concrete instance of RescoringMatchScorer  
  
## Methods 

### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[MatchScorer.toString()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.MatchScorer#com_google_appengine_api_search_MatchScorer_toString__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
