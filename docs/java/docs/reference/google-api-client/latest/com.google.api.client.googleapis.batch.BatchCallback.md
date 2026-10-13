---
url: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.batch.BatchCallback
title: Interface BatchCallback<T,E> (2.9.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:20.031213+00:00
---

# Interface BatchCallback<T,E> (2.9.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.batch.BatchCallback

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BatchCallback<T,E> (2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.1  2.7.2  2.6.0  2.5.1  2.4.1  2.1.2  2.0.1  1.35.2  1.34.1  1.33.4 
    
    
    public interface BatchCallback<T,E>

Callback for an individual batch response.

Sample use:
    
    
     batch.queue(volumesList.buildHttpRequest(), Volumes.class, GoogleJsonErrorContainer.class,
         new BatchCallback<Volumes, GoogleJsonErrorContainer>() {
    
           public void onSuccess(Volumes volumes, HttpHeaders responseHeaders) {
             log("Success");
             printVolumes(volumes.getItems());
           }
    
           public void onFailure(GoogleJsonErrorContainer e, HttpHeaders responseHeaders) {
             log(e.getError().getMessage());
           }
         });
     

## Type Parameters  
  
---  
**Name** | **Description**  
`T` |   
`E` |   
  
## Methods 

### onFailure(E e, HttpHeaders responseHeaders)
    
    
    public abstract void onFailure(E e, HttpHeaders responseHeaders)

Called if the individual batch response is unsuccessful.

**Parameters**  
---  
**Name** | **Description**  
`e` | `E`  
instance of data class representing the error response content  
`responseHeaders` | `com.google.api.client.http.HttpHeaders`  
Headers of the batch response  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### onSuccess(T t, HttpHeaders responseHeaders)
    
    
    public abstract void onSuccess(T t, HttpHeaders responseHeaders)

Called if the individual batch response is successful.

**Parameters**  
---  
**Name** | **Description**  
`t` | `T`  
instance of the parsed data model class  
`responseHeaders` | `com.google.api.client.http.HttpHeaders`  
Headers of the batch response  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
