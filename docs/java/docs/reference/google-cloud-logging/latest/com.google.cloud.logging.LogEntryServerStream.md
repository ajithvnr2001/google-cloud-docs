---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntryServerStream
title: Class LogEntryServerStream (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:15.697855+00:00
---

# Class LogEntryServerStream (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntryServerStream

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LogEntryServerStream (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public class LogEntryServerStream implements Iterable<LogEntry>

The class implements [Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html) interface over {@see LogEntry}. It wraps around [BidiStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStream.html) bi-directional gRPC stream to support iterating through ingested responses. The class uses {@see LogEntryIterator} to iterate through the processed responses. The stream should be explicitly canceled by calling {@see LogEntryServerStream#cancel()} method. The class does not provide recovery or resuming functionality over the stream.

To iterate run:
    
    
     LogEntryServerStream stream;
     // code to initialize stream
     for (LogEntry log : stream) {
       // do something with logs
     }
     stream.cancel();
     

The iteration can be blocked on waiting for another response sent in the stream.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LogEntryServerStream

## Implements

[Iterable<LogEntry>](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable<com/google/cloud/logging/LogEntry>.html)

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

### cancel()
    
    
    public void cancel()

Cleanly cancels a partially consumed stream. The associated iterator will return false for the hasNext() in the next iteration. This maintains the contract that an observed true from hasNext() will yield an item in next(), but afterwards will return false.

### convert(TailLogEntriesResponse resp)
    
    
    public List<LogEntry> convert(TailLogEntriesResponse resp)

**Parameter**  
---  
**Name** | **Description**  
`resp` | `[TailLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.TailLogEntriesResponse)`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)>` |   
  
### getInternalStream()
    
    
    public BidiStream<TailLogEntriesRequest,TailLogEntriesResponse> getInternalStream()

**Returns**  
---  
**Type** | **Description**  
`[BidiStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStream.html)<[TailLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.TailLogEntriesRequest),[TailLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.TailLogEntriesResponse)>` |   
  
### isReceiveReady()
    
    
    public boolean isReceiveReady()

Returns true if the next call to the iterator's hasNext() or next() is guaranteed to be nonblocking.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | If the call on any of the iterator's methods is guaranteed to be nonblocking.  
  
### iterator()
    
    
    public Iterator<LogEntry> iterator()

**Returns**  
---  
**Type** | **Description**  
`[Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html)<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
