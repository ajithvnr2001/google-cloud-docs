---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadAsFutureByteString
title: Class ReadAsFutureByteString (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:18.851469+00:00
---

# Class ReadAsFutureByteString (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadAsFutureByteString

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ReadAsFutureByteString (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public final class ReadAsFutureByteString extends ReadProjectionConfigs.BaseConfig<ApiFuture<ZeroCopySupport.DisposableByteString>,BaseObjectReadSessionStreamRead.AccumulatingRead<ZeroCopySupport.DisposableByteString>>

Read a range of `byte`s as an [ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)`<`DisposableByteString``

` `

> The resulting DisposableByteString MUST be close()ed to avoid leaking memory

Instances of this class are immutable and thread safe. See Also: <xref uid="com.google.cloud.storage.BlobReadSession.<Projection>readAs(com.google.cloud.storage.ReadProjectionConfig<Projection>)" data-throw-if-not-resolved="false">BlobReadSession#readAs(ReadProjectionConfig), [ReadProjectionConfigs#asFutureBytes()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs#com_google_cloud_storage_ReadProjectionConfigs_asFutureBytes__)

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ReadProjectionConfig<Projection>](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfig) > com.google.cloud.storage.ReadProjectionConfigs.BaseConfig > ReadAsFutureByteString

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

### equals(Object o)
    
    
    public boolean equals(Object o)

**Parameter**  
---  
**Name** | **Description**  
`o` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getRange()
    
    
    public RangeSpec getRange()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

The [RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec) to be used for any read using this instance.

_Default:_ [RangeSpec#all()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec#com_google_cloud_storage_RangeSpec_all__)

**Returns**  
---  
**Type** | **Description**  
`[RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

### withRangeSpec(RangeSpec range)
    
    
    public ReadAsFutureByteString withRangeSpec(RangeSpec range)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Return an instance with the [RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec) set to the specified value.

_Default:_ [RangeSpec#all()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec#com_google_cloud_storage_RangeSpec_all__) See Also: [#getRange()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadAsFutureByteString#com_google_cloud_storage_ReadAsFutureByteString_getRange__)

**Parameter**  
---  
**Name** | **Description**  
`range` | `[RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec)`  
The [RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec) to be used for any read using the returned instance. Must be non-null.  
**Returns**  
---  
**Type** | **Description**  
`[ReadAsFutureByteString](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadAsFutureByteString)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
