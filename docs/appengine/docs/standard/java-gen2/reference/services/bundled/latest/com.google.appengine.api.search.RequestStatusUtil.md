---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RequestStatusUtil
title: Class RequestStatusUtil (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:10:03.563859+00:00
---

# Class RequestStatusUtil (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.RequestStatusUtil

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class RequestStatusUtil (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class RequestStatusUtil

Collection of utility methods for SearchServicePb.RequestStatus.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RequestStatusUtil

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

### newInvalidRequestStatus(IllegalArgumentException e)
    
    
    public static SearchServicePb.RequestStatus newInvalidRequestStatus(IllegalArgumentException e)

Creates a RequestStatus message suitable for reporting an invalid request.

**Parameter**  
---  
**Name** | **Description**  
`e` | `[IllegalArgumentException](https://docs.oracle.com/javase/8/docs/api/java/lang/IllegalArgumentException.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.search.proto.SearchServicePb.RequestStatus` |   
  
### newStatus(SearchServicePb.SearchServiceError.ErrorCode code)
    
    
    public static SearchServicePb.RequestStatus newStatus(SearchServicePb.SearchServiceError.ErrorCode code)

Creates a SearchServicePb.RequestStatus from the given code.

**Parameter**  
---  
**Name** | **Description**  
`code` | `com.google.appengine.api.search.proto.SearchServicePb.SearchServiceError.ErrorCode`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.search.proto.SearchServicePb.RequestStatus` |   
  
### newStatus(SearchServicePb.SearchServiceError.ErrorCode code, String message)
    
    
    public static SearchServicePb.RequestStatus newStatus(SearchServicePb.SearchServiceError.ErrorCode code, String message)

Creates a SearchServicePb.RequestStatus from the given code and message.

**Parameters**  
---  
**Name** | **Description**  
`code` | `com.google.appengine.api.search.proto.SearchServicePb.SearchServiceError.ErrorCode`  
  
`message` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.search.proto.SearchServicePb.RequestStatus` |   
  
### newStatusBuilder(SearchServicePb.SearchServiceError.ErrorCode code, String message)
    
    
    public static SearchServicePb.RequestStatus.Builder newStatusBuilder(SearchServicePb.SearchServiceError.ErrorCode code, String message)

Creates a SearchServicePb.RequestStatus.Builder from the given code and message.

**Parameters**  
---  
**Name** | **Description**  
`code` | `com.google.appengine.api.search.proto.SearchServicePb.SearchServiceError.ErrorCode`  
  
`message` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.search.proto.SearchServicePb.RequestStatus.Builder` |   
  
### newUnknownIndexStatus(SearchServicePb.IndexSpec indexSpec)
    
    
    public static SearchServicePb.RequestStatus newUnknownIndexStatus(SearchServicePb.IndexSpec indexSpec)

Creates a RequestStatus message suitable for reporting an unknown index. We use SearchServicePb.SearchServiceError.ErrorCode#OK because the unknown index isn't an error condition but just a notice to the user.

**Parameter**  
---  
**Name** | **Description**  
`indexSpec` | `com.google.appengine.api.search.proto.SearchServicePb.IndexSpec`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.search.proto.SearchServicePb.RequestStatus` |   
  
### reduce(Collection<SearchServicePb.RequestStatus> statuses)
    
    
    public static SearchServicePb.RequestStatus reduce(Collection<SearchServicePb.RequestStatus> statuses)

For a 'batch' request, determines a single status to stand for all. Code will be OK if and only if the collection contains no non-OK statuses.

If the collection is empty, the result will be an OK status with no detail.

If the collection has one element, the result will be that element.

If the collection has multiple elements with the same error code, the result will have that error code and the corresponding canonical code.

If there are multiple error statuses in the collection, the one with the highest numerical code in the ErrorCode enum will be chosen as representative, and the errorDetail field of the result will contain at least the errorDetail of that status.

**Parameter**  
---  
**Name** | **Description**  
`statuses` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<com.google.appengine.api.search.proto.SearchServicePb.RequestStatus>`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.search.proto.SearchServicePb.RequestStatus` |   
  
### toCanonicalCode(SearchServicePb.SearchServiceError.ErrorCode appCode)
    
    
    public static Codes.Code toCanonicalCode(SearchServicePb.SearchServiceError.ErrorCode appCode)

Converts SearchServicePb.SearchServiceError.ErrorCode to canonical error code.

**Parameter**  
---  
**Name** | **Description**  
`appCode` | `com.google.appengine.api.search.proto.SearchServicePb.SearchServiceError.ErrorCode`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.apphosting.base.protos.Codes.Code` |   
  
## Constructors 

### RequestStatusUtil()
    
    
    public RequestStatusUtil()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
