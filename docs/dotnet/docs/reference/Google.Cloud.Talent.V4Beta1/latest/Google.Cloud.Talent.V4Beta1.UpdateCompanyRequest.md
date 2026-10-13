---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.UpdateCompanyRequest
title: Google Cloud Talent Solution v4beta1 API - Class UpdateCompanyRequest (3.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:43.966173+00:00
---

# Google Cloud Talent Solution v4beta1 API - Class UpdateCompanyRequest (3.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.UpdateCompanyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Talent Solution v4beta1 API - Class UpdateCompanyRequest (3.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.UpdateCompanyRequest)
  * [ 3.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/3.0.0-beta06/Google.Cloud.Talent.V4Beta1.UpdateCompanyRequest)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/2.0.0-beta07/Google.Cloud.Talent.V4Beta1.UpdateCompanyRequest)


    
    
    public sealed class UpdateCompanyRequest : IMessage<UpdateCompanyRequest>, IEquatable<UpdateCompanyRequest>, IDeepCloneable<UpdateCompanyRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Talent Solution v4beta1 API class UpdateCompanyRequest.

Request for updating a specified company.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateCompanyRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.UpdateCompanyRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.UpdateCompanyRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.UpdateCompanyRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Talent.V4Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1)

## Assembly

Google.Cloud.Talent.V4Beta1.dll

## Constructors 

### UpdateCompanyRequest()
    
    
    public UpdateCompanyRequest()

### UpdateCompanyRequest(UpdateCompanyRequest)
    
    
    public UpdateCompanyRequest(UpdateCompanyRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateCompanyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.UpdateCompanyRequest)`  
  
  
## Properties 

### Company
    
    
    public Company Company { get; set; }

Required. The company resource to replace the current resource in the system.

**Property Value**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Talent.V4Beta1/latest/Google.Cloud.Talent.V4Beta1.Company)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Strongly recommended for the best service experience.

If [update_mask][google.cloud.talent.v4beta1.UpdateCompanyRequest.update_mask] is provided, only the specified fields in [company][google.cloud.talent.v4beta1.UpdateCompanyRequest.company] are updated. Otherwise all the fields are updated.

A field mask to specify the company fields to be updated. Only top level fields of [Company][google.cloud.talent.v4beta1.Company] are supported.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
