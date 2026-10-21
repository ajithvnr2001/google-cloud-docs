---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression
title: Class SortExpression (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:43:32.470476+00:00
---

# Class SortExpression (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class SortExpression (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class SortExpression

Sorting specification for a single dimension. Multi-dimensional sorting is supported by a collection of SortExpressions.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SortExpression

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

## Static Fields 

### DOCUMENT_ID_FIELD_NAME
    
    
    public static final String DOCUMENT_ID_FIELD_NAME

The expression to be used if you wish to sort by document id field [Document#getId()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document#com_google_appengine_api_search_Document_getId__). You need to create a sort expression as
    
    
     SortExpression expr = SortExpression.newBuilder()
         .setExpression(SortExpression.DOCUMENT_ID_FIELD_NAME)
         .setDefaultValue("")
         .build();
     

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### LANGUAGE_FIELD_NAME
    
    
    public static final String LANGUAGE_FIELD_NAME

The expression to be used if you wish to sort by language code associated with the locale field [Document#getLocale()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document#com_google_appengine_api_search_Document_getLocale__). You need to create a sort expression as
    
    
     SortExpression expr = SortExpression.newBuilder()
         .setExpression(SortExpression.LANGUAGE_FIELD_NAME)
         .setDefaultValue("")
         .build();
     

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### RANK_FIELD_NAME
    
    
    public static final String RANK_FIELD_NAME

The expression to be used if you wish to sort by rank field. By default, results are sorted in descending value of rank. To sort in ascending order, you need to create a sort expression as
    
    
     SortExpression expr = SortExpression.newBuilder()
         .setExpression(SortExpression.RANK_FIELD_NAME)
         .setDirection(SortExpression.SortDirection.ASCENDING)
         .setDefaultValueNumeric(0)
         .build();
     

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### SCORE_FIELD_NAME
    
    
    public static final String SCORE_FIELD_NAME

The expression to be used if you wish to sort by document score. You need to create a sort expression as
    
    
     SortExpression expr = SortExpression.newBuilder()
         .setExpression(String.format(
             "%s + rating * 0.01", SortExpression.SCORE_FIELD_NAME))
         .setDirection(SortExpression.SortDirection.DESCENDING)
         .setDefaultValueNumeric(0)
         .build();
     

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### TIMESTAMP_FIELD_NAME
    
    
    public static final String TIMESTAMP_FIELD_NAME

The expression to be used if you wish to sort by seconds since EPOCH that the document was written. You need to create a sort expression as
    
    
     SortExpression expr = SortExpression.newBuilder()
         .setExpression(SortExpression.TIMESTAMP_FIELD_NAME)
         .setDefaultValueNumeric(0)
         .build();
     

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### newBuilder()
    
    
    public static SortExpression.Builder newBuilder()

Creates and returns a SortExpression Builder.

**Returns**  
---  
**Type** | **Description**  
`[SortExpression.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder)` | a new [SortExpression.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.Builder). Set the parameters for the sort specification on the Builder, and use the Builder#build() method to create a concrete instance of SortExpression  
  
## Methods 

### getDefaultValue()
    
    
    public String getDefaultValue()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the default value for the field. Can be null  
  
### getDefaultValueDate()
    
    
    public Date getDefaultValueDate()

**Returns**  
---  
**Type** | **Description**  
`[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)` | the default date value for the field. Can be null  
  
### getDefaultValueNumeric()
    
    
    public Double getDefaultValueNumeric()

**Returns**  
---  
**Type** | **Description**  
`[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)` | the default numeric value for the field. Can be null  
  
### getDirection()
    
    
    public SortExpression.SortDirection getDirection()

**Returns**  
---  
**Type** | **Description**  
`[SortExpression.SortDirection](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortExpression.SortDirection)` | the direction to sort the search results in  
  
### getExpression()
    
    
    public String getExpression()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the expression to evaluate for each document and sort by  
  
### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
