---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.ImmutableEmptyMap
title: Class BlobInfo.ImmutableEmptyMap<K,V> (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:19.892171+00:00
---

# Class BlobInfo.ImmutableEmptyMap<K,V> (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.ImmutableEmptyMap

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BlobInfo.ImmutableEmptyMap<K,V> (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public static final class BlobInfo.ImmutableEmptyMap<K,V> extends AbstractMap<K,V>

This class is meant for internal use only. Users are discouraged from using this class.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMap](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html) > BlobInfo.ImmutableEmptyMap<K,V>

## Inherited Members

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

[AbstractMap.clear()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#clear--)

[AbstractMap.clone()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#clone--)

[AbstractMap.containsKey(Object)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#containsKey-java.lang.Object-)

[AbstractMap.containsValue(Object)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#containsValue-java.lang.Object-)

[AbstractMap.entrySet()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#entrySet--)

[AbstractMap.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#equals-java.lang.Object-)

[AbstractMap.get(Object)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#get-java.lang.Object-)

[AbstractMap.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#hashCode--)

[AbstractMap.isEmpty()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#isEmpty--)

[AbstractMap.keySet()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#keySet--)

[AbstractMap.put(K,V)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#put-K-V-)

[AbstractMap.putAll(Map<? extends K,? extends V>)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#putAll-java.util.Map<?%20extends%20K-?%20extends%20V>-)

[AbstractMap.remove(Object)](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#remove-java.lang.Object-)

[AbstractMap.size()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#size--)

[AbstractMap.toString()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#toString--)

[AbstractMap.values()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#values--)

## Type Parameters  
  
---  
**Name** | **Description**  
`K` |   
`V` |   
  
## Constructors 

### ImmutableEmptyMap()
    
    
    public ImmutableEmptyMap()

## Methods 

### entrySet()
    
    
    public Set<Map.Entry<K,V>> entrySet()

**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Entry](https://docs.oracle.com/javase/8/docs/api/java/util/Map/Entry.html)<K,V>>` |   
**Overrides**

[AbstractMap.entrySet()](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html#entrySet--)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
