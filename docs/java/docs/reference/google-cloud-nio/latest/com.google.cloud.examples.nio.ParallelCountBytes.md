---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-nio/latest/com.google.cloud.examples.nio.ParallelCountBytes
title: Class ParallelCountBytes (0.139.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:49.473768+00:00
---

# Class ParallelCountBytes (0.139.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-nio/latest/com.google.cloud.examples.nio.ParallelCountBytes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ParallelCountBytes (0.139.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.139.0 (latest)  0.135.0  0.134.0  0.133.0  0.131.0  0.128.13  0.127.38  0.126.19  0.125.0  0.124.21  0.123.28 
    
    
    public class ParallelCountBytes

ParallelCountBytes will read through the whole file given as input.

This example shows how to go through all the contents of a file, in order, using multithreaded NIO reads. It prints a MD5 hash and reports how long it took.

See the [ README](https://github.com/googleapis/google-cloud-java/blob/master/google-cloud-examples/README.md) for compilation instructions. Run this code with
    
    
    target/appassembler/bin/ParallelCountBytes 

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ParallelCountBytes

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

### main(String[] args)
    
    
    public static void main(String[] args)

See the class documentation.

**Parameter**  
---  
**Name** | **Description**  
`args` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[Exception](https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html)` |   
  
## Constructors 

### ParallelCountBytes()
    
    
    public ParallelCountBytes()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
