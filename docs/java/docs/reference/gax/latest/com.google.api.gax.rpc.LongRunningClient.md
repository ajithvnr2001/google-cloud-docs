---
url: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LongRunningClient
title: Interface LongRunningClient (2.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:59.069480+00:00
---

# Interface LongRunningClient (2.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LongRunningClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LongRunningClient (2.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.87.0 (latest)  2.83.0  2.82.0  2.81.0  2.80.0  2.79.0  2.76.0  2.75.0  2.74.1  2.73.1  2.72.2  2.71.0  2.70.3  2.69.0  2.68.2  2.67.0  2.66.0  2.65.0  2.63.1  2.62.0  2.61.0  2.60.0  2.59.1  2.58.0  2.57.0  2.55.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.1  2.47.0  2.46.1  2.45.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.1  2.33.0  2.32.1  2.31.1  2.30.1  2.24.0  2.23.3  2.22.0  2.21.0  2.20.1  2.19.6  2.18.7  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.2  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1 
    
    
    public interface LongRunningClient

Implementation-agnostic interface for managing long-running operations.

## Methods 

### cancelOperationCallable()
    
    
    public abstract UnaryCallable<String,Void> cancelOperationCallable()

Returns a [UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable) which can issue calls to cancel an operation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### deleteOperationCallable()
    
    
    public abstract UnaryCallable<String,Void> deleteOperationCallable()

Returns a [UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable) which can issue calls to delete an operation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### getOperationCallable()
    
    
    public abstract UnaryCallable<String,OperationSnapshot> getOperationCallable()

Returns a [UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable) which can issue calls to get the latest state of an operation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[OperationSnapshot](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationSnapshot)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
