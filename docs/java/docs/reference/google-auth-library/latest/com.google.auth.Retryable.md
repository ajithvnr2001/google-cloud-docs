---
url: https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Retryable
title: Interface Retryable (1.54.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:39.526944+00:00
---

# Interface Retryable (1.54.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.Retryable

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Retryable (1.54.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.54.0 (latest)  1.50.0  1.49.0  1.48.0  1.46.0  1.43.0  1.42.1  1.41.0  1.40.0  1.39.1  1.38.0  1.37.1  1.36.0  1.35.0  1.34.0  1.33.1  1.32.1  1.31.0  1.30.1  1.29.1-SNAPSHOT  1.28.0  1.27.0  1.26.0  1.25.0  1.24.1  1.20.0  1.19.0  1.18.0  1.7.0  1.6.1  1.4.0  1.3.0 
    
    
    public interface Retryable

## Methods 

### getRetryCount()
    
    
    public abstract int getRetryCount()

Gets a number of performed retries for related HttpRequest

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | a number of performed retries  
  
### isRetryable()
    
    
    public abstract boolean isRetryable()

A flag indicating whether the error is retryable

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true if related error is retryable, false otherwise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
