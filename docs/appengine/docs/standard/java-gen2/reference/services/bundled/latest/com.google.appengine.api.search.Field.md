---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field
title: Class Field (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:15:44.571301+00:00
---

# Class Field (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Field (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class Field implements Serializable

Represents a field of a [Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document), which is a name, an optional locale, and at most one value: text, HTML, atom, date, GeoPoint, untokenizedPrefix, tokenizedPrefix or vector. Field name lengths are between 1 and [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_NAME_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_NAME_LENGTH) characters, and text and HTML values are limited to [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_TEXT_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_TEXT_LENGTH). Atoms are limited to [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_ATOM_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_ATOM_LENGTH) characters, both prefix types are limited to [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_PREFIX_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_PREFIX_LENGTH) . Vector field size is limited to [com.google.appengine.api.search.checkers.SearchApiLimits#VECTOR_FIELD_MAX_SIZE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_VECTOR_FIELD_MAX_SIZE) and dates must not have a time component.

There are 5 types of text fields, ATOM, TEXT, HTML, UNTOKENIZED_PREFIX, and TOKENIZED_PREFIX. Atom fields when queried, are checked for equality. For example, if you add a field with name `code` and an ATOM value of "928A 33B-1", then query `code:"928A 33B-1"` would match the document with this field, while query `code:928A` would not. TEXT fields, unlike ATOM, match both on equality or if any token extracted from the original field matches. Thus if `code` field had the value set with [Field.Builder#setText(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder#com_google_appengine_api_search_Field_Builder_setText_java_lang_String_) method, both queries would match. HTML fields have HTML tags stripped before tokenization. Untokenized prefix fields match queries that are prefixes containing the contiguous starting characters of the whole field. For example if the field was "the quick brown fox", the query "the qui" would match whereas "th qui" would not. On the other hand, Tokenized prefix fields match if the query terms are prefixes of individual terms in the field. If the query is a phrase of terms, the ordering of the terms will matter. For example if the field is "the quick brown fox", the query "th qui bro" would match whereas "bro qui the" would not. Vector fields are only used to compute the dot product between a given constant vector and the provided vector field for sorting and field expressions only. for example, if a 3d vector is named "scores" and has a value of (1,2,3) then the expression `dot(scores, vector(3,2,1))` will be evaluated to 10.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Field

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

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

### newBuilder()
    
    
    public static Field.Builder newBuilder()

Creates a field builder.

**Returns**  
---  
**Type** | **Description**  
`[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)` | a new builder for creating fields  
  
## Methods 

### equals(Object object)
    
    
    public boolean equals(Object object)

**Parameter**  
---  
**Name** | **Description**  
`object` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getAtom()
    
    
    public String getAtom()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the atomic value of the field. Can be null  
  
### getDate()
    
    
    public Date getDate()

**Returns**  
---  
**Type** | **Description**  
`[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)` | the date value of the field. Can be null  
  
### getGeoPoint()
    
    
    public GeoPoint getGeoPoint()

**Returns**  
---  
**Type** | **Description**  
`[GeoPoint](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GeoPoint)` | the [GeoPoint](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GeoPoint) value of the field. Can be null  
  
### getHTML()
    
    
    public String getHTML()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the HTML value of the field. Can be null  
  
### getLocale()
    
    
    public Locale getLocale()

**Returns**  
---  
**Type** | **Description**  
`[Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html)` | the locale the field value is written in. Can be null. If none is given the locale of the document will be used  
  
### getName()
    
    
    public String getName()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the name of the field  
  
### getNumber()
    
    
    public Double getNumber()

**Returns**  
---  
**Type** | **Description**  
`[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)` | the numeric value of the field. Can be null  
  
### getText()
    
    
    public String getText()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the text value of the field. Can be null  
  
### getTokenizedPrefix()
    
    
    public String getTokenizedPrefix()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the String value of the tokenized prefix field. Can be null  
  
### getType()
    
    
    public Field.FieldType getType()

**Returns**  
---  
**Type** | **Description**  
`[Field.FieldType](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.FieldType)` | the type of value of the field. Can be null  
  
### getUntokenizedPrefix()
    
    
    public String getUntokenizedPrefix()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the String value of the untokenized prefix field. Can be null  
  
### getVector()
    
    
    public List<Double> getVector()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)>` | the vector value of the field.  
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

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
