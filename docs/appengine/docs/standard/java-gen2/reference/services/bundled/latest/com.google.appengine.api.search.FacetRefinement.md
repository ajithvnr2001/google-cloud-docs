---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement
title: Class FacetRefinement (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:58:34.474497+00:00
---

# Class FacetRefinement (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class FacetRefinement (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class FacetRefinement

A Facet Refinement to filter out search results based on a facet value. 

We recommend using refinement token strings instead of this class. We include a refinement token string with each [FacetResultValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetResultValue) returned by the backend that can be passed to [Query.Builder#addFacetRefinementFromToken(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder#com_google_appengine_api_search_Query_Builder_addFacetRefinementFromToken_java_lang_String_) to refine follow-up queries. 

We also support manually-specified query refinements by passing an instance of this class to [Query.Builder#addFacetRefinement(FacetRefinement)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query.Builder#com_google_appengine_api_search_Query_Builder_addFacetRefinement_com_google_appengine_api_search_FacetRefinement_). 

Example: Request to only return documents that have a number facet named "rating" with a value between one and two:
    
    
     FacetRefinement lowRating = FacetRefinement.withRange("rating", FacetRange.startEnd(1.0, 2.0));
     query.addFacetRefinement(lowRating);
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FacetRefinement

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

## Static Methods 

### fromTokenString(String token)
    
    
    public static FacetRefinement fromTokenString(String token)

Converts a token string to a FacetRefinement object. 

NOTE: Do not persist token strings. The format may change.

**Parameter**  
---  
**Name** | **Description**  
`token` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A token string returned by [FacetResultValue#getRefinementToken](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetResultValue#com_google_appengine_api_search_FacetResultValue_getRefinementToken_) or [FacetRefinement#toTokenString](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement#com_google_appengine_api_search_FacetRefinement_toTokenString_).  
**Returns**  
---  
**Type** | **Description**  
`[FacetRefinement](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement)` | A [FacetRefinement](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement) object.  
  
### withRange(String name, FacetRange range)
    
    
    public static FacetRefinement withRange(String name, FacetRange range)

Create a [FacetRefinement](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement) with the given `name` and `range`.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the facet.  
`range` | `[FacetRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRange)`  
the range of the numeric facet.  
**Returns**  
---  
**Type** | **Description**  
`[FacetRefinement](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement)` | an instance of [FacetRefinement](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement).  
  
### withValue(String name, String value)
    
    
    public static FacetRefinement withValue(String name, String value)

Create a [FacetRefinement](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement) with the given `name` and `value`.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the facet.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the value of the facet (both numeric and atom).  
**Returns**  
---  
**Type** | **Description**  
`[FacetRefinement](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement)` | an instance of [FacetRefinement](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRefinement).  
  
## Methods 

### getName()
    
    
    public String getName()

Returns the name of the facet.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getRange()
    
    
    public FacetRange getRange()

Returns the range for numeric facets or null if there is no range.

**Returns**  
---  
**Type** | **Description**  
`[FacetRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetRange)` |   
  
### getValue()
    
    
    public String getValue()

Returns the value of the facet or null if there is no value.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

### toTokenString()
    
    
    public String toTokenString()

Converts this refinement to a token string safe to be used in HTML. 

NOTE: Do not persist token strings. The format may change.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | A token string safe to be used in HTML for this facet refinement.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
