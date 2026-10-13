---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.GoogleServiceInfo
title: Network Management v1 API - Class GoogleServiceInfo (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:21.798518+00:00
---

# Network Management v1 API - Class GoogleServiceInfo (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.GoogleServiceInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Management v1 API - Class GoogleServiceInfo (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.1.0  1.0.0 
    
    
    public sealed class GoogleServiceInfo : IMessage<GoogleServiceInfo>, IEquatable<GoogleServiceInfo>, IDeepCloneable<GoogleServiceInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Management v1 API class GoogleServiceInfo.

For display only. Details of a Google Service sending packets to a VPC network. Although the source IP might be a publicly routable address, some Google Services use special routes within Google production infrastructure to reach Compute Engine Instances. <https://cloud.google.com/vpc/docs/routes#special_return_paths>

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GoogleServiceInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GoogleServiceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.GoogleServiceInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GoogleServiceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.GoogleServiceInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GoogleServiceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.GoogleServiceInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1)

## Assembly

Google.Cloud.NetworkManagement.V1.dll

## Constructors 

### GoogleServiceInfo()
    
    
    public GoogleServiceInfo()

### GoogleServiceInfo(GoogleServiceInfo)
    
    
    public GoogleServiceInfo(GoogleServiceInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GoogleServiceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.GoogleServiceInfo)`  
  
  
## Properties 

### GoogleServiceType
    
    
    public GoogleServiceInfo.Types.GoogleServiceType GoogleServiceType { get; set; }

Recognized type of a Google Service.

**Property Value**  
---  
**Type** | **Description**  
`[GoogleServiceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.GoogleServiceInfo)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.GoogleServiceInfo.Types)[GoogleServiceType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.GoogleServiceInfo.Types.GoogleServiceType)` |   
  
### SourceIp
    
    
    public string SourceIp { get; set; }

Source IP address.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
