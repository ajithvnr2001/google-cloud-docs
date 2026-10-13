---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.stub.GkeInferenceQuickstartStub
title: Class GkeInferenceQuickstartStub (0.19.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:31.829121+00:00
---

# Class GkeInferenceQuickstartStub (0.19.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.stub.GkeInferenceQuickstartStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GkeInferenceQuickstartStub (0.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.0 (latest)  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public abstract class GkeInferenceQuickstartStub implements BackgroundResource

Base stub class for the GkeInferenceQuickstart service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GkeInferenceQuickstartStub

## Implements

[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource.html)

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

## Constructors 

### GkeInferenceQuickstartStub()
    
    
    public GkeInferenceQuickstartStub()

## Methods 

### close()
    
    
    public abstract void close()

### fetchBenchmarkingDataCallable()
    
    
    public UnaryCallable<FetchBenchmarkingDataRequest,FetchBenchmarkingDataResponse> fetchBenchmarkingDataCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchBenchmarkingDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchBenchmarkingDataRequest),[FetchBenchmarkingDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchBenchmarkingDataResponse)>` |   
  
### fetchModelServerVersionsCallable()
    
    
    public UnaryCallable<FetchModelServerVersionsRequest,FetchModelServerVersionsResponse> fetchModelServerVersionsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchModelServerVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchModelServerVersionsRequest),[FetchModelServerVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchModelServerVersionsResponse)>` |   
  
### fetchModelServerVersionsPagedCallable()
    
    
    public UnaryCallable<FetchModelServerVersionsRequest,GkeInferenceQuickstartClient.FetchModelServerVersionsPagedResponse> fetchModelServerVersionsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchModelServerVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchModelServerVersionsRequest),[FetchModelServerVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.GkeInferenceQuickstartClient.FetchModelServerVersionsPagedResponse)>` |   
  
### fetchModelServersCallable()
    
    
    public UnaryCallable<FetchModelServersRequest,FetchModelServersResponse> fetchModelServersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchModelServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchModelServersRequest),[FetchModelServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchModelServersResponse)>` |   
  
### fetchModelServersPagedCallable()
    
    
    public UnaryCallable<FetchModelServersRequest,GkeInferenceQuickstartClient.FetchModelServersPagedResponse> fetchModelServersPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchModelServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchModelServersRequest),[FetchModelServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.GkeInferenceQuickstartClient.FetchModelServersPagedResponse)>` |   
  
### fetchModelsCallable()
    
    
    public UnaryCallable<FetchModelsRequest,FetchModelsResponse> fetchModelsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchModelsRequest),[FetchModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchModelsResponse)>` |   
  
### fetchModelsPagedCallable()
    
    
    public UnaryCallable<FetchModelsRequest,GkeInferenceQuickstartClient.FetchModelsPagedResponse> fetchModelsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchModelsRequest),[FetchModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.GkeInferenceQuickstartClient.FetchModelsPagedResponse)>` |   
  
### fetchProfilesCallable()
    
    
    public UnaryCallable<FetchProfilesRequest,FetchProfilesResponse> fetchProfilesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchProfilesRequest),[FetchProfilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchProfilesResponse)>` |   
  
### fetchProfilesPagedCallable()
    
    
    public UnaryCallable<FetchProfilesRequest,GkeInferenceQuickstartClient.FetchProfilesPagedResponse> fetchProfilesPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.FetchProfilesRequest),[FetchProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.GkeInferenceQuickstartClient.FetchProfilesPagedResponse)>` |   
  
### generateOptimizedManifestCallable()
    
    
    public UnaryCallable<GenerateOptimizedManifestRequest,GenerateOptimizedManifestResponse> generateOptimizedManifestCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateOptimizedManifestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.GenerateOptimizedManifestRequest),[GenerateOptimizedManifestResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.GenerateOptimizedManifestResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
