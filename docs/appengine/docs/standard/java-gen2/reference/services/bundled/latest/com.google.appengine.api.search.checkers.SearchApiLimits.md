---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits
title: Class SearchApiLimits (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:55:32.342786+00:00
---

# Class SearchApiLimits (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.SearchApiLimits

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class SearchApiLimits (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class SearchApiLimits

Contains limits on field values, document sizes, and other properties of objects in the Search API.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SearchApiLimits

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

### FACET_DEFAULT_DISCOVERY_LIMIT
    
    
    public static final int FACET_DEFAULT_DISCOVERY_LIMIT

The default value for number of discovered facets.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### FACET_MAXIMUM_CONSTRAINTS
    
    
    public static final int FACET_MAXIMUM_CONSTRAINTS

The maximum number of facet value constraint can be requested.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### FACET_MAXIMUM_DEPTH
    
    
    public static final int FACET_MAXIMUM_DEPTH

The maximum number for facet depth option.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### FACET_MAXIMUM_DISCOVERY_LIMIT
    
    
    public static final int FACET_MAXIMUM_DISCOVERY_LIMIT

The maximum number of facet discoveries that can be requested.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### FACET_MAXIMUM_RANGES
    
    
    public static final int FACET_MAXIMUM_RANGES

The maximum number of facet ranges can be requested.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### FACET_MAXIMUM_VALUE_LIMIT
    
    
    public static final int FACET_MAXIMUM_VALUE_LIMIT

The maximum value for facet value limit option.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### FIELD_NAME_PATTERN
    
    
    public static final String FIELD_NAME_PATTERN

The pattern each document field name should match.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### GET_INDEXES_DEFAULT_LIMIT
    
    
    public static final int GET_INDEXES_DEFAULT_LIMIT

The default number of indexes we will try to return.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### GET_INDEXES_MAXIMUM_LIMIT
    
    
    public static final int GET_INDEXES_MAXIMUM_LIMIT

The maximum number of indexes that can be requested to be returned in list indexes results.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### GET_INDEXES_MAXIMUM_OFFSET
    
    
    public static final int GET_INDEXES_MAXIMUM_OFFSET

The maximum offset of the first index returned in list indexes results.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### GET_RANGE_DEFAULT_LIMIT
    
    
    public static final int GET_RANGE_DEFAULT_LIMIT

The default number of documents requested for get range requests.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### GET_RANGE_MAXIMUM_LIMIT
    
    
    public static final int GET_RANGE_MAXIMUM_LIMIT

The maximum number of documents which can be requested for get range requests.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_ATOM_LENGTH
    
    
    public static final int MAXIMUM_ATOM_LENGTH

The maximum length of an atom in bytes (500).

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_CURSOR_LENGTH
    
    
    public static final int MAXIMUM_CURSOR_LENGTH

The maximum length of a cursor.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_DATE_VALUE
    
    
    public static final Date MAXIMUM_DATE_VALUE

The maximum date that can be stored in a date field.

**Field Value**  
---  
**Type** | **Description**  
`[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)` |   
  
### MAXIMUM_DOCUMENT_ID_LENGTH
    
    
    public static final int MAXIMUM_DOCUMENT_ID_LENGTH

The maximum length of a document id.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_DOCUMENT_LENGTH
    
    
    public static final int MAXIMUM_DOCUMENT_LENGTH

The maximum length of a document.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_INDEX_NAME_LENGTH
    
    
    public static final int MAXIMUM_INDEX_NAME_LENGTH

The maximum length for an index name.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_NAME_LENGTH
    
    
    public static final int MAXIMUM_NAME_LENGTH

The maximum length of a field or facet name in bytes (500).

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_NEGATIVE_LATITUDE
    
    
    public static final double MAXIMUM_NEGATIVE_LATITUDE

The maximum negative degrees for latitude.

**Field Value**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_NEGATIVE_LONGITUDE
    
    
    public static final double MAXIMUM_NEGATIVE_LONGITUDE

The maximum negative degrees for longitude.

**Field Value**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_NUMBER_VALUE
    
    
    public static final double MAXIMUM_NUMBER_VALUE

The maximum value that can be stored in a number field (2147483647).

**Field Value**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_POSITIVE_LATITUDE
    
    
    public static final double MAXIMUM_POSITIVE_LATITUDE

The maximum positive degrees for latitude.

**Field Value**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_POSITIVE_LONGITUDE
    
    
    public static final double MAXIMUM_POSITIVE_LONGITUDE

The maximum positive degrees for longitude.

**Field Value**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_PREFIX_LENGTH
    
    
    public static final int MAXIMUM_PREFIX_LENGTH

The maximum length of a prefix field in bytes (500).

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_QUERY_LENGTH
    
    
    public static final int MAXIMUM_QUERY_LENGTH

The maximum length of a query string.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAXIMUM_TEXT_LENGTH
    
    
    public static final int MAXIMUM_TEXT_LENGTH

The maximum length of a text or HTML in bytes (1048576).

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MINIMUM_DATE_VALUE
    
    
    public static final Date MINIMUM_DATE_VALUE

The minimum date that can be stored in a date field.

**Field Value**  
---  
**Type** | **Description**  
`[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)` |   
  
### MINIMUM_NUMBER_VALUE
    
    
    public static final double MINIMUM_NUMBER_VALUE

The minimum value that can be stored in a number field (-2147483647).

**Field Value**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PUT_MAXIMUM_DOCS_PER_REQUEST
    
    
    public static final int PUT_MAXIMUM_DOCS_PER_REQUEST

The maximum number of documents allowed per index and delete request.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SEARCH_DEFAULT_LIMIT
    
    
    public static final int SEARCH_DEFAULT_LIMIT

The default limit on the number of documents to return in results.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SEARCH_DEFAULT_NUMBER_FOUND_ACCURACY
    
    
    public static final int SEARCH_DEFAULT_NUMBER_FOUND_ACCURACY

The default found count accuracy is the limit.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SEARCH_DEFAULT_SORTED_LIMIT
    
    
    public static final int SEARCH_DEFAULT_SORTED_LIMIT

The default number of documents to score.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SEARCH_MAXIMUM_LIMIT
    
    
    public static final int SEARCH_MAXIMUM_LIMIT

The maximum number of documents that can be requested to be returned in search results.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SEARCH_MAXIMUM_NUMBER_FOUND_ACCURACY
    
    
    public static final int SEARCH_MAXIMUM_NUMBER_FOUND_ACCURACY

The maximum number found accuracy that can be requested.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SEARCH_MAXIMUM_NUMBER_OF_FIELDS_TO_RETURN
    
    
    public static final int SEARCH_MAXIMUM_NUMBER_OF_FIELDS_TO_RETURN

The maximum number of names of fields to return in results.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SEARCH_MAXIMUM_OFFSET
    
    
    public static final int SEARCH_MAXIMUM_OFFSET

The maximum offset into all search results to return results from.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SEARCH_MAXIMUM_SORTED_LIMIT
    
    
    public static final int SEARCH_MAXIMUM_SORTED_LIMIT

The maximum number of documents that can be requested to be scored.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### VECTOR_FIELD_MAX_SIZE
    
    
    public static final int VECTOR_FIELD_MAX_SIZE

The maximum size of a vector field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
