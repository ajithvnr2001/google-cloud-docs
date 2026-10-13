---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceControl.V1/latest/Google.Cloud.ServiceControl.V1.AllocateQuotaRequest
title: Service Control v1 API - Class AllocateQuotaRequest (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:41.273674+00:00
---

# Service Control v1 API - Class AllocateQuotaRequest (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceControl.V1/latest/Google.Cloud.ServiceControl.V1.AllocateQuotaRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Control v1 API - Class AllocateQuotaRequest (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.0 (latest)  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class AllocateQuotaRequest : IMessage<AllocateQuotaRequest>, IEquatable<AllocateQuotaRequest>, IDeepCloneable<AllocateQuotaRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Service Control v1 API class AllocateQuotaRequest.

Request message for the AllocateQuota method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AllocateQuotaRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AllocateQuotaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceControl.V1/latest/Google.Cloud.ServiceControl.V1.AllocateQuotaRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AllocateQuotaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceControl.V1/latest/Google.Cloud.ServiceControl.V1.AllocateQuotaRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AllocateQuotaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceControl.V1/latest/Google.Cloud.ServiceControl.V1.AllocateQuotaRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ServiceControl.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceControl.V1/latest/Google.Cloud.ServiceControl.V1)

## Assembly

Google.Cloud.ServiceControl.V1.dll

## Constructors 

### AllocateQuotaRequest()
    
    
    public AllocateQuotaRequest()

### AllocateQuotaRequest(AllocateQuotaRequest)
    
    
    public AllocateQuotaRequest(AllocateQuotaRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AllocateQuotaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceControl.V1/latest/Google.Cloud.ServiceControl.V1.AllocateQuotaRequest)`  
  
  
## Properties 

### AllocateOperation
    
    
    public QuotaOperation AllocateOperation { get; set; }

Operation that describes the quota allocation.

**Property Value**  
---  
**Type** | **Description**  
`[QuotaOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceControl.V1/latest/Google.Cloud.ServiceControl.V1.QuotaOperation)` |   
  
### ServiceConfigId
    
    
    public string ServiceConfigId { get; set; }

Specifies which version of service configuration should be used to process the request. If unspecified or no matching version can be found, the latest one will be used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceName
    
    
    public string ServiceName { get; set; }

Name of the service as specified in the service configuration. For example, `"pubsub.googleapis.com"`.

See [google.api.Service][google.api.Service] for the definition of a service name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-26 UTC."],[],[]] 
