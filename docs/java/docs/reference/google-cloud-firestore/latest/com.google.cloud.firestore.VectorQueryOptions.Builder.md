---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.VectorQueryOptions.Builder
title: Class VectorQueryOptions.Builder (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:45.131293+00:00
---

# Class VectorQueryOptions.Builder (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.VectorQueryOptions.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VectorQueryOptions.Builder (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 
    
    
    public static final class VectorQueryOptions.Builder

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > VectorQueryOptions.Builder

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

## Methods 

### build()
    
    
    public VectorQueryOptions build()

**Returns**  
---  
**Type** | **Description**  
`[VectorQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.VectorQueryOptions)` |   
  
### setDistanceResultField(FieldPath fieldPath)
    
    
    public VectorQueryOptions.Builder setDistanceResultField(FieldPath fieldPath)

Specifies the name of the field that will be set on each returned DocumentSnapshot, which will contain the computed distance for the document. If `null`, then the computed distance will not be returned. Default value: `null`.

**Parameter**  
---  
**Name** | **Description**  
`fieldPath` | `[FieldPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FieldPath)`  
A [FieldPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FieldPath) value specifying the distance result field.  
**Returns**  
---  
**Type** | **Description**  
`[VectorQueryOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.VectorQueryOptions.Builder)` |   
  
### setDistanceResultField(String fieldPath)
    
    
    public VectorQueryOptions.Builder setDistanceResultField(String fieldPath)

Specifies the name of the field that will be set on each returned DocumentSnapshot, which will contain the computed distance for the document. If `null`, then the computed distance will not be returned. Default value: `null`.

**Parameter**  
---  
**Name** | **Description**  
`fieldPath` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A string value specifying the distance result field.  
**Returns**  
---  
**Type** | **Description**  
`[VectorQueryOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.VectorQueryOptions.Builder)` |   
  
### setDistanceThreshold(Double distanceThreshold)
    
    
    public VectorQueryOptions.Builder setDistanceThreshold(Double distanceThreshold)

Specifies a threshold for which no less similar documents will be returned. The behavior of the specified `distanceMeasure` will affect the meaning of the distance threshold.

  * For `distanceMeasure: "EUCLIDEAN"`, the meaning of `distanceThreshold` is: ` SELECT docs WHERE euclidean_distance <= distanceThreshold`
  * For `distanceMeasure: "COSINE"`, the meaning of `distanceThreshold` is: `SELECT docs WHERE cosine_distance <= distanceThreshold`
  * For `distanceMeasure: "DOT_PRODUCT"`, the meaning of `distanceThreshold` is: ` SELECT docs WHERE dot_product_distance >= distanceThreshold`



If `null`, then the computed distance will not be returned. Default value: `null`.

**Parameter**  
---  
**Name** | **Description**  
`distanceThreshold` | `[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)`  
A Double value specifying the distance threshold.  
**Returns**  
---  
**Type** | **Description**  
`[VectorQueryOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.VectorQueryOptions.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
