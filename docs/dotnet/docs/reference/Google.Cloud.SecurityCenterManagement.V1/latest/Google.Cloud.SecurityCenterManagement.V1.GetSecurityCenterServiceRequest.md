---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest
title: Security Center Management v1 API - Class GetSecurityCenterServiceRequest (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:44.995395+00:00
---

# Security Center Management v1 API - Class GetSecurityCenterServiceRequest (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Center Management v1 API - Class GetSecurityCenterServiceRequest (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.2.0/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.1.0/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.0.0/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest)


    
    
    public sealed class GetSecurityCenterServiceRequest : IMessage<GetSecurityCenterServiceRequest>, IEquatable<GetSecurityCenterServiceRequest>, IDeepCloneable<GetSecurityCenterServiceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Security Center Management v1 API class GetSecurityCenterServiceRequest.

Request message for [SecurityCenterManagement.GetSecurityCenterService][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityCenterService].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetSecurityCenterServiceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetSecurityCenterServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetSecurityCenterServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetSecurityCenterServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenterManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1)

## Assembly

Google.Cloud.SecurityCenterManagement.V1.dll

## Constructors 

### GetSecurityCenterServiceRequest()
    
    
    public GetSecurityCenterServiceRequest()

### GetSecurityCenterServiceRequest(GetSecurityCenterServiceRequest)
    
    
    public GetSecurityCenterServiceRequest(GetSecurityCenterServiceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetSecurityCenterServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The Security Command Center service to retrieve, in one of the following formats:

  * organizations/{organization}/locations/{location}/securityCenterServices/{service}
  * folders/{folder}/locations/{location}/securityCenterServices/{service}
  * projects/{project}/locations/{location}/securityCenterServices/{service}



The following values are valid for `{service}`:

  * `container-threat-detection`
  * `event-threat-detection`
  * `security-health-analytics`
  * `vm-threat-detection`
  * `web-security-scanner`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SecurityCenterServiceName
    
    
    public SecurityCenterServiceName SecurityCenterServiceName { get; set; }

[SecurityCenterServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterServiceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest#Google_Cloud_SecurityCenterManagement_V1_GetSecurityCenterServiceRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SecurityCenterServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterServiceName)` |   
  
### ShowEligibleModulesOnly
    
    
    public bool ShowEligibleModulesOnly { get; set; }

Set to `true` to show only modules that are in scope. By default, all modules are shown.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
