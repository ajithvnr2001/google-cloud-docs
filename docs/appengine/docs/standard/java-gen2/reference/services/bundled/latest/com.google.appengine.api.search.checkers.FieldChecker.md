---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.FieldChecker
title: Class FieldChecker (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:45:30.011795+00:00
---

# Class FieldChecker (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.FieldChecker

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class FieldChecker (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class FieldChecker

Provides checks for Field names, language code, and values: text, HTML, atom or date.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FieldChecker

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

### checkAtom(String atom)
    
    
    public static String checkAtom(String atom)

Checks whether an atom is valid. An atom can be null or a string between 1 and SearchApiLimits.MAXIMUM_ATOM_LENGTH in length.

**Parameter**  
---  
**Name** | **Description**  
`atom` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the atom to check  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the checked atom  
  
### checkDate(Date date)
    
    
    public static Date checkDate(Date date)

Checks whether a date is within range. Date is nullable.

**Parameter**  
---  
**Name** | **Description**  
`date` | `[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)`  
the date to check  
**Returns**  
---  
**Type** | **Description**  
`[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)` | the checked date  
**Exceptions**  
---  
**Type** | **Description**  
`[IllegalArgumentException](https://docs.oracle.com/javase/8/docs/api/java/lang/IllegalArgumentException.html)` | if date is out of range  
  
### checkExpression(String expression)
    
    
    public static String checkExpression(String expression)

Checks whether a field expression is not null and is parsable.

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the expression to check  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the checked expression  
  
### checkFieldName(String name)
    
    
    public static String checkFieldName(String name)

Checks whether a field name is valid. The field name length must be between 1 and [SearchApiLimits#MAXIMUM_NAME_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_NAME_LENGTH) and it should match [SearchApiLimits#FIELD_NAME_PATTERN](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_FIELD_NAME_PATTERN).

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the field name to check  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the checked field name  
  
### checkFieldName(String name, String fieldName)
    
    
    public static String checkFieldName(String name, String fieldName)

Checks whether a field name is valid. The field name length must be between 1 and [SearchApiLimits#MAXIMUM_NAME_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_MAXIMUM_NAME_LENGTH) and it should match [SearchApiLimits#FIELD_NAME_PATTERN](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits#com_google_appengine_api_search_checkers_SearchApiLimits_FIELD_NAME_PATTERN).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the field name to check  
`fieldName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the Java field name of the class where name is checked  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the checked field name  
  
### checkHTML(String html)
    
    
    public static String checkHTML(String html)

Checks whether a html is valid. A html can be null or a string between 0 and SearchApiLimits.MAXIMUM_TEXT_LENGTH in length.

**Parameter**  
---  
**Name** | **Description**  
`html` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the html to check  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the checked html  
  
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
  
### checkPrefix(String prefix)
    
    
    public static String checkPrefix(String prefix)

Checks whether a prefix field is valid. A prefix field can be null or a string between 1 and SearchApiLimits.MAXIMUM_PREFIX_LENGTH in length.

**Parameter**  
---  
**Name** | **Description**  
`prefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the prefix to check  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the checked prefix  
  
### checkSortExpression(String expression)
    
    
    public static String checkSortExpression(String expression)

Checks whether a sort bexpression is not null and is parsable.

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the expression to check  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the checked expression  
  
### checkText(String text)
    
    
    public static String checkText(String text)

Checks whether a text is valid. A text can be null, or a string between 0 and SearchApiLimits.MAXIMUM_TEXT_LENGTH in length.

**Parameter**  
---  
**Name** | **Description**  
`text` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the text to check  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the checked text  
  
### checkValid(DocumentPb.Field field)
    
    
    public static DocumentPb.Field checkValid(DocumentPb.Field field)

**Parameter**  
---  
**Name** | **Description**  
`field` | `com.google.apphosting.api.search.DocumentPb.Field`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.apphosting.api.search.DocumentPb.Field` |   
  
### checkVector(List<Double> vector)
    
    
    public static List<Double> checkVector(List<Double> vector)

Checks whether a vector field is valid. A vector field can be an array of any number with size less than SearchApiLimits.VECTOR_FIELD_MAX_SIZE.

**Parameter**  
---  
**Name** | **Description**  
`vector` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)>`  
the vector to check  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)>` |   
  
### parseLocale(String locale)
    
    
    public static Locale parseLocale(String locale)

Returns a [Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html) parsed from the given locale string.

**Parameter**  
---  
**Name** | **Description**  
`locale` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
a string representation of a [Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html)  
**Returns**  
---  
**Type** | **Description**  
`[Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html)` | a [Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html) parsed from the given locale string  
  
## Constructors 

### FieldChecker()
    
    
    public FieldChecker()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
