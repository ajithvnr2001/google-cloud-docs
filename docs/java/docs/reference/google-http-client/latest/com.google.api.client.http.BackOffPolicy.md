---
url: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.BackOffPolicy
title: Interface BackOffPolicy (2.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:56.989289+00:00
---

# Interface BackOffPolicy (2.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.BackOffPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BackOffPolicy (2.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.0 (latest)  2.1.1  2.0.3  1.47.1  1.46.3  1.45.3  1.44.2  1.43.2  1.42.3  1.41.8 
    
    
    public interface BackOffPolicy

**Deprecated.** _(scheduled to be removed in 1.18) Use[HttpBackOffUnsuccessfulResponseHandler](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpBackOffUnsuccessfulResponseHandler) instead._

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
Strategy interface to control back off between retry attempts.

## Static Fields 

### STOP (deprecated)
    
    
    public static final long STOP

Value indicating that no more retries should be made, see [#getNextBackOffMillis()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.BackOffPolicy#com_google_api_client_http_BackOffPolicy_getNextBackOffMillis__).

**Field Value**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Methods 

### getNextBackOffMillis() (deprecated)
    
    
    public abstract long getNextBackOffMillis()

Gets the number of milliseconds to wait before retrying an HTTP request. If [#STOP](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.BackOffPolicy#com_google_api_client_http_BackOffPolicy_STOP) is returned, no retries should be made.

This method should be used as follows:

long backoffTime = backoffPolicy.getNextBackoffMs(); if (backoffTime == BackoffPolicy.STOP) { // Stop retrying. } else { // Retry after backoffTime. }

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the number of milliseconds to wait when backing off requests, or [#STOP](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.BackOffPolicy#com_google_api_client_http_BackOffPolicy_STOP) if no more retries should be made  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### isBackOffRequired(int statusCode) (deprecated)
    
    
    public abstract boolean isBackOffRequired(int statusCode)

Determines if back off is required based on the specified status code.

Implementations may want to back off on server or product-specific errors.

**Parameter**  
---  
**Name** | **Description**  
`statusCode` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
HTTP status code  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### reset() (deprecated)
    
    
    public abstract void reset()

Reset Back off counters (if any) in an implementation-specific fashion.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
