---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.RecordSet.Builder
title: Class RecordSet.Builder (2.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:45.924744+00:00
---

# Class RecordSet.Builder (2.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.RecordSet.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RecordSet.Builder (2.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.97.0 (latest)  2.93.0  2.92.0  2.91.0  2.89.0  2.86.0  2.85.0  2.83.0  2.81.0  2.80.0  2.79.0  2.78.0  2.76.0  2.74.0  2.73.0  2.72.0  2.71.0  2.70.0  2.68.0  2.66.0  2.65.0  2.62.0  2.61.0  2.60.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.8  2.0.9 
    
    
    public static class RecordSet.Builder

A builder for [RecordSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.RecordSet).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RecordSet.Builder

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

### addRecord(String record)
    
    
    public RecordSet.Builder addRecord(String record)

Adds a record to the record set. The records should be as defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1). Examples of records are available in Google DNS documentation. See Also: [Google DNS documentation](https://cloud.google.com/dns/what-is-cloud-dns#supported_record_types)

**Parameter**  
---  
**Name** | **Description**  
`record` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RecordSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.RecordSet.Builder)` |   
  
### build()
    
    
    public RecordSet build()

Builds the record set.

**Returns**  
---  
**Type** | **Description**  
`[RecordSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.RecordSet)` |   
  
### clearRecords()
    
    
    public RecordSet.Builder clearRecords()

Removes all the records.

**Returns**  
---  
**Type** | **Description**  
`[RecordSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.RecordSet.Builder)` |   
  
### removeRecord(String record)
    
    
    public RecordSet.Builder removeRecord(String record)

Removes a record from the set. An exact match is required.

**Parameter**  
---  
**Name** | **Description**  
`record` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RecordSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.RecordSet.Builder)` |   
  
### setName(String name)
    
    
    public RecordSet.Builder setName(String name)

Sets the name for this record set. For example, www.example.com.

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RecordSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.RecordSet.Builder)` |   
  
### setRecords(List<String> records)
    
    
    public RecordSet.Builder setRecords(List<String> records)

Replaces the current records with the provided list of records.

**Parameter**  
---  
**Name** | **Description**  
`records` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[RecordSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.RecordSet.Builder)` |   
  
### setTtl(int duration, TimeUnit unit)
    
    
    public RecordSet.Builder setTtl(int duration, TimeUnit unit)

Sets the time that this record can be cached by resolvers. This number must be non-negative. The maximum duration must be equivalent to at most Integer#MAX_VALUE seconds.

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
A non-negative number of time units  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
The unit of the ttl parameter  
**Returns**  
---  
**Type** | **Description**  
`[RecordSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.RecordSet.Builder)` |   
  
### setType(RecordSet.Type type)
    
    
    public RecordSet.Builder setType(RecordSet.Type type)

The identifier of a supported record type, for example, A, AAAA, MX, TXT, and so on.

**Parameter**  
---  
**Name** | **Description**  
`type` | `[RecordSet.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.RecordSet.Type)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RecordSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dns/latest/com.google.cloud.dns.RecordSet.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
