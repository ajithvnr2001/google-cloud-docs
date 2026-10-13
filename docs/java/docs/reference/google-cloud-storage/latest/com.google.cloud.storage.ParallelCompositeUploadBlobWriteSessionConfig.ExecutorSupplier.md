---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier
title: Class ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:39.982231+00:00
---

# Class ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public abstract static class ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier extends ParallelCompositeUploadBlobWriteSessionConfig.Factory<Executor> implements Serializable

Class which will be used to supply an Executor where work will be submitted when performing a parallel composite upload. See Also: #withExecutorSupplier(ExecutorSupplier)

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.cloud.storage.ParallelCompositeUploadBlobWriteSessionConfig.Factory > ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

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

### cachedPool()
    
    
    public static ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier cachedPool()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Create a cached thread pool for submitting work See Also: #withExecutorSupplier(ExecutorSupplier)

**Returns**  
---  
**Type** | **Description**  
`[ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier)` |   
  
### fixedPool(int poolSize)
    
    
    public static ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier fixedPool(int poolSize)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Create a fixed size thread pool for submitting work See Also: #withExecutorSupplier(ExecutorSupplier)

**Parameter**  
---  
**Name** | **Description**  
`poolSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the number of threads in the pool  
**Returns**  
---  
**Type** | **Description**  
`[ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier)` |   
  
### useExecutor(Executor executor)
    
    
    public static ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier useExecutor(Executor executor)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Wrap an existing executor instance which will be used for submitting work

**_Choosing to use this supplier type will make your instance of[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions) unable to be serialized._** See Also: #withExecutorSupplier(ExecutorSupplier)

**Parameter**  
---  
**Name** | **Description**  
`executor` | `[Executor](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html)`  
the executor to use  
**Returns**  
---  
**Type** | **Description**  
`[ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
