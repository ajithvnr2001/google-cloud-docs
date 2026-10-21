---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder
title: Class Field.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:29:25.168407+00:00
---

# Class Field.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Field.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class Field.Builder

A field builder. Fields must have a name, and optionally a locale and at most one of text, html, atom or date.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Field.Builder

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
    
    
    public Field build()

Builds a field using this builder. The field must have a valid name, string value, type.

**Returns**  
---  
**Type** | **Description**  
`[Field](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field)` | a [Field](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field) built by this builder  
  
### setAtom(String atom)
    
    
    public Field.Builder setAtom(String atom)

Sets an atomic value, indivisible text, for the field.

**Parameter**  
---  
**Name** | **Description**  
`atom` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the indivisible text of the field  
**Returns**  
---  
**Type** | **Description**  
`[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)` | this builder  
  
### setDate(Date date)
    
    
    public Field.Builder setDate(Date date)

Sets a date associated with the field.

**Parameter**  
---  
**Name** | **Description**  
`date` | `[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)`  
the date of the field  
**Returns**  
---  
**Type** | **Description**  
`[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)` | this builder  
  
### setGeoPoint(GeoPoint geoPoint)
    
    
    public Field.Builder setGeoPoint(GeoPoint geoPoint)

Sets a [GeoPoint](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GeoPoint) value for the field.

**Parameter**  
---  
**Name** | **Description**  
`geoPoint` | `[GeoPoint](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GeoPoint)`  
the [GeoPoint](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GeoPoint) value of the field  
**Returns**  
---  
**Type** | **Description**  
`[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)` | this builder  
  
### setHTML(String html)
    
    
    public Field.Builder setHTML(String html)

Sets a HTML value for the field.

**Parameter**  
---  
**Name** | **Description**  
`html` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the HTML value of the field  
**Returns**  
---  
**Type** | **Description**  
`[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)` | this builder  
  
### setLocale(Locale locale)
    
    
    public Field.Builder setLocale(Locale locale)

Sets the Locale of the field value. If none is given, then the locale of the document will be used.

**Parameter**  
---  
**Name** | **Description**  
`locale` | `[Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html)`  
the locale the field value is written in  
**Returns**  
---  
**Type** | **Description**  
`[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)` | this builder  
  
### setName(String name)
    
    
    public Field.Builder setName(String name)

Sets a name for the field. The field name length must be between 1 and FieldChecker#MAXIMUM_NAME_LENGTH and it should match [com.google.appengine.api.search.checkers.SearchApiLimits#FIELD_NAME_PATTERN](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_FIELD_NAME_PATTERN).

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the field  
**Returns**  
---  
**Type** | **Description**  
`[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)` | this builder  
  
### setNumber(double number)
    
    
    public Field.Builder setNumber(double number)

Sets a numeric value for the field. The `number` must be between [com.google.appengine.api.search.checkers.SearchApiLimits#MINIMUM_NUMBER_VALUE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MINIMUM_NUMBER_VALUE) and [com.google.appengine.api.search.checkers.SearchApiLimits#MAXIMUM_NUMBER_VALUE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_NUMBER_VALUE).

**Parameter**  
---  
**Name** | **Description**  
`number` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the numeric value of the field  
**Returns**  
---  
**Type** | **Description**  
`[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)` | this builder  
  
### setText(String text)
    
    
    public Field.Builder setText(String text)

Sets a text value for the field.

**Parameter**  
---  
**Name** | **Description**  
`text` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the text value of the field  
**Returns**  
---  
**Type** | **Description**  
`[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)` | this builder  
  
### setTokenizedPrefix(String tokenizedPrefix)
    
    
    public Field.Builder setTokenizedPrefix(String tokenizedPrefix)

Sets a tokenized prefix value for the field.

**Parameter**  
---  
**Name** | **Description**  
`tokenizedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the string value of the field  
**Returns**  
---  
**Type** | **Description**  
`[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)` | this builder  
  
### setUntokenizedPrefix(String untokenizedPrefix)
    
    
    public Field.Builder setUntokenizedPrefix(String untokenizedPrefix)

Sets an untokenized prefix value for the field.

**Parameter**  
---  
**Name** | **Description**  
`untokenizedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the string value of the field  
**Returns**  
---  
**Type** | **Description**  
`[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)` | this builder  
  
### setVector(List<Double> vector)
    
    
    public Field.Builder setVector(List<Double> vector)

Sets a vector value for the field.

**Parameter**  
---  
**Name** | **Description**  
`vector` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)>`  
a list of Double values forming a vector field value  
**Returns**  
---  
**Type** | **Description**  
`[Field.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.Builder)` | this builder  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
