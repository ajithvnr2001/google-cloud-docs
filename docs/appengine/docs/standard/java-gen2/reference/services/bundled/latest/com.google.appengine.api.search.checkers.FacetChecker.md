---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.FacetChecker
title: Class FacetChecker (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:22:37.452488+00:00
---

# Class FacetChecker (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.FacetChecker

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class FacetChecker (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class FacetChecker

Provides checks for Facet names and values: atom or number.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FacetChecker

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

### checkAtom(String value)
    
    
    public static String checkAtom(String value)

Checks whether an atom is valid. An atom can be null or a string between 1 and SearchApiLimits.MAXIMUM_ATOM_LENGTH in length, inclusive.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the atom value to check  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the checked atom  
  
### checkFacetName(String name)
    
    
    public static String checkFacetName(String name)

Checks whether a facet name is valid. The facet name length must be between 1 and [SearchApiLimits#MAXIMUM_NAME_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_NAME_LENGTH) inclusive, and it should match [SearchApiLimits#FIELD_NAME_PATTERN](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_FIELD_NAME_PATTERN).

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the facet name to check  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the checked facet name  
  
### checkFacetName(String name, String callerContext)
    
    
    public static String checkFacetName(String name, String callerContext)

Checks whether a facet name is valid. The facet name length must be between 1 and [SearchApiLimits#MAXIMUM_NAME_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_NAME_LENGTH) inclusive, and it should match [SearchApiLimits#FIELD_NAME_PATTERN](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_FIELD_NAME_PATTERN).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the facet name to check  
`callerContext` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the caller context used for creating error message in case of a failure.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the checked facet name  
  
### checkFacetValue(DocumentPb.FacetValue value)
    
    
    public static DocumentPb.FacetValue checkFacetValue(DocumentPb.FacetValue value)

Checks whether a facet value is valid.

**Parameter**  
---  
**Name** | **Description**  
`value` | `com.google.apphosting.api.search.DocumentPb.FacetValue`  
the facet value to check  
**Returns**  
---  
**Type** | **Description**  
`com.google.apphosting.api.search.DocumentPb.FacetValue` | the checked facet value  
  
### checkNumber(Double value)
    
    
    public static Double checkNumber(Double value)

Checks whether a number is valid. A number can be null or a value between [SearchApiLimits#MINIMUM_NUMBER_VALUE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MINIMUM_NUMBER_VALUE) and [SearchApiLimits#MAXIMUM_NUMBER_VALUE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_NUMBER_VALUE), inclusive.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)`  
the value to check  
**Returns**  
---  
**Type** | **Description**  
`[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)` | the checked number  
  
### checkValid(DocumentPb.Facet facet)
    
    
    public static DocumentPb.Facet checkValid(DocumentPb.Facet facet)

**Parameter**  
---  
**Name** | **Description**  
`facet` | `com.google.apphosting.api.search.DocumentPb.Facet`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.apphosting.api.search.DocumentPb.Facet` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
