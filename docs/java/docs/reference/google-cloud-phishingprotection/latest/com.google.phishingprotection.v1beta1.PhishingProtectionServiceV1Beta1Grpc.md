---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-phishingprotection/latest/com.google.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1Grpc
title: Class PhishingProtectionServiceV1Beta1Grpc (0.130.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:34.352471+00:00
---

# Class PhishingProtectionServiceV1Beta1Grpc (0.130.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-phishingprotection/latest/com.google.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1Grpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PhishingProtectionServiceV1Beta1Grpc (0.130.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.130.0 (latest)  0.126.0  0.125.0  0.124.0  0.122.0  0.119.0  0.118.0  0.116.0  0.114.0  0.113.0  0.111.0  0.109.0  0.107.0  0.106.0  0.105.0  0.104.0  0.103.0  0.101.0  0.99.0  0.98.0  0.95.0  0.94.0  0.93.0  0.91.0  0.90.0  0.89.0  0.88.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.6  0.33.1  0.32.11 
    
    
    public final class PhishingProtectionServiceV1Beta1Grpc

Service to report phishing URIs.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PhishingProtectionServiceV1Beta1Grpc

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

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(PhishingProtectionServiceV1Beta1Grpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(PhishingProtectionServiceV1Beta1Grpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[PhishingProtectionServiceV1Beta1Grpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-phishingprotection/latest/com.google.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1Grpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getReportPhishingMethod()
    
    
    public static MethodDescriptor<ReportPhishingRequest,ReportPhishingResponse> getReportPhishingMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ReportPhishingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-phishingprotection/latest/com.google.phishingprotection.v1beta1.ReportPhishingRequest),[ReportPhishingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-phishingprotection/latest/com.google.phishingprotection.v1beta1.ReportPhishingResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### newBlockingStub(Channel channel)
    
    
    public static PhishingProtectionServiceV1Beta1Grpc.PhishingProtectionServiceV1Beta1BlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[PhishingProtectionServiceV1Beta1Grpc.PhishingProtectionServiceV1Beta1BlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-phishingprotection/latest/com.google.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1Grpc.PhishingProtectionServiceV1Beta1BlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static PhishingProtectionServiceV1Beta1Grpc.PhishingProtectionServiceV1Beta1BlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[PhishingProtectionServiceV1Beta1Grpc.PhishingProtectionServiceV1Beta1BlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-phishingprotection/latest/com.google.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1Grpc.PhishingProtectionServiceV1Beta1BlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static PhishingProtectionServiceV1Beta1Grpc.PhishingProtectionServiceV1Beta1FutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[PhishingProtectionServiceV1Beta1Grpc.PhishingProtectionServiceV1Beta1FutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-phishingprotection/latest/com.google.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1Grpc.PhishingProtectionServiceV1Beta1FutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static PhishingProtectionServiceV1Beta1Grpc.PhishingProtectionServiceV1Beta1Stub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[PhishingProtectionServiceV1Beta1Grpc.PhishingProtectionServiceV1Beta1Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-phishingprotection/latest/com.google.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1Grpc.PhishingProtectionServiceV1Beta1Stub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
