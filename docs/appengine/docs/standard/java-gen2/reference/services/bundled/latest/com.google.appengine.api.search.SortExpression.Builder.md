---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder
title: Class SortExpression.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:30:53.050981+00:00
---

# Class SortExpression.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class SortExpression.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class SortExpression.Builder

A builder that constructs [SortExpressions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression). The user must provide an expression. The expression can be as simple as a field name, or can be some other expression such as `"score + count(likes) * 0.1"`, which combines a scorer score with a count of the number of likes values times 0.1. A default value must be specified for the expression. 
    
    
       SortExpression expr = SortExpression.newBuilder()
           .setExpression(String.format(
               "%s + count(likes) * 0.1", SortExpression.SCORE_FIELD_NAME))
           .setDirection(SortExpression.SortDirection.ASCENDING)
           .setDefaultValueNumeric(0.0)
           .build()
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SortExpression.Builder

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

### build()
    
    
    public SortExpression build()

Builds a [SortExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression) from the set values.

**Returns**  
---  
**Type** | **Description**  
`[SortExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression)` | a [SortExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression) built from the set values  
  
### setDefaultValue(String defaultValue)
    
    
    public SortExpression.Builder setDefaultValue(String defaultValue)

Sets the default value for the field for sorting purposes. Must provide for text sorts.

**Parameter**  
---  
**Name** | **Description**  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the default value for the field  
**Returns**  
---  
**Type** | **Description**  
`[SortExpression.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder)` | this Builder  
  
### setDefaultValueDate(Date defaultValue)
    
    
    public SortExpression.Builder setDefaultValueDate(Date defaultValue)

Sets the default value for the field for sorting purposes. Must provide for Date sorts. Typically, you should use [com.google.appengine.api.search.checkers.SearchApiLimits#MINIMUM_DATE_VALUE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MINIMUM_DATE_VALUE) or [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_DATE_VALUE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_DATE_VALUE) as a default value.

**Parameter**  
---  
**Name** | **Description**  
`defaultValue` | `[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)`  
the default value for the field  
**Returns**  
---  
**Type** | **Description**  
`[SortExpression.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder)` | this Builder  
  
### setDefaultValueNumeric(double defaultValue)
    
    
    public SortExpression.Builder setDefaultValueNumeric(double defaultValue)

Sets the default value for the field for sorting purposes. Must provide for numeric sorts.

**Parameter**  
---  
**Name** | **Description**  
`defaultValue` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the default value for the field  
**Returns**  
---  
**Type** | **Description**  
`[SortExpression.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder)` | this Builder  
  
### setDirection(SortExpression.SortDirection direction)
    
    
    public SortExpression.Builder setDirection(SortExpression.SortDirection direction)

Sets the direction to sort the search results in.

**Parameter**  
---  
**Name** | **Description**  
`direction` | `[SortExpression.SortDirection](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.SortDirection)`  
the direction to sort the search results in. The default direction is SortDirection#DESCENDING  
**Returns**  
---  
**Type** | **Description**  
`[SortExpression.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder)` | this Builder  
  
### setExpression(String expression)
    
    
    public SortExpression.Builder setExpression(String expression)

Sets an expression to be evaluated for each document to sort by. A default string value [#setDefaultValue(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder#com_google_appengine_api_search_SortExpression_Builder_setDefaultValue_java_lang_String_) or numeric [#setDefaultValueNumeric(double)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder#com_google_appengine_api_search_SortExpression_Builder_setDefaultValueNumeric_double_) or date [#setDefaultValueDate(Date)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder#com_google_appengine_api_search_SortExpression_Builder_setDefaultValueDate_java_util_Date_) must be specified for the expression.

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the expression to evaluate for each document to sort by  
**Returns**  
---  
**Type** | **Description**  
`[SortExpression.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder)` | this Builder  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
