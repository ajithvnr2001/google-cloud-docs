---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.stub.LanguageServiceStub
title: Class LanguageServiceStub (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:46:05.293967+00:00
---

# Class LanguageServiceStub (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.stub.LanguageServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LanguageServiceStub (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.1  2.3.4  2.2.0  2.1.10 
    
    
    public abstract class LanguageServiceStub implements BackgroundResource

Base stub class for the LanguageService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LanguageServiceStub

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

### LanguageServiceStub()
    
    
    public LanguageServiceStub()

## Methods 

### analyzeEntitiesCallable()
    
    
    public UnaryCallable<AnalyzeEntitiesRequest,AnalyzeEntitiesResponse> analyzeEntitiesCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AnalyzeEntitiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeEntitiesRequest),[AnalyzeEntitiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeEntitiesResponse)>` |   
  
### analyzeSentimentCallable()
    
    
    public UnaryCallable<AnalyzeSentimentRequest,AnalyzeSentimentResponse> analyzeSentimentCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AnalyzeSentimentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeSentimentRequest),[AnalyzeSentimentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeSentimentResponse)>` |   
  
### annotateTextCallable()
    
    
    public UnaryCallable<AnnotateTextRequest,AnnotateTextResponse> annotateTextCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AnnotateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnnotateTextRequest),[AnnotateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnnotateTextResponse)>` |   
  
### classifyTextCallable()
    
    
    public UnaryCallable<ClassifyTextRequest,ClassifyTextResponse> classifyTextCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ClassifyTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ClassifyTextRequest),[ClassifyTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ClassifyTextResponse)>` |   
  
### close()
    
    
    public abstract void close()

### moderateTextCallable()
    
    
    public UnaryCallable<ModerateTextRequest,ModerateTextResponse> moderateTextCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ModerateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ModerateTextRequest),[ModerateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ModerateTextResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
