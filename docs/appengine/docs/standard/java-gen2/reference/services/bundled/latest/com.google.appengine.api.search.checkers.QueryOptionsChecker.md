---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.QueryOptionsChecker
title: Class QueryOptionsChecker (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:35:47.640652+00:00
---

# Class QueryOptionsChecker (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.checkers.QueryOptionsChecker

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class QueryOptionsChecker (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class QueryOptionsChecker

Checks values of [com.google.appengine.api.search.QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > QueryOptionsChecker

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

### checkFieldNames(List<String> fieldNames)
    
    
    public static List<String> checkFieldNames(List<String> fieldNames)

Checks that there are at most

# MAXIMUM_NUMBER_OF_FIELDS_TO_RETURN field names and

that each field name is valid.

**Parameter**  
---  
**Name** | **Description**  
`fieldNames` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
the list of field names to check  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | the checked list of field names  
  
### checkLimit(int limit)
    
    
    public static int checkLimit(int limit)

Checks whether the number of documents to return is between 1 and the maximum.

**Parameter**  
---  
**Name** | **Description**  
`limit` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the maximum number of documents to return in search results  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the checked number of documents to return  
  
### checkNumberFoundAccuracy(int numberFoundAccuracy)
    
    
    public static int checkNumberFoundAccuracy(int numberFoundAccuracy)

Checks whether the minimum number of documents found accuracy is between 1 and the maximum.

**Parameter**  
---  
**Name** | **Description**  
`numberFoundAccuracy` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the minimum number of documents found accuracy  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the checked accuracy  
  
### checkOffset(Integer offset)
    
    
    public static Integer checkOffset(Integer offset)

Checks whether the offset is between 0 and the maximum. Can be null.

**Parameter**  
---  
**Name** | **Description**  
`offset` | `[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)`  
the offset of the first result to return results  
**Returns**  
---  
**Type** | **Description**  
`[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)` | the checked offset of the first result to return  
  
### checkValid(SearchServicePb.SearchParams params)
    
    
    public static SearchServicePb.SearchParams checkValid(SearchServicePb.SearchParams params)

Checks the search options are valid, specifically, has a non-null number of documents to return specification, a valid cursor if present, valid sort specification list, a valid collection of field names for sorting, and a valid scorer specification.

**Parameter**  
---  
**Name** | **Description**  
`params` | `com.google.appengine.api.search.proto.SearchServicePb.SearchParams`  
the SearchParams to check  
**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.search.proto.SearchServicePb.SearchParams` | this checked SearchParams  
  
## Constructors 

### QueryOptionsChecker()
    
    
    public QueryOptionsChecker()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
